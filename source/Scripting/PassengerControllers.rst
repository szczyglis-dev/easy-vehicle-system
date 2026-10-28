.. _evs-scripting-passengercontrollers--passenger-occupancy-and-controllers:

Passenger occupancy and controllers
===================================

Passenger integration separates the fact that a seat is occupied from the way its character is controlled. ``PassengerSeat`` validates and owns occupancy. A controller strategy decides how an admitted body is attached, posed and advanced. The body adapter exposes the character that strategy operates on.

This separation lets an application retain its own character framework while using package seats, reservations and events. Choose the controller by ownership needs: native passenger physics, animation with limb overlays, simple attachment or application-owned behavior.

.. _evs-scripting-passengercontrollers--implementation-map:

Implementation map
------------------

+-------------------------+------------------------------------------------------------------+
| Class                   | Responsibility                                                   |
+=========================+==================================================================+
| ``Passengers``          | Discovers owned seats/handles and schedules passenger work.      |
+-------------------------+------------------------------------------------------------------+
| ``PassengerSeat``       | Owns admission, occupancy, reservations and controller handover. |
+-------------------------+------------------------------------------------------------------+
| ``PassengerController`` | Defines per-seat attachment, detachment and stepping behavior.   |
+-------------------------+------------------------------------------------------------------+
| ``PassengerBody``       | Base character adapter used by seats and controller strategies.  |
+-------------------------+------------------------------------------------------------------+
| ``CustomPassengerBody`` | Minimal body for application-owned Custom occupancy.             |
+-------------------------+------------------------------------------------------------------+
| ``HumanoidPassenger``   | Connects humanoid rig, pose and physical passenger behavior.     |
+-------------------------+------------------------------------------------------------------+

.. _evs-scripting-passengercontrollers--seat-versus-character:

Seat versus character
---------------------

The body adapter is the character-facing half of the integration. It answers whether the body can enter and provides attachment/detachment behavior used by a strategy. The seat-facing half owns who occupies the seat and whether another operation has reserved it. Neither half should silently choose the application's active player.

Use ``HumanoidPassenger`` when the package should operate its mapped humanoid. Use ``CustomPassengerBody`` when an external framework keeps character hierarchy, physics and pose. For a new body subclass, inspect both ``CanEnter`` overloads and the attachment/detachment contract; admission should reject an incompatible strategy before it partially changes the character.

``CustomPassengerBody`` accepts Custom, and automatic spawn-on-start skips Custom. Instantiate that body in the application and request entry explicitly. Choose the seat's controller strategy before requesting entry. Runtime ``SetPassengerController`` is a handover operation and can fail for a busy or incompatible body; check the return instead of assuming the requested enum is already active. ``ControllerChanged`` reports a successful strategy change with the previous and new choices.

Think of the seat as the authority and the controller as its implementation choice. A strategy should not independently announce a second entry or maintain a competing occupied flag. This is especially important when switching a seated character from animation to physics: ownership changes, but there is still one seat and one occupant.

``PassengerType`` describes the seat's role, such as driver or passenger. ``PassengerControllerType`` describes how its occupant is managed. A custom player character can occupy a driver seat without requiring the package to take over its hierarchy or animation; the application must then connect possession and driving input itself.

``PassengerSeat`` owns occupancy, reservation, controller strategy and lifecycle events. ``PassengerBody`` owns the character-specific attachment/detachment/pose hooks. A new controller strategy instance belongs to each seat. ``PassengerType`` classifies the role; ``PassengerControllerType`` selects behavior.

+--------------------+------------------------------------------------------------------------+
| Controller         | Ownership                                                              |
+====================+========================================================================+
| ``RagdollPhysics`` | Physical/IK character path                                             |
+--------------------+------------------------------------------------------------------------+
| Animator           | Application animation on an attached character                         |
+--------------------+------------------------------------------------------------------------+
| ``AnimatorIK``     | Animation with configured limb IK overlays                             |
+--------------------+------------------------------------------------------------------------+
| ``AttachOnly``     | Parenting/alignment without humanoid posing                            |
+--------------------+------------------------------------------------------------------------+
| Custom             | Occupancy only; application owns character hierarchy, pose and physics |
+--------------------+------------------------------------------------------------------------+

.. _evs-scripting-passengercontrollers--connect-a-custom-character:

Connect a custom character
--------------------------

