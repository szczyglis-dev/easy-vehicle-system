.. _evs-api-suspension--suspension-and-linkage-api:

Suspension and linkage API
==========================

Read :doc:`the system explanation </Scripting/Suspension>` for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from ``MonoBehaviour``, ``Object`` or ``ScriptableObject`` are documented by Unity.

.. _evs-api-suspension--types:

Types
-----

-  :ref:`AntiRoll <evs-api-suspension--antiroll>`
-  :ref:`AntiRoll.Axle <evs-api-suspension--antirollaxle>`
-  :ref:`ControlArm <evs-api-suspension--controlarm>`
-  :ref:`HalfShaft <evs-api-suspension--halfshaft>`
-  :ref:`ShockAbsorber <evs-api-suspension--shockabsorber>`
-  :ref:`SteeringTieRod <evs-api-suspension--steeringtierod>`
-  :ref:`Suspension <evs-api-suspension--suspension>`
-  :ref:`SuspensionAxle <evs-api-suspension--suspensionaxle>`
-  :ref:`SuspensionHub <evs-api-suspension--suspensionhub>`
-  :ref:`SuspensionRotationAxes <evs-api-suspension--suspensionrotationaxes>`
-  :ref:`SuspensionRotationLimits <evs-api-suspension--suspensionrotationlimits>`

.. _evs-api-suspension--antiroll:

AntiRoll
--------

**Runtime/Drive/Suspension/AntiRoll.cs**

Adds cross-wheel roll support for the configured wheel relationships.

**Inherits / implements:** :ref:`DriveModule <evs-api-driveprofiles--drivemodule>`.

.. _evs-api-suspension--methods:

Methods
~~~~~~~

+-------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                               | Role and behavior                                                                            | Arguments and result                                                                                                                                            |
+=========================================================================+==============================================================================================+=================================================================================================================================================================+
| ``public override void Step(VehicleController v, Command c, float dt)`` | Transfers bounded anti-roll load between eligible supported wheels in configured axle pairs. | ``v`` — V, interpreted by this operation in the declared type. ``c`` — C, interpreted by this operation in the declared type. ``dt`` — Elapsed time in seconds. |
+-------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool SupportsProfile(DriveProfile profile)``          | Checks movement-family compatibility; this is independent of the Unity enabled flag.         | ``profile`` — Movement/surface configuration, according to its declared type. **Returns:** ``true`` when the described condition holds; ``false`` otherwise.    |
+-------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-suspension--state-and-configuration:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------+-------------------------------------------------------------------+
| Member                                            | Meaning                                                           |
+===================================================+===================================================================+
| ``public override int ExecutionOrder { get; }``   | Default local priority within phase/category.                     |
+---------------------------------------------------+-------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }`` | Cross-category execution barrier used by the module pipeline.     |
+---------------------------------------------------+-------------------------------------------------------------------+
| ``public Axle[] axles``                           | Authored axles used by ``AntiRoll``.                              |
+---------------------------------------------------+-------------------------------------------------------------------+
| ``public float stiffness``                        | Authored stiffness used by ``AntiRoll``. Initial value: ``4500``. |
+---------------------------------------------------+-------------------------------------------------------------------+

.. _evs-api-suspension--antirollaxle:

AntiRoll.Axle
-------------

**Runtime/Drive/Suspension/AntiRoll.cs**

Value data for axle; its fields are listed below.

.. _evs-api-suspension--state-and-configuration-1:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

====================== ============================
Member                 Meaning
====================== ============================
``public Wheel left``  Authored left used by Axle.
``public Wheel right`` Authored right used by Axle.
====================== ============================

.. _evs-api-suspension--controlarm:

ControlArm
----------

**Runtime/Drive/Suspension/ControlArm.cs**

Resolves a visual control arm against its authored geometry.

**Inherits / implements:** ``MonoBehaviour``.

.. _evs-api-suspension--methods-1:

Methods
~~~~~~~

