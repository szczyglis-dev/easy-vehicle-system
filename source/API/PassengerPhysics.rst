.. _evs-api-passengerphysics--physical-passengers-and-limb-configuration-api:

Physical passengers and limb configuration API
==============================================

Read :doc:`the system explanation </Scripting/PassengerPhysics>` for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from ``MonoBehaviour``, ``Object`` or ``ScriptableObject`` are documented by Unity.

.. _evs-api-passengerphysics--types:

Types
-----

-  :ref:`HumanoidIK <evs-api-passengerphysics--humanoidik>`
-  :ref:`PassengerBodyPart <evs-api-passengerphysics--passengerbodypart>`
-  :ref:`PassengerBodyPartConfig <evs-api-passengerphysics--passengerbodypartconfig>`
-  :ref:`PassengerBodyPartMode <evs-api-passengerphysics--passengerbodypartmode>`
-  :ref:`PassengerFootConfig <evs-api-passengerphysics--passengerfootconfig>`
-  :ref:`PassengerHandConfig <evs-api-passengerphysics--passengerhandconfig>`
-  :ref:`PassengerRestraints <evs-api-passengerphysics--passengerrestraints>`
-  :ref:`RagdollCollisionHelper <evs-api-passengerphysics--ragdollcollisionhelper>`
-  :ref:`RagdollCollisionRelay <evs-api-passengerphysics--ragdollcollisionrelay>`

.. _evs-api-passengerphysics--humanoidik:

HumanoidIK
----------

**Runtime/World/Passengers/IK/HumanoidIK.cs**

Uses character frames to resolve limb targets.

**Inherits / implements:** ``MonoBehaviour``.

.. _evs-api-passengerphysics--methods:

Methods
~~~~~~~

+-------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                                                     | Role and behavior                                                                                          | Arguments and result                                                                                                                                                                                                                                                                                                                                                                                                                           |
+===============================================================================================================================+============================================================================================================+================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| ``public virtual void Solve(PassengerSeat seat)``                                                                             | Solves the mapped humanoid pose for the supplied limb targets/configuration.                               | ``seat`` — Seat context whose admission/occupancy rules remain authoritative.                                                                                                                                                                                                                                                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Solve(PassengerSeat seat, bool initializeFreeArms)``                                                    | Solves the mapped humanoid pose for the supplied limb targets/configuration.                               | ``seat`` — Seat context whose admission/occupancy rules remain authoritative. ``initializeFreeArms`` — Whether to establish an initial pose for otherwise free arms.                                                                                                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SolveHands(PassengerSeat seat)``                                                                        | Solves the selected hand targets using the character's mapped arm/palm frames.                             | ``seat`` — Seat context whose admission/occupancy rules remain authoritative.                                                                                                                                                                                                                                                                                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SolveHands(PassengerSeat seat, bool initializeFreeArms)``                                               | Solves the selected hand targets using the character's mapped arm/palm frames.                             | ``seat`` — Seat context whose admission/occupancy rules remain authoritative. ``initializeFreeArms`` — Whether to establish an initial pose for otherwise free arms.                                                                                                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SolveFootPosition(bool left, Vector3 position, Vector3 bend)``                                          | Solves a leg toward the requested ankle/foot target while respecting its mapped frames.                    | ``left`` — ``true`` selects the left hand; ``false`` selects the right. ``position`` — Requested point or switch detent; see its declared type and owning operation. ``bend`` — Bend, interpreted by this operation in the declared type.                                                                                                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void CapturePalmFrames()``                                                                                   | Captures the mapped wrist-to-palm frames used by subsequent hand targeting.                                | No arguments; no returned value.                                                                                                                                                                                                                                                                                                                                                                                                               |
+-------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void MapAnimator(Animator animator)``                                                                        | Resolves humanoid bone references from the supplied Animator, optionally filling only missing references.  | ``animator`` — Character Animator providing mapped bones/animation context.                                                                                                                                                                                                                                                                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void MapAnimator(Animator animator, bool fillMissingOnly)``                                                  | Resolves humanoid bone references from the supplied Animator, optionally filling only missing references.  | ``animator`` — Character Animator providing mapped bones/animation context. ``fillMissingOnly`` — Preserve existing mapped references and fill only missing ones.                                                                                                                                                                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryArmPose(PassengerSeat seat, bool left, out Quaternion upperRotation, out Quaternion lowerRotation)`` | Solves a candidate arm pose for the supplied target; ``false`` leaves the caller responsible for fallback. | ``seat`` — Seat context whose admission/occupancy rules remain authoritative. ``left`` — ``true`` selects the left hand; ``false`` selects the right. ``upperRotation`` — Upper rotation, interpreted by this operation in the declared type. ``lowerRotation`` — Lower rotation, interpreted by this operation in the declared type. **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values. |
+-------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryLegPose(PassengerSeat seat, bool left, out Quaternion upperRotation, out Quaternion lowerRotation)`` | Solves a candidate leg pose for the supplied ankle target.                                                 | ``seat`` — Seat context whose admission/occupancy rules remain authoritative. ``left`` — ``true`` selects the left hand; ``false`` selects the right. ``upperRotation`` — Upper rotation, interpreted by this operation in the declared type. ``lowerRotation`` — Lower rotation, interpreted by this operation in the declared type. **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values. |
+-------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-passengerphysics--state-and-configuration:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| Member                              | Meaning                                                                                                           |
+=====================================+===================================================================================================================+
| ``public Transform leftUpperArm``   | Authored left upper arm used by ``HumanoidIK``.                                                                   |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public Transform leftLowerArm``   | Authored left lower arm used by ``HumanoidIK``.                                                                   |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public Transform leftHand``       | Authored left hand used by ``HumanoidIK``.                                                                        |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public Transform rightUpperArm``  | Authored right upper arm used by ``HumanoidIK``.                                                                  |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public Transform rightLowerArm``  | Authored right lower arm used by ``HumanoidIK``.                                                                  |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public Transform rightHand``      | Authored right hand used by ``HumanoidIK``.                                                                       |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public Transform leftUpperLeg``   | Authored left upper leg used by ``HumanoidIK``.                                                                   |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public Transform leftLowerLeg``   | Authored left lower leg used by ``HumanoidIK``.                                                                   |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public Transform leftFoot``       | Authored left foot used by ``HumanoidIK``.                                                                        |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public Transform rightUpperLeg``  | Authored right upper leg used by ``HumanoidIK``.                                                                  |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public Transform rightLowerLeg``  | Authored right lower leg used by ``HumanoidIK``.                                                                  |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public Transform rightFoot``      | Authored right foot used by ``HumanoidIK``.                                                                       |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public bool matchTargetRotation`` | Authored match target rotation used by ``HumanoidIK``.                                                            |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public Transform leftElbowHint``  | Authored left elbow hint used by ``HumanoidIK``.                                                                  |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public Transform rightElbowHint`` | Authored right elbow hint used by ``HumanoidIK``.                                                                 |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public float maximumForearmRoll`` | Forearm roll for standalone IK without passenger anatomy. Passenger rigs use the saved elbow twist range instead. |
+-------------------------------------+-------------------------------------------------------------------------------------------------------------------+

