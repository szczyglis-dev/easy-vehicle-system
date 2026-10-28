.. _evs-api-tracks--tracked-movement-api:

Tracked movement API
====================

Read :doc:`the system explanation </Scripting/Tracks>` for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from ``MonoBehaviour``, ``Object`` or ``ScriptableObject`` are documented by Unity.

.. _evs-api-tracks--types:

Types
-----

-  :ref:`TrackPathBuilder <evs-api-tracks--trackpathbuilder>`
-  :ref:`TrackPathBuilder.LinkOrder <evs-api-tracks--trackpathbuilderlinkorder>`
-  :ref:`TrackPathBuilder.LinkPosition <evs-api-tracks--trackpathbuilderlinkposition>`
-  :ref:`TrackVisuals <evs-api-tracks--trackvisuals>`
-  :ref:`TrackVisuals.Belt <evs-api-tracks--trackvisualsbelt>`
-  :ref:`TrackVisuals.Roller <evs-api-tracks--trackvisualsroller>`
-  :ref:`TrackedProfile <evs-api-tracks--trackedprofile>`
-  :ref:`Tracks <evs-api-tracks--tracks>`

.. _evs-api-tracks--trackpathbuilder:

TrackPathBuilder
----------------

**Runtime/Exterior/TrackPathBuilder.cs**

Prepares reusable closed paths during authoring.

**Inherits / implements:** ``MonoBehaviour``.

.. _evs-api-tracks--state-and-configuration:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| Member                                                      | Meaning                                                                                            |
+=============================================================+====================================================================================================+
| ``public TrackVisuals visuals``                             | Assign the vehicle's ``TrackVisuals``. Automatically found in parents when available.              |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| ``public bool leftBelt``                                    | Authored left belt used by ``TrackPathBuilder``. Initial value: ``true``.                          |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| ``public Transform linksParent``                            | Collect mesh objects recursively from this parent. Leave empty to use only Explicit Links.         |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| ``public Transform[] explicitLinks``                        | Additional links, or the complete list when Links Parent is empty. Duplicates are removed.         |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| ``public Transform pathParent``                             | Optional destination. If empty, a dedicated Path object is created beside this builder.            |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| ``public LinkOrder order``                                  | Authored order used by ``TrackPathBuilder``. Initial value: ``LinkOrder.AroundBelt``.              |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| ``public LinkPosition position``                            | Authored position used by ``TrackPathBuilder``. Initial value: ``LinkPosition.MeshBoundsCenter``.  |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| ``public bool reverseOrder``                                | Reverse the node order and matching links together.                                                |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| ``public float travelDirection``                            | Direction relative to positive wheel rim speed; default matches clockwise ordering in vehicle Y/Z. |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
| ``public virtual Transform[] GeneratedNodes { get; set; }`` | Read-only/resolved generated nodes for ``TrackPathBuilder``.                                       |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------+

.. _evs-api-tracks--trackpathbuilderlinkorder:

TrackPathBuilder.LinkOrder
--------------------------

**Runtime/Exterior/TrackPathBuilder.cs**

Defines the allowed link order choices used by this topic.

.. _evs-api-tracks--values:

Values
~~~~~~

-  ``AroundBelt``
-  ``InputOrder``

.. _evs-api-tracks--trackpathbuilderlinkposition:

TrackPathBuilder.LinkPosition
-----------------------------

**Runtime/Exterior/TrackPathBuilder.cs**

Defines the allowed link position choices used by this topic.

.. _evs-api-tracks--values-1:

Values
~~~~~~

-  ``MeshBoundsCenter``
-  ``TransformPivot``

.. _evs-api-tracks--trackvisuals:

TrackVisuals
------------

**Runtime/Exterior/TrackVisuals.cs**

Moves visible links and rollers from wheel motion.

**Inherits / implements:** :ref:`ExteriorModule <evs-api-modules--exteriormodule>`.

.. _evs-api-tracks--methods:

Methods
~~~~~~~