The example selects the Custom strategy before requesting entry. Either operation can fail, so the result is returned to the caller. Do not update application possession merely because an ``Enter`` button was pressed; update it after successful admission or from the seat's occupancy event.

For Custom mode, decide explicitly what happens to the character's movement controller, camera, collisions and visible seated representation. The seat supplies occupancy coordination, not assumptions about those application systems. On exit, restore only state that the integration actually took ownership of.

Put ``CustomPassengerBody`` on your character, select Custom on the seat and assign the body below. Call ``Enter``/``Exit`` from the application. The boolean return is immediate occupancy admission, not an animated access completion.

**Example: ``CustomCharacterOccupancy.cs``**

.. raw:: html

   <!-- example: CustomCharacterOccupancy.cs -->

.. code-block:: csharp

   using UnityEngine;
   using EasyVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class CustomCharacterOccupancy : MonoBehaviour
       {
           public PassengerSeat seat;
           public CustomPassengerBody character;

           public bool Enter()
           {
               if (!seat || !character || !seat.SetPassengerController(PassengerControllerType.Custom))
                   return false;
               return seat.TryEnter(character);
           }

           public bool Exit() => seat && seat.TryExit();
       }
   }

Handle ``Entered``/``Exited``/``ResetRequested`` to move or animate your character framework. The package does not add a seated pose, ejection impulse or automatic respawn to a Custom occupant.

.. _evs-scripting-passengercontrollers--replace-the-seat-strategy-factory:

Replace the seat strategy factory
---------------------------------

Override ``CreatePassengerController`` when the existing enum choice should create an application-specific strategy. Returning the base factory result for other choices keeps them available. The created strategy instance belongs to that seat, so counters and captured state are not shared across unrelated seats.

The example calls ``base.Attach`` before recording success. A failed base attachment must not count as an admitted occupant. For a more extensive implementation, pair any acquired resources or subscriptions with ``Detach`` cleanup, and account for both ordinary exit and handover to another strategy.

Use a derived seat when a strategy needs application state while retaining occupancy validation/events. This example counts successful Custom attachments. Its controller extends the public Custom implementation, so it does not call package-internal body helpers.

**Example: ``ApplicationPassengerSeat.cs``**

.. raw:: html

   <!-- example: ApplicationPassengerSeat.cs -->

.. code-block:: csharp

   using UnityEngine;
   using EasyVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class ApplicationPassengerSeat : PassengerSeat
       {
           protected override PassengerController CreatePassengerController(PassengerControllerType type)
               => type == PassengerControllerType.Custom
                   ? new CountingCustomController()
                   : base.CreatePassengerController(type);
       }

       public class CountingCustomController : CustomPassengerController
       {
           public int Attachments { get; private set; }

           public override bool Attach(PassengerBody body, PassengerSeat seat)
           {
               if (!base.Attach(body, seat)) return false;
               Attachments++;
               return true;
           }
       }
   }

Strategies do not publish seat occupancy events themselves. A complete replacement owns its attachment/cleanup work, while the seat retains admission and event ordering. See :doc:`access </Scripting/PassengerAccess>` for asynchronous boarding and :doc:`physics </Scripting/PassengerPhysics>` for dynamic occupants.

.. _evs-scripting-passengercontrollers--complete-public-method-and-event-index:

Complete public method and event index
--------------------------------------

The lists below cover public methods and events for this topic and their package base contracts. Signatures include overloads. See :doc:`the detailed seats, bodies and controller strategies API </API/PassengerControllers>` for arguments, return semantics, state and configuration. An override replaces the matching inherited implementation; it is not an additional call to make.

.. _evs-scripting-passengercontrollers--animatorikpassengercontroller:

AnimatorIKPassengerController
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`AnimatorIKPassengerController <evs-api-passengercontrollers--animatorikpassengercontroller>` gives the full declared contract.

+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| Method                                                                  | Role                                                                                                                |
+=========================================================================+=====================================================================================================================+
| ``public override bool Attach(PassengerBody body, PassengerSeat seat)`` | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. |
+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+

.. _evs-scripting-passengercontrollers--animatorpassengercontroller:

AnimatorPassengerController
~~~~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`AnimatorPassengerController <evs-api-passengercontrollers--animatorpassengercontroller>` gives the full declared contract.

+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| Method                                                                  | Role                                                                                                                |
+=========================================================================+=====================================================================================================================+
| ``public override bool Attach(PassengerBody body, PassengerSeat seat)`` | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. |
+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+

