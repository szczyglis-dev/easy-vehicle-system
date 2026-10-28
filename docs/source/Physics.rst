.. _evs-physics--vehicle-physics:

Vehicle physics
===============

Easy Vehicle System combines Unity physics with configurable vehicle mechanics. ``VehicleController`` owns the chassis ``Rigidbody``, reads input, runs the active ``DriveProfile`` and schedules the installed modules. Wheel vehicles use ``WheelCollider`` contacts for suspension and tire forces. Flying and water vehicles use their profile's propulsion and support model, with optional wheels for ground contact.

Start with correct geometry and a stable chassis, then tune suspension, propulsion, steering and assists in that order. Effects and visible suspension parts should follow the resulting motion.

.. _evs-physics--chassis-coordinates-and-units:

Chassis, coordinates and units
------------------------------

Keep the vehicle root at unit scale, with local +Z forward and +Y up. Put model-specific scaling and orientation corrections on visual children. Body colliders define the chassis shape for impacts; wheel contacts provide tire support separately.

+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| Setting or property                                             | Purpose                                                                                                         |
+=================================================================+=================================================================================================================+
| ``VehicleController.Body``                                      | The vehicle's physical ``Rigidbody``; use it to read velocity or apply additional forces from custom mechanics. |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``VehicleController.settings.mass``                             | Chassis mass in kilograms. Configuration applies a minimum of 100 kg.                                           |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``VehicleController.settings.centerOfMass``                     | Explicit local center of mass relative to the vehicle root, in metres.                                          |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``VehicleController.wheelSetup``                                | Authored wheel geometry, references, roles and multipliers.                                                     |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``VehicleController.Wheels``                                    | Runtime wheel adapters for the configured vehicle.                                                              |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``VehicleController.SpeedKph`` / ``VehicleController.SpeedMph`` | Speed magnitude in km/h or mph, including lateral and vertical motion.                                          |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``VehicleController.ForwardSpeed``                              | Signed velocity along the vehicle's forward axis, in m/s.                                                       |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``VehicleController.GetSpeed(SpeedUnit unit)``                  | Speed magnitude in the requested unit.                                                                          |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+

Distances and suspension travel use metres, forces use newtons, and torque uses N·m. Speed fields with a unit selector can be authored in km/h, mph or m/s; changing the displayed unit preserves the physical value. See :doc:`Speed units </SpeedUnits>`.

A lower center of mass can reduce rollover tendency, but it cannot correct an incorrect wheelbase, intersecting colliders or insufficient suspension travel. Physical passengers and articulated parts have their own bodies and can affect the loaded vehicle's behavior.

.. _evs-physics--wheel-geometry-and-contact:

Wheel geometry and contact
--------------------------

Add each wheel to ``VehicleController.wheelSetup`` and assign its ``WheelCollider``, visual, radius, width and mass. Select the steering, driving, service-brake and handbrake roles for that wheel. Each collider must belong to the vehicle's ``Rigidbody`` and appear only once in the setup.

``WheelCollider`` supplies spring/damper support, slip-based tire friction and wheel rotation. Chassis colliders handle body impacts. Ordinary collider friction materials do not replace the tire-friction configuration: use ``settings.grip`` and ``Surface`` components to tune tire grip on different ground materials.

Native wheel contact uses a raycast-based approximation. Sharp steps, thin obstacles and high-speed terrain changes may need additional support:

-  ``ContactEnvelope`` adds sampled contact support around the tire's contact region. Configure its ground filtering, sampling and correction limits for the terrain.
-  Solid-tire helpers add physical collision support for cases where native wheel contact alone is insufficient.
-  Body collision proxies should leave room for normal wheel travel instead of catching the ground before the tires do.

Set up and tune these helpers after the native wheel geometry works on flat ground. See :doc:`Tire contact </ContactEnvelope>`, :doc:`Tire collision </TireCollision>` and :doc:`Ground surfaces </Surfaces>`.

.. _evs-physics--suspension-and-body-support:

Suspension and body support
---------------------------

``Suspension`` configures the native wheel springs, damping and travel. Use its fields rather than maintaining a second set of values directly on the same ``WheelCollider``.

+---------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| Field                                       | What to tune                                                                                                |
+=============================================+=============================================================================================================+
| ``settings.suspensionTravel``               | Available suspension stroke in metres. Leave room for compression and extension at the intended load.       |
+---------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| ``Suspension.spring``                       | Spring stiffness in N/m. Increase it when the intended load compresses the suspension too far.              |
+---------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| ``Suspension.damper``                       | Damping in N·s/m. Increase gradually to reduce repeated oscillation after the springs support the load.     |
+---------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| ``Suspension.targetPosition``               | Normalized native spring target, from 0 to 1. Tune together with travel and loaded ride height.             |
+---------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| ``Suspension.automaticForceApplication``    | Enables placement of wheel-force application points relative to the center of mass.                         |
+---------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| ``Suspension.forceOffsetBelowCenterOfMass`` | Offset used by automatic force application, in metres.                                                      |
+---------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| ``Suspension.degressiveDamping``            | Limits the growth of damping force at high suspension stroke speeds.                                        |
+---------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| ``Suspension.damperBlowoffSpeed``           | Stroke-speed threshold for degressive damping, in m/s.                                                      |
+---------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| ``Suspension.arcadeBumpDamping``            | Optional assistance that damps excessive upward body motion while the wheels remain sufficiently supported. |
+---------------------------------------------+-------------------------------------------------------------------------------------------------------------+

