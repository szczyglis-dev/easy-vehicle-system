.. _evs-scripting-events--events-and-telemetry:

Events and telemetry
====================

Events connect the vehicle to UI, audio and application rules without making those consumers run the mechanics themselves. There are two useful kinds of observation: snapshots for continuously changing state, and notifications for accepted transitions such as ignition, entry or a committed interaction.

A display usually needs the latest ``Telemetry``; a quest or interaction system usually needs a particular event. Choosing the right source avoids reconstructing meaning from raw velocities or repeatedly comparing Inspector fields.

.. _evs-scripting-events--implementation-map:

Implementation map
------------------

+-----------------------+-----------------------------------------------------------------------------------------+
| Class                 | Responsibility                                                                          |
+=======================+=========================================================================================+
| ``VehicleController`` | Publishes command, configuration, ownership, collision and post-pipeline notifications. |
+-----------------------+-----------------------------------------------------------------------------------------+
| ``Telemetry``         | Carries the cached vehicle readings used by displays and observers.                     |
+-----------------------+-----------------------------------------------------------------------------------------+
| ``Impact``            | Stores copied collision information for deferred consumers.                             |
+-----------------------+-----------------------------------------------------------------------------------------+
| ``Module``            | Exposes lifecycle notifications around registered module work.                          |
+-----------------------+-----------------------------------------------------------------------------------------+
| ``Events``            | Provides vehicle feedback events for effect integrations.                               |
+-----------------------+-----------------------------------------------------------------------------------------+

.. _evs-scripting-events--subscribe-to-a-components-events:

Subscribe to a component's events
---------------------------------

An event lets a component notify your application when something happens. For example, ``Engine.EngineStateChanged`` reports an ignition/shutdown state change, while ``PassengerSeat.Entered`` reports that a body has actually occupied the seat. Subscribe to the component that owns the result you need, rather than reconstructing it from input or polling every frame.

A C# subscription has three parts: the source instance, the event and a handler with matching arguments. ``engine.EngineStateChanged += OnEngineStateChanged`` adds the handler; ``-=`` removes that same handler from that same engine. An ``Action<bool>`` event needs a handler accepting one bool. ``PassengerSeat.Exited`` needs a body and ``PassengerExitReason``, in that order.

Subscribe in ``OnEnable`` and unsubscribe in ``OnDisable`` for an observer that should follow its Unity enabled lifetime. Use named methods, or retain a delegate if using a lambda. Writing a new lambda when unsubscribing creates another delegate and does not remove the original subscription.

.. _evs-scripting-events--bind-engine-and-seat-state:

Bind engine and seat state
~~~~~~~~~~~~~~~~~~~~~~~~~~

Assign the engine and seat in the Inspector. The example reads their initial state, then updates only when their events fire. Reading initial state matters because subscribing does not replay earlier events: an already running engine or occupied seat may not change again soon.

**Example: ``VehicleEventBinding.cs``**

.. raw:: html

   <!-- example: VehicleEventBinding.cs -->

.. code-block:: csharp

   using UnityEngine;
   using EasyVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class VehicleEventBinding : MonoBehaviour
       {
           public Engine engine;
           public PassengerSeat seat;
           public bool EngineRunning { get; private set; }
           public bool SeatOccupied { get; private set; }

           private Engine subscribedEngine;
           private PassengerSeat subscribedSeat;

           private void OnEnable() => Bind(engine, seat);
           private void OnDisable() => Unsubscribe();

           public void Bind(Engine nextEngine, PassengerSeat nextSeat)
           {
               Unsubscribe();
               engine = nextEngine;
               seat = nextSeat;
               EngineRunning = engine && engine.EngineRunning;
               SeatOccupied = seat && seat.Occupant;
               if (!isActiveAndEnabled) return;

               subscribedEngine = engine;
               subscribedSeat = seat;
               if (subscribedEngine)
                   subscribedEngine.EngineStateChanged += OnEngineStateChanged;
               if (subscribedSeat)
               {
                   subscribedSeat.Entered += OnEntered;
                   subscribedSeat.Exited += OnExited;
               }
           }

           private void Unsubscribe()
           {
               if (subscribedEngine)
                   subscribedEngine.EngineStateChanged -= OnEngineStateChanged;
               if (subscribedSeat)
               {
                   subscribedSeat.Entered -= OnEntered;
                   subscribedSeat.Exited -= OnExited;
               }
               subscribedEngine = null;
               subscribedSeat = null;
           }

           private void OnEngineStateChanged(bool running) => EngineRunning = running;
           private void OnEntered(PassengerBody body) => SeatOccupied = true;
           private void OnExited(PassengerBody body, PassengerExitReason reason)
               => SeatOccupied = false;
       }
   }

