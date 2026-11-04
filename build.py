#!/usr/bin/env python3
"""Excel làm "máy tính", Markdown làm nơi sửa + hiển thị.

  python build.py export [--force]   # tạo docs/*.md từ file Excel (chạy 1 lần để khởi tạo)
  python build.py sync               # đọc ô nhập trong docs/*.md -> ghi vào Excel -> tính lại
                                     # bằng LibreOffice -> ghi lại mọi bảng trong docs/*.md
"""
import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from openpyxl import load_workbook
from openpyxl.cell.cell import MergedCell
from openpyxl.utils import column_index_from_string as col_idx
from openpyxl.utils import get_column_letter as col_letter
from openpyxl.worksheet.formula import ArrayFormula

from tables import DOCS_DIR, EXTRA_MD, SHEETS, TABLES, TEMPLATE

ROOT = Path(__file__).parent
BUILD = ROOT / "build"
ERRORS = ("#REF!", "#NAME?", "#VALUE!", "#DIV/0!", "#N/A", "#NUM!", "#NULL!")


# ------------------------------------------------------------------ helpers
def is_formula(v):
    return isinstance(v, ArrayFormula) or (isinstance(v, str) and v.startswith("="))


def fmt_computed(v, number_format=""):
    if v is None:
        return ""
    if isinstance(v, bool):
        return "TRUE" if v else "FALSE"
    if isinstance(v, (int, float)):
        if "%" in number_format:
            return f"{v * 100:.1f}%"
        if abs(v) >= 1000:
            return f"{v:,.0f}"
        s = f"{v:.4f}".rstrip("0").rstrip(".")
        return s if s not in ("", "-0") else "0"
    return str(v)


def raw_text(v):
    """Ô hằng số -> chuỗi hiển thị (giá trị thật, không định dạng)."""
    if v is None:
        return ""
    if isinstance(v, bool):
        return "TRUE" if v else "FALSE"
    if isinstance(v, (int, float)):
        s = f"{v:.10g}"
        return repr(v) if "e" in s else s
    return str(v)


def esc(s):
    return s.replace("\r", "").replace("|", "\\|").replace("\n", "<br>")


def unesc(s):
    return s.replace("\\|", "|").replace("<br>", "\n").strip()


def parse_input(s):
    """Chuỗi trong md -> giá trị ghi vào Excel."""
    if s == "":
        return None
    if re.fullmatch(r"-?\d+(\.\d+)?", s):
        f = float(s)
        return int(f) if f.is_integer() and "." not in s else f
    if re.fullmatch(r"-?\d{1,3}(,\d{3})+(\.\d+)?", s):
        return float(s.replace(",", ""))
    if re.fullmatch(r"-?\d+(\.\d+)?%", s):
        return float(s[:-1]) / 100
    return s


def expand_rows(spec):
    out = []
    for r in spec:
        out.extend(range(r[0], r[1] + 1) if isinstance(r, tuple) else [r])
    return out


def col_range(s):
    a, b = s.split("-")
    return list(range(col_idx(a), col_idx(b) + 1))


def cell_text(wst, wsv, r, c):
    tv = wst.cell(r, c).value
    if is_formula(tv):
        return fmt_computed(wsv.cell(r, c).value, wst.cell(r, c).number_format)
    return raw_text(tv)


def kv_items(spec, wst):
    out = []
    for it in spec["items"]:
        if isinstance(it, tuple):
            label, ref = it
        else:
            ref = it
            row = wst[ref].row
            label = str(wst.cell(row, 1).value or ref)
        out.append((label, ref))
    return out


