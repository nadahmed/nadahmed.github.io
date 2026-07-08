.. _self-balancing-robot:

Self Balancing Robot
====================

**Stack:** Arduino, MPU6050, PID, DC Motors

..  youtube:: vwax-K6ykNc
   :width: 100%

**TL;DR** — Built a two-wheeled robot that maintains upright balance using an
IMU and PID control loop. Course project for Microprocessors and Interfacing.

---

A classic inverted-pendulum problem implemented on a custom chassis. An MPU6050
accelerometer + gyroscope provides tilt angle readings, which feed into a PID
controller that drives two DC motors to keep the robot upright. Tuning the PID
gains was the bulk of the work — too aggressive and the bot oscillates, too
conservative and it falls over.

Key Details
-----------

- **Sensor** — MPU6050 (6-axis IMU) for angle estimation
- **Control** — PID loop running on an Arduino microcontroller
- **Actuation** — Dual DC motors with PWM speed control
- **Chassis** — Custom 3D-printed frame
- **Power** — Li-ion battery pack