Call ``Bind(nextEngine, nextSeat)`` when the application changes vehicles. It removes old subscriptions before adding new ones and captures the actual subscribed instances for cleanup. Merely assigning another Inspector field while enabled does not move an existing subscription. The properties above are ready for a UI adapter; they do not start the engine, enter a seat or change input ownership.

.. _evs-scripting-events--inspector-callbacks-and-c-events:

Inspector callbacks and C# events
---------------------------------

C# events use ``+=`` and ``-=``. Inspector callbacks are ``UnityEvent`` fields: configure them in the Inspector, or use ``AddListener`` and ``RemoveListener`` for runtime listeners. For example, ``ControlInteraction.onCommit`` is a ``UnityEvent``, not an event named ``Commit``; ``Commit()`` is the operation that commits the interaction.

For a runtime listener, pair ``interaction.onCommit.AddListener(OnCommitted)`` with ``interaction.onCommit.RemoveListener(OnCommitted)`` at the same lifecycle boundary. ``OnCommitted`` takes no arguments for this callback. Configure persistent Inspector listeners on the component itself; removing a runtime listener is not a request to erase those Inspector bindings.

Choose the notification boundary deliberately. A switch request event means the requested detent changed; a settled event means its visible travel finished. A successful access request means the sequence started; seat entry means occupancy changed. Use the owning type's :ref:`API event table <evs-api--event-subscriptions-and-payloads>` for the exact payload and timing. Keep a gameplay action in one commit path so an Inspector listener and a supplied callback do not invoke it twice.

.. _evs-scripting-events--choose-the-observation-point:

Choose the observation point
----------------------------

The word “after” in ``AfterPhysicsStep`` refers to completion of the package's ordered module work. Unity still owns native simulation timing. If an observer needs a result from a later native collision callback, use that callback's notification rather than assuming that an additional native simulation has just occurred.

Keep synchronous handlers short. Copy the values needed for later UI or application work and return. For a buffered history, retain value snapshots rather than a reference to a live ``Collision``. For asynchronous processing, the application is responsible for thread boundaries; event delivery itself is on Unity's main thread.

``AfterPhysicsStep`` publishes the immutable telemetry snapshot after the module pipeline. It describes the outputs from that pipeline and the current cached physics readings; it is not a separate extra physics simulation. Cache it for UI rendering.

Action events generally report actual transitions made through public methods. Assigning a public field does not necessarily invoke the same validation/events. Continuous observers report resolved state. Publishers run synchronously on Unity's main thread; avoid re-entering the same action from its event.

Use a copied ``Impact`` when work outlives a collision callback. A live Unity ``Collision`` belongs to that callback.

.. _evs-scripting-events--observe-without-polling-physics:

Observe without polling physics
-------------------------------

The component initializes from ``Telemetry`` before subscribing, so a newly opened readout can show the current cached state immediately. It captures the subscribed vehicle separately from the editable ``vehicle`` field. Cleanup therefore removes the handler from the object that actually owns it, even if the field was changed in the Inspector.

Expose read-only properties to a UI framework and let that framework decide formatting and refresh frequency. The mechanical event should not depend on a particular text label, canvas or unit display.

Attach this to a UI/controller object and assign the vehicle. It exposes values for your UI framework; no UI package is required. It subscribes once and removes that subscription on disable.

**Example: ``VehicleReadout.cs``**

.. raw:: html

   <!-- example: VehicleReadout.cs -->

.. code-block:: csharp

   using UnityEngine;
   using EasyVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class VehicleReadout : MonoBehaviour
       {
           public VehicleController vehicle;
           public float SpeedKph { get; private set; }
           public float Rpm { get; private set; }
           private VehicleController subscribed;

           private void OnEnable()
           {
               subscribed = vehicle;
               if (!subscribed) return;
               Receive(subscribed.Telemetry);
               subscribed.AfterPhysicsStep += Receive;
           }

           private void OnDisable()
           {
               if (subscribed) subscribed.AfterPhysicsStep -= Receive;
               subscribed = null;
           }

           private void Receive(Telemetry state)
           {
               SpeedKph = state.SpeedKph;
               Rpm = state.Rpm;
           }
       }
   }