# ------------------------------------------------------------------ render
def render_table(spec, wst, wsv):
    """-> (marker_note, [markdown lines])"""
    if spec["kind"] == "kv":
        items = kv_items(spec, wst)
        headers = ["Item", "Value"]
        rows = [[esc(l), esc(cell_text(wst, wsv, wst[ref].row, wst[ref].column))] for l, ref in items]
        formula_cols = []
    else:
        cols = col_range(spec["cols"])
        rows_n = expand_rows(spec["rows"])
        if "headers" in spec:
            headers = spec["headers"]
        else:
            headers = [raw_text(wst.cell(spec["header"], c).value) for c in cols]
        # dòng "trống" = mọi ô rỗng; ô CÔNG THỨC trả về 0 cũng tính là rỗng
        # (ví dụ cột FP value ở các dòng chưa dùng)
        def blank(r):
            for c in cols:
                t = cell_text(wst, wsv, r, c)
                if t == "" or (t == "0" and is_formula(wst.cell(r, c).value)):
                    continue
                return False
            return True

        keep = [r for r in rows_n if not blank(r)]
        if not spec.get("skip_blank"):          # bảng nhập: chỉ cắt các dòng trống Ở CUỐI
            last = max(keep) if keep else rows_n[0] - 1
            keep = [r for r in rows_n if r <= last]
        rows = [[esc(cell_text(wst, wsv, r, c)) for c in cols] for r in keep]
        # cột "tính toán" = cột mà đa số ô là công thức
        formula_cols = []
        for c in cols:
            n = sum(is_formula(wst.cell(r, c).value) for r in rows_n)
            if n and n >= len(rows_n) / 2:
                formula_cols.append(col_letter(c))

    if not spec["editable"]:
        note = "derived - auto-generated, do not edit"
    elif formula_cols:
        note = f"input table - computed columns (do not edit): {', '.join(formula_cols)}"
    else:
        note = "input table"
    lines = ["| " + " | ".join(esc(h) for h in headers) + " |",
             "|" + "|".join("---" for _ in headers) + "|"]
    lines += ["| " + " | ".join(r) + " |" for r in rows]
    return note, lines


def block_re(tid):
    return re.compile(rf"<!-- BEGIN:{re.escape(tid)}\b[^\n]*-->\n(.*?)<!-- END:{re.escape(tid)} -->", re.S)


def make_block(spec, wst, wsv):
    note, lines = render_table(spec, wst, wsv)
    out = [f"<!-- BEGIN:{spec['id']} | {note} -->", *lines, f"<!-- END:{spec['id']} -->"]
    return "\n".join(out)


def parse_block(text, tid):
    m = block_re(tid).search(text)
    if not m:
        return None
    rows = []
    for ln in m.group(1).splitlines()[2:]:  # bỏ header + dòng ---
        ln = ln.strip()
        if not ln.startswith("|"):
            continue
        parts = re.split(r"(?<!\\)\|", ln)[1:-1]
        rows.append([unesc(p) for p in parts])
    return rows


# ------------------------------------------------------------------ export
def intro_lines(ws, first_header):
    out = []
    for r in range(2, min(first_header, 9)):
        a, b = ws.cell(r, 1).value, ws.cell(r, 2).value
        if isinstance(a, str) and a.isupper() and isinstance(b, str):
            body = b.strip().split("\n")
            out.append(f"> **{a.title()}**: " + body[0])
            out += [f">  {x}" for x in body[1:]]
            out.append(">")
    return out[:-1] if out else out


def build_md(sheet, wst, wsv):
    specs = [t for t in TABLES if t["sheet"] == sheet]
    first_header = min(t.get("header", 99) for t in specs)
    md = [f"# {wst['A1'].value}", ""]
    il = intro_lines(wst, first_header)
    if il:
        md += il + [""]
    md += ["<!-- Chỉ sửa trong các bảng 'input'. Phần giữa BEGIN/END sẽ được build.py ghi lại. -->", ""]
    for s in specs:
        md += [f"## {s['title']}", "", make_block(s, wst, wsv), ""]
        for ref in s.get("notes", []):
            md += [f"_{wst[ref].value}_", ""]
    if sheet in EXTRA_MD:
        md += [EXTRA_MD[sheet]]
    return "\n".join(md).rstrip() + "\n"


def cmd_export(force):
    docs = ROOT / DOCS_DIR
    existing = [p for p in docs.glob("*.md")] if docs.exists() else []
    if existing and not force:
        sys.exit("docs/ đã có file .md. Chạy lại với --force nếu muốn GHI ĐÈ (sẽ mất dữ liệu bạn đã sửa trong md).")
    docs.mkdir(exist_ok=True)
    wst = load_workbook(ROOT / TEMPLATE)
    wsv = load_workbook(ROOT / TEMPLATE, data_only=True)
    for sh in SHEETS:
        (docs / f"{sh}.md").write_text(build_md(sh, wst[sh], wsv[sh]), encoding="utf-8")
        print("wrote", f"{DOCS_DIR}/{sh}.md")


# ------------------------------------------------------------------ sync
def find_soffice():
    p = shutil.which("soffice") or shutil.which("libreoffice")
    if not p:
        sys.exit("Không tìm thấy LibreOffice (soffice). Cài: sudo apt-get install -y libreoffice-calc")
    return p


