.. _evs-api-aircraft--flight-and-landing-gear-api:

Flight and landing gear API
===========================

Read :doc:`the system explanation </Scripting/Aircraft>` for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from ``MonoBehaviour``, ``Object`` or ``ScriptableObject`` are documented by Unity.

.. _evs-api-aircraft--types:

Types
-----

-  :ref:`AerobaticAirplaneProfile <evs-api-aircraft--aerobaticairplaneprofile>`
-  :ref:`AircraftControlSurface <evs-api-aircraft--aircraftcontrolsurface>`
-  :ref:`AircraftControlSurfaces <evs-api-aircraft--aircraftcontrolsurfaces>`
-  :ref:`AircraftSurfaceType <evs-api-aircraft--aircraftsurfacetype>`
-  :ref:`AirplaneGroundContact <evs-api-aircraft--airplanegroundcontact>`
-  :ref:`AirplaneProfile <evs-api-aircraft--airplaneprofile>`
-  :ref:`HelicopterProfile <evs-api-aircraft--helicopterprofile>`
-  :ref:`HoverVisuals <evs-api-aircraft--hovervisuals>`
-  :ref:`HoverVisuals.TiltMount <evs-api-aircraft--hovervisualstiltmount>`
-  :ref:`JetProfile <evs-api-aircraft--jetprofile>`
-  :ref:`LandingGear <evs-api-aircraft--landinggear>`
-  :ref:`LandingGearPart <evs-api-aircraft--landinggearpart>`
-  :ref:`LandingGearPartType <evs-api-aircraft--landinggearparttype>`
-  :ref:`LandingGearState <evs-api-aircraft--landinggearstate>`
-  :ref:`LandingGearSuspension <evs-api-aircraft--landinggearsuspension>`
-  :ref:`LandingGearSuspensionPart <evs-api-aircraft--landinggearsuspensionpart>`
-  :ref:`Propulsion <evs-api-aircraft--propulsion>`
-  :ref:`Propulsion.Propeller <evs-api-aircraft--propulsionpropeller>`

.. _evs-api-aircraft--aerobaticairplaneprofile:

AerobaticAirplaneProfile
------------------------

**Runtime/Drive/Profiles/AerobaticAirplaneProfile.cs**

Defines body-rate airplane control without auto-leveling.

**Inherits / implements:** :ref:`AirplaneProfile <evs-api-aircraft--airplaneprofile>`.

.. _evs-api-aircraft--methods:

Methods
~~~~~~~

+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+
| Signature                                                     | Role and behavior                                                                                               | Arguments and result                                               |
+===============================================================+=================================================================================================================+====================================================================+
| ``public AerobaticAirplaneProfile()``                         | Constructs ``AerobaticAirplaneProfile`` with the supplied initial state.                                        | **Returns:** New instance initialized from the supplied arguments. |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+
| ``public override void Configure(VehicleController vehicle)`` | Runs airplane family setup, then raises the native angular-velocity allowance for configured body-rate control. | ``vehicle`` — Vehicle context/owner receiving the operation.       |
+---------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------+

.. _evs-api-aircraft--state-and-configuration:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                      | Meaning                                                                                                                                   |
+=============================================+===========================================================================================================================================+
| ``public float pitchRate``                  | Authored pitch rate used by ``AerobaticAirplaneProfile``. Initial value: ``110f``.                                                        |
+---------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float rollRate``                   | Authored roll rate used by ``AerobaticAirplaneProfile``. Initial value: ``200f``.                                                         |
+---------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float yawRate``                    | Authored yaw rate used by ``AerobaticAirplaneProfile``. Initial value: ``45f``.                                                           |
+---------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float rateResponse``               | Authored rate response used by ``AerobaticAirplaneProfile``. Initial value: ``6f``.                                                       |
+---------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float minimumAirControlAuthority`` | Optional low-speed / thrust-vectoring control assistance. Zero requires airflow; higher values allow fighter-style recovery near a stall. |
+---------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-aircraft--aircraftcontrolsurface:

AircraftControlSurface
----------------------

**Runtime/Exterior/Aircraft/AircraftControlSurface.cs**

Configuration/implementation type for aircraft control surface within flight and landing gear.

**Inherits / implements:** :ref:`AircraftControlMotion <evs-api-interior--aircraftcontrolmotion>`.

.. _evs-api-aircraft--methods-1:

Methods
~~~~~~~

+-----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                           | Role and behavior                                                                                           | Arguments and result                                                                                                                                                                                                                                                                                     |
+=====================================================================================================+=============================================================================================================+==========================================================================================================================================================================================================================================================================================================+
| ``public virtual void SetControls(float pitch, float roll, float yaw, float flap, float airbrake)`` | Applies pitch/roll/yaw/flap/airbrake contributions through this surface's authored axis and motion mapping. | ``pitch`` — Normalized pitch input, or audio pitch multiplier in an audio operation. ``roll`` — Normalized roll input. ``yaw`` — Normalized yaw input. ``flap`` — Flap, interpreted by this operation in the declared type. ``airbrake`` — Airbrake, interpreted by this operation in the declared type. |
+-----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-aircraft--state-and-configuration-1:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------+-----------------------------------------------------------------------------------------------+
| Member                              | Meaning                                                                                       |
+=====================================+===============================================================================================+
| ``public AircraftSurfaceType type`` | Authored type used by ``AircraftControlSurface``.                                             |
+-------------------------------------+-----------------------------------------------------------------------------------------------+
| ``public Vector3 customMix``        | Pitch, roll and yaw mix for Custom; enables new airframe layouts without new controller code. |
+-------------------------------------+-----------------------------------------------------------------------------------------------+
| ``public bool invert``              | Authored invert used by ``AircraftControlSurface``.                                           |
+-------------------------------------+-----------------------------------------------------------------------------------------------+

