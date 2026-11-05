# Parameters — Fixed for the whole class

> **Input**: Labour-market data, productivity assumptions and the team capacity, fixed for the whole cohort.
>
> **Output**: Every derived number in W1, W2, W4 and W5 traces back to a cell on this sheet.
>
> **Why Fixed**: If each team invented its own rates the exercise would test guessing rather than the model, and results would not be comparable at marking. The point of a published parameter is that the subjectivity sits in ONE auditable place instead of forty scattered ones.

<!-- Chỉ sửa trong các bảng 'input'. Phần giữa BEGIN/END sẽ được build.py ghi lại. -->

## 1. Effort size to base hours

<!-- BEGIN:sizes | input table -->
| Size | Hours |  | Note |
|---|---|---|---|
| S | 4 |  | Ceiling for one L3 row is 16 h — above that it is not yet an L3 row |
| M | 8 |  | Matches the test: ask a developer; an answer of 4–16 h is correct granularity |
| L | 16 |  |  |
<!-- END:sizes -->

## 2. Technical layer to AI leverage and default seniority

<!-- BEGIN:layers | input table -->
| Layer | AI leverage factor | Default band | Note |
|---|---|---|---|
| FE | 0.35 | Junior | Screens, forms, repeated patterns — AI generates these well |
| BE | 0.7 | Senior | Business logic, state, concurrency |
| INT | 1 | Senior | Third-party APIs, credentials, sandboxes — AI helps least here |
<!-- END:layers -->

## 3. Hourly cost by seniority band (VND / hour)

<!-- BEGIN:rates | input table -->
| Band | Rate |  | Source |
|---|---|---|---|
| Junior | 200000 |  | ITviec 2025-26 median 25.35m VND/month x 1.35 overhead / 176 h |
| Senior | 300000 |  | ITviec 2025-26 median 39.9m VND/month x 1.35 / 176 h |
| Expert | 400000 |  | ITviec 2025-26 median 54.9m VND/month x 1.35 / 176 h |
<!-- END:rates -->

## 4. Verification factor

<!-- BEGIN:verification | input table -->
| EARS precise? | Factor |  | Note |
|---|---|---|---|
| Yes | 0.15 |  | Clear criteria — fast to verify, often automatable |
| No | 0.4 |  | Vague criteria — a person must reason the answer out from scratch |
<!-- END:verification -->

## 5. Function point weights

<!-- BEGIN:fp_weights | input table -->
| FP type | Weight |  | What it counts |
|---|---|---|---|
| EI | 4 |  | External Input — data crosses the boundary inward and changes stored data |
| EO | 5 |  | External Output — data leaves the boundary WITH derived values or calculation |
| EQ | 4 |  | External inQuiry — retrieval only, no derived data, nothing stored changes |
| ILF | 10 |  | Internal Logical File — a group of data the system itself maintains |
| EIF | 7 |  | External Interface File — data the system reads but never maintains |
| NC | 0 |  | Not countable — a business rule or non-functional item inside another transaction |
| Hours per unadjusted function point | 3 |  | Class parameter, PRE-AI gross hours. Published industry figures range very widely; calibrate this from your own delivered projects rather than importing a benchmark |
<!-- END:fp_weights -->

## 6. Team capacity for DBIZ3

<!-- BEGIN:capacity | input table -->
| Item | Value |
|---|---|
| Team members | 4 |
| Weeks | 12 |
| Productive hours per person per week | 5 |
| Total capacity (person-hours) | 240 |
<!-- END:capacity -->

## 7. Thresholds

<!-- BEGIN:thresholds | input table -->
| Item | Value |
|---|---|
| Must, maximum share of scope effort | 0.6 |
| Could, target share of scope effort | 0.2 |
| Hidden technical work, minimum share | 0.1 |
| Maximum hours for one L3 row | 16 |
| Minimum number of features | 3 |
| Maximum number of features | 6 |
| Estimate variance that triggers a review | 0.3 |
<!-- END:thresholds -->

## 9. Estimation basis (Bottom-up | Function-point)

<!-- BEGIN:basis | input table -->
| Item | Value |
|---|---|
| Estimation basis | Bottom-up |
<!-- END:basis -->
