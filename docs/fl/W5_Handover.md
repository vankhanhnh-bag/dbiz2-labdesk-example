# W5 — Baseline and handover

> **Input**: The three headline figures from W2_Rollup and the assumption set from Parameters.
>
> **Output**: Git tag fl-v1.0, business-case.md (three figures plus assumptions), tasks.md seeded risk-first, and one consolidated open-questions table.
>
> **Procedure**: 1. The commit message records that all thresholds pass.
>  2. Fill sections 1 and 2 below; export them as business-case.md.
>  3. In section 3, filter Effective priority = Must and sort Risk order ascending — that is the order for tasks.md.
>  4. Complete section 4 and confirm nothing is left dangling.

<!-- Chỉ sửa trong các bảng 'input'. Phần giữa BEGIN/END sẽ được build.py ghi lại. -->

## 1. Three scenarios

<!-- BEGIN:scenarios | input table - computed columns (do not edit): B, C -->
| Scenario | Person-hours | Cost (VND) | Role in the sensitivity analysis |
|---|---|---|---|
| Pessimistic — Must only | 302 | 86,000,000 | Lowest investment, lowest benefit |
| Base — Must + Should | 386.2 | 109,060,000 | The client figure; base cash flow for NPV |
| Optimistic — full scope | 395 | 111,500,000 | If the Could pool is never consumed |
<!-- END:scenarios -->

_The three MoSCoW tiers ARE the three scenarios — no invented plus-or-minus 20%._

## 2. Assumptions

<!-- BEGIN:assumptions | input table - computed columns (do not edit): B -->
| Assumption | Value | Source |
|---|---|---|
| Junior rate | 200,000 | ITviec 2025-26 salary report |
| Senior rate | 300,000 | ITviec 2025-26 salary report |
| Expert rate | 400,000 | ITviec 2025-26 salary report |
| AI leverage — FE / BE / INT | 0.35 / 0.7 / 1 | Class parameter, recalibrated each cohort |
| Verification factor — precise / vague | 0.15 / 0.4 | Class parameter |
| Hours per function point | 3 | Class parameter — used only for the cross-check |
| Team capacity (person-hours) | 240 | 4 people x 12 weeks x 5 h |
| Money contingency on the Must set | 0.1 | Covers estimation error only. Do NOT add 20% on top of the Could pool — same buffer twice. |
<!-- END:assumptions -->

## 3. tasks.md seed

<!-- BEGIN:tasks | derived - auto-generated, do not edit -->
| L3 ID | Layer | Effective priority | Person-hours | Risk order |
|---|---|---|---|---|
| FR-01-01-FE | FE | Must | 4 | 3 |
| FR-01-01-BE | BE | Must | 6.8 | 2 |
| FR-01-02-FE | FE | Must | 4 | 3 |
| FR-01-02-BE | BE | Must | 13.6 | 2 |
| FR-01-03-BE | BE | Must | 13.6 | 2 |
| FR-01-04-FE | FE | Should | 4 | 3 |
| FR-01-04-BE | BE | Should | 3.4 | 2 |
| FR-01-05-BE | BE | Must | 13.6 | 2 |
| FR-01-05-FE | FE | Must | 4 | 3 |
| FR-01-06-BE | BE | Should | 13.6 | 2 |
| FR-01-06-FE | FE | Should | 4 | 3 |
| FR-01-07-BE | BE | Must | 13.6 | 2 |
| FR-01-08-FE | FE | Should | 4 | 3 |
| FR-01-08-BE | BE | Should | 6.8 | 2 |
| FR-02-01-FE | FE | Must | 4 | 3 |
| FR-02-01-BE | BE | Must | 6.8 | 2 |
| FR-02-02-BE | BE | Must | 6.8 | 2 |
| FR-02-02-FE | FE | Must | 2 | 3 |
| FR-02-03-BE | BE | Must | 6.8 | 2 |
| FR-02-04-BE | BE | Must | 13.6 | 2 |
| FR-02-05-BE | BE | Must | 3.4 | 2 |
| FR-02-06-INT | INT | Must | 22.4 | 1 |
| FR-02-06-BE | BE | Must | 6.8 | 2 |
| FR-02-07-BE | BE | Must | 13.6 | 2 |
| FR-02-08-BE | BE | Must | 6.8 | 2 |
| FR-02-08-FE | FE | Must | 2 | 3 |
| FR-02-09-BE | BE | Must | 6.8 | 2 |
| FR-02-09-FE | FE | Must | 4 | 3 |
| FR-02-10-BE | BE | Should | 6.8 | 2 |
| FR-02-10-FE | FE | Should | 2 | 3 |
| FR-02-11-INT | INT | Should | 11.2 | 1 |
| FR-02-11-FE | FE | Should | 4 | 3 |
| FR-02-12-BE | BE | Should | 13.6 | 2 |
| FR-02-12-FE | FE | Should | 2 | 3 |
| FR-02-13-BE | BE | Could | 6.8 | 2 |
| FR-02-13-FE | FE | Could | 2 | 3 |
| FR-02-14-FE | FE | Must | 4 | 3 |
| FR-02-14-BE | BE | Must | 3.4 | 2 |
| FR-02-15-FE | FE | Must | 4 | 3 |
| FR-02-15-BE | BE | Must | 6.8 | 2 |
| FR-02-16-BE | BE | Must | 6.8 | 2 |
| FR-02-16-FE | FE | Must | 2 | 3 |
| FR-02-17-BE | BE | Must | 13.6 | 2 |
| FR-02-17-FE | FE | Must | 2 | 3 |
| FR-03-01-BE | BE | Must | 3.4 | 2 |
| FR-03-02-BE | BE | Must | 6.8 | 2 |
| FR-03-02-INT | INT | Must | 9.2 | 1 |
| FR-03-03-BE | BE | Must | 6.8 | 2 |
| FR-03-03-FE | FE | Must | 4 | 3 |
| FR-03-04-BE | BE | Must | 3.4 | 2 |
| FR-03-04-FE | FE | Must | 2 | 3 |
| FR-04-01-BE | BE | Must | 13.6 | 2 |
| FR-04-01-FE | FE | Must | 4 | 3 |
| FR-04-02-BE | BE | Must | 6.8 | 2 |
| FR-04-02-BE | BE | Must | 6.8 | 2 |
| FR-04-03-BE | BE | Must | 6.8 | 2 |
| FR-04-04-BE | BE | Must | 6.8 | 2 |
| FR-04-05-BE | BE | Should | 6.8 | 2 |
| FR-04-06-FE | FE | Should | 2 | 3 |
<!-- END:tasks -->

_Risk order puts integrations first: the unknowns must be touched early, not at the end of DBIZ3._

## 4. Open questions

<!-- BEGIN:questions | input table -->
| # | [NEEDS CLARIFICATION] question | Blocking? | Owning feature | Default applied |
|---|---|---|---|---|
| 1 | [NEEDS CLARIFICATION: which totals must the weekly summary contain?] | No | F-03 | Assuming sessions per workstation and hours per workstation |
| 2 | [NEEDS CLARIFICATION: is card-swipe data pulled as a daily batch or in real time?] | Yes | F-02 | Assuming a daily batch |
<!-- END:questions -->
