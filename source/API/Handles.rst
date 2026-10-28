.. _evs-api-handles--limb-handles-and-transfers-api:

Limb handles and transfers API
==============================

Read :doc:`the system explanation </Scripting/Handles>` for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from ``MonoBehaviour``, ``Object`` or ``ScriptableObject`` are documented by Unity.

.. _evs-api-handles--types:

Types
-----

-  :ref:`AnchorHandle <evs-api-handles--anchorhandle>`
-  :ref:`HandTransferHandle <evs-api-handles--handtransferhandle>`
-  :ref:`HandleInput <evs-api-handles--handleinput>`
-  :ref:`HandleMotion <evs-api-handles--handlemotion>`
-  :ref:`HandleSelector <evs-api-handles--handleselector>`
-  :ref:`IHandle <evs-api-handles--ihandle>`
-  :ref:`JoystickHandle <evs-api-handles--joystickhandle>`
-  :ref:`MotorcycleHandle <evs-api-handles--motorcyclehandle>`
-  :ref:`PedalFootHandle <evs-api-handles--pedalfoothandle>`
-  :ref:`PedalHandle <evs-api-handles--pedalhandle>`
-  :ref:`SteeringWheelHandle <evs-api-handles--steeringwheelhandle>`
-  :ref:`SteeringWheelHandle.RimSample <evs-api-handles--steeringwheelhandlerimsample>`
-  :ref:`SteeringWheelHandle.SteeringGripMode <evs-api-handles--steeringwheelhandlesteeringgripmode>`
-  :ref:`SwitchHandle <evs-api-handles--switchhandle>`
-  :ref:`SwitchPosition <evs-api-handles--switchposition>`
-  :ref:`ThrottleHandle <evs-api-handles--throttlehandle>`
-  :ref:`VehicleHandle <evs-api-handles--vehiclehandle>`
-  :ref:`YokeHandle <evs-api-handles--yokehandle>`

.. _evs-api-handles--anchorhandle:

AnchorHandle
------------

**Runtime/World/Passengers/IK/Handle/AnchorHandle.cs**

Exposes authored hand/foot anchors without control animation.

**Inherits / implements:** :ref:`VehicleHandle <evs-api-handles--vehiclehandle>`.

.. _evs-api-handles--methods:

Methods
~~~~~~~

+-----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                       | Role and behavior                                                                                                  | Arguments and result                                                                                                                                                            |
+=================================================================+====================================================================================================================+=================================================================================================================================================================================+
| ``public override Transform GetAnchor(PassengerBodyPart part)`` | Returns the assigned anchor directly. The seat is responsible for assigning this handle to the intended body part. | ``part`` — Selected body-part enum or part configuration, as declared. **Returns:** Stable contact ``Transform``, or ``null`` under the availability conditions described here. |
+-----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-handles--state-and-configuration:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------+---------------------------------------------------------------------------------------------------------+
| Member                      | Meaning                                                                                                 |
+=============================+=========================================================================================================+
| ``public Transform anchor`` | Stable authored contact returned to the seat. Use palm or ankle frame appropriate to the assigned limb. |
+-----------------------------+---------------------------------------------------------------------------------------------------------+

.. _evs-api-handles--handtransferhandle:

HandTransferHandle
------------------

**Runtime/World/Passengers/IK/Handle/HandTransferHandle.cs**

Temporarily moves a hand to another control and restores its binding.

**Inherits / implements:** :ref:`VehicleHandle <evs-api-handles--vehiclehandle>`.

.. _evs-api-handles--methods-1:

Methods
~~~~~~~

+---------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                                                       | Role and behavior                                                                                                                                                                                 | Arguments and result                                                                                                                                                                                                                                                                                                                                                                                                 |
+=================================================================================================================================+===================================================================================================================================================================================================+======================================================================================================================================================================================================================================================================================================================================================================================================================+
| ``public virtual bool Begin(PassengerSeat passengerSeat, PassengerBodyPart hand, VehicleHandle next, Action onArrival = null)`` | Starts release → travel → destination bind/callback → dwell → release → return. Rejects busy/disabled helpers, missing occupancy, invalid hand/source/destination or uncontrolled source binding. | ``passengerSeat`` — Seat whose occupied hand is temporarily controlled. ``hand`` — ``LeftHand`` or ``RightHand`` for a hand operation. ``next`` — Destination handle; must supply a valid contact for the selected limb. ``onArrival`` — Optional callback invoked once at the temporary destination before Arrived. Default: ``null``. **Returns:** ``true`` if the operation starts; ``false`` if admission fails. |
+---------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override Transform GetAnchor(PassengerBodyPart bodyPart)``                                                             | Returns this transfer's persistent temporary target. ``Begin``/active ownership determines which hand uses it.                                                                                    | ``bodyPart`` — Selected passenger body-part enum. **Returns:** Stable contact ``Transform``, or ``null`` under the availability conditions described here.                                                                                                                                                                                                                                                           |
+---------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override float HandContact(bool left)``                                                                                | Returns contact participation for the selected hand; guidance can remain enabled while surface contact is released.                                                                               | ``left`` — ``true`` selects the left hand; ``false`` selects the right. **Returns:** Normalized fraction in 0–1.                                                                                                                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool HandSteering(bool left)``                                                                                | Reports whether the selected hand participates in steering support.                                                                                                                               | ``left`` — ``true`` selects the left hand; ``false`` selects the right. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated.                                                                                                                                                                                                                |
+---------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void SetInput(Command command, float deltaTime)``                                                             | Advances the active release/travel/dwell/return phase. Cancels if occupancy, destination or binding ownership is no longer valid.                                                                 | ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop.                                                                                                                                                                                                                                                          |
+---------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Cancel()``                                                                                                | Cancels an active transfer, clears its arrival callback and restores the saved handle/hold only while this transfer still owns the binding.                                                       | No arguments; no returned value.                                                                                                                                                                                                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-handles--events-and-inspector-callbacks:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------+------------------------------------------------------------------------------------------------------------+
| Declaration                       | Trigger, payload and meaning                                                                               |
+===================================+============================================================================================================+
| ``public event Action Started``   | After temporary hand ownership begins. No payload.                                                         |
+-----------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public event Action Arrived``   | After the hand reaches and binds to the temporary destination, following the arrival callback. No payload. |
+-----------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public event Action Completed`` | After the out-and-back hand transfer completes and its binding is restored. No payload.                    |
+-----------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public event Action Cancelled`` | After an active hand transfer is cancelled and owned bindings are cleaned up. No payload.                  |
+-----------------------------------+------------------------------------------------------------------------------------------------------------+