def recalc(src: Path, outdir: Path) -> Path:
    outdir.mkdir(parents=True, exist_ok=True)
    profile = Path(tempfile.mkdtemp()) / "profile"
    cmd = [find_soffice(), "--headless", "--norestore", "--nolockcheck",
           f"-env:UserInstallation={profile.as_uri()}",
           "--convert-to", "xlsx", "--outdir", str(outdir), str(src)]
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    out = outdir / src.name
    if r.returncode != 0 or not out.exists():
        sys.exit(f"LibreOffice lỗi:\n{r.stdout}\n{r.stderr}")
    return out


def apply_inputs(wb, md_texts):
    """Ghi các ô nhập từ md vào workbook (bỏ qua ô công thức). Trả về danh sách thay đổi."""
    changes, problems = [], []
    for spec in TABLES:
        if not spec["editable"]:
            continue
        text = md_texts.get(spec["sheet"])
        rows = parse_block(text, spec["id"]) if text else None
        if rows is None:
            problems.append(f"thiếu khối {spec['id']} trong {spec['sheet']}.md - bỏ qua")
            continue
        ws = wb[spec["sheet"]]

        if spec["kind"] == "kv":
            items = kv_items(spec, ws)
            for (label, ref), row in zip(items, rows):
                new = row[1] if len(row) > 1 else ""
                changes += _write(ws, ws[ref], new, f"{spec['sheet']}!{ref}")
            continue

        cols = col_range(spec["cols"])
        rows_n = expand_rows(spec["rows"])
        if len(rows) > len(rows_n):
            sys.exit(f"{spec['sheet']}.md / {spec['id']}: {len(rows)} dòng, nhưng Excel chỉ có chỗ cho {len(rows_n)} dòng.")
        for i, r in enumerate(rows_n):
            md_row = rows[i] if i < len(rows) else None
            for j, c in enumerate(cols):
                cell = ws.cell(r, c)
                new = (md_row[j] if md_row and j < len(md_row) else "")
                changes += _write(ws, cell, new, f"{spec['sheet']}!{cell.coordinate}")
    return changes, problems


def _write(ws, cell, new_text, where):
    if isinstance(cell, MergedCell) or is_formula(cell.value):
        return []
    if raw_text(cell.value).strip() == new_text:
        return []
    old = cell.value
    cell.value = parse_input(new_text)
    return [(where, old, cell.value)]


def cmd_sync():
    docs = ROOT / DOCS_DIR
    md_texts = {sh: (docs / f"{sh}.md").read_text(encoding="utf-8")
                for sh in SHEETS if (docs / f"{sh}.md").exists()}
    if not md_texts:
        sys.exit("Chưa có docs/*.md. Chạy: python build.py export")

    # 1) ghi ô nhập vào bản sao của Excel
    wb = load_workbook(ROOT / TEMPLATE)
    changes, problems = apply_inputs(wb, md_texts)
    BUILD.mkdir(exist_ok=True)
    stage = BUILD / "stage"
    stage.mkdir(exist_ok=True)
    src = stage / Path(TEMPLATE).name
    wb.save(src)

    # 2) tính lại bằng LibreOffice
    out = recalc(src, BUILD / "recalculated")

    # 3) đọc kết quả, viết lại mọi khối bảng trong md
    wst = load_workbook(src)                      # công thức + ô nhập ĐÃ áp dụng chỉnh sửa từ md
    wsv = load_workbook(out, data_only=True)      # giá trị vừa tính
    bad = []
    for sh in md_texts:
        text = md_texts[sh]
        for spec in [t for t in TABLES if t["sheet"] == sh]:
            if not block_re(spec["id"]).search(text):
                continue
            new_block = make_block(spec, wst[sh], wsv[sh])
            text = block_re(spec["id"]).sub(lambda m: new_block, text, count=1)
            if any(e in new_block for e in ERRORS):
                bad.append(f"{sh} / {spec['id']}")
        if text != md_texts[sh]:
            (docs / f"{sh}.md").write_text(text, encoding="utf-8")
            print("updated", f"{DOCS_DIR}/{sh}.md")

    print(f"\n{len(changes)} ô nhập thay đổi so với Excel gốc:")
    for w, o, n in changes[:40]:
        print(f"  {w}: {o!r} -> {n!r}")
    if len(changes) > 40:
        print(f"  ... và {len(changes) - 40} ô nữa")
    for p in problems:
        print("CẢNH BÁO:", p)
    if bad:
        print("CẢNH BÁO: có lỗi công thức (#REF!, #NAME?...) trong:", ", ".join(bad))
        sys.exit(1)


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    e = sp.add_parser("export")
    e.add_argument("--force", action="store_true")
    sp.add_parser("sync")
    a = ap.parse_args()
    cmd_export(a.force) if a.cmd == "export" else cmd_sync()


if __name__ == "__main__":
    main()
