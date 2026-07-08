.. _hr-system:

HRMS with Biometric Attendance Integration
===========================================

**Stack:** Django, Django REST Framework, Angular, PostgreSQL

**TL;DR** — Replaced a manual paper-based attendance process for a government
organization by pulling real-time fingerprint punch data from Nitgen Access
Manager into a clean web interface.

- **Biometric data pipeline** — Read punch logs directly from Nitgen's MSSQL
  database via ODBC, eliminating manual register-to-spreadsheet workflows.
  Real-time webhook for instant check-in/out capture.
- **Attendance dashboard** — Daily check-in, check-out, and overtime records
  surfaced in an Angular SPA with filtering by date, employee, and department.
  Late arrival / early leave flagged automatically.
- **Sync infrastructure** — Batch sync commands for users and attendance logs
  with streaming progress feedback. Handles thousands of punches without
  dropping data.
- **Architecture** — Django REST API + Angular frontend, Swagger docs, Docker
  deployment. Read from MSSQL, write to PostgreSQL — zero downtime during
  migration.