.. _evs-scripting-passengercontrollers--attachonlypassengercontroller:

AttachOnlyPassengerController
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`AttachOnlyPassengerController <evs-api-passengercontrollers--attachonlypassengercontroller>` gives the full declared contract.

+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| Method                                                                  | Role                                                                                                                |
+=========================================================================+=====================================================================================================================+
| ``public override bool Attach(PassengerBody body, PassengerSeat seat)`` | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. |
+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+

.. _evs-scripting-passengercontrollers--custompassengerbody:

CustomPassengerBody
~~~~~~~~~~~~~~~~~~~

:ref:`CustomPassengerBody <evs-api-passengercontrollers--custompassengerbody>` gives the full declared contract.

+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| Method                                                                                    | Role                                                                                                                |
+===========================================================================================+=====================================================================================================================+
| ``public override bool CanEnter(PassengerSeat seat)``                                     | Checks body/seat compatibility before attachment; overloads distinguish seat and controller-strategy requirements.  |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public override bool CanEnter(PassengerSeat seat, PassengerControllerType controller)`` | Checks body/seat compatibility before attachment; overloads distinguish seat and controller-strategy requirements.  |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public override bool Attach(PassengerSeat seat)``                                       | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public override void Detach(PassengerExitReason reason)``                               | Ends the owned character or hitch relationship and releases the state/resources owned by that relationship.         |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+

.. _evs-scripting-passengercontrollers--custompassengercontroller:

CustomPassengerController
~~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`CustomPassengerController <evs-api-passengercontrollers--custompassengercontroller>` gives the full declared contract.

+----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| Method                                                                                             | Role                                                                                                                |
+====================================================================================================+=====================================================================================================================+
| ``public override bool Attach(PassengerBody body, PassengerSeat seat)``                            | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. |
+----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public override void Detach(PassengerBody body, PassengerExitReason reason, bool preservePose)`` | Ends the owned character or hitch relationship and releases the state/resources owned by that relationship.         |
+----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+

.. _evs-scripting-passengercontrollers--humanoidpassenger:

HumanoidPassenger
~~~~~~~~~~~~~~~~~

:ref:`HumanoidPassenger <evs-api-passengercontrollers--humanoidpassenger>` gives the full declared contract.

+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| Method                                                                                    | Role                                                                                                                |
+===========================================================================================+=====================================================================================================================+
| ``public virtual void PrepareRagdollCollisions()``                                        | Prepares the character's skeletal collision exclusions and collision relays.                                        |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public override bool Attach(PassengerSeat seat)``                                       | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SolveSeatedIK()``                                                   | Applies the seated character's configured limb IK targets.                                                          |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public override void StepSeated(Passengers core, float deltaTime)``                     | Advances this body's seated behavior through its selected character path.                                           |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public override void ResetSeatedPose()``                                                | Restores the character's seated pose/support through the selected physical/animation path.                          |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public override void DetachForTransition()``                                            | Releases seated ownership for an animated character handover while preserving the required transition pose.         |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public override void Detach(PassengerExitReason reason)``                               | Ends the owned character or hitch relationship and releases the state/resources owned by that relationship.         |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ActivateRagdoll()``                                                 | Hands the character to free skeletal physics, releasing seated pose ownership.                                      |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public override bool CanEnter(PassengerSeat seat)``                                     | Checks body/seat compatibility before attachment; overloads distinguish seat and controller-strategy requirements.  |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public override bool CanEnter(PassengerSeat seat, PassengerControllerType controller)`` | Checks body/seat compatibility before attachment; overloads distinguish seat and controller-strategy requirements.  |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public virtual void RestoreAccessReferencePose()``                                      | Restores the character pose retained for an access-motion handover.                                                 |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public virtual void PreviewAccessPose(PassengerSeat seat)``                             | Applies an access reference pose for character/seat authoring or transition preparation.                            |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public override void AddVelocity(Vector3 velocityChange)``                              | Adds the supplied velocity change to the character bodies used by this body implementation.                         |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ReadAnatomicalJointSettings()``                                     | Reads saved native joint configuration into the character's runtime anatomical references.                          |
+-------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+

+------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| Event / callback                                                 | Role                                                                                                                             |
+==================================================================+==================================================================================================================================+
| ``public event System.Action<HumanoidPassenger> BeforeSeatedIK`` | Immediately before seated IK work. Payload: ``HumanoidPassenger``; custom pose inputs must respect the selected character owner. |
+------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``public event System.Action<HumanoidPassenger> AfterSeatedIK``  | Immediately after seated IK work. Payload: ``HumanoidPassenger``.                                                                |
+------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+