.. _evs-api-handles--state-and-configuration-1:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------+--------------------------------------------------------------------------------------+
| Member                                  | Meaning                                                                              |
+=========================================+======================================================================================+
| ``public float travelDuration``         | Seconds for each outward/return travel leg, excluding release and destination dwell. |
+-----------------------------------------+--------------------------------------------------------------------------------------+
| ``public float releaseDuration``        | Time to release palm contact before target travel, in seconds.                       |
+-----------------------------------------+--------------------------------------------------------------------------------------+
| ``public float dwellDuration``          | Time held at the temporary destination before return begins, in seconds.             |
+-----------------------------------------+--------------------------------------------------------------------------------------+
| ``public virtual bool IsBusy { get; }`` | True during any active release, travel, dwell or return phase.                       |
+-----------------------------------------+--------------------------------------------------------------------------------------+

.. _evs-api-handles--handleinput:

HandleInput
-----------

**Runtime/World/Passengers/IK/Handle/HandleSelector.cs**

Defines the allowed handle input choices used by this topic.

.. _evs-api-handles--values:

Values
~~~~~~

-  ``Brake``
-  ``Throttle``
-  ``Clutch``
-  ``Steering``
-  ``Pitch``
-  ``Roll``
-  ``Yaw``
-  ``Lift``
-  ``Strafe``

.. _evs-api-handles--handlemotion:

HandleMotion
------------

**Runtime/World/Passengers/IK/Handle/HandleMotion.cs**

Serializable geometry mapper from normalized travel or an explicit offset to an anchored transform.

.. _evs-api-handles--methods-2:

Methods
~~~~~~~

+-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| Signature                                       | Role and behavior                                                                                                                                                    | Arguments and result                                                     |
+=================================================+======================================================================================================================================================================+==========================================================================+
| ``public virtual void SetValue(float value)``   | Clamps a fraction to 0–1, maps it between minimum and maximum, then applies ``SetOffset``. Rotation uses degrees; translation uses local distance.                   | ``value`` — Normalized travel in 0–1, mapped to minimum/maximum.         |
+-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+
| ``public virtual void SetOffset(float offset)`` | Resets ``movingPart`` to the independent anchor and applies rotation in degrees or translation in local units. Invalid/nonfinite/self-descendant frames are ignored. | ``offset`` — Offset, interpreted by this operation in the declared type. |
+-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------+

.. _evs-api-handles--state-and-configuration-2:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| Member                                    | Meaning                                                                                                             |
+===========================================+=====================================================================================================================+
| ``public Transform movingPart``           | ``Transform`` whose pose this mapper owns; keep imported-mesh offsets on its child.                                 |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public Transform anchor``               | Independent neutral motion frame. Self/descendant anchors are rejected.                                             |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public AircraftControlMotionMode mode`` | Chooses rotation (degrees) or translation (local distance) for minimum/maximum/offset.                              |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public Vector3 localAxis``              | Motion axis in the anchor frame; normalized before application, with a right-axis fallback for a degenerate vector. |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public float minimum``                  | Offset at normalized value zero: degrees in rotation mode, local distance in translation mode.                      |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public float maximum``                  | Offset at normalized value one; values may be signed/reversed to match model direction.                             |
+-------------------------------------------+---------------------------------------------------------------------------------------------------------------------+

.. _evs-api-handles--handleselector:

HandleSelector
--------------

**Runtime/World/Passengers/IK/Handle/HandleSelector.cs**

Chooses between two handles while preserving one seat assignment.

**Inherits / implements:** :ref:`VehicleHandle <evs-api-handles--vehiclehandle>`.

.. _evs-api-handles--methods-3:

Methods
~~~~~~~

+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                           | Role and behavior                                                                                    | Arguments and result                                                                                                                                                            |
+=====================================================================+======================================================================================================+=================================================================================================================================================================================+
| ``public virtual void SelectActive(bool value)``                    | Selects the active or idle handle and takes manual selection ownership.                              | ``value`` — Requested bool state for this operation.                                                                                                                            |
+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void FollowInput()``                               | Releases a manual selection/value override and resumes configured input following.                   | No arguments; no returned value.                                                                                                                                                |
+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void SetInput(Command command, float deltaTime)`` | Chooses active/default handle from its configured Command mapping unless a manual selection owns it. | ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop.                     |
+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override Transform GetAnchor(PassengerBodyPart part)``     | Forwards contact lookup to the currently selected eligible handle.                                   | ``part`` — Selected body-part enum or part configuration, as declared. **Returns:** Stable contact ``Transform``, or ``null`` under the availability conditions described here. |
+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-handles--events-and-inspector-callbacks-1:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| Declaration                                                    | Trigger, payload and meaning                                                                                      |
+================================================================+===================================================================================================================+
| ``public event System.Action<VehicleHandle> SelectionChanged`` | When the selected destination handle changes. Payload: ``VehicleHandle``, possibly ``null``; this is not arrival. |
+----------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+

.. _evs-api-handles--state-and-configuration-3:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------+----------------------------------------------------------------------------------+
| Member                                                   | Meaning                                                                          |
+==========================================================+==================================================================================+
| ``public VehicleHandle defaultHandle``                   | Authored default handle used by ``HandleSelector``.                              |
+----------------------------------------------------------+----------------------------------------------------------------------------------+
| ``public VehicleHandle activeHandle``                    | Authored active handle used by ``HandleSelector``.                               |
+----------------------------------------------------------+----------------------------------------------------------------------------------+
| ``public HandleInput input``                             | Authored input used by ``HandleSelector``. Initial value: ``HandleInput.Brake``. |
+----------------------------------------------------------+----------------------------------------------------------------------------------+
| ``public float threshold``                               | Authored threshold used by ``HandleSelector``. Initial value: ``.05f``.          |
+----------------------------------------------------------+----------------------------------------------------------------------------------+
| ``public virtual VehicleHandle SelectedHandle { get; }`` | Current active/default contact provider selected by ``HandleSelector``.          |
+----------------------------------------------------------+----------------------------------------------------------------------------------+

.. _evs-api-handles--ihandle:

IHandle
-------

**Runtime/World/Passengers/IK/Handle/VehicleHandle.cs**

Common contact, preparation, binding and input contract.

.. _evs-api-handles--methods-4:

