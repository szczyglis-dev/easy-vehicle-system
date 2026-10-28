.. _evs-api-passengercontrollers--seats-bodies-and-controller-strategies-api:

Seats, bodies and controller strategies API
===========================================

Read :doc:`the system explanation </Scripting/PassengerControllers>` for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from ``MonoBehaviour``, ``Object`` or ``ScriptableObject`` are documented by Unity.

.. _evs-api-passengercontrollers--types:

Types
-----

-  :ref:`AnimatorIKPassengerController <evs-api-passengercontrollers--animatorikpassengercontroller>`
-  :ref:`AnimatorPassengerController <evs-api-passengercontrollers--animatorpassengercontroller>`
-  :ref:`AttachOnlyPassengerController <evs-api-passengercontrollers--attachonlypassengercontroller>`
-  :ref:`CustomPassengerBody <evs-api-passengercontrollers--custompassengerbody>`
-  :ref:`CustomPassengerController <evs-api-passengercontrollers--custompassengercontroller>`
-  :ref:`HumanoidPassenger <evs-api-passengercontrollers--humanoidpassenger>`
-  :ref:`IPassengerModule <evs-api-passengercontrollers--ipassengermodule>`
-  :ref:`MotorcycleRider <evs-api-passengercontrollers--motorcyclerider>`
-  :ref:`PassengerBehaviour <evs-api-passengercontrollers--passengerbehaviour>`
-  :ref:`PassengerBody <evs-api-passengercontrollers--passengerbody>`
-  :ref:`PassengerController <evs-api-passengercontrollers--passengercontroller>`
-  :ref:`PassengerControllerType <evs-api-passengercontrollers--passengercontrollertype>`
-  :ref:`PassengerExitReason <evs-api-passengercontrollers--passengerexitreason>`
-  :ref:`PassengerModule <evs-api-passengercontrollers--passengermodule>`
-  :ref:`PassengerSeat <evs-api-passengercontrollers--passengerseat>`
-  :ref:`PassengerType <evs-api-passengercontrollers--passengertype>`
-  :ref:`Passengers <evs-api-passengercontrollers--passengers>`
-  :ref:`RagdollPhysicsPassengerController <evs-api-passengercontrollers--ragdollphysicspassengercontroller>`

.. _evs-api-passengercontrollers--animatorikpassengercontroller:

AnimatorIKPassengerController
-----------------------------

**Runtime/World/Passengers/Controllers/AnimatorIKPassengerController.cs**

Configuration/implementation type for animator ikpassenger controller within seats, bodies and controller strategies.

**Inherits / implements:** :ref:`PassengerController <evs-api-passengercontrollers--passengercontroller>`.

.. _evs-api-passengercontrollers--methods:

Methods
~~~~~~~

+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                               | Role and behavior                                                                                                   | Arguments and result                                                                                                                                                                                                                                                                   |
+=========================================================================+=====================================================================================================================+========================================================================================================================================================================================================================================================================================+
| ``public override bool Attach(PassengerBody body, PassengerSeat seat)`` | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. | ``body`` — Character or rigidbody context, according to the declared type. ``seat`` — Seat context whose admission/occupancy rules remain authoritative. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-passengercontrollers--state-and-configuration:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------+----------------------------------------------------------------+
| Member                                                    | Meaning                                                        |
+===========================================================+================================================================+
| ``public override PassengerControllerType Type { get; }`` | Read-only/resolved type for ``AnimatorIKPassengerController``. |
+-----------------------------------------------------------+----------------------------------------------------------------+

.. _evs-api-passengercontrollers--animatorpassengercontroller:

AnimatorPassengerController
---------------------------

**Runtime/World/Passengers/Controllers/AnimatorPassengerController.cs**

Configuration/implementation type for animator passenger controller within seats, bodies and controller strategies.

**Inherits / implements:** :ref:`PassengerController <evs-api-passengercontrollers--passengercontroller>`.

.. _evs-api-passengercontrollers--methods-1:

Methods
~~~~~~~

+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                               | Role and behavior                                                                                                   | Arguments and result                                                                                                                                                                                                                                                                   |
+=========================================================================+=====================================================================================================================+========================================================================================================================================================================================================================================================================================+
| ``public override bool Attach(PassengerBody body, PassengerSeat seat)`` | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. | ``body`` — Character or rigidbody context, according to the declared type. ``seat`` — Seat context whose admission/occupancy rules remain authoritative. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-passengercontrollers--state-and-configuration-1:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------+--------------------------------------------------------------+
| Member                                                    | Meaning                                                      |
+===========================================================+==============================================================+
| ``public override PassengerControllerType Type { get; }`` | Read-only/resolved type for ``AnimatorPassengerController``. |
+-----------------------------------------------------------+--------------------------------------------------------------+

.. _evs-api-passengercontrollers--attachonlypassengercontroller:

AttachOnlyPassengerController
-----------------------------

**Runtime/World/Passengers/Controllers/AttachOnlyPassengerController.cs**

Configuration/implementation type for attach only passenger controller within seats, bodies and controller strategies.

**Inherits / implements:** :ref:`PassengerController <evs-api-passengercontrollers--passengercontroller>`.

.. _evs-api-passengercontrollers--methods-2:

Methods
~~~~~~~