.. _evs-scripting-passengercontrollers--imodule:

IModule
~~~~~~~

:ref:`IModule <evs-api-modules--imodule>` gives the full declared contract.

+----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Method                                                                     | Role                                                                                                                        |
+============================================================================+=============================================================================================================================+
| ``void Configure(VehicleController vehicle)``                              | Repeatable setup contract supplied with the owning ``VehicleController``.                                                   |
+----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``void Step(VehicleController vehicle, Command command, float deltaTime)`` | Contract for one owner-supplied fixed tick; implement only the module responsibility and use the supplied Command/timestep. |
+----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+

.. _evs-scripting-passengercontrollers--module:

Module
~~~~~~

:ref:`Module <evs-api-modules--module>` gives the full declared contract.

+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Method                                                                                    | Role                                                                                                                                   |
+===========================================================================================+========================================================================================================================================+
| ``public virtual void Configure(VehicleController vehicle)``                              | Empty base setup hook. Derived components may cache references/apply persistent settings; the controller owns lifecycle notifications. |
+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Step(VehicleController vehicle, Command command, float deltaTime)`` | Empty base extension point. The controller schedules derived work and emits lifecycle notifications around it.                         |
+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetEnabled(bool value)``                                            | Changes module enabled state and publishes an actual requested-flag change.                                                            |
+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SupportsProfile(DriveProfile profile)``                             | Checks movement-family compatibility; this is independent of the Unity enabled flag.                                                   |
+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+

+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| Event / callback                                                          | Role                                                                                                              |
+===========================================================================+===================================================================================================================+
| ``public event System.Action<bool> EnabledChanged``                       | After ``SetEnabled`` changes the module flag. Payload: requested enabled bool; no event for an unchanged request. |
+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public event System.Action<VehicleController> Configured``              | After controller-driven module configuration. Payload: the owning ``VehicleController``.                          |
+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public event System.Action<VehicleController, Command, float> Stepped`` | After this registered module has stepped. Payload: vehicle, sampled Command, timestep in seconds.                 |
+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+

.. _evs-scripting-passengercontrollers--motorcyclerider:

MotorcycleRider
~~~~~~~~~~~~~~~

:ref:`MotorcycleRider <evs-api-passengercontrollers--motorcyclerider>` gives the full declared contract.

+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| Method                                                        | Role                                                                          |
+===============================================================+===============================================================================+
| ``public override void ResetPassenger(Passengers core)``      | Resets this passenger behavior's state for the supplied seat.                 |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+
| ``public override bool AppliesTo(VehicleController vehicle)`` | Checks whether this passenger behavior should run for the supplied seat/role. |
+---------------------------------------------------------------+-------------------------------------------------------------------------------+

.. _evs-scripting-passengercontrollers--passengerbehaviour:

PassengerBehaviour
~~~~~~~~~~~~~~~~~~

:ref:`PassengerBehaviour <evs-api-passengercontrollers--passengerbehaviour>` gives the full declared contract.

+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Method                                                                          | Role                                                                          |
+=================================================================================+===============================================================================+
| ``public sealed override void StepPassenger(Passengers core, float deltaTime)`` | Advances passenger work in the supplied seat/core context.                    |
+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| ``public virtual bool AppliesTo(VehicleController vehicle)``                    | Checks whether this passenger behavior should run for the supplied seat/role. |
+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

.. _evs-scripting-passengercontrollers--passengerbody:

PassengerBody
~~~~~~~~~~~~~

:ref:`PassengerBody <evs-api-passengercontrollers--passengerbody>` gives the full declared contract.

