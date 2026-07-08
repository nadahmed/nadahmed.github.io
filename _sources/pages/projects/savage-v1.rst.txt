.. _savage-v1:

Savage V1 — Line Follower
=========================

**Stack:** Arduino, IR Sensors, DC Motors

.. image:: /_static/images/electronic/savage-v1.jpg
   :width: 100%

**TL;DR** — My first functional line-following robot. Follows a 2-inch black
line on a white surface using IR reflectance sensors.

---

The bot that started it all. Savage V1 uses an array of IR sensors to detect a
black line on a white background and drives two DC motors to stay on track.
Simple bang-bang control — if a sensor drifts off the line, the corresponding
motor corrects. No PID, no frills, just persistent trial-and-error tuning of
sensor heights and motor speeds.

Key Details
-----------

- **Sensors** — 5 IR reflectance sensor array
- **Control** — Bang-bang (on/off) correction logic
- **Actuation** — Dual DC motors with differential steering
- **Microcontroller** — Arduino (ATmega328P)