+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                               | Role and behavior                                                                                                   | Arguments and result                                                                                                                                                                                                                                                                   |
+=========================================================================+=====================================================================================================================+========================================================================================================================================================================================================================================================================================+
| ``public override bool Attach(PassengerBody body, PassengerSeat seat)`` | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. | ``body`` — Character or rigidbody context, according to the declared type. ``seat`` — Seat context whose admission/occupancy rules remain authoritative. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-passengercontrollers--state-and-configuration-2:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------+----------------------------------------------------------------+
| Member                                                    | Meaning                                                        |
+===========================================================+================================================================+
| ``public override PassengerControllerType Type { get; }`` | Read-only/resolved type for ``AttachOnlyPassengerController``. |
+-----------------------------------------------------------+----------------------------------------------------------------+

.. _evs-api-passengercontrollers--custompassengerbody:

CustomPassengerBody
-------------------

**Runtime/World/Passengers/Bodies/CustomPassengerBody.cs**

Minimal body for application-owned Custom occupancy.

**Inherits / implements:** :ref:`PassengerBody <evs-api-passengercontrollers--passengerbody>`.

.. _evs-api-passengercontrollers--methods-3:

Methods
~~~~~~~

+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                 | Role and behavior                                                                                                   | Arguments and result                                                                                                                                                                                                                          |
+===========================================================================================+=====================================================================================================================+===============================================================================================================================================================================================================================================+
| ``public override bool CanEnter(PassengerSeat seat)``                                     | Checks body/seat compatibility before attachment; overloads distinguish seat and controller-strategy requirements.  | ``seat`` — Seat context whose admission/occupancy rules remain authoritative. **Returns:** ``true`` when the described condition holds; ``false`` otherwise.                                                                                  |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool CanEnter(PassengerSeat seat, PassengerControllerType controller)`` | Checks body/seat compatibility before attachment; overloads distinguish seat and controller-strategy requirements.  | ``seat`` — Seat context whose admission/occupancy rules remain authoritative. ``controller`` — Controller, interpreted by this operation in the declared type. **Returns:** ``true`` when the described condition holds; ``false`` otherwise. |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool Attach(PassengerSeat seat)``                                       | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. | ``seat`` — Seat context whose admission/occupancy rules remain authoritative. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated.                                   |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Detach(PassengerExitReason reason)``                               | Ends the owned character or hitch relationship and releases the state/resources owned by that relationship.         | ``reason`` — Reason for occupancy release, used by controller/body cleanup policy.                                                                                                                                                            |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-passengercontrollers--custompassengercontroller:

CustomPassengerController
-------------------------

**Runtime/World/Passengers/Controllers/CustomPassengerController.cs**

Configuration/implementation type for custom passenger controller within seats, bodies and controller strategies.

**Inherits / implements:** :ref:`PassengerController <evs-api-passengercontrollers--passengercontroller>`.

.. _evs-api-passengercontrollers--methods-4:

Methods
~~~~~~~

+----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                          | Role and behavior                                                                                                   | Arguments and result                                                                                                                                                                                                                                                                   |
+====================================================================================================+=====================================================================================================================+========================================================================================================================================================================================================================================================================================+
| ``public override bool Attach(PassengerBody body, PassengerSeat seat)``                            | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. | ``body`` — Character or rigidbody context, according to the declared type. ``seat`` — Seat context whose admission/occupancy rules remain authoritative. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
+----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Detach(PassengerBody body, PassengerExitReason reason, bool preservePose)`` | Ends the owned character or hitch relationship and releases the state/resources owned by that relationship.         | ``body`` — Character or rigidbody context, according to the declared type. ``reason`` — Reason for occupancy release, used by controller/body cleanup policy. ``preservePose`` — Whether this handover must retain the current character pose.                                         |
+----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-passengercontrollers--state-and-configuration-3:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------+------------------------------------------------------------+
| Member                                                    | Meaning                                                    |
+===========================================================+============================================================+
| ``public override PassengerControllerType Type { get; }`` | Read-only/resolved type for ``CustomPassengerController``. |
+-----------------------------------------------------------+------------------------------------------------------------+

.. _evs-api-passengercontrollers--humanoidpassenger:

HumanoidPassenger
-----------------

**Runtime/World/Passengers/Bodies/HumanoidPassenger.cs**

Connects humanoid rig, pose and physical passenger behavior.

**Inherits / implements:** :ref:`PassengerBody <evs-api-passengercontrollers--passengerbody>`.

.. _evs-api-passengercontrollers--methods-5:

Methods
~~~~~~~