+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| Method                                                                                   | Role                                                                                                                |
+==========================================================================================+=====================================================================================================================+
| ``public abstract bool Attach(PassengerSeat seat)``                                      | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. |
+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public abstract void Detach(PassengerExitReason reason)``                              | Ends the owned character or hitch relationship and releases the state/resources owned by that relationship.         |
+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public virtual void DetachForTransition()``                                            | Releases seated ownership for an animated character handover while preserving the required transition pose.         |
+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public virtual void StepSeated(Passengers core, float deltaTime)``                     | Advances this body's seated behavior through its selected character path.                                           |
+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ResetSeatedPose()``                                                | Restores the character's seated pose/support through the selected physical/animation path.                          |
+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool CanEnter(PassengerSeat seat)``                                     | Checks body/seat compatibility before attachment; overloads distinguish seat and controller-strategy requirements.  |
+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool CanEnter(PassengerSeat seat, PassengerControllerType controller)`` | Checks body/seat compatibility before attachment; overloads distinguish seat and controller-strategy requirements.  |
+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public virtual void AddVelocity(Vector3 velocityChange)``                              | Adds the supplied velocity change to the character bodies used by this body implementation.                         |
+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+

.. _evs-scripting-passengercontrollers--passengercontroller:

PassengerController
~~~~~~~~~~~~~~~~~~~

:ref:`PassengerController <evs-api-passengercontrollers--passengercontroller>` gives the full declared contract.

+---------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| Method                                                                                            | Role                                                                                                                           |
+===================================================================================================+================================================================================================================================+
| ``public abstract bool Attach(PassengerBody body, PassengerSeat seat)``                           | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication.            |
+---------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Detach(PassengerBody body, PassengerExitReason reason, bool preservePose)`` | Ends the owned character or hitch relationship and releases the state/resources owned by that relationship.                    |
+---------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Step(PassengerBody body, Passengers core, float deltaTime)``                | Empty base passenger strategy step; derived strategies decide which body work they own.                                        |
+---------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public static PassengerController Create(PassengerControllerType type)``                        | Creates the built-in strategy for a ``PassengerControllerType``; seat factory overrides can substitute application strategies. |
+---------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+

.. _evs-scripting-passengercontrollers--passengermodule:

PassengerModule
~~~~~~~~~~~~~~~

:ref:`PassengerModule <evs-api-passengercontrollers--passengermodule>` gives the full declared contract.

+---------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Method                                                                                            | Role                                                                                                                                              |
+===================================================================================================+===================================================================================================================================================+
| ``public sealed override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Intentionally empty sealed module-pipeline entry point. Passenger-local work runs through ``StepPassenger``/``RenderPassenger`` under Passengers. |
+---------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void PreparePassenger(Passengers core, PassengerSeat seat)``                     | Prepares this passenger behavior for an occupied seat.                                                                                            |
+---------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ResetPassenger(Passengers core)``                                           | Resets this passenger behavior's state for the supplied seat.                                                                                     |
+---------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void RenderPassenger(Passengers core)``                                          | Advances render-time passenger presentation owned by this behavior/core.                                                                          |
+---------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void StepPassenger(Passengers core, float deltaTime)``                           | Advances passenger work in the supplied seat/core context.                                                                                        |
+---------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-scripting-passengercontrollers--passengerseat:

PassengerSeat
~~~~~~~~~~~~~

:ref:`PassengerSeat <evs-api-passengercontrollers--passengerseat>` gives the full declared contract.

+-------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Method                                                                                                            | Role                                                                                                                                                        |
+===================================================================================================================+=============================================================================================================================================================+
| ``public virtual bool Spawn()``                                                                                   | Creates/requests the configured passenger representation through the seat's spawn policy.                                                                   |
+-------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool Eject(Vector3 velocityChange)``                                                             | Requests whole-occupant release through the seat's controller/body lifecycle.                                                                               |
+-------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void StepPassenger(Passengers core, float deltaTime)``                                           | Advances passenger work in the supplied seat/core context.                                                                                                  |
+-------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void RestoreDamageFeedback()``                                                                   | Restores the eligible seated limb supports released by damage feedback.                                                                                     |
+-------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SetPassengerController(PassengerControllerType type)``                                      | Requests a validated strategy handover for the seat; an incompatible/busy handover can be rejected.                                                         |
+-------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetCollisionExclusions(bool self, bool vehicle)``                                           | Sets seated self/vehicle collision exclusion policy and updates the occupied character.                                                                     |
+-------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetReleaseCollisions(bool self, bool vehicle)``                                             | Configures self/vehicle contacts permitted after release, either seat-wide or for one limb.                                                                 |
+-------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetReleaseCollisions(PassengerBodyPart part, bool self, bool vehicle)``                     | Configures self/vehicle contacts permitted after release, either seat-wide or for one limb.                                                                 |
+-------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void RefreshCollisionSettings()``                                                                | Reapplies the seat's collision policy to its current occupant.                                                                                              |
+-------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual PassengerBodyPartConfig GetBodyPart(PassengerBodyPart part)``                                    | Returns the seat configuration for a selected limb/body part.                                                                                               |
+-------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryReserve(PassengerAccess owner)``                                                         | Reserves a seat for an identified access/request owner without establishing occupancy.                                                                      |
+-------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ReleaseReservation(PassengerAccess owner)``                                                 | Releases a seat reservation belonging to the supplied reservation owner.                                                                                    |
+-------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryEnter(PassengerBody passenger)``                                                         | Attempts immediate validated occupancy with a body or supplied character representation; seat events are emitted only through successful occupancy changes. |
+-------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryEnter(PassengerBody passenger, PassengerAccess reservation)``                            | Attempts immediate validated occupancy with a body or supplied character representation; seat events are emitted only through successful occupancy changes. |
+-------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryExit(PassengerExitReason reason = PassengerExitReason.Exit, bool preservePose = false)`` | Releases current occupancy through its active strategy and exit reason; it does not run an animated access sequence.                                        |
+-------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

