.. _evs-clutch--clutch-setup:

Clutch setup
============

Add ``Clutch`` for driver-operated disengagement, analog launches and automatic coupling assistance. Assign it to ``Engine.clutch``, or let configuration resolve the registered module.

.. _evs-clutch--configure:

Configure
---------

1. Register the clutch and check the engine reference.
2. Keep ``automatic`` enabled for automatic launch/coasting assistance, or turn it off for continuous driver control.
3. Set ``torqueCapacity`` for the engine's crankshaft torque and ``Engine.rotationalInertia`` for the desired flywheel response.
4. Connect the input channel: **0 released/connected**, **1 depressed/disconnected**. Intermediate values control torque capacity.
5. Check neutral revving, gradual launch, abrupt release, shifting and braking with both transmission modes.

``engagementRate`` smooths automatic assistance; it does not delay a driver pedal release. ``allowLaunchWheelspin`` controls whether the stored flywheel-energy share passes through traction control.

Use ``InputBuffer.SetClutch(float)`` or the corresponding ActionInput axis. See :doc:`Input </Input>` for bindings. Configure coasting losses separately from service brakes; releasing throttle should not be used as a substitute for parking.

The engine has idle support; stalls and clutch heat/wear are outside this model. See the :ref:`drive dynamics reference <evs-scripting-drivedynamics--clutch>` for coupling, energy transfer and gearbox interaction.
