# W3 — Cross-team review

> **Input**: The owning team's W0–W2 sheets, plus the machine signals already computed in W2_Rollup.
>
> **Output**: A completed eight-criterion checklist and a defect log with at least two concrete, evidenced defects. The defect log is the input to W4.
>
> **Who Fills What**: BLUE cells = the OWNING team, filled before handing the file over. ORANGE cells = the REVIEWING team. Green cells are computed. Neither team writes in the other's colour.
>
> **Procedure**: 1. Teams swap files in a ring: A reviews B, B reviews C, C reviews A.
>  2. The reviewer reads the machine signals in column D — three criteria are already answered.
>  3. The reviewer judges the five human criteria IN THIS ORDER: C2, then C3, C4, C5, then C8. Every finding must quote the offending cell.
>  4. The reviewer presents. The owning team may ONLY ask clarifying questions — no rebuttal here.
>
> **Rule**: A review that reports 'looks fine' scores zero. Minimum two defects with evidence.

<!-- Chỉ sửa trong các bảng 'input'. Phần giữa BEGIN/END sẽ được build.py ghi lại. -->

## Teams

<!-- BEGIN:teams | input table -->
| Item | Value |
|---|---|
| Owning team | Team ... |
| Reviewing team | Team ... |
<!-- END:teams -->

## Checklist - eight quality criteria

<!-- BEGIN:checklist | input table - computed columns (do not edit): D -->
| # | Criterion | Judged by | Machine signal (computed) | Owning team's self-assessment | Reviewer verdict and evidence | Reviewer: pass? | Note |
|---|---|---|---|---|---|---|---|
| C1 | Two-way traceability | Machine + person | Features: 4  \|  see _coverage.md |  |  |  |  |
| C2 | Scope boundary explicit (Won't-have with a reason) | Person | Won't-have rows recorded: 3 |  |  |  |  |
| C3 | MECE — no duplicates, no missing CRUD | Person | Not machine-checkable — read it |  |  |  |  |
| C4 | State and time transitions have a trigger | Person | Read it — look for CLOCK-triggered functions |  |  |  |  |
| C5 | Hidden technical work | Machine + person | Hidden share: 62.9%  (floor 10%) |  |  |  |  |
| C6 | Granularity 4-16 hours | Machine | L3 rows above ceiling: 0 |  |  |  |  |
| C7 | Layer label FE / BE / INT present | Machine + person | L3 rows missing a layer: 0 |  |  |  |  |
| C8 | Independently testable EARS sentence | Person | Rows flagged EARS not precise: 2 |  |  |  |  |
<!-- END:checklist -->

## Defect log

<!-- BEGIN:defects | input table - computed columns (do not edit): H -->
| # | Location (L2 / L3 ID) | Criterion | Evidence — quote the offending cell | Reviewer's proposed bucket | Owning team's response | Owning team's decision | Person-hours affected |
|---|---|---|---|---|---|---|---|
| 1 | FR-01-02 | C3 MECE | Column C overlaps the constraint already implied by FR-01-01 | Fix now - merge or cross-reference | Accepted - kept separate, rationale added | Fix now | 17.6 |
| 2 | FR-03-04 | C8 EARS | Column M says No; the criterion does not state which totals the summary contains | Mark [NEEDS CLARIFICATION] | Accepted - question raised with the client | Clarify | 5.4 |
<!-- END:defects -->
