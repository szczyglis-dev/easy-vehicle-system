.. _evs-tractioncontrol--traction-control-setup:

Traction control setup
======================

TractionControl limits driven-wheel torque when native tire contact indicates excess slip. Use it after the engine, wheel roles and ground grip are working.

.. _evs-tractioncontrol--tune-intervention:

Tune intervention
-----------------

1. Add TractionControl and drive on a consistent ground surface.
2. Start with the configured Target Slip and Launch Reference Speed.
3. Adjust Reduction Rate for intervention speed and Recovery Rate for returning power.
4. Use Traction Reserve and Reserve Grip For Cornering to leave capacity for cornering.
5. Compare the same launch and turn with the module enabled and disabled.

A very low target slip or slow recovery can make the vehicle feel underpowered. Check physical contact, braking and gearing before compensating with more engine torque.

Use DrivingAssists if TCS and steering stability should share a control panel. While that facade is enabled, configure the shared values there. ``Active``, ``MinimumTorqueScale`` and ``MaximumSlip`` help diagnose intervention.

For contact-capacity calculations, locked-differential interaction and a runtime control example, see :doc:`drivetrain reference </Scripting/DriveDynamics>`.
