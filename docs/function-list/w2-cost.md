# W2 Costing and roll-up: LabDesk

> Worked example for teaching (LabDesk). Not a student submission and not a real product.

Lesson 5 (block W2). Fully derived from [W1](w1-function-list.md), the effective priorities in [W4](w4-priorities.md) and the class Parameters:

- Person-hours = base hours x AI leverage factor + base hours x verification factor.
- AI leverage: FE 0.35, BE 0.7, INT 1.0. Verification factor: 0.15 when the EARS criterion is precise, 0.4 when it is vague.
- Rate: FE Junior 200.000 VND/h; BE and INT Senior 300.000 VND/h.

## Cost per L3 work item

| L3 ID | Feature | Layer | Base h | AI-adj. h | Verif. h | Person-hours | Band | Cost (VND) | Effective priority |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FR-00-01-FE | F-00 | FE | 4.0 | 1.4 | 0.6 | 2.0 | Junior | 400.000 | Must |
| FR-00-01-INT | F-00 | INT | 8.0 | 8.0 | 1.2 | 9.2 | Senior | 2.760.000 | Must |
| FR-00-02-BE | F-00 | BE | 4.0 | 2.8 | 0.6 | 3.4 | Senior | 1.020.000 | Must |
| FR-00-03-BE1 | F-00 | BE | 8.0 | 5.6 | 1.2 | 6.8 | Senior | 2.040.000 | Must |
| FR-00-03-BE2 | F-00 | BE | 4.0 | 2.8 | 0.6 | 3.4 | Senior | 1.020.000 | Must |
| FR-00-04-BE | F-00 | BE | 4.0 | 2.8 | 0.6 | 3.4 | Senior | 1.020.000 | Should |
| FR-01-01-BE | F-01 | BE | 4.0 | 2.8 | 0.6 | 3.4 | Senior | 1.020.000 | Must |
| FR-01-01-FE | F-01 | FE | 4.0 | 1.4 | 0.6 | 2.0 | Junior | 400.000 | Must |
| FR-01-02-BE | F-01 | BE | 4.0 | 2.8 | 0.6 | 3.4 | Senior | 1.020.000 | Must |
| FR-01-02-FE | F-01 | FE | 8.0 | 2.8 | 1.2 | 4.0 | Junior | 800.000 | Must |
| FR-01-03-BE | F-01 | BE | 4.0 | 2.8 | 0.6 | 3.4 | Senior | 1.020.000 | Must |
| FR-01-03-FE | F-01 | FE | 4.0 | 1.4 | 0.6 | 2.0 | Junior | 400.000 | Must |
| FR-01-04-BE | F-01 | BE | 8.0 | 5.6 | 1.2 | 6.8 | Senior | 2.040.000 | Must |
| FR-01-05-BE | F-01 | BE | 4.0 | 2.8 | 0.6 | 3.4 | Senior | 1.020.000 | Must |
| FR-01-06-BE | F-01 | BE | 4.0 | 2.8 | 0.6 | 3.4 | Senior | 1.020.000 | Must |
| FR-01-06-INT | F-01 | INT | 8.0 | 8.0 | 1.2 | 9.2 | Senior | 2.760.000 | Must |
| FR-01-07-BE | F-01 | BE | 4.0 | 2.8 | 0.6 | 3.4 | Senior | 1.020.000 | Must |
| FR-01-07-FE | F-01 | FE | 4.0 | 1.4 | 0.6 | 2.0 | Junior | 400.000 | Must |
| FR-01-08-BE | F-01 | BE | 4.0 | 2.8 | 0.6 | 3.4 | Senior | 1.020.000 | Must |
| FR-01-08-FE | F-01 | FE | 4.0 | 1.4 | 0.6 | 2.0 | Junior | 400.000 | Must |
| FR-01-09-BE | F-01 | BE | 4.0 | 2.8 | 0.6 | 3.4 | Senior | 1.020.000 | Could |
| FR-01-09-INT | F-01 | INT | 4.0 | 4.0 | 0.6 | 4.6 | Senior | 1.380.000 | Could |
| FR-01-10-BE | F-01 | BE | 4.0 | 2.8 | 0.6 | 3.4 | Senior | 1.020.000 | Could |
| FR-01-10-FE | F-01 | FE | 4.0 | 1.4 | 0.6 | 2.0 | Junior | 400.000 | Could |
| FR-01-11-BE | F-01 | BE | 4.0 | 2.8 | 0.6 | 3.4 | Senior | 1.020.000 | Could |
| FR-01-11-FE | F-01 | FE | 4.0 | 1.4 | 0.6 | 2.0 | Junior | 400.000 | Could |
| FR-02-01-BE | F-02 | BE | 4.0 | 2.8 | 0.6 | 3.4 | Senior | 1.020.000 | Must |
| FR-02-01-FE | F-02 | FE | 4.0 | 1.4 | 0.6 | 2.0 | Junior | 400.000 | Must |
| FR-02-02-FE | F-02 | FE | 4.0 | 1.4 | 0.6 | 2.0 | Junior | 400.000 | Must |
| FR-02-03-BE | F-02 | BE | 4.0 | 2.8 | 0.6 | 3.4 | Senior | 1.020.000 | Must |
| FR-02-04-BE1 | F-02 | BE | 8.0 | 5.6 | 1.2 | 6.8 | Senior | 2.040.000 | Must |
| FR-02-04-BE2 | F-02 | BE | 4.0 | 2.8 | 0.6 | 3.4 | Senior | 1.020.000 | Must |
| FR-02-05-INT | F-02 | INT | 4.0 | 4.0 | 0.6 | 4.6 | Senior | 1.380.000 | Should |
| FR-02-06-BE | F-02 | BE | 8.0 | 5.6 | 1.2 | 6.8 | Senior | 2.040.000 | Should |
| FR-03-01-BE | F-03 | BE | 4.0 | 2.8 | 0.6 | 3.4 | Senior | 1.020.000 | Should |
| FR-03-01-FE | F-03 | FE | 8.0 | 2.8 | 1.2 | 4.0 | Junior | 800.000 | Should |
| FR-03-02-BE | F-03 | BE | 4.0 | 2.8 | 0.6 | 3.4 | Senior | 1.020.000 | Should |
| FR-03-02-FE | F-03 | FE | 4.0 | 1.4 | 0.6 | 2.0 | Junior | 400.000 | Should |
| FR-03-03-BE | F-03 | BE | 4.0 | 2.8 | 0.6 | 3.4 | Senior | 1.020.000 | Should |
| FR-03-03-INT | F-03 | INT | 4.0 | 4.0 | 0.6 | 4.6 | Senior | 1.380.000 | Should |
| FR-03-04-BE | F-03 | BE | 4.0 | 2.8 | 0.6 | 3.4 | Senior | 1.020.000 | Should |
| FR-03-04-FE | F-03 | FE | 8.0 | 2.8 | 1.2 | 4.0 | Junior | 800.000 | Should |
| FR-03-05-BE | F-03 | BE | 8.0 | 5.6 | 1.2 | 6.8 | Senior | 2.040.000 | Could |
| FR-03-05-FE | F-03 | FE | 4.0 | 1.4 | 0.6 | 2.0 | Junior | 400.000 | Could |
| FR-03-06-BE | F-03 | BE | 8.0 | 5.6 | 1.2 | 6.8 | Senior | 2.040.000 | Could |
| FR-03-06-FE | F-03 | FE | 8.0 | 2.8 | 1.2 | 4.0 | Junior | 800.000 | Could |

