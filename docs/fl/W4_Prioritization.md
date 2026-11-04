# W4 — Repair and prioritise

> **Input**: Initial priority from W1, the defect log from W3, and the team capacity from Parameters.
>
> **Output**: An effective priority for every L2 function, each change carrying the rule it followed and a written justification. The effective priority flows back into W2_Costing and re-drives every total.
>
> **Procedure**: 1. Sort every W3 defect into one of three buckets: Fix now / Clarify / Reject. Rejecting is allowed, but the reason must be written down.
>  2. Repair STRUCTURE first: merge duplicates, add clock-triggered functions, add missing hidden work, split rows above the ceiling.
>  3. Recalculate and read the new numbers.
>  4. CUT: first move rows out to Won't-have, then demote Must -> Should -> Could. One sentence of justification per change.
>  5. Recalculate and confirm every threshold passes.
>
> **The Rule On The Board**: Cut by lowering priority, NEVER by lowering effort. Effort changes only when the technical scope of the row genuinely changes, and what was dropped must be written down.

<!-- Chỉ sửa trong các bảng 'input'. Phần giữa BEGIN/END sẽ được build.py ghi lại. -->

## Decision rules

<!-- BEGIN:rules | input table -->
| Rule | MoSCoW meaning | Test question |  | Kano category that usually maps here |
|---|---|---|---|---|
| R1 · Must | The release has no viable use without it | If it is absent on delivery day, is the release unusable? |  | Must-be — invisible when present, fatal when absent |
| R2 · Should | Important, but a workaround exists | Painful to leave out, yet the solution still works? |  | One-dimensional — more of it, more satisfaction |
| R3 · Could | Desirable, low impact if dropped | Would anyone notice within the first month? |  | Attractive — a delighter, never a Must |
| R4 · Won't | Agreed as out of scope for this release | Did the client accept deferring it, and is it in W0 Table 3? |  | Indifferent — asked for, but nobody actually cares |
<!-- END:rules -->

## Priority table

