# W6 Cash flow and investment decision: LabDesk

> Worked example for teaching (LabDesk). Not a student submission and not a real product.

Lesson 6 (Capital Budgeting). Takes the three scenarios from [W5](w5-handover.md).

## 1. Assumptions

| Assumption | Value |
| --- | --- |
| Discount rate (hurdle rate) | 12% per year |
| Evaluation horizon | 5 years |
| Annual running cost | 15% of build cost per year (hosting, email service, maintenance) |
| Contingency | 10% of the Must cost = 2.748.000 VND, recalculated from W5 |
| Steady-state annual benefit | Must 18.000.000 · Should 8.000.000 · Could 2.000.000 VND |
| Adoption ramp-up (share of steady-state benefit) | Year 1: 40% · Year 2: 70% · Year 3 to 5: 100% |

Where the benefit comes from (team estimates, to be checked with the faculty after one semester): technician time no longer spent on the paper sign-up sheet and on chasing empty seats (Must), fewer seats left empty because no-shows are released and limited, and faulty seats blocked before students sit at them (Should), better planning from occupancy reports (Could).

## Pessimistic: Must only

| Line item | Year 0 | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
| --- | --- | --- | --- | --- | --- | --- |
| Benefits | 0 | 7.200.000 | 12.600.000 | 18.000.000 | 18.000.000 | 18.000.000 |
| Running cost | 0 | -4.122.000 | -4.122.000 | -4.122.000 | -4.122.000 | -4.122.000 |
| Investment (build + contingency) | -30.228.000 | 0 | 0 | 0 | 0 | 0 |
| Net cash flow | -30.228.000 | 3.078.000 | 8.478.000 | 13.878.000 | 13.878.000 | 13.878.000 |
| Cumulative net cash flow | -30.228.000 | -27.150.000 | -18.672.000 | -4.794.000 | 9.084.000 | 22.962.000 |
| PV of net cash flow | -30.228.000 | 2.748.214 | 6.758.610 | 9.878.086 | 8.819.720 | 7.874.750 |

## Base: Must + Should

| Line item | Year 0 | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
| --- | --- | --- | --- | --- | --- | --- |
| Benefits | 0 | 10.400.000 | 18.200.000 | 26.000.000 | 26.000.000 | 26.000.000 |
| Running cost | 0 | -5.907.000 | -5.907.000 | -5.907.000 | -5.907.000 | -5.907.000 |
| Investment (build + contingency) | -42.128.000 | 0 | 0 | 0 | 0 | 0 |
| Net cash flow | -42.128.000 | 4.493.000 | 12.293.000 | 20.093.000 | 20.093.000 | 20.093.000 |
| Cumulative net cash flow | -42.128.000 | -37.635.000 | -25.342.000 | -5.249.000 | 14.844.000 | 34.937.000 |
| PV of net cash flow | -42.128.000 | 4.011.607 | 9.799.904 | 14.301.801 | 12.769.465 | 11.401.308 |

## Optimistic: full scope

| Line item | Year 0 | Year 1 | Year 2 | Year 3 | Year 4 | Year 5 |
| --- | --- | --- | --- | --- | --- | --- |
| Benefits | 0 | 11.200.000 | 19.600.000 | 28.000.000 | 28.000.000 | 28.000.000 |
| Running cost | 0 | -7.485.000 | -7.485.000 | -7.485.000 | -7.485.000 | -7.485.000 |
| Investment (build + contingency) | -52.648.000 | 0 | 0 | 0 | 0 | 0 |
| Net cash flow | -52.648.000 | 3.715.000 | 12.115.000 | 20.515.000 | 20.515.000 | 20.515.000 |
| Cumulative net cash flow | -52.648.000 | -48.933.000 | -36.818.000 | -16.303.000 | 4.212.000 | 24.727.000 |
| PV of net cash flow | -52.648.000 | 3.316.964 | 9.658.004 | 14.602.172 | 13.037.653 | 11.640.762 |

## Results

| Metric | Pessimistic: Must only | Base: Must + Should | Optimistic: full scope |
| --- | --- | --- | --- |
| Year-0 investment (VND) | 30.228.000 | 42.128.000 | 52.648.000 |
| Steady-state benefit per year (VND) | 18.000.000 | 26.000.000 | 28.000.000 |
| NPV at 12% (VND) | 5.851.380 | 10.156.085 | -392.445 |
| IRR | 18.2% | 19.6% | 11.8% |
| Simple payback (years) | 3.35 | 3.26 | 3.79 |
| Profitability index | 1.19 | 1.24 | 0.99 |
| Decision signal | ACCEPT | ACCEPT | REJECT / REVIEW |

Reading: The Base scenario has the highest NPV; the Base scenario has the highest IRR. Benefits, running costs, investment, NPV, IRR and payback above are recalculated from W5 and the assumptions at the top of this file. The contingency remains 10% of the Must cost.
Formulas: NPV = sum of net cash flow / (1 + r)^t for t = 0 to 5; IRR is the rate at which NPV = 0; payback interpolates inside the year in which the cumulative net cash flow turns positive; profitability index = 1 + NPV / investment.