+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                 | Role and behavior                                                                                                   | Arguments and result                                                                                                                                                                                                                          |
+===========================================================================================+=====================================================================================================================+===============================================================================================================================================================================================================================================+
| ``public virtual void PrepareRagdollCollisions()``                                        | Prepares the character's skeletal collision exclusions and collision relays.                                        | No arguments; no returned value.                                                                                                                                                                                                              |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool Attach(PassengerSeat seat)``                                       | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. | ``seat`` — Seat context whose admission/occupancy rules remain authoritative. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated.                                   |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SolveSeatedIK()``                                                   | Applies the seated character's configured limb IK targets.                                                          | No arguments; no returned value.                                                                                                                                                                                                              |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void StepSeated(Passengers core, float deltaTime)``                     | Advances this body's seated behavior through its selected character path.                                           | ``core`` — Owning audio or passenger core supplying shared context. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop.                                                                                                      |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void ResetSeatedPose()``                                                | Restores the character's seated pose/support through the selected physical/animation path.                          | No arguments; no returned value.                                                                                                                                                                                                              |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void DetachForTransition()``                                            | Releases seated ownership for an animated character handover while preserving the required transition pose.         | No arguments; no returned value.                                                                                                                                                                                                              |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Detach(PassengerExitReason reason)``                               | Ends the owned character or hitch relationship and releases the state/resources owned by that relationship.         | ``reason`` — Reason for occupancy release, used by controller/body cleanup policy.                                                                                                                                                            |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ActivateRagdoll()``                                                 | Hands the character to free skeletal physics, releasing seated pose ownership.                                      | No arguments; no returned value.                                                                                                                                                                                                              |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool CanEnter(PassengerSeat seat)``                                     | Checks body/seat compatibility before attachment; overloads distinguish seat and controller-strategy requirements.  | ``seat`` — Seat context whose admission/occupancy rules remain authoritative. **Returns:** ``true`` when the described condition holds; ``false`` otherwise.                                                                                  |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool CanEnter(PassengerSeat seat, PassengerControllerType controller)`` | Checks body/seat compatibility before attachment; overloads distinguish seat and controller-strategy requirements.  | ``seat`` — Seat context whose admission/occupancy rules remain authoritative. ``controller`` — Controller, interpreted by this operation in the declared type. **Returns:** ``true`` when the described condition holds; ``false`` otherwise. |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void RestoreAccessReferencePose()``                                      | Restores the character pose retained for an access-motion handover.                                                 | No arguments; no returned value.                                                                                                                                                                                                              |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void PreviewAccessPose(PassengerSeat seat)``                             | Applies an access reference pose for character/seat authoring or transition preparation.                            | ``seat`` — Seat context whose admission/occupancy rules remain authoritative.                                                                                                                                                                 |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void AddVelocity(Vector3 velocityChange)``                              | Adds the supplied velocity change to the character bodies used by this body implementation.                         | ``velocityChange`` — World velocity change in m/s.                                                                                                                                                                                            |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ReadAnatomicalJointSettings()``                                     | Reads saved native joint configuration into the character's runtime anatomical references.                          | No arguments; no returned value.                                                                                                                                                                                                              |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-passengercontrollers--events-and-inspector-callbacks:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| Declaration                                                      | Trigger, payload and meaning                                                                                                     |
+==================================================================+==================================================================================================================================+
| ``public event System.Action<HumanoidPassenger> BeforeSeatedIK`` | Immediately before seated IK work. Payload: ``HumanoidPassenger``; custom pose inputs must respect the selected character owner. |
+------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``public event System.Action<HumanoidPassenger> AfterSeatedIK``  | Immediately after seated IK work. Payload: ``HumanoidPassenger``.                                                                |
+------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-passengercontrollers--state-and-configuration-4:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                                | Meaning                                                                                                                                                                                   |
+=======================================================================+===========================================================================================================================================================================================+
| ``public Animator animator``                                          | Inspector configuration.                                                                                                                                                                  |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform pelvis``                                           | Authored pelvis used by ``HumanoidPassenger``.                                                                                                                                            |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public HumanoidIK ik``                                              | Authored ik used by ``HumanoidPassenger``.                                                                                                                                                |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool physicalWhileSeated``                                   | Keeps the seated skeleton physically simulated rather than attaching it as a kinematic character.                                                                                         |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float exitCollisionClearance``                               | Keep the previous vehicle excluded until the departing character clears its combined collider bounds by this distance. Prevents animated kinematic limbs from blocking the doors/chassis. |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public HumanoidJointDefinition[] anatomicalJoints``                 | Configured skeletal joints and reference data used by IK. Tune axes, anchors and limits on each ``ConfigurableJoint`` component.                                                          |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float freeRagdollAngularDamping``                            | Passive rotational damping while falling or lying down. Does not hold a pose or freeze bones.                                                                                             |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public int freeRagdollSolverIterations``                            | Authored free ragdoll solver iterations used by ``HumanoidPassenger``. Initial value: ``12``.                                                                                             |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public int freeRagdollSolverVelocityIterations``                    | Authored free ragdoll solver velocity iterations used by ``HumanoidPassenger``. Initial value: ``4``.                                                                                     |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool freeRagdollPreprocessing``                              | Enable joint preprocessing for free ragdolls. Leave off when impacts pin bones against the ground: preprocessing incompatible contact/joint constraints can sustain head oscillations.    |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float freeRagdollJointDamping``                              | Passive damping of relative bone rotation. The pose spring stays zero, so joints never return to a riding/idle pose.                                                                      |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float freeRagdollMaximumDampingTorque``                      | Authored free ragdoll maximum damping torque used by ``HumanoidPassenger``. Initial value: ``20``.                                                                                        |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Rigidbody[] ragdollBodies``                                  | Authored ragdoll bodies used by ``HumanoidPassenger``. Initial value: ``System.Array.Empty<Rigidbody>()``.                                                                                |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual ConfigurableJoint[] authoredRagdollJoints { get; }`` | Joint components from the anatomical configuration.                                                                                                                                       |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool automaticSeatedIK``                                     | Apply the Animator + IK overlay in ``LateUpdate``. Disable to call ``SolveSeatedIK`` from your own animation pipeline.                                                                    |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool IsRagdollActive { get; protected set; }``       | Current is ragdoll active predicate; read it instead of maintaining a second application flag.                                                                                            |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual int RestraintCount { get; }``                        | Read-only/resolved restraint count for ``HumanoidPassenger``.                                                                                                                             |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SoftHarness { get; }``                          | Read-only/resolved soft harness for ``HumanoidPassenger``.                                                                                                                                |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual Animator SeatedAnimator { get; }``                   | Read-only/resolved seated animator for ``HumanoidPassenger``.                                                                                                                             |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-passengercontrollers--ipassengermodule:

IPassengerModule
----------------

**Runtime/World/Passengers/Core/PassengerModule.cs**

