.. _agnistop:

AgniStop — Fire Safety IoT
===========================

**Stack:** Go, Angular, GraphQL, LoRaWAN, ChirpStack, SQLite, Redis

.. image:: /_static/images/software/agnistop.jpeg
   :width: 100%

**TL;DR** — End-to-end IoT fire safety system connecting LoRaWAN smoke/heat
detectors to a real-time web dashboard with sub-second alerting, multi-channel
notifications, and interactive floor-plan maps. Ready to white-label or deploy
as a SaaS product.

---

The Problem
-----------

Traditional fire alarm systems are closed, expensive, and don't integrate with
modern building management. Facilities with hundreds of sensors have no way to
monitor battery health, detect sensor faults remotely, or get instant alerts
when an alarm triggers — they rely on audible sirens and manual inspection.

The Product
-----------

AgniStop replaces dumb smoke alarms with a cloud-connected intelligent
monitoring platform. LoRaWAN-enabled sensors (AN102C/AN102D) transmit telemetry
over long range through walls and floors. The backend ingests these signals via
ChirpStack, decodes the binary payloads, logs every event with RF metrics, and
pushes real-time updates to the dashboard — all in under a second.

Key Capabilities
----------------

- **Real-time monitoring** — GraphQL subscriptions push alarm events to all
  connected clients instantly via WebSocket. Audible alerts on the dashboard
  when smoke is detected.
- **Interactive floor-plan maps** — Drag-and-drop alarm markers on zone images.
  Position persists as percentages for responsive scaling. Fire marshals can
  see exactly which sensor triggered, where.
- **Multi-channel notifications** — In-app (WebSocket), email (SMTP), SMS
  (pluggable). Escalate automatically based on alarm severity.
- **Sensor health dashboard** — Battery levels, RF signal (RSSI/SNR), sensor
  self-test failures, and optical maze pollution — all tracked per-device. Know
  when a sensor needs maintenance before it fails.
- **Comprehensive event logs** — Every LoRa uplink recorded with timestamp,
  RSSI, SNR, battery voltage, gateway ID, sensor type, and alarm status.
  Audit-ready for fire safety compliance.
- **Zone management** — Organize sensors by building, floor, or room. Upload
  floor plans, position alarms visually.
- **Silence / reset** — Individual or global alarm silencing from the dashboard.
  No need to physically access the sensor.

Technical Architecture
----------------------

Backend (Go)
^^^^^^^^^^^^

- GraphQL API (gqlgen) with WebSocket subscriptions
- Redis Stream consumer for real-time LoRa uplink ingestion
- Binary protocol decoders for AN102C (smoke + temp + humidity) and AN102D
  sensors
- ChirpStack gRPC integration for device sync
- Pluggable notifiers: WebSocket, email, SMS, console
- Pluggable storage: local filesystem or AWS S3
- OAuth 2.0 authentication with session cookies
- SQLite + Redis caching (extensible to PostgreSQL)

Frontend (Angular)
^^^^^^^^^^^^^^^^^^

- Real-time dashboard with zone overview and alarm stats
- Interactive floor-plan maps with draggable alarm markers
- Paginated event log explorer (RSSI, SNR, battery, gateway)
- Audible alarm playback on ALERT state
- Angular Material + Tailwind CSS UI
- Apollo GraphQL client with WebSocket transport

Monetization Paths
------------------

- **Hardware + SaaS bundle** — Sell LoRaWAN sensors pre-paired with a cloud
  subscription. Tiered pricing by sensor count or zone count.
- **White-label** — Rebrand the entire platform (Angular + Go backend) for fire
  safety companies managing multiple client sites.
- **Professional monitoring** — Feed alarm events into a central monitoring
  station. Charge monthly for dispatch services.
- **Compliance reporting** — Generate NFPA / local fire code reports from the
  event log database. Premium add-on for regulated industries.
- **Predictive maintenance** — Battery level and self-test monitoring enables
  proactive sensor replacement contracts.

Current Status
--------------

Fully functional prototype with three components:

- Go based GraphQL server with ChirpStack integration
- Angular web dashboard
- Wails desktop tool for testing alarm states
