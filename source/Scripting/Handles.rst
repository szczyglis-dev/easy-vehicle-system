.. _evs-scripting-handles--limb-handles-and-transfers:

Limb handles and transfers
==========================

A handle is the passenger-facing description of a control or support target. It tells the passenger system where a hand or foot should make contact. Some handles also move that contact in response to input, such as a pedal travelling under the driver's foot. The seat owns the limb binding; the handle owns the contact geometry and control presentation.

Keep the contact and the mechanic separate. A throttle handle can move the cockpit lever while an input provider supplies propulsion intent to the engine. Replacing the lever model or hand pose then does not require replacing the engine. For a custom control, first decide whether you need a new target, a new motion mapping or a new gameplay action; these have different extension points.

.. _evs-scripting-handles--implementation-map:

Implementation map
------------------

+------------------------------------------+-----------------------------------------------------------------------+
| Class                                    | Responsibility                                                        |
+==========================================+=======================================================================+
| ``IHandle`` / ``VehicleHandle``          | Common contact, preparation, binding and input contract.              |
+------------------------------------------+-----------------------------------------------------------------------+
| ``AnchorHandle``                         | Exposes authored hand/foot anchors without control animation.         |
+------------------------------------------+-----------------------------------------------------------------------+
| ``SteeringWheelHandle`` / ``YokeHandle`` | Describes steering contacts, surface geometry and hand participation. |
+------------------------------------------+-----------------------------------------------------------------------+
| ``JoystickHandle``                       | Combines authored steering contacts with pitch/roll motion.           |
+------------------------------------------+-----------------------------------------------------------------------+
| ``MotorcycleHandle``                     | Supplies fixed left/right contacts with prepared finger poses.        |
+------------------------------------------+-----------------------------------------------------------------------+
| ``ThrottleHandle`` / ``HandleMotion``    | Maps normalized travel to an anchored lever pose.                     |
+------------------------------------------+-----------------------------------------------------------------------+
| ``PedalHandle``                          | Animates pedal travel and exposes an ankle contact.                   |
+------------------------------------------+-----------------------------------------------------------------------+
| ``PedalFootHandle``                      | Transfers one stable ankle target between pedals.                     |
+------------------------------------------+-----------------------------------------------------------------------+
| ``SwitchHandle``                         | Owns requested detents, travel and request/arrival events.            |
+------------------------------------------+-----------------------------------------------------------------------+
| ``HandleSelector``                       | Chooses between two handles while preserving one seat assignment.     |
+------------------------------------------+-----------------------------------------------------------------------+
| ``HandTransferHandle``                   | Temporarily moves a hand to another control and restores its binding. |
+------------------------------------------+-----------------------------------------------------------------------+
| ``Passengers``                           | Discovers owned handles and supplies input before seat work.          |
+------------------------------------------+-----------------------------------------------------------------------+

.. _evs-scripting-handles--handle-contract:

Handle contract
---------------

The seat asks its configured handle for a target for a specific ``PassengerBodyPart``. ``GetAnchor(part)`` returns a stable ``Transform``, or ``null`` if that part is unsupported. Moving the transform updates the target without replacing the binding. Creating a new target on every query would repeatedly invalidate contact identity and generate unnecessary objects.

Preparation has two levels. ``Prepare()`` establishes reusable handle geometry. ``BindBodyPart(part, ik, animator)`` prepares that geometry for the current occupant, including adaptive finger binding when enabled. Keep character proportions and calibration on the character; a handle should describe its control surface rather than assume one particular hand size.

During the passenger pass, handles receive ``SetInput(command, deltaTime)`` in ``InputOrder``. This lets a coordinating handle consume state after handles it depends on. The seat then resolves its limb targets. Do not sample another keyboard input or tick the same passenger-driven operation from an independent loop. ``PedalHandle`` and ``PedalFootHandle`` already own render-rate travel through their built-in callbacks; their ``SetInput`` selects demand rather than advancing that travel twice.

``HandDriven(left)`` indicates whether the physical hand should be guided, ``HandSteering(left)`` whether it participates in steering support, and ``HandContact(left)`` supplies contact participation. These are different questions: a travelling hand may remain guided while its locked surface contact is released. The bool ``left`` means left hand when ``true`` and right hand when ``false``.

.. _evs-scripting-handles--connect-a-custom-target:

Connect a custom target
~~~~~~~~~~~~~~~~~~~~~~~

Use a ``VehicleHandle`` subclass when the application already knows where a palm should go. Place the component and its contact beneath the vehicle, assign it to the relevant seat limb, and let your animation or aiming system move the contact. The passenger system continues to own the limb; the application owns only the target pose.

**Example: ``ApplicationPalmHandle.cs``**