Configuration/implementation type for ipassenger module within seats, bodies and controller strategies.

**Inherits / implements:** :ref:`IWorldModule <evs-api-modules--iworldmodule>`.

.. _evs-api-passengercontrollers--motorcyclerider:

MotorcycleRider
---------------

**Runtime/World/Passengers/Seats/MotorcycleRider.cs**

Configuration/implementation type for motorcycle rider within seats, bodies and controller strategies.

**Inherits / implements:** :ref:`PassengerBehaviour <evs-api-passengercontrollers--passengerbehaviour>`.

.. _evs-api-passengercontrollers--methods-6:

Methods
~~~~~~~

+---------------------------------------------------------------+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                     | Role and behavior                                                             | Arguments and result                                                                                                                                                                       |
+===============================================================+===============================================================================+============================================================================================================================================================================================+
| ``public override void ResetPassenger(Passengers core)``      | Resets this passenger behavior's state for the supplied seat.                 | ``core`` — Owning audio or passenger core supplying shared context.                                                                                                                        |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool AppliesTo(VehicleController vehicle)`` | Checks whether this passenger behavior should run for the supplied seat/role. | ``vehicle`` — Vehicle context/owner receiving the operation. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-passengercontrollers--state-and-configuration-5:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Member                                                       | Meaning                                                                                                                   |
+==============================================================+===========================================================================================================================+
| ``public bool motorcycleProfileOnly``                        | Run this rider behaviour only while the vehicle uses ``MotorcycleProfile``. Disable to use it with another drive profile. |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public Transform leftFootGround``                          | Authored left foot ground used by ``MotorcycleRider``.                                                                    |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public Transform rightFootGround``                         | Authored right foot ground used by ``MotorcycleRider``.                                                                   |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public Transform leftFootRiding``                          | Authored left foot riding used by ``MotorcycleRider``.                                                                    |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public Transform rightFootRiding``                         | Authored right foot riding used by ``MotorcycleRider``.                                                                   |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public float liftStartsAtKph``                             | Authored lift starts at kph used by ``MotorcycleRider``. Initial value: ``1``.                                            |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public float fullyRaisedAtKph``                            | Authored fully raised at kph used by ``MotorcycleRider``. Initial value: ``8``.                                           |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public float blendSpeed``                                  | Authored blend speed used by ``MotorcycleRider``. Initial value: ``4``.                                                   |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float RidingBlend { get; protected set; }`` | Read-only/resolved riding blend for ``MotorcycleRider``.                                                                  |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-passengercontrollers--passengerbehaviour:

PassengerBehaviour
------------------

**Runtime/World/Passengers/Core/PassengerBehaviour.cs**

Configuration/implementation type for passenger behaviour within seats, bodies and controller strategies.

**Inherits / implements:** :ref:`PassengerModule <evs-api-passengercontrollers--passengermodule>`.

.. _evs-api-passengercontrollers--methods-7:

Methods
~~~~~~~

+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                       | Role and behavior                                                             | Arguments and result                                                                                                                                                                       |
+=================================================================================+===============================================================================+============================================================================================================================================================================================+
| ``public sealed override void StepPassenger(Passengers core, float deltaTime)`` | Advances passenger work in the supplied seat/core context.                    | ``core`` — Owning audio or passenger core supplying shared context. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop.                                                   |
+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool AppliesTo(VehicleController vehicle)``                    | Checks whether this passenger behavior should run for the supplied seat/role. | ``vehicle`` — Vehicle context/owner receiving the operation. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-passengercontrollers--state-and-configuration-6:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------+-----------------------------------------------+
| Member                                          | Meaning                                       |
+=================================================+===============================================+
| ``public PassengerSeat seat``                   | Authored seat used by ``PassengerBehaviour``. |
+-------------------------------------------------+-----------------------------------------------+
| ``public override int ExecutionOrder { get; }`` | Default local priority within phase/category. |
+-------------------------------------------------+-----------------------------------------------+

.. _evs-api-passengercontrollers--passengerbody:

PassengerBody
-------------

**Runtime/World/Passengers/Bodies/PassengerBody.cs**

Base character adapter used by seats and controller strategies.

**Inherits / implements:** ``MonoBehaviour``.

.. _evs-api-passengercontrollers--methods-8:

Methods
~~~~~~~