.. _evs-api-passengerphysics--passengerbodypart:

PassengerBodyPart
-----------------

**Runtime/World/Passengers/Seats/PassengerBodyPartConfig.cs**

Defines the allowed passenger body part choices used by this topic.

.. _evs-api-passengerphysics--values:

Values
~~~~~~

-  ``LeftHand``
-  ``RightHand``
-  ``LeftFoot``
-  ``RightFoot``

.. _evs-api-passengerphysics--passengerbodypartconfig:

PassengerBodyPartConfig
-----------------------

**Runtime/World/Passengers/Seats/PassengerBodyPartConfig.cs**

Describes each limb's mode, target and support choices.

.. _evs-api-passengerphysics--methods-1:

Methods
~~~~~~~

+--------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                          | Role and behavior                                                          | Arguments and result                                                                                                                                                         |
+====================================================================+============================================================================+==============================================================================================================================================================================+
| ``public virtual Transform ResolveTarget(PassengerBodyPart part)`` | Resolves this limb configuration's effective direct/handle contact target. | ``part`` — Selected body-part enum or part configuration, as declared. **Returns:** Returned ``Transform``; ownership remains as specified by the creating/lookup operation. |
+--------------------------------------------------------------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-passengerphysics--state-and-configuration-1:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Member                                                  | Meaning                                                                                                                  |
+=========================================================+==========================================================================================================================+
| ``public Transform anchor``                             | Authored anchor used by ``PassengerBodyPartConfig``.                                                                     |
+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| ``public PassengerBodyPartMode mode``                   | Authored mode used by ``PassengerBodyPartConfig``.                                                                       |
+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| ``public VehicleHandle handle``                         | Authored handle used by ``PassengerBodyPartConfig``.                                                                     |
+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| ``public bool enableVehicleCollidersOnRelease``         | Enable contacts with the vehicle when this limb enters Free. The seat-wide setting also enables this for released limbs. |
+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| ``public bool enableSelfCollidersOnRelease``            | Enable contacts between this Free limb and the ragdoll's own body. Neighboring skeletal bodies keep collisions disabled. |
+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| ``public bool IsReleasedByDamage { get; }``             | Current is released by damage predicate; read it instead of maintaining a second application flag.                       |
+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| ``public PassengerBodyPartMode EffectiveMode { get; }`` | Read-only/resolved effective mode for ``PassengerBodyPartConfig``.                                                       |
+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| ``public bool IsControlled { get; }``                   | Whether this body part uses an IK handle rather than animation or free motion.                                           |
+---------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-passengerphysics--passengerbodypartmode:

