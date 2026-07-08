.. _gym-management:

SharkRaven — Gym Management System
===================================

**Stack:** Next.js, TypeScript, PostgreSQL, shadcn/ui

**TL;DR** — Multi-branch gym management SaaS built from scratch with
face-recognition kiosk attendance, double-entry accounting, and full member
lifecycle management (enrollment, workouts, diet, medical, locker, lead CRM).

- **Kiosk attendance** — Face recognition via DeepStack AI for contactless
  check-in/out; dedicated fullscreen kiosk mode for gym entrances.
- **Double-entry accounting** — Invoicing, billing, payment collection, general
  ledger, journal entries, and cash-flow reporting. No ORM — raw SQL with
  repository pattern for audit-grade data integrity.
- **Member lifecycle** — Enrollment → membership plans → fitness assessments →
  workout & diet plans → medical vitals tracking → locker assignments.
- **Operations** — RBAC with granular branch-scoped permissions, lead CRM
  (Kanban pipeline), product/inventory management, email & SMS campaigns.
- **Architecture** — Next.js 16 + React 19, Server Actions only (no REST for
  UI), custom encrypted session auth, TanStack Query, Zod validation, spec-
  driven development with Gherkin-style specs, Jest + Playwright.