.. raw:: html

   <!-- example: ApplicationPalmHandle.cs -->

.. code-block:: csharp

   using UnityEngine;
   using EasyVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class ApplicationPalmHandle : VehicleHandle
       {
           public Transform contact;

           public override Transform GetAnchor(PassengerBodyPart part)
               => isActiveAndEnabled && part == PassengerBodyPart.RightHand ? contact : null;
       }
   }

The example accepts only the right hand and returns ``null`` for other parts. Add separate left/right targets if both hands are supported. For a palm-contact binding, place the target on the palm's contact surface; for a foot, use the ankle frame expected by the limb configuration. A wrist pivot and a palm contact are not interchangeable positions.

.. _evs-scripting-handles--runtime-handover:

Runtime handover
----------------

A limb configuration selects its mode, handle and optional direct anchor. Changing those choices rebuilds that limb's owned contact at the next applicable passenger pass. Other limbs and torso support remain in place. This is useful for changing a hand from a steering wheel to an auxiliary control without making the passenger exit and enter again.

Handover still needs one owner. An application gesture, steering regrip and a switch interaction must not independently save and restore the same limb fields. Use ``HandTransferHandle`` for an out-and-back gesture, ``HandleSelector`` for persistent selection between contacts, or steering reservations for an application task that temporarily takes a steering hand. These helpers retain their own ownership checks and cleanup boundaries.

.. _evs-scripting-handles--grip-dimensions:

Grip dimensions
---------------

Grip dimensions describe the surface the fingers should wrap around. They do not resize the visible model. If the configured grip is thicker than the rendered lever, the fingers can close around an invisible larger cylinder; if it is thinner, they can cut through the mesh. Measure the actual control in the same local frame used by the handle before tuning finger fitting.

.. _evs-scripting-handles--cylindrical-controls:

Cylindrical controls
~~~~~~~~~~~~~~~~~~~~

``VehicleHandle.gripDiameter`` is the full cylinder diameter in metres, not its radius. A 0.04 m diameter describes a 4 cm thick grip. The cylinder runs along the palm anchor's local X axis. Its centerline lies half that diameter toward local +Y from the palm contact. The target therefore describes contact on the cylinder surface rather than the center of the rod.

For a new lever, create a unit-scale contact child at the desired palm contact. Align its local X with the length of the grip and +Y toward the rod's centerline. Keep imported-mesh axis corrections on a separate mesh child. Positive uniform scale preserves the geometric assumptions; a nonuniformly scaled cylinder cannot be represented by a single diameter.

``adaptiveGrip`` enables fitting for supported hand bindings. ``gripDiameter`` describes the object; character finger lengths, flexion axes and pad sizes describe the hand. Increasing the grip diameter to hide a bad finger axis usually fixes one pose while making others worse. Validate the contact orientation and character calibration first.

.. _evs-scripting-handles--steering-rims-and-authored-contacts:

Steering rims and authored contacts
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A wheel uses ``rimRadius`` for the centerline radius and ``tubeRadius`` for the rim tube's radius. These are two different measurements, and ``tubeRadius`` is a radius rather than the cylinder diameter above. ``tubeDepthRadius`` can describe a different fore/aft tube section. ``customRim`` replaces the circular centerline with a closed set of at least three samples for irregular wheels.

``leftAngle`` and ``rightAngle`` place contacts around the rim. ``reverseApproach`` changes which direction faces away from the driver. With ``authoredTargets``, the component retains manually placed palm targets instead of generating their position from the rim. ``stickGrip`` then selects cylindrical fitting at those authored targets, which is useful for a joystick or another grip that uses steering-hand behavior without being a wheel rim.

Geometry changes require preparation and occupant rebinding, not just a new numeric value. Apply them at an explicit authoring/spawn boundary when possible. The following component is intended for an unoccupied vehicle: it updates a cylinder dimension and prepares the handle. For an already occupied seat, also perform the appropriate occupant binding refresh through its normal passenger lifecycle.

**Example: ``CylinderGripSetup.cs``**

.. raw:: html

   <!-- example: CylinderGripSetup.cs -->

.. code-block:: csharp

   using UnityEngine;
   using EasyVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class CylinderGripSetup : MonoBehaviour
       {
           public VehicleHandle handle;
           [Min(.004f)] public float diameterMetres = .04f;

           public void ApplyBeforeSeating()
           {
               if (!handle) return;
               handle.gripDiameter = Mathf.Max(.004f, diameterMetres);
               handle.Prepare();
           }
       }
   }

This example changes the common cylindrical measurement. It does not change ``SteeringWheelHandle.tubeRadius``, scale a mesh or calibrate a character. For a steering rim, configure the rim-specific measurements instead. See :doc:`Grip solving </Scripting/GripSolving>` for fitting and steering reservations.

