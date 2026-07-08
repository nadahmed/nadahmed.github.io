.. _tld-logger:

Temperature Logger for Jute Mill Treatment
===========================================

**Stack:** ESP8266, Angular, Highcharts, pdfmake, PT100/MAX31865

.. image:: /_static/images/electronic/tld_v2.jpeg
   :width: 100%

**TL;DR** — Embedded temperature logger used in jute mills to monitor wooden
crate treatment in burners. Logs temperature on a configurable interval with
start/stop timer, displays a live graph, and generates printable PDF reports
with company details for shipment compliance.

---

What It Does
------------

Jute mills treat wooden crates/carriers in burner/heat machines before shipping.
This device sits alongside the burner, reads temperature from a PT100 RTD sensor
via MAX31865, and logs it at configurable intervals. Operators start/stop the
logging session, view a real-time temperature graph, and print a PDF report to
attach to the shipment — proving the treatment was done at the right temperature.

Device Interaction
------------------

- **Connecting** — The ESP8266 creates its own Wi-Fi hotspot. Users connect
  their phone/laptop to the ``HIVECORE TLD`` network. Captive portal auto-redirects
  to the Angular dashboard — no app install, no configuration.
- **Live view** — Real-time temperature displayed on the built-in 16x2 LCD and
  streamed to the browser via Server-Sent Events. Highcharts graph updates live.
- **Logging session** — Operators set the sampling interval and press start. The
  device records temperature data points until stopped. Timer shows elapsed time.
- **PDF reports** — At the end of a session, a PDF report is generated client-side
  (pdfmake/PDFKit). It includes the temperature log table and configurable company
  contact details, invoice info, and shipment references. Operators print and
  attach to the shipment.

Key Features
------------

- **Captive portal** — Connect to the device's Wi-Fi, the dashboard opens
  automatically. No internet required.
- **Configurable logging interval** — Set how often temperature is sampled (every
  few seconds, minutes, etc.).
- **Start/stop timer** — Control exactly when logging begins and ends.
- **Live temperature graph** — Highcharts line chart updates in real-time via SSE.
- **PDF generation** — Client-side PDF with temperature data, configurable company
  info, invoice/contract numbers, notify party, and total pallets.
- **Settings persistence** — Company details and interval settings survive device
  restarts.
- **Local LCD display** — 16x2 I2C LCD shows current temperature at a glance
  without needing to connect a device.
- **OTA updates** — Firmware can be updated wirelessly via the browser.

Tech Stack
----------

- **Firmware** — ESP8266, Arduino framework, PlatformIO, LittleFS
- **Frontend** — Angular 15+, Angular Material, Highcharts, pdfmake
- **Real-time** — Server-Sent Events (SSE)
- **Sensor** — PT100 RTD via MAX31865 (SPI)
- **Display** — 16x2 I2C LCD
- **Captive portal** — ESPAsyncDNSServer + ESPAsyncWebServer

