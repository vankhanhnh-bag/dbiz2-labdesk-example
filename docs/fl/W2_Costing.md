# W2 — Costing, item by item

> **Input**: Every L3 row from W1, plus the rates and factors from Parameters. Nothing is typed on this sheet.
>
> **Output**: Cost of each L3 work item, a subtotal per L2 function, and a function-point cross-check of the whole estimate. These feed W2_Rollup.
>
> **Procedure**: The sheet is fully derived. The team's job is to READ it, in this order:
>  1. Find the most expensive L3 row. Is it expensive because it is large, or because it is hard?
>  2. Compare two rows with the same size label but different layers — the gap is the AI leverage effect.
>  3. Find a row where EARS precise? is No and read its verification hours.
>  4. Read the function-point cross-check at the bottom and explain the variance.
>
> **Teaching Point**: Flip one cell in W1 column M from Yes to No and watch the cost move. That is the cheapest possible proof that a vague specification is measurably more expensive.

<!-- Chỉ sửa trong các bảng 'input'. Phần giữa BEGIN/END sẽ được build.py ghi lại. -->

## Cost per L3 work item

<!-- BEGIN:l3 | derived - auto-generated, do not edit -->
| L3 ID | Feature | L2 ID | Layer | Base hours | AI factor | AI-adj. hours | Verif. factor | Verif. hours | Person-hours | Band | Rate | Cost (VND) | Effective priority |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| FR-01-01-FE | F-01 | FR-01-01 | FE | 16 | 0.35 | 5.6 | 0.15 | 2.4 | 8 | Junior | 200,000 | 1,600,000 | Should |
| FR-01-01-BE | F-01 | FR-01-01 | BE | 8 | 0.7 | 5.6 | 0.15 | 1.2 | 6.8 | Senior | 300,000 | 2,040,000 | Should |
| FR-01-02-FE | F-01 | FR-01-02 | FE | 8 | 0.35 | 2.8 | 0.15 | 1.2 | 4 | Junior | 200,000 | 800,000 | Must |
| FR-01-02-BE | F-01 | FR-01-02 | BE | 16 | 0.7 | 11.2 | 0.15 | 2.4 | 13.6 | Senior | 300,000 | 4,080,000 | Must |
| FR-01-03-BE | F-01 | FR-01-03 | BE | 16 | 0.7 | 11.2 | 0.15 | 2.4 | 13.6 | Senior | 300,000 | 4,080,000 | Must |
| FR-01-04-FE | F-01 | FR-01-04 | FE | 8 | 0.35 | 2.8 | 0.15 | 1.2 | 4 | Junior | 200,000 | 800,000 | Should |
| FR-01-04-BE | F-01 | FR-01-04 | BE | 4 | 0.7 | 2.8 | 0.15 | 0.6 | 3.4 | Senior | 300,000 | 1,020,000 | Should |
| FR-01-05-BE | F-01 | FR-01-05 | BE | 16 | 0.7 | 11.2 | 0.15 | 2.4 | 13.6 | Senior | 300,000 | 4,080,000 | Must |
| FR-01-05-FE | F-01 | FR-01-05 | FE | 8 | 0.35 | 2.8 | 0.15 | 1.2 | 4 | Junior | 200,000 | 800,000 | Must |
| FR-01-06-BE | F-01 | FR-01-06 | BE | 16 | 0.7 | 11.2 | 0.15 | 2.4 | 13.6 | Senior | 300,000 | 4,080,000 | Should |
| FR-01-06-FE | F-01 | FR-01-06 | FE | 8 | 0.35 | 2.8 | 0.15 | 1.2 | 4 | Junior | 200,000 | 800,000 | Should |
| FR-01-07-BE | F-01 | FR-01-07 | BE | 16 | 0.7 | 11.2 | 0.15 | 2.4 | 13.6 | Senior | 300,000 | 4,080,000 | Must |
| FR-01-08-FE | F-01 | FR-01-08 | FE | 8 | 0.35 | 2.8 | 0.15 | 1.2 | 4 | Junior | 200,000 | 800,000 | Should |
| FR-01-08-BE | F-01 | FR-01-08 | BE | 8 | 0.7 | 5.6 | 0.15 | 1.2 | 6.8 | Senior | 300,000 | 2,040,000 | Should |
| FR-02-01-FE | F-02 | FR-02-01 | FE | 8 | 0.35 | 2.8 | 0.15 | 1.2 | 4 | Junior | 200,000 | 800,000 | Must |
| FR-02-01-BE | F-02 | FR-02-01 | BE | 8 | 0.7 | 5.6 | 0.15 | 1.2 | 6.8 | Senior | 300,000 | 2,040,000 | Must |
| FR-02-02-BE | F-02 | FR-02-02 | BE | 8 | 0.7 | 5.6 | 0.15 | 1.2 | 6.8 | Senior | 300,000 | 2,040,000 | Must |
| FR-02-02-FE | F-02 | FR-02-02 | FE | 4 | 0.35 | 1.4 | 0.15 | 0.6 | 2 | Junior | 200,000 | 400,000 | Must |
| FR-02-03-BE | F-02 | FR-02-03 | BE | 8 | 0.7 | 5.6 | 0.15 | 1.2 | 6.8 | Senior | 300,000 | 2,040,000 | Must |
| FR-02-04-BE | F-02 | FR-02-04 | BE | 16 | 0.7 | 11.2 | 0.15 | 2.4 | 13.6 | Senior | 300,000 | 4,080,000 | Must |
| FR-02-05-BE | F-02 | FR-02-05 | BE | 4 | 0.7 | 2.8 | 0.15 | 0.6 | 3.4 | Senior | 300,000 | 1,020,000 | Must |
| FR-02-06-INT | F-02 | FR-02-06 | INT | 16 | 1 | 16 | 0.4 | 6.4 | 22.4 | Senior | 300,000 | 6,720,000 | Must |
| FR-02-06-BE | F-02 | FR-02-06 | BE | 8 | 0.7 | 5.6 | 0.15 | 1.2 | 6.8 | Senior | 300,000 | 2,040,000 | Must |
| FR-02-07-BE | F-02 | FR-02-07 | BE | 16 | 0.7 | 11.2 | 0.15 | 2.4 | 13.6 | Senior | 300,000 | 4,080,000 | Must |
| FR-02-08-BE | F-02 | FR-02-08 | BE | 8 | 0.7 | 5.6 | 0.15 | 1.2 | 6.8 | Senior | 300,000 | 2,040,000 | Must |
| FR-02-08-FE | F-02 | FR-02-08 | FE | 4 | 0.35 | 1.4 | 0.15 | 0.6 | 2 | Junior | 200,000 | 400,000 | Must |
| FR-02-09-BE | F-02 | FR-02-09 | BE | 8 | 0.7 | 5.6 | 0.15 | 1.2 | 6.8 | Senior | 300,000 | 2,040,000 | Must |
| FR-02-09-FE | F-02 | FR-02-09 | FE | 8 | 0.35 | 2.8 | 0.15 | 1.2 | 4 | Junior | 200,000 | 800,000 | Must |
| FR-02-10-BE | F-02 | FR-02-10 | BE | 8 | 0.7 | 5.6 | 0.15 | 1.2 | 6.8 | Senior | 300,000 | 2,040,000 | Should |
| FR-02-10-FE | F-02 | FR-02-10 | FE | 4 | 0.35 | 1.4 | 0.15 | 0.6 | 2 | Junior | 200,000 | 400,000 | Should |
| FR-02-11-INT | F-02 | FR-02-11 | INT | 8 | 1 | 8 | 0.4 | 3.2 | 11.2 | Senior | 300,000 | 3,360,000 | Should |
| FR-02-11-FE | F-02 | FR-02-11 | FE | 8 | 0.35 | 2.8 | 0.15 | 1.2 | 4 | Junior | 200,000 | 800,000 | Should |
| FR-02-12-BE | F-02 | FR-02-12 | BE | 16 | 0.7 | 11.2 | 0.15 | 2.4 | 13.6 | Senior | 300,000 | 4,080,000 | Should |
| FR-02-12-FE | F-02 | FR-02-12 | FE | 4 | 0.35 | 1.4 | 0.15 | 0.6 | 2 | Junior | 200,000 | 400,000 | Should |
| FR-02-13-BE | F-02 | FR-02-13 | BE | 8 | 0.7 | 5.6 | 0.15 | 1.2 | 6.8 | Senior | 300,000 | 2,040,000 | Could |
| FR-02-13-FE | F-02 | FR-02-13 | FE | 4 | 0.35 | 1.4 | 0.15 | 0.6 | 2 | Junior | 200,000 | 400,000 | Could |
| FR-02-14-FE | F-02 | FR-02-14 | FE | 8 | 0.35 | 2.8 | 0.15 | 1.2 | 4 | Junior | 200,000 | 800,000 | Must |
| FR-02-14-BE | F-02 | FR-02-14 | BE | 4 | 0.7 | 2.8 | 0.15 | 0.6 | 3.4 | Senior | 300,000 | 1,020,000 | Must |
| FR-02-15-FE | F-02 | FR-02-15 | FE | 8 | 0.35 | 2.8 | 0.15 | 1.2 | 4 | Junior | 200,000 | 800,000 | Must |
| FR-02-15-BE | F-02 | FR-02-15 | BE | 8 | 0.7 | 5.6 | 0.15 | 1.2 | 6.8 | Senior | 300,000 | 2,040,000 | Must |
| FR-02-16-BE | F-02 | FR-02-16 | BE | 8 | 0.7 | 5.6 | 0.15 | 1.2 | 6.8 | Senior | 300,000 | 2,040,000 | Must |
| FR-02-16-FE | F-02 | FR-02-16 | FE | 4 | 0.35 | 1.4 | 0.15 | 0.6 | 2 | Junior | 200,000 | 400,000 | Must |
| FR-02-17-BE | F-02 | FR-02-17 | BE | 16 | 0.7 | 11.2 | 0.15 | 2.4 | 13.6 | Senior | 300,000 | 4,080,000 | Must |
| FR-02-17-FE | F-02 | FR-02-17 | FE | 4 | 0.35 | 1.4 | 0.15 | 0.6 | 2 | Junior | 200,000 | 400,000 | Must |
| FR-03-01-BE | F-03 | FR-03-01 | BE | 4 | 0.7 | 2.8 | 0.15 | 0.6 | 3.4 | Senior | 300,000 | 1,020,000 | Must |
| FR-03-02-BE | F-03 | FR-03-02 | BE | 8 | 0.7 | 5.6 | 0.15 | 1.2 | 6.8 | Senior | 300,000 | 2,040,000 | Must |
| FR-03-02-INT | F-03 | FR-03-02 | INT | 8 | 1 | 8 | 0.15 | 1.2 | 9.2 | Senior | 300,000 | 2,760,000 | Must |
| FR-03-03-BE | F-03 | FR-03-03 | BE | 8 | 0.7 | 5.6 | 0.15 | 1.2 | 6.8 | Senior | 300,000 | 2,040,000 | Must |
| FR-03-03-FE | F-03 | FR-03-03 | FE | 8 | 0.35 | 2.8 | 0.15 | 1.2 | 4 | Junior | 200,000 | 800,000 | Must |
| FR-03-04-BE | F-03 | FR-03-04 | BE | 4 | 0.7 | 2.8 | 0.15 | 0.6 | 3.4 | Senior | 300,000 | 1,020,000 | Must |
| FR-03-04-FE | F-03 | FR-03-04 | FE | 4 | 0.35 | 1.4 | 0.15 | 0.6 | 2 | Junior | 200,000 | 400,000 | Must |
| FR-04-01-BE | F-04 | FR-04-01 | BE | 16 | 0.7 | 11.2 | 0.15 | 2.4 | 13.6 | Senior | 300,000 | 4,080,000 | Must |
| FR-04-01-FE | F-04 | FR-04-01 | FE | 8 | 0.35 | 2.8 | 0.15 | 1.2 | 4 | Junior | 200,000 | 800,000 | Must |
| FR-04-02-BE | F-04 | FR-04-02 | BE | 8 | 0.7 | 5.6 | 0.15 | 1.2 | 6.8 | Senior | 300,000 | 2,040,000 | Must |
| FR-04-02-BE | F-04 | FR-04-02 | BE | 8 | 0.7 | 5.6 | 0.15 | 1.2 | 6.8 | Senior | 300,000 | 2,040,000 | Must |
| FR-04-03-BE | F-04 | FR-04-03 | BE | 8 | 0.7 | 5.6 | 0.15 | 1.2 | 6.8 | Senior | 300,000 | 2,040,000 | Must |
| FR-04-04-BE | F-04 | FR-04-04 | BE | 8 | 0.7 | 5.6 | 0.15 | 1.2 | 6.8 | Senior | 300,000 | 2,040,000 | Must |
| FR-04-05-BE | F-04 | FR-04-05 | BE | 8 | 0.7 | 5.6 | 0.15 | 1.2 | 6.8 | Senior | 300,000 | 2,040,000 | Should |
| FR-04-06-FE | F-04 | FR-04-06 | FE | 4 | 0.35 | 1.4 | 0.15 | 0.6 | 2 | Junior | 200,000 | 400,000 | Should |
| TOTAL |  |  |  | 512 |  | 316.2 |  | 82.8 | 399 |  |  | 112,300,000 |  |
<!-- END:l3 -->