Rebind the component when changing its vehicle; merely editing the field while enabled does not move the captured subscription.

.. _evs-scripting-events--state-and-lifecycle-events:

State and lifecycle events
--------------------------

Prefer the publisher closest to the rule you are implementing. A seat's ``Entered`` event means occupancy has changed; an access sequence's ``Finished`` event means that sequence has ended. Those are different moments and can have different outcomes after cancellation. Similarly, an accepted damage hit and a completed geometry upload serve different consumers.

When implementing a derived component, preserve the relationship between state mutation and notification. Publish success only after the corresponding state is valid. Callers may inspect the component synchronously inside a handler, so notifying before updating its state exposes an inconsistent result.

+------------------------+---------------------------------------------------------------------------------------------+
| Source                 | Observe                                                                                     |
+========================+=============================================================================================+
| ``VehicleController``  | Configuration, input source, module membership, drive profile, teleport and sampled command |
+------------------------+---------------------------------------------------------------------------------------------+
| ``Engine``             | Ignition and accepted gear changes                                                          |
+------------------------+---------------------------------------------------------------------------------------------+
| ``FuelTank``           | Quantity change, empty transition and actual fuel increase                                  |
+------------------------+---------------------------------------------------------------------------------------------+
| ``PassengerSeat``      | ``Entered``, ``Exited``, ``ControllerChanged`` and custom ``ResetRequested``                |
+------------------------+---------------------------------------------------------------------------------------------+
| ``ControlInteraction`` | Inspector callbacks ``onStarted``, ``onCommit``, ``onCompleted`` and ``onCancelled``        |
+------------------------+---------------------------------------------------------------------------------------------+
| ``Damage``             | Accepted ``DamageHit`` snapshots                                                            |
+------------------------+---------------------------------------------------------------------------------------------+

Use named handlers or retain delegate references when unsubscribing. A protected Raise helper emits a notification; it does not implement the corresponding state change for a replacement.

.. _evs-scripting-events--complete-public-method-and-event-index:

Complete public method and event index
--------------------------------------

The lists below cover public methods and events for this topic and their package base contracts. Signatures include overloads. See :doc:`the detailed telemetry and feedback events API </API/Events>` for arguments, return semantics, state and configuration. An override replaces the matching inherited implementation; it is not an additional call to make.

.. _evs-scripting-events--events:

Events
~~~~~~

:ref:`Events <evs-api-events--events>` gives the full declared contract.

+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Method                                                                                     | Role                                                                                                                                   |
+============================================================================================+========================================================================================================================================+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Derives vehicle feedback transitions from current resolved mechanics/contact state and publishes corresponding ``EffectEvent`` values. |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ResetState()``                                                       | Clears the declaring mechanic's retained simulation history at an explicit reset boundary.                                             |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Publish(string id, float intensity, Vector3 position)``              | Publishes a vehicle feedback event through the Events component.                                                                       |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+

+---------------------------------------------+-----------------------------------------------------------+
| Event / callback                            | Role                                                      |
+=============================================+===========================================================+
| ``public event Action<EffectEvent> Raised`` | When Events publishes feedback. Payload: ``EffectEvent``. |
+---------------------------------------------+-----------------------------------------------------------+

.. _evs-scripting-events--feedback:

Feedback
~~~~~~~~

:ref:`Feedback <evs-api-events--feedback>` gives the full declared contract.

+-------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| Method                                                                  | Role                                                                                                   |
+=========================================================================+========================================================================================================+
| ``public override void Configure(VehicleController v)``                 | Resizes contact storage and clears surface caches for the configured wheel set.                        |
+-------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController v, Command c, float dt)`` | Samples wheel contact/activity and resolves presentation surfaces, then publishes changes and Sampled. |
+-------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+
| ``public virtual void ClearSurfaceCache()``                             | Invalidates cached collider-to-effect-surface resolutions so later feedback can resolve again.         |
+-------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+

+----------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Event / callback                                                     | Role                                                                                                                      |
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

.. _evs-scripting-events--imodule:

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

.. _evs-scripting-events--module:

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

.. _evs-scripting-events--telemetry:

Telemetry
~~~~~~~~~

-  ``public float GetSpeed(SpeedUnit unit)`` — Returns speed from the captured snapshot in the requested unit.
