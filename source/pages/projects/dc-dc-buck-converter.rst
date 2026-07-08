.. _dc-dc-buck-converter:

Variable DC-DC Buck Converter
==============================

**Stack:** LT1074, Breadboard, Power Electronics

.. image:: /_static/images/electronic/buck-converter.jpg
   :width: 100%

**TL;DR** — Breadboard implementation of a variable step-down switching
regulator for 3rd-year Power Electronics course. Uses an LT1074 to avoid
complicated transistor switching and feedback networks.

---

A practical deep-dive into switching regulator design. Rather than building a
discrete transistor-based buck converter (which would require careful driver
and feedback compensation networks), this project used the LT1074 — a
monolithic switching regulator IC that integrates the power switch, oscillator,
and control circuitry into a single package.

Built entirely on a breadboard with through-hole components. The output voltage
is adjustable via a trim potentiometer in the feedback divider. Used for
powering downstream embedded circuits at variable voltages.

Key Details
-----------

- **Regulator** — LT1074 step-down switching regulator
- **Input** — 12-15 V DC
- **Output** — Adjustable 3.3–12 V DC
- **Topology** — Buck (step-down) converter
- **Construction** — Breadboard with through-hole components
