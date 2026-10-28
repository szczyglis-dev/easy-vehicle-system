.. _evs-aircraft--aircraft-setup:

Aircraft setup
==============

The package includes built-in controls and physics for multiple types of flying vehicles: airplanes, aerobatic aircraft, jets, helicopters, drones and hover vehicles. Choose a drive profile for the movement you want, then configure its controls, body, propulsion and optional landing gear. Cockpit animation, rotor visuals, sound and effects can be added independently.

.. _evs-aircraft--choose-a-flight-profile:

Choose a flight profile
-----------------------

+--------------------+----------------------------------------------------------------+----------------------------------------------------------------------------------------+
| Profile            | Suitable vehicles                                              | Movement and control                                                                   |
+====================+================================================================+========================================================================================+
| Airplane           | Light aircraft and other assisted fixed-wing vehicles          | Assisted flight with pitch/bank limits, takeoff handling and ground/air blending.      |
+--------------------+----------------------------------------------------------------+----------------------------------------------------------------------------------------+
| Aerobatic Airplane | Aerobatic and freely maneuvering fixed-wing aircraft           | Pitch, roll and yaw rate control, including inverted flight.                           |
+--------------------+----------------------------------------------------------------+----------------------------------------------------------------------------------------+
| Jet                | Fighter jets and other fast fixed-wing aircraft                | Aerodynamic drag/lift, body-rate controls and G-limited response.                      |
+--------------------+----------------------------------------------------------------+----------------------------------------------------------------------------------------+
| Helicopter         | Helicopters and rotorcraft controlled by tilting the body      | Rotor-powered lift, pitch/roll movement, yaw and optional altitude hold.               |
+--------------------+----------------------------------------------------------------+----------------------------------------------------------------------------------------+
| Hover              | Drones, hovering platforms, flying cars and UFO-style vehicles | Direct forward/reverse movement, sideways thrust, vertical lift and assisted leveling. |
+--------------------+----------------------------------------------------------------+----------------------------------------------------------------------------------------+

A drone is a vehicle configuration rather than a separate profile. Use **Hover** for direct movement and strafing, or **Helicopter** when horizontal movement should come from body tilt. The number and placement of visible rotors are configured separately from the movement profile.

.. _evs-aircraft--create-an-aircraft:

Create an aircraft
------------------

1. Prepare a unit-scale vehicle root facing +Z with a Rigidbody and a suitable hull collider.
2. Select **Tools → EasyVehicleSystem → Add Vehicle**, then choose the desired flight preset. On an existing vehicle, choose the profile under **VehicleController → Setup → Drive mode** and configure its supporting modules.
3. Set mass and the profile's movement settings. Keep an enabled ``Drive`` module registered so the selected profile receives physics updates.
4. Assign the input source. Use ``KeyboardFlightInput`` for the supplied keyboard controls, ``ActionInput`` for configured actions or ``ExternalController`` for commands from your application. See :doc:`Input </Input>`.
5. Configure propulsion and, where required, engine ignition and fuel. Add landing-gear wheels only when the chosen setup needs them.
6. Apply vehicle configuration and confirm movement before adding cockpit animation, occupants and effects.

Hover and Helicopter profiles do not require Wheel Setup entries. For fixed-wing aircraft, configure the profile's **Use Landing Gear** option according to whether the airframe has physical gear wheels.

.. _evs-aircraft--airplanes-and-jets:

Airplanes and jets
------------------

Configure mass, engine power, thrust, lift speed and flight-control response in **Setup**. Create landing-gear wheels as described in :ref:`Getting started <evs-gettingstarted--create-your-first-wheel-vehicle>`. Turn **Drive** off on every gear wheel: aircraft propulsion acts on the body, not through driven wheels. Assign taxi steering and braking to the appropriate wheels.

Configure suspension, tire grip, braking and ground steering, then apply vehicle configuration. Check taxiing, takeoff, engine-off glide and landing before adding cockpit animation.

The shared wheel modules handle runway contact. ``AirplaneGroundContact`` exposes ``IsAirborne`` and ``FlightBlend``; takeoff contact grace and transition times control blending between ground and flight handling. Tire smoke, marks and audio use the same contact feedback as ground vehicles.

.. _evs-aircraft--tune-the-flight-envelope:

Tune the flight envelope
------------------------

Start with mass, thrust, lift speed and maximum speed. Verify takeoff before changing attitude response. Use the drive profile's aircraft engine, gear-suspension, grip and ground-steering settings: Configure reapplies those values to the relevant modules.

