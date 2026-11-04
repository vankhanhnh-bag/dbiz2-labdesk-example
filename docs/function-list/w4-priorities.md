# W4 Priorities: LabDesk

> Worked example for teaching (LabDesk). Not a student submission and not a real product.

Lesson 5 (block W4). Cut by lowering priority, never by lowering estimates. Every change names its rule.

| Rule | MoSCoW meaning | Test question |
|---|---|---|
| R1 Must | The release has no viable use without it | If it is absent on delivery day, is the release useless? |
| R2 Should | Important, but a workaround exists | Painful to leave out, yet the solution still works? |
| R3 Could | Desirable, low impact if dropped | Would anyone notice within the first month? |
| R4 Won't | Agreed out of scope for this release | Did the client accept deferring it? |

| Feature | L2 ID | L2 function name | Initial priority | Effective priority | Justification (required if changed) | Person-hours | Cost (VND) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| F-00 | FR-00-01 | Sign in with the university account | Must | Must |  | 11.2 | 3.160.000 |
| F-00 | FR-00-02 | Enforce user roles | Must | Must |  | 3.4 | 1.020.000 |
| F-00 | FR-00-03 | Deploy automatically | Must | Must |  | 10.2 | 3.060.000 |
| F-00 | FR-00-04 | Record errors and alert the team | Must | Should | R2: the team can read server logs by hand during the first weeks; painful, not fatal. | 3.4 | 1.020.000 |
| F-01 | FR-01-01 | Show time slots with free seats | Must | Must |  | 5.4 | 1.420.000 |
| F-01 | FR-01-02 | Show the seat map | Must | Must |  | 7.4 | 1.820.000 |
| F-01 | FR-01-03 | Save a booking | Must | Must |  | 5.4 | 1.420.000 |
| F-01 | FR-01-04 | Refuse a seat taken after the map loaded | Must | Must |  | 6.8 | 2.040.000 |
| F-01 | FR-01-05 | Refuse a second booking in the same slot | Must | Must |  | 3.4 | 1.020.000 |
| F-01 | FR-01-06 | Send the booking confirmation | Must | Must |  | 12.6 | 3.780.000 |
| F-01 | FR-01-07 | Cancel a booking | Must | Must |  | 5.4 | 1.420.000 |
| F-01 | FR-01-08 | View my bookings | Must | Must |  | 5.4 | 1.420.000 |
| F-01 | FR-01-09 | Remind the student before the slot | Should | Could | R3: nobody would notice its absence in the first month; the confirmation email already carries the time. | 8.0 | 2.400.000 |
| F-01 | FR-01-10 | Add the booking to a calendar | Could | Could |  | 5.4 | 1.420.000 |
| F-01 | FR-01-11 | Show seat equipment on the seat map | Could | Could |  | 5.4 | 1.420.000 |
| F-02 | FR-02-01 | Check in at the lab | Must | Must |  | 5.4 | 1.420.000 |
| F-02 | FR-02-02 | Explain a failed check-in | Must | Must |  | 2.0 | 400.000 |
| F-02 | FR-02-03 | Refuse a late check-in | Must | Must |  | 3.4 | 1.020.000 |
| F-02 | FR-02-04 | Release no-show seats | Must | Must |  | 10.2 | 3.060.000 |
| F-02 | FR-02-05 | Send the no-show notice | Must | Should | R2: My bookings already shows the No-show status; the email is a courtesy with a workaround. | 4.6 | 1.380.000 |
| F-02 | FR-02-06 | Suspend booking rights after repeated no-shows | Should | Should |  | 6.8 | 2.040.000 |
| F-03 | FR-03-01 | Block a seat for maintenance | Should | Should |  | 7.4 | 1.820.000 |
| F-03 | FR-03-02 | Unblock a seat | Should | Should |  | 5.4 | 1.420.000 |
| F-03 | FR-03-03 | Warn students whose seat is blocked | Should | Should |  | 8.0 | 2.400.000 |
| F-03 | FR-03-04 | View lab occupancy | Should | Should |  | 7.4 | 1.820.000 |
| F-03 | FR-03-05 | Export the monthly occupancy report | Could | Could |  | 8.8 | 2.440.000 |
| F-03 | FR-03-06 | Show the occupancy trend | Could | Could |  | 10.8 | 2.840.000 |
