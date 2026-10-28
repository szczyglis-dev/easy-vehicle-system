.. _evs-vehicletuning--tune-a-vehicle:

Tune a vehicle
==============

For km/h, mph or m/s authoring and readouts, see :doc:`Speed units </SpeedUnits>`.

Change one group at a time and compare the same maneuver. Use the controller's Live values to distinguish an input problem, a mechanical limit and a presentation problem.

.. _evs-vehicletuning--1-establish-the-physical-scale:

1. Establish the physical scale
-------------------------------

Verify wheel radius/width, wheelbase, track width, chassis clearance and center of mass. Use the intended loaded mass, including physical characters and hinged parts. Configuration currently applies a minimum chassis mass of 100 kg.

A scaled visual model alone does not make a correct contact setup. Complete :ref:`wheel setup <evs-gettingstarted--create-your-first-wheel-vehicle>` before increasing grip or torque.

.. _evs-vehicletuning--2-make-suspension-support-the-load:

2. Make suspension support the load
-----------------------------------

Tune spring, damping, travel and target position until the vehicle settles within useful travel. Then check braking, cornering and a small bump. Add anti-roll support afterward. See :doc:`Suspension </Suspension>`.

.. _evs-vehicletuning--3-match-engine-and-gearing:

3. Match engine and gearing
---------------------------

For gearbox drive, tune Peak Torque, torque curve, idle/redline and ratios together. Maximum Power and Maximum Drive Acceleration can cap the result; raising torque alone may not increase acceleration when a cap is active.

Direct mode uses Vehicle Settings' wheel-torque budget. Top Speed supplies a soft drive-torque fade, not a forced velocity. With gears, ratios, redline, drag and available power also determine attainable speed.

Set shift timing and automatic RPM thresholds after the gear range works. Configure a clutch if the player needs a pedal or a controllable launch. See :doc:`Gearbox </Gearbox>`, :doc:`Clutch </Clutch>` and :doc:`drivetrain reference </Scripting/DriveDynamics>`.

.. _evs-vehicletuning--4-tune-steering-and-grip:

4. Tune steering and grip
-------------------------

Set the road-wheel steering limit for the geometry. Configure visible steering-wheel travel separately. Adjust digital steering speed, optional speed/radius limits and Ackermann behavior, then check with the intended analog or digital input.

Set base grip and :doc:`ground Surface multipliers </Surfaces>`. Add traction/stability assistance after native contact behavior is acceptable. If DrivingAssists is installed, edit its shared settings there.

.. _evs-vehicletuning--5-validate-before-adding-effects:

5. Validate before adding effects
---------------------------------

Check start/stop, reverse, a tight turn, a fast turn, a slope and a landing. Verify passenger load and a reset/re-enable cycle. Save persistent changes outside Play Mode and repeat with a fresh instance.

Only then balance engine sound, exhaust, tire particles and marks. Those outputs should explain the mechanical behavior, not hide missing contact or an unsuitable drivetrain. Use :doc:`Troubleshooting </Troubleshooting>` when a symptom cannot be isolated.