Methods
~~~~~~~

+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                       | Role and behavior                                                                                                   | Arguments and result                                                                                                                                                                                              |
+=================================================================================+=====================================================================================================================+===================================================================================================================================================================================================================+
| ``void Prepare()``                                                              | Prepares reusable contact geometry or handle initialization without entering a seat.                                | No arguments; no returned value.                                                                                                                                                                                  |
+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``Transform GetAnchor(PassengerBodyPart part)``                                 | Returns the stable contact transform for a supported body part, or ``null`` when unavailable/unsupported.           | ``part`` — Selected body-part enum or part configuration, as declared. **Returns:** Stable contact ``Transform``, or ``null`` under the availability conditions described here.                                   |
+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``void BindBodyPart(PassengerBodyPart part, HumanoidIK ik, Animator animator)`` | Prepares the selected limb for this handle, including supported adaptive finger binding and palm frames.            | ``part`` — Selected body-part enum or part configuration, as declared. ``ik`` — Mapped humanoid limb/frame helper for this character. ``animator`` — Character Animator providing mapped bones/animation context. |
+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``void SetInput(Command command, float deltaTime)``                             | Consumes the owner-supplied command/timestep as part of the passenger handle pass.                                  | ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop.                                                       |
+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``bool HandDriven(bool left)``                                                  | Reports whether the selected hand should receive physical target guidance.                                          | ``left`` — ``true`` selects the left hand; ``false`` selects the right. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated.             |
+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``bool HandSteering(bool left)``                                                | Reports whether the selected hand participates in steering support.                                                 | ``left`` — ``true`` selects the left hand; ``false`` selects the right. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated.             |
+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``float HandContact(bool left)``                                                | Returns contact participation for the selected hand; guidance can remain enabled while surface contact is released. | ``left`` — ``true`` selects the left hand; ``false`` selects the right. **Returns:** Normalized fraction in 0–1.                                                                                                  |
+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-handles--joystickhandle:

JoystickHandle
--------------

**Runtime/World/Passengers/IK/Handle/JoystickHandle.cs**

Combines authored steering contacts with pitch/roll motion.

**Inherits / implements:** :ref:`SteeringWheelHandle <evs-api-handles--steeringwheelhandle>`.

.. _evs-api-handles--methods-5:

Methods
~~~~~~~

+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| Signature                                                    | Role and behavior                                                                                                                  | Arguments and result                                                                                                   |
+==============================================================+====================================================================================================================================+========================================================================================================================+
| ``public virtual void SetControls(float pitch, float roll)`` | Maps pitch -1..1 to ``HandleMotion`` travel and applies roll around ``localRollAxis`` between ``minimumRoll`` and ``maximumRoll``. | ``pitch`` — Normalized pitch input, or audio pitch multiplier in an audio operation. ``roll`` — Normalized roll input. |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-handles--state-and-configuration-4:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------+------------------------------------------------------------------------------------------+
| Member                           | Meaning                                                                                  |
+==================================+==========================================================================================+
| ``public HandleMotion motion``   | Authored motion used by ``JoystickHandle``. Initial value: ``new HandleMotion()``.       |
+----------------------------------+------------------------------------------------------------------------------------------+
| ``public Vector3 localRollAxis`` | Authored local roll axis used by ``JoystickHandle``. Initial value: ``Vector3.forward``. |
+----------------------------------+------------------------------------------------------------------------------------------+
| ``public float minimumRoll``     | Authored minimum roll used by ``JoystickHandle``. Initial value: ``-6``.                 |
+----------------------------------+------------------------------------------------------------------------------------------+
| ``public float maximumRoll``     | Authored maximum roll used by ``JoystickHandle``. Initial value: ``6``.                  |
+----------------------------------+------------------------------------------------------------------------------------------+

.. _evs-api-handles--motorcyclehandle:

MotorcycleHandle
----------------

**Runtime/World/Passengers/IK/Handle/MotorcycleHandle.cs**

Supplies fixed left/right contacts with prepared finger poses.

**Inherits / implements:** :ref:`VehicleHandle <evs-api-handles--vehiclehandle>`.

.. _evs-api-handles--methods-6:

Methods
~~~~~~~

+-------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                       | Role and behavior                                                                                        | Arguments and result                                                                                                                                                                                              |
+=================================================================================================+==========================================================================================================+===================================================================================================================================================================================================================+
| ``public override void BindBodyPart(PassengerBodyPart part, HumanoidIK ik, Animator animator)`` | Prepares the selected limb for this handle, including supported adaptive finger binding and palm frames. | ``part`` — Selected body-part enum or part configuration, as declared. ``ik`` — Mapped humanoid limb/frame helper for this character. ``animator`` — Character Animator providing mapped bones/animation context. |
+-------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override Transform GetAnchor(PassengerBodyPart part)``                                 | Returns the prepared left/right grip target for the requested hand.                                      | ``part`` — Selected body-part enum or part configuration, as declared. **Returns:** Stable contact ``Transform``, or ``null`` under the availability conditions described here.                                   |
+-------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-handles--state-and-configuration-5:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Member                                          | Meaning                                                                                                              |
+=================================================+======================================================================================================================+
| ``public float gripRadius``                     | Tube radius in local metres. Grip centres stay fixed; the editor updates the palm contacts and prepares the fingers. |
+-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| ``public float gripLength``                     | Authored grip length used by ``MotorcycleHandle``. Initial value: ``.11f``.                                          |
+-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| ``public Transform leftGrip``                   | Centre of the left grip. Local X runs along the tube; local Y points from the palm towards the tube centre.          |
+-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| ``public Transform rightGrip``                  | Authored right grip used by ``MotorcycleHandle``.                                                                    |
+-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| ``public override float GripDiameter { get; }`` | Resolved cylindrical grip diameter in metres, full width rather than radius.                                         |
+-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool IsPrepared { get; }``     | Whether fixed motorcycle hand/finger preparation is available.                                                       |
+-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+

.. _evs-api-handles--pedalfoothandle:

PedalFootHandle
---------------

**Runtime/Interior/Controls/PedalFootHandle.cs**

Transfers one stable ankle target between pedals.

**Inherits / implements:** :ref:`VehicleHandle <evs-api-handles--vehiclehandle>`.

.. _evs-api-handles--methods-7:

Methods
~~~~~~~