+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                | Role and behavior                                                                                                   | Arguments and result                                                                                                                                                                                                                          |
+==========================================================================================+=====================================================================================================================+===============================================================================================================================================================================================================================================+
| ``public abstract bool Attach(PassengerSeat seat)``                                      | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. | ``seat`` — Seat context whose admission/occupancy rules remain authoritative. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated.                                   |
+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public abstract void Detach(PassengerExitReason reason)``                              | Ends the owned character or hitch relationship and releases the state/resources owned by that relationship.         | ``reason`` — Reason for occupancy release, used by controller/body cleanup policy.                                                                                                                                                            |
+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void DetachForTransition()``                                            | Releases seated ownership for an animated character handover while preserving the required transition pose.         | No arguments; no returned value.                                                                                                                                                                                                              |
+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void StepSeated(Passengers core, float deltaTime)``                     | Advances this body's seated behavior through its selected character path.                                           | ``core`` — Owning audio or passenger core supplying shared context. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop.                                                                                                      |
+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ResetSeatedPose()``                                                | Restores the character's seated pose/support through the selected physical/animation path.                          | No arguments; no returned value.                                                                                                                                                                                                              |
+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool CanEnter(PassengerSeat seat)``                                     | Checks body/seat compatibility before attachment; overloads distinguish seat and controller-strategy requirements.  | ``seat`` — Seat context whose admission/occupancy rules remain authoritative. **Returns:** ``true`` when the described condition holds; ``false`` otherwise.                                                                                  |
+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool CanEnter(PassengerSeat seat, PassengerControllerType controller)`` | Checks body/seat compatibility before attachment; overloads distinguish seat and controller-strategy requirements.  | ``seat`` — Seat context whose admission/occupancy rules remain authoritative. ``controller`` — Controller, interpreted by this operation in the declared type. **Returns:** ``true`` when the described condition holds; ``false`` otherwise. |
+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void AddVelocity(Vector3 velocityChange)``                              | Adds the supplied velocity change to the character bodies used by this body implementation.                         | ``velocityChange`` — World velocity change in m/s.                                                                                                                                                                                            |
+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-passengercontrollers--state-and-configuration-7:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| Member                                                                 | Meaning                                                                                               |
+========================================================================+=======================================================================================================+
| ``public virtual PassengerSeat Seat { get; protected set; }``          | Read-only/resolved seat for ``PassengerBody``.                                                        |
+------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| ``public virtual bool IsExternallyControlled { get; protected set; }`` | Current is externally controlled predicate; read it instead of maintaining a second application flag. |
+------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| ``public virtual bool IsCustomControlled { get; protected set; }``     | Current is custom controlled predicate; read it instead of maintaining a second application flag.     |
+------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+

.. _evs-api-passengercontrollers--passengercontroller:

PassengerController
-------------------

**Runtime/World/Passengers/Controllers/PassengerController.cs**

Per-seat strategy for body attachment, detachment and stepping; the seat retains occupancy authority.

.. _evs-api-passengercontrollers--methods-9:

Methods
~~~~~~~

+---------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                         | Role and behavior                                                                                                              | Arguments and result                                                                                                                                                                                                                                                                   |
+===================================================================================================+================================================================================================================================+========================================================================================================================================================================================================================================================================================+
| ``public abstract bool Attach(PassengerBody body, PassengerSeat seat)``                           | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication.            | ``body`` — Character or rigidbody context, according to the declared type. ``seat`` — Seat context whose admission/occupancy rules remain authoritative. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
+---------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Detach(PassengerBody body, PassengerExitReason reason, bool preservePose)`` | Ends the owned character or hitch relationship and releases the state/resources owned by that relationship.                    | ``body`` — Character or rigidbody context, according to the declared type. ``reason`` — Reason for occupancy release, used by controller/body cleanup policy. ``preservePose`` — Whether this handover must retain the current character pose.                                         |
+---------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Step(PassengerBody body, Passengers core, float deltaTime)``                | Empty base passenger strategy step; derived strategies decide which body work they own.                                        | ``body`` — Character or rigidbody context, according to the declared type. ``core`` — Owning audio or passenger core supplying shared context. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop.                                                                    |
+---------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public static PassengerController Create(PassengerControllerType type)``                        | Creates the built-in strategy for a ``PassengerControllerType``; seat factory overrides can substitute application strategies. | ``type`` — Type, interpreted by this operation in the declared type. **Returns:** Returned ``PassengerController``; ownership remains as specified by the creating/lookup operation.                                                                                                   |
+---------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-passengercontrollers--state-and-configuration-8:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------+------------------------------------------------------+
| Member                                                    | Meaning                                              |
+===========================================================+======================================================+
| ``public abstract PassengerControllerType Type { get; }`` | Read-only/resolved type for ``PassengerController``. |
+-----------------------------------------------------------+------------------------------------------------------+

.. _evs-api-passengercontrollers--passengercontrollertype:

PassengerControllerType
-----------------------

**Runtime/World/Passengers/Controllers/PassengerController.cs**

Defines the allowed passenger controller type choices used by this topic.

.. _evs-api-passengercontrollers--values:

Values
~~~~~~

-  ``RagdollPhysics = 0``
-  ``Animator = 1``
-  ``[InspectorName("Animator + IK")] AnimatorIK = 2``
-  ``AttachOnly = 3``
-  ``Custom = 4``

.. _evs-api-passengercontrollers--passengerexitreason:

PassengerExitReason
-------------------

**Runtime/World/Passengers/Seats/PassengerSeat.cs**

Defines the allowed passenger exit reason choices used by this topic.

.. _evs-api-passengercontrollers--values-1:

Values
~~~~~~

-  ``Exit``
-  ``Ejected``
-  ``Disabled``
-  ``Destroyed``

.. _evs-api-passengercontrollers--passengermodule:

PassengerModule
---------------

**Runtime/World/Passengers/Core/PassengerModule.cs**

Configuration/implementation type for passenger module within seats, bodies and controller strategies.

**Inherits / implements:** :ref:`WorldModule <evs-api-modules--worldmodule>`, :ref:`IPassengerModule <evs-api-passengercontrollers--ipassengermodule>`.

.. _evs-api-passengercontrollers--methods-10:

Methods
~~~~~~~

