.. _evs-scripting-passengeraccess--animated-access-contracts:

Animated access contracts
=========================

Passenger access coordinates an asynchronous journey between a standing character and a seat. The seat supplies an entry/exit endpoint and admission rules; an access motion moves or animates the character; ``PassengerAccess`` owns the reservation and the sequence that hands ownership across.

This is useful when a button press should open a door, play a boarding animation and only then establish occupancy. It is a different operation from immediate ``PassengerSeat.TryEnter``, so admission, animation progress and final seat state must be observed separately.

.. _evs-scripting-passengeraccess--implementation-map:

Implementation map
------------------

+----------------------------+---------------------------------------------------------------------------+
| Class                      | Responsibility                                                            |
+============================+===========================================================================+
| ``PassengerAccess``        | Owns the entry/exit state machine, reservation and cancellation.          |
+----------------------------+---------------------------------------------------------------------------+
| ``SeatAccess``             | Describes the seat endpoint, outside marker, door and admission settings. |
+----------------------------+---------------------------------------------------------------------------+
| ``AccessMotion``           | Abstract motion adapter for beginning, sampling and ending access.        |
+----------------------------+---------------------------------------------------------------------------+
| ``HumanoidAccessMotion``   | Built-in Animator-based humanoid access implementation.                   |
+----------------------------+---------------------------------------------------------------------------+
| ``AccessAnimationProfile`` | Stores animation states, references and timing configuration.             |
+----------------------------+---------------------------------------------------------------------------+
| ``AccessAnimationEvents``  | Relays animation access markers into the sequence.                        |
+----------------------------+---------------------------------------------------------------------------+

``PassengerAccess`` owns a reservation and the entry/exit state machine; ``AccessMotion`` owns character motion. ``SeatAccess`` stores the seat, outside endpoint, optional door, profile and admission/clearance settings.

.. _evs-scripting-passengeraccess--admission-and-completion:

Admission and completion
------------------------

A reservation prevents another access request from taking the seat during the handover. Entry does not become occupancy merely because motion starts; exit can release occupancy while the access sequence still owns the character's departure. Application controls should represent “boarding” or “exiting” explicitly instead of treating every admitted request as already complete.

Use ``Finished`` to release application UI locks, then inspect actual occupancy to decide possession. Cancellation can happen before or after a particular handover boundary, so a single animation-success flag is not a replacement for checking the seat.

``TryEnter``/``TryExit`` return admission, not final occupancy/completion. ``State`` progresses through Opening, Moving and Closing. Entry commits occupancy after motion handover; exit releases seating before motion while retaining reservation. ``Finished``/completed/cancelled are distinct from seat ``Entered``/``Exited``.

An outside marker supplies a feet-level endpoint and optional heading. Ground projection changes the effective endpoint without moving the marker. ``Exit`` clearance is an endpoint capsule check, not navigation or full-body obstacle avoidance.

.. _evs-scripting-passengeraccess--animation-bindings:

Animation bindings
------------------

``HumanoidAccessMotion`` moves the character using an Animator-backed access sequence. The animation profile provides the reference frames and state/timing configuration; ``SeatAccess`` supplies the endpoint and optional door. The same character motion can therefore be reused with different seat endpoints if the authored geometry and animation remain compatible.

``Configure`` the standing/seated reference states as well as enter/exit states. Root-motion orientation, useful clip range and transition settings must agree with the reference used for spatial matching. A clip that looks correct in isolation can still hand the character to the seat with an offset if its import or state setup differs from the reference.

For another animation framework, derive ``AccessMotion`` instead of making ``PassengerAccess`` discover that framework. Implement admission, sampling, completion and cleanup there. Use ``CanPlay`` to reject incompatible access before reservation/motion becomes an abandoned partial operation.

The reference clip supplies a spatial/timing calibration for the state being played. Keep its useful motion range consistent with the Animator state's speed, transition and offsets. If those disagree, a visually correct clip can still reach the handover point at the wrong place or time.

Door markers are part of the same timeline. Verify that they fall inside the played range and are delivered from the actual animated object. A clip containing an event outside its useful range cannot open the door simply because that event exists in the asset.

``AccessAnimationProfile`` explicitly supplies controller/layer, standing/seated/enter/exit paths, triggers and matching Humanoid reference clips. The Animator owns playback; references calibrate spatial frames. The built-in adapter expects single-clip access states matching those references, not arbitrary Blend Trees.