.. _evs-api-aircraft--aircraftcontrolsurfaces:

AircraftControlSurfaces
-----------------------

**Runtime/Exterior/Aircraft/AircraftControlSurfaces.cs**

Presents the configured control-surface motion.

**Inherits / implements:** :ref:`ExteriorModule <evs-api-modules--exteriormodule>`.

.. _evs-api-aircraft--methods-2:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                  | Role and behavior                                                                                                                           | Arguments and result                                                                                                                                                                                                     |
+============================================================================================+=============================================================================================================================================+==========================================================================================================================================================================================================================+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Smooths external or command-following pitch/roll/yaw, applies surface geometry and publishes changed presentation.                          | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetControls(float pitch, float roll, float yaw)``                    | Takes external pitch/roll/yaw presentation ownership for configured control-surface entries; ``FollowVehicle`` restores mechanic-following. | ``pitch`` — Normalized pitch input, or audio pitch multiplier in an audio operation. ``roll`` — Normalized roll input. ``yaw`` — Normalized yaw input.                                                                   |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void FollowVehicle()``                                                    | Releases external presentation ownership and resumes vehicle-state following.                                                               | No arguments; no returned value.                                                                                                                                                                                         |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetFlaps(float value)``                                              | Updates normalized flap presentation for the configured aircraft control surfaces.                                                          | ``value`` — Requested state/value in this operation's domain; use its configured range/unit.                                                                                                                             |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetAirbrake(float value)``                                           | Updates the normalized aircraft airbrake presentation request.                                                                              | ``value`` — Requested state/value in this operation's domain; use its configured range/unit.                                                                                                                             |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-aircraft--events-and-inspector-callbacks:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| Declaration                                          | Trigger, payload and meaning                                                                                        |
+======================================================+=====================================================================================================================+
| ``public event Action<Vector3> ControlsChanged``     | When aircraft surface-control presentation changes. Payload: the component's pitch/roll/yaw Vector3 representation. |
+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public event Action<float> FlapsChanged``          | When flap presentation request changes. Payload: normalized flap value.                                             |
+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public event Action<float> AirbrakeChanged``       | When airbrake presentation request changes. Payload: normalized airbrake value.                                     |
+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public event Action<bool> ExternalControlChanged`` | When aircraft surface presentation changes external/follow-vehicle ownership. Payload: external-control bool.       |
+------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+

.. _evs-api-aircraft--state-and-configuration-2:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| Member                                            | Meaning                                                                                                          |
+===================================================+==================================================================================================================+
| ``public AircraftControlSurface[] surfaces``      | Authored surfaces used by ``AircraftControlSurfaces``. Initial value: ``Array.Empty<AircraftControlSurface>()``. |
+---------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``public float response``                         | Authored response used by ``AircraftControlSurfaces``. Initial value: ``5``.                                     |
+---------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``public float flaps``                            | Requested flap deployment from zero retracted to one fully extended.                                             |
+---------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``public float airbrake``                         | Requested aerodynamic brake deployment from zero to one.                                                         |
+---------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``public bool externalControl``                   | Uses explicit surface controls instead of the vehicle's current flight command.                                  |
+---------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }`` | Cross-category execution barrier used by the module pipeline.                                                    |
+---------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``public virtual Vector3 Controls { get; }``      | Read-only/resolved controls for ``AircraftControlSurfaces``.                                                     |
+---------------------------------------------------+------------------------------------------------------------------------------------------------------------------+

.. _evs-api-aircraft--aircraftsurfacetype:

AircraftSurfaceType
-------------------

**Runtime/Exterior/Aircraft/AircraftControlSurface.cs**

Defines the allowed aircraft surface type choices used by this topic.

.. _evs-api-aircraft--values:

Values
~~~~~~

-  ``Rudder``
-  ``LeftAileron``
-  ``RightAileron``
-  ``Elevator``
-  ``LeftElevator``
-  ``RightElevator``
-  ``Flap``
-  ``Airbrake``
-  ``Custom``

.. _evs-api-aircraft--airplanegroundcontact:

AirplaneGroundContact
---------------------

**Runtime/Drive/Air/AirplaneGroundContact.cs**

``Tracks`` ground support and ground/air authority blending.

**Inherits / implements:** :ref:`PhysicsModule <evs-api-modules--physicsmodule>`.