+-------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                           | Role and behavior                                                                              | Arguments and result                                                                                                                                                                                                                                                                                                             |
+=====================================================================================+================================================================================================+==================================================================================================================================================================================================================================================================================================================================+
| ``public override void Configure(VehicleController owner)``                         | Caches vehicle/Tracks and prepares left/right belt paths and retained link poses.              | ``owner`` — Unity/application owner whose identity controls this relationship or resource.                                                                                                                                                                                                                                       |
+-------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool SupportsProfile(DriveProfile profile)``                      | Checks movement-family compatibility; this is independent of the Unity enabled flag.           | ``profile`` — Movement/surface configuration, according to its declared type. **Returns:** ``true`` when the described condition holds; ``false`` otherwise.                                                                                                                                                                     |
+-------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryGetPathPoint(Belt belt, int index, out Vector3 position)`` | Reads an interpolated point/orientation on a prepared belt path without advancing belt travel. | ``belt`` — Track side/path to query. ``index`` — Zero-based configured-entry index; use the owner's current list ordering. ``position`` — Requested point or switch detent; see its declared type and owning operation. **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values. |
+-------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void AdvanceVisuals(float deltaTime)``                             | Advances belt-link and roller presentation from the configured wheel motion.                   | ``deltaTime`` — Elapsed time in seconds supplied by the owning loop.                                                                                                                                                                                                                                                             |
+-------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-tracks--state-and-configuration-1:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------+--------------------------------------------------------------------------------------+
| Member                                                      | Meaning                                                                              |
+=============================================================+======================================================================================+
| ``public Belt leftBelt``                                    | Authored left belt used by ``TrackVisuals``. Initial value: ``new Belt()``.          |
+-------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public Belt rightBelt``                                   | Authored right belt used by ``TrackVisuals``. Initial value: ``new Belt()``.         |
+-------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public Roller[] rollers``                                 | Authored rollers used by ``TrackVisuals``. Initial value: ``Array.Empty<Roller>()``. |
+-------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public virtual float LeftSpeed { get; protected set; }``  | Read-only/resolved left speed for ``TrackVisuals``.                                  |
+-------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public virtual float RightSpeed { get; protected set; }`` | Read-only/resolved right speed for ``TrackVisuals``.                                 |
+-------------------------------------------------------------+--------------------------------------------------------------------------------------+

.. _evs-api-tracks--trackvisualsbelt:

TrackVisuals.Belt
-----------------

**Runtime/Exterior/TrackVisuals.cs**

Configuration/implementation type for belt within tracked movement.

.. _evs-api-tracks--state-and-configuration-2:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------+---------------------------------------------------------------------------+
| Member                           | Meaning                                                                   |
+==================================+===========================================================================+
| ``public Transform[] path``      | Authored path used by Belt. Initial value: ``Array.Empty<Transform>()``.  |
+----------------------------------+---------------------------------------------------------------------------+
| ``public Transform[] links``     | Authored links used by Belt. Initial value: ``Array.Empty<Transform>()``. |
+----------------------------------+---------------------------------------------------------------------------+
| ``public float travelDirection`` | Path travel direction relative to positive wheel rim speed.               |
+----------------------------------+---------------------------------------------------------------------------+
| ``public float Travel { get; }`` | Read-only/resolved travel for Belt.                                       |
+----------------------------------+---------------------------------------------------------------------------+

.. _evs-api-tracks--trackvisualsroller:

TrackVisuals.Roller
-------------------

**Runtime/Exterior/TrackVisuals.cs**

Configuration/implementation type for roller within tracked movement.

.. _evs-api-tracks--state-and-configuration-3:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------+-----------------------------------------------------------------------------------+
| Member                         | Meaning                                                                           |
+================================+===================================================================================+
| ``public Transform transform`` | Authored transform used by Roller.                                                |
+--------------------------------+-----------------------------------------------------------------------------------+
| ``public bool left``           | Uses the left belt speed rather than the right when rotating this visible roller. |
+--------------------------------+-----------------------------------------------------------------------------------+
| ``public float radius``        | Authored radius used by Roller. Initial value: ``.5f``.                           |
+--------------------------------+-----------------------------------------------------------------------------------+
| ``public Vector3 localAxis``   | Authored local axis used by Roller. Initial value: ``Vector3.right``.             |
+--------------------------------+-----------------------------------------------------------------------------------+

.. _evs-api-tracks--trackedprofile:

TrackedProfile
--------------

**Runtime/Drive/Profiles/TrackedProfile.cs**

Maps tracked propulsion/turning intent into movement behavior.

**Inherits / implements:** :ref:`DriveProfile <evs-api-driveprofiles--driveprofile>`.