+-------------------------------------------------------+-----------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                             | Role and behavior                                                                       | Arguments and result                                                                                                                                                           |
+=======================================================+=========================================================================================+================================================================================================================================================================================+
| ``public virtual Vector3 ResolveHub(Vector3 sample)`` | Resolves the hub position from this control arm's authored geometry.                    | ``sample`` — Output water sample; read it only when sampling returns ``true``. **Returns:** Returned Vector3; ownership remains as specified by the creating/lookup operation. |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void UpdatePose()``                  | Recomputes this visual linkage's pose from its authored geometry and current endpoints. | No arguments; no returned value.                                                                                                                                               |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-suspension--state-and-configuration-2:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| Member                                                        | Meaning                                                                                                             |
+===============================================================+=====================================================================================================================+
| ``public Transform pivot``                                    | Authored pivot used by ``ControlArm``.                                                                              |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public Transform innerFrontAnchor``                         | Authored inner front anchor used by ``ControlArm``.                                                                 |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public Transform innerRearAnchor``                          | Authored inner rear anchor used by ``ControlArm``.                                                                  |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public Transform outerJoint``                               | Authored outer joint used by ``ControlArm``.                                                                        |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public Transform hub``                                      | Authored hub used by ``ControlArm``.                                                                                |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public Transform shockAnchor``                              | Authored shock anchor used by ``ControlArm``.                                                                       |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public Transform frontLeg``                                 | Authored front leg used by ``ControlArm``.                                                                          |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public Transform rearLeg``                                  | Authored rear leg used by ``ControlArm``.                                                                           |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public Transform upright``                                  | Authored upright used by ``ControlArm``.                                                                            |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public WheelCollider wheel``                                | Authored wheel used by ``ControlArm``.                                                                              |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public Wheel wheelAdapter``                                 | Authored wheel adapter used by ``ControlArm``.                                                                      |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public SteeringTieRod steeringLinkage``                     | Authored steering linkage used by ``ControlArm``.                                                                   |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public float armLength``                                    | Distance from hinge centre to outer ball joint, in metres. Pivot local X points outward; local Z is the hinge axis. |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public SuspensionRotationLimits rotationLimits``            | Authored rotation limits used by ``ControlArm``. Initial value: ``new SuspensionRotationLimits()``.                 |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public Vector3 hubOffset``                                  | Authored hub offset used by ``ControlArm``. Initial value: ``new Vector3(0, .25f, 0)``.                             |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public float shockMountFraction``                           | Authored shock mount fraction used by ``ControlArm``. Initial value: ``.7f``.                                       |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public float minimumAngle``                                 | Authored minimum angle used by ``ControlArm``. Initial value: ``-30``.                                              |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public float maximumAngle``                                 | Authored maximum angle used by ``ControlArm``. Initial value: ``30``.                                               |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public Vector3 localLengthAxis``                            | Authored local length axis used by ``ControlArm``. Initial value: ``Vector3.up``.                                   |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public float meshLength``                                   | Authored mesh length used by ``ControlArm``. Initial value: ``2``.                                                  |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public bool constrainNativeWheel``                          | Authored constrain native wheel used by ``ControlArm``. Initial value: ``true``.                                    |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public bool showGizmos``                                    | Authored show gizmos used by ``ControlArm``. Initial value: ``true``.                                               |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public virtual float CurrentAngle { get; protected set; }`` | Read-only/resolved current angle for ``ControlArm``.                                                                |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool OutsideTravel { get; }``                | Read-only/resolved outside travel for ``ControlArm``.                                                               |
+---------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+

.. _evs-api-suspension--halfshaft:

HalfShaft
---------

**Runtime/Drive/Suspension/HalfShaft.cs**

Presents axle articulation and shaft rotation.

**Inherits / implements:** ``MonoBehaviour``.

.. _evs-api-suspension--methods-2:

Methods
~~~~~~~

+--------------------------------------+-----------------------------------------------------------------------------------------+----------------------------------+
| Signature                            | Role and behavior                                                                       | Arguments and result             |
+======================================+=========================================================================================+==================================+
| ``public virtual void UpdatePose()`` | Recomputes this visual linkage's pose from its authored geometry and current endpoints. | No arguments; no returned value. |
+--------------------------------------+-----------------------------------------------------------------------------------------+----------------------------------+