.. _evs-api-aircraft--methods-3:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                  | Role and behavior                                                                                               | Arguments and result                                                                                                                                                                                                     |
+============================================================================================+=================================================================================================================+==========================================================================================================================================================================================================================+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Counts operational native gear contacts, updates airborne/takeoff grace and blends ground/flight authority.     | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Configure(VehicleController vehicle)``                              | Restores prior contact material state, resets ground/air history and prepares applicable ground contact policy. | ``vehicle`` — Vehicle context/owner receiving the operation.                                                                                                                                                             |
+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool SupportsProfile(DriveProfile profile)``                             | Checks movement-family compatibility; this is independent of the Unity enabled flag.                            | ``profile`` — Movement/surface configuration, according to its declared type. **Returns:** ``true`` when the described condition holds; ``false`` otherwise.                                                             |
+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-aircraft--state-and-configuration-3:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| Member                                                            | Meaning                                                                                  |
+===================================================================+==========================================================================================+
| ``public virtual bool IsAirborne { get; protected set; }``        | Current is airborne predicate; read it instead of maintaining a second application flag. |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| ``public virtual float FlightBlend { get; protected set; }``      | Smoothed blend from ground behavior at zero to flight behavior at one.                   |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| ``public virtual int GroundedWheelCount { get; protected set; }`` | Read-only/resolved grounded wheel count for ``AirplaneGroundContact``.                   |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }``                 | Cross-category execution barrier used by the module pipeline.                            |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| ``public override int ExecutionOrder { get; }``                   | Default local priority within phase/category.                                            |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------+

.. _evs-api-aircraft--airplaneprofile:

AirplaneProfile
---------------

**Runtime/Drive/Profiles/AirplaneProfile.cs**

Defines assisted airplane movement and aircraft configuration.

**Inherits / implements:** :ref:`AirProfile <evs-api-driveprofiles--airprofile>`.

.. _evs-api-aircraft--methods-4:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                  | Role and behavior                                                                                                                   | Arguments and result                                                                                                                                                                                                       |
+============================================================================================+=====================================================================================================================================+============================================================================================================================================================================================================================+
| ``public AirplaneProfile()``                                                               | Constructs ``AirplaneProfile`` with the supplied initial state.                                                                     | **Returns:** New instance initialized from the supplied arguments.                                                                                                                                                         |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Configure(VehicleController vehicle)``                              | Ensures propulsion/ground-contact helpers and writes aircraft-owned engine, steering, braking, grip/travel and suspension settings. | ``vehicle`` — Vehicle context/owner receiving the operation.                                                                                                                                                               |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Applies assisted aircraft thrust/lift/attitude response using current speed and ground-contact authority.                           | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop.   |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override float ResolveDriveDemand(VehicleController vehicle, Command command)``   | Maps the command and strategy state to propulsion demand for surrounding mechanics.                                                 | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. **Returns:** Computed float in the operation's documented unit/domain. |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override float ResolveExternalDriveIntent(VehicleController vehicle)``            | Returns signed non-wheel propulsion intent used by shared coasting/contact policy.                                                  | ``vehicle`` — Vehicle context/owner receiving the operation. **Returns:** Computed float in the operation's documented unit/domain.                                                                                        |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-aircraft--state-and-configuration-4:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Member                                            | Meaning                                                                                                                         |
+===================================================+=================================================================================================================================+
| ``public float enginePowerKw``                    | Authored engine power kw used by ``AirplaneProfile``. Initial value: ``180f``.                                                  |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public float engineIdleRpm``                    | Authored engine idle rpm used by ``AirplaneProfile``. Initial value: ``700f``.                                                  |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public float engineMaximumRpm``                 | Authored engine maximum rpm used by ``AirplaneProfile``. Initial value: ``2700f``.                                              |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumSpeed``                     | Forward airspeed limit in m/s. Thrust fades out near this speed.                                                                |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public float liftSpeed``                        | Minimum forward airspeed for ground rotation/takeoff, in m/s.                                                                   |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public float stallSpeedRatio``                  | Authored stall speed ratio used by ``AirplaneProfile``. Initial value: ``0.55f``.                                               |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public float liftMultiplier``                   | Authored lift multiplier used by ``AirplaneProfile``. Initial value: ``1.12f``.                                                 |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumLiftAcceleration``          | Authored maximum lift acceleration used by ``AirplaneProfile``. Initial value: ``35f``.                                         |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public float flightPathResponse``               | Authored flight path response used by ``AirplaneProfile``. Initial value: ``2f``.                                               |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumAlignmentAcceleration``     | Authored maximum alignment acceleration used by ``AirplaneProfile``. Initial value: ``18f``.                                    |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public bool useLandingGear``                    | Keep native tires active in flight to detect touchdown without rebuilding wheel actors. Disable only for a wheel-free aircraft. |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool RequiresWheels { get; }``  | Whether this profile requires valid wheel definitions during configuration.                                                     |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public float groundAcceleration``               | Authored ground acceleration used by ``AirplaneProfile``. Initial value: ``6f``.                                                |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public float groundReverseSpeed``               | Ground-only reverse speed in m/s. Zero disables reverse thrust.                                                                 |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public float groundReverseAcceleration``        | Authored ground reverse acceleration used by ``AirplaneProfile``. Initial value: ``2f``.                                        |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public float groundHandlingAssistance``         | Shared steering yaw and lateral grip assistance, only while tires touch the ground.                                             |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public float groundYawResponse``                | Authored ground yaw response used by ``AirplaneProfile``. Initial value: ``4f``.                                                |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public float groundLateralResponse``            | Authored ground lateral response used by ``AirplaneProfile``. Initial value: ``5f``.                                            |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public float groundSteeringAngle``              | Authored ground steering angle used by ``AirplaneProfile``. Initial value: ``35f``.                                             |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public float minimumGroundTurnRadius``          | Authored minimum ground turn radius used by ``AirplaneProfile``. Initial value: ``6f``.                                         |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumGroundLateralAcceleration`` | Authored maximum ground lateral acceleration used by ``AirplaneProfile``. Initial value: ``5f``.                                |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public float groundSteeringRate``               | Authored ground steering rate used by ``AirplaneProfile``. Initial value: ``75f``.                                              |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public float serviceBrakeTorque``               | Authored service brake torque used by ``AirplaneProfile``. Initial value: ``3000f``.                                            |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public float parkingBrakeTorque``               | Authored parking brake torque used by ``AirplaneProfile``. Initial value: ``5000f``.                                            |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public float tireGrip``                         | Authored tire grip used by ``AirplaneProfile``. Initial value: ``1.3f``.                                                        |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public float suspensionTravel``                 | Authored suspension travel used by ``AirplaneProfile``. Initial value: ``0.18f``.                                               |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public float suspensionSpring``                 | Authored suspension spring used by ``AirplaneProfile``. Initial value: ``24000f``.                                              |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public float suspensionDamper``                 | Authored suspension damper used by ``AirplaneProfile``. Initial value: ``1785f``.                                               |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public float groundFriction``                   | Legacy hull-contact friction for wheel-free aircraft only. Gear tires use the shared Friction module.                           |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public float takeoffContactGrace``              | Seconds without tire contact before entering flight. Touchdown is detected on the first tire contact.                           |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public float flightTransitionTime``             | Authored flight transition time used by ``AirplaneProfile``. Initial value: ``0.35f``.                                          |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public float landingTransitionTime``            | Authored landing transition time used by ``AirplaneProfile``. Initial value: ``0.08f``.                                         |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public float groundRotationAuthority``          | Authored ground rotation authority used by ``AirplaneProfile``. Initial value: ``0.7f``.                                        |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumPitch``                     | Pitch attitude limit in the assisted profile. Aerobatic profiles use angular rates instead.                                     |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumBank``                      | Authored maximum bank used by ``AirplaneProfile``. Initial value: ``45f``.                                                      |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public float attitudeStrength``                 | Authored attitude strength used by ``AirplaneProfile``. Initial value: ``14f``.                                                 |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public float attitudeDamping``                  | Authored attitude damping used by ``AirplaneProfile``. Initial value: ``6f``.                                                   |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumControlAcceleration``       | Authored maximum control acceleration used by ``AirplaneProfile``. Initial value: ``20f``.                                      |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public float coordinatedTurn``                  | Authored coordinated turn used by ``AirplaneProfile``. Initial value: ``1.8f``.                                                 |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public float rudderRate``                       | Authored rudder rate used by ``AirplaneProfile``. Initial value: ``35f``.                                                       |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumTurnRate``                  | Authored maximum turn rate used by ``AirplaneProfile``. Initial value: ``70f``.                                                 |
+---------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-aircraft--helicopterprofile:

HelicopterProfile
-----------------

**Runtime/Drive/Profiles/HelicopterProfile.cs**

Configuration/implementation type for helicopter profile within flight and landing gear.

**Inherits / implements:** :ref:`AirProfile <evs-api-driveprofiles--airprofile>`.

.. _evs-api-aircraft--methods-5:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                  | Role and behavior                                                                                      | Arguments and result                                                                                                                                                                                                     |
+============================================================================================+========================================================================================================+==========================================================================================================================================================================================================================+
| ``public HelicopterProfile()``                                                             | Constructs ``HelicopterProfile`` with the supplied initial state.                                      | **Returns:** New instance initialized from the supplied arguments.                                                                                                                                                       |
+--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Configure(VehicleController vehicle)``                              | Ensures a Propulsion helper exists for helicopter presentation/spool integration.                      | ``vehicle`` — Vehicle context/owner receiving the operation.                                                                                                                                                             |
+--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Applies resistance, spool-dependent powered support, lift/height hold and commanded helicopter motion. | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-aircraft--state-and-configuration-5:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                      | Meaning                                                                                                                                                                                                                                 |
+=============================================+=========================================================================================================================================================================================================================================+
| ``public bool compensateGravity``           | Authored compensate gravity used by ``HelicopterProfile``. Initial value: ``true``.                                                                                                                                                     |
+---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool holdAltitude``                | Hold height after releasing ascend/descend and brake horizontal drift after releasing movement, without returning to a position. Requires a running engine and fully spooled rotor. Disable for the original vertical damping behavior. |
+---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool automaticLeveling``           | Authored automatic leveling used by ``HelicopterProfile``. Initial value: ``true``.                                                                                                                                                     |
+---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float verticalDamping``            | Authored vertical damping used by ``HelicopterProfile``. Initial value: ``1.5f``.                                                                                                                                                       |
+---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float attitudeStrength``           | Authored attitude strength used by ``HelicopterProfile``. Initial value: ``18``.                                                                                                                                                        |
+---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float attitudeInputScale``         | Pitch/roll input contribution to the target up vector.                                                                                                                                                                                  |
+---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float tiltAccelerationMultiplier`` | Multiplier for horizontal acceleration from rotor tilt.                                                                                                                                                                                 |
+---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float yawAcceleration``            | Authored yaw acceleration used by ``HelicopterProfile``. Initial value: ``5``.                                                                                                                                                          |
+---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-aircraft--hovervisuals:

HoverVisuals
------------

**Runtime/Exterior/Aircraft/HoverVisuals.cs**

Configuration/implementation type for hover visuals within flight and landing gear.

**Inherits / implements:** :ref:`ExteriorModule <evs-api-modules--exteriormodule>`.

.. _evs-api-aircraft--methods-6:

Methods
~~~~~~~

+------------------------------------------------------------------------------------+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                          | Role and behavior                                                       | Arguments and result                                                                                                                                                                                                                                 |
+====================================================================================+=========================================================================+======================================================================================================================================================================================================================================================+
| ``public override void Configure(VehicleController owner)``                        | Stores the vehicle whose hover transition geometry should be displayed. | ``owner`` — Unity/application owner whose identity controls this relationship or resource.                                                                                                                                                           |
+------------------------------------------------------------------------------------+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual Quaternion GetWheelTilt(WheelSetup wheel, HoverProfile profile)`` | Returns the wheel's hover-transition presentation tilt.                 | ``wheel`` — Native wheel or wheel adapter being configured/queried. ``profile`` — Movement/surface configuration, according to its declared type. **Returns:** Returned Quaternion; ownership remains as specified by the creating/lookup operation. |
+------------------------------------------------------------------------------------+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-aircraft--state-and-configuration-6:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------+---------------------------------------------------------------------------------------------------------------+
| Member                            | Meaning                                                                                                       |
+===================================+===============================================================================================================+
| ``public TiltMount[] tiltMounts`` | Optional hover engine mounts. Uses folded-wheel thrust, turn and strafe tilt without the wheel-fold rotation. |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------+

.. _evs-api-aircraft--hovervisualstiltmount:

HoverVisuals.TiltMount
----------------------

**Runtime/Exterior/Aircraft/HoverVisuals.cs**

Configuration/implementation type for tilt mount within flight and landing gear.

.. _evs-api-aircraft--state-and-configuration-7:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------+---------------------------------------------------------------------------------------+
| Member                             | Meaning                                                                               |
+====================================+=======================================================================================+
| ``public Transform transform``     | Authored transform used by ``TiltMount``.                                             |
+------------------------------------+---------------------------------------------------------------------------------------+
| ``public Quaternion restRotation`` | Authored rest rotation used by ``TiltMount``. Initial value: ``Quaternion.identity``. |
+------------------------------------+---------------------------------------------------------------------------------------+

.. _evs-api-aircraft--jetprofile:

JetProfile
----------

**Runtime/Drive/Profiles/JetProfile.cs**

Adds jet-specific aerodynamic response and limits.

**Inherits / implements:** :ref:`AerobaticAirplaneProfile <evs-api-aircraft--aerobaticairplaneprofile>`.

.. _evs-api-aircraft--methods-7:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                  | Role and behavior                                                                                 | Arguments and result                                                                                                                                                                                                     |
+============================================================================================+===================================================================================================+==========================================================================================================================================================================================================================+
| ``public JetProfile()``                                                                    | Constructs ``JetProfile`` with the supplied initial state.                                        | **Returns:** New instance initialized from the supplied arguments.                                                                                                                                                       |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Applies jet flight response, pressure/parasite/induced drag and bounded lift/trajectory behavior. | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual Vector3 PressureDragAcceleration(Transform frame, Vector3 velocity)``     | Evaluates jet pressure-drag acceleration from the supplied speed/state.                           | ``frame`` — Frame, interpreted by this operation in the declared type. ``velocity`` — World velocity in m/s. **Returns:** Returned Vector3; ownership remains as specified by the creating/lookup operation.             |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-aircraft--state-and-configuration-8:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------+----------------------------------------------------------------------------------------+
| Member                                 | Meaning                                                                                |
+========================================+========================================================================================+
| ``public float parasiteDrag``          | Forward parasite drag acceleration / speed squared, in 1/metres.                       |
+----------------------------------------+----------------------------------------------------------------------------------------+
| ``public float wingPressureDrag``      | Additional quadratic pressure drag for airflow across the wings / across the fuselage. |
+----------------------------------------+----------------------------------------------------------------------------------------+
| ``public float sidePressureDrag``      | Authored side pressure drag used by ``JetProfile``. Initial value: ``0.008f``.         |
+----------------------------------------+----------------------------------------------------------------------------------------+
| ``public float inducedDrag``           | Induced drag acceleration at one G; grows with aerodynamic load squared.               |
+----------------------------------------+----------------------------------------------------------------------------------------+
| ``public float referenceAirspeed``     | Authored reference airspeed used by ``JetProfile``. Initial value: ``100f``.           |
+----------------------------------------+----------------------------------------------------------------------------------------+
| ``public float pitchPathResponse``     | Authored pitch path response used by ``JetProfile``. Initial value: ``5f``.            |
+----------------------------------------+----------------------------------------------------------------------------------------+
| ``public float yawPathResponse``       | Authored yaw path response used by ``JetProfile``. Initial value: ``4f``.              |
+----------------------------------------+----------------------------------------------------------------------------------------+
| ``public float maximumG``              | Authored maximum g used by ``JetProfile``. Initial value: ``4.5f``.                    |
+----------------------------------------+----------------------------------------------------------------------------------------+
| ``public float stallAngle``            | Authored stall angle used by ``JetProfile``. Initial value: ``35f``.                   |
+----------------------------------------+----------------------------------------------------------------------------------------+
| ``public float coordinatedTurnAssist`` | Authored coordinated turn assist used by ``JetProfile``. Initial value: ``0.8f``.      |
+----------------------------------------+----------------------------------------------------------------------------------------+

.. _evs-api-aircraft--landinggear:

LandingGear
-----------

**Runtime/Exterior/Aircraft/LandingGear.cs**

Owns deployment sequencing and physical gear-contact availability.

**Inherits / implements:** :ref:`ExteriorModule <evs-api-modules--exteriormodule>`.

.. _evs-api-aircraft--methods-8:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                  | Role and behavior                                                                                                 | Arguments and result                                                                                                                                                                                                     |
+============================================================================================+===================================================================================================================+==========================================================================================================================================================================================================================+
| ``public override void Configure(VehicleController vehicle)``                              | Connects suspension, initializes authored deployment once and synchronizes gear-part/contact policy.              | ``vehicle`` — Vehicle context/owner receiving the operation.                                                                                                                                                             |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ResetGear(bool deployed)``                                           | Synchronizes gear state immediately for spawn/reset, bypassing ordinary request interlocks.                       | ``deployed`` — ``true`` requests deployment; ``false`` requests retraction.                                                                                                                                              |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Advances part delays/travel and gear state; retraction waits for unloaded suspension alignment before continuing. | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SetDeployed(bool deployed)``                                         | Requests landing-gear deployment/retraction subject to clearance, ground and alignment interlocks.                | ``deployed`` — ``true`` requests deployment; ``false`` requests retraction. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated.                |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool Toggle()``                                                           | Requests the opposite current body/switch/wiper/profile/gear state through the declaring component.               | **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated.                                                                                            |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-aircraft--events-and-inspector-callbacks-1:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| Declaration                                            | Trigger, payload and meaning                                                                                                                          |
+========================================================+=======================================================================================================================================================+
| ``public event Action<LandingGearState> StateChanged`` | When deployment sequencing changes ``LandingGearState``. Payload: actual sequence state; use this rather than treating request acceptance as arrival. |
+--------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-aircraft--state-and-configuration-9:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| Member                                                            | Meaning                                                                                       |
+===================================================================+===============================================================================================+
| ``public LandingGearPart[] parts``                                | Authored parts used by ``LandingGear``. Initial value: ``Array.Empty<LandingGearPart>()``.    |
+-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``public WheelCollider[] wheels``                                 | Authored wheels used by ``LandingGear``. Initial value: ``Array.Empty<WheelCollider>()``.     |
+-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``public bool initiallyDeployed``                                 | Authored initially deployed used by ``LandingGear``. Initial value: ``true``.                 |
+-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``public bool preventGroundRetraction``                           | Prevent retraction while tires touch the ground or the hull is within Ground Clearance Lock.  |
+-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``public LayerMask groundMask``                                   | Authored ground mask used by ``LandingGear``. Initial value: ``~0``.                          |
+-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``public float groundClearanceLock``                              | Authored ground clearance lock used by ``LandingGear``. Initial value: ``.6f``.               |
+-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``public virtual LandingGearState State { get; protected set; }`` | Read-only/resolved state for ``LandingGear``.                                                 |
+-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``public virtual bool RequestedDeployed { get; protected set; }`` | Read-only/resolved requested deployed for ``LandingGear``.                                    |
+-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``public virtual bool IsDeployed { get; }``                       | Current is deployed predicate; read it instead of maintaining a second application flag.      |
+-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }``                 | Cross-category execution barrier used by the module pipeline.                                 |
+-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``public override int ExecutionOrder { get; }``                   | Default local priority within phase/category.                                                 |
+-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``public virtual bool IsGroundLocked { get; }``                   | Current is ground locked predicate; read it instead of maintaining a second application flag. |
+-------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+

.. _evs-api-aircraft--landinggearpart:

LandingGearPart
---------------

**Runtime/Exterior/Aircraft/LandingGearPart.cs**

Maps deployment progress to a door/strut pose.

**Inherits / implements:** :ref:`AircraftControlMotion <evs-api-interior--aircraftcontrolmotion>`.

.. _evs-api-aircraft--methods-9:

Methods
~~~~~~~

+--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                      | Role and behavior                                                                                                                            | Arguments and result                                                                                                                                                                              |
+================================================================================+==============================================================================================================================================+===================================================================================================================================================================================================+
| ``public virtual void CaptureDeployedPose()``                                  | Captures the current gear-part pose as the fully deployed baseline.                                                                          | No arguments; no returned value.                                                                                                                                                                  |
+--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void SetValue(float normalized)``                            | Applies deployed fraction: 1 fully deployed, 0 fully retracted, retaining the captured deployed mesh offset and current suspension rotation. | ``normalized`` — Normalized value; the owner maps it to its configured range.                                                                                                                     |
+--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetRetraction(float amount)``                            | Applies landing-gear travel with zero deployed and one retracted.                                                                            | ``amount`` — Requested damage/repair amount in the mechanic's damage units.                                                                                                                       |
+--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Animate(bool deployed, float elapsed, float deltaTime)`` | Applies gear-part deployment animation using its authored motion mapping.                                                                    | ``deployed`` — ``true`` requests deployment; ``false`` requests retraction. ``elapsed`` — Elapsed operation time in seconds. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetImmediate(bool deployed)``                            | Synchronizes this part immediately to the requested deployed/retracted pose through its gear-part mapping.                                   | ``deployed`` — ``true`` requests deployment; ``false`` requests retraction.                                                                                                                       |
+--------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-aircraft--state-and-configuration-10:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------+----------------------------------------------------------------------+
| Member                                                            | Meaning                                                              |
+===================================================================+======================================================================+
| ``public LandingGearPartType type``                               | Authored type used by ``LandingGearPart``.                           |
+-------------------------------------------------------------------+----------------------------------------------------------------------+
| ``public float duration``                                         | Authored duration used by ``LandingGearPart``. Initial value: ``2``. |
+-------------------------------------------------------------------+----------------------------------------------------------------------+
| ``public float retractDelay``                                     | Delay before this gear part starts retraction, in seconds.           |
+-------------------------------------------------------------------+----------------------------------------------------------------------+
| ``public float extendDelay``                                      | Delay before this gear part starts extension, in seconds.            |
+-------------------------------------------------------------------+----------------------------------------------------------------------+
| ``public virtual float RetractionFraction { get; }``              | Gear-part travel from fully extended at zero to retracted at one.    |
+-------------------------------------------------------------------+----------------------------------------------------------------------+
| ``public virtual float DeployedFraction { get; protected set; }`` | Current deployed fraction: one deployed, zero retracted.             |
+-------------------------------------------------------------------+----------------------------------------------------------------------+

.. _evs-api-aircraft--landinggearparttype:

LandingGearPartType
-------------------

**Runtime/Exterior/Aircraft/LandingGearPart.cs**

Defines the allowed landing gear part type choices used by this topic.

.. _evs-api-aircraft--values-1:

Values
~~~~~~

-  ``Strut``
-  ``Door``
-  ``Link``
-  ``Custom``

.. _evs-api-aircraft--landinggearstate:

LandingGearState
----------------

**Runtime/Exterior/Aircraft/LandingGear.cs**

Defines the allowed landing gear state choices used by this topic.

.. _evs-api-aircraft--values-2:

Values
~~~~~~

-  ``Deployed``
-  ``Retracting``
-  ``Retracted``
-  ``Extending``

.. _evs-api-aircraft--landinggearsuspension:

LandingGearSuspension
---------------------

**Runtime/Exterior/Aircraft/LandingGearSuspension.cs**

Configuration/implementation type for landing gear suspension within flight and landing gear.

**Inherits / implements:** :ref:`ExteriorModule <evs-api-modules--exteriormodule>`.

.. _evs-api-aircraft--methods-10:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                  | Role and behavior                                                                                                         | Arguments and result                                                                                                                                                                                                     |
+============================================================================================+===========================================================================================================================+==========================================================================================================================================================================================================================+
| ``public override void Configure(VehicleController vehicle)``                              | Connects ``LandingGear`` and prepares changed runtime leg state while preserving authored deployed geometry in Edit Mode. | ``vehicle`` — Vehicle context/owner receiving the operation.                                                                                                                                                             |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ResetSuspension()``                                                  | Clears load-driven landing-gear hinge displacement and velocity.                                                          | No arguments; no returned value.                                                                                                                                                                                         |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Uses native wheel load to advance each leg's bounded angular spring/damper/inertia model.                                 | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-aircraft--state-and-configuration-11:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| Member                                            | Meaning                                                                                                        |
+===================================================+================================================================================================================+
| ``public LandingGearSuspensionPart[] parts``      | Authored parts used by ``LandingGearSuspension``. Initial value: ``Array.Empty<LandingGearSuspensionPart>()``. |
+---------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }`` | Cross-category execution barrier used by the module pipeline.                                                  |
+---------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| ``public override int ExecutionOrder { get; }``   | Default local priority within phase/category.                                                                  |
+---------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
| ``public virtual bool IsStraight { get; }``       | Current is straight predicate; read it instead of maintaining a second application flag.                       |
+---------------------------------------------------+----------------------------------------------------------------------------------------------------------------+

.. _evs-api-aircraft--landinggearsuspensionpart:

LandingGearSuspensionPart
-------------------------

**Runtime/Exterior/Aircraft/LandingGearSuspensionPart.cs**

Describes load-driven hinge response for a gear part.

**Inherits / implements:** ``MonoBehaviour``.

