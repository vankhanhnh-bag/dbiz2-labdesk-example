# W5 Baseline and handover: LabDesk

> Worked example for teaching (LabDesk). Not a student submission and not a real product.

Lesson 5 (block W5). The baseline every later lesson and DBIZ3 refer to.

## 1. Three scenarios

| Scenario | Person-hours | Cost (VND) | Role in the cash-flow analysis (W6) |
| --- | --- | --- | --- |
| Pessimistic: Must only | 97.6 | 27.480.000 | Lowest investment, lowest benefit |
| Base: Must + Should | 140.6 | 39.380.000 | The client figure; base cash flow |
| Optimistic: full scope | 179.0 | 49.900.000 | If the Could pool is never consumed |

## 2. Assumptions

| Assumption | Value | Source |
| --- | --- | --- |
| Junior / Senior / Expert rate | 200.000 / 300.000 / 400.000 VND per hour | Class Parameters (ITviec 2025-26 salary report) |
| AI leverage FE / BE / INT | 0.35 / 0.7 / 1.0 | Class Parameters |
| Verification factor precise / vague | 0.15 / 0.4 | Class Parameters |
| Hours per function point (cross-check only) | 3 | Class Parameters |
| Team capacity | 360 person-hours (6 people x 12 weeks x 5 h) | Class Parameters |
| Money contingency on the Must set | 10% = 2.748.000 VND (recalculated from W4 Must cost) | Class Parameters |

## 3. tasks.md seed (effective priority Must)

Risk order: 1 = INT (external services), 2 = BE, 3 = FE. DBIZ3 starts with the riskiest rows.

| L3 ID | Layer | Person-hours | Risk order |
| --- | --- | --- | --- |
| FR-00-01-INT | INT | 9.2 | 1 |
| FR-01-06-INT | INT | 9.2 | 1 |
| FR-00-02-BE | BE | 3.4 | 2 |
| FR-00-03-BE1 | BE | 6.8 | 2 |
| FR-00-03-BE2 | BE | 3.4 | 2 |
| FR-01-01-BE | BE | 3.4 | 2 |
| FR-01-02-BE | BE | 3.4 | 2 |
| FR-01-03-BE | BE | 3.4 | 2 |
| FR-01-04-BE | BE | 6.8 | 2 |
| FR-01-05-BE | BE | 3.4 | 2 |
| FR-01-06-BE | BE | 3.4 | 2 |
| FR-01-07-BE | BE | 3.4 | 2 |
| FR-01-08-BE | BE | 3.4 | 2 |
| FR-02-01-BE | BE | 3.4 | 2 |
| FR-02-03-BE | BE | 3.4 | 2 |
| FR-02-04-BE1 | BE | 6.8 | 2 |
| FR-02-04-BE2 | BE | 3.4 | 2 |
| FR-00-01-FE | FE | 2.0 | 3 |
| FR-01-01-FE | FE | 2.0 | 3 |
| FR-01-02-FE | FE | 4.0 | 3 |
| FR-01-03-FE | FE | 2.0 | 3 |
| FR-01-07-FE | FE | 2.0 | 3 |
| FR-01-08-FE | FE | 2.0 | 3 |
| FR-02-01-FE | FE | 2.0 | 3 |
| FR-02-02-FE | FE | 2.0 | 3 |

## 4. Open questions for the client

| # | Question | Blocking? |
|---|---|---|
| 1 | May Lab Technicians use a paper list for blocked seats until F-03 is delivered? | No |
| 2 | Is 15 minutes the agreed check-in window for every lab? | Yes (FR-02-03, FR-02-04) |
