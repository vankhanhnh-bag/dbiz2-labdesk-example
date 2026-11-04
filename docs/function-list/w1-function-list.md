# W1 Function List: LabDesk

> Worked example for teaching (LabDesk). Not a student submission and not a real product.

Lesson 5 (block W1). L2 = a business behaviour the client signs off, with its EARS criterion and function-point type. L3 = one work item in one layer (FE, BE, INT), sized S = 4 h, M = 8 h, L = 16 h. Initial priority is set here; the effective priority comes from [W4](w4-priorities.md).

Sources swept, one diagram per pass: Use Case, Sequence, Context, CVCA, Architecture + ADR.

## L2 functions

| Feature | L2 ID | L2 function name | Actor | EARS acceptance criterion | Source trace | Initial priority | FP type |
|---|---|---|---|---|---|---|---|
| F-00 | FR-00-01 | Sign in with the university account | Student, Lab Technician | WHEN a user opens LabDesk without a session, the system SHALL send them to the university sign-in page and start a session for the account that returns. | Context: University SSO; ADR-002 | Should | EQ |
| F-00 | FR-00-02 | Enforce user roles | System | IF a signed-in user who is not a Lab Technician opens a technician screen, THEN the system SHALL refuse access and show the student home page. | Use Case Diagram (two actors); ADR-002 | Should | NC |
| F-00 | FR-00-03 | Deploy automatically | System | WHEN a change is merged into the main branch, the system SHALL build it, run the tests and deploy it to the staging server. | Architecture; ADR-001 | Must | NC |
| F-00 | FR-00-04 | Record errors and alert the team | System | IF a request fails with a server error, THEN the system SHALL record the error and alert the integrator within 5 minutes. | Architecture | Must | NC |
| F-01 | FR-01-01 | Show time slots with free seats | Student | WHEN a student opens the booking page, the system SHALL display the labs and time slots of the next 7 days with the number of free seats in each. | UC:UC-01; Context: Student | Must | EQ |
| F-01 | FR-01-02 | Show the seat map | Student | WHEN a student selects a slot, the system SHALL display the seat map of that lab with each seat shown as free, booked or blocked. | UC:UC-01; SD-UC-01 | Must | EQ |
| F-01 | FR-01-03 | Save a booking | Student | WHEN a student confirms a free seat, the system SHALL save a booking for that student, slot and seat with status Confirmed. | UC:UC-01; SD-UC-01 | Must | EI |
| F-01 | FR-01-04 | Refuse a seat taken after the map loaded | System | IF the seat a student confirms was booked by someone else after the seat map was loaded, THEN the system SHALL reject the booking and reload the seat map with a message. | SD-UC-01 (alt: seat taken) | Must | NC |
| F-01 | FR-01-05 | Refuse a second booking in the same slot | System | IF a student who already holds a booking in a slot confirms another seat in the same slot, THEN the system SHALL reject the booking and show the existing one. | BR-01; UC:UC-01 | Must | NC |
| F-01 | FR-01-06 | Send the booking confirmation | Student | WHEN a booking is confirmed, the system SHALL send the student a confirmation email that contains a check-in QR code. | Context: Email service; ADR-003 | Must | EO |
| F-01 | FR-01-07 | Cancel a booking | Student | WHEN a student cancels a Confirmed booking before its slot starts, the system SHALL set the booking to Cancelled and free the seat. | UC:UC-02 | Must | EI |
| F-01 | FR-01-08 | View my bookings | Student | WHEN a student opens My bookings, the system SHALL list the student's bookings of today and the next 7 days with their status. | UC:UC-03 | Must | EQ |
| F-01 | FR-01-09 | Remind the student before the slot | Student | WHEN 30 minutes remain before a slot starts, the system SHALL email a reminder to every student with a Confirmed booking in that slot. | UC:UC-01 (team proposal) | Should | EO |
| F-01 | FR-01-10 | Add the booking to a calendar | Student | WHEN a student selects Add to calendar on a Confirmed booking, the system SHALL provide a calendar file with the lab, the seat and the slot time. | UC:UC-03 (team proposal) | Could | EO |
| F-01 | FR-01-11 | Show seat equipment on the seat map | Student | WHEN a student selects a seat on the seat map, the system SHALL show the equipment of that seat (screens, software installed). | UC:UC-01 (student survey in the user meeting) | Could | EQ |
| F-02 | FR-02-01 | Check in at the lab | Student | WHEN a student opens the check-in link of a lab between the start of a slot and 15 minutes after it, while holding a Confirmed booking for that lab and slot, the system SHALL set the booking to Checked-in. | UC:UC-04; SD-UC-04 | Must | EI |
| F-02 | FR-02-02 | Explain a failed check-in | Student | IF a student opens the check-in link without a Confirmed booking for that lab and slot, THEN the system SHALL show why check-in failed and list the student's bookings for today. | UC:UC-04 (alternative flow) | Must | EQ |
| F-02 | FR-02-03 | Refuse a late check-in | System | IF a student opens the check-in link more than 15 minutes after the slot started, THEN the system SHALL refuse the check-in and say that the seat was released. | BR-02; UC:UC-04 | Must | NC |
| F-02 | FR-02-04 | Release no-show seats | System | WHEN 15 minutes have passed since a slot started, the system SHALL set every booking of that slot that is still Confirmed to No-show and free its seat. | UC:UC-05 (added after Lesson 7); ADR-004 | Must | NC |
| F-02 | FR-02-05 | Send the no-show notice | Student | WHEN a booking becomes No-show, the system SHALL send the student a no-show notice. | UC:UC-05; Context: Email service | Must | EO |
| F-02 | FR-02-06 | Suspend booking rights after repeated no-shows | System | IF a student reaches 3 no-shows within 30 days, THEN the system SHALL suspend the student's booking rights for 7 days. | BR-04; UC:UC-05 | Should | NC |
| F-03 | FR-03-01 | Block a seat for maintenance | Lab Technician | WHEN a Lab Technician blocks a seat with a reason and a period, the system SHALL mark the seat Blocked for that period and refuse new bookings on it. | UC:UC-06; BR-03 | Should | EI |
| F-03 | FR-03-02 | Unblock a seat | Lab Technician | WHEN a Lab Technician unblocks a seat, the system SHALL make the seat bookable from that moment. | UC:UC-06 | Should | EI |
| F-03 | FR-03-03 | Warn students whose seat is blocked | Student | IF a seat is blocked while it holds Confirmed bookings, THEN the system SHALL cancel those bookings and email each student. | UC:UC-06; Context: Email service | Should | EO |
| F-03 | FR-03-04 | View lab occupancy | Lab Technician | WHEN a Lab Technician opens the occupancy page, the system SHALL show for each slot of today the number of booked, checked-in and free seats per lab. | UC:UC-07 | Should | EQ |
| F-03 | FR-03-05 | Export the monthly occupancy report | Lab Technician | WHEN a Lab Technician requests the report of a month, the system SHALL provide a spreadsheet with bookings, check-ins and no-shows per lab and slot. | UC:UC-07 (faculty request) | Could | EO |
| F-03 | FR-03-06 | Show the occupancy trend | Lab Technician | WHEN a Lab Technician opens the trend view, the system SHALL show the weekly occupancy rate of each lab over the last 8 weeks. | UC:UC-07 (team proposal) | Could | EO |