.. _evs-api-suspension--state-and-configuration-3:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| Member                                                     | Meaning                                                                                                         |
+============================================================+=================================================================================================================+
| ``public Transform innerAnchor``                           | Authored inner anchor used by ``HalfShaft``.                                                                    |
+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public Transform outerAnchor``                           | Authored outer anchor used by ``HalfShaft``.                                                                    |
+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public WheelCollider wheel``                             | Authored wheel used by ``HalfShaft``.                                                                           |
+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public Transform shaft``                                 | Authored shaft used by ``HalfShaft``.                                                                           |
+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public Vector3 localRotationAxis``                       | Cardinal mesh axis used for both length and rotation (Unity cylinder: Y).                                       |
+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public Vector3 rotationOffset``                          | Authored rotation offset used by ``HalfShaft``.                                                                 |
+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public float meshLength``                                | Authored mesh length used by ``HalfShaft``. Initial value: ``2``.                                               |
+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public SuspensionRotationLimits articulation``           | Swing permissions in the neutral mesh frame. For a Y cylinder along chassis X, Z permits vertical articulation. |
+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public SuspensionRotationAxes spinAxes``                 | Permitted spin axes in mesh-local space. Enable the selected ``localRotationAxis`` to retain wheel spin.        |
+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public float spinMultiplier``                            | Authored spin multiplier used by ``HalfShaft``. Initial value: ``1``.                                           |
+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public float spinOffset``                                | Authored spin offset used by ``HalfShaft``.                                                                     |
+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public float maximumJointAngle``                         | Authored maximum joint angle used by ``HalfShaft``. Initial value: ``45``.                                      |
+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public bool showGizmos``                                 | Authored show gizmos used by ``HalfShaft``. Initial value: ``true``.                                            |
+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public virtual float SpinAngle { get; protected set; }`` | Read-only/resolved spin angle for ``HalfShaft``.                                                                |
+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public virtual float JointAngle { get; }``               | Read-only/resolved joint angle for ``HalfShaft``.                                                               |
+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+

.. _evs-api-suspension--shockabsorber:

ShockAbsorber
-------------

**Runtime/Drive/Suspension/ShockAbsorber.cs**

Animates a telescoping shock and optionally overrides one wheel's physics.

**Inherits / implements:** ``MonoBehaviour``.

.. _evs-api-suspension--methods-3:

Methods
~~~~~~~

+--------------------------------------+-----------------------------------------------------------------------------------------+----------------------------------+
| Signature                            | Role and behavior                                                                       | Arguments and result             |
+======================================+=========================================================================================+==================================+
| ``public virtual void UpdatePose()`` | Recomputes this visual linkage's pose from its authored geometry and current endpoints. | No arguments; no returned value. |
+--------------------------------------+-----------------------------------------------------------------------------------------+----------------------------------+

