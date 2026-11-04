"""Khai báo: bảng nào nằm ở đâu trong Excel -> nằm ở file .md nào.

kind="table": một vùng bảng (header + các dòng, ví dụ cột A..Q)
kind="kv"   : danh sách "nhãn -> một ô" (dùng cho các ô tổng / kiểm tra lẻ)

editable=True  : bảng có ô NHẬP (ô hằng số). Bạn sửa trong .md, script ghi vào Excel.
                 Ô có công thức luôn bị bỏ qua khi ghi và được tính lại.
editable=False : bảng chỉ để xem (toàn công thức), luôn bị ghi đè khi build.
skip_blank=True: bỏ các dòng trống (chỉ dùng cho bảng chỉ-xem).
"""

TEMPLATE = "model/Midterm_-_Excel.xlsx"
DOCS_DIR = "docs/fl"

# Thứ tự file .md (tên file = tên sheet + ".md")
SHEETS = ["Parameters", "W0_Scope", "W1_FunctionList", "W2_Costing",
          "W2_Rollup", "W3_CrossReview", "W4_Prioritization", "W5_Handover"]

# Nội dung tự do thêm vào cuối file khi export lần đầu (script KHÔNG đụng vào sau đó)
EXTRA_MD = {
    "W2_Rollup": "## Three observations the team carries into W4\n\n1. \n2. \n3. \n",
}


def T(sheet, id, title, **kw):
    return dict(sheet=sheet, id=id, title=title, kind=kw.pop("kind", "table"), **kw)


TABLES = [
    # ---------------- Parameters ----------------
    T("Parameters", "sizes", "1. Effort size to base hours", header=8, rows=[(9, 11)], cols="A-D", editable=True),
    T("Parameters", "layers", "2. Technical layer to AI leverage and default seniority", header=14, rows=[(15, 17)], cols="A-D", editable=True),
    T("Parameters", "rates", "3. Hourly cost by seniority band (VND / hour)", header=20, rows=[(21, 23)], cols="A-D", editable=True),
    T("Parameters", "verification", "4. Verification factor", header=26, rows=[(27, 28)], cols="A-D", editable=True),
    T("Parameters", "fp_weights", "5. Function point weights", header=31, rows=[(32, 38)], cols="A-D", editable=True),
    T("Parameters", "capacity", "6. Team capacity for DBIZ3", kind="kv", editable=True,
      items=["B42", "B43", "B44", "B45"]),
    T("Parameters", "thresholds", "7. Thresholds", kind="kv", editable=True,
      items=["B48", "B49", "B50", "B51", "B52", "B53", "B54"]),
    T("Parameters", "basis", "9. Estimation basis (Bottom-up | Function-point)", kind="kv", editable=True,
      items=["B63"]),

    # ---------------- W0 ----------------
    T("W0_Scope", "uc", "Table 1 · Use case inventory", header=9, rows=[(10, 29)], cols="A-D", editable=True),
    T("W0_Scope", "uc_check", "Table 1 · checks", kind="kv", editable=False,
      items=[("Use cases listed", "B30"), ("Assignment check", "C30")]),
    T("W0_Scope", "features", "Table 2 · Feature list (flows into W1)", header=33, rows=[(34, 45)], cols="A-F", editable=True),
    T("W0_Scope", "features_check", "Table 2 · checks", kind="kv", editable=False,
      items=[("Feature count", "B46"), ("Feature count check", "C46")]),
    T("W0_Scope", "wont", "Table 3 · Won't-have", header=49, rows=[(50, 59)], cols="A-C", editable=True),
    T("W0_Scope", "data_fn", "Table 4 · Data functions (ILF / EIF)", header=62, rows=[(63, 76)], cols="A-D", editable=True),
    T("W0_Scope", "data_fn_total", "Table 4 · total", kind="kv", editable=False,
      items=[("Total data-function points", "D77")]),

    # ---------------- W1 ----------------
    T("W1_FunctionList", "main", "Function list (L2 / L3)", header=9, rows=[(10, 129)], cols="A-Q", editable=True),
    T("W1_FunctionList", "totals", "Totals and integrity", kind="kv", editable=False,
      items=[("L2 / L3 count", "C130"), ("Total base hours", "L130"),
             ("Total transactional FP", "Q130"), ("Integrity", "C131")]),

    # ---------------- W2_Costing ----------------
    T("W2_Costing", "l3", "Cost per L3 work item", header=8, rows=[(9, 129)], cols="A-N", editable=False, skip_blank=True),
    T("W2_Costing", "l2", "Cost per L2 function", header=132, rows=[(133, 172)], cols="A-H", editable=False, skip_blank=True),
    T("W2_Costing", "fp_check", "Function-point cross-check", headers=["Item", "Value", "Note"],
      rows=[(175, 185)], cols="A-C", editable=False, skip_blank=True, notes=["A186"]),

    # ---------------- W2_Rollup ----------------
    T("W2_Rollup", "features", "Per feature (effective priority, after W4)", header=8, rows=[(9, 21)], cols="A-O",
      editable=False, skip_blank=True, notes=["A22"]),
    T("W2_Rollup", "headline", "The three headline figures", header=25, rows=[(26, 28)], cols="A-E", editable=False),
    T("W2_Rollup", "thresholds", "Threshold check", header=31, rows=[(32, 37)], cols="A-E", editable=False),

    # ---------------- W3 ----------------
    T("W3_CrossReview", "teams", "Teams", kind="kv", editable=True,
      items=[("Owning team", "B9"), ("Reviewing team", "D9")]),
    T("W3_CrossReview", "checklist", "Checklist - eight quality criteria", header=12, rows=[(13, 20)], cols="A-H", editable=True),
    T("W3_CrossReview", "defects", "Defect log", header=23, rows=[(24, 38)], cols="A-H", editable=True),

    # ---------------- W4 ----------------
    T("W4_Prioritization", "rules", "Decision rules", header=10, rows=[(11, 14)], cols="A-E", editable=True),
    T("W4_Prioritization", "main", "Priority table", header=18, rows=[(19, 58)], cols="A-K", editable=True),
    T("W4_Prioritization", "control", "Control panel", header=61, rows=[(62, 65)], cols="A-D", editable=False),

    # ---------------- W5 ----------------
    T("W5_Handover", "scenarios", "1. Three scenarios", header=8, rows=[(9, 11)], cols="A-D", editable=True, notes=["A12"]),
    T("W5_Handover", "assumptions", "2. Assumptions", header=15, rows=[(16, 23)], cols="A-C", editable=True),
    T("W5_Handover", "tasks", "3. tasks.md seed", header=26, rows=[(27, 146)], cols="A-E",
      editable=False, skip_blank=True, notes=["A147"]),
    T("W5_Handover", "questions", "4. Open questions", header=150, rows=[(151, 160)], cols="A-E", editable=True),
]
