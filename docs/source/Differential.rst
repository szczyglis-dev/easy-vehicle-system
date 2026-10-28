.. _evs-differential--differential-setup:

Differential setup
==================

Add Differential when a driven axle needs open, limited-slip or locked coupling instead of the engine's basic wheel-weight distribution.

.. _evs-differential--configure-an-axle:

Configure an axle
-----------------

1. Add Differential to the vehicle.
2. Add an Axle entry and assign its left/right driven WheelColliders.
3. Choose a mode below. Add more pairs for other driven axles.
4. Apply configuration and check straight driving, a turn and one wheel on low-traction ground.

+--------------+------------------------------------------------+-----------------------------------------+
| Mode         | Use                                            | Main tuning                             |
+==============+================================================+=========================================+
| Open         | Axle torque limited by the lower-traction side | Traction estimate                       |
+--------------+------------------------------------------------+-----------------------------------------+
| Limited slip | Bias toward the slower or supported side       | Torque Bias Ratio and Slip RPM Range    |
+--------------+------------------------------------------------+-----------------------------------------+
| Locked       | Stronger coupling between wheel speeds         | Locked Coupling and Maximum Lock Torque |
+--------------+------------------------------------------------+-----------------------------------------+

Keep each wheel in one axle pair. Wheels outside the configured pairs keep their engine allocation. Disable the module to compare against that base allocation.

This is per-pair coupling, not a center differential between complete axles. See :ref:`drivetrain reference <evs-scripting-drivedynamics--differential>` for torque behavior and an axle configuration example.
