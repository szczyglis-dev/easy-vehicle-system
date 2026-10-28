.. _evs-configuration--vehicle-configuration:

Vehicle configuration
=====================

.. _evs-configuration--add-a-vehicle-or-component:

Add a vehicle or component
--------------------------

Select a scene GameObject or an object in Prefab Mode, then use **Tools > EasyVehicleSystem > Add Vehicle**. Choose a :doc:`drive profile </DriveProfiles>` for the vehicle.

Setup adds the profile's relevant mechanics, input adapter and presentation components. Existing owned WheelColliders can populate Wheel Setup; review every role and reference. You must supply body colliders, model geometry, hinges, seat/control anchors, light objects, effect outlets and other model-specific bindings.

Repeating the same preset preserves existing tuning/references and adds missing components. Choosing a different profile initializes that profile and its initial vehicle Settings. Setup changes support grouped Undo. Open prefab assets in Prefab Mode before using scene setup tools.

Use **Component > EasyVehicleSystem** or **Tools > EasyVehicleSystem > Add Component** for model-mounted helpers and standalone components. The controller's **Add module** menu adds registered mechanics; custom Module subclasses appear under **Custom**. Handles are configured under Seats rather than the module scheduler.

.. _evs-configuration--controller-tabs:

Controller tabs
---------------

+---------+------------------------------------------------------------------------------------+
| Tab     | Purpose                                                                            |
+=========+====================================================================================+
| Setup   | Body/input references, drive profile, vehicle Settings and module copy/paste/reset |
+---------+------------------------------------------------------------------------------------+
| Wheels  | Central Wheel Setup list, discovery and per-wheel geometry/roles                   |
+---------+------------------------------------------------------------------------------------+
| Seats   | Passenger core, seats, occupants and a collapsible **Handles** group               |
+---------+------------------------------------------------------------------------------------+
| Modules | Category groups, local/category ordering and embedded module inspectors            |
+---------+------------------------------------------------------------------------------------+
| Effects | Optional presentation systems and audio channels                                   |
+---------+------------------------------------------------------------------------------------+
| Live    | Telemetry and available runtime controls                                           |
+---------+------------------------------------------------------------------------------------+

Click **Apply vehicle configuration** after persistent configuration or wheel-geometry changes. Validation rejects missing/duplicate wheel colliders and wheels owned by another Rigidbody. Non-wheel profiles can use an empty list.

.. _evs-configuration--coordinate-system-and-units:

Coordinate system and units
---------------------------

Keep the root at unit scale, facing local +Z with +Y up. Put imported mesh scaling on visual children where practical. Mass is kilograms; distance/travel is metres; torque is N·m; rates and angular limits use the units shown by each field. ``settings.centerOfMass`` is an explicit local center-of-mass position relative to the root.

.. _evs-configuration--wheel-setup:

Wheel Setup
-----------

For a complete first-time walkthrough, including adding **Wheel** to each tire object, see :ref:`Create your first wheel vehicle <evs-gettingstarted--create-your-first-wheel-vehicle>`.

Each entry supplies its WheelCollider, wheel visual and optional caliper visual; availability; Steer, Drive, Brake and Handbrake flags; radius, width and mass; and steering, drive and braking multipliers. Wheel count is configurable. Negative steering multipliers support counter-steering axles. Driven-wheel weights control base torque allocation.

Author through Wheel Setup and read the runtime adapters through ``Wheels``. Each WheelCollider must belong to this vehicle’s Rigidbody and occur once in the list. Scene gizmos preview tire radius/width from the authoring data.

:doc:`Contact envelope </ContactEnvelope>`, :doc:`Tire collision </TireCollision>`, :doc:`Suspension </Suspension>` and :doc:`Traction control </TractionControl>` explain the corresponding optional mechanics.

.. _evs-configuration--configure-modules-independently:

Configure modules independently
-------------------------------

Use a component's enabled checkbox to stop its scheduled behavior, and internal switches for individual features. Existing native settings or already detached objects may persist; disabling a script is not a full vehicle reset. Root modules have embedded inspectors; **Modules > Show standalone module inspectors** controls whether their ordinary Unity inspectors are also shown. Child components remain available on their own objects. The preference does not change enabled state.

Audio channels are grouped beneath Audio. Passenger behaviours are owned by Passengers. If their parent is absent, orphaned components are shown in a **parent missing** group. Nested vehicles do not inherit a parent's core.

Choose execution phase/local order in custom code when required. Inspector local-order overrides and category order can be applied without resetting mechanics through ``RefreshModuleOrder()``. See :doc:`Architecture </Architecture>`.

.. _evs-configuration--connect-references:

Connect references
------------------

Assign model geometry, control targets and assets explicitly. ``ConnectAvailableModules()`` fills missing local module/controller references while preserving explicit assignments. For automatic setup policies and custom modules, see :doc:`Scripting </Scripting>`.

.. _evs-configuration--copy-paste-and-reset:

Copy, paste and reset
---------------------

**Copy modules** captures the controller and its owned Module components, including disabled and child modules. **Paste modules** replaces the destination module layout/settings and remaps vehicle-local references to corresponding destination objects. Shared assets/external references stay shared; missing destinations stay empty. Geometry, nested vehicles and unrelated components are not copied. Missing module holders can be created without duplicating a model.

These actions are available outside Play Mode and support Undo. The clipboard lasts until scripts reload. **Reset data** asks for confirmation, restores component defaults and clears authored references while keeping component layout and unrelated objects. Unity's ordinary component Copy applies to that component alone.

See :doc:`Inspector controls </InspectorConfiguration>` for subsystem settings and :doc:`Vehicle tuning </VehicleTuning>` for physical tuning.