Airplane uses assisted attitude limits; Aerobatic Airplane and Jet use body-rate controls for rolls and inverted flight. Jet adds aerodynamic drag/lift and a G-limited response. Tune low-speed authority separately from high-speed response.

Use Landing Gear requires configured wheels. For a wheel-free airframe disable it explicitly and check the hull contact/flight path. For retraction, keep wheel definitions authored and let LandingGear manage contact availability.

.. _evs-aircraft--helicopters:

Helicopters
-----------

Choose **Helicopter** and tune the following settings in its drive profile:

-  **Acceleration** sets the vertical control authority and the basis for rotor-tilt movement. **Tilt Acceleration Multiplier** adjusts horizontal acceleration from body tilt.
-  **Compensate Gravity** supplies powered lift against gravity. **Vertical Damping** controls climb/descent damping, while **Drag** slows body motion.
-  **Automatic Leveling**, **Attitude Strength** and **Attitude Input Scale** shape the pitch/roll response. **Yaw Acceleration** controls turning around the vertical axis.
-  **Hold Altitude** captures the current height after releasing ascend/descend. With automatic leveling enabled, neutral movement input also brakes horizontal drift. It holds height and damps motion; it does not return the helicopter to a saved horizontal position.

Helicopter configuration ensures a ``Propulsion`` module exists. Set its **Spin Up Seconds** and **Spin Down Seconds**, then assign the main and tail rotor meshes in its propeller entries. Start the engine and allow the rotor to spool up before expecting full lift. Altitude hold requires a running engine and a nearly fully spooled rotor; stopping the engine releases the hold, and lift decreases as the rotor slows.

``KeyboardFlightInput`` maps W/S to pitch, A/D to roll, Q/E to yaw and Shift/Ctrl to ascend/descend. For custom controls, supply ``Command.Pitch``, ``Roll``, ``Yaw`` and ``Lift``. Configure the rotor axes and direction so visible rotation matches the model.

.. _evs-aircraft--drones-and-hover-vehicles:

Drones and hover vehicles
-------------------------

Choose **Hover** for a drone, hovering platform or flying car that should move directly along its forward and sideways axes. Configure:

-  **Acceleration** for horizontal thrust and lift commands, **Drag** for resistance, and **Yaw Acceleration / Yaw Damping** for turning.
-  **Compensate Gravity** for powered support, **Vertical Damping** for climb/descent damping, and **Maximum Ascent / Descent Acceleration** for vertical correction limits.
-  **Automatic Leveling**, **Attitude Strength**, **Body Tilt Degrees** and **Body Tilt Response** for the hull's assisted attitude and lean.
-  **Surface Support**, **Height**, **Spring**, **Damping** and **Ground Mask** for minimum clearance above nearby surfaces. Height is a ground-clearance setting, not an absolute flight-altitude target. Lift commands still allow ascent above the surface-support region.

With neutral lift input, gravity compensation and damping reduce vertical drift. Hover does not use the Helicopter profile's captured-altitude hold. If an Engine is installed, its running state controls whether the Hover profile applies powered movement.

Hover configuration ensures ``HoverVisuals`` exists. Add rotor or engine mounts to its tilt entries and set their neutral poses. For spinning rotors, add/configure ``Propulsion`` and assign each visible rotor separately. Wheel Tilt Response and wheel thrust/steering tilt settings control visual wheel lean on hover-capable cars; they do not change the wheel's authored neutral orientation.

``KeyboardFlightInput`` uses W/S for forward/reverse thrust, A/D for yaw, Q/E for sideways movement and Shift/Ctrl for ascend/descend. Custom providers use ``Command.Throttle``, ``Steering`` or ``Yaw``, ``Strafe`` and ``Lift``.

For a drive/hover vehicle, register both strategies in ``ProfileSwitcher`` and assign a bidirectional ``HoverDriveTransition`` to their IDs. The supplied Car/Porsche uses drive ↔ hover to fold wheels and restore road contact. See :doc:`Changing movement modes </Media>`.

.. _evs-aircraft--animate-cockpit-and-exterior-controls:

Animate cockpit and exterior controls
-------------------------------------

