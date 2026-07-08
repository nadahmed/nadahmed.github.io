.. _h-bridge-motor-driver:

H-Bridge Motor Driver (MOSFETs)
================================

**Stack:** MOSFETs, NPN Transistors, Perfboard

.. image:: /_static/images/electronic/h-bridge.jpg
   :width: 100%

**TL;DR** — Custom H-bridge using 2 N-Channel and 2 P-Channel MOSFETs with NPN
transistor drivers. Designed to drive DC motors for a Mars Rover project.

---

Built a discrete H-bridge motor driver from scratch — no L298 or integrated
driver IC. The design uses four MOSFETs (two N-channel, two P-channel) in a
classic H-bridge configuration, with NPN bipolar transistors providing the
gate drive logic.

The NPN transistors level-shift the microcontroller's 5 V logic signals to
drive the MOSFET gates properly, ensuring clean switching. Flyback diodes
protect against inductive kickback from the DC motors.

Designed specifically for the Mars Rover project's drive motors, where both
forward/reverse and PWM speed control were needed.

Key Details
-----------

- **High-side** — 2x P-Channel MOSFETs (IRF9540 or equivalent)
- **Low-side** — 2x N-Channel MOSFETs (IRF540 or equivalent)
- **Gate drivers** — 2x NPN transistors (2N2222) for level shifting
- **Protection** — Flyback diodes across each MOSFET
- **Control** — PWM-compatible for variable speed
- **Construction** — Perfboard with point-to-point soldering