+---------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                         | Role and behavior                                                                                                                                 | Arguments and result                                                                                                                                                                                                     |
+===================================================================================================+===================================================================================================================================================+==========================================================================================================================================================================================================================+
| ``public sealed override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Intentionally empty sealed module-pipeline entry point. Passenger-local work runs through ``StepPassenger``/``RenderPassenger`` under Passengers. | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+---------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void PreparePassenger(Passengers core, PassengerSeat seat)``                     | Prepares this passenger behavior for an occupied seat.                                                                                            | ``core`` — Owning audio or passenger core supplying shared context. ``seat`` — Seat context whose admission/occupancy rules remain authoritative.                                                                        |
+---------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ResetPassenger(Passengers core)``                                           | Resets this passenger behavior's state for the supplied seat.                                                                                     | ``core`` — Owning audio or passenger core supplying shared context.                                                                                                                                                      |
+---------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void RenderPassenger(Passengers core)``                                          | Advances render-time passenger presentation owned by this behavior/core.                                                                          | ``core`` — Owning audio or passenger core supplying shared context.                                                                                                                                                      |
+---------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void StepPassenger(Passengers core, float deltaTime)``                           | Advances passenger work in the supplied seat/core context.                                                                                        | ``core`` — Owning audio or passenger core supplying shared context. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop.                                                                                 |
+---------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-passengercontrollers--state-and-configuration-9:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------+---------------------------------------------------------------+
| Member                                                   | Meaning                                                       |
+==========================================================+===============================================================+
| ``public sealed override ExecutionPhase Phase { get; }`` | Cross-category execution barrier used by the module pipeline. |
+----------------------------------------------------------+---------------------------------------------------------------+

.. _evs-api-passengercontrollers--passengerseat:

PassengerSeat
-------------

**Runtime/World/Passengers/Seats/PassengerSeat.cs**

``Entered``, ``Exited``, ``ControllerChanged`` and custom ``ResetRequested``

**Inherits / implements:** ``MonoBehaviour``.

.. _evs-api-passengercontrollers--methods-11:

Methods
~~~~~~~