.. _evs-api-tracks--methods-1:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                  | Role and behavior                                                                                              | Arguments and result                                                                                                                                                                                                       |
+============================================================================================+================================================================================================================+============================================================================================================================================================================================================================+
| ``public TrackedProfile()``                                                                | Constructs ``TrackedProfile`` with the supplied initial state.                                                 | **Returns:** New instance initialized from the supplied arguments.                                                                                                                                                         |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Configure(VehicleController vehicle)``                              | Ensures a Tracks component exists; explicit side membership remains vehicle-owned configuration.               | ``vehicle`` — Vehicle context/owner receiving the operation.                                                                                                                                                               |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Resolves engine output and side/pivot demand, then applies bounded tracked propulsion to the configured sides. | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop.   |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override float ResolveDriveDemand(VehicleController vehicle, Command command)``   | Maps the command and strategy state to propulsion demand for surrounding mechanics.                            | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. **Returns:** Computed float in the operation's documented unit/domain. |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-tracks--state-and-configuration-4:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                               | Meaning                                                                                                                                            |
+======================================================+====================================================================================================================================================+
| ``public float steeringMix``                         | Steering strength applied to the configured inside-track speed reduction.                                                                          |
+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float steeringBrakeTorque``                 | Maximum per-wheel braking for inside belt speed regulation; shared service/parking brakes take priority.                                           |
+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float insideTrackSpeedRatio``               | Inside belt target speed relative to the outside belt during a moving turn.                                                                        |
+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float pivotTrackSpeed``                     | Equal and opposite belt speed during a stationary turn, in m/s at full steering.                                                                   |
+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float pivotTransitionTime``                 | Authored pivot transition time used by ``TrackedProfile``. Initial value: ``0.3f``.                                                                |
+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float trackSpeedResponse``                  | Authored track speed response used by ``TrackedProfile``. Initial value: ``2f``.                                                                   |
+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float turnSpeedCompensation``               | Speed compensation during moving turns: accelerates the outside belt to preserve the mean belt-speed target. Zero uses brake-steer speed loss.     |
+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool redistributeSteeringTorque``           | Route unused inside-track drive torque to the outside track within the existing engine torque and power limits.                                    |
+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float lateralGrip``                         | Lateral tire grip relative to ordinary tires, allowing the road wheels to skid sideways during turns.                                              |
+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float lowSpeedTurnGrip``                    | Lateral grip during a powered brake-steer launch. Blends to Lateral Grip between 1 and 4 m/s; use the same value to disable the release.           |
+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float lateralStability``                    | Grounded chassis lateral-velocity damping per second. Keeps the hull following its heading while road wheels scrub during turns. Zero disables it. |
+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumLateralStabilityAcceleration`` | Maximum lateral stability acceleration in m/s², additionally limited by tire contact load and surface grip.                                        |
+------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-tracks--tracks:

Tracks
------

**Runtime/Drive/Grounded/Tracks.cs**

Owns explicit side membership and tracked support policy.

**Inherits / implements:** :ref:`DriveModule <evs-api-driveprofiles--drivemodule>`.

.. _evs-api-tracks--methods-2:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                  | Role and behavior                                                                              | Arguments and result                                                                                                                                                                                                     |
+============================================================================================+================================================================================================+==========================================================================================================================================================================================================================+
| ``public override void Configure(VehicleController vehicle)``                              | Clears retained pivot state/blend before tracked movement resumes.                             | ``vehicle`` — Vehicle context/owner receiving the operation.                                                                                                                                                             |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Applies supported load/grip-limited lateral/pivot stabilization for an active tracked profile. | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool SupportsProfile(DriveProfile profile)``                             | Checks movement-family compatibility; this is independent of the Unity enabled flag.           | ``profile`` — Movement/surface configuration, according to its declared type. **Returns:** ``true`` when the described condition holds; ``false`` otherwise.                                                             |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual int SideOf(WheelCollider wheel)``                                         | Resolves a native wheel's left/right tracked-side membership.                                  | ``wheel`` — Native wheel or wheel adapter being configured/queried. **Returns:** Computed int in the operation's documented unit/domain.                                                                                 |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-tracks--state-and-configuration-5:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------+----------------------------------------------------------------------------------------+
| Member                                                      | Meaning                                                                                |
+=============================================================+========================================================================================+
| ``public WheelCollider[] leftWheels``                       | Authored left wheels used by Tracks. Initial value: ``Array.Empty<WheelCollider>()``.  |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------+
| ``public WheelCollider[] rightWheels``                      | Authored right wheels used by Tracks. Initial value: ``Array.Empty<WheelCollider>()``. |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------+
| ``public virtual float PivotBlend { get; protected set; }`` | Read-only/resolved pivot blend for Tracks.                                             |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------+