First check the resting vehicle on level ground, then braking, cornering and a small bump. Add ``AntiRoll`` after basic suspension support works. A visual ``ShockAbsorber`` or linkage does not provide physical support unless its corresponding physics override is configured. Use only one shock physics override per wheel.

Disabling a setup component does not necessarily undo values already written to native physics components. Reconfigure the vehicle when changing persistent setup. See :doc:`Suspension setup </Suspension>` and the :doc:`suspension scripting reference </Scripting/Suspension>`.

.. _evs-physics--propulsion-brakes-and-steering:

Propulsion, brakes and steering
-------------------------------

Direct wheel driving uses ``settings.motorTorque`` as a wheel-torque budget distributed across driven wheels. ``settings.topSpeedKph`` supplies a soft drive-torque fade; it does not forcibly clamp chassis velocity. Descents, impacts and external forces can therefore carry the vehicle beyond that speed.

With a gearbox, engine torque and RPM, gear ratios, drivetrain efficiency and configured power or acceleration limits determine the available wheel torque. Optional clutch and flywheel behavior adds coupling and rotational inertia. ``Differential`` modes redistribute or couple axle torque; they are not exact constraints on wheel angular velocity.

``Brakes`` applies braking through the configured wheel roles and multipliers. ``settings.brakeTorque`` controls the service-brake torque budget. Set up service brakes and handbrakes deliberately, especially for vehicles with several axles.

``Steering`` drives the configured steering wheels using ``settings.steeringAngle``, steering response and per-wheel multipliers. ``Steering.speedSensitiveSteering`` can reduce steering authority with speed; ``Steering.advancedSteeringGeometry`` enables the optional radius/grip limits and Ackermann geometry. Negative per-wheel steering multipliers support counter-steering axles.

Tune the visible steering-wheel travel separately from road-wheel angles. See :doc:`Vehicle tuning </VehicleTuning>`, :doc:`Gearbox </Gearbox>`, :doc:`Clutch </Clutch>` and :doc:`Drive dynamics </Scripting/DriveDynamics>`.

.. _evs-physics--driving-assists-and-other-vehicle-types:

Driving assists and other vehicle types
---------------------------------------

``TractionControl`` and ``DrivingAssists`` provide configurable slip and stability assistance. Establish suitable geometry, grip and suspension before increasing assistance. ``MotorcycleBalance`` provides assisted balance and lean for motorcycles.

The active ``DriveProfile`` determines the vehicle's movement model. Hover, aircraft and water profiles apply their own support and propulsion behavior; changing only a wheeled vehicle's torque settings does not turn it into a flying or floating vehicle. See :doc:`Drive profiles </DriveProfiles>`, :doc:`Aircraft </Aircraft>`, :doc:`Water </Water>` and :doc:`Tracked vehicles </Tracked>` for the corresponding setup.

These systems are intended for configurable game handling. Motorcycle balance, hover support, aerodynamics and buoyancy are assisted gameplay models rather than engineering simulations.

.. _evs-physics--apply-and-inspect-changes:

Apply and inspect changes
-------------------------

1. Configure the chassis and ``wheelSetup`` outside Play Mode.
2. Click **Apply vehicle configuration** in the controller Inspector. From code, call ``VehicleController.ApplyConfiguration()`` or use ``VehicleController.TryApplyConfiguration(out string error)`` to handle validation failure.
3. Check the controller's **Live** values and the actual wheel contacts. Distinguish missing input from missing traction or a drivetrain limit.
4. Compare rest, acceleration, braking, reverse, a tight turn, a fast turn, a slope and a landing with the intended load.
5. Save persistent changes outside Play Mode and check a fresh instance of the vehicle.

When tuning high-speed collisions or many articulated bodies, review Unity's fixed timestep, collision-detection mode and solver settings for your scene. Smaller timesteps and more solver work cost CPU time; choose settings using the target platform and expected vehicle count. See :doc:`Performance </Performance>` and :doc:`Troubleshooting </Troubleshooting>`.

.. _evs-physics--physical-limits-and-reset-behavior:

Physical limits and reset behavior
----------------------------------

-  The package does not simulate tire temperature or wear, full drivetrain elasticity, synchronizer mechanics, engine stalling or clutch heat/wear.
-  Physical passengers and detachable parts use native bodies and joints. Their configured force limits and reachable anchors determine when they yield or release.
-  Mesh deformation affects supported readable visual meshes. It does not continuously reshape collision proxies or skinned meshes.
-  Tire marks are bounded contact ribbons, with the limitations described in their setup guide.
-  ``VehicleController.Teleport(position, rotation)`` repositions the vehicle; it does not repair dents, replace detached parts or rearm weapons. Supply the repair or respawn policy your game needs.

See :doc:`Damage </Damage>`, :doc:`Passengers </Passengers>` and :doc:`Scripting </Scripting>` for integration with your gameplay.