+-------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                                         | Role and behavior                                                                                                                                           | Arguments and result                                                                                                                                                                                                                                                                                                                    |
+===================================================================================================================+=============================================================================================================================================================+=========================================================================================================================================================================================================================================================================================================================================+
| ``public virtual bool Spawn()``                                                                                   | Creates/requests the configured passenger representation through the seat's spawn policy.                                                                   | **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated.                                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool Eject(Vector3 velocityChange)``                                                             | Requests whole-occupant release through the seat's controller/body lifecycle.                                                                               | ``velocityChange`` — World velocity change in m/s. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated.                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void StepPassenger(Passengers core, float deltaTime)``                                           | Advances passenger work in the supplied seat/core context.                                                                                                  | ``core`` — Owning audio or passenger core supplying shared context. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop.                                                                                                                                                                                                |
+-------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void RestoreDamageFeedback()``                                                                   | Restores the eligible seated limb supports released by damage feedback.                                                                                     | No arguments; no returned value.                                                                                                                                                                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SetPassengerController(PassengerControllerType type)``                                      | Requests a validated strategy handover for the seat; an incompatible/busy handover can be rejected.                                                         | ``type`` — Type, interpreted by this operation in the declared type. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated.                                                                                                                                      |
+-------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetCollisionExclusions(bool self, bool vehicle)``                                           | Sets seated self/vehicle collision exclusion policy and updates the occupied character.                                                                     | ``self`` — Whether the selected policy applies to contacts within the passenger skeleton. ``vehicle`` — Whether the policy applies to passenger-versus-vehicle contacts.                                                                                                                                                                |
+-------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetReleaseCollisions(bool self, bool vehicle)``                                             | Configures self/vehicle contacts permitted after release, either seat-wide or for one limb.                                                                 | ``self`` — Whether the selected policy applies to contacts within the passenger skeleton. ``vehicle`` — Whether the policy applies to passenger-versus-vehicle contacts.                                                                                                                                                                |
+-------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetReleaseCollisions(PassengerBodyPart part, bool self, bool vehicle)``                     | Configures self/vehicle contacts permitted after release, either seat-wide or for one limb.                                                                 | ``part`` — Selected body-part enum or part configuration, as declared. ``self`` — Whether the selected policy applies to contacts within the passenger skeleton. ``vehicle`` — Whether the policy applies to passenger-versus-vehicle contacts.                                                                                         |
+-------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void RefreshCollisionSettings()``                                                                | Reapplies the seat's collision policy to its current occupant.                                                                                              | No arguments; no returned value.                                                                                                                                                                                                                                                                                                        |
+-------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual PassengerBodyPartConfig GetBodyPart(PassengerBodyPart part)``                                    | Returns the seat configuration for a selected limb/body part.                                                                                               | ``part`` — Selected body-part enum or part configuration, as declared. **Returns:** Returned ``PassengerBodyPartConfig``; ownership remains as specified by the creating/lookup operation.                                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryReserve(PassengerAccess owner)``                                                         | Reserves a seat for an identified access/request owner without establishing occupancy.                                                                      | ``owner`` — Unity/application owner whose identity controls this relationship or resource. **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values.                                                                                                                                     |
+-------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ReleaseReservation(PassengerAccess owner)``                                                 | Releases a seat reservation belonging to the supplied reservation owner.                                                                                    | ``owner`` — Unity/application owner whose identity controls this relationship or resource.                                                                                                                                                                                                                                              |
+-------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryEnter(PassengerBody passenger)``                                                         | Attempts immediate validated occupancy with a body or supplied character representation; seat events are emitted only through successful occupancy changes. | ``passenger`` — Character body receiving motion/attachment. **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values.                                                                                                                                                                    |
+-------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryEnter(PassengerBody passenger, PassengerAccess reservation)``                            | Attempts immediate validated occupancy with a body or supplied character representation; seat events are emitted only through successful occupancy changes. | ``passenger`` — Character body receiving motion/attachment. ``reservation`` — Identity that owns the seat reservation; release must use that owner. **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values.                                                                            |
+-------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryExit(PassengerExitReason reason = PassengerExitReason.Exit, bool preservePose = false)`` | Releases current occupancy through its active strategy and exit reason; it does not run an animated access sequence.                                        | ``reason`` — Reason for occupancy release, used by controller/body cleanup policy. Default: ``PassengerExitReason.Exit``. ``preservePose`` — Whether this handover must retain the current character pose. Default: ``false``. **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values. |
+-------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-passengercontrollers--events-and-inspector-callbacks-1:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| Declaration                                                                                                | Trigger, payload and meaning                                                                                                                 |
+============================================================================================================+==============================================================================================================================================+
| ``public event Action<PassengerSeat, PassengerControllerType, PassengerControllerType> ControllerChanged`` | After a successful seat strategy handover. Payload: seat, previous controller type, new controller type; no extra entry/exit is synthesized. |
+------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerBody> Entered``                                                             | After accepted seat occupancy. Payload identifies the occupant; the Passengers-core delegate also includes the seat.                         |
+------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerBody> ResetRequested``                                                      | When Custom occupancy receives a reset request. Payload: ``PassengerBody``; application owns the actual custom-character reset.              |
+------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerBody, PassengerExitReason> Exited``                                         | After occupancy is released. Payload identifies occupant and ``PassengerExitReason``; the core delegate also includes the seat.              |
+------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-passengercontrollers--state-and-configuration-10:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                                 | Meaning                                                                                                                                                                                                    |
+========================================================================+============================================================================================================================================================================================================+
| ``public virtual PassengerControllerType Controller { get; }``         | Read-only/resolved controller for ``PassengerSeat``.                                                                                                                                                       |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual PassengerControllerType ActiveController { get; }``   | Read-only/resolved active controller for ``PassengerSeat``.                                                                                                                                                |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool PassengerReleasedByDamage { get; }``             | Read-only/resolved passenger released by damage for ``PassengerSeat``.                                                                                                                                     |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool HandsReleasedByDamage { get; }``                 | Read-only/resolved hands released by damage for ``PassengerSeat``.                                                                                                                                         |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool FeetReleasedByDamage { get; }``                  | Read-only/resolved feet released by damage for ``PassengerSeat``.                                                                                                                                          |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public PassengerType passengerType``                                 | Authored passenger type used by ``PassengerSeat``. Initial value: ``PassengerType.HumanoidPassenger``.                                                                                                     |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public string customTypeId``                                         | Application-defined type for Custom occupants; avoids changing the enum.                                                                                                                                   |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool spawnOnStart``                                           | Authored spawn on start used by ``PassengerSeat``. Initial value: ``true``.                                                                                                                                |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public PassengerBody bodyPrefab``                                    | Authored body prefab used by ``PassengerSeat``.                                                                                                                                                            |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public PassengerBody body``                                          | Optional pre-placed body. Leave empty to spawn the prefab.                                                                                                                                                 |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform spineAnchor``                                       | Pelvis / seated spine origin, facing forward, Y up.                                                                                                                                                        |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public string seatId``                                               | Authored seat id used by ``PassengerSeat``. Initial value: ``"passenger"``.                                                                                                                                |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform exitAnchor``                                        | Authored exit anchor used by ``PassengerSeat``.                                                                                                                                                            |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool parentWhileSeated``                                      | Authored parent while seated used by ``PassengerSeat``. Initial value: ``true``.                                                                                                                           |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool excludeVehicleCollisionsOnEnter``                        | Exclude contacts with the vehicle on entry and while held. Release options may restore them. Disable to keep vehicle contacts enabled, including after regrip and reseating.                               |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool excludeSelfCollisionsOnEnter``                           | Exclude self contacts on entry and while held. Release options may restore them. Disable to keep self contacts enabled, including after regrip and reseating. Native joint collision settings still apply. |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool enableVehicleCollidersOnRelease``                        | Enable vehicle contacts for every Free limb, and for the whole mannequin when ejected. Individual limb settings can also enable contacts independently.                                                    |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool enableSelfCollidersOnRelease``                           | Enable self contacts for every Free limb, and for the whole mannequin when ejected. Individual limb settings can also enable contacts independently. Neighboring skeletal bodies keep collisions disabled. |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public PassengerHandConfig leftHand``                                | Authored left hand used by ``PassengerSeat``. Initial value: ``new PassengerHandConfig()``.                                                                                                                |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public PassengerHandConfig rightHand``                               | Authored right hand used by ``PassengerSeat``. Initial value: ``new PassengerHandConfig()``.                                                                                                               |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public PassengerFootConfig leftFoot``                                | Authored left foot used by ``PassengerSeat``. Initial value: ``new PassengerFootConfig()``.                                                                                                                |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public PassengerFootConfig rightFoot``                               | Authored right foot used by ``PassengerSeat``. Initial value: ``new PassengerFootConfig()``.                                                                                                               |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public PassengerRestraints restraints``                              | Authored restraints used by ``PassengerSeat``. Initial value: ``new PassengerRestraints()``.                                                                                                               |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual PassengerBody Occupant { get; protected set; }``      | Body currently admitted to this seat, or ``null`` when empty.                                                                                                                                              |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual PassengerAccess Reservation { get; protected set; }`` | Current seat-access/request reservation identity; reservation does not itself mean occupancy.                                                                                                              |
+------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-passengercontrollers--passengertype:

PassengerType
-------------

**Runtime/World/Passengers/Seats/PassengerSeat.cs**

Defines the allowed passenger type choices used by this topic.

.. _evs-api-passengercontrollers--values-2:

Values
~~~~~~