## Cost per L2 function

<!-- BEGIN:l2 | derived - auto-generated, do not edit -->
| L2 ID | L2 function name | Feature | FP type | L3 items | Person-hours | Cost (VND) | Effective priority |
|---|---|---|---|---|---|---|---|
| FR-01-01 | Submit supplier & raw material carbon data | F-01 | EI | 2 | 14.8 | 3,640,000 | Should |
| FR-01-02 | Manage GHG methodology & emission factors | F-01 | EI | 2 | 17.6 | 4,880,000 | Must |
| FR-01-03 | Calculate batch carbon intensity | F-01 | EO | 1 | 13.6 | 4,080,000 | Must |
| FR-01-04 | View batch carbon intensity | F-01 | EQ | 2 | 7.4 | 1,820,000 | Should |
| FR-01-05 | Calculate shipment-level product carbon footprint | F-01 | EO | 2 | 17.6 | 4,880,000 | Must |
| FR-01-06 | Perform Scope 3 assessment | F-01 | EO | 2 | 17.6 | 4,880,000 | Should |
| FR-01-07 | Maintain carbon traceability linkage | F-01 | NC | 1 | 13.6 | 4,080,000 | Must |
| FR-01-08 | View carbon traceability record | F-01 | EQ | 2 | 10.8 | 2,840,000 | Should |
| FR-02-01 | Load shipment inputs for CBAM estimation | F-02 | EQ | 2 | 10.8 | 2,840,000 | Must |
| FR-02-02 | Validate CBAM calculation eligibility and inputs | F-02 | NC | 2 | 8.8 | 2,440,000 | Must |
| FR-02-03 | Calculate verified embedded emissions | F-02 | EO | 1 | 6.8 | 2,040,000 | Must |
| FR-02-04 | Determine CBAM-exempt emissions | F-02 | EO | 1 | 13.6 | 4,080,000 | Must |
| FR-02-05 | Calculate emissions subject to CBAM | F-02 | EO | 1 | 3.4 | 1,020,000 | Must |
| FR-02-06 | Retrieve applicable CBAM certificate price | F-02 | EQ | 2 | 29.2 | 8,760,000 | Must |
| FR-02-07 | Recognize carbon price paid at origin | F-02 | EO | 1 | 13.6 | 4,080,000 | Must |
| FR-02-08 | Calculate estimated CBAM cost | F-02 | EO | 2 | 8.8 | 2,440,000 | Must |
| FR-02-09 | Generate CBAM calculation breakdown and assumptions | F-02 | EO | 2 | 10.8 | 2,840,000 | Must |
| FR-02-10 | Generate CBAM certificate price scenarios | F-02 | EO | 2 | 8.8 | 2,440,000 | Should |
| FR-02-11 | Display EU ETS certificate price trend | F-02 | EQ | 2 | 15.2 | 4,160,000 | Should |
| FR-02-12 | Generate and download CBAM estimation report | F-02 | EO | 2 | 15.6 | 4,480,000 | Should |
| FR-02-13 | Share CBAM estimation result | F-02 | EO | 2 | 8.8 | 2,440,000 | Could |
| FR-02-14 | Display active and scheduled CBAM regulatory configuration | F-02 | EQ | 2 | 7.4 | 1,820,000 | Must |
| FR-02-15 | Create or update a draft CBAM regulatory rule set | F-02 | EI | 2 | 10.8 | 2,840,000 | Must |
| FR-02-16 | Validate CBAM regulatory rules before activation | F-02 | NC | 2 | 8.8 | 2,440,000 | Must |
| FR-02-17 | Version and activate a CBAM regulatory rule set | F-02 | EI | 2 | 15.6 | 4,480,000 | Must |
| FR-03-01 | Filter green steel options | F-03 | EI | 1 | 3.4 | 1,020,000 | Must |
| FR-03-02 | Retrieve green steel profiles | F-03 | EQ | 2 | 16 | 4,800,000 | Must |
| FR-03-03 | Evaluate and score options | F-03 | EO | 2 | 10.8 | 2,840,000 | Must |
| FR-03-04 | Generate recommendation | F-03 | EO | 2 | 5.4 | 1,420,000 | Must |
| FR-04-01 | Authenticate user login | F-04 | EI | 2 | 17.6 | 4,880,000 | Must |
| FR-04-02 | Configure RBAC permissions | F-04 | EI | 2 | 13.6 | 4,080,000 | Must |
| FR-04-03 | Authorize system actions | F-04 | EI | 1 | 6.8 | 2,040,000 | Must |
| FR-04-04 | Record system audit logs | F-04 | EI | 1 | 6.8 | 2,040,000 | Must |
| FR-04-05 | Export audit logs | F-04 | EO | 1 | 6.8 | 2,040,000 | Should |
| FR-04-06 | Export audit logs | F-04 | EO | 1 | 2 | 400,000 | Should |
<!-- END:l2 -->