.. _evs-api-suspension--state-and-configuration-4:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| Member                                           | Meaning                                                                                                                       |
+==================================================+===============================================================================================================================+
| ``public Transform chassisAnchor``               | Authored chassis anchor used by ``ShockAbsorber``.                                                                            |
+--------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform wheelAnchor``                 | Authored wheel anchor used by ``ShockAbsorber``.                                                                              |
+--------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform casing``                      | Authored casing used by ``ShockAbsorber``.                                                                                    |
+--------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform piston``                      | Authored piston used by ``ShockAbsorber``.                                                                                    |
+--------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector3 localLengthAxis``               | Authored local length axis used by ``ShockAbsorber``. Initial value: ``Vector3.up``.                                          |
+--------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector3 rotationOffset``                | Authored rotation offset used by ``ShockAbsorber``.                                                                           |
+--------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| ``public SuspensionRotationLimits articulation`` | Authored articulation used by ``ShockAbsorber``. Initial value: ``new SuspensionRotationLimits()``.                           |
+--------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| ``public float meshLength``                      | Authored mesh length used by ``ShockAbsorber``. Initial value: ``2``.                                                         |
+--------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| ``public float casingLength``                    | Authored casing length used by ``ShockAbsorber``. Initial value: ``.65f``.                                                    |
+--------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| ``public float pistonLength``                    | Authored piston length used by ``ShockAbsorber``. Initial value: ``.65f``.                                                    |
+--------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| ``public float minimumLength``                   | Authored minimum length used by ``ShockAbsorber``. Initial value: ``.7f``.                                                    |
+--------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumLength``                   | Authored maximum length used by ``ShockAbsorber``. Initial value: ``1.25f``.                                                  |
+--------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| ``public WheelCollider wheel``                   | Authored wheel used by ``ShockAbsorber``.                                                                                     |
+--------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| ``public bool overrideWheelPhysics``             | Overrides this wheel's native spring, damper and travel through the EVS Suspension module. Use one active override per wheel. |
+--------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| ``public float spring``                          | Shock spring stiffness, N/m. Motion ratio converts this to wheel stiffness.                                                   |
+--------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| ``public float damper``                          | Shock damping coefficient, N s/m.                                                                                             |
+--------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| ``public float suspensionTravel``                | Authored suspension travel used by ``ShockAbsorber``. Initial value: ``.65f``.                                                |
+--------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| ``public float targetPosition``                  | Authored target position used by ``ShockAbsorber``. Initial value: ``.5f``.                                                   |
+--------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| ``public float motionRatio``                     | Shock travel / wheel travel. Wheel-equivalent spring and damping scale with this ratio squared.                               |
+--------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float WheelSpring { get; }``    | Read-only/resolved wheel spring for ``ShockAbsorber``.                                                                        |
+--------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float WheelDamper { get; }``    | Read-only/resolved wheel damper for ``ShockAbsorber``.                                                                        |
+--------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| ``public bool showGizmos``                       | Authored show gizmos used by ``ShockAbsorber``. Initial value: ``true``.                                                      |
+--------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float CurrentLength { get; }``  | Read-only/resolved current length for ``ShockAbsorber``.                                                                      |
+--------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float Compression { get; }``    | Resolved suspension compression of the configured wheel.                                                                      |
+--------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool OutsideTravel { get; }``   | Read-only/resolved outside travel for ``ShockAbsorber``.                                                                      |
+--------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-suspension--steeringtierod:

SteeringTieRod
--------------

**Runtime/Drive/Suspension/SteeringTieRod.cs**

``Tracks`` steering-link endpoints and geometry.

**Inherits / implements:** ``MonoBehaviour``.

.. _evs-api-suspension--methods-4:

Methods
~~~~~~~

+----------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| Signature                                                | Role and behavior                                                                       | Arguments and result                                                                                            |
+==========================================================+=========================================================================================+=================================================================================================================+
| ``public virtual void ApplyNativeSteering(float angle)`` | Applies resolved linkage steering placement to the native wheel configuration.          | ``angle`` — Angular coordinate in degrees for this geometry operation.                                          |
+----------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public virtual float ResolveSteering(float demand)``   | Resolves the linkage's steering geometry for the supplied wheel/angle state.            | ``demand`` — Normalized actuator demand. **Returns:** Computed float in the operation's documented unit/domain. |
+----------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public virtual void UpdatePose()``                     | Recomputes this visual linkage's pose from its authored geometry and current endpoints. | No arguments; no returned value.                                                                                |
+----------------------------------------------------------+-----------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+