-  ``HumanoidDriver``
-  ``HumanoidPassenger``
-  ``Custom``

.. _evs-api-passengercontrollers--passengers:

Passengers
----------

**Runtime/World/Passengers/Core/Passengers.cs**

Discovers owned handles and supplies input before seat work.

**Inherits / implements:** :ref:`WorldModule <evs-api-modules--worldmodule>`.

.. _evs-api-passengercontrollers--methods-12:

Methods
~~~~~~~

+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                                  | Role and behavior                                                                                         | Arguments and result                                                                                                                                                                                                                                                                                          |
+============================================================================================================+===========================================================================================================+===============================================================================================================================================================================================================================================================================================================+
| ``public virtual void RefreshPassengers()``                                                                | Rebuilds the owned seat, handle and passenger-behavior snapshot.                                          | No arguments; no returned value.                                                                                                                                                                                                                                                                              |
+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Configure(VehicleController vehicle)``                                              | Rebuilds the owned passenger seats, ordered handles and passenger-local behaviors.                        | ``vehicle`` — Vehicle context/owner receiving the operation.                                                                                                                                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)``                 | Supplies commands to handles in order, then advances passenger modules and seats from the owned snapshot. | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop.                                                                                      |
+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void PrepareOccupant(PassengerSeat seat)``                                                | Prepares a seat's occupant and its local handles/passenger behaviors.                                     | ``seat`` — Seat context whose admission/occupancy rules remain authoritative.                                                                                                                                                                                                                                 |
+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ResetOccupants()``                                                                   | Resets eligible owned seated/released occupants through their seat lifecycle.                             | No arguments; no returned value.                                                                                                                                                                                                                                                                              |
+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryEnter(PassengerBody body, PassengerSeat seat = null)``                            | Routes an entry request through an owned seat/passenger selection and that seat's validation.             | ``body`` — Character or rigidbody context, according to the declared type. ``seat`` — Seat context whose admission/occupancy rules remain authoritative. Default: ``null``. **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values.                          |
+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryExit(PassengerBody body, PassengerExitReason reason = PassengerExitReason.Exit)`` | Requests immediate exit or starts animated departure, depending on the declaring owner.                   | ``body`` — Character or rigidbody context, according to the declared type. ``reason`` — Reason for occupancy release, used by controller/body cleanup policy. Default: ``PassengerExitReason.Exit``. **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values. |
+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-passengercontrollers--events-and-inspector-callbacks-2:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Declaration                                                                       | Trigger, payload and meaning                                                                                                    |
+===================================================================================+=================================================================================================================================+
| ``public event Action<PassengerSeat, PassengerBody> Entered``                     | After accepted seat occupancy. Payload identifies the occupant; the Passengers-core delegate also includes the seat.            |
+-----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerSeat, PassengerBody, PassengerExitReason> Exited`` | After occupancy is released. Payload identifies occupant and ``PassengerExitReason``; the core delegate also includes the seat. |
+-----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-passengercontrollers--state-and-configuration-11:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------+----------------------------------------------------------------------+
| Member                                                               | Meaning                                                              |
+======================================================================+======================================================================+
| ``public bool spawnOnStart``                                         | Authored spawn on start used by Passengers. Initial value: ``true``. |
+----------------------------------------------------------------------+----------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }``                    | Cross-category execution barrier used by the module pipeline.        |
+----------------------------------------------------------------------+----------------------------------------------------------------------+
| ``public virtual VehicleController Vehicle { get; protected set; }`` | Read-only/resolved vehicle for Passengers.                           |
+----------------------------------------------------------------------+----------------------------------------------------------------------+
| ``public virtual PassengerSeat[] Seats { get; }``                    | Read-only/resolved seats for Passengers.                             |
+----------------------------------------------------------------------+----------------------------------------------------------------------+
| ``public virtual PassengerModule[] PassengerModules { get; }``       | Read-only/resolved passenger modules for Passengers.                 |
+----------------------------------------------------------------------+----------------------------------------------------------------------+

.. _evs-api-passengercontrollers--ragdollphysicspassengercontroller:

RagdollPhysicsPassengerController
---------------------------------

**Runtime/World/Passengers/Controllers/RagdollPhysicsPassengerController.cs**

Configuration/implementation type for ragdoll physics passenger controller within seats, bodies and controller strategies.

**Inherits / implements:** :ref:`PassengerController <evs-api-passengercontrollers--passengercontroller>`.

.. _evs-api-passengercontrollers--methods-13:

Methods
~~~~~~~

+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                           | Role and behavior                                                                                                   | Arguments and result                                                                                                                                                                                                                                                                   |
+=====================================================================================+=====================================================================================================================+========================================================================================================================================================================================================================================================================================+
| ``public override bool Attach(PassengerBody body, PassengerSeat seat)``             | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. | ``body`` — Character or rigidbody context, according to the declared type. ``seat`` — Seat context whose admission/occupancy rules remain authoritative. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(PassengerBody body, Passengers core, float deltaTime)`` | Calls the admitted body's ``StepSeated`` through the physical passenger path.                                       | ``body`` — Character or rigidbody context, according to the declared type. ``core`` — Owning audio or passenger core supplying shared context. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop.                                                                    |
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-passengercontrollers--state-and-configuration-12:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------+--------------------------------------------------------------------+
| Member                                                    | Meaning                                                            |
+===========================================================+====================================================================+
| ``public override PassengerControllerType Type { get; }`` | Read-only/resolved type for ``RagdollPhysicsPassengerController``. |
+-----------------------------------------------------------+--------------------------------------------------------------------+
