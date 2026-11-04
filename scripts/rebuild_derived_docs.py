#!/usr/bin/env python3
"""Rebuild LabDesk's derived Markdown tables from W0/W1/W4 source data.

Manual inputs:
- W1 L2/L3 rows (scope, estimates, EARS precision)
- W4 Effective priority and justification
- Class parameters kept below and assumptions in W5/W6

Generated outputs:
- W4 Person-hours and Cost columns
- W2 costing, roll-ups, scenarios and threshold checks
- W5 scenarios, contingency and Must-only task seed
- W6 cash-flow tables and investment metrics

The script intentionally fails on missing IDs or unexpected table structures rather
than silently producing incomplete or misleading project numbers.
"""
from __future__ import annotations

import math
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

W0 = ROOT / "docs/function-list/w0-scope.md"
W1 = ROOT / "docs/function-list/w1-function-list.md"
W2 = ROOT / "docs/function-list/w2-cost.md"
W4 = ROOT / "docs/function-list/w4-priorities.md"
W5 = ROOT / "docs/function-list/w5-handover.md"
W6 = ROOT / "docs/function-list/w6-cash-flow.md"

# Class Parameters referenced by the existing W2/W5 documentation.
AI_LEVERAGE = {"FE": 0.35, "BE": 0.70, "INT": 1.00}
VERIFICATION_FACTOR = {"Yes": 0.15, "No": 0.40}
HOURLY_RATE = {"Junior": 200_000, "Senior": 300_000}
LAYER_BAND = {"FE": "Junior", "BE": "Senior", "INT": "Senior"}