.. _evs-scripting-handles--pedal-state-and-actions:

Pedal state and actions
-----------------------

``PedalHandle`` moves a pedal between released and pressed angles and exposes ``contactAnchor`` for the occupant's ankle. Parent that contact to the moving pedal so the target follows travel. ``motion`` holds the pivot mapping; ``releasedAngle`` and ``pressedAngle`` describe the model's endpoints in degrees.

With ``useResolvedPedals``, throttle/brake presentation follows ``DriveDemand`` and ``ServiceBrake``. This matters for signed forward/reverse input: a command can request the opposite direction while mechanics are still resolving it as braking. Reading the resolved actuator makes the foot match the vehicle's actual pedal interpretation. Other ``HandleInput`` selections read their mapped command channel.

``pressDuration`` and ``releaseDuration`` are the seconds needed for full travel. Smaller demands stop proportionally earlier. ``TargetValue`` is requested demand in 0–1; ``Value`` is current displayed travel. The render-rate ``Tick`` moves between them. ``onValueChanged`` reports displayed-value changes, so it can fire repeatedly while a pedal travels rather than only once when demand changes.

+-------------------------+----------------------------------------------------------------------------------+
| Operation               | Ownership and result                                                             |
+=========================+==================================================================================+
| ``SetValue(value)``     | Takes external ownership, clamps to 0–1 and requests smooth travel.              |
+-------------------------+----------------------------------------------------------------------------------+
| ``SetImmediate(value)`` | Takes external ownership and synchronizes value/pose immediately.                |
+-------------------------+----------------------------------------------------------------------------------+
| ``FollowInput()``       | Returns demand ownership to the configured input mapping.                        |
+-------------------------+----------------------------------------------------------------------------------+
| ``ResetMotion()``       | Releases external ownership, resets demand/travel and applies the released pose. |
+-------------------------+----------------------------------------------------------------------------------+

For a scripted pedal sequence, call ``SetValue`` when its demand changes and ``FollowInput`` when the sequence ends. Ordinary driving should remain in input-following mode. Calling ``SetValue`` every frame from an unrelated script would keep taking ownership away from input.

.. _evs-scripting-handles--moving-one-foot-between-pedals:

Moving one foot between pedals
------------------------------

``PedalFootHandle`` gives the seat one stable ankle target while choosing an accelerator or brake destination. Assign the two pedal handles, select ``foot``, and keep its ``target`` separate from both moving pedals. The seat binds to this helper; it does not switch directly between pedal transforms every frame.

Automatic selection reads resolved service braking. ``brakeThreshold`` starts brake selection; ``brakeReleaseThreshold`` provides hysteresis when returning to the accelerator. This avoids rapid switching around a tiny fluctuating brake value. The target travels in the helper's local frame, blends toward the moving destination and adds a lift arc using ``liftHeight`` over ``transferDuration``.

Use ``SelectBrake`` or ``SelectPedal`` for a temporary application choice. Manual selection persists until ``FollowInput()``; selecting ``null`` temporarily removes the usable destination. ``SnapToSelected()`` finishes target travel immediately, useful when establishing an initial seated pose. ``SelectionChanged`` means the destination selection changed, not that the foot has arrived. Read ``IsTransferring`` when arrival matters.

**Example: ``PedalFootOverride.cs``**

.. raw:: html

   <!-- example: PedalFootOverride.cs -->

.. code-block:: csharp

   using UnityEngine;
   using EasyVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class PedalFootOverride : MonoBehaviour
       {
           public PedalFootHandle foot;

           public void HoldBrakePose()
           {
               if (foot) foot.SelectBrake(true);
           }

           public void ResumeDrivingPose()
           {
               if (foot) foot.FollowInput();
           }

           private void OnDisable() => ResumeDrivingPose();
       }
   }

This controls the character's pedal choice only. It does not apply a vehicle brake request. Feed braking through the input/mechanic API when the application needs the vehicle itself to stop.

.. _evs-scripting-handles--switch-requests-and-settled-presentation:

Switch requests and settled presentation
----------------------------------------

``SwitchHandle`` presents two-position off/on controls or three-position negative/neutral/positive controls. ``Position`` is the requested detent; ``Value`` is normalized displayed travel. ``transitionDuration`` controls how long the visible mechanism takes to reach its destination. ``handAnchor`` follows the model and provides a palm target.

Use ``SetValue(bool)`` or ``Toggle()`` for binary controls. Enable ``threePosition`` before calling ``SetPosition(SwitchPosition.Negative)``; invalid enum values throw, and a negative binary position is rejected with an exception. For three-position geometry, ``neutralOffset`` is the middle pose between ``motion.minimum`` and ``motion.maximum``, expressed in the selected motion unit.