+------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| Event / callback                                                                                           | Role                                                                                                                                         |
+============================================================================================================+==============================================================================================================================================+
| ``public event Action<PassengerSeat, PassengerControllerType, PassengerControllerType> ControllerChanged`` | After a successful seat strategy handover. Payload: seat, previous controller type, new controller type; no extra entry/exit is synthesized. |
+------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerBody> Entered``                                                             | After accepted seat occupancy. Payload identifies the occupant; the Passengers-core delegate also includes the seat.                         |
+------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerBody> ResetRequested``                                                      | When Custom occupancy receives a reset request. Payload: ``PassengerBody``; application owns the actual custom-character reset.              |
+------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerBody, PassengerExitReason> Exited``                                         | After occupancy is released. Payload identifies occupant and ``PassengerExitReason``; the core delegate also includes the seat.              |
+------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-scripting-passengercontrollers--passengers:

Passengers
~~~~~~~~~~

:ref:`Passengers <evs-api-passengercontrollers--passengers>` gives the full declared contract.

+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Method                                                                                                     | Role                                                                                                      |
+============================================================================================================+===========================================================================================================+
| ``public virtual void RefreshPassengers()``                                                                | Rebuilds the owned seat, handle and passenger-behavior snapshot.                                          |
+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public override void Configure(VehicleController vehicle)``                                              | Rebuilds the owned passenger seats, ordered handles and passenger-local behaviors.                        |
+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)``                 | Supplies commands to handles in order, then advances passenger modules and seats from the owned snapshot. |
+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public virtual void PrepareOccupant(PassengerSeat seat)``                                                | Prepares a seat's occupant and its local handles/passenger behaviors.                                     |
+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public virtual void ResetOccupants()``                                                                   | Resets eligible owned seated/released occupants through their seat lifecycle.                             |
+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryEnter(PassengerBody body, PassengerSeat seat = null)``                            | Routes an entry request through an owned seat/passenger selection and that seat's validation.             |
+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryExit(PassengerBody body, PassengerExitReason reason = PassengerExitReason.Exit)`` | Requests immediate exit or starts animated departure, depending on the declaring owner.                   |
+------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+

+-----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Event / callback                                                                  | Role                                                                                                                            |
+===================================================================================+=================================================================================================================================+
| ``public event Action<PassengerSeat, PassengerBody> Entered``                     | After accepted seat occupancy. Payload identifies the occupant; the Passengers-core delegate also includes the seat.            |
+-----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerSeat, PassengerBody, PassengerExitReason> Exited`` | After occupancy is released. Payload identifies occupant and ``PassengerExitReason``; the core delegate also includes the seat. |
+-----------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+

.. _evs-scripting-passengercontrollers--ragdollphysicspassengercontroller:

RagdollPhysicsPassengerController
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:ref:`RagdollPhysicsPassengerController <evs-api-passengercontrollers--ragdollphysicspassengercontroller>` gives the full declared contract.

+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| Method                                                                              | Role                                                                                                                |
+=====================================================================================+=====================================================================================================================+
| ``public override bool Attach(PassengerBody body, PassengerSeat seat)``             | Attaches a body using this controller/body strategy; successful attachment is separate from seat event publication. |
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(PassengerBody body, Passengers core, float deltaTime)`` | Calls the admitted body's ``StepSeated`` through the physical passenger path.                                       |
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
