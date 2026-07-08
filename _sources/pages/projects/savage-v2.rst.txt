.. _savage-v2:

Savage V2 — Line + Ceiling Follower
====================================

**Stack:** Arduino, IR Sensors, DC Motors, Gearbox

.. image:: /_static/images/electronic/savage-v2.jpg
   :width: 100%

**TL;DR** — Savage V1 heavily modified to climb 30-degree inclines and follow
a ceiling-mounted track.

---

Took the Savage V1 chassis and pushed it beyond its original design. The goal
was to follow a black line not just on flat ground but also up ramps and along
a ceiling track. Required mechanical changes (lower center of gravity, stronger
gear ratio) as well as firmware tweaks (higher PWM thresholds on inclines,
sensor inversion for ceiling mode).

Also included a half-hearted obstacle avoidance mode — it worked, barely. The
focus was always on the line/ceiling following.

Key Details
-----------

- **Incline** — Up to 30-degree ramps with adjusted motor power
- **Ceiling mode** — Inverted IR sensor logic for overhead tracks
- **Mechanical** — Lowered chassis, reinforced gearbox
- **Control** — Enhanced bang-bang with incline detection heuristic