.. _evs-api-suspension--state-and-configuration-5:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Member                                                            | Meaning                                                                                              |
+===================================================================+======================================================================================================+
| ``public WheelCollider wheel``                                    | Authored wheel used by ``SteeringTieRod``.                                                           |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public Transform knuckle``                                      | Authored knuckle used by ``SteeringTieRod``.                                                         |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public Transform steeringPivot``                                | Independent kingpin anchor on the suspension carrier. Keep it outside the steered knuckle hierarchy. |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public Vector3 wheelCenterOffset``                              | Neutral wheel centre relative to the steering pivot, in the native wheel frame (metres).             |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public Transform rackReference``                                | Authored rack reference used by ``SteeringTieRod``.                                                  |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public Transform rackEnd``                                      | Authored rack end used by ``SteeringTieRod``.                                                        |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public Transform steeringArmAnchor``                            | Authored steering arm anchor used by ``SteeringTieRod``.                                             |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public Transform rod``                                          | Authored rod used by ``SteeringTieRod``.                                                             |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public Transform steeringLever``                                | Authored steering lever used by ``SteeringTieRod``.                                                  |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public float rodLength``                                        | Authored rod length used by ``SteeringTieRod``. Initial value: ``1.2f``.                             |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public float maximumRackTravel``                                | Authored maximum rack travel used by ``SteeringTieRod``. Initial value: ``.25f``.                    |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public float maximumSteeringAngle``                             | Authored maximum steering angle used by ``SteeringTieRod``. Initial value: ``40``.                   |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public Vector3 rackLocalAxis``                                  | Authored rack local axis used by ``SteeringTieRod``. Initial value: ``Vector3.right``.               |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public SuspensionRotationLimits steeringRotation``              | Knuckle rotation permissions in the native wheel frame. Native steering uses local Y.                |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public SuspensionRotationLimits rodArticulation``               | Rod swivel permissions relative to the rack frame, with its mesh axis pointing across the chassis.   |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public Vector3 localLengthAxis``                                | Authored local length axis used by ``SteeringTieRod``. Initial value: ``Vector3.up``.                |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public float meshLength``                                       | Authored mesh length used by ``SteeringTieRod``. Initial value: ``2``.                               |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public float previewSteeringAngle``                             | Authored preview steering angle used by ``SteeringTieRod``.                                          |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public bool showGizmos``                                        | Authored show gizmos used by ``SteeringTieRod``. Initial value: ``true``.                            |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public virtual float RackDisplacement { get; protected set; }`` | Read-only/resolved rack displacement for ``SteeringTieRod``.                                         |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public virtual float CurrentAngle { get; protected set; }``     | Read-only/resolved current angle for ``SteeringTieRod``.                                             |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public virtual bool Reachable { get; protected set; }``         | Read-only/resolved reachable for ``SteeringTieRod``.                                                 |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public virtual Vector3 WorldSteeringOffset { get; }``           | Read-only/resolved world steering offset for ``SteeringTieRod``.                                     |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+

.. _evs-api-suspension--suspension:

Suspension
----------

**Runtime/Drive/Suspension/Suspension.cs**

Configures native wheel support and suspension-related response.

**Inherits / implements:** :ref:`DriveModule <evs-api-driveprofiles--drivemodule>`.

.. _evs-api-suspension--methods-5:

Methods
~~~~~~~

+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                               | Role and behavior                                                                                                            | Arguments and result                                                                                                                                            |
+=========================================================================+==============================================================================================================================+=================================================================================================================================================================+
| ``public override void Configure(VehicleController v)``                 | Builds owned shock-override mappings, clears travel history and applies configured native wheel spring/damper/travel policy. | ``v`` — V, interpreted by this operation in the declared type.                                                                                                  |
+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController v, Command c, float dt)`` | Updates per-wheel override settings, force-application placement and motion-dependent damping using envelope/native support. | ``v`` — V, interpreted by this operation in the declared type. ``c`` — C, interpreted by this operation in the declared type. ``dt`` — Elapsed time in seconds. |
+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool SupportsProfile(DriveProfile profile)``          | Checks movement-family compatibility; this is independent of the Unity enabled flag.                                         | ``profile`` — Movement/surface configuration, according to its declared type. **Returns:** ``true`` when the described condition holds; ``false`` otherwise.    |
+-------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-suspension--state-and-configuration-6:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------+----------------------------------------------------------------------------------------------+
| Member                                            | Meaning                                                                                      |
+===================================================+==============================================================================================+
| ``public override int ExecutionOrder { get; }``   | Default local priority within phase/category.                                                |
+---------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }`` | Cross-category execution barrier used by the module pipeline.                                |
+---------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``public float spring``                           | Authored spring used by Suspension. Initial value: ``26250``.                                |
+---------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``public float damper``                           | Authored damper used by Suspension. Initial value: ``2295``.                                 |
+---------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``public float targetPosition``                   | Authored target position used by Suspension. Initial value: ``0.5f``.                        |
+---------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``public float forceApplicationHeight``           | Authored force application height used by Suspension. Initial value: ``0.15f``.              |
+---------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``public bool automaticForceApplication``         | Place the wheel force application point below this vehicle's centre of mass.                 |
+---------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``public float forceOffsetBelowCenterOfMass``     | Authored force offset below center of mass used by Suspension. Initial value: ``.3f``.       |
+---------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``public float bodySwayTravelRatio``              | Additional force lever arm as a fraction of suspension travel, allowing body pitch and roll. |
+---------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``public float wheelDampingRate``                 | Authored wheel damping rate used by Suspension. Initial value: ``.02f``.                     |
+---------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``public bool limitExpansionVelocity``            | Authored limit expansion velocity used by Suspension. Initial value: ``true``.               |
+---------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``public bool degressiveDamping``                 | Limit high-speed damper force while keeping full low-speed body damping.                     |
+---------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``public float damperBlowoffSpeed``               | Suspension stroke speed where the damper force stops rising linearly (m/s).                  |
+---------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``public bool arcadeBumpDamping``                 | Game-oriented damping of excessive upward body motion while most wheels remain supported.    |
+---------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``public float supportedRiseSpeed``               | Authored supported rise speed used by Suspension. Initial value: ``.75f``.                   |
+---------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``public float bumpDampingResponse``              | Authored bump damping response used by Suspension. Initial value: ``10``.                    |
+---------------------------------------------------+----------------------------------------------------------------------------------------------+

