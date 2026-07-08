.. _savage-v3:

Savage V3 — Modular LFR
========================

**Stack:** Arduino, Bluetooth, MIT App Inventor 2, Modular Chassis

.. image:: /_static/images/electronic/savage-v3.jpg
   :width: 100%

**TL;DR** — Complete redesign with modular chassis, improved firmware, and
Bluetooth control via a custom Android app with gyroscope steering.

---

Savage V3 was a ground-up rebuild. The chassis switched to a modular design —
sensor board, motor drivers, and microcontroller on separate PCBs that could be
swapped independently. The firmware was rewritten from scratch with cleaner
state-machine architecture.

The standout feature was Bluetooth control via a custom Android app built in
MIT App Inventor 2. The app used the phone's gyroscope for steering — tilt
left/right to turn, tilt forward to accelerate — replacing physical buttons
with an intuitive motion-based interface.

Key Details
-----------

- **Modular design** — Separate PCBs for sensors, motor drivers, MCU
- **Firmware** — State-machine architecture, cleaner than V1/V2
- **Bluetooth** — HC-05 module for wireless control
- **Android app** — MIT App Inventor 2 with gyroscope-based steering
- **Chassis** — Custom modular frame with mounting points for each module