<!-- BEGIN:main | input table - computed columns (do not edit): A, B, C, D, H, J, K -->
| Feature | L2 ID | L2 function name | Initial priority | Rule applied | Kano category | New priority | Effective priority | Justification (required if changed) | Person-hours | Cost (VND) |
|---|---|---|---|---|---|---|---|---|---|---|
| F-01 | FR-01-01 | Submit supplier & raw material carbon data | Must |  |  |  | Must |  | 10.8 | 2,840,000 |
| F-01 | FR-01-02 | Manage GHG methodology & emission factors | Must |  |  |  | Must |  | 17.6 | 4,880,000 |
| F-01 | FR-01-03 | Calculate batch carbon intensity | Must |  |  |  | Must |  | 13.6 | 4,080,000 |
| F-01 | FR-01-04 | View batch carbon intensity | Should |  |  |  | Should |  | 7.4 | 1,820,000 |
| F-01 | FR-01-05 | Calculate shipment-level product carbon footprint | Must |  |  |  | Must |  | 17.6 | 4,880,000 |
| F-01 | FR-01-06 | Perform Scope 3 assessment | Should |  |  |  | Should |  | 17.6 | 4,880,000 |
| F-01 | FR-01-07 | Maintain carbon traceability linkage | Must |  |  |  | Must |  | 13.6 | 4,080,000 |
| F-01 | FR-01-08 | View carbon traceability record | Should |  |  |  | Should |  | 10.8 | 2,840,000 |
| F-02 | FR-02-01 | Load shipment inputs for CBAM estimation | Must |  |  |  | Must |  | 10.8 | 2,840,000 |
| F-02 | FR-02-02 | Validate CBAM calculation eligibility and inputs | Must |  |  |  | Must |  | 8.8 | 2,440,000 |
| F-02 | FR-02-03 | Calculate verified embedded emissions | Must |  |  |  | Must |  | 6.8 | 2,040,000 |
| F-02 | FR-02-04 | Determine CBAM-exempt emissions | Must |  |  |  | Must |  | 13.6 | 4,080,000 |
| F-02 | FR-02-05 | Calculate emissions subject to CBAM | Must |  |  |  | Must |  | 3.4 | 1,020,000 |
| F-02 | FR-02-06 | Retrieve applicable CBAM certificate price | Must |  |  |  | Must |  | 29.2 | 8,760,000 |
| F-02 | FR-02-07 | Recognize carbon price paid at origin | Must |  |  |  | Must |  | 13.6 | 4,080,000 |
| F-02 | FR-02-08 | Calculate estimated CBAM cost | Must |  |  |  | Must |  | 8.8 | 2,440,000 |
| F-02 | FR-02-09 | Generate CBAM calculation breakdown and assumptions | Must |  |  |  | Must |  | 10.8 | 2,840,000 |
| F-02 | FR-02-10 | Generate CBAM certificate price scenarios | Should |  |  |  | Should |  | 8.8 | 2,440,000 |
| F-02 | FR-02-11 | Display EU ETS certificate price trend | Should |  |  |  | Should |  | 15.2 | 4,160,000 |
| F-02 | FR-02-12 | Generate and download CBAM estimation report | Should |  |  |  | Should |  | 15.6 | 4,480,000 |
| F-02 | FR-02-13 | Share CBAM estimation result | Could |  |  |  | Could |  | 8.8 | 2,440,000 |
| F-02 | FR-02-14 | Display active and scheduled CBAM regulatory configuration | Must |  |  |  | Must |  | 7.4 | 1,820,000 |
| F-02 | FR-02-15 | Create or update a draft CBAM regulatory rule set | Must |  |  |  | Must |  | 10.8 | 2,840,000 |
| F-02 | FR-02-16 | Validate CBAM regulatory rules before activation | Must |  |  |  | Must |  | 8.8 | 2,440,000 |
| F-02 | FR-02-17 | Version and activate a CBAM regulatory rule set | Must |  |  |  | Must |  | 15.6 | 4,480,000 |
| F-03 | FR-03-01 | Filter green steel options | Must |  |  |  | Must |  | 3.4 | 1,020,000 |
| F-03 | FR-03-02 | Retrieve green steel profiles | Must |  |  |  | Must |  | 16 | 4,800,000 |
| F-03 | FR-03-03 | Evaluate and score options | Must |  |  |  | Must |  | 10.8 | 2,840,000 |
| F-03 | FR-03-04 | Generate recommendation | Must |  |  |  | Must |  | 5.4 | 1,420,000 |
| F-04 | FR-04-01 | Authenticate user login | Must |  |  |  | Must |  | 17.6 | 4,880,000 |
| F-04 | FR-04-02 | Configure RBAC permissions | Must |  |  |  | Must |  | 13.6 | 4,080,000 |
| F-04 | FR-04-03 | Authorize system actions | Must |  |  |  | Must |  | 6.8 | 2,040,000 |
| F-04 | FR-04-04 | Record system audit logs | Must |  |  |  | Must |  | 6.8 | 2,040,000 |
| F-04 | FR-04-05 | Export audit logs | Should |  |  |  | Should |  | 6.8 | 2,040,000 |
| F-04 | FR-04-06 | Export audit logs | Should |  |  |  | Should |  | 2 | 400,000 |
<!-- END:main -->

## Control panel

<!-- BEGIN:control | derived - auto-generated, do not edit -->
| Indicator | Current | Threshold | Verdict |
|---|---|---|---|
| Must share of in-scope effort | 76.5% | 60.0% | OVER THRESHOLD |
| Could share (contingency pool) | 2.2% | 20.0% | POOL TOO THIN |
| In-scope effort vs capacity (p-h) | 395 | 240 | OVER THRESHOLD |
| Expected cost (Must + Should) | 109,060,000 |  | The figure given to the client and used for NPV in Session 8 |
<!-- END:control -->
