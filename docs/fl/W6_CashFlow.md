# Cash Flow, NPV, IRR & Payback

> Whole-project analysis using the Base scope (Must + Should). Initial investment links to W5; update only the yellow assumption cells.

<!-- Chỉ sửa trong các bảng 'input'. Phần giữa BEGIN/END sẽ được build.py ghi lại. -->

## 1. Cash-flow assumptions

<!-- BEGIN:assumptions | input table -->
| Assumption | Value | Unit | Source / basis |
|---|---|---|---|
| Scope | Whole project — Base (Must + Should) |  | Lecturer guidance: whole-project analysis is acceptable |
| Initial implementation cost | 109,060,000 | VND | Linked from W5_Handover Base cost (Must + Should) |
| Discount rate | 0.1 | % | Team assumption — replace with WACC / required return if available |
| Analysis horizon | 5 | years | Team assumption; model supports 1–10 years |
| Year 1 gross annual benefit | 65600000 | VND / year | INPUT REQUIRED — quantify validated business benefits |
| Annual benefit growth | 0.3 | % / year | Team assumption |
| Year 1 recurring operating cost | 16,359,000 | VND / year | INPUT REQUIRED — hosting, maintenance, data/API, support, etc. |
| Annual operating-cost growth | 0.0331 | % / year | Team assumption |
| Terminal / residual value | 0 | VND | Optional; received at the end of the analysis horizon |
<!-- END:assumptions -->

## 2. Scenario drivers | inherited assumptions and W5 scope

<!-- BEGIN:drivers | derived - auto-generated, do not edit -->
| Input / metric | Pessimistic: Must | Base: Must + Should | Optimistic: Full | Calculation basis |
|---|---|---|---|---|
| Build cost (VND) | 86,000,000 | 109,060,000 | 111,500,000 | W5 scope costs; Base also links to existing B8 |
| Must-only contingency (VND) | 8,600,000 | 8,600,000 | 8,600,000 | 10% of Must cost as defined in W5 assumptions |
| Year-0 investment (VND) | 94,600,000 | 117,660,000 | 120,100,000 | Build cost + Must contingency |
| Benefit allocation / Base | 78.9% | 100.0% | 102.2% | Proxy: relative build cost vs. the Base scope |
| Year-1 gross annual benefit (VND) | 51,729,323 | 65,600,000 | 67,067,669 | Existing B11 × benefit allocation |
| Year-1 annual running cost (VND) | 12,900,000 | 16,359,000 | 16,725,000 | Existing B13 × benefit allocation |
<!-- END:drivers -->

_Benefit and running-cost allocations are proportional sensitivity proxies; confirm scenario-specific benefits before treating decisions as final._

## 3. Pessimistic: Must only | cash flow (VND)

<!-- BEGIN:pessimistic | derived - auto-generated, do not edit -->
| Line item (VND) | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| Benefits | 0 | 51,729,323 | 67,248,120 | 87,422,556 | 113,649,323 | 147,744,120 |
| Running cost | 0 | -12,900,000 | -13,326,990 | -13,768,113 | -14,223,838 | -14,694,647 |
| Investment (build + contingency) | -94,600,000 | 0 | 0 | 0 | 0 | 0 |
| Terminal / residual value | 0 | 0 | 0 | 0 | 0 | 0 |
| Net cash flow | -94,600,000 | 38,829,323 | 53,921,130 | 73,654,443 | 99,425,485 | 133,049,473 |
| Cumulative net cash flow | -94,600,000 | -55,770,677 | -1,849,546 | 71,804,897 | 171,230,382 | 304,279,855 |
| PV of net cash flow | -94,600,000 | 35,299,385 | 44,562,918 | 55,337,673 | 67,908,944 | 82,613,255 |
| Payback point (years) |  |  |  | 2.0251 |  |  |
<!-- END:pessimistic -->

## 3. Base: Must + Should | cash flow (VND)