``PositionChanged`` and ``ValueChanged`` report changed requests. ``PositionReached`` and ``Switched`` report settled motion from ``SetInput``. A change between negative and positive changes the detent but keeps ``IsOn`` ``true``, so a bool-only listener cannot distinguish those states. Use position events when all three detents carry different meaning.

``SetImmediate`` and ``SetPositionImmediate`` synchronize silently. A mechanic-to-control binding should use them when displaying an existing state, so displaying “gear deployed” does not issue another gear request. Use request events for player intent and settled events for physical clicks; ``SwitchAudio`` already follows settled presentation.

.. _evs-scripting-handles--observe-all-switch-detents:

Observe all switch detents
~~~~~~~~~~~~~~~~~~~~~~~~~~

When a three-position switch has different meanings at both ends, subscribe to ``PositionChanged`` instead of the bool event. This observer captures the subscribed source and removes the same handler on disable. It exposes the requested detent for application UI; use ``PositionReached`` instead if the consumer needs settled presentation.

**Example: ``SwitchDetentObserver.cs``**

.. raw:: html

   <!-- example: SwitchDetentObserver.cs -->

.. code-block:: csharp

   using UnityEngine;
   using EasyVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class SwitchDetentObserver : MonoBehaviour
       {
           public SwitchHandle control;
           public SwitchPosition RequestedPosition { get; private set; }
           private SwitchHandle subscribed;

           private void OnEnable()
           {
               subscribed = control;
               if (!subscribed) return;
               subscribed.Prepare();
               RequestedPosition = subscribed.Position;
               subscribed.PositionChanged += Receive;
           }

           private void OnDisable()
           {
               if (subscribed) subscribed.PositionChanged -= Receive;
               subscribed = null;
           }

           private void Receive(SwitchPosition position) => RequestedPosition = position;
       }
   }

Editing ``control`` while enabled does not rebind the captured subscription. Use an explicit rebind or disable/re-enable this adapter when changing its source. Keep the gameplay action in the request/interaction path rather than adding it to a passive readout.

.. _evs-scripting-handles--temporary-hand-transfer:

Temporary hand transfer
-----------------------

``HandTransferHandle`` implements a guided trip from the currently controlled hand to a destination handle and back. ``Begin`` validates occupancy, the chosen hand, source control and destination target. An admitted transfer saves the current handle/hold choices and installs its temporary target for that hand.

The sequence releases palm contact for ``releaseDuration``, travels for ``travelDuration``, binds at the destination, invokes the arrival callback and ``Arrived``, waits for ``dwellDuration``, releases the destination contact, then travels back. Motion is interpolated relative to the vehicle so forward travel does not leave the hand behind in world space. ``IsBusy`` remains ``true`` throughout the sequence.

Use the arrival callback for a simple action that should occur when the hand reaches a control. Use :doc:`ControlInteraction </Scripting/Interactions>` when the action also needs reusable commit, completion, timeout and presentation-mode policy. Keep one transfer helper per simultaneous hand.

``Cancel()`` ends only an active transfer. Disable and loss of the original occupant also cancel it. Restoration checks whether the hand is still using this transfer or its destination before restoring the saved binding; it does not blindly overwrite an unrelated replacement owner's choice. Observe ``Completed`` and ``Cancelled`` to end application UI/input locks.

.. _evs-scripting-handles--extending-or-selecting-a-handle:

Extending or selecting a handle
-------------------------------

Use ``AnchorHandle`` for authored static contacts. Derive from ``VehicleHandle`` for a new contact/control contract. Derive from ``SteeringWheelHandle`` when steering participation and its surface/hand-state API are useful. ``JoystickHandle`` adds pitch/roll mapping around authored contacts; ``YokeHandle`` retains the steering-wheel contract. ``MotorcycleHandle`` uses prepared fixed finger poses, so prepare and save poses for the intended character variants during authoring.

``HandleMotion`` is the small geometry mapper used by several controls. ``SetValue`` maps 0–1 to its minimum/maximum; ``SetOffset`` applies a degree offset for rotation or local-distance offset for translation. It requires a valid independent ``anchor``, resets the part to that frame and applies the offset. It is not an input provider or a passenger scheduler.

``HandleSelector`` is useful when the seat should keep one assigned handle while another system chooses between idle/active contacts. Use its selection action for manual ownership and ``FollowInput`` to resume configured input selection. For each replacement, preserve stable targets and the base binding/cleanup behavior that the seat relies on.

.. _evs-scripting-handles--complete-public-method-and-event-index:

Complete public method and event index
--------------------------------------

