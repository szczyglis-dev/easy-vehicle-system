.. _evs-architecture--architecture-and-update-ownership:

Architecture and update ownership
=================================

The package is built around one vehicle owner and small components with separate responsibilities. ``VehicleController`` owns the root body, command sampling and module schedule. Modules contribute mechanics; strategies specialize movement or passenger behavior; presentation components consume resolved state.

Two structures help navigate the implementation: categories describe what a component is responsible for, while phases describe when its work runs. They are deliberately separate. A component's folder/category is not sufficient to determine its position relative to another mechanic.

.. _evs-architecture--implementation-map:

Implementation map
------------------

+-----------------------+--------------------------------------------------------------------------------+
| Class                 | Responsibility                                                                 |
+=======================+================================================================================+
| ``VehicleController`` | Vehicle composition root, configuration boundary and fixed-step orchestration. |
+-----------------------+--------------------------------------------------------------------------------+
| ``IModule``           | ``Module`` contracts, categories and the phase dependency sequence.            |
+-----------------------+--------------------------------------------------------------------------------+
| ``Module``            | Common component lifecycle and profile-compatibility behavior.                 |
+-----------------------+--------------------------------------------------------------------------------+
| ``CategoryCore``      | Controller-owned schedule for one module category.                             |
+-----------------------+--------------------------------------------------------------------------------+
| ``Drive``             | Nested owner of the current movement strategy.                                 |
+-----------------------+--------------------------------------------------------------------------------+
| ``Passengers``        | Nested owner of seats, handles and passenger updates.                          |
+-----------------------+--------------------------------------------------------------------------------+
| ``Audio``             | Nested owner of audio-channel rendering and routing.                           |
+-----------------------+--------------------------------------------------------------------------------+

Part of the :doc:`Scripting Reference </Scripting/index>`.

Public types use ``EasyVehicleSystem``; reference the ``EasyVehicleSystem.Runtime`` assembly from your integration. Runtime components do not depend on the demo assembly or a global player singleton.

.. _evs-architecture--vehicle-composition:

Vehicle composition
-------------------

The hierarchy is an ownership boundary, not a requirement that every category have a dedicated ``GameObject``. Modules can live on appropriate owned children. The controller's registry determines participation; helper components such as a blade or a hand target may instead be advanced by their local owner.

Use the tree below as a responsibility map. For a new feature, first locate the owner that should call it. A new optional mechanic usually belongs in the module pipeline; a new audio channel belongs under ``Audio``; a new limb contact belongs under ``Passengers``. Adding another independent Unity callback is not necessary for every new component.

A vehicle root owns a ``VehicleController``, ``Rigidbody``, body collider and registered modules. ``WheelColliders`` belong to that ``Rigidbody``; child transforms can hold meshes, lights, controls, passengers and other modules. Discovery includes inactive children and stops at a nested ``VehicleController``.

``wheelSetup`` is the authored wheel configuration. ``Wheels`` exposes the controller-managed runtime adapters. ``Wheel`` visuals follow suspension/steering/spin; brake-caliper visuals follow suspension and steering without tire spin.

Logical organization, with representative components:

.. code:: text

   VehicleController
   |__ Controller
   |   |__ Input (IInput)
   |   |   |__ KeyboardDriveInput
   |   |   |__ ActionInput
   |   |   |__ InputBuffer / ExternalController
   |   |__ InputGate
   |   |__ ProfileSwitcher
   |__ Physics
   |   |__ Friction
   |   |__ WheelDynamics
   |   |__ TireCollision
   |   |__ Damage
   |   |__ MeshDeformation
   |__ Drive
   |   |__ Drive
   |   |   |__ Selected DriveProfile
   |   |__ Steering
   |   |__ Brakes / ParkingHold
   |   |__ Suspension / AntiRoll / ContactEnvelope
   |   |__ MotorcycleBalance
   |   |__ Tracks
   |__ Engine
   |   |__ Engine
   |   |__ Transmission
   |   |__ AutomaticGearbox / ManualGearbox
   |   |__ Clutch
   |   |__ Differential
   |   |__ TractionControl
   |   |__ FuelTank
   |__ Interior
   |   |__ SteeringWheelAnimator / YokeAnimator / SteeringStickAnimator
   |   |__ ThrottleAnimator
   |   |__ RearMirrors
   |   |__ Wipers
   |   |__ CarHud / AircraftHud
   |__ Exterior
   |   |__ Body
   |   |   |__ BodyPart
   |   |__ MovingPart
   |   |__ Lights
   |   |__ LandingGear
   |   |   |__ LandingGearPart
   |   |__ LandingGearSuspension
   |   |__ Propulsion / HoverVisuals
   |   |__ AircraftControlSurfaces
   |   |__ TrackVisuals
   |__ World
   |   |__ Passengers
   |   |   |__ PassengerSeat
   |   |   |   |__ PassengerBody
   |   |   |   |__ Passenger controller strategy
   |   |   |__ VehicleHandle
   |   |   |__ PassengerBehaviour
   |   |__ Coupler / Trailer
   |   |__ WaterInteraction
   |   |__ WeaponBarrel / RocketLauncher / ObjectDropper
   |__ Effects
       |__ Feedback / Events
       |__ Audio
       |   |__ EngineAudio
       |   |__ TireAudio
       |   |__ Other AudioModule channels
       |__ TireSmoke / ExhaustSmoke
       |__ Skidmarks

