.. _esp8266-programmer:

ESP8266 ESP-01 Programmer Kit
==============================

**Stack:** ESP8266, FTDI, Perfboard

.. image:: /_static/images/electronic/esp8266-programmer.jpg
   :width: 100%

**TL;DR** — A custom perfboard kit that handles all the internal wiring required
to program an ESP-01 module. Place the FTDI and ESP-01 on the kit, press a
button, and flash firmware.

---

Programming the ESP-01 module is notoriously fiddly — you need to wire the
correct GPIO pins high/low to enter flash mode, manage the voltage levels, and
hold the reset sequence. This kit eliminates all that headache.

A custom perfboard with pin headers for both the FTDI programmer and the ESP-01
module. Internal traces handle the CH_PD pull-up, GPIO0 pull-down for flash
mode, and the reset/program button logic. Drop the modules in, press the button,
and flash via the Arduino IDE or esptool. No jumper wires, no breadboard
spaghetti.

Key Details
-----------

- **Design** — Single perfboard with FTDI + ESP-01 pin headers
- **Features** — One-button flash mode entry, CH_PD pull-up, GPIO0 pull-down,
  reset circuit
- **Use case** — Rapid prototyping and firmware updates for ESP-01 modules
- **Compatibility** — Works with any standard FTDI (3.3 V) adapter