+-----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                     | Role and behavior                                                                                                                            | Arguments and result                                                                                                                                                            |
+===============================================================================================+==============================================================================================================================================+=================================================================================================================================================================================+
| ``public override void Prepare()``                                                            | Prepares reusable contact geometry or handle initialization without entering a seat.                                                         | No arguments; no returned value.                                                                                                                                                |
+-----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Tick(float deltaTime)``                                                 | Advances the declaring presentation/state machine by elapsed seconds; avoid a second call when its built-in owner already ticks it.          | ``deltaTime`` — Elapsed time in seconds supplied by the owning loop.                                                                                                            |
+-----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override Transform GetAnchor(PassengerBodyPart part)``                               | Returns its stable ankle target only for the configured foot with an enabled same-vehicle destination; otherwise returns ``null``.           | ``part`` — Selected body-part enum or part configuration, as declared. **Returns:** Stable contact ``Transform``, or ``null`` under the availability conditions described here. |
+-----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void SetInput(Command command, float deltaTime)``                           | Selects brake/accelerator from resolved service braking with hysteresis while automatic selection owns the foot; it does not advance travel. | ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop.                     |
+-----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SelectPedal(VehicleHandle pedal)``                                      | Selects a specific pedal handle, including ``null`` to release a usable foot destination.                                                    | ``pedal`` — Selected pedal handle; ``null`` releases a usable foot destination.                                                                                                 |
+-----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SelectBrake(bool value)``                                               | Selects the brake or accelerator pedal and takes manual foot-selection ownership.                                                            | ``value`` — Requested bool state for this operation.                                                                                                                            |
+-----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void FollowInput()``                                                         | Releases a manual selection/value override and resumes configured input following.                                                           | No arguments; no returned value.                                                                                                                                                |
+-----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetPedals(VehicleHandle acceleratorHandle, VehicleHandle brakeHandle)`` | Replaces the accelerator/brake handle references used by foot selection.                                                                     | ``acceleratorHandle`` — Handle supplying the accelerator ankle target. ``brakeHandle`` — Handle supplying the brake ankle target.                                               |
+-----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SnapToSelected()``                                                      | Finishes the foot target's current transfer immediately at its selected pedal.                                                               | No arguments; no returned value.                                                                                                                                                |
+-----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-handles--events-and-inspector-callbacks-2:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| Declaration                                             | Trigger, payload and meaning                                                                                      |
+=========================================================+===================================================================================================================+
| ``public event Action<VehicleHandle> SelectionChanged`` | When the selected destination handle changes. Payload: ``VehicleHandle``, possibly ``null``; this is not arrival. |
+---------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+

.. _evs-api-handles--state-and-configuration-6:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| Member                                                                 | Meaning                                                                                          |
+========================================================================+==================================================================================================+
| ``public VehicleHandle accelerator``                                   | Handle providing the accelerator ankle destination.                                              |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public VehicleHandle brake``                                         | Handle providing the brake ankle destination.                                                    |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public PassengerBodyPart foot``                                      | ``LeftFoot`` or ``RightFoot`` served by this helper; other limb queries return no usable target. |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public Transform target``                                            | Stable ankle target owned by this helper, independent of both moving pedals.                     |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public float brakeThreshold``                                        | Resolved service-brake level that starts automatic brake selection.                              |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public float brakeReleaseThreshold``                                 | Lower brake threshold used to leave brake selection, providing hysteresis.                       |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public float transferDuration``                                      | Seconds for the stable ankle target to travel to a newly selected pedal.                         |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public float liftHeight``                                            | Extra local-up height in metres at the transfer arc's middle.                                    |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public virtual VehicleHandle SelectedPedal { get; protected set; }`` | Current ankle destination handle; it can be ``null`` for an intentionally released target.       |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public virtual bool FollowsInput { get; }``                          | Whether ordinary input mapping owns this control instead of an application override.             |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public virtual bool IsTransferring { get; }``                        | Whether the pedal-foot target has not yet finished its configured travel.                        |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+

.. _evs-api-handles--pedalhandle:

PedalHandle
-----------

**Runtime/Interior/Controls/PedalHandle.cs**

Animates pedal travel and exposes an ankle contact.

**Inherits / implements:** :ref:`VehicleHandle <evs-api-handles--vehiclehandle>`.

.. _evs-api-handles--methods-8:

Methods
~~~~~~~

+---------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                           | Role and behavior                                                                                                                                             | Arguments and result                                                                                                                                                            |
+=====================================================================+===============================================================================================================================================================+=================================================================================================================================================================================+
| ``public override void Prepare()``                                  | Prepares reusable contact geometry or handle initialization without entering a seat.                                                                          | No arguments; no returned value.                                                                                                                                                |
+---------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ResetMotion()``                               | Clears presentation requests and restores the released/default motion state.                                                                                  | No arguments; no returned value.                                                                                                                                                |
+---------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Tick(float deltaTime)``                       | Advances the declaring presentation/state machine by elapsed seconds; avoid a second call when its built-in owner already ticks it.                           | ``deltaTime`` — Elapsed time in seconds supplied by the owning loop.                                                                                                            |
+---------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override Transform GetAnchor(PassengerBodyPart part)``     | Returns ``contactAnchor`` directly; author this as the ankle target beneath the moving pedal.                                                                 | ``part`` — Selected body-part enum or part configuration, as declared. **Returns:** Stable contact ``Transform``, or ``null`` under the availability conditions described here. |
+---------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void SetInput(Command command, float deltaTime)`` | Updates ``TargetValue`` only while ``FollowsInput``. Reads resolved pedals or the configured Command channel; render-rate ``Tick`` advances displayed travel. | ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop.                     |
+---------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetValue(float value)``                       | Takes external demand ownership, sanitizes/clamps value to 0–1 and requests smoothed pedal travel. ``FollowInput`` releases the override.                     | ``value`` — Normalized value clamped to 0–1 by this control.                                                                                                                    |
+---------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetImmediate(float value)``                   | Takes external value ownership, clamps normalized travel and applies it immediately; ``onValueChanged`` reports an actual displayed-value change.             | ``value`` — Normalized value clamped to 0–1 by this control.                                                                                                                    |
+---------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void FollowInput()``                               | Releases a manual selection/value override and resumes configured input following.                                                                            | No arguments; no returned value.                                                                                                                                                |
+---------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-handles--events-and-inspector-callbacks-3:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Declaration                                 | Trigger, payload and meaning                                                                                                                                    |
+=============================================+=================================================================================================================================================================+
| ``public UnityEvent<float> onValueChanged`` | After this control's value changes. Payload: the event's value type; ``PedalHandle`` reports displayed travel, ``SwitchHandle`` reports a changed bool request. |
+---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-handles--state-and-configuration-7:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Member                                                       | Meaning                                                                                                                   |
+==============================================================+===========================================================================================================================+
| ``public AnchoredRotation motion``                           | Authored motion used by ``PedalHandle``. Initial value: ``new AnchoredRotation()``.                                       |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public HandleInput input``                                 | Command channel selected when resolving this pedal's demand.                                                              |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public bool useResolvedPedals``                            | For throttle/brake, use the vehicle's resolved propulsion and service brake rather than the shared forward/reverse input. |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public bool absoluteInput``                                | Use absolute input for signed propulsion/reverse commands.                                                                |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public float pressDuration``                               | Seconds for full released-to-pressed travel; smaller demands stop proportionally earlier.                                 |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public float releaseDuration``                             | Seconds for full pressed-to-released travel.                                                                              |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public float releasedAngle``                               | Pedal angle in degrees at displayed value zero.                                                                           |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public float pressedAngle``                                | Pedal angle in degrees at displayed value one.                                                                            |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public Transform contactAnchor``                           | Ankle target for a seated foot, parented to the moving pedal.                                                             |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float Value { get; protected set; }``       | Current displayed pedal travel in 0–1; it can lag ``TargetValue`` while motion is smoothed.                               |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float TargetValue { get; protected set; }`` | Requested pedal demand in 0–1; displayed Value approaches it with press/release travel.                                   |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool FollowsInput { get; protected set; }`` | Whether ordinary input mapping owns this control instead of an application override.                                      |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-handles--steeringwheelhandle:

SteeringWheelHandle
-------------------

**Runtime/World/Passengers/IK/Handle/SteeringWheelHandle.cs**

Describes steering contacts, surface geometry and hand participation.

**Inherits / implements:** :ref:`VehicleHandle <evs-api-handles--vehiclehandle>`.

.. _evs-api-handles--methods-9:

Methods
~~~~~~~

+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                                            | Role and behavior                                                                                                                     | Arguments and result                                                                                                                                                                                                                                              |
+======================================================================================================================+=======================================================================================================================================+===================================================================================================================================================================================================================================================================+
| ``public override void Prepare()``                                                                                   | Prepares reusable contact geometry or handle initialization without entering a seat.                                                  | No arguments; no returned value.                                                                                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void BindBodyPart(PassengerBodyPart part, HumanoidIK ik, Animator animator)``                      | Prepares the selected limb for this handle, including supported adaptive finger binding and palm frames.                              | ``part`` — Selected body-part enum or part configuration, as declared. ``ik`` — Mapped humanoid limb/frame helper for this character. ``animator`` — Character Animator providing mapped bones/animation context.                                                 |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual Vector3 Centerline(float angle)``                                                                   | Evaluates the steering-rim centerline at an angular coordinate in the wheel's local frame.                                            | ``angle`` — Angular coordinate in degrees for this geometry operation. **Returns:** Returned Vector3; ownership remains as specified by the creating/lookup operation.                                                                                            |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float RadiusAt(float angle)``                                                                       | Returns the steering-rim tube radius at the supplied angular coordinate.                                                              | ``angle`` — Angular coordinate in degrees for this geometry operation. **Returns:** Surface distance/radius in the unit and frame described by this operation.                                                                                                    |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float SignedDistanceLocal(Vector3 point)``                                                          | Evaluates a wheel-local point against the steering tube and returns scaled surface distance.                                          | ``point`` — Geometry point in the declared coordinate frame. **Returns:** Surface distance/radius in the unit and frame described by this operation.                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetGripMode(SteeringGripMode mode)``                                                           | Chooses both hands, left only, right only or released steering-grip permission.                                                       | ``mode`` — Mode, interpreted by this operation in the declared type.                                                                                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool AllowsHand(bool left)``                                                                        | Checks enabled state and the configured left/right grip-mode permission.                                                              | ``left`` — ``true`` selects the left hand; ``false`` selects the right. **Returns:** ``true`` when the described condition holds; ``false`` otherwise.                                                                                                            |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override Transform GetAnchor(PassengerBodyPart part)``                                                      | Returns ``leftTarget``/``rightTarget`` only for an allowed corresponding hand; unsupported limbs or disallowed hands return ``null``. | ``part`` — Selected body-part enum or part configuration, as declared. **Returns:** Stable contact ``Transform``, or ``null`` under the availability conditions described here.                                                                                   |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool HandDriven(bool left)``                                                                       | Reports whether the selected hand should receive physical target guidance.                                                            | ``left`` — ``true`` selects the left hand; ``false`` selects the right. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated.                                                             |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool HandSteering(bool left)``                                                                     | Reports whether the selected hand participates in steering support.                                                                   | ``left`` — ``true`` selects the left hand; ``false`` selects the right. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated.                                                             |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetHandControl(bool left, bool driven, bool steering)``                                        | Selects physical-guidance and steering-support participation independently for one hand.                                              | ``left`` — ``true`` selects the left hand; ``false`` selects the right. ``driven`` — Whether physical hand guidance is enabled. ``steering`` — Normalized steering input, or bool steering participation when declared bool.                                      |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool HandPoseFrozen(bool left)``                                                                    | Reports whether the selected hand retains its captured pose rather than continuously refitting.                                       | ``left`` — ``true`` selects the left hand; ``false`` selects the right. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated.                                                             |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool HandPinch(bool left)``                                                                         | Reports whether the selected hand uses the pinch gesture.                                                                             | ``left`` — ``true`` selects the left hand; ``false`` selects the right. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated.                                                             |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetHandPoseFrozen(bool left, bool value)``                                                     | Chooses captured-pose reuse for the selected hand.                                                                                    | ``left`` — ``true`` selects the left hand; ``false`` selects the right. ``value`` — Requested bool state for this operation.                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetHandPinch(bool left, bool value)``                                                          | Enables/disables the selected hand's pinch gesture.                                                                                   | ``left`` — ``true`` selects the left hand; ``false`` selects the right. ``value`` — Requested bool state for this operation.                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float HandFingerExtension(bool left)``                                                              | Returns the selected hand's normalized finger-extension gesture.                                                                      | ``left`` — ``true`` selects the left hand; ``false`` selects the right. **Returns:** Normalized fraction in 0–1.                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetHandFingerExtension(bool left, float value)``                                               | Sets normalized finger extension for one steering hand.                                                                               | ``left`` — ``true`` selects the left hand; ``false`` selects the right. ``value`` — Normalized value clamped to 0–1 by this control.                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float PalmPressure(bool left)``                                                                     | Returns normalized palm-pressure presentation for the selected hand.                                                                  | ``left`` — ``true`` selects the left hand; ``false`` selects the right. **Returns:** Normalized fraction in 0–1.                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetPalmPressure(bool left, float value)``                                                      | Sets normalized palm pressure and updates a bound adaptive hand when applicable.                                                      | ``left`` — ``true`` selects the left hand; ``false`` selects the right. ``value`` — Normalized value clamped to 0–1 by this control.                                                                                                                              |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float HandClosure(bool left)``                                                                      | Returns normalized finger-closure state for the selected steering hand.                                                               | ``left`` — ``true`` selects the left hand; ``false`` selects the right. **Returns:** Normalized fraction in 0–1.                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override float HandContact(bool left)``                                                                     | Returns contact participation for the selected hand; guidance can remain enabled while surface contact is released.                   | ``left`` — ``true`` selects the left hand; ``false`` selects the right. **Returns:** Normalized fraction in 0–1.                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool HandPreclosing(bool left)``                                                                    | Reports whether fingers are closing before palm contact settles.                                                                      | ``left`` — ``true`` selects the left hand; ``false`` selects the right. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated.                                                             |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetHandContact(bool left, float closure, float contact, bool preclosing = false)``             | Sets normalized closure/contact and the preclosing flag for one steering hand.                                                        | ``left`` — ``true`` selects the left hand; ``false`` selects the right. ``closure`` — Normalized finger closure. ``contact`` — Normalized physical contact participation. ``preclosing`` — Whether fingers close before palm contact settles. Default: ``false``. |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float SignedDistance(Vector3 worldPoint)``                                                          | Returns signed world-space distance to the steering tube surface; positive means outside.                                             | ``worldPoint`` — World-space target/sample point. **Returns:** Surface distance/radius in the unit and frame described by this operation.                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void GetContactFrame(float angle, out Vector3 point, out Quaternion rotation)``                     | Returns a world-space contact point/orientation at an angular coordinate around the steering rim.                                     | ``angle`` — Angular coordinate in degrees for this geometry operation. ``point`` — Geometry point in the declared coordinate frame. ``rotation`` — Requested/output orientation in the declared frame.                                                            |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void GetPalmContactFrame(float angle, float pressure, out Vector3 point, out Quaternion rotation)`` | Returns a world palm-contact frame including the requested pressure adjustment.                                                       | ``angle`` — Angular coordinate in degrees for this geometry operation. ``pressure`` — Normalized palm pressure. ``point`` — Geometry point in the declared coordinate frame. ``rotation`` — Requested/output orientation in the declared frame.                   |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void UpdateTargets()``                                                                              | Updates steering palm targets from current geometry without changing seat occupancy.                                                  | No arguments; no returned value.                                                                                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-handles--state-and-configuration-8:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                   | Meaning                                                                                                                            |
+==========================================================+====================================================================================================================================+
| ``public SteeringGripMode gripMode``                     | Authored grip mode used by ``SteeringWheelHandle``. Initial value: ``SteeringGripMode.BothHands``.                                 |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool allowHandRegrip``                          | Allow automatic hand repositioning and column support while steering. Disable for fixed handlebar grips.                           |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool varyGripWithSteering``                     | Vary palm pressure, finger closure and relaxed finger poses while steering. Disable to keep a full wrapped grip on attached hands. |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public SteeringHandRegripSettings regrip``             | Authored regrip used by ``SteeringWheelHandle``. Initial value: ``new SteeringHandRegripSettings()``.                              |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector3 center``                                | Authored center used by ``SteeringWheelHandle``.                                                                                   |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public float rimRadius``                               | Authored rim radius used by ``SteeringWheelHandle``. Initial value: ``.1744f``.                                                    |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public float tubeRadius``                              | Radius of the rim tube, not its diameter.                                                                                          |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public float tubeDepthRadius``                         | Fore/aft tube radius. Zero uses a circular section equal to Tube Radius.                                                           |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public RimSample[] customRim``                         | Optional closed centerline for flat-bottomed or irregular wheels. At least three samples.                                          |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public float leftAngle``                               | Authored left angle used by ``SteeringWheelHandle``. Initial value: ``180``.                                                       |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public float rightAngle``                              | Authored right angle used by ``SteeringWheelHandle``.                                                                              |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool reverseApproach``                          | The wheel-local direction away from the driver is +Z. Reverse for a backwards pivot.                                               |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool authoredTargets``                          | Keep manually authored palm anchors instead of regenerating wheel-rim contacts. Use for control sticks.                            |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool stickGrip``                                | Fit fingers and thumb around Grip Diameter at the authored palm anchors.                                                           |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform leftTarget``                          | Authored left target used by ``SteeringWheelHandle``.                                                                              |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform rightTarget``                         | Authored right target used by ``SteeringWheelHandle``.                                                                             |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool showFingerContacts``                       | Authored show finger contacts used by ``SteeringWheelHandle``. Initial value: ``true``.                                            |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public float wrappedPalmInset``                        | Move a fully wrapped palm inward towards the rim, in metres.                                                                       |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public float wrappedPalmTilt``                         | Tilt a fully wrapped palm towards the wheel centre, in degrees.                                                                    |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool overridePressurePalm``                     | Authored override pressure palm used by ``SteeringWheelHandle``.                                                                   |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector3 pressurePalmOffset``                    | Pressure contact-frame offset in metres. Y slides along the palm; Z moves towards/away from the rim.                               |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector3 pressurePalmRotation``                  | Extra pressure palm rotation in contact-frame degrees.                                                                             |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector3 pressureFingerAngles``                  | Pressure finger flexion in degrees: base, middle and tip. Does not change thumb posing.                                            |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual Vector3 PressureFingerAngles { get; }`` | Resolved base/middle/tip pressure flexion angles in degrees.                                                                       |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool HasCustomRim { get; }``            | True when at least three custom rim centerline samples are configured.                                                             |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual int GeometrySignature { get; }``        | Hash of geometry inputs used to detect a changed steering surface.                                                                 |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float WorldScale { get; }``             | Absolute steering-control world X scale used by the uniform-scale geometry model.                                                  |
+----------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-handles--steeringwheelhandlerimsample:

SteeringWheelHandle.RimSample
-----------------------------

**Runtime/World/Passengers/IK/Handle/SteeringWheelHandle.cs**

Value data for rim sample; its fields are listed below.

.. _evs-api-handles--state-and-configuration-9:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------+--------------------------------------------------------------------+
| Member                      | Meaning                                                            |
+=============================+====================================================================+
| ``public Vector3 position`` | World-space position used by the current contact or motion sample. |
+-----------------------------+--------------------------------------------------------------------+
| ``public float radius``     | Authored radius used by ``RimSample``.                             |
+-----------------------------+--------------------------------------------------------------------+

.. _evs-api-handles--steeringwheelhandlesteeringgripmode:

SteeringWheelHandle.SteeringGripMode
------------------------------------

**Runtime/World/Passengers/IK/Handle/SteeringWheelHandle.cs**

Defines the allowed steering grip mode choices used by this topic.

.. _evs-api-handles--values-1:

Values
~~~~~~

-  ``BothHands``
-  ``LeftHand``
-  ``RightHand``
-  ``Released``

.. _evs-api-handles--switchhandle:

SwitchHandle
------------

**Runtime/World/Passengers/IK/Handle/SwitchHandle.cs**

Owns requested detents, travel and request/arrival events.

**Inherits / implements:** :ref:`VehicleHandle <evs-api-handles--vehiclehandle>`.