PassengerBodyPartMode
---------------------

**Runtime/World/Passengers/Seats/PassengerBodyPartConfig.cs**

Defines the allowed passenger body part mode choices used by this topic.

.. _evs-api-passengerphysics--values-1:

Values
~~~~~~

-  ``[InspectorName("IK Handle")] IKHandle = 0``
-  ``Animator = 1``
-  ``Free = 2``

.. _evs-api-passengerphysics--passengerfootconfig:

PassengerFootConfig
-------------------

**Runtime/World/Passengers/Seats/PassengerBodyPartConfig.cs**

Per-foot mode, target and pinning/rotation configuration used by the seat.

**Inherits / implements:** :ref:`PassengerBodyPartConfig <evs-api-passengerphysics--passengerbodypartconfig>`.

.. _evs-api-passengerphysics--methods-2:

Methods
~~~~~~~

+---------------------------------------------+---------------------------------------------------------------------+---------------------------------------------------------------------------+
| Signature                                   | Role and behavior                                                   | Arguments and result                                                      |
+=============================================+=====================================================================+===========================================================================+
| ``public void PinTo(VehicleHandle target)`` | Assigns an ankle target/handle and the foot's hold/rotation policy. | ``target`` — Configured target object/point; see declared type and owner. |
+---------------------------------------------+---------------------------------------------------------------------+---------------------------------------------------------------------------+
| ``public void PinTo(Transform target)``     | Assigns an ankle target/handle and the foot's hold/rotation policy. | ``target`` — Configured target object/point; see declared type and owner. |
+---------------------------------------------+---------------------------------------------------------------------+---------------------------------------------------------------------------+
| ``public void ReleasePin()``                | Removes the foot's pinned target/hold policy.                       | No arguments; no returned value.                                          |
+---------------------------------------------+---------------------------------------------------------------------+---------------------------------------------------------------------------+

.. _evs-api-passengerphysics--state-and-configuration-2:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                 | Meaning                                                                                                                                                                                                                                       |
+========================================+===============================================================================================================================================================================================================================================+
| ``public bool hold``                   | Authored hold used by ``PassengerFootConfig``. Initial value: ``true``.                                                                                                                                                                       |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool pinToAnchor``            | Physically lock the foot position to its resolved anchor while Hold and IK Handle mode are enabled. Requires a physical seated passenger. Overrides spring and travel settings; ankle rotation remains free unless Align Rotation is enabled. |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool limitTravel``            | Authored limit travel used by ``PassengerFootConfig``.                                                                                                                                                                                        |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float travel``                | Authored travel used by ``PassengerFootConfig``. Initial value: ``.035f``.                                                                                                                                                                    |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumAcceleration``   | Authored maximum acceleration used by ``PassengerFootConfig``.                                                                                                                                                                                |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float spring``                | Authored spring used by ``PassengerFootConfig``. Initial value: ``1200``.                                                                                                                                                                     |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float damper``                | Authored damper used by ``PassengerFootConfig``. Initial value: ``70``.                                                                                                                                                                       |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool alignRotation``          | Guide the ankle orientation towards the authored target rotation, including moving pedals. Disabled by default.                                                                                                                               |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float rotationSpring``        | Authored rotation spring used by ``PassengerFootConfig``. Initial value: ``160``.                                                                                                                                                             |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float rotationDamper``        | Authored rotation damper used by ``PassengerFootConfig``. Initial value: ``12``.                                                                                                                                                              |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumRotationTorque`` | Authored maximum rotation torque used by ``PassengerFootConfig``. Initial value: ``25``.                                                                                                                                                      |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-passengerphysics--passengerhandconfig:

PassengerHandConfig
-------------------

**Runtime/World/Passengers/Seats/PassengerBodyPartConfig.cs**

