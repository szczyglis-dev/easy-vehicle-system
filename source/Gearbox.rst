.. _evs-gearbox--gearbox-setup:

Gearbox setup
=============

For km/h, mph or m/s authoring and readouts, see :doc:`Speed units </SpeedUnits>`.

Use a manual or automatic gearbox for ratio-based propulsion. Direct mode drives without selectable gears.

.. _evs-gearbox--configure:

Configure
---------

1. Configure forward ratios as ordered positive values, a positive reverse ratio, final drive and efficiency.
2. Set shift duration and direction-change safety speed.
3. For Automatic, set upshift/downshift RPM and minimum gear time. Leave a useful gap between thresholds to avoid repeated shifts.
4. Check engine idle/redline, torque curve and launch behavior together with the ratios.
5. Check every gear, neutral, reverse, low-speed direction changes, slopes and airborne wheels.

Use ``TrySelectGear`` and shift requests for custom controls so safety checks apply. Invalid gears, unsafe reversals and over-rev downshifts are rejected. A request during a shift may also be rejected; implement any desired input queue in the application.

In Manual, positive throttle accelerates in the selected gear and brake remains separate. With signed keyboard driving, stop, release the brake and press again to request reverse. See :doc:`Input </Input>` for the supplied mappings and analog channel rules.

An enabled :doc:`Clutch </Clutch>` permits free revving and driver-controlled release. Automatic forward shifts pause while the driver controls an open/slipping clutch. Speed depends on ratios, torque, drag and redline; the engine also applies a soft torque fade near the configured road-speed limit.

See the :ref:`drive dynamics reference <evs-scripting-drivedynamics--engine-and-gearbox>` for shift decisions, wheel-RPM coupling and slope direction-request behavior.
