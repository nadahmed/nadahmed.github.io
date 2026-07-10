.. _moneycounter-display:

TW600L Money Counter — External Display
========================================

**Stack:** ATmega8A, AVR C++, PlatformIO, avr-libc, 7-segment display

..  youtube:: 2rj1b9FMeFM
   :width: 100%

..  youtube:: U8P_6evZP6w
   :width: 100%

..  youtube:: tK-sghOiGhE
   :width: 100%

**TL;DR** — Zero-Arduino AVR C++ firmware that decodes the TW600L money counter
protocol via external interrupt and drives a 3-digit multiplexed 7-segment
display. Branch-free pin control, subtraction-based digit extraction, and
throttled sensor polling free ~26 % CPU time vs naive implementations.

---

The Problem
-----------

Off-the-shelf external displays for the TW600L currency counter are expensive
and limited. The goal was to build a low-cost alternative using parts readily
available in Bangladesh, designed for local manufacturing with minimal BOM cost
and fast assembly.

What I Built
------------

A compact, interrupt-driven firmware that captures 4-byte packets from the
TW600L sensor via ``INT0`` and drives a common-cathode/common-anode auto-
detecting 3-digit 7-segment display. The entire project is written in plain
AVR C++ without a single Arduino dependency.

Key Features
------------

- **Zero Arduino Dependencies** — Built directly on avr-libc for smaller
  footprint and precise timing.
- **Interrupt-Driven Decoding** — ``INT0`` captures TW600L data in the
  background without polling.
- **Non-Blocking Display** — State-machine multiplexing of segments without
  halting the CPU.
- **Auto-Detect Display Type** — PD4 is sensed at boot; firmware auto-inverts
  polarity for common cathode vs common anode. No code changes needed.
- **Branch-Free Pin Control** — Pre-computed port/mask lookup tables with
  zero branches or switch statements in the hot path.
- **Subtraction-Based Digit Extraction** — No division in the hot path (the
  ATmega8A has no hardware divider).
- **PROGMEM Segment Patterns** — All 10 segment patterns stored in flash,
  zero RAM consumed.
- **Throttled Sensor Polling** — ``sensor.available()`` checked only once per
  display refresh (~476 Hz) instead of every segment update (~10 kHz),
  eliminating ~99.8 % of redundant calls.

Architecture
------------

The firmware is split into two clean layers:

- **``TW600L``** — Interrupt-driven decoder for the TW600L 4-byte packet
  protocol. Data arrives on PD3 (data) clocked by PD2 (INT0).
- **``SevenSeg``** — State-machine display driver that iterates through 3
  digits × 7 segments. At ``init()``, all port pointers and masks are
  pre-computed; polarity inversion is applied via a single XOR with a
  pre-set flag.

PCB & Manufacturing
-------------------

Designed for Bangladesh's local electronics ecosystem. Every decision was
driven by cost and manufacturability:

- **Single-layer PCB** — Local vendors charge significantly less for single-
  layer boards; all routing fits on one layer with no vias.
- **Minimal component count** — Fewer parts means less soldering time and
  lower BOM cost.
- **Bent-pin SMD display** — The 7-segment display pins are bent flat and
  soldered directly to the PCB as a surface-mount part, eliminating the need
  for a separate socket or connector. Through-hole components sit on the
  opposite side.
- **Custom KiCad footprints** — The display and several other parts lacked
  existing library footprints (or finding them was too time-consuming), so
  all custom footprints were built from scratch in KiCad.

Performance

At 8 MHz, a full display refresh of 3 digits × 7 segments takes ~2.1 ms
(~476 Hz). Leading zeros are blanked — value ``0`` displays as ``"0"``,
``42`` as ``"42"``, ``234`` as ``"234"``.