# W0 — Establish scope and split into features

> **Input**: The Use Case Diagram, the CVCA and the Context Diagram, updated after the user meeting. Every diagram element must already carry an ID.
>
> **Output**: (a) a complete use-case inventory, (b) a small set of features, each a folder under specs/, (c) an explicit Won't-have list, (d) the data functions the system maintains or reads. Feature IDs feed column A of W1.
>
> **Procedure**: 1. List EVERY use case in Table 1 — names only, no discussion yet.
>  2. Cluster them into features in Table 2. A feature name is a business noun the client recognises, never a screen name or a technical module.
>  3. Coverage check against the CVCA: every primary actor must be served by at least one feature.
>  4. Record anything excluded in Table 3, with the reason.
>  5. In Table 4, list the data the system MAINTAINS (ILF) and the data it only READS from another system (EIF). Read these off the Context Diagram boundary.
>
> **Rule**: Merge any feature expected to hold fewer than 3 L2 rows. A feature that no use case and no CVCA flow points at does not belong in the release.

<!-- Chỉ sửa trong các bảng 'input'. Phần giữa BEGIN/END sẽ được build.py ghi lại. -->

## Table 1 · Use case inventory

<!-- BEGIN:uc | input table -->
| Use case ID | Use case name | Primary actor | Assigned feature |
|---|---|---|---|
| UC-01 | Submit production & energy data | Production Dep. | F-01 |
| UC-02 | Manage GHG methodology & emission factors | Sustainability & ESG Dep. | F-01 |
| UC-03 | Access batch carbon intensity         | Production Dep. | F-01 |
| UC-04 | Calculate shipment-level PCF | Export Sales & Marketing | F-01 |
| UC-05 | Perform Scope 3 assessment | Procurement Dep. | F-01 |
| UC-06 | View carbon traceability record         | Sustainability & ESG Dep. | F-01 |
| UC-07 | Estimate & analyze CBAM exposure for shipment | Export Sales & Marketing Dep.; Procurement & Raw Materials Dep. | F-02 |
| UC-08 | Manage CBAM regulatory rules & parameters | Compliance / Product Owner | F-02 |
| UC-09 | Compare and recommend green steel options | Customer | F-03 |
| UC-10 | Authenticate and sign in to the platform | All Users | F-04 |
| UC-11 | Configure Role-Based Access Control (RBAC) and system authorization | System Admin | F-04 |
| UC-12 | Monitor, track, and export system audit logs | System Admin / Auditor | F-04 |
<!-- END:uc -->

## Table 1 · checks

<!-- BEGIN:uc_check | derived - auto-generated, do not edit -->
| Item | Value |
|---|---|
| Use cases listed | 12 |
| Assignment check | All assigned |
<!-- END:uc_check -->

## Table 2 · Feature list (flows into W1)

<!-- BEGIN:features | input table -->
| Feature ID | Feature name (business noun) | Scope in one sentence | Primary actors served | Owner | Use cases covered |
|---|---|---|---|---|---|
| F-01 | Carbon Traceability & Product Carbon Footprint Management | Consolidate production, supplier, energy and shipment data to calculate and trace carbon footprint from raw material through to a shipped product batch. | - Production Department<br>- Procurement Department <br>- Sustainability & ESG Department<br>- Export Sales & Marketing  |  | UC-01; UC-02; UC-03; UC-04; UC-05; UC-06 |
| F-02 | CBAM Compliance & Carbon Cost Estimation | Estimate CBAM exposure per shipment, share results, and manage regulatory parameters | - Export Sales & Marketing<br>- Procurement & Raw Materials<br>- Compliance / Product Owner |  | UC-07, UC-08 |
| F-03 | Green Steel Comparison & Recommendation | Compare green steel options based on carbon, cost, technical, supplier, CBAM and other decision criteria, evaluate trade-offs, and generate an explained recommendation. | Customers  |  | UC-09 |
| F-04 | Platform, Access & Operations | Sign-in, authorisation, deployment, audit log | All users |  | UC-10, UC-11,.UC-12 |
<!-- END:features -->

## Table 2 · checks

<!-- BEGIN:features_check | derived - auto-generated, do not edit -->
| Item | Value |
|---|---|
| Feature count | 4 |
| Feature count check | PASS |
<!-- END:features_check -->

## Table 3 · Won't-have

<!-- BEGIN:wont | input table -->
| Excluded from scope | How it surfaced | Reason for exclusion |
|---|---|---|
| Automated IoT live-streaming for tier-2/tier-3 supplier emissions | Proposed by the technical team during architecture review | Out of scope for Release 1: suppliers currently provide document-based carbon data |
| Direct online financial settlement for CBAM certificates | Raised by client stakeholders at the user meeting | Financial transactions and certificate purchasing are handled externally by EU importers |
| Automated third-party BSI certification generation | Produced by AI in the initial scoping draft | EcoTrace generates carbon evidence files; official certification and EPD issuance must be performed independently by BSI |
<!-- END:wont -->

## Table 4 · Data functions (ILF / EIF)

<!-- BEGIN:data_fn | input table - computed columns (do not edit): D -->
| Data group | ILF / EIF | Why | Function points |
|---|---|---|---|
| Carbon Methodologies & Rules | ILF | Created and maintained inside the system by the ESG department | 10 |
| Product Carbon Footprint (PCF) Records | ILF | Calculated and maintained within the EcoTrace platform | 10 |
| Compliance Reports & Audit Logs | ILF | Generated and stored internally for auditing and tracking | 10 |
| SAP ERP Transactional Data | EIF | Read from the core SAP S/4HANA system, never written | 7 |
| Energy & Operational Emissions | EIF | Read from SCADA and iLotusLand systems, never written | 7 |
| Logistics & Shipment Data | EIF | Read from Hoa Phat Logistics system, never written | 7 |
| EU ETS Carbon Prices | EIF | Read from external carbon market feeds, never written | 7 |
<!-- END:data_fn -->

## Table 4 · total

<!-- BEGIN:data_fn_total | derived - auto-generated, do not edit -->
| Item | Value |
|---|---|
| Total data-function points | 58 |
<!-- END:data_fn_total -->
