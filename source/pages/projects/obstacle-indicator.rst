.. _obstacle-indicator:

Obstacle Indicator for the Blind (Acoustics)
=============================================

**Stack:** Arduino, Ultrasonic Sensor, Piezo Buzzer

.. image:: /_static/images/electronic/obstacle-indicator.png
   :width: 100%

**TL;DR** — A wearable assistive device that maps obstacle distance to sound
frequency — higher pitch when closer, lower when farther, silence when clear.

---

A hobby project exploring assistive technology. An HC-SR04 ultrasonic sensor
measures distance to the nearest obstacle. The reading maps to a PWM frequency
output on a piezo buzzer — the closer the obstacle, the higher the pitch. When
no obstacle is within range, the buzzer stays silent.

The concept is simple but effective: it gives the user an intuitive audio cue
for spatial awareness without requiring visual attention. Designed to be worn
on a wrist strap or clipped to a cane.

Key Details
-----------

- **Sensor** — HC-SR04 ultrasonic distance sensor
- **Output** — Piezo buzzer with variable PWM frequency
- **Mapping** — Distance → frequency (inverse linear)
- **Range** — ~2 cm to ~4 m detection
- **Power** — 9 V battery or USB power bank