.. _evs-api-handles--methods-10:

Methods
~~~~~~~

+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                             | Role and behavior                                                                                                                                                                                     | Arguments and result                                                                                                                                                            |
+=======================================================================+=======================================================================================================================================================================================================+=================================================================================================================================================================================+
| ``public override void Prepare()``                                    | Prepares reusable contact geometry or handle initialization without entering a seat.                                                                                                                  | No arguments; no returned value.                                                                                                                                                |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override Transform GetAnchor(PassengerBodyPart part)``       | Returns ``handAnchor`` directly; it does not filter the requested body-part enum.                                                                                                                     | ``part`` — Selected body-part enum or part configuration, as declared. **Returns:** Stable contact ``Transform``, or ``null`` under the availability conditions described here. |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetValue(bool value)``                          | Requests Positive for ``true`` and Neutral for ``false``. Changed requests emit position/bool notifications and start travel.                                                                         | ``value`` — Requested bool state for this operation.                                                                                                                            |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Toggle()``                                      | Requests the opposite current body/switch/wiper/profile/gear state through the declaring component.                                                                                                   | No arguments; no returned value.                                                                                                                                                |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetPosition(SwitchPosition position)``          | Requests a detent. Invalid enum values throw ``ArgumentOutOfRangeException``; Negative in binary mode throws ``InvalidOperationException``. A changed request starts travel and emits request events. | ``position`` — Requested point or switch detent; see its declared type and owning operation.                                                                                    |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetImmediate(bool value)``                      | Silently synchronizes Positive/Neutral, displayed value and motion without request or settlement callbacks.                                                                                           | ``value`` — Requested bool state for this operation.                                                                                                                            |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetPositionImmediate(SwitchPosition position)`` | Silently synchronizes a switch detent and displayed pose without issuing control events.                                                                                                              | ``position`` — Requested point or switch detent; see its declared type and owning operation.                                                                                    |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void SetInput(Command command, float deltaTime)``   | Advances detent travel by elapsed seconds, applies motion, then emits Switched and ``PositionReached`` on settlement.                                                                                 | ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop.                     |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-handles--events-and-inspector-callbacks-4:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Declaration                                             | Trigger, payload and meaning                                                                                                                                                                             |
+=========================================================+==========================================================================================================================================================================================================+
| ``public event Action<bool> ValueChanged``              | When the requested binary ``IsOn`` state changes. Payload: bool. Moving between negative and positive detents keeps ``IsOn`` ``true`` and does not emit this event. Immediate synchronization is silent. |
+---------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<bool> Switched``                  | When switch presentation settles. Payload: bool ``IsOn``; negative and positive three-position states both count as on.                                                                                  |
+---------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<SwitchPosition> PositionChanged`` | When requested switch detent changes. Payload: ``SwitchPosition``; distinguish all three positions with this event.                                                                                      |
+---------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<SwitchPosition> PositionReached`` | When switch travel settles at its detent. Payload: ``SwitchPosition``.                                                                                                                                   |
+---------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent<bool> onValueChanged``              | After this control's value changes. Payload: the event's value type; ``PedalHandle`` reports displayed travel, ``SwitchHandle`` reports a changed bool request.                                          |
+---------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent<SwitchPosition> onPositionChanged`` | After a changed switch detent request. Payload: ``SwitchPosition``; silent immediate synchronization does not invoke it.                                                                                 |
+---------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-handles--state-and-configuration-10:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| Member                                                             | Meaning                                                                                       |
+====================================================================+===============================================================================================+
| ``public Transform handAnchor``                                    | Palm contact belonging to the moving switch geometry.                                         |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``public HandleMotion motion``                                     | Authored motion used by ``SwitchHandle``. Initial value: ``new HandleMotion { minimum = 25``. |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``public bool initiallyOn``                                        | Initial binary request used by first preparation.                                             |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``public bool threePosition``                                      | Enables Negative/Neutral/Positive detents; without it Negative requests throw.                |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``public SwitchPosition initialPosition``                          | Initial three-position detent used by first preparation.                                      |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``public float neutralOffset``                                     | Middle-detent geometry offset in degrees or local distance, according to motion.mode.         |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``public float transitionDuration``                                | Seconds for visible detent travel; settlement events follow that travel.                      |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``public virtual bool IsOn { get; }``                              | For a switch, Position is not Neutral; negative and positive both count as on.                |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``public virtual SwitchPosition Position { get; protected set; }`` | Requested switch detent, distinct from displayed travel and arrival.                          |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``public virtual float Value { get; protected set; }``             | Current normalized displayed detent travel; Position is the requested discrete state.         |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``public virtual bool IsMoving { get; }``                          | Whether displayed switch travel differs from its requested detent target.                     |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+

.. _evs-api-handles--switchposition:

SwitchPosition
--------------

**Runtime/World/Passengers/IK/Handle/SwitchHandle.cs**

Defines the allowed switch position choices used by this topic.

.. _evs-api-handles--values-2:

Values
~~~~~~

-  ``Negative = -1``
-  ``Neutral = 0``
-  ``Positive = 1``

.. _evs-api-handles--throttlehandle:

ThrottleHandle
--------------

**Runtime/World/Passengers/IK/Handle/ThrottleHandle.cs**

Maps normalized travel to an anchored lever pose.

**Inherits / implements:** :ref:`VehicleHandle <evs-api-handles--vehiclehandle>`.

.. _evs-api-handles--methods-11:

Methods
~~~~~~~

+-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                       | Role and behavior                                                                                                   | Arguments and result                                                                                                                                                            |
+=================================================================+=====================================================================================================================+=================================================================================================================================================================================+
| ``public override Transform GetAnchor(PassengerBodyPart part)`` | Returns ``handAnchor`` directly; it does not filter the requested body-part enum.                                   | ``part`` — Selected body-part enum or part configuration, as declared. **Returns:** Stable contact ``Transform``, or ``null`` under the availability conditions described here. |
+-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetValue(float value)``                   | Passes normalized lever travel to its ``HandleMotion`` geometry mapper; it does not set mechanical engine throttle. | ``value`` — Normalized value clamped to 0–1 by this control.                                                                                                                    |
+-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-handles--state-and-configuration-11:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------+------------------------------------------------------------------------------------+
| Member                          | Meaning                                                                            |
+=================================+====================================================================================+
| ``public Transform handAnchor`` | Authored hand anchor used by ``ThrottleHandle``.                                   |
+---------------------------------+------------------------------------------------------------------------------------+
| ``public HandleMotion motion``  | Authored motion used by ``ThrottleHandle``. Initial value: ``new HandleMotion()``. |
+---------------------------------+------------------------------------------------------------------------------------+

.. _evs-api-handles--vehiclehandle:

VehicleHandle
-------------

**Runtime/World/Passengers/IK/Handle/VehicleHandle.cs**

Common contact, preparation, binding and input contract.

**Inherits / implements:** ``MonoBehaviour``, :ref:`IHandle <evs-api-handles--ihandle>`.

.. _evs-api-handles--methods-12:

Methods
~~~~~~~

+------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                      | Role and behavior                                                                                                               | Arguments and result                                                                                                                                                                                              |
+================================================================================================+=================================================================================================================================+===================================================================================================================================================================================================================+
| ``public virtual void Prepare()``                                                              | Prepares reusable contact geometry or handle initialization without entering a seat.                                            | No arguments; no returned value.                                                                                                                                                                                  |
+------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ResetHandle()``                                                          | Resets local handle state through the common extensible handle contract.                                                        | No arguments; no returned value.                                                                                                                                                                                  |
+------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void BindBodyPart(PassengerBodyPart part, HumanoidIK ik, Animator animator)`` | Prepares the selected limb for this handle, including supported adaptive finger binding and palm frames.                        | ``part`` — Selected body-part enum or part configuration, as declared. ``ik`` — Mapped humanoid limb/frame helper for this character. ``animator`` — Character Animator providing mapped bones/animation context. |
+------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public abstract Transform GetAnchor(PassengerBodyPart part)``                                | Returns the stable contact transform for a supported body part, or ``null`` when unavailable/unsupported.                       | ``part`` — Selected body-part enum or part configuration, as declared. **Returns:** Stable contact ``Transform``, or ``null`` under the availability conditions described here.                                   |
+------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetInput(Command command, float deltaTime)``                             | Receives the sampled command/timestep from Passengers. Base implementation is empty; override for input-driven handle behavior. | ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop.                                                       |
+------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool HandDriven(bool left)``                                                  | Reports whether the selected hand should receive physical target guidance.                                                      | ``left`` — ``true`` selects the left hand; ``false`` selects the right. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated.             |
+------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool HandSteering(bool left)``                                                | Reports whether the selected hand participates in steering support.                                                             | ``left`` — ``true`` selects the left hand; ``false`` selects the right. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated.             |
+------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float HandContact(bool left)``                                                | Returns contact participation for the selected hand; guidance can remain enabled while surface contact is released.             | ``left`` — ``true`` selects the left hand; ``false`` selects the right. **Returns:** Normalized fraction in 0–1.                                                                                                  |
+------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-handles--state-and-configuration-12:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                         | Meaning                                                                                                                                       |
+================================================+===============================================================================================================================================+
| ``public bool adaptiveGrip``                   | Fit fingers around this handle. Applies to hands only; foot anchors are unaffected.                                                           |
+------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float gripDiameter``                  | Grip diameter in metres in the palm anchor's local space. The cylinder runs along anchor X, with its centre towards +Y from the palm contact. |
+------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float palmTravel``                    | Capture tolerance before a palm is attached with locked translation. Angular tracking remains compliant.                                      |
+------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float palmCaptureSpeed``              | Speed at which a newly closed contact takes up remaining slack, in metres per second.                                                         |
+------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float positionSpring``                | Authored position spring used by ``VehicleHandle``. Initial value: ``2000``.                                                                  |
+------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float positionDamper``                | Authored position damper used by ``VehicleHandle``. Initial value: ``60``.                                                                    |
+------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumPalmForce``              | Authored maximum palm force used by ``VehicleHandle``. Initial value: ``90``.                                                                 |
+------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float angularSpring``                 | Authored angular spring used by ``VehicleHandle``. Initial value: ``500``.                                                                    |
+------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float angularDamper``                 | Authored angular damper used by ``VehicleHandle``. Initial value: ``20``.                                                                     |
+------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumTorque``                 | Authored maximum torque used by ``VehicleHandle``. Initial value: ``25``.                                                                     |
+------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float armSpring``                     | Active ragdoll shoulder and elbow support towards the geometric arm pose.                                                                     |
+------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float armDamper``                     | Authored arm damper used by ``VehicleHandle``. Initial value: ``12``.                                                                         |
+------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float armMaximumTorque``              | Authored arm maximum torque used by ``VehicleHandle``. Initial value: ``25``.                                                                 |
+------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float GripDiameter { get; }`` | Resolved cylindrical grip diameter in metres, full width rather than radius.                                                                  |
+------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual int InputOrder { get; }``     | Input-consumption priority among handles; higher values consume after dependencies.                                                           |
+------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-handles--yokehandle:

YokeHandle
----------

**Runtime/World/Passengers/IK/Handle/YokeHandle.cs**

Describes steering contacts, surface geometry and hand participation.

**Inherits / implements:** :ref:`SteeringWheelHandle <evs-api-handles--steeringwheelhandle>`.
