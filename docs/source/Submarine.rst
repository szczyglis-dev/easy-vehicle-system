.. _evs-submarine--submarine-setup:

Submarine setup
===============

Choose Submarine for underwater displacement, powered thrust, yaw, pitch and vertical movement. It uses a wheel-free hull.

.. _evs-submarine--build:

Build
-----

1. Prepare the root Rigidbody and hull collider, then choose **Add Vehicle → Submarine**.
2. Set mass and hull half-height for the surface displacement transition.
3. Assign WaterInteraction and a provider, or set the profile's fallback water plane and bounds.
4. Connect forward/reverse, turning, lift, pitch and brake input.
5. Check submerged rest, ascent/descent, reversal, engine-off drift and leaving the water bounds.

Buoyancy remains with the engine off; powered motion does not. Outside water, the profile supplies neither buoyancy nor water propulsion. Submarine support does not use surface-boat wake and splash channels.

.. _evs-submarine--depth-and-attitude:

Depth and attitude
------------------

With Hold Depth enabled, releasing lift input captures the current height. The engine must remain powered and the hull in water to maintain it. Disable Hold Depth for passive displacement and damping. Tune pitch range and response separately from vertical lift.

.. _evs-submarine--propeller-presentation:

Propeller presentation
----------------------

Assign the visible shaft in Propulsion's Propellers list. Enable Only With Thrust to stop it at idle, Reverse With Thrust for reversal, and Only In Water to stop it when dry. Add steering/lift/pitch demand only if that propeller should visibly react to those controls.

Set Spin Up/Down times for the desired visual response or choose Instant Thrust Response. These settings animate the mesh; thrust comes from the drive profile.

See :doc:`water setup </Water>`, :doc:`demo controls </Demo>` and the :doc:`water reference </Scripting/Water>` for sampling, depth hold and propeller integration.