-  **Yoke:** assign the rotating pivot and pitch slide to ``YokeAnimator``. Place their neutral anchors at the actual column axes, then set roll angle, pitch travel and response.
-  **Stick:** use ``SteeringStickAnimator`` with ``StickSetup`` for pitch and roll. Assign the grip surface and its hand anchors. Configure a separate rest or throttle target for the other hand.
-  **Throttle:** configure ``ThrottleAnimator`` and the handle's moving pivot/neutral anchor. ``SetThrottle(0..1)`` controls visual position; ``FollowVehicle()`` resumes automatic presentation. Request engine thrust through the input provider.
-  **Control surfaces:** add ``AircraftControlSurface`` to each moving surface, configure its hinge, axis and direction, then register it in ``AircraftControlSurfaces.surfaces``.

``AircraftControlMotion`` supports rotation in degrees or translation in metres around an independent neutral anchor. ``SetValue(0..1)`` applies an absolute pose. Keep imported mesh corrections below the moving pivot.

Use ``AircraftControlSurfaces.SetControls(pitch, roll, yaw)`` for external presentation, ``FollowVehicle()`` for vehicle input, and ``SetFlaps`` / ``SetAirbrake`` for the additional channels. Surface animation does not change drive-profile aerodynamic authority.

Fit hand anchors and grip thickness to your control geometry and character; see :doc:`Seats and handles </SeatsAndHandles>` and :doc:`Grip calibration </SteeringHandGrip>`. Use the seated preview after editing the targets.

.. _evs-aircraft--retractable-landing-gear:

Retractable landing gear
------------------------

1. Add ``LandingGear`` and assign its native WheelCollider list.
2. Add a ``LandingGearPart`` for each moving strut, door or link and register the parts on LandingGear.
3. Assign each part's moving mesh and independent pivot anchor. Set its rotation axis or translation direction, retraction travel, duration and extension/retraction delays.
4. Use **Use current model pose as deployed (0)** to capture the reference pose. Preview the entire sequence, including doors and wheel clearance.
5. Configure the ground-contact/clearance interlock. Check deployment and retraction in flight and rejection on the ground.

**Preview retraction** and ``SetRetraction(0..1)`` use **0 deployed / 1 retracted**. The part's ``SetValue`` and ``DeployedFraction`` use **1 deployed / 0 retracted**. ``maximum`` sets signed retraction travel from the deployed pose; ``minimum`` is not used for gear motion.

``SetDeployed(bool)`` and ``Toggle()`` report whether a request was accepted. ``State``, ``RequestedDeployed``, ``IsDeployed``, ``IsGroundLocked`` and ``StateChanged`` support custom controls and instruments. Wheel contact is enabled at the fully deployed endpoint; hull colliders supply belly contact with the gear raised.

For explicit reset, ``ResetGear(bool deployed)`` applies the requested state immediately, bypassing the ground interlock. Reserve this for reset or spawn logic.

.. _evs-aircraft--hinged-gear-suspension:

Hinged gear suspension
----------------------

Add ``LandingGearSuspension`` and configure its ``parts``. Each entry references a LandingGearPart, native WheelCollider, hinge axis and signed maximum opening angle. Set ``authoredAngle`` to the opening already present in the deployed model, or zero for a straight leg.

Tune **Spring Torque** in N·m/rad, **Damping Torque** in N·m·s/rad and **Angular Inertia** in kg·m². The native wheel supports the aircraft; contact load also bends the configured hinge. Check hinge limits and wheel alignment throughout suspension travel.

``IsStraight`` indicates readiness for retraction. ``ResetSuspension()`` clears displacement and angular velocity. Coordinate this with gear reset and vehicle teleport in application reset logic.

.. _evs-aircraft--instruments-sound-and-effects:

Instruments, sound and effects
------------------------------

``AircraftHud`` publishes telemetry and ``Changed``, can bind a controller with ``Bind``, and exposes the landing gear. Assign ``customTexture`` for your own cockpit display. Subscribe to vehicle telemetry for custom airspeed, altitude, attitude and G-load instruments; see :doc:`API </API>`.

Assign an engine sound profile for the selected flight mode. Use ``Propulsion`` for visible propellers and rotors, and optional ``PropulsionJets`` for aircraft outlets. Configure emission, particle prefab/material and propulsion-spool response independently of mechanical thrust. See :doc:`Audio </Audio>` and :doc:`Particles </Particles>`.

For supplied keyboard bindings and example aircraft, see :doc:`Demo </Demo>`. For custom input, see :doc:`Input </Input>`.

For detailed flight, rotorcraft and landing-gear behavior, see :doc:`Aircraft scripting </Scripting/Aircraft>`.
