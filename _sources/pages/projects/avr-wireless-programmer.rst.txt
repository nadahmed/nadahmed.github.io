.. _avr-wireless-programmer:

Wireless AVR Programmer — ESP32 Standalone ISP
===============================================

**Stack:** ESP32, C++, Arduino framework, PlatformIO, SPI, ESPAsyncWebServer, ArduinoJson, LittleFS

**TL;DR** — A self-contained ESP32 that acts as a wireless ISP programmer for AVR microcontrollers.
Hosts its own Wi‑Fi access point with a web UI — upload a .hex file through a browser, click flash,
and the ESP32 programs the target chip over SPI. No USB, no ISP dongle, no PC required.

---

The Problem
-----------

Programming AVR microcontrollers (ATmega328P, ATmega168, ATmega8) typically requires a dedicated
USB-to-ISP dongle (Arduino-as-ISP, USBasp, AVRISP mkII) tethered to a computer. This is fine on a
workbench but impractical for field deployment, quick iterations on a soldering bench, or when you
need to flash a chip that's already embedded in a device. On top of that, a misconfigured clock fuse
can "brick" a chip by disabling its internal oscillator, requiring an external clock source just to
recover it.

What I Built
------------

An ESP32-based standalone ISP programmer that completely eliminates the need for a PC in the
programming workflow. It creates its own Wi‑Fi access point (``AVR_Wireless_Station``), serves a
responsive dark-theme web interface, and communicates with the target AVR over hardware SPI using
the standard Atmel ISP 4-wire protocol. A continuous 1 MHz PWM signal on GPIO4 provides a rescue
clock to keep bricked chips alive during programming.

Key Features
------------

- **Wireless operation** — ESP32 acts as a Wi‑Fi access point. No router, no cables, no host PC.
- **Web-based file management** — Upload .hex files, browse stored binaries, delete them — all from
  a browser running on a phone, tablet, or laptop.
- **Intel HEX parser** — Handles record types 00 (data), 01 (EOF), 02 (extended segment address),
  and 04 (extended linear address) with arbitrary base address offsets.
- **Fuse presets** — 11 pre-computed low/high fuse configurations across three chips for common
  clock sources (internal RC 1 MHz / 8 MHz, external 16 MHz crystal, external clock rescue mode).
- **Automatic chip detection** — Reads the 3-byte device signature and validates the selected fuse
  preset against the connected chip, rejecting mismatches to prevent bricking.
- **Flash verify** — Optional readback verification that compares every programmed byte against
  the original binary.
- **Rescue clock** — Continuous 1 MHz square wave on GPIO4 drives the target's XTAL1 pin,
  enabling recovery of chips whose fuses are set to external clock/crystal sources.
- **Persistent storage** — Uploaded binaries are stored on ESP32's LittleFS (1.25 MB dedicated
  partition), surviving power loss.
- **OTA-ready layout** — Two 1.25 MB app partitions enable future over-the-air firmware updates
  without reprogramming the ESP32 via USB.
- **LED status** — On-board LED signals idle (off), programming activity (flicker), or failure
  (100 ms blink).

Architecture
------------

The firmware is split into two main modules:

**AVRProgrammer (``AVRProgrammer.h`` / ``AVRProgrammer.cpp``)**
  Implements the full AVR ISP protocol over hardware SPI at 100 kHz. Every transaction is a 4-byte
  packet. Key operations:

  - Programming Enable handshake (``0xAC 0x53 0x00 0x00``)
  - Signature read (``0x30 0x00 0xAA 0x00``)
  - Fuse write (low / high / extended)
  - Chip erase
  - Page-buffer load (word-by-word) and page-commit for flash programming
  - Flash readback for verification
  - Bit-bang SPI fallback (maintained for reference)

  Flash pages are 128 bytes (64 words) for ATmega168/328P and 64 bytes (32 words) for ATmega8.
  Each page is fully buffered before the write command is issued, with a 10 ms settling delay.

**HTTP Server & API (``main.cpp``)**
  An ESPAsyncWebServer instance on port 80 serves the web UI and a RESTful JSON API:

  ``GET /``
    Returns the web interface (embedded dark-theme HTML/CSS/JS).
  ``POST /api/upload-hex``
    Accepts a JSON payload with filename + Intel HEX content, parses it into binary, and stores
    it on LittleFS.
  ``GET /api/hex-files``
    Lists all stored .bin files with sizes.
  ``DELETE /api/hex-files?name=...``
    Removes a stored file.
  ``POST /api/flash``
    Triggers the full ISP pipeline: enter programming mode → verify signature → optionally burn
    fuses → chip erase → write flash → optionally verify → exit.

Rescue Clock
------------

The ESP32's LEDC peripheral generates a continuous 1 MHz, 50 % duty cycle square wave on GPIO4,
connected to the target's XTAL1 input. This ensures the AVR has a valid clock source regardless
of its fuse settings. A chip whose fuses are set to "External Crystal" or "External Clock" would
otherwise be unrecoverable through ISP without an external signal generator. The rescue clock starts
at boot and runs continuously.

Wiring
------

Target AVR pins (shown for DIP-28 ATmega328P):

  +----------+-----------------------------+
  | ESP32    | Target                      |
  +==========+=============================+
  | GPIO 18  | SCK   (Pin 19)              |
  | GPIO 19  | MISO  (Pin 18)              |
  | GPIO 23  | MOSI  (Pin 17)              |
  | GPIO  5  | /RESET (Pin 1)              |
  | GPIO  4  | XTAL1 (Pin 9) — rescue clk  |
  | GPIO 13  | Status LED (via 220 Ω)      |
  | 3.3V     | VCC    (Pin 7)              |
  | GND      | GND    (Pin 22)             |
  +----------+-----------------------------+

Supported Targets
-----------------

  +-------------+-----------+---------------+------------------+
  | Chip        | Flash     | Page          | Signature        |
  +=============+===========+===============+==================+
  | ATmega8/A   | 8 KB      | 64 B (32 w)   | 0x1E 0x93 0x07   |
  | ATmega168/P | 16 KB     | 128 B (64 w)  | 0x1E 0x94 0x06   |
  | ATmega328P  | 32 KB     | 128 B (64 w)  | 0x1E 0x95 0x0F   |
  +-------------+-----------+---------------+------------------+