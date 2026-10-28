.. _evs-api-events--telemetry-and-feedback-events-api:

Telemetry and feedback events API
=================================

Read :doc:`the system explanation </Scripting/Events>` for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from ``MonoBehaviour``, ``Object`` or ``ScriptableObject`` are documented by Unity.

.. _evs-api-events--types:

Types
-----

-  :ref:`EffectEvent <evs-api-events--effectevent>`
-  :ref:`EventIds <evs-api-events--eventids>`
-  :ref:`Events <evs-api-events--events>`
-  :ref:`Feedback <evs-api-events--feedback>`
-  :ref:`Impact <evs-api-events--impact>`
-  :ref:`Telemetry <evs-api-events--telemetry>`
-  :ref:`WheelContact <evs-api-events--wheelcontact>`

.. _evs-api-events--effectevent:

EffectEvent
-----------

**Runtime/Effects/Feedback/Events.cs**

Value data for effect event; its fields are listed below.

.. _evs-api-events--methods:

Methods
~~~~~~~

+----------------------------------------------------------------------+-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                            | Role and behavior                                           | Arguments and result                                                                                                                                                                                                                                                                                  |
+======================================================================+=============================================================+=======================================================================================================================================================================================================================================================================================================+
| ``public EffectEvent(string id, float intensity, Vector3 position)`` | Constructs ``EffectEvent`` with the supplied initial state. | ``id`` — Case-sensitive authored body-part identifier. ``intensity`` — Intensity, interpreted by this operation in the declared type. ``position`` — Requested point or switch detent; see its declared type and owning operation. **Returns:** New instance initialized from the supplied arguments. |
+----------------------------------------------------------------------+-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-events--state-and-configuration:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------+----------------------------------------------------------+
| Member                               | Meaning                                                  |
+======================================+==========================================================+
| ``public readonly string Id``        | Read-only id stored by this snapshot/data object.        |
+--------------------------------------+----------------------------------------------------------+
| ``public readonly float Intensity``  | Read-only intensity stored by this snapshot/data object. |
+--------------------------------------+----------------------------------------------------------+
| ``public readonly Vector3 Position`` | World-space position carried by the effect event.        |
+--------------------------------------+----------------------------------------------------------+

.. _evs-api-events--eventids:

EventIds
--------

**Runtime/Effects/Feedback/Events.cs**

Configuration/implementation type for event ids within telemetry and feedback events.

.. _evs-api-events--state-and-configuration-1:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------+--------------------------------------------------------------------------------------+
| Member                                | Meaning                                                                              |
+=======================================+======================================================================================+
| ``public const string Overturned``    | Authored overturned used by ``EventIds``. Initial value: ``"vehicle.overturned"``.   |
+---------------------------------------+--------------------------------------------------------------------------------------+
| ``public const string Recovered``     | Authored recovered used by ``EventIds``. Initial value: ``"vehicle.recovered"``.     |
+---------------------------------------+--------------------------------------------------------------------------------------+
| ``public const string Reset``         | Authored reset used by ``EventIds``. Initial value: ``"vehicle.reset"``.             |
+---------------------------------------+--------------------------------------------------------------------------------------+
| ``public const string LightsChanged`` | Authored lights changed used by ``EventIds``. Initial value: ``"lights.changed"``.   |
+---------------------------------------+--------------------------------------------------------------------------------------+
| ``public const string Collision``     | Authored collision used by ``EventIds``. Initial value: ``"collision"``.             |
+---------------------------------------+--------------------------------------------------------------------------------------+
| ``public const string GearChanged``   | Authored gear changed used by ``EventIds``. Initial value: ``"gear.changed"``.       |
+---------------------------------------+--------------------------------------------------------------------------------------+
| ``public const string SkidStarted``   | Authored skid started used by ``EventIds``. Initial value: ``"tires.skid.started"``. |
+---------------------------------------+--------------------------------------------------------------------------------------+
| ``public const string SkidStopped``   | Authored skid stopped used by ``EventIds``. Initial value: ``"tires.skid.stopped"``. |
+---------------------------------------+--------------------------------------------------------------------------------------+
| ``public const string BrakeStarted``  | Authored brake started used by ``EventIds``. Initial value: ``"brakes.started"``.    |
+---------------------------------------+--------------------------------------------------------------------------------------+

.. _evs-api-events--events:

Events
------

**Runtime/Effects/Feedback/Events.cs**

Provides vehicle feedback events for effect integrations.

**Inherits / implements:** :ref:`EffectsModule <evs-api-presentation--effectsmodule>`.

.. _evs-api-events--methods-1:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                  | Role and behavior                                                                                                                      | Arguments and result                                                                                                                                                                                                               |
+============================================================================================+========================================================================================================================================+====================================================================================================================================================================================================================================+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Derives vehicle feedback transitions from current resolved mechanics/contact state and publishes corresponding ``EffectEvent`` values. | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop.           |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ResetState()``                                                       | Clears the declaring mechanic's retained simulation history at an explicit reset boundary.                                             | No arguments; no returned value.                                                                                                                                                                                                   |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Publish(string id, float intensity, Vector3 position)``              | Publishes a vehicle feedback event through the Events component.                                                                       | ``id`` — Case-sensitive authored body-part identifier. ``intensity`` — Intensity, interpreted by this operation in the declared type. ``position`` — Requested point or switch detent; see its declared type and owning operation. |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-events--events-and-inspector-callbacks:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------+-----------------------------------------------------------+
| Declaration                                 | Trigger, payload and meaning                              |
+=============================================+===========================================================+
| ``public event Action<EffectEvent> Raised`` | When Events publishes feedback. Payload: ``EffectEvent``. |
+---------------------------------------------+-----------------------------------------------------------+

.. _evs-api-events--state-and-configuration-2:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| Member                                                       | Meaning                                                                                    |
+==============================================================+============================================================================================+
| ``public bool detectOverturn``                               | Authored detect overturn used by Events. Initial value: ``true``.                          |
+--------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| ``public float overturnAngle``                               | Authored overturn angle used by Events. Initial value: ``70``.                             |
+--------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| ``public float recoveryAngle``                               | Authored recovery angle used by Events. Initial value: ``40``.                             |
+--------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| ``public float overturnDelay``                               | Time continuously tilted before reporting overturn, in seconds.                            |
+--------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| ``public virtual bool IsOverturned { get; protected set; }`` | Current is overturned predicate; read it instead of maintaining a second application flag. |
+--------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }``            | Cross-category execution barrier used by the module pipeline.                              |
+--------------------------------------------------------------+--------------------------------------------------------------------------------------------+

.. _evs-api-events--feedback:

Feedback
--------

**Runtime/Effects/Feedback/Feedback.cs**

Builds per-wheel presentation state after mechanics.

**Inherits / implements:** :ref:`EffectsModule <evs-api-presentation--effectsmodule>`.

.. _evs-api-events--methods-2:

Methods
~~~~~~~

+-------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                               | Role and behavior                                                                                      | Arguments and result                                                                                                                                            |
+=========================================================================+========================================================================================================+=================================================================================================================================================================+
| ``public override void Configure(VehicleController v)``                 | Resizes contact storage and clears surface caches for the configured wheel set.                        | ``v`` — V, interpreted by this operation in the declared type.                                                                                                  |
+-------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController v, Command c, float dt)`` | Samples wheel contact/activity and resolves presentation surfaces, then publishes changes and Sampled. | ``v`` — V, interpreted by this operation in the declared type. ``c`` — C, interpreted by this operation in the declared type. ``dt`` — Elapsed time in seconds. |
+-------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ClearSurfaceCache()``                             | Invalidates cached collider-to-effect-surface resolutions so later feedback can resolve again.         | No arguments; no returned value.                                                                                                                                |
+-------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-events--events-and-inspector-callbacks-1:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Declaration                                                          | Trigger, payload and meaning                                                                                              |
+======================================================================+===========================================================================================================================+
| ``public event Action Sampled``                                      | After Feedback updates its wheel/contact classification. No payload; read the component's current cached feedback.        |
+----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<int, bool> WheelGroundedChanged``              | When a wheel's feedback grounded state changes. Payload: wheel index and grounded bool.                                   |
+----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<int, TireSurfaceProfile> WheelSurfaceChanged`` | When a wheel's selected presentation surface changes. Payload: wheel index and ``TireSurfaceProfile``, possibly ``null``. |
+----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<bool> SkiddingChanged``                        | When aggregate feedback skid state changes. Payload: bool.                                                                |
+----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<bool> BrakingChanged``                         | When aggregate feedback braking state changes. Payload: bool.                                                             |
+----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-events--state-and-configuration-3:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| Member                                                             | Meaning                                                                                                    |
+====================================================================+============================================================================================================+
| ``public override int ExecutionOrder { get; }``                    | Default local priority within phase/category.                                                              |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }``                  | Cross-category execution barrier used by the module pipeline.                                              |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public VehicleController vehicle``                               | Authored vehicle used by Feedback.                                                                         |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public Engine engine``                                           | Authored engine used by Feedback.                                                                          |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public TireSurfaceProfile defaultSurface``                       | Fallback for unmarked colliders. Null preserves legacy asphalt effects.                                    |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public Events events``                                           | Authored events used by Feedback.                                                                          |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public float skidStartSlip``                                     | Authored skid start slip used by Feedback. Initial value: ``0.22f``.                                       |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public float fullSkidSlip``                                      | Authored full skid slip used by Feedback. Initial value: ``0.9f``.                                         |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public float minimumSkidSpeed``                                  | Authored minimum skid speed used by Feedback. Initial value: ``1``.                                        |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public float minimumCollisionSpeed``                             | Authored minimum collision speed used by Feedback. Initial value: ``1.5f``.                                |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public float skidSpeedRange``                                    | Speed span in m/s over which skid intensity reaches its full value above Minimum Skid Speed.               |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public float skidEventStartIntensity``                           | Authored skid event start intensity used by Feedback. Initial value: ``.15f``.                             |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public float skidEventStopIntensity``                            | Authored skid event stop intensity used by Feedback. Initial value: ``.05f``.                              |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public float brakeEventThreshold``                               | Authored brake event threshold used by Feedback. Initial value: ``.1f``.                                   |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public float brakeEventMinimumSpeedKph``                         | Authored brake event minimum speed kph used by Feedback. Initial value: ``3``.                             |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public float fullCollisionSpeed``                                | Normal collision speed in m/s that produces full event intensity.                                          |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public virtual WheelContact[] Contacts { get; protected set; }`` | Read-only/resolved contacts for Feedback.                                                                  |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public virtual float SkidIntensity { get; protected set; }``     | Read-only/resolved skid intensity for Feedback.                                                            |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public float touchdownSlipSeconds``                              | Decay time for physical tire spin-up slip after first surface contact. Shared by smoke, decals and squeal. |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+

.. _evs-api-events--impact:

Impact
------

**Runtime/Core/Impact.cs**

Stores copied collision information for deferred consumers.

.. _evs-api-events--methods-3:

Methods
~~~~~~~

+---------------------------------------------------------------+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                     | Role and behavior                                  | Arguments and result                                                                                                                                                                                                                      |
+===============================================================+====================================================+===========================================================================================================================================================================================================================================+
| ``public Impact(Collision collision, Vector3 fallbackPoint)`` | Constructs Impact with the supplied initial state. | ``collision`` — Collision, interpreted by this operation in the declared type. ``fallbackPoint`` — Fallback point, interpreted by this operation in the declared type. **Returns:** New instance initialized from the supplied arguments. |
+---------------------------------------------------------------+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-events--state-and-configuration-4:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------+-------------------------------------------------------------------------------------------+
| Member                                       | Meaning                                                                                   |
+==============================================+===========================================================================================+
| ``public readonly Vector3 Point``            | Copied world contact point/normal, relative velocity in m/s and collision impulse in N·s. |
+----------------------------------------------+-------------------------------------------------------------------------------------------+
| ``public readonly Vector3 Normal``           | Copied world contact point/normal, relative velocity in m/s and collision impulse in N·s. |
+----------------------------------------------+-------------------------------------------------------------------------------------------+
| ``public readonly Vector3 RelativeVelocity`` | Copied world contact point/normal, relative velocity in m/s and collision impulse in N·s. |
+----------------------------------------------+-------------------------------------------------------------------------------------------+
| ``public readonly Vector3 Impulse``          | Copied world contact point/normal, relative velocity in m/s and collision impulse in N·s. |
+----------------------------------------------+-------------------------------------------------------------------------------------------+
| ``public readonly Collider OtherCollider``   | External collider that produced the copied impact.                                        |
+----------------------------------------------+-------------------------------------------------------------------------------------------+
| ``public readonly Collider SelfCollider``    | Owned collider that received the copied impact.                                           |
+----------------------------------------------+-------------------------------------------------------------------------------------------+
| ``public readonly bool HasContact``          | Read-only has contact stored by this snapshot/data object.                                |
+----------------------------------------------+-------------------------------------------------------------------------------------------+

.. _evs-api-events--telemetry:

Telemetry
---------

**Runtime/Core/Telemetry.cs**

Carries the cached vehicle readings used by displays and observers.

.. _evs-api-events--methods-4:

Methods
~~~~~~~

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                                                                                                                                                                                                                                                                                | Role and behavior                                     | Arguments and result                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
+==========================================================================================================================================================================================================================================================================================================================================================+=======================================================+=========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| ``public Telemetry(float speed, float forward, float rpm, float throttle, float brake, float steer, int gear, string label, int grounded, int count, bool handbrake, Quaternion rotation, Vector3 position, Vector3 velocity, Vector3 acceleration, Vector3 gravity, float heightAboveGround, bool hasGroundBelow, string transmissionMode = "Direct")`` | Constructs Telemetry with the supplied initial state. | ``speed`` — Speed, interpreted by this operation in the declared type. ``forward`` — Forward, interpreted by this operation in the declared type. ``rpm`` — Rpm, interpreted by this operation in the declared type. ``throttle`` — Normalized propulsion/throttle request. ``brake`` — Normalized brake request. ``steer`` — Steer, interpreted by this operation in the declared type. ``gear`` — Signed gear index: -1 reverse, 0 neutral, positive forward. ``label`` — Label, interpreted by this operation in the declared type. ``grounded`` — Grounded, interpreted by this operation in the declared type. ``count`` — Count, interpreted by this operation in the declared type. ``handbrake`` — Handbrake request. ``rotation`` — Requested/output orientation in the declared frame. ``position`` — Requested point or switch detent; see its declared type and owning operation. ``velocity`` — World velocity in m/s. ``acceleration`` — Acceleration, interpreted by this operation in the declared type. ``gravity`` — Gravity, interpreted by this operation in the declared type. ``heightAboveGround`` — Height above ground, interpreted by this operation in the declared type. ``hasGroundBelow`` — Has ground below, interpreted by this operation in the declared type. ``transmissionMode`` — Transmission mode, interpreted by this operation in the declared type. Default: ``"Direct"``. **Returns:** New instance initialized from the supplied arguments. |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-events--state-and-configuration-5:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                      | Meaning                                                                                                                                                                                                                    |
+=============================================+============================================================================================================================================================================================================================+
| ``public readonly float SpeedKph``          | Read-only speed kph stored by this snapshot/data object.                                                                                                                                                                   |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public readonly float ForwardSpeed``      | Read-only forward speed stored by this snapshot/data object.                                                                                                                                                               |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public readonly float Rpm``               | Read-only rpm stored by this snapshot/data object.                                                                                                                                                                         |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public readonly float Throttle``          | Read-only throttle stored by this snapshot/data object.                                                                                                                                                                    |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public readonly float Brake``             | Read-only brake stored by this snapshot/data object.                                                                                                                                                                       |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public readonly float SteeringAngle``     | Read-only steering angle stored by this snapshot/data object.                                                                                                                                                              |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public readonly int Gear``                | Read-only gear stored by this snapshot/data object.                                                                                                                                                                        |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public readonly int GroundedWheels``      | Read-only grounded wheels stored by this snapshot/data object.                                                                                                                                                             |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public readonly int WheelCount``          | Read-only wheel count stored by this snapshot/data object.                                                                                                                                                                 |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public readonly string GearLabel``        | Read-only gear label stored by this snapshot/data object.                                                                                                                                                                  |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public readonly string TransmissionMode`` | Read-only transmission mode stored by this snapshot/data object.                                                                                                                                                           |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public readonly bool Handbrake``          | Read-only handbrake stored by this snapshot/data object.                                                                                                                                                                   |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public readonly bool HasGroundBelow``     | Read-only has ground below stored by this snapshot/data object.                                                                                                                                                            |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public readonly float HeightAboveGround`` | Read-only height above ground stored by this snapshot/data object.                                                                                                                                                         |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public readonly Quaternion Rotation``     | World pose/velocity plus attitude relative to gravity. Pitch is nose-up positive; roll is right-bank positive; heading is clockwise from world +Z. World-space chassis orientation captured after the simulation pipeline. |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public readonly Vector3 Velocity``        | World-space linear velocity captured in the snapshot, in m/s.                                                                                                                                                              |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public readonly Vector3 SpecificForce``   | Accelerometer reading, excluding gravity: rest is 1 G, free fall is 0 G.                                                                                                                                                   |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public readonly float GForce``            | Read-only gforce stored by this snapshot/data object.                                                                                                                                                                      |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public readonly float NormalG``           | Read-only normal g stored by this snapshot/data object.                                                                                                                                                                    |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public readonly float PitchDegrees``      | Read-only pitch degrees stored by this snapshot/data object.                                                                                                                                                               |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public readonly float RollDegrees``       | Read-only roll degrees stored by this snapshot/data object.                                                                                                                                                                |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public readonly float HeadingDegrees``    | Read-only heading degrees stored by this snapshot/data object.                                                                                                                                                             |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public readonly float AltitudeMetres``    | Read-only altitude metres stored by this snapshot/data object.                                                                                                                                                             |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public readonly float VerticalSpeed``     | Read-only vertical speed stored by this snapshot/data object.                                                                                                                                                              |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public readonly float Airspeed``          | Read-only airspeed stored by this snapshot/data object.                                                                                                                                                                    |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+-------------------------------------------+----------------------------------------------------------------------------------------+
| Member                                    | Meaning                                                                                |
+===========================================+========================================================================================+
| ``public float SpeedMph { get; }``        | Unsigned speed of this captured snapshot in mph.                                       |
+-------------------------------------------+----------------------------------------------------------------------------------------+
| ``public float GetSpeed(SpeedUnit unit)`` | Returns the speed of this snapshot in the requested unit; does not read the live body. |
+-------------------------------------------+----------------------------------------------------------------------------------------+

.. _evs-api-events--wheelcontact:

WheelContact
------------

**Runtime/Effects/Feedback/WheelContact.cs**

Carries cached contact/activity and selected effect-surface data.

.. _evs-api-events--state-and-configuration-6:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------+---------------------------------------------------+
| Member                                | Meaning                                           |
+=======================================+===================================================+
| ``public bool Grounded``              | Authored grounded used by ``WheelContact``.       |
+---------------------------------------+---------------------------------------------------+
| ``public WheelHit Hit``               | Authored hit used by ``WheelContact``.            |
+---------------------------------------+---------------------------------------------------+
| ``public TireSurfaceProfile Surface`` | Authored surface used by ``WheelContact``.        |
+---------------------------------------+---------------------------------------------------+
| ``public float SurfaceSpeed``         | Authored surface speed used by ``WheelContact``.  |
+---------------------------------------+---------------------------------------------------+
| ``public float Slip``                 | Authored slip used by ``WheelContact``.           |
+---------------------------------------+---------------------------------------------------+
| ``public float SkidIntensity``        | Authored skid intensity used by ``WheelContact``. |
+---------------------------------------+---------------------------------------------------+