def read(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"Required source file is missing: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def write_if_changed(path: Path, content: str) -> None:
    if read(path) != content:
        path.write_text(content, encoding="utf-8")
        print(f"Updated {path.relative_to(ROOT)}")
    else:
        print(f"No change: {path.relative_to(ROOT)}")


def cells(line: str) -> list[str]:
    return [part.strip() for part in line.strip().strip("|").split("|")]


def is_table_line(line: str) -> bool:
    return line.strip().startswith("|") and line.strip().endswith("|")


def find_tables(document: str, after_heading: str | None = None) -> list[tuple[int, int, list[str], list[list[str]]]]:
    lines = document.splitlines()
    start_at = 0
    if after_heading:
        try:
            start_at = next(i for i, line in enumerate(lines) if line.strip().startswith(after_heading)) + 1
        except StopIteration as exc:
            raise ValueError(f"Heading not found: {after_heading}") from exc

    found = []
    i = start_at
    while i < len(lines):
        if not is_table_line(lines[i]):
            i += 1
            continue
        begin = i
        while i < len(lines) and is_table_line(lines[i]):
            i += 1
        raw = [cells(line) for line in lines[begin:i]]
        if len(raw) >= 2:
            header = raw[0]
            body = [row for row in raw[2:] if not all(re.fullmatch(r":?-{3,}:?", c or "-") for c in row)]
            found.append((begin, i, header, body))
    return found


def table_by_header(document: str, token: str, after_heading: str | None = None):
    for table in find_tables(document, after_heading):
        if any(token.lower() in h.lower() for h in table[2]):
            return table
    raise ValueError(f"Markdown table with header containing {token!r} not found")


def row_dict(header: list[str], row: list[str]) -> dict[str, str]:
    if len(header) != len(row):
        raise ValueError(f"Table row has {len(row)} cells; expected {len(header)}: {row}")
    return dict(zip(header, row))


def parse_num(value: str) -> float:
    value = value.strip().replace("**", "").replace(",", "")
    value = value.replace("VND", "").replace("h", "").replace("%", "").strip()
    if not value:
        return 0.0
    if re.fullmatch(r"-?\d{1,3}(?:\.\d{3})+", value):
        value = value.replace(".", "")
    return float(value)


def parse_money(value: str) -> int:
    return int(round(parse_num(value)))


def fmt1(value: float) -> str:
    return f"{value:.1f}"


def fmt_pct(value: float) -> str:
    return f"{value:.1f}%"


def fmt_money(value: float | int) -> str:
    return f"{int(round(value)):,}".replace(",", ".")


def fmt_signed_money(value: float | int) -> str:
    rounded = int(round(value))
    return ("-" if rounded < 0 else "") + fmt_money(abs(rounded))


def render_table(header: list[str], rows: list[list[object]]) -> str:
    def clean(value: object) -> str:
        return str(value).replace("|", r"\|").replace("\n", " ").strip()
    lines = ["| " + " | ".join(clean(x) for x in header) + " |",
             "| " + " | ".join("---" for _ in header) + " |"]
    lines.extend("| " + " | ".join(clean(x) for x in row) + " |" for row in rows)
    return "\n".join(lines)


def replace_table(document: str, token: str, replacement: str, after_heading: str | None = None) -> str:
    begin, end, _, _ = table_by_header(document, token, after_heading)
    lines = document.splitlines()
    lines[begin:end] = replacement.splitlines()
    return "\n".join(lines) + ("\n" if document.endswith("\n") else "")


def parse_percent(text: str, label: str) -> float:
    match = re.search(re.escape(label) + r".*?(\d+(?:\.\d+)?)\s*%", text, re.I)
    if not match:
        raise ValueError(f"Could not read percentage for {label!r}")
    return float(match.group(1)) / 100.0


def numbers_in(text: str) -> list[float]:
    matches = re.findall(r"(?<![A-Za-z])\d{1,3}(?:\.\d{3})+(?!\d)|(?<![A-Za-z])\d+(?:\.\d+)?", text)
    return [parse_num(x) for x in matches]


def update_assumption_value(document: str, assumption: str, value: str) -> str:
    begin, end, header, rows = table_by_header(document, "Source", "## 2. Assumptions")
    updated = []
    changed = False
    for row in rows:
        item = row_dict(header, row)
        if item.get("Assumption", "").strip() == assumption:
            item["Value"] = value
            changed = True
        updated.append([item[h] for h in header])
    if not changed:
        raise ValueError(f"Assumption row not found: {assumption}")
    return replace_table(document, "Source", render_table(header, updated), "## 2. Assumptions")


def irr(cashflows: list[float]) -> float | None:
    def npv(rate: float) -> float:
        return sum(cf / ((1.0 + rate) ** year) for year, cf in enumerate(cashflows))
    low, high = -0.9999, 10.0
    if npv(low) * npv(high) > 0:
        return None
    for _ in range(250):
        mid = (low + high) / 2
        value = npv(mid)
        if abs(value) < 1e-7:
            return mid
        if npv(low) * value > 0:
            low = mid
        else:
            high = mid
    return (low + high) / 2


def payback(cashflows: list[float]) -> float | None:
    cumulative = cashflows[0]
    for year in range(1, len(cashflows)):
        previous = cumulative
        cumulative += cashflows[year]
        if cumulative >= 0 and cashflows[year] > 0:
            return (year - 1) + (-previous / cashflows[year])
    return None


def main() -> None:
    w0, w1, w2, w4, w5, w6 = map(read, (W0, W1, W2, W4, W5, W6))

    # Parse the source Feature list and W1 L2/L3 tables.
    _, _, feature_header, feature_rows = table_by_header(w0, "Feature ID", "## Table 2.")
    feature_names = {
        row_dict(feature_header, row)["Feature ID"]: row_dict(feature_header, row)["Feature name (business noun)"]
        for row in feature_rows
    }

    _, _, l2_header, l2_rows = table_by_header(w1, "L2 ID", "## L2 functions")
    l2_items = [row_dict(l2_header, row) for row in l2_rows]
    l2_to_feature = {row["L2 ID"]: row["Feature"] for row in l2_items}
    l2_names = {row["L2 ID"]: row["L2 function name"] for row in l2_items}
    l2_initial = {row["L2 ID"]: row["Initial priority"] for row in l2_items}

    _, _, l3_header, l3_rows = table_by_header(w1, "L3 ID", "## L3 work items")
    l3_items = [row_dict(l3_header, row) for row in l3_rows]

    # W5 Class Parameters are the editable source of estimation rates and factors.
    _, _, w5_assumption_header, w5_assumption_rows = table_by_header(w5, "Source", "## 2. Assumptions")
    w5_assumptions = {row_dict(w5_assumption_header, row)["Assumption"]: row_dict(w5_assumption_header, row)["Value"]
                      for row in w5_assumption_rows}
    rate_values = numbers_in(w5_assumptions["Junior / Senior / Expert rate"])
    ai_values = numbers_in(w5_assumptions["AI leverage FE / BE / INT"])
    verification_values = numbers_in(w5_assumptions["Verification factor precise / vague"])
    if len(rate_values) < 2 or len(ai_values) < 3 or len(verification_values) < 2:
        raise ValueError("W5 rate, AI leverage or verification-factor parameters are incomplete")
    HOURLY_RATE = {"Junior": rate_values[0], "Senior": rate_values[1]}
    AI_LEVERAGE = dict(zip(("FE", "BE", "INT"), ai_values[:3]))
    VERIFICATION_FACTOR = {"Yes": verification_values[0], "No": verification_values[1]}

    # W4 Effective priority and justification are manual inputs; derived effort/cost are outputs.
    _, _, w4_header, w4_rows = table_by_header(w4, "Effective priority")
    w4_items = [row_dict(w4_header, row) for row in w4_rows]
    priority_by_l2 = {row["L2 ID"]: row["Effective priority"] for row in w4_items}
    justification_by_l2 = {row["L2 ID"]: row.get("Justification (required if changed)", "") for row in w4_items}

    missing_priorities = sorted(set(l2_to_feature) - set(priority_by_l2))
    if missing_priorities:
        raise ValueError("Add these new L2 IDs to W4 and set their Effective priority before syncing: " + ", ".join(missing_priorities))
    unknown_priorities = sorted({p for p in priority_by_l2.values() if p not in {"Must", "Should", "Could", "Won't"}})
    if unknown_priorities:
        raise ValueError("Unsupported W4 Effective priority value(s): " + ", ".join(unknown_priorities))

    # Calculate each L3 work item from W1 plus its L2 effective priority from W4.
    work = []
    by_l2 = defaultdict(list)
    for row in l3_items:
        l3_id = row["L3 ID"]
        l2_id = row["L2 ID"]
        if l2_id not in l2_to_feature:
            raise ValueError(f"{l3_id} refers to unknown L2 ID {l2_id}")
        layer = row["Layer"]
        if layer not in AI_LEVERAGE or layer not in LAYER_BAND:
            raise ValueError(f"Unsupported layer {layer!r} in {l3_id}")
        precision = row["EARS precise?"]
        if precision not in VERIFICATION_FACTOR:
            raise ValueError(f"EARS precise? must be Yes/No for {l3_id}, got {precision!r}")
        base = parse_num(row["Base hours"])
        if base <= 0:
            raise ValueError(f"Base hours must be positive for {l3_id}")
        ai_hours = base * AI_LEVERAGE[layer]
        verification_hours = base * VERIFICATION_FACTOR[precision]
        person_hours = ai_hours + verification_hours
        band = LAYER_BAND[layer]
        cost = round(person_hours * HOURLY_RATE[band])
        item = {
            "l3_id": l3_id, "l2_id": l2_id, "feature": l2_to_feature[l2_id],
            "layer": layer, "base": base, "ai": ai_hours, "verification": verification_hours,
            "hours": person_hours, "band": band, "cost": cost,
            "priority": priority_by_l2[l2_id], "hidden": row["Hidden work?"].lower() == "yes",
        }
        work.append(item)
        by_l2[l2_id].append(item)

    # Update W4's derived Person-hours and Cost columns, preserving priority and justification.
    w4_output = []
    w4_totals = {}
    for row in w4_items:
        l2_id = row["L2 ID"]
        total_hours = sum(x["hours"] for x in by_l2[l2_id])
        total_cost = sum(x["cost"] for x in by_l2[l2_id])
        row["Person-hours"] = fmt1(total_hours)
        row["Cost (VND)"] = fmt_money(total_cost)
        w4_totals[l2_id] = (total_hours, total_cost)
        w4_output.append([row[h] for h in w4_header])
    w4 = replace_table(w4, "Effective priority", render_table(w4_header, w4_output))

    # Preserve the manually maintained transactional-FP cross-check per feature.
    _, _, old_rollup_header, old_rollup_rows = table_by_header(w2, "In-scope cost")
    fp_by_feature = {}
    total_fp_text = None
    for row in old_rollup_rows:
        item = row_dict(old_rollup_header, row)
        feature = item["Feature"].replace("**", "")
        if feature == "Project":
            total_fp_text = item["Transactional FP"]
        else:
            fp_by_feature[feature] = item["Transactional FP"]
    if total_fp_text is None:
        raise ValueError("Could not find the Project transactional-FP total in W2")
    missing_fp = sorted(set(feature_names) - set(fp_by_feature))
    if missing_fp:
        raise ValueError("New feature(s) need a manually confirmed Transactional FP cross-check in W2 before automation: " + ", ".join(missing_fp))
    total_fp = parse_num(total_fp_text)

    # W2: detailed L3 costing.
    cost_header = ["L3 ID", "Feature", "Layer", "Base h", "AI-adj. h", "Verif. h",
                   "Person-hours", "Band", "Cost (VND)", "Effective priority"]
    cost_rows = [[x["l3_id"], x["feature"], x["layer"], fmt1(x["base"]), fmt1(x["ai"]),
                  fmt1(x["verification"]), fmt1(x["hours"]), x["band"], fmt_money(x["cost"]),
                  x["priority"]] for x in work]
    w2 = replace_table(w2, "L3 ID", render_table(cost_header, cost_rows), "## Cost per L3 work item")

    # W2: roll-up per feature and project.
    grouped = defaultdict(list)
    for item in work:
        grouped[item["feature"]].append(item)
    rollup_header = ["Feature", "Name", "L2", "L3", "Base h", "Must p-h", "Should p-h", "Could p-h",
                     "In-scope p-h", "In-scope cost (VND)", "Must share", "Transactional FP", "Base h per FP"]
    rollup_rows = []
    totals = defaultdict(float)
    for feature in feature_names:
        items = grouped[feature]
        base_hours = sum(x["base"] for x in items)
        l2_ids = {x["l2_id"] for x in items}
        # Count all L2 functions in the feature, including any with no L3 rows.
        feature_l2 = [x for x in l2_items if x["Feature"] == feature]
        hours_by_priority = {p: sum(x["hours"] for x in items if x["priority"] == p) for p in ("Must", "Should", "Could")}
        cost_in_scope = sum(x["cost"] for x in items if x["priority"] in {"Must", "Should", "Could"})
        in_scope = sum(hours_by_priority.values())
        fp = parse_num(fp_by_feature[feature])
        rollup_rows.append([feature, feature_names[feature], len(feature_l2), len(items), fmt1(base_hours),
                            fmt1(hours_by_priority["Must"]), fmt1(hours_by_priority["Should"]),
                            fmt1(hours_by_priority["Could"]), fmt1(in_scope), fmt_money(cost_in_scope),
                            fmt_pct(100 * hours_by_priority["Must"] / in_scope if in_scope else 0),
                            fp_by_feature[feature], fmt1(base_hours / fp if fp else 0)])
        totals["l2"] += len(feature_l2)
        totals["l3"] += len(items)
        totals["base"] += base_hours
        totals["must"] += hours_by_priority["Must"]
        totals["should"] += hours_by_priority["Should"]
        totals["could"] += hours_by_priority["Could"]
        totals["cost"] += cost_in_scope
    total_scope_hours = totals["must"] + totals["should"] + totals["could"]
    rollup_rows.append(["**Project**", "", int(totals["l2"]), int(totals["l3"]), fmt1(totals["base"]),
                        fmt1(totals["must"]), fmt1(totals["should"]), fmt1(totals["could"]),
                        fmt1(total_scope_hours), fmt_money(totals["cost"]),
                        fmt_pct(100 * totals["must"] / total_scope_hours if total_scope_hours else 0),
                        total_fp, fmt1(totals["base"] / total_fp if total_fp else 0)])
    w2 = replace_table(w2, "In-scope cost", render_table(rollup_header, rollup_rows), "## Roll-up per feature")

    # W2: three scope scenarios.
    scenario_defs = [
        ("Committed", "Must only", {"Must"}, "What the team guarantees to deliver"),
        ("Expected", "Must + Should", {"Must", "Should"}, "The figure given to the client; the base cash flow in W6"),
        ("Ceiling", "Must + Should + Could", {"Must", "Should", "Could"}, "If the Could pool is never consumed"),
    ]
    headline_rows = []
    scenario_totals = {}
    for label, scope, priorities, meaning in scenario_defs:
        hours = sum(x["hours"] for x in work if x["priority"] in priorities)
        cost = sum(x["cost"] for x in work if x["priority"] in priorities)
        scenario_totals[label] = (hours, cost)
        headline_rows.append([label, scope, fmt1(hours), fmt_money(cost), meaning])
    headline_header = ["Scenario", "Scope", "Person-hours", "Cost (VND)", "Meaning"]
    w2 = replace_table(w2, "Meaning", render_table(headline_header, headline_rows), "## The three headline figures")

    # Use the already parsed W5 assumptions for threshold checks and downstream cash flow.
    capacity_match = re.search(r"(\d+(?:\.\d+)?)\s*person-hours", w5_assumptions["Team capacity"], re.I)
    if not capacity_match:
        raise ValueError("Could not parse Team capacity from W5")
    capacity = float(capacity_match.group(1))
    fp_hours = numbers_in(w5_assumptions["Hours per function point (cross-check only)"])[0]
    must_cost = scenario_totals["Committed"][1]
    contingency_pct = parse_percent(w5_assumptions["Money contingency on the Must set"], "")
    contingency = round(must_cost * contingency_pct)

    hidden_hours = sum(x["hours"] for x in work if x["hidden"] and x["priority"] in {"Must", "Should", "Could"})
    hidden_share = 100 * hidden_hours / total_scope_hours if total_scope_hours else 0
    must_share = 100 * totals["must"] / total_scope_hours if total_scope_hours else 0
    could_share = 100 * totals["could"] / total_scope_hours if total_scope_hours else 0
    fp_estimated_hours = total_fp * fp_hours
    fp_gap = 100 * abs(fp_estimated_hours - totals["base"]) / totals["base"] if totals["base"] else 0
    above_ceiling = sum(1 for x in l3_items if parse_num(x["Base hours"]) > 16)
    no_must_features = [feature for feature in feature_names
                        if not any(x["priority"] == "Must" for x in grouped[feature])]
    feature_count = len(feature_names)
    threshold_rows = [
        ["Must share of in-scope effort", fmt_pct(must_share), "at most 60%", "PASS" if must_share <= 60 else "REVIEW"],
        ["Could share (contingency pool)", fmt_pct(could_share), "target 20%", "PASS"],
        ["In-scope effort vs team capacity", f"{fmt1(total_scope_hours)} p-h", f"at most {fmt1(capacity)} p-h",
         "PASS" if total_scope_hours <= capacity else "REVIEW"],
        ["Hidden technical work, share of effort", fmt_pct(hidden_share), "at least 10%", "PASS" if hidden_share >= 10 else "REVIEW"],
        ["L3 rows above 16 hours", above_ceiling, "0", "PASS" if above_ceiling == 0 else "REVIEW"],
        ["Feature count", feature_count, "3 to 6", "PASS" if 3 <= feature_count <= 6 else "REVIEW"],
        [f"Function-point cross-check: {int(total_fp)} transactional FP x {fmt1(fp_hours)} h = {fmt1(fp_estimated_hours)} h vs {fmt1(totals['base'])} bottom-up base h",
         f"{fmt1(fp_gap)}% apart", "at most 30%", "PASS" if fp_gap <= 30 else "REVIEW"],
    ]
    threshold_header = ["Indicator", "Value", "Threshold", "Verdict"]
    w2 = replace_table(w2, "Indicator", render_table(threshold_header, threshold_rows), "## Threshold check (after W4)")
    observations = [
        "Three observations the team carries into W4:",
        "",
        f"1. Must represents {fmt_pct(must_share)} of in-scope effort against a 60% ceiling; assess every new Must against this limit.",
        f"2. Hidden technical work is {fmt_pct(hidden_share)} of in-scope effort (threshold: at least 10%).",
        (f"3. These features currently have no Must L2 function: {', '.join(no_must_features)}."
         if no_must_features else "3. Every feature currently has at least one Must L2 function."),
    ]
    marker = "Three observations the team carries into W4:"
    if marker in w2:
        w2 = w2[:w2.index(marker)] + "\n".join(observations) + "\n"

    # W5: scenario baseline, contingency and Must-only task seed.
    w5_scenario_header = ["Scenario", "Person-hours", "Cost (VND)", "Role in the cash-flow analysis (W6)"]
    w5_scenario_rows = [
        ["Pessimistic: Must only", fmt1(scenario_totals["Committed"][0]), fmt_money(scenario_totals["Committed"][1]), "Lowest investment, lowest benefit"],
        ["Base: Must + Should", fmt1(scenario_totals["Expected"][0]), fmt_money(scenario_totals["Expected"][1]), "The client figure; base cash flow"],
        ["Optimistic: full scope", fmt1(scenario_totals["Ceiling"][0]), fmt_money(scenario_totals["Ceiling"][1]), "If the Could pool is never consumed"],
    ]
    w5 = replace_table(w5, "Role in the cash-flow analysis", render_table(w5_scenario_header, w5_scenario_rows), "## 1. Three scenarios")
    w5 = update_assumption_value(w5, "Money contingency on the Must set",
                                  f"{contingency_pct * 100:g}% = {fmt_money(contingency)} VND (recalculated from W4 Must cost)")
    task_items = [x for x in work if x["priority"] == "Must"]
    risk_order = {"INT": 1, "BE": 2, "FE": 3}
    task_items.sort(key=lambda x: (risk_order[x["layer"]], next(i for i, y in enumerate(work) if y["l3_id"] == x["l3_id"])))
    task_header = ["L3 ID", "Layer", "Person-hours", "Risk order"]
    task_rows = [[x["l3_id"], x["layer"], fmt1(x["hours"]), risk_order[x["layer"]]] for x in task_items]
    w5 = replace_table(w5, "Risk order", render_table(task_header, task_rows), "## 3. tasks.md seed (effective priority Must)")

    # W6: read its assumptions before updating the derived contingency row.
    _, _, w6_assumption_header, w6_assumption_rows = table_by_header(w6, "Value", "## 1. Assumptions")
    w6_assumptions = {row_dict(w6_assumption_header, row)["Assumption"]: row_dict(w6_assumption_header, row)["Value"]
                      for row in w6_assumption_rows}
    discount_rate = parse_percent(w6_assumptions["Discount rate (hurdle rate)"], "")
    horizon_match = re.search(r"(\d+)", w6_assumptions["Evaluation horizon"])
    running_rate = parse_percent(w6_assumptions["Annual running cost"], "")
    if not horizon_match:
        raise ValueError("Could not parse W6 evaluation horizon")
    horizon = int(horizon_match.group(1))
    benefits_text = w6_assumptions["Steady-state annual benefit"]
    benefit_values = numbers_in(benefits_text)
    if len(benefit_values) < 3:
        raise ValueError("Could not parse Must/Should/Could steady-state benefits from W6")
    benefit_by_priority = dict(zip(("Must", "Should", "Could"), benefit_values[:3]))
    ramp_values = [float(x) for x in re.findall(
        r"Year\s+\d+(?:\s+to\s+\d+)?:\s*(\d+(?:\.\d+)?)\s*%",
        w6_assumptions["Adoption ramp-up (share of steady-state benefit)"],
        re.I,
    )]
    ramp = [x / 100 for x in ramp_values]
    if len(ramp) < 3:
        raise ValueError("W6 adoption ramp-up must define Year 1, Year 2 and Year 3+ percentages")
    ramp_by_year = [ramp[0], ramp[1]] + [ramp[2]] * max(0, horizon - 2)
    w6 = replace_table(w6, "Value", render_table(
        w6_assumption_header,
        [[row_dict(w6_assumption_header, row)["Assumption"],
          (f"{contingency_pct * 100:g}% of the Must cost = {fmt_money(contingency)} VND, recalculated from W5")
          if row_dict(w6_assumption_header, row)["Assumption"] == "Contingency"
          else row_dict(w6_assumption_header, row)["Value"]]
         for row in w6_assumption_rows]), "## 1. Assumptions")

    # Recompute cash-flow schedules from the W5 scenario build costs.
    cash_scenarios = [
        ("Pessimistic: Must only", "Committed", {"Must"}),
        ("Base: Must + Should", "Expected", {"Must", "Should"}),
        ("Optimistic: full scope", "Ceiling", {"Must", "Should", "Could"}),
    ]
    cash_results = {}
    for heading, scenario_key, priorities in cash_scenarios:
        build_cost = scenario_totals[scenario_key][1]
        investment = build_cost + contingency
        steady_benefit = sum(benefit_by_priority[p] for p in priorities)
        running_cost = build_cost * running_rate
        annual_benefits = [0] + [steady_benefit * ramp_by_year[y - 1] for y in range(1, horizon + 1)]
        annual_running = [0] + [-running_cost] * horizon
        investments = [-investment] + [0] * horizon
        net = [annual_benefits[i] + annual_running[i] + investments[i] for i in range(horizon + 1)]
        cumulative = []
        running_total = 0
        for value in net:
            running_total += value
            cumulative.append(running_total)
        pv = [net[y] / ((1 + discount_rate) ** y) for y in range(horizon + 1)]
        npv_value = sum(pv)
        irr_value = irr(net)
        payback_value = payback(net)
        pi = 1 + npv_value / investment if investment else float("nan")
        cash_results[scenario_key] = {
            "investment": investment, "benefit": steady_benefit, "net": net, "npv": npv_value,
            "irr": irr_value, "payback": payback_value, "pi": pi,
            "decision": "ACCEPT" if npv_value >= 0 and irr_value is not None and irr_value >= discount_rate else "REJECT / REVIEW",
        }
        line_header = ["Line item"] + [f"Year {y}" for y in range(horizon + 1)]
        line_rows = [
            ["Benefits"] + [fmt_money(x) for x in annual_benefits],
            ["Running cost"] + [fmt_signed_money(x) for x in annual_running],
            ["Investment (build + contingency)"] + [fmt_signed_money(x) for x in investments],
            ["Net cash flow"] + [fmt_signed_money(x) for x in net],
            ["Cumulative net cash flow"] + [fmt_signed_money(x) for x in cumulative],
            ["PV of net cash flow"] + [fmt_signed_money(x) for x in pv],
        ]
        w6 = replace_table(w6, "Line item", render_table(line_header, line_rows), f"## {heading}")

    # W6: investment metrics.
    results_header = ["Metric", "Pessimistic: Must only", "Base: Must + Should", "Optimistic: full scope"]
    metric_rows = [
        ["Year-0 investment (VND)"] + [fmt_money(cash_results[k]["investment"]) for k in ("Committed", "Expected", "Ceiling")],
        ["Steady-state benefit per year (VND)"] + [fmt_money(cash_results[k]["benefit"]) for k in ("Committed", "Expected", "Ceiling")],
        [f"NPV at {discount_rate * 100:g}% (VND)"] + [fmt_signed_money(cash_results[k]["npv"]) for k in ("Committed", "Expected", "Ceiling")],
        ["IRR"] + [f"{cash_results[k]['irr'] * 100:.1f}%" if cash_results[k]["irr"] is not None else "N/A" for k in ("Committed", "Expected", "Ceiling")],
        ["Simple payback (years)"] + [f"{cash_results[k]['payback']:.2f}" if cash_results[k]["payback"] is not None else "N/A" for k in ("Committed", "Expected", "Ceiling")],
        ["Profitability index"] + [f"{cash_results[k]['pi']:.2f}" for k in ("Committed", "Expected", "Ceiling")],
        ["Decision signal"] + [cash_results[k]["decision"] for k in ("Committed", "Expected", "Ceiling")],
    ]
    w6 = replace_table(w6, "Metric", render_table(results_header, metric_rows), "## Results")

    # Keep the explanatory reading aligned with the newly computed metrics.
    best_npv = max(cash_results, key=lambda key: cash_results[key]["npv"])
    best_irr = max(cash_results, key=lambda key: cash_results[key]["irr"] if cash_results[key]["irr"] is not None else -math.inf)
    scenario_label = {"Committed": "Pessimistic", "Expected": "Base", "Ceiling": "Optimistic"}
    reading = (f"Reading: The {scenario_label[best_npv]} scenario has the highest NPV; the "
               f"{scenario_label[best_irr]} scenario has the highest IRR. Benefits, running costs, "
               f"investment, NPV, IRR and payback above are recalculated from W5 and the assumptions "
               f"at the top of this file. The contingency remains {contingency_pct * 100:g}% of the Must cost.")
    if "Reading:" in w6:
        w6 = w6[:w6.index("Reading:")] + reading + "\n" + w6[w6.index("Formulas:"):]

    # Write only after all validations and calculations have succeeded.
    write_if_changed(W4, w4)
    write_if_changed(W2, w2)
    write_if_changed(W5, w5)
    write_if_changed(W6, w6)
    print("Derived Markdown tables rebuilt successfully.")


if __name__ == "__main__":
    main()
