.. _xfishery-controller:

xFishery — ESP32 Feeder Controller
===================================

**Stack:** ESP32, C++, FreeRTOS, PlatformIO, ThingsBoard MQTT

**TL;DR** — Firmware for an ESP32-powered aquaculture fish feeder with a
custom LCD menu system, rotary encoder input, cloud telemetry, and remote
feed control via ThingsBoard.

---

The Problem
-----------

xFishery needed a simple, reliable controller for their automatic fish
feeder that operators could configure on-device without a computer, while
also supporting remote monitoring and control from a cloud dashboard.

What I Built
------------

A full-featured ESP32 firmware with a reusable, tree-based LCD menu system
that handles all local interaction. Operators navigate through menus using
a rotary encoder — scroll to select, push to confirm. No touchscreen, no
serial terminal, no mobile app required for day-to-day operation.

Key Features
------------

- **Extensible menu tree** — Generic composite tree structure where any node
  can hold sub-menus or trigger actions. Adding a new feature is just
  instantiating a ``Menu`` node with a callback. Used for feeder controls,
  WiFi settings, and LCD backlight toggling.
- **Rotary encoder navigation** — Scroll up/down through menu items, push to
  select. Debounced via ezButton library with callback-based event handling.
- **Local feeder control** — Manual on/off toggle, timed auto-feed with
  configurable duration, and real-time feed monitoring via a dedicated
  FreeRTOS task.
- **WiFiManager captive portal** — First-time setup via smartphone: the ESP32
  creates its own access point, user connects and configures WiFi credentials
  plus ThingsBoard server/token through a web form. No hardcoded secrets.
- **ThingsBoard cloud integration** — MQTT telemetry (RSSI, channel, local IP)
  every 2 seconds. RPC handlers for remote feed triggering and feed-duration
  calculation based on daily feed rate.
- **NVS persistence** — Feed duration, ThingsBoard credentials, and WiFi
  settings survive power loss via ESP32 Non-Volatile Storage.
- **FreeRTOS multitasking** — Separate tasks for UI polling, MQTT connection,
  and feed timing. Binary semaphore guards WiFiManager lifecycle to prevent
  race conditions.

Architecture
------------

The firmware is structured around a few reusable components:

- ``Menu`` — Generic tree node with title, parent pointer, child array, and
  a ``std::function`` callback. Entire menu is statically declared before
  ``setup()``.
- ``MenuCursor`` — Orchestrates LCD rendering and navigation. Registers itself
  as an observer of the rotary encoder events. Supports a cursor-disabled mode
  for handing control to the WiFiManager portal.
- ``ScrollControl`` — Rotary encoder driver that exposes ``onDirectionChange``
  and ``onButtonPress`` callbacks.
- ``Feeder`` — Meyer's singleton managing the motor GPIO pin, feed duration,
  and start/stop state. Polled by a dedicated FreeRTOS task.
- ``ThingsBoardSetup`` — MQTT client running in its own task. Subscribes to
  RPC topics, publishes telemetry on a 2-second timer.
- ``WifiSetup`` — WiFiManager wrapper that runs the captive portal in a
  separate task with mutex protection.

Interaction Model
^^^^^^^^^^^^^^^^^

- **Rotary encoder** → scroll menu / select item
- **16x2 LCD** → focused item on row 0, subtitle on row 1
- **Push button** → execute menu callback or launch submenu
- **Captive portal** → WiFi + cloud config via smartphone

Cloud Integration
^^^^^^^^^^^^^^^^^

- **MQTT** → ThingsBoard over TLS (configurable)
- **Telemetry** → RSSI, channel, BSSID, IP, simulated temp
- **RPC** → ``feedCalculation`` (compute duration from daily rate),
  ``example_set_switch`` (start/stop motor)
- **Attributes** → network diagnostics pushed every 2 s