## Roll-up per feature

| Feature | Name | L2 | L3 | Base h | Must p-h | Should p-h | Could p-h | In-scope p-h | In-scope cost (VND) | Must share | Transactional FP | Base h per FP |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| F-00 | Platform and Access | 4 | 6 | 32.0 | 24.8 | 3.4 | 0.0 | 28.2 | 8.260.000 | 87.9% | 4 | 8.0 |
| F-01 | Seat Booking | 11 | 20 | 92.0 | 51.8 | 0.0 | 18.8 | 70.6 | 19.580.000 | 73.4% | 39 | 2.4 |
| F-02 | Check-in and No-show | 6 | 8 | 40.0 | 21.0 | 11.4 | 0.0 | 32.4 | 9.320.000 | 64.8% | 13 | 3.1 |
| F-03 | Lab Operations | 6 | 12 | 68.0 | 0.0 | 28.2 | 19.6 | 47.8 | 12.740.000 | 0.0% | 27 | 2.5 |
| **Project** |  | 27 | 46 | 232.0 | 97.6 | 43.0 | 38.4 | 179.0 | 49.900.000 | 54.5% | 83.0 | 2.8 |

## The three headline figures

| Scenario | Scope | Person-hours | Cost (VND) | Meaning |
| --- | --- | --- | --- | --- |
| Committed | Must only | 97.6 | 27.480.000 | What the team guarantees to deliver |
| Expected | Must + Should | 140.6 | 39.380.000 | The figure given to the client; the base cash flow in W6 |
| Ceiling | Must + Should + Could | 179.0 | 49.900.000 | If the Could pool is never consumed |

## Threshold check (after W4)

| Indicator | Value | Threshold | Verdict |
| --- | --- | --- | --- |
| Must share of in-scope effort | 54.5% | at most 60% | PASS |
| Could share (contingency pool) | 21.5% | target 20% | PASS |
| In-scope effort vs team capacity | 179.0 p-h | at most 360.0 p-h | PASS |
| Hidden technical work, share of effort | 11.4% | at least 10% | PASS |
| L3 rows above 16 hours | 0 | 0 | PASS |
| Feature count | 4 | 3 to 6 | PASS |
| Function-point cross-check: 83 transactional FP x 3.0 h = 249.0 h vs 232.0 bottom-up base h | 7.3% apart | at most 30% | PASS |

Three observations the team carries into W4:

1. Must represents 54.5% of in-scope effort against a 60% ceiling; assess every new Must against this limit.
2. Hidden technical work is 11.4% of in-scope effort (threshold: at least 10%).
3. These features currently have no Must L2 function: F-03.