+------------+----------------------+----------------------------------------------------------------+
| Category   | Extension base       | Typical responsibilities                                       |
+============+======================+================================================================+
| Controller | ``ControllerModule`` | Input providers and profile/input routing                      |
+------------+----------------------+----------------------------------------------------------------+
| Physics    | ``PhysicsModule``    | ``Wheel`` dynamics, friction, tire contact and damage          |
+------------+----------------------+----------------------------------------------------------------+
| ``Drive``  | ``DriveModule``      | Pedals, steering, suspension and vehicle strategies            |
+------------+----------------------+----------------------------------------------------------------+
| ``Engine`` | ``EngineModule``     | ``Engine``, gearbox, clutch, differential and traction control |
+------------+----------------------+----------------------------------------------------------------+
| Interior   | ``InteriorModule``   | Cockpit animators, displays, mirrors and wipers                |
+------------+----------------------+----------------------------------------------------------------+
| Exterior   | ``ExteriorModule``   | ``Body`` parts, lights, landing gear and vehicle presentation  |
+------------+----------------------+----------------------------------------------------------------+
| World      | ``WorldModule``      | ``Passengers``, towing, water interaction and weapons          |
+------------+----------------------+----------------------------------------------------------------+
| Effects    | ``EffectsModule``    | ``Contact`` feedback, audio, particles and tire marks          |
+------------+----------------------+----------------------------------------------------------------+

Each category has an ``I<Category>Module`` contract and a controller-owned ``CategoryCore``. These cores are ordinary objects, not extra scene components.

.. _evs-architecture--physics-pipeline:

Physics pipeline
----------------

A fixed tick begins from one sampled intent. Mechanics resolve that intent progressively: input may request acceleration while braking or clutch policy temporarily reduces transmitted drive. Consumers should therefore choose deliberately between raw ``Command`` values and resolved outputs such as ``DriveDemand``, ``ServiceBrake`` and ``SteeringAngle``.

This is particularly important for presentation. A brake pedal may follow resolved service braking, a gear indicator follows accepted gear state, and tire effects follow contact/slip feedback. Reading raw keyboard state from each renderer would make alternate input providers behave differently even when they submit equivalent commands.

``IInput.ReadCommand → Command → execution phases → module Step → Telemetry/events``.

The controller samples one command per ``FixedUpdate``, clears transient wheel actuation, then advances enabled, profile-compatible modules. Every mechanic receives the same command and elapsed time. Ordering is:

1. ``ExecutionPhase`` dependency barrier.
2. The controller's category order within that phase.
3. A module's effective local order within its category. Equal orders retain registration/discovery order.

Phases cover ``Contact``, ``Transmission``, Braking, ``TrailerBraking``, ``Clutch``, Power, ``Differential``, ``Steering``, ``Drive``, ``Friction``, Assistance, ``Suspension``, Balance, Presentation, ``Coasting``, Parking, ``WheelDynamics``, ``Feedback`` and ``Collision``. They are library execution barriers, independent of Unity's script-order settings. A local order cannot move an engine before its braking/clutch dependencies.

``AfterPhysicsStep`` publishes the complete immutable telemetry snapshot after the pipeline. ``Impact`` copies collision data for deferred consumers; a live Unity ``Collision`` should only be used during its callback. Presentation reads actuator state, contact feedback and events rather than inferring physics from keyboard input.

.. _evs-architecture--membership-and-configuration:

Membership and configuration
----------------------------

Registration and unregistration rebuild immutable membership/order snapshots. The current physics tick retains its captured snapshot; membership/order edits affect the next tick. A disabled or destroyed component is skipped when execution reaches it.

``Configure(vehicle)`` may run repeatedly and in Edit Mode. Cache references and apply persistent settings there; do not assume a running simulation. ``TryApplyConfiguration`` validates wheels, applies persistent configuration and rebuilds ordering. ``RefreshModuleOrder`` only rebuilds scheduling, without reconfiguring wheels or resetting module state.

Use ``RegisterModule``, ``UnregisterModule``, ``AddModule<T>`` and ``DiscoverModules`` for membership. Unregistering removes physics-pipeline membership; disable an old component too when it owns frame callbacks, resources or subscriptions. Later discovery includes owned components again, so remove a retired component if it must not return.

.. _evs-architecture--nested-owners:

Nested owners
-------------

Nested ownership keeps specialized helpers from becoming unrelated top-level mechanics. An audio channel does not need to know category ordering, and a finger pose helper does not need to sample vehicle input. Its owner supplies the relevant context at the appropriate time.

When replacing an owner, inventory its local resources and children as well as its public methods. Scheduling replacement work without retiring old subscriptions or transform writers can leave two implementations active even though only one appears in the module registry.

-  **``Audio``** owns its local ``AudioModule`` channels, rendering them once per frame. Channels own their generated audio sources; the core controls mixer/spatial settings. Core disable suspends all its channels.
-  **``Passengers``** discovers seats, handles and passenger behaviours. Handles supply contact frames; the passenger core advances them and their occupants. Each seat owns occupancy, per-limb bindings and a controller-strategy instance.
-  **``Drive``** advances the selected serializable ``DriveProfile``. Profiles contain configuration; simulation history lives on the vehicle's modules.

Do not tick a registered module, owned handle or audio channel a second time from another update loop. See :doc:`Seats and handles </SeatsAndHandles>`, :doc:`Audio </Audio>` and :doc:`Drive profiles </DriveProfiles>`.

.. _evs-architecture--extending-a-system:

Extending a system
------------------

Derive from a category base for a new responsibility, or inherit a concrete built-in component for a compatible replacement. Public operations and state use virtual dispatch; protected lifecycle hooks and event publishers support custom implementations. Explicit assigned references remain authoritative. Registry lookup accepts classes and capability interfaces, with caller-owned lists for multiple providers.

The component authoring and ownership contracts are described in :doc:`Configuration </Configuration>`; lifecycle, inheritance, event and scheduling examples are in :doc:`Scripting </Scripting>`. Private solver caches and fixed nested-scheduling guards are implementation details.