.. _evs-api-aircraft--state-and-configuration-12:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                              | Meaning                                                                                                                                                                                     |
+=====================================+=============================================================================================================================================================================================+
| ``public LandingGearPart gearPart`` | Authored gear part used by ``LandingGearSuspensionPart``.                                                                                                                                   |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public WheelCollider wheel``      | Authored wheel used by ``LandingGearSuspensionPart``.                                                                                                                                       |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector3 localAxis``        | Authored local axis used by ``LandingGearSuspensionPart``. Initial value: ``Vector3.forward``.                                                                                              |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumAngle``       | Authored maximum angle used by ``LandingGearSuspensionPart``. Initial value: ``28``.                                                                                                        |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float authoredAngle``      | Angle already present in the authored deployed mesh, in degrees.                                                                                                                            |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float springTorque``       | Rotational spring response is integrated by ``LandingGearSuspension``; ``authoredAngle`` describes the existing deployed geometry and must not be captured from a compressed animated pose. |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float dampingTorque``      | Authored damping torque used by ``LandingGearSuspensionPart``. Initial value: ``3500``.                                                                                                     |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float angularInertia``     | Authored angular inertia used by ``LandingGearSuspensionPart``. Initial value: ``500``.                                                                                                     |
+-------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-aircraft--propulsion:

Propulsion
----------

**Runtime/Exterior/Aircraft/Propulsion.cs**

Animates supported propeller/rotor geometry; extensible for boat presentation.

**Inherits / implements:** :ref:`ExteriorModule <evs-api-modules--exteriormodule>`.

.. _evs-api-aircraft--methods-11:

Methods
~~~~~~~

+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                      | Role and behavior                                                                                  | Arguments and result                                                                                                                                         |
+================================================================+====================================================================================================+==============================================================================================================================================================+
| ``public override void Configure(VehicleController owner)``    | Stores the owner and resolves missing hull/engine references used by spool/propeller presentation. | ``owner`` — Unity/application owner whose identity controls this relationship or resource.                                                                   |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool SupportsProfile(DriveProfile profile)`` | Checks movement-family compatibility; this is independent of the Unity enabled flag.               | ``profile`` — Movement/surface configuration, according to its declared type. **Returns:** ``true`` when the described condition holds; ``false`` otherwise. |
+----------------------------------------------------------------+----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-aircraft--events-and-inspector-callbacks-2:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| Declaration                                 | Trigger, payload and meaning                                                                                                     |
+=============================================+==================================================================================================================================+
| ``public event Action<float> SpeedChanged`` | When resolved propulsion presentation speed changes. Payload: the component's current speed value; it does not set engine power. |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-aircraft--state-and-configuration-13:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| Member                                                           | Meaning                                                                                  |
+==================================================================+==========================================================================================+
| ``public Engine engine``                                         | Authored engine used by Propulsion.                                                      |
+------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| ``public Propeller[] propellers``                                | Authored propellers used by Propulsion. Initial value: ``Array.Empty<Propeller>()``.     |
+------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| ``public float spinUpSeconds``                                   | Authored spin up seconds used by Propulsion. Initial value: ``1.8f``.                    |
+------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| ``public float spinDownSeconds``                                 | Authored spin down seconds used by Propulsion. Initial value: ``2.4f``.                  |
+------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| ``public virtual float SpeedNormalized { get; protected set; }`` | Resolved normalized propeller/rotor presentation speed, separate from mechanical thrust. |
+------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| ``public Transform rotor``                                       | Authored rotor used by Propulsion.                                                       |
+------------------------------------------------------------------+------------------------------------------------------------------------------------------+

.. _evs-api-aircraft--propulsionpropeller:

Propulsion.Propeller
--------------------

**Runtime/Exterior/Aircraft/Propulsion.cs**

Configuration/implementation type for propeller within flight and landing gear.

.. _evs-api-aircraft--state-and-configuration-14:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| Member                                | Meaning                                                                                                                        |
+=======================================+================================================================================================================================+
| ``public Transform transform``        | Authored transform used by Propeller.                                                                                          |
+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector3 localAxis``          | Authored local axis used by Propeller. Initial value: ``Vector3.up``.                                                          |
+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public float degreesPerSecond``     | Authored degrees per second used by Propeller. Initial value: ``900``.                                                         |
+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public bool useEngineRpm``          | Derive rotor speed from engine RPM instead of fixed degrees per second.                                                        |
+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public bool onlyWithThrust``        | Scale rotation by throttle and enabled maneuver demands. No demand stops the shaft. Works with fixed speed or engine RPM.      |
+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public bool reverseWithThrust``     | Reverse rotation for negative throttle. Independent of Only With Thrust and Use Engine Rpm.                                    |
+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public bool instantThrustResponse`` | Bypass smoothing of control-driven shaft demand to match immediate thrust forces. Engine-only rotation keeps its engine spool. |
+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public bool spinWithSteering``      | Include combined Steering/Yaw demand, including turning at rest. Forward/reverse throttle determines shaft direction.          |
+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public bool spinWithLift``          | Include vertical Lift demand in shaft rotation.                                                                                |
+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public bool spinWithPitch``         | Include Pitch demand in shaft rotation.                                                                                        |
+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public bool onlyInWater``           | Require an enabled water provider/fallback and at least partial hull immersion. A dry hull stops shaft rotation.               |
+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public float maneuverSpeed``        | Shaft speed at full steering, lift or pitch demand; throttle can request a higher speed.                                       |
+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public float rpmRatio``             | Rotor RPM / engine RPM. Negative values reverse rotation.                                                                      |
+---------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