The lists below cover public methods and events for this topic and their package base contracts. Signatures include overloads. See :doc:`the detailed limb handles and transfers API </API/Handles>` for arguments, return semantics, state and configuration. An override replaces the matching inherited implementation; it is not an additional call to make.

.. _evs-scripting-handles--anchorhandle:

AnchorHandle
~~~~~~~~~~~~

:ref:`AnchorHandle <evs-api-handles--anchorhandle>` gives the full declared contract.

+-----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| Method                                                          | Role                                                                                                               |
+=================================================================+====================================================================================================================+
| ``public override Transform GetAnchor(PassengerBodyPart part)`` | Returns the assigned anchor directly. The seat is responsible for assigning this handle to the intended body part. |
+-----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------+

.. _evs-scripting-handles--handtransferhandle:

HandTransferHandle
~~~~~~~~~~~~~~~~~~

:ref:`HandTransferHandle <evs-api-handles--handtransferhandle>` gives the full declared contract.

+---------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Method                                                                                                                          | Role                                                                                                                                                                                              |
+=================================================================================================================================+===================================================================================================================================================================================================+
| ``public virtual bool Begin(PassengerSeat passengerSeat, PassengerBodyPart hand, VehicleHandle next, Action onArrival = null)`` | Starts release → travel → destination bind/callback → dwell → release → return. Rejects busy/disabled helpers, missing occupancy, invalid hand/source/destination or uncontrolled source binding. |
+---------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override Transform GetAnchor(PassengerBodyPart bodyPart)``                                                             | Returns this transfer's persistent temporary target. ``Begin``/active ownership determines which hand uses it.                                                                                    |
+---------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override float HandContact(bool left)``                                                                                | Returns contact participation for the selected hand; guidance can remain enabled while surface contact is released.                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool HandSteering(bool left)``                                                                                | Reports whether the selected hand participates in steering support.                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void SetInput(Command command, float deltaTime)``                                                             | Advances the active release/travel/dwell/return phase. Cancels if occupancy, destination or binding ownership is no longer valid.                                                                 |
+---------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Cancel()``                                                                                                | Cancels an active transfer, clears its arrival callback and restores the saved handle/hold only while this transfer still owns the binding.                                                       |
+---------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+-----------------------------------+------------------------------------------------------------------------------------------------------------+
| Event / callback                  | Role                                                                                                       |
+===================================+============================================================================================================+
| ``public event Action Started``   | After temporary hand ownership begins. No payload.                                                         |
+-----------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public event Action Arrived``   | After the hand reaches and binds to the temporary destination, following the arrival callback. No payload. |
+-----------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public event Action Completed`` | After the out-and-back hand transfer completes and its binding is restored. No payload.                    |
+-----------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public event Action Cancelled`` | After an active hand transfer is cancelled and owned bindings are cleaned up. No payload.                  |
+-----------------------------------+------------------------------------------------------------------------------------------------------------+

.. _evs-scripting-handles--handlemotion:

HandleMotion
~~~~~~~~~~~~

:ref:`HandleMotion <evs-api-handles--handlemotion>` gives the full declared contract.

+-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Method                                          | Role                                                                                                                                                                 |
+=================================================+======================================================================================================================================================================+
| ``public virtual void SetValue(float value)``   | Clamps a fraction to 0–1, maps it between minimum and maximum, then applies ``SetOffset``. Rotation uses degrees; translation uses local distance.                   |
+-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetOffset(float offset)`` | Resets ``movingPart`` to the independent anchor and applies rotation in degrees or translation in local units. Invalid/nonfinite/self-descendant frames are ignored. |
+-------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-scripting-handles--handleselector:

HandleSelector
~~~~~~~~~~~~~~

:ref:`HandleSelector <evs-api-handles--handleselector>` gives the full declared contract.

+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Method                                                              | Role                                                                                                 |
+=====================================================================+======================================================================================================+
| ``public virtual void SelectActive(bool value)``                    | Selects the active or idle handle and takes manual selection ownership.                              |
+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public virtual void FollowInput()``                               | Releases a manual selection/value override and resumes configured input following.                   |
+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public override void SetInput(Command command, float deltaTime)`` | Chooses active/default handle from its configured Command mapping unless a manual selection owns it. |
+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public override Transform GetAnchor(PassengerBodyPart part)``     | Forwards contact lookup to the currently selected eligible handle.                                   |
+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+

+----------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| Event / callback                                               | Role                                                                                                              |
+================================================================+===================================================================================================================+
| ``public event System.Action<VehicleHandle> SelectionChanged`` | When the selected destination handle changes. Payload: ``VehicleHandle``, possibly ``null``; this is not arrival. |
+----------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+

.. _evs-scripting-handles--ihandle:

IHandle
~~~~~~~

:ref:`IHandle <evs-api-handles--ihandle>` gives the full declared contract.

+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| Method                                                                          | Role                                                                                                                |
+=================================================================================+=====================================================================================================================+
| ``void Prepare()``                                                              | Prepares reusable contact geometry or handle initialization without entering a seat.                                |
+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``Transform GetAnchor(PassengerBodyPart part)``                                 | Returns the stable contact transform for a supported body part, or ``null`` when unavailable/unsupported.           |
+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``void BindBodyPart(PassengerBodyPart part, HumanoidIK ik, Animator animator)`` | Prepares the selected limb for this handle, including supported adaptive finger binding and palm frames.            |
+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``void SetInput(Command command, float deltaTime)``                             | Consumes the owner-supplied command/timestep as part of the passenger handle pass.                                  |
+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``bool HandDriven(bool left)``                                                  | Reports whether the selected hand should receive physical target guidance.                                          |
+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``bool HandSteering(bool left)``                                                | Reports whether the selected hand participates in steering support.                                                 |
+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``float HandContact(bool left)``                                                | Returns contact participation for the selected hand; guidance can remain enabled while surface contact is released. |
+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+

.. _evs-scripting-handles--joystickhandle:

JoystickHandle
~~~~~~~~~~~~~~

:ref:`JoystickHandle <evs-api-handles--joystickhandle>` gives the full declared contract.

+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| Method                                                       | Role                                                                                                                               |
+==============================================================+====================================================================================================================================+
| ``public virtual void SetControls(float pitch, float roll)`` | Maps pitch -1..1 to ``HandleMotion`` travel and applies roll around ``localRollAxis`` between ``minimumRoll`` and ``maximumRoll``. |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-scripting-handles--motorcyclehandle:

MotorcycleHandle
~~~~~~~~~~~~~~~~

:ref:`MotorcycleHandle <evs-api-handles--motorcyclehandle>` gives the full declared contract.

+-------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| Method                                                                                          | Role                                                                                                     |
+=================================================================================================+==========================================================================================================+
| ``public override void BindBodyPart(PassengerBodyPart part, HumanoidIK ik, Animator animator)`` | Prepares the selected limb for this handle, including supported adaptive finger binding and palm frames. |
+-------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| ``public override Transform GetAnchor(PassengerBodyPart part)``                                 | Returns the prepared left/right grip target for the requested hand.                                      |
+-------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+

.. _evs-scripting-handles--pedalfoothandle:

PedalFootHandle
~~~~~~~~~~~~~~~

:ref:`PedalFootHandle <evs-api-handles--pedalfoothandle>` gives the full declared contract.

+-----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| Method                                                                                        | Role                                                                                                                                         |
+===============================================================================================+==============================================================================================================================================+
| ``public override void Prepare()``                                                            | Prepares reusable contact geometry or handle initialization without entering a seat.                                                         |
+-----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Tick(float deltaTime)``                                                 | Advances the declaring presentation/state machine by elapsed seconds; avoid a second call when its built-in owner already ticks it.          |
+-----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override Transform GetAnchor(PassengerBodyPart part)``                               | Returns its stable ankle target only for the configured foot with an enabled same-vehicle destination; otherwise returns ``null``.           |
+-----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void SetInput(Command command, float deltaTime)``                           | Selects brake/accelerator from resolved service braking with hysteresis while automatic selection owns the foot; it does not advance travel. |
+-----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SelectPedal(VehicleHandle pedal)``                                      | Selects a specific pedal handle, including ``null`` to release a usable foot destination.                                                    |
+-----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SelectBrake(bool value)``                                               | Selects the brake or accelerator pedal and takes manual foot-selection ownership.                                                            |
+-----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void FollowInput()``                                                         | Releases a manual selection/value override and resumes configured input following.                                                           |
+-----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetPedals(VehicleHandle acceleratorHandle, VehicleHandle brakeHandle)`` | Replaces the accelerator/brake handle references used by foot selection.                                                                     |
+-----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SnapToSelected()``                                                      | Finishes the foot target's current transfer immediately at its selected pedal.                                                               |
+-----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+

+---------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| Event / callback                                        | Role                                                                                                              |
+=========================================================+===================================================================================================================+
| ``public event Action<VehicleHandle> SelectionChanged`` | When the selected destination handle changes. Payload: ``VehicleHandle``, possibly ``null``; this is not arrival. |
+---------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+

.. _evs-scripting-handles--pedalhandle:

PedalHandle
~~~~~~~~~~~

:ref:`PedalHandle <evs-api-handles--pedalhandle>` gives the full declared contract.