.. _evs-api-suspension--suspensionaxle:

SuspensionAxle
--------------

**Runtime/Drive/Suspension/SuspensionAxle.cs**

Configuration/implementation type for suspension axle within suspension and linkage.

**Inherits / implements:** ``MonoBehaviour``.

.. _evs-api-suspension--methods-6:

Methods
~~~~~~~

+--------------------------------------+-----------------------------------------------------------------------------------------+----------------------------------+
| Signature                            | Role and behavior                                                                       | Arguments and result             |
+======================================+=========================================================================================+==================================+
| ``public virtual void UpdatePose()`` | Recomputes this visual linkage's pose from its authored geometry and current endpoints. | No arguments; no returned value. |
+--------------------------------------+-----------------------------------------------------------------------------------------+----------------------------------+

.. _evs-api-suspension--state-and-configuration-7:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Member                                           | Meaning                                                                                              |
+==================================================+======================================================================================================+
| ``public Transform leftAnchor``                  | Authored left anchor used by ``SuspensionAxle``.                                                     |
+--------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public Transform rightAnchor``                 | Authored right anchor used by ``SuspensionAxle``.                                                    |
+--------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public Transform housing``                     | Authored housing used by ``SuspensionAxle``.                                                         |
+--------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public Vector3 localLengthAxis``               | Authored local length axis used by ``SuspensionAxle``. Initial value: ``Vector3.up``.                |
+--------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public Vector3 rotationOffset``                | Authored rotation offset used by ``SuspensionAxle``.                                                 |
+--------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public SuspensionRotationLimits articulation`` | Authored articulation used by ``SuspensionAxle``. Initial value: ``new SuspensionRotationLimits()``. |
+--------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public float meshLength``                      | Authored mesh length used by ``SuspensionAxle``. Initial value: ``2``.                               |
+--------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public bool showGizmos``                       | Authored show gizmos used by ``SuspensionAxle``. Initial value: ``true``.                            |
+--------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public virtual float CurrentLength { get; }``  | Read-only/resolved current length for ``SuspensionAxle``.                                            |
+--------------------------------------------------+------------------------------------------------------------------------------------------------------+

.. _evs-api-suspension--suspensionhub:

SuspensionHub
-------------

**Runtime/Drive/Suspension/SuspensionHub.cs**

Provides hub/kingpin geometry for the wheel assembly.

**Inherits / implements:** ``MonoBehaviour``.

.. _evs-api-suspension--methods-7:

Methods
~~~~~~~

+--------------------------------------+-----------------------------------------------------------------------------------------+----------------------------------+
| Signature                            | Role and behavior                                                                       | Arguments and result             |
+======================================+=========================================================================================+==================================+
| ``public virtual void UpdatePose()`` | Recomputes this visual linkage's pose from its authored geometry and current endpoints. | No arguments; no returned value. |
+--------------------------------------+-----------------------------------------------------------------------------------------+----------------------------------+

