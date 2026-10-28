.. _evs-passengers--passengers:

Passengers
==========

``Passengers`` manages a vehicle's seats and occupants. Each ``PassengerSeat`` stores its character, role, pose and controller configuration.

Before assigning a physical humanoid, follow :doc:`Prepare a humanoid ragdoll </HumanAnatomy>` to create its bodies, auto-fill its references and convert its anatomical joints.

.. _evs-passengers--add-an-occupant:

Add an occupant
---------------

1. Add **Vehicle Passengers** through **Modules → Add module → Base → World**.
2. Open **VehicleController → Seats** and add a Passenger Seat.
3. Assign a pre-placed body or a character prefab. Enable spawn-on-start on the seat and core for automatic spawning.
4. Choose a passenger-controller mode from the table below.
5. Place ``spineAnchor`` at the seated pelvis, with +Y up and +Z forward. Assign the limb and exit targets.
6. For a humanoid, configure bone mapping and anatomical joints on the character. Review Auto-fill results before saving the rig.
7. Use **Preview seated pose** to check fit, then check occupancy and vehicle motion in Play Mode.

A pre-placed body takes priority over the prefab. Call ``RefreshPassengers()`` after adding or removing seats at runtime.

.. _evs-passengers--choose-a-controller:

Choose a controller
-------------------

=============== ===================================================
Mode            Pose ownership
=============== ===================================================
Ragdoll Physics Dynamic character supported by physical restraints.
Animator        Character animation.
Animator + IK   Animation with configured limb IK overlays.
Attach Only     Character attachment without humanoid solving.
Custom          Application-owned attachment, pose and motion.
=============== ===================================================

Use ``SetPassengerController`` to switch modes. Seat roles classify occupants; they do not assign vehicle input authority.

.. _evs-passengers--fit-and-support-the-character:

Fit and support the character
-----------------------------

Use **Seated pose** to adjust pelvis, backrest and limb targets. Keep contacts within anatomical reach. In Play Mode, **Apply seated tuning** rebuilds the occupied pose; save persistent edits outside Play Mode.

Configure pelvis/chest support, travel and damping under **Advanced → Fine Tuning**. Increase support gradually and check idle, acceleration and braking. For hand and foot ownership, grips and pins, see :doc:`Seats and handles </SeatsAndHandles>`. For joint preparation, see :doc:`Anatomical calibration </HumanAnatomy>`.

A hand can use a fixed grip, a compliant rest or Free mode. The :ref:`passenger physics reference <evs-scripting-passengerphysics--seated-fitting-and-hand-rests>` describes their parameters, angular support and settling behavior.

.. _evs-passengers--occupancy-and-entryexit:

Occupancy and entry/exit
------------------------

Use ``Spawn()`` for the configured body or ``TryEnter()`` for an existing character. Use ``TryExit()`` for normal exit and ``Eject()`` for physical release. Disabling the seat/core releases its occupant; the application owns detached characters and their lifetime.

Subscribe to ``Entered``, ``Exited`` and ``ControllerChanged`` for gameplay integration. Use :doc:`Passenger access </PassengerAccess>` for animated boarding, walking and door coordination. See the :doc:`API reference </API>` for programmatic occupancy controls.

.. _evs-passengers--collision-and-tilt-response:

Collision and tilt response
---------------------------

Under **Damage feedback**, enable hand/foot release or whole-passenger ejection and set the collision force, speed and tilt thresholds. Check these with your character mass and vehicle physics. Limb release and whole-body ejection have separate settings.

Configure collision exclusions and reseating/reset behavior for your game. The :doc:`passenger physics reference </Scripting/PassengerPhysics>` documents threshold calculations, release latches, collision restoration and ragdoll state.

.. _evs-passengers--extend-the-system:

Extend the system
-----------------

Derive from ``PassengerBehaviour`` for additional seated behavior, ``PassengerBody`` for another body type, or supply a passenger controller through the seat factory. For application-owned characters use **Custom** with ``CustomPassengerBody`` and handle the occupancy/reset events. See :doc:`Scripting </Scripting>` for contracts and examples.