+---------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Method                                                              | Role                                                                                                                                                          |
+=====================================================================+===============================================================================================================================================================+
| ``public override void Prepare()``                                  | Prepares reusable contact geometry or handle initialization without entering a seat.                                                                          |
+---------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ResetMotion()``                               | Clears presentation requests and restores the released/default motion state.                                                                                  |
+---------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Tick(float deltaTime)``                       | Advances the declaring presentation/state machine by elapsed seconds; avoid a second call when its built-in owner already ticks it.                           |
+---------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override Transform GetAnchor(PassengerBodyPart part)``     | Returns ``contactAnchor`` directly; author this as the ankle target beneath the moving pedal.                                                                 |
+---------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void SetInput(Command command, float deltaTime)`` | Updates ``TargetValue`` only while ``FollowsInput``. Reads resolved pedals or the configured Command channel; render-rate ``Tick`` advances displayed travel. |
+---------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetValue(float value)``                       | Takes external demand ownership, sanitizes/clamps value to 0–1 and requests smoothed pedal travel. ``FollowInput`` releases the override.                     |
+---------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetImmediate(float value)``                   | Takes external value ownership, clamps normalized travel and applies it immediately; ``onValueChanged`` reports an actual displayed-value change.             |
+---------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void FollowInput()``                               | Releases a manual selection/value override and resumes configured input following.                                                                            |
+---------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

+---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Event / callback                            | Role                                                                                                                                                            |
+=============================================+=================================================================================================================================================================+
| ``public UnityEvent<float> onValueChanged`` | After this control's value changes. Payload: the event's value type; ``PedalHandle`` reports displayed travel, ``SwitchHandle`` reports a changed bool request. |
+---------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-scripting-handles--steeringwheelhandle:

SteeringWheelHandle
~~~~~~~~~~~~~~~~~~~

:ref:`SteeringWheelHandle <evs-api-handles--steeringwheelhandle>` gives the full declared contract.

+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Method                                                                                                               | Role                                                                                                                                  |
+======================================================================================================================+=======================================================================================================================================+
| ``public override void Prepare()``                                                                                   | Prepares reusable contact geometry or handle initialization without entering a seat.                                                  |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void BindBodyPart(PassengerBodyPart part, HumanoidIK ik, Animator animator)``                      | Prepares the selected limb for this handle, including supported adaptive finger binding and palm frames.                              |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual Vector3 Centerline(float angle)``                                                                   | Evaluates the steering-rim centerline at an angular coordinate in the wheel's local frame.                                            |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float RadiusAt(float angle)``                                                                       | Returns the steering-rim tube radius at the supplied angular coordinate.                                                              |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float SignedDistanceLocal(Vector3 point)``                                                          | Evaluates a wheel-local point against the steering tube and returns scaled surface distance.                                          |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetGripMode(SteeringGripMode mode)``                                                           | Chooses both hands, left only, right only or released steering-grip permission.                                                       |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool AllowsHand(bool left)``                                                                        | Checks enabled state and the configured left/right grip-mode permission.                                                              |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``public override Transform GetAnchor(PassengerBodyPart part)``                                                      | Returns ``leftTarget``/``rightTarget`` only for an allowed corresponding hand; unsupported limbs or disallowed hands return ``null``. |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool HandDriven(bool left)``                                                                       | Reports whether the selected hand should receive physical target guidance.                                                            |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool HandSteering(bool left)``                                                                     | Reports whether the selected hand participates in steering support.                                                                   |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetHandControl(bool left, bool driven, bool steering)``                                        | Selects physical-guidance and steering-support participation independently for one hand.                                              |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool HandPoseFrozen(bool left)``                                                                    | Reports whether the selected hand retains its captured pose rather than continuously refitting.                                       |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool HandPinch(bool left)``                                                                         | Reports whether the selected hand uses the pinch gesture.                                                                             |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetHandPoseFrozen(bool left, bool value)``                                                     | Chooses captured-pose reuse for the selected hand.                                                                                    |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetHandPinch(bool left, bool value)``                                                          | Enables/disables the selected hand's pinch gesture.                                                                                   |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float HandFingerExtension(bool left)``                                                              | Returns the selected hand's normalized finger-extension gesture.                                                                      |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetHandFingerExtension(bool left, float value)``                                               | Sets normalized finger extension for one steering hand.                                                                               |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float PalmPressure(bool left)``                                                                     | Returns normalized palm-pressure presentation for the selected hand.                                                                  |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetPalmPressure(bool left, float value)``                                                      | Sets normalized palm pressure and updates a bound adaptive hand when applicable.                                                      |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float HandClosure(bool left)``                                                                      | Returns normalized finger-closure state for the selected steering hand.                                                               |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``public override float HandContact(bool left)``                                                                     | Returns contact participation for the selected hand; guidance can remain enabled while surface contact is released.                   |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool HandPreclosing(bool left)``                                                                    | Reports whether fingers are closing before palm contact settles.                                                                      |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetHandContact(bool left, float closure, float contact, bool preclosing = false)``             | Sets normalized closure/contact and the preclosing flag for one steering hand.                                                        |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float SignedDistance(Vector3 worldPoint)``                                                          | Returns signed world-space distance to the steering tube surface; positive means outside.                                             |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void GetContactFrame(float angle, out Vector3 point, out Quaternion rotation)``                     | Returns a world-space contact point/orientation at an angular coordinate around the steering rim.                                     |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void GetPalmContactFrame(float angle, float pressure, out Vector3 point, out Quaternion rotation)`` | Returns a world palm-contact frame including the requested pressure adjustment.                                                       |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void UpdateTargets()``                                                                              | Updates steering palm targets from current geometry without changing seat occupancy.                                                  |
+----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-scripting-handles--switchhandle:

SwitchHandle
~~~~~~~~~~~~

:ref:`SwitchHandle <evs-api-handles--switchhandle>` gives the full declared contract.

+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Method                                                                | Role                                                                                                                                                                                                  |
+=======================================================================+=======================================================================================================================================================================================================+
| ``public override void Prepare()``                                    | Prepares reusable contact geometry or handle initialization without entering a seat.                                                                                                                  |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override Transform GetAnchor(PassengerBodyPart part)``       | Returns ``handAnchor`` directly; it does not filter the requested body-part enum.                                                                                                                     |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetValue(bool value)``                          | Requests Positive for ``true`` and Neutral for ``false``. Changed requests emit position/bool notifications and start travel.                                                                         |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Toggle()``                                      | Requests the opposite current body/switch/wiper/profile/gear state through the declaring component.                                                                                                   |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetPosition(SwitchPosition position)``          | Requests a detent. Invalid enum values throw ``ArgumentOutOfRangeException``; Negative in binary mode throws ``InvalidOperationException``. A changed request starts travel and emits request events. |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetImmediate(bool value)``                      | Silently synchronizes Positive/Neutral, displayed value and motion without request or settlement callbacks.                                                                                           |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetPositionImmediate(SwitchPosition position)`` | Silently synchronizes a switch detent and displayed pose without issuing control events.                                                                                                              |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void SetInput(Command command, float deltaTime)``   | Advances detent travel by elapsed seconds, applies motion, then emits Switched and ``PositionReached`` on settlement.                                                                                 |
+-----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

+---------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Event / callback                                        | Role                                                                                                                                                                                                     |
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

.. _evs-scripting-handles--throttlehandle:

ThrottleHandle
~~~~~~~~~~~~~~

:ref:`ThrottleHandle <evs-api-handles--throttlehandle>` gives the full declared contract.

+-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| Method                                                          | Role                                                                                                                |
+=================================================================+=====================================================================================================================+
| ``public override Transform GetAnchor(PassengerBodyPart part)`` | Returns ``handAnchor`` directly; it does not filter the requested body-part enum.                                   |
+-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetValue(float value)``                   | Passes normalized lever travel to its ``HandleMotion`` geometry mapper; it does not set mechanical engine throttle. |
+-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+

.. _evs-scripting-handles--vehiclehandle:

VehicleHandle
~~~~~~~~~~~~~

:ref:`VehicleHandle <evs-api-handles--vehiclehandle>` gives the full declared contract.

+------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Method                                                                                         | Role                                                                                                                            |
+================================================================================================+=================================================================================================================================+
| ``public virtual void Prepare()``                                                              | Prepares reusable contact geometry or handle initialization without entering a seat.                                            |
+------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ResetHandle()``                                                          | Resets local handle state through the common extensible handle contract.                                                        |
+------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void BindBodyPart(PassengerBodyPart part, HumanoidIK ik, Animator animator)`` | Prepares the selected limb for this handle, including supported adaptive finger binding and palm frames.                        |
+------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public abstract Transform GetAnchor(PassengerBodyPart part)``                                | Returns the stable contact transform for a supported body part, or ``null`` when unavailable/unsupported.                       |
+------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetInput(Command command, float deltaTime)``                             | Receives the sampled command/timestep from Passengers. Base implementation is empty; override for input-driven handle behavior. |
+------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool HandDriven(bool left)``                                                  | Reports whether the selected hand should receive physical target guidance.                                                      |
+------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool HandSteering(bool left)``                                                | Reports whether the selected hand participates in steering support.                                                             |
+------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float HandContact(bool left)``                                                | Returns contact participation for the selected hand; guidance can remain enabled while surface contact is released.             |
+------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------+
