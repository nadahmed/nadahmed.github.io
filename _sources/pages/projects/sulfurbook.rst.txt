.. _sulfurbook:

SulfurBook — Double-Entry Bookkeeping
=====================================

**Stack:** Python, PostgreSQL, MCP (Model Context Protocol)

.. image:: /_static/images/software/sulfurbook.jpeg
   :width: 100%

SulfurBook is a personal finance and bookkeeping tool designed around the
principles of double-entry accounting. The goal is to make financial records
more reliable, auditable, and easier to reason about without sacrificing
clarity for everyday use.

What It Does
------------

The application tracks transactions in a structured ledger and keeps account
balances consistent through double-entry bookkeeping rules. It is designed for
people who want more discipline in their finances while still keeping the
workflow approachable.

Key capabilities include:

- ledger-based transaction entry
- account and category tracking
- balance checks for financial integrity
- reporting views for monthly activity and summaries
- a clean interface for daily bookkeeping work

Why It Matters
--------------

Many personal finance tools focus on budgeting and visual summaries, but they
rarely model the accounting relationships that make records trustworthy. This
project was built to explore that space more intentionally and to create an
experience that feels both practical and structurally sound.

Technical Approach
------------------

The system is implemented in Python with PostgreSQL for persistence. A major
part of the project is the use of Model Context Protocol (MCP) servers so that
AI agents can interact with the financial ledger directly for reporting,
auditing, and workflow automation.

This architecture makes the project more than a simple CRUD interface: it is a
foundation for future automation, financial analysis, and explainable account
insights.

Current Direction
-----------------

The project is being developed as a long-term personal accounting workspace.
The near-term focus is on improving reliability, reporting quality, and the
ergonomics of transaction entry while keeping the core accounting model intact.

.. button-link:: https://github.com/nadahmed/sulfur-ledger
   :color: primary
   :shadow:

   View on GitHub
