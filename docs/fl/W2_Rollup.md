# W2 — Roll-up and threshold check

> **Input**: W2_Costing, which reads W1 and W4. Nothing is typed here except the three shared observations at the bottom.
>
> **Output**: Per-feature totals, the three headline figures for Session 8, and a pass/fail on every threshold — shown twice: as first written in W1, and after the W4 decisions.
>
> **Procedure**: 1. The integrator merges the branches and commits.
>  2. Recalculate. Fix nothing yet.
>  3. Just observe and assess whether the cost analysis is good enough

<!-- Chỉ sửa trong các bảng 'input'. Phần giữa BEGIN/END sẽ được build.py ghi lại. -->

## Per feature (effective priority, after W4)

<!-- BEGIN:features | derived - auto-generated, do not edit -->
| Feature | Name | L2 | L3 | Base h (in use) | Must (p-h) | Should | Could | Won't | In-scope p-h | In-scope cost | Must % | Bottom-up h | Transactional FP | Bottom-up h per FP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F-01 | Carbon Traceability & Product Carbon Footprint Management | 8 | 14 | 156 | 62.4 | 50.6 | 0 | 0 | 113 | 31,100,000 | 55.2% | 156 | 31 | 5.0323 |
| F-02 | CBAM Compliance & Carbon Cost Estimation | 17 | 30 | 240 | 137.6 | 39.6 | 17.6 | 0 | 194.8 | 55,240,000 | 70.6% | 240 | 69 | 3.4783 |
| F-03 | Green Steel Comparison & Recommendation | 4 | 7 | 44 | 35.6 | 0 | 0 | 0 | 35.6 | 10,080,000 | 100.0% | 44 | 18 | 2.4444 |
| F-04 | Platform, Access & Operations | 6 | 8 | 68 | 44.8 | 8.8 | 0 | 0 | 53.6 | 15,480,000 | 83.6% | 68 | 26 | 2.6154 |
|  | PROJECT TOTAL | 35 | 59 | 508 | 280.4 | 99 | 17.6 | 0 | 397 | 111,900,000 | 70.6% | 508 | 144 | 3.5278 |
<!-- END:features -->

_Columns M-O compare the two sizing methods FEATURE BY FEATURE. Data functions (ILF / EIF) are counted once for the whole product, so column N holds transactional function points only — read column O as a RELATIVE figure. Features should cluster around a similar hours-per-FP ratio; the one sitting far from its siblings is where somebody mis-sized something, or where NC rows are carrying work that function points cannot see._

## The three headline figures

<!-- BEGIN:headline | derived - auto-generated, do not edit -->
| Scenario | Scope | Person-hours | Cost (VND) | Meaning |
|---|---|---|---|---|
| Committed | Must only | 280.4 | 80,320,000 | What the team guarantees to deliver — the Minimum Usable SubseT |
| Expected | Must + Should | 379.4 | 107,020,000 | The figure given to the client; the base cash flow for Session 8 |
| Ceiling | Must + Should + Could | 397 | 111,900,000 | If the Could contingency pool is never consumed |
<!-- END:headline -->

## Threshold check

<!-- BEGIN:thresholds | derived - auto-generated, do not edit -->
| Indicator | As written | After W4 | Threshold | Verdict (after W4) |
|---|---|---|---|---|
| Must share of in-scope effort | 74.1% | 70.6% | 60.0% | ABOVE CEILING - demote some Must rows |
| Could share (contingency pool) | 2.7% | 4.4% | 20.0% | POOL TOO THIN - nothing left to drop when late |
| In-scope effort vs team capacity (p-h) | 397 | 397 | 240 | OVER CAPACITY |
| Hidden technical work, share of effort | 63.2% | 63.2% | 10.0% | PASS |
| L3 rows above the hour ceiling | 0 | 0 | 0 | PASS |
| Feature count | 4 | 4 | 3-6 | PASS |
<!-- END:thresholds -->

## Three observations the team carries into W4

1. 
2. 
3.