.. _evs-api-suspension--state-and-configuration-8:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| Member                                             | Meaning                                                                                                |
+====================================================+========================================================================================================+
| ``public WheelCollider wheel``                     | Authored wheel used by ``SuspensionHub``.                                                              |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| ``public Wheel wheelAdapter``                      | Optional EVS wheel: follows its smoothed visual position after ``Wheel.LateUpdate``.                   |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| ``public SteeringTieRod steeringLinkage``          | Authored steering linkage used by ``SuspensionHub``.                                                   |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| ``public bool followSteering``                     | Authored follow steering used by ``SuspensionHub``. Initial value: ``true``.                           |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| ``public Vector3 positionOffset``                  | Authored position offset used by ``SuspensionHub``.                                                    |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| ``public Vector3 rotationOffset``                  | Authored rotation offset used by ``SuspensionHub``.                                                    |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| ``public SuspensionRotationLimits rotationLimits`` | Authored rotation limits used by ``SuspensionHub``. Initial value: ``new SuspensionRotationLimits()``. |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| ``public bool showGizmos``                         | Authored show gizmos used by ``SuspensionHub``. Initial value: ``true``.                               |
+----------------------------------------------------+--------------------------------------------------------------------------------------------------------+

.. _evs-api-suspension--suspensionrotationaxes:

SuspensionRotationAxes
----------------------

**Runtime/Drive/Suspension/SuspensionRotationLimits.cs**

Defines the allowed suspension rotation axes choices used by this topic.

.. _evs-api-suspension--values:

Values
~~~~~~

-  ``None = 0``
-  ``X = 1``
-  ``Y = 2``
-  ``Z = 4``
-  ``All = X \| Y \| Z``

.. _evs-api-suspension--suspensionrotationlimits:

SuspensionRotationLimits
------------------------

**Runtime/Drive/Suspension/SuspensionRotationLimits.cs**

Configuration/implementation type for suspension rotation limits within suspension and linkage.

.. _evs-api-suspension--methods-8:

Methods
~~~~~~~

+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                           | Role and behavior                                                                                | Arguments and result                                                                                                                                                                                                            |
+=====================================================================+==================================================================================================+=================================================================================================================================================================================================================================+
| ``public Quaternion Apply(Quaternion desired, Quaternion neutral)`` | Applies authored angular permissions/limits to a world rotation relative to its reference frame. | ``desired`` — Desired, interpreted by this operation in the declared type. ``neutral`` — Neutral reference orientation/pose. **Returns:** Returned Quaternion; ownership remains as specified by the creating/lookup operation. |
+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Quaternion ApplyLocal(Quaternion relative)``               | Constrains a local requested rotation to the configured angular permissions and bounds.          | ``relative`` — Whether the operation interprets its change relative to current state. **Returns:** Returned Quaternion; ownership remains as specified by the creating/lookup operation.                                        |
+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float Angle(float angle, Vector3 axis)``                   | Returns a signed angular component in degrees for the configured constrained frame.              | ``angle`` — Angular coordinate in degrees for this geometry operation. ``axis`` — Axis interpreted in the declaring geometry frame. **Returns:** Computed float in the operation's documented unit/domain.                      |
+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-suspension--state-and-configuration-9:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| Member                                        | Meaning                                                                                                         |
+===============================================+=================================================================================================================+
| ``public SuspensionRotationAxes allowedAxes`` | Authored allowed axes used by ``SuspensionRotationLimits``. Initial value: ``SuspensionRotationAxes.All``.      |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public bool limitAngles``                   | Authored limit angles used by ``SuspensionRotationLimits``.                                                     |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public Vector3 minimumAngles``              | Authored minimum angles used by ``SuspensionRotationLimits``. Initial value: ``new Vector3(-180, -180, -180)``. |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public Vector3 maximumAngles``              | Authored maximum angles used by ``SuspensionRotationLimits``. Initial value: ``new Vector3(180, 180, 180)``.    |
+-----------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