<!-- BEGIN:base | derived - auto-generated, do not edit -->
| Line item (VND) | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| Benefits | 0 | 65,600,000 | 85,280,000 | 110,864,000 | 144,123,200 | 187,360,160 |
| Running cost | 0 | -16,359,000 | -16,900,483 | -17,459,889 | -18,037,811 | -18,634,863 |
| Investment (build + contingency) | -117,660,000 | 0 | 0 | 0 | 0 | 0 |
| Terminal / residual value | 0 | 0 | 0 | 0 | 0 | 0 |
| Net cash flow | -117,660,000 | 49,241,000 | 68,379,517 | 93,404,111 | 126,085,389 | 168,725,297 |
| Cumulative net cash flow | -117,660,000 | -68,419,000 | -39,483 | 93,364,628 | 219,450,017 | 388,175,314 |
| PV of net cash flow | -117,660,000 | 44,764,545 | 56,511,998 | 70,175,891 | 86,118,017 | 104,765,135 |
| Payback point (years) |  |  |  | 2.0004 |  |  |
<!-- END:base -->

## 3. Optimistic: full scope | cash flow (VND)

<!-- BEGIN:optimistic | derived - auto-generated, do not edit -->
| Line item (VND) | 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| Benefits | 0 | 67,067,669 | 87,187,970 | 113,344,361 | 147,347,669 | 191,551,970 |
| Running cost | 0 | -16,725,000 | -17,278,598 | -17,850,519 | -18,441,371 | -19,051,781 |
| Investment (build + contingency) | -120,100,000 | 0 | 0 | 0 | 0 | 0 |
| Terminal / residual value | 0 | 0 | 0 | 0 | 0 | 0 |
| Net cash flow | -120,100,000 | 50,342,669 | 69,909,372 | 95,493,842 | 128,906,298 | 172,500,189 |
| Cumulative net cash flow | -120,100,000 | -69,757,331 | 152,042 | 95,645,883 | 224,552,181 | 397,052,371 |
| PV of net cash flow | -120,100,000 | 45,766,063 | 57,776,341 | 71,745,937 | 88,044,736 | 107,109,046 |
| Payback point (years) |  |  | 1.9978 |  |  |  |
<!-- END:optimistic -->

## 4. Results | five-year scenario investment appraisal

<!-- BEGIN:results | derived - auto-generated, do not edit -->
| Metric | Pessimistic: Must only | Base: Must + Should | Optimistic: full scope |
|---|---|---|---|
| Year-0 investment (VND) | 94,600,000 | 117,660,000 | 120,100,000 |
| Year-1 gross benefit (VND) | 51,729,323 | 65,600,000 | 67,067,669 |
| Year-5 gross benefit (VND) | 147,744,120 | 187,360,160 | 191,551,970 |
| NPV at hurdle rate (VND) | 191,122,175 | 244,675,586 | 250,342,122 |
| IRR | 57.8% | 59.0% | 59.1% |
| Simple payback (years) | 2.0251 | 2.0004 | 1.9978 |
| Profitability index | 3.0203 | 3.0795 | 3.0844 |
| Decision signal | ACCEPT | ACCEPT | ACCEPT |
<!-- END:results -->

## 5. Reading the model

- The three MoSCoW cases use W5_Handover's Must, Must + Should and full-scope build costs, not LabDesk's sample VND figures.
- Existing CashFlow assumptions B7:B15 have been retained. Benefits use original Year-1 Base benefit and annual growth; costs use original recurring-cost assumption and annual growth.
- Must contingency equals the 10% assumption in W5_Handover and is added once in Year 0 for each scenario. No separate 20% Could money buffer is added.
- Pessimistic and Optimistic benefit and running-cost estimates are scaled proportionally to build cost. This is an illustrative sensitivity proxy, not separately validated revenue or savings.
- NPV = sum of discounted Year-0 to Year-5 net cash flows; IRR solves NPV = 0; simple payback interpolates the first positive cumulative cash flow; PI = 1 + NPV / Year-0 investment.
- ACCEPT when NPV is positive, IRR exceeds the existing hurdle rate and PI is greater than 1. Payback is shown separately; financial acceptance still requires validating project benefits.