Configuration/implementation type for passenger hand config within physical passengers and limb configuration.

**Inherits / implements:** :ref:`PassengerBodyPartConfig <evs-api-passengerphysics--passengerbodypartconfig>`.

.. _evs-api-passengerphysics--state-and-configuration-3:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                       | Meaning                                                                                                                                                                                                                                                     |
+==============================================+=============================================================================================================================================================================================================================================================+
| ``public bool animateThumb``                 | Allow grip solvers to pose the thumb. Disable to keep its authored local pose across handle changes.                                                                                                                                                        |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool palmContact``                  | Authored palm contact used by ``PassengerHandConfig``.                                                                                                                                                                                                      |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool hold``                         | Authored hold used by ``PassengerHandConfig``. Initial value: ``true``.                                                                                                                                                                                     |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float spring``                      | Authored spring used by ``PassengerHandConfig``. Initial value: ``2200``.                                                                                                                                                                                   |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float damper``                      | Authored damper used by ``PassengerHandConfig``. Initial value: ``180``.                                                                                                                                                                                    |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool relaxedRest``                  | Soft support around a direct hand anchor, with weaker arm pose motors and free wrist rotation. Reapply seated tuning after editing. Handles and palm grips retain their own support.                                                                        |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float restSpring``                  | Authored rest spring used by ``PassengerHandConfig``. Initial value: ``300``.                                                                                                                                                                               |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float restDamper``                  | Authored rest damper used by ``PassengerHandConfig``. Initial value: ``24``.                                                                                                                                                                                |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool limitRestTravel``              | Bound wrist distance from the rest anchor using a native joint limit. Disable for force-limited spring support only, allowing the hand to yield under larger loads. Reapply seated tuning after editing.                                                    |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float restTravel``                  | Authored rest travel used by ``PassengerHandConfig``. Initial value: ``.12f``.                                                                                                                                                                              |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumRestForce``            | Authored maximum rest force used by ``PassengerHandConfig``. Initial value: ``80``.                                                                                                                                                                         |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float restArmSpring``               | Authored rest arm spring used by ``PassengerHandConfig``. Initial value: ``6``.                                                                                                                                                                             |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float restArmDamper``               | Authored rest arm damper used by ``PassengerHandConfig``. Initial value: ``1.5f``.                                                                                                                                                                          |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float restArmMaximumTorque``        | Authored rest arm maximum torque used by ``PassengerHandConfig``. Initial value: ``15``.                                                                                                                                                                    |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool alignRestRotation``            | Let the physical resting wrist follow its anchor rotation with a bounded angular spring. Uses the calibrated palm frame when a ``HandGrip`` is present, otherwise the wrist frame. Reapply seated tuning after enabling; anchor rotation then updates live. |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float restRotationSpring``          | Authored rest rotation spring used by ``PassengerHandConfig``. Initial value: ``12``.                                                                                                                                                                       |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float restRotationDamper``          | Authored rest rotation damper used by ``PassengerHandConfig``. Initial value: ``2``.                                                                                                                                                                        |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumRestRotationTorque``   | Authored maximum rest rotation torque used by ``PassengerHandConfig``. Initial value: ``8``.                                                                                                                                                                |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool poseFreeArm``                  | In Free mode, pose this arm toward its direct anchor once on entry, then let it hang. No car-to-hand support or angular position spring is created. Reapply seated tuning to change the initial pose.                                                       |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float freeArmDamper``               | Authored free arm damper used by ``PassengerHandConfig``. Initial value: ``3``.                                                                                                                                                                             |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float freeArmMaximumDampingTorque`` | Authored free arm maximum damping torque used by ``PassengerHandConfig``. Initial value: ``15``.                                                                                                                                                            |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector3 freeWristRotation``         | Authored free wrist rotation used by ``PassengerHandConfig``.                                                                                                                                                                                               |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool UsesFreeArmPose { get; }``     | Read-only/resolved uses free arm pose for ``PassengerHandConfig``.                                                                                                                                                                                          |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool UsesRelaxedRest { get; }``     | Read-only/resolved uses relaxed rest for ``PassengerHandConfig``.                                                                                                                                                                                           |
+----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-passengerphysics--passengerrestraints:

PassengerRestraints
-------------------

**Runtime/World/Passengers/Physics/PassengerRestraints.cs**

Stores harness, release, damping and ejection configuration.