``Configure`` useful clip ranges, retained import orientation/position, state offsets/exit times, playback speed, transition allowance and completion timeout together. Profile door events must exist in the useful range and be delivered at playback. ``State`` transitions complete only after the terminal-state handover.

.. _evs-scripting-passengeraccess--request-and-observe-access:

Request and observe access
--------------------------

Assign ``PassengerAccess`` on the character and a configured ``SeatAccess``. The named completion handler survives cancellation and is unsubscribed from the exact captured source.

**Example: ``PassengerAccessButton.cs``**

.. raw:: html

   <!-- example: PassengerAccessButton.cs -->

.. code-block:: csharp

   using UnityEngine;
   using EasyVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class PassengerAccessButton : MonoBehaviour
       {
           public PassengerAccess access;
           public SeatAccess target;
           public bool LastCompleted { get; private set; }
           private PassengerAccess subscribed;

           private void OnEnable()
           {
               subscribed = access;
               if (subscribed) subscribed.Finished += OnFinished;
           }

           private void OnDisable()
           {
               if (subscribed) subscribed.Finished -= OnFinished;
               subscribed = null;
           }

           public bool Enter() => access && access.TryEnter(target);
           public bool Exit() => access && access.TryExit();
           private void OnFinished(PassengerAccess source, bool success)
               => LastCompleted = success;
       }
   }

.. _evs-scripting-passengeraccess--cancellation-and-extension:

Cancellation and extension
--------------------------

A custom ``AccessMotion`` implements ``Begin``, ``Sample`` and ``End``. ``Begin`` accepts the selected ``SeatAccess``, character body and direction; use it to acquire only the motion resources this adapter owns. ``Sample(float normalizedTime)`` receives progress, while ``End(bool completed)`` is the cleanup boundary for both success and interruption.

Use ``IsComplete``, ``GetDuration`` and ``CompletionTimeout`` coherently when the external animation or navigation system can outlast nominal progress. A timeout must end the adapter's ownership rather than leaving a character controller disabled forever. Keep seat selection and player identity outside the reusable motion adapter.

``Cancel`` unwinds motion/reservation. Interrupted ordinary exit may reseat its own released occupant; external ejection is not undone. Already committed occupancy may remain after closure cancellation. Read actual occupancy in completion handlers.

Derive from ``AccessMotion`` for navigation, another animation framework or whole-body clearance. Implement its completion/timeout contract. Derive ``SeatAccess`` for custom door admission/readiness. Do not infer the controlled player or target vehicle inside a reusable motion adapter.

.. _evs-scripting-passengeraccess--complete-public-method-and-event-index:

Complete public method and event index
--------------------------------------

The lists below cover public methods and events for this topic and their package base contracts. Signatures include overloads. See :doc:`the detailed animated access API </API/PassengerAccess>` for arguments, return semantics, state and configuration. An override replaces the matching inherited implementation; it is not an additional call to make.

.. _evs-scripting-passengeraccess--accessanimationevents:

AccessAnimationEvents
~~~~~~~~~~~~~~~~~~~~~

:ref:`AccessAnimationEvents <evs-api-passengeraccess--accessanimationevents>` gives the full declared contract.

+-------------------------------------------+-----------------------------------------------------------------------------+
| Method                                    | Role                                                                        |
+===========================================+=============================================================================+
| ``public virtual void AccessOpenDoor()``  | Delivers an animation marker requesting opening of the current access door. |
+-------------------------------------------+-----------------------------------------------------------------------------+
| ``public virtual void AccessCloseDoor()`` | Delivers an animation marker requesting closure of the current access door. |
+-------------------------------------------+-----------------------------------------------------------------------------+

.. _evs-scripting-passengeraccess--accessmotion:

AccessMotion
~~~~~~~~~~~~

:ref:`AccessMotion <evs-api-passengeraccess--accessmotion>` gives the full declared contract.

+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| Method                                                                                     | Role                                                                                                                                                 |
+============================================================================================+======================================================================================================================================================+
| ``public abstract bool Begin(SeatAccess access, PassengerBody passenger, bool entering)``  | Attempts to begin character motion for the selected endpoint/body/direction. False rejects the adapter operation before successful motion ownership. |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public abstract void End(bool completed)``                                               | Ends the motion adapter, using the completion flag to restore or hand over its owned state.                                                          |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool CanPlay(SeatAccess access, PassengerBody passenger, bool entering)`` | Checks whether the motion adapter can play this access operation for the supplied body and direction.                                                |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float GetDuration(SeatAccess access, bool entering)``                     | Returns nominal access-motion duration for this endpoint and direction.                                                                              |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public abstract void Sample(float normalizedTime)``                                      | Receives normalized access progress from ``PassengerAccess``; implement pose/motion sampling without choosing a new seat.                            |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-scripting-passengeraccess--humanoidaccessmotion:

HumanoidAccessMotion
~~~~~~~~~~~~~~~~~~~~

:ref:`HumanoidAccessMotion <evs-api-passengeraccess--humanoidaccessmotion>` gives the full declared contract.

+-----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| Method                                                                                        | Role                                                                                                                                    |
+===============================================================================================+=========================================================================================================================================+
| ``public virtual void Configure(AccessAnimationProfile profile)``                             | Selects the ``AccessAnimationProfile`` used by subsequent access motion.                                                                |
+-----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool Begin(SeatAccess target, PassengerBody passenger, bool isEntering)``   | Validates humanoid Animator, clips, mapped feet/pelvis and non-ragdoll state, then captures character/Animator state for access motion. |
+-----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void End(bool completed)``                                                  | Ends the motion adapter, using the completion flag to restore or hand over its owned state.                                             |
+-----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float Duration(bool entering)``                                              | Returns the built-in humanoid motion duration for the selected access direction/configuration.                                          |
+-----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool CanPlay(SeatAccess target, PassengerBody passenger, bool isEntering)`` | Checks whether the motion adapter can play this access operation for the supplied body and direction.                                   |
+-----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| ``public override float GetDuration(SeatAccess target, bool isEntering)``                     | Returns nominal access-motion duration for this endpoint and direction.                                                                 |
+-----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Sample(float normalizedTime)``                                         | Evaluates the access motion or water style at the supplied normalized/world sample coordinates.                                         |
+-----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ReleaseIdleFeet()``                                                     | Releases temporary idle-foot ownership held during humanoid access motion.                                                              |
+-----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-scripting-passengeraccess--passengeraccess:

PassengerAccess
~~~~~~~~~~~~~~~

:ref:`PassengerAccess <evs-api-passengeraccess--passengeraccess>` gives the full declared contract.

+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| Method                                              | Role                                                                                                                                                 |
+=====================================================+======================================================================================================================================================+
| ``public virtual bool TryEnter(SeatAccess access)`` | Admits an asynchronous entry and reserves the endpoint/seat. True means started, not occupied/completed; observe Finished and actual seat occupancy. |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryExit()``                   | Admits asynchronous departure. Seat release and motion completion occur at different boundaries; observe Finished for sequence outcome.              |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void AnimationDoor(bool open)``    | Routes an animation door request into the current passenger access sequence.                                                                         |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Cancel()``                    | Unwinds this access attempt's motion/reservation and performs its state-specific occupancy cleanup. Already committed occupancy need not be undone.  |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+

+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Event / callback                                                   | Role                                                                                                                                 |
+====================================================================+======================================================================================================================================+
| ``public event Action<PassengerAccess, AccessState> StateChanged`` | When access sequencing changes. Payload: ``PassengerAccess`` and ``AccessState``; seat occupancy may commit at a different boundary. |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerAccess, bool> Finished``            | When an access attempt ends. Payload: ``PassengerAccess`` and success bool; inspect actual occupancy after cancellation/handover.    |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent started``                                      | Inspector callback when access sequencing starts; no payload.                                                                        |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent completed``                                    | Inspector callback when access succeeds; no payload.                                                                                 |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent cancelled``                                    | Inspector callback when access is cancelled; no payload.                                                                             |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-scripting-passengeraccess--seataccess:

SeatAccess
~~~~~~~~~~

:ref:`SeatAccess <evs-api-passengeraccess--seataccess>` gives the full declared contract.

+------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| Method                                                                 | Role                                                                                         |
+========================================================================+==============================================================================================+
| ``public virtual void RequestDoor(bool open)``                         | Requests the configured access door's required state for the current operation.              |
+------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``public virtual bool DoorReady(bool open)``                           | Checks whether the configured door has reached the required access state.                    |
+------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``public virtual bool CanContinue(PassengerBody passenger)``           | Checks whether an admitted seat-access sequence can still continue.                          |
+------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``public virtual bool CanUse(PassengerBody passenger, bool entering)`` | Checks whether a seat-access endpoint is currently usable by the supplied passenger.         |
+------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``public virtual bool IsExitClear(PassengerBody passenger)``           | Checks the configured outside endpoint capsule for exit clearance; it does not plan a route. |
+------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+