## L3 work items

| L3 ID | L2 ID | Layer | L3 work item | Size | Base hours | EARS precise? | Hidden work? |
|---|---|---|---|---|---|---|---|
| FR-00-01-FE | FR-00-01 | FE | Screen: sign-in page and session handling | S | 4 | Yes | No |
| FR-00-01-INT | FR-00-01 | INT | Integration: university SSO login and callback | M | 8 | Yes | No |
| FR-00-02-BE | FR-00-02 | BE | Role check on every technician route | S | 4 | Yes | Yes |
| FR-00-03-BE1 | FR-00-03 | BE | Pipeline: build, test and deploy to staging | M | 8 | Yes | Yes |
| FR-00-03-BE2 | FR-00-03 | BE | Daily database backup and a restore test | S | 4 | Yes | Yes |
| FR-00-04-BE | FR-00-04 | BE | Error logging and alert rule | S | 4 | Yes | Yes |
| FR-01-01-BE | FR-01-01 | BE | API: slots of the next 7 days with free-seat counts | S | 4 | Yes | No |
| FR-01-01-FE | FR-01-01 | FE | Screen: slot picker (S-F01-01) | S | 4 | Yes | No |
| FR-01-02-BE | FR-01-02 | BE | API: seat states for one slot | S | 4 | Yes | No |
| FR-01-02-FE | FR-01-02 | FE | Screen: seat map grid with seat states (S-F01-02) | M | 8 | Yes | No |
| FR-01-03-BE | FR-01-03 | BE | API: create booking | S | 4 | Yes | No |
| FR-01-03-FE | FR-01-03 | FE | Book-seat action and success state | S | 4 | Yes | No |
| FR-01-04-BE | FR-01-04 | BE | Re-check the seat inside the save transaction | M | 8 | Yes | No |
| FR-01-05-BE | FR-01-05 | BE | Check one booking per student per slot | S | 4 | Yes | No |
| FR-01-06-BE | FR-01-06 | BE | Generate the check-in QR token | S | 4 | Yes | No |
| FR-01-06-INT | FR-01-06 | INT | Integration: email service, confirmation message | M | 8 | Yes | No |
| FR-01-07-BE | FR-01-07 | BE | API: cancel booking and free the seat | S | 4 | Yes | No |
| FR-01-07-FE | FR-01-07 | FE | Cancel action with confirmation modal | S | 4 | Yes | No |
| FR-01-08-BE | FR-01-08 | BE | API: bookings of the signed-in student | S | 4 | Yes | No |
| FR-01-08-FE | FR-01-08 | FE | Screen: my bookings (S-F01-03) | S | 4 | Yes | No |
| FR-01-09-BE | FR-01-09 | BE | Job: find bookings 30 minutes before start | S | 4 | Yes | No |
| FR-01-09-INT | FR-01-09 | INT | Email service: reminder message | S | 4 | Yes | No |
| FR-01-10-BE | FR-01-10 | BE | API: calendar file for one booking | S | 4 | Yes | No |
| FR-01-10-FE | FR-01-10 | FE | Add-to-calendar action | S | 4 | Yes | No |
| FR-01-11-BE | FR-01-11 | BE | API: equipment of one seat | S | 4 | Yes | No |
| FR-01-11-FE | FR-01-11 | FE | Seat detail panel | S | 4 | Yes | No |
| FR-02-01-BE | FR-02-01 | BE | API: check in | S | 4 | Yes | No |
| FR-02-01-FE | FR-02-01 | FE | Screen: check-in result (S-F02-01) | S | 4 | Yes | No |
| FR-02-02-FE | FR-02-02 | FE | Error state with today's bookings | S | 4 | Yes | No |
| FR-02-03-BE | FR-02-03 | BE | Time-window check on check-in | S | 4 | Yes | No |
| FR-02-04-BE1 | FR-02-04 | BE | Job: release no-shows 15 minutes after start | M | 8 | Yes | No |
| FR-02-04-BE2 | FR-02-04 | BE | Scheduler set-up for timed jobs (ADR-004) | S | 4 | Yes | Yes |
| FR-02-05-INT | FR-02-05 | INT | Email service: no-show message | S | 4 | Yes | No |
| FR-02-06-BE | FR-02-06 | BE | Count no-shows and suspend booking rights | M | 8 | Yes | No |
| FR-03-01-BE | FR-03-01 | BE | API: block a seat for a period | S | 4 | Yes | No |
| FR-03-01-FE | FR-03-01 | FE | Screen: seat maintenance with block modal (S-F03-02) | M | 8 | Yes | No |
| FR-03-02-BE | FR-03-02 | BE | API: unblock a seat | S | 4 | Yes | No |
| FR-03-02-FE | FR-03-02 | FE | Unblock action | S | 4 | Yes | No |
| FR-03-03-BE | FR-03-03 | BE | Cancel bookings on a newly blocked seat | S | 4 | Yes | No |
| FR-03-03-INT | FR-03-03 | INT | Email service: seat-blocked message | S | 4 | Yes | No |
| FR-03-04-BE | FR-03-04 | BE | API: occupancy of today per lab and slot | S | 4 | Yes | No |
| FR-03-04-FE | FR-03-04 | FE | Screen: lab occupancy (S-F03-01) | M | 8 | Yes | No |
| FR-03-05-BE | FR-03-05 | BE | Report query and spreadsheet file | M | 8 | Yes | No |
| FR-03-05-FE | FR-03-05 | FE | Export action and month picker | S | 4 | Yes | No |
| FR-03-06-BE | FR-03-06 | BE | API: weekly occupancy rates | M | 8 | Yes | No |
| FR-03-06-FE | FR-03-06 | FE | Trend chart | M | 8 | Yes | No |

27 L2 functions, 46 L3 work items, 232 base hours. No row is above the 16-hour ceiling.

NC rows (FR-00-02, FR-00-03, FR-01-04, FR-02-04 ...) score zero function points but carry real work: that gap is why the function-point count is only a cross-check.