.. _evs-api-passengerphysics--state-and-configuration-4:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                             | Meaning                                                                                                                                                                 |
+====================================================+=========================================================================================================================================================================+
| ``public bool releaseHandsOnCollision``            | Let arms fall after a sufficiently strong vehicle contact.                                                                                                              |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool releaseFeetOnCollision``             | Release pedal/rest pins after a sufficiently strong contact.                                                                                                            |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool releaseHandsOnSpin``                 | Authored release hands on spin used by ``PassengerRestraints``. Initial value: ``false``.                                                                               |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool releaseFeetOnSpin``                  | Authored release feet on spin used by ``PassengerRestraints``. Initial value: ``false``.                                                                                |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float minimumReleaseCollisionForce``      | Minimum average collision force in newtons (contact impulse divided by the physics timestep). Both force and speed thresholds must be met.                              |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float minimumReleaseCollisionSpeed``      | Minimum relative collision speed in m/s. Filters small support contacts even on heavy vehicles.                                                                         |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float minimumReleaseAngle``               | Vehicle up angle from gravity up. 90 degrees means on its side; this detects roll/pitch, not ordinary yaw turns.                                                        |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float releaseTiltDelay``                  | Seconds continuously beyond the tilt angle before releasing limbs.                                                                                                      |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool enablePassengerEjection``            | Allow the whole occupant to detach from the seat into a free ragdoll. Removes every hand, foot, pelvis and chest restraint. Independent of the limb-only options above. |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool ejectPassengerOnCollision``          | Whole occupant release after a sufficiently strong new contact.                                                                                                         |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool ejectPassengerOnSpin``               | Whole occupant release after sustained roll/pitch tilt.                                                                                                                 |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float minimumEjectionCollisionForce``     | Minimum average contact force in N: impulse divided by the physics timestep.                                                                                            |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float minimumEjectionCollisionSpeed``     | Minimum relative collision speed in m/s; force and speed thresholds must both be met.                                                                                   |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float minimumEjectionAngle``              | Authored minimum ejection angle used by ``PassengerRestraints``. Initial value: ``90``.                                                                                 |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float ejectionTiltDelay``                 | Authored ejection tilt delay used by ``PassengerRestraints``. Initial value: ``.1f``.                                                                                   |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector3 passengerEjectionVelocity``       | Optional additional velocity in vehicle-local m/s. Existing ragdoll linear/angular motion is preserved.                                                                 |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool reseatEjectedOnReset``               | Authored reseat ejected on reset used by ``PassengerRestraints``. Initial value: ``true``.                                                                              |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public int solverIterations``                    | Minimum solver iterations on seated bones only. Zero preserves the body's setting; higher authored values are retained. Restored on release.                            |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public int solverVelocityIterations``            | Authored solver velocity iterations used by ``PassengerRestraints``. Initial value: ``4``.                                                                              |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float relativeLinearDamping``             | Damping per second relative to the vehicle velocity at each bone, not world-space drag. Zero disables it.                                                               |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float relativeAngularDamping``            | Angular damping per second relative to the vehicle. Zero disables it.                                                                                                   |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumDampingAcceleration``        | Maximum additional damping acceleration in m/s². Zero disables linear damping.                                                                                          |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumDampingAngularAcceleration`` | Maximum additional angular damping acceleration in rad/s². Zero disables angular damping.                                                                               |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float seatSpring``                        | Authored seat spring used by ``PassengerRestraints``. Initial value: ``14000``.                                                                                         |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float seatDamper``                        | Authored seat damper used by ``PassengerRestraints``. Initial value: ``1300``.                                                                                          |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float torsoSwayDegrees``                  | Authored torso sway degrees used by ``PassengerRestraints``. Initial value: ``12``.                                                                                     |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float seatTravel``                        | Authored seat travel used by ``PassengerRestraints``. Initial value: ``.025f``.                                                                                         |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool softHarness``                        | Bounded native spring drives support pelvis and chest without bone pose overrides. Foot pins are configured separately on each foot.                                    |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool limitHarnessTravel``                 | Keep the pelvis inside Seat Travel and the chest inside Chest Travel using native joint limits. Angular sway stays physical.                                            |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float chestSupportStrength``              | Scales chest support independently of the pelvis. Reapply seated tuning or re-enter the seat after editing. One preserves the original support.                         |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float harnessChestTravel``                | Authored harness chest travel used by ``PassengerRestraints``. Initial value: ``.06f``.                                                                                 |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float harnessFrequency``                  | Authored harness frequency used by ``PassengerRestraints``. Initial value: ``3``.                                                                                       |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float harnessDampingRatio``               | Authored harness damping ratio used by ``PassengerRestraints``. Initial value: ``1``.                                                                                   |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float harnessMaximumAcceleration``        | Authored harness maximum acceleration used by ``PassengerRestraints``. Initial value: ``80``.                                                                           |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float harnessAngularSpring``              | Authored harness angular spring used by ``PassengerRestraints``. Initial value: ``16``.                                                                                 |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float harnessAngularDamper``              | Authored harness angular damper used by ``PassengerRestraints``. Initial value: ``3``.                                                                                  |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float harnessMaximumTorquePerKg``         | Authored harness maximum torque per kg used by ``PassengerRestraints``. Initial value: ``8``.                                                                           |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float harnessSideLean``                   | Soft angular travel around the captured seated pose, measured in seat axes.                                                                                             |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float harnessForwardLean``                | Authored harness forward lean used by ``PassengerRestraints``. Initial value: ``22``.                                                                                   |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float harnessTwist``                      | Authored harness twist used by ``PassengerRestraints``. Initial value: ``28``.                                                                                          |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float harnessLimitSpringPerKg``           | Authored harness limit spring per kg used by ``PassengerRestraints``. Initial value: ``60``.                                                                            |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float harnessLimitDamperPerKg``           | Authored harness limit damper per kg used by ``PassengerRestraints``. Initial value: ``6``.                                                                             |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-passengerphysics--ragdollcollisionhelper:

RagdollCollisionHelper
----------------------

**Runtime/World/Damage/RagdollCollisionHelper.cs**

Configuration/implementation type for ragdoll collision helper within physical passengers and limb configuration.

**Inherits / implements:** ``MonoBehaviour``, :ref:`ICollisionDamageResponse <evs-api-damage--icollisiondamageresponse>`.

.. _evs-api-passengerphysics--state-and-configuration-5:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                      | Meaning                                                                                                                                                                       |
+=============================================================+===============================================================================================================================================================================+
| ``public float minimumImpactSpeed``                         | Minimum incoming normal speed of the contacting body and relative impact required to knock down a standing character. Idle animation touching a parked body is not an impact. |
+-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumBoneSpeed``                           | Free-flight bone speed cap in metres/second; moving contacts temporarily raise this budget.                                                                                   |
+-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumCarrySpeed``                          | Maximum contacting-body speed used for the temporary carry budget, plus 2 m/s slack. Fades after release; never applies a force.                                              |
+-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumUpwardSpeed``                         | Upward speed cap prevents launch impulses while allowing the body to climb a hood.                                                                                            |
+-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumAngularSpeed``                        | Maximum bone angular speed in radians/second.                                                                                                                                 |
+-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumDepenetrationSpeed``                  | Maximum native overlap correction speed in metres/second.                                                                                                                     |
+-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool disableJointProjection``                      | Authored disable joint projection used by ``RagdollCollisionHelper``. Initial value: ``true``.                                                                                |
+-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool useSpeculativeContacts``                      | Speculative contacts while standing/animated. Dynamic ragdolls use Ragdoll Collision Detection instead to avoid speculative ghost contacts moving resting joints.             |
+-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public CollisionDetectionMode ragdollCollisionDetection`` | Authored ragdoll collision detection used by ``RagdollCollisionHelper``. Initial value: ``CollisionDetectionMode.ContinuousDynamic``.                                         |
+-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float vehicleResponse``                            | Inverse-mass/inertia response of the other dynamic body for this contact only. Zero makes the contact one-way.                                                                |
+-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumContactVelocityChange``               | Maximum contact impulse per bone/pair in units of bone mass times this velocity change.                                                                                       |
+-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float vehicleContactFriction``                     | Authored vehicle contact friction used by ``RagdollCollisionHelper``. Initial value: ``.45f``.                                                                                |
+-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float vehicleDamageScale``                         | Scales collision speed used for vehicle damage; normal environment collisions remain unchanged.                                                                               |
+-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool IsKnockedDown { get; }``              | Current is knocked down predicate; read it instead of maintaining a second application flag.                                                                                  |
+-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float CollisionDamageScale { get; }``      | Read-only/resolved collision damage scale for ``RagdollCollisionHelper``.                                                                                                     |
+-------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-passengerphysics--ragdollcollisionrelay:

RagdollCollisionRelay
---------------------

**Runtime/World/Damage/RagdollCollisionRelay.cs**

Configuration/implementation type for ragdoll collision relay within physical passengers and limb configuration.

**Inherits / implements:** ``MonoBehaviour``.