## Function-point cross-check

<!-- BEGIN:fp_check | derived - auto-generated, do not edit -->
| Item | Value | Note |
|---|---|---|
| Transactional function points (EI / EO / EQ) | 144 | Counted once per L2 row, from W1 column Q |
| Data function points (ILF / EIF) | 58 | From W0 Table 4 — counted once for the whole product |
| Unadjusted function points | 202 | Transactional + data |
| Hours per FP (class parameter) | 3 | Pre-AI gross hours |
| Functional work — function-point estimate (h) | 606 | What function points can see |
| Non-functional (NC) work — bottom-up (h) | 40 | The 0 function point problem: concurrency, authorisation, deployment. IFPUG needs a separate method (SNAP) for this |
| Function-point basis total (h) | 646 | Functional + non-functional |
| Bottom-up basis total (h) | 512 | Sum of W1 column L |
| Variance | -20.7% | Within tolerance - the two methods agree |
| Active estimation basis | Bottom-up | Set on Parameters section 9 |
| Base hours actually in use | 512 | What the cost columns are built from right now |
<!-- END:fp_check -->

_Read it this way: function points size the FUNCTIONAL work only, so the NC line is added separately rather than folded in. Switching the basis on Parameters section 9 changes which of the two totals drives every cost in the workbook; NC rows stay on bottom-up either way, because there is no function-point number for them to come from._
