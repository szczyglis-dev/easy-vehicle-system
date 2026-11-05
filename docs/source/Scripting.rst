.. _evs-scripting--extend-and-integrate:

Extend and integrate
====================

To configure built-in systems, begin with :ref:`Basic Inspector workflow <evs-inspectorconfiguration--basic-inspector-workflow>` and the :ref:`Inspector-first guide index <evs-scripting-index--start-with-inspector-setup>`. Adding lights, suspension, clips, particles and ordinary model bindings does not require the custom implementation examples in this chapter.

Start with :doc:`Custom modules </Scripting/CustomModules>` for a complete module tutorial, or :doc:`Profiling and debugging </Scripting/ProfilingAndDebugging>` for captures and custom markers.

For km/h, mph or m/s authoring and readouts, see :doc:`Speed units </SpeedUnits>`.

Extend the package at the boundary that already owns the behavior you want to change. Public actions are the right tool for invoking existing behavior. A derived component changes an implementation. A capability interface lets consumers work with several implementations without knowing their concrete types.

The examples in this chapter show two common ways to customize the package: installing a new scheduled mechanic and replacing a narrow part of a built-in mechanic. Both preserve the surrounding vehicle lifecycle rather than copying the complete controller.

.. _evs-scripting--implementation-map:

Implementation map
------------------

+--------------------------+-------------------------------------------------------------------------+
| Class                    | Responsibility                                                          |
+==========================+=========================================================================+
| ``VehicleModule``        | Base registration/configuration/step contract for new mechanics.        |
+--------------------------+-------------------------------------------------------------------------+
| ``PhysicsModule``        | Category base used by the downforce example.                            |
+--------------------------+-------------------------------------------------------------------------+
| ``ModuleSetupAttribute`` | Optional installation/menu policy for custom module types.              |
+--------------------------+-------------------------------------------------------------------------+
| ``VehicleController``    | Public registration, lookup and reference-connection operations.        |
+--------------------------+-------------------------------------------------------------------------+
| ``Engine``               | Provides the virtual crank-torque hook used by the replacement example. |
+--------------------------+-------------------------------------------------------------------------+
| ``ModuleCatalog``        | Discovers eligible module implementations for setup tooling.            |
+--------------------------+-------------------------------------------------------------------------+

Part of the :doc:`Scripting Reference </Scripting/index>`. Namespace: ``EasyVehicleSystem``; reference the runtime assembly from your project's asmdef.

.. _evs-scripting--choose-the-smallest-integration-point:

Choose the smallest integration point
-------------------------------------

Start with the caller's need. If a UI button should start the engine, call its action; deriving an engine just to expose that button adds an unnecessary replacement. If an application needs a different torque calculation, a derived engine is appropriate. If several unrelated mechanics should expose a shared application reading, define a capability interface rather than inheriting them all from one concrete component.

Keep application-specific dependencies in adapters. A reusable vehicle mechanic should not discover the local player, UI canvas or network session itself. Pass a reference or feed commands/events across a small explicit boundary.

+---------------------------------+--------------------------------------------------------------+
| Goal                            | Use                                                          |
+=================================+==============================================================+
| Trigger an existing behavior    | Its public action or ``UnityEvent`` binding                  |
+---------------------------------+--------------------------------------------------------------+
| Observe state                   | Typed events or telemetry snapshots                          |
+---------------------------------+--------------------------------------------------------------+
| Supply controls                 | ``IVehicleInput``, ``InputBuffer`` or ``ExternalController`` |
+---------------------------------+--------------------------------------------------------------+
| Add a mechanic                  | A category ``VehicleModule`` subclass                        |
+---------------------------------+--------------------------------------------------------------+
| Alter an existing mechanic      | Its virtual operation in a derived component                 |
+---------------------------------+--------------------------------------------------------------+
| Add a movement family           | A serializable ``DriveProfile``                              |
+---------------------------------+--------------------------------------------------------------+
| Supply a hand/foot contact      | ``VehicleHandle``                                            |
+---------------------------------+--------------------------------------------------------------+
| Use another character framework | ``PassengerBody``, a seat strategy or ``AccessMotion``       |
+---------------------------------+--------------------------------------------------------------+
| Connect an ocean                | ``WaterProvider``                                            |
+---------------------------------+--------------------------------------------------------------+

Keep one owner for each responsibility. Replacing a mechanic requires updating explicit references and retiring the old implementation. Adding an observer does not.

.. _evs-scripting--add-a-mechanic:

Add a mechanic
--------------

Choose a category base for responsibility and a phase for dependencies. The downforce below is an assistance force, so it does not need to replace wheel drive or steering. It reads the configured vehicle's speed and applies acceleration to the root ``Rigidbody`` through ``Body``.

``ForceMode.Acceleration`` makes this example's strength an acceleration rather than a force in newtons. The threshold is expressed in km/h because it compares with ``SpeedKph``. State the same units in custom Inspector labels or tooltips so users do not have to infer them from implementation.

This component adds downforce in the Assistance phase. Add it through the controller's Custom module menu, or register an existing instance with ``RegisterModule``. A category base supplies category membership; ``Phase`` and ``ExecutionOrder`` select scheduling.

**Example:** ``SpeedDownforce.cs``

.. raw:: html

   <!-- example: SpeedDownforce.cs -->

.. code-block:: csharp

   using UnityEngine;
   using EasyVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       [AddComponentMenu("My Game/Vehicles/Speed Downforce")]
       public class SpeedDownforce : PhysicsModule
       {
           [Min(0)] public float acceleration = 2;
           [Min(0)] public float minimumSpeedKph = 30;
           public override ExecutionPhase Phase => ExecutionPhase.Assistance;
           public override int ExecutionOrder => 100;

           public override void Step(VehicleController vehicle, Command command, float dt)
           {
               if (vehicle.SpeedKph >= minimumSpeedKph)
                   vehicle.Body.AddForce(-vehicle.transform.up * acceleration,
                       ForceMode.Acceleration);
           }
       }
   }

The controller calls ``Step`` once per physics tick. Do not call it again from your own ``FixedUpdate``. Use ``Configure`` for owner-local references and persistent setup; it can run repeatedly, including in Edit Mode.

.. _evs-scripting--install-your-component-on-a-vehicle-step-by-step:

Install your component on a vehicle, step by step
-------------------------------------------------

A script must first be a Unity component, then participate in the package's module contract, and finally belong to this vehicle's registered module set. The three installation paths below use the same ``SpeedDownforce`` example. Choose one path for each intended instance; they do not require separate implementations of the mechanic.

.. _evs-scripting--1-prepare-a-discoverable-module:

1. Prepare a discoverable module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Save the example as ``SpeedDownforce.cs`` in your application's runtime scripts, outside an ``Editor`` folder. Let Unity finish compiling and resolve compilation errors before adding it.
2. Keep the component class public, concrete and non-generic. The script filename should match the component class name so Unity can attach it normally.
3. Derive from a category base such as ``PhysicsModule``, ``DriveModule``, ``EngineModule``, ``InteriorModule``, ``ExteriorModule``, ``WorldModule``, ``EffectsModule`` or ``ControllerModule``. Reference ``EasyVehicleSystem.Runtime`` if your application uses an asmdef.
4. Put repeatable setup in ``Configure(vehicle)`` and scheduled mechanic work in ``Step(vehicle, command, deltaTime)``. Choose ``Phase`` and ``ExecutionOrder`` for dependencies; do not add a second ``FixedUpdate`` that runs the same work.
5. Keep the script in your own assembly. The controller's menu places types from the package runtime assembly under **Base** and types from other assemblies under **Custom**.

The category base matters beyond its name. For example, ``PhysicsModule`` implements ``IPhysicsModule``; the Inspector uses that category interface to choose the menu group. Deriving only from ``VehicleModule`` and overriding ``Category`` does not supply the interface used by the menu. An ordinary ``MonoBehaviour``, or a class that only implements ``IVehicleModule`` without deriving from ``VehicleModule``, is not part of the controller's module discovery.

.. _evs-scripting--2-add-through-the-controllers-add-module-menu:

2. Add through the controller's Add module menu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Select the vehicle root that owns ``VehicleController``.
2. Open **Modules**, then **Add module...**.
3. Choose **Custom → Physics → Speed Downforce** for the example above. The category comes from its module contract, and the displayed component name comes from the class name.
4. Edit the component's acceleration and minimum speed. The custom component appears in the controller's corresponding module category; use its selection control to inspect the actual component.
5. Click **Apply vehicle configuration** to apply setup and run registered module configuration. Fix any reported vehicle/wheel validation error before checking.

The menu creates the ordinary module on the root, then rediscovers vehicle modules so it is included in the controller's list. Audio channels and passenger behaviors have additional owner-specific authoring steps; use their dedicated technical chapters when extending those systems. The menu operation is distinct from the final configuration step.

``AddComponentMenu`` controls Unity's regular **Add Component** menu. It does not define the controller's **Custom** path. A nonempty attribute, such as the one on ``SpeedDownforce``, is optional for normal module discovery.

.. _evs-scripting--3-add-manually-on-the-vehicle-root:

3. Add manually on the vehicle root
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Select the same GameObject as ``VehicleController``.
2. Use Unity's **Add Component** and select **My Game → Vehicles → Speed Downforce**, or drag ``SpeedDownforce.cs`` onto the object.
3. Return to the controller's **Modules** tab and click **Discover and order vehicle modules**.
4. Confirm that the instance appears under **Physics**, then set its configuration/references.
5. Click **Apply vehicle configuration**.

Discovery rebuilds the registry from the hierarchy; it does not call ``Configure`` on newly found modules. Applying configuration performs that setup. If you also need missing module/controller references filled, use the controller component's context menu **Connect available modules**, then apply configuration. Existing explicit references remain authoritative.

.. _evs-scripting--4-add-manually-on-a-child-object:

4. Add manually on a child object
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Create a child beneath the vehicle, for example ``Custom mechanics``.
2. Keep it beneath the intended ``VehicleController``. Do not add a second controller to that branch unless it is a separate vehicle.
3. Add ``SpeedDownforce`` to the child using **Add Component** or by dragging its script.
4. On the main controller, run **Discover and order vehicle modules**, then **Apply vehicle configuration**.
5. Configure any geometry or local references on the child component. ``Step`` still receives the owning vehicle; use ``vehicle.Body`` for forces on the chassis rather than expecting a Rigidbody on that child.

This is useful for organizing mechanisms or placing a component beside its own geometry. A child placement does not require a different base class or another registration component. Discovery includes inactive children, but their modules do not step until their GameObjects and components are active/enabled.

.. _evs-scripting--how-the-controller-discovers-and-runs-modules:

How the controller discovers and runs modules
---------------------------------------------

There are two different searches. The Inspector searches compiled types to populate **Add module**. The runtime controller searches component instances already attached to its hierarchy. A type appearing in the menu does not mean an instance has been installed, and an installed instance does not have to be offered by that menu to be discoverable.

``DiscoverModules()`` uses ``GetComponentsInChildren<VehicleModule>(true)``: it includes the root and all inactive/active descendants. It keeps an instance only when its nearest parent ``VehicleController``, including inactive parents, is this controller. A nested vehicle therefore owns its own branch; modules below it are excluded from the outer vehicle. Object names, hierarchy depth and the ``AddComponentMenu`` path do not determine ownership.

The controller orders discovered modules by effective local order and rebuilds category/phase scheduling. Startup ``Awake`` runs discovery followed by configuration, so components saved on the prefab are available without an application bootstrap script. The controller does not rescan the entire hierarchy every tick. A component added later through ``GameObject.AddComponent`` needs explicit registration or rediscovery.

+--------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| Operation                            | What it does                                                                                                                                                            | When to use it                                                                   |
+======================================+=========================================================================================================================================================================+==================================================================================+
| ``DiscoverModules()``                | Rebuilds membership from owned root/child instances and refreshes order; does not configure each found instance.                                                        | After assembling/reparenting a hierarchy or manually adding several components.  |
+--------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ``RegisterModule(instance)``         | Adds an existing instance, refreshes scheduling and immediately calls its ``Configure`` for this vehicle. An already registered instance is not added/configured again. | After creating one runtime component or explicitly installing an existing one.   |
+--------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ``AddModule<T>()``                   | Creates ``T`` on the controller's own GameObject and registers/configures it.                                                                                           | A new root-level runtime mechanic.                                               |
+--------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ``ConnectAvailableModules()``        | Runs discovery and fills missing compatible module/controller references; can select an input provider if none is assigned.                                             | Setup where installed components should find unassigned dependencies.            |
+--------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ``TryApplyConfiguration(out error)`` | Validates current vehicle setup, configures runtime wheels and all registered modules, and refreshes scheduling.                                                        | After changing setup that must be applied to native components or module caches. |
+--------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ``RefreshModuleOrder()``             | Rebuilds scheduling without searching for components or applying configuration.                                                                                         | Ordering changes among already registered modules.                               |
+--------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+

Being discovered and being executed are separate conditions. The controller must be enabled and valid; a module must be active/enabled and support the selected profile. ``SupportsProfile`` controls movement compatibility. Registered disabled modules still receive configuration, so setup should tolerate disabled and Edit Mode use. Use the :doc:`module lifecycle reference </Scripting/Modules>` for lookup, ordering and replacement details.

.. _evs-scripting--create-and-register-a-module-from-code:

Create and register a module from code
--------------------------------------

Call the following methods from your runtime spawn/setup flow after the vehicle itself is configured. Save the component beside ``SpeedDownforce.cs`` in the same example namespace. ``InstallOnRoot`` uses the combined controller API. ``InstallOnChild`` creates an owned child, sets its values, then registers that exact instance.

**Example:** ``CustomModuleInstallation.cs``

.. raw:: html

   <!-- example: CustomModuleInstallation.cs -->

.. code-block:: csharp

   using UnityEngine;
   using EasyVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class CustomModuleInstallation : MonoBehaviour
       {
           public VehicleController vehicle;

           public void InstallOnRoot()
           {
               if (!vehicle) return;
               vehicle.AddModule<SpeedDownforce>();
           }

           public void InstallOnChild()
           {
               if (!vehicle) return;
               var child = new GameObject("Custom downforce");
               child.transform.SetParent(vehicle.transform, false);
               var module = child.AddComponent<SpeedDownforce>();
               module.acceleration = 3;
               module.minimumSpeedKph = 40;
               vehicle.RegisterModule(module);
           }
       }
   }

Each call intentionally adds an instance. If the feature should be unique, find the intended existing instance before creating another. If several components are assembled together, an alternative is to finish authoring them, run ``ConnectAvailableModules()`` and then ``TryApplyConfiguration(out error)``. Do not assume ``TryApplyConfiguration`` will discover components that were never registered.

``RegisterModule`` is an explicit low-level registry operation, not an ownership search. Keep registered instances under the intended controller just as in the child example. Moving an already registered component between vehicles needs an explicit handover: unregister it from the old controller, reparent it, then register/configure it on the new one.

.. _evs-scripting--menu-visibility-and-installation-policy:

Menu visibility and installation policy
---------------------------------------

Most application modules need no metadata beyond a category base. Use ``ModuleSetupAttribute`` only when you want a specific setup policy. These choices are separate from discovery of components that already exist on the hierarchy.

+-----------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Declaration / condition                                                                 | Effect                                                                                                                              |
+=========================================================================================+=====================================================================================================================================+
| Public concrete category-module class in your runtime assembly                          | Eligible for normal Unity attachment and the controller's corresponding **Custom** category.                                        |
+-----------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``[AddComponentMenu("My Game/Vehicles/Speed Downforce")]``                              | Gives Unity's regular **Add Component** a path; does not change the controller's Custom category/name.                              |
+-----------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``[AddComponentMenu("")]``                                                              | Hides the type from the controller menu unless ``ModuleOnly = true`` opts it back in.                                               |
+-----------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``[ModuleSetup(ModuleOnly = true)]``                                                    | Allows a module hidden by an empty ``AddComponentMenu`` to appear in the controller menu.                                           |
+-----------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``[ModuleSetup(IncludeInFull = false)]``                                                | Excludes the type from automatic full setup/catalog installation; the Inspector's explicit **Add module** choice remains available. |
+-----------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``[ModuleSetup(EnabledByDefault = false)]``                                             | Disables a newly installed instance in full setup. It does not make every manually/menu-created instance start disabled.            |
+-----------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Abstract/open generic class, missing category interface or compilation/assembly problem | Not a usable normal Custom-menu entry; fix the type/assembly before checking hierarchy ownership.                                   |
+-----------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+

For a hidden optional module, ``[ModuleSetup(ModuleOnly = true, IncludeInFull = false)]`` combines manual controller-menu availability with exclusion from full setup. Do not add a registration list or modify package source just to make an ordinary custom module discoverable.

.. _evs-scripting--when-a-component-is-missing:

When a component is missing
---------------------------

If the class is absent from **Add module → Custom**, check compilation, runtime assembly placement, its concrete category base and any inherited ``AddComponentMenu``/``ModuleSetup`` metadata. If an instance is absent from the controller's list, check that it derives from ``VehicleModule``, belongs under this controller rather than a nested vehicle, and that discovery has run since it was added.

If the instance is listed but its ``Step`` does not run, check active/enabled state, ``SupportsProfile``, controller validation errors and whether its system uses a nested scheduler. ``VehicleHandle`` is a passenger-owned helper, not a top-level ``VehicleModule``: assign it through the seat/``Passengers`` system and follow :doc:`Handles </Scripting/Handles>`. Audio channels and passenger modules likewise keep their owner-specific update contracts; do not add an independent tick to force them to run.

.. _evs-scripting--extend-an-existing-operation:

Extend an existing operation
----------------------------

``virtual`` marks a method or property as replaceable through inheritance. ``override`` supplies the derived implementation while preserving dispatch through a base-typed reference. ``base`` calls the inherited implementation explicitly; use it when adding behavior around the existing algorithm.

``sealed`` prevents further inheritance of a class, or further overriding of a particular override. It is useful for fixed data/implementation contracts but is not an extension point. A public field is configurable data, not a virtual operation: hiding it in a subclass creates another field rather than changing what existing code reads.

The example below changes only crank-torque evaluation. It retains running-state handling, gearbox selection, clutch coupling and the rest of the engine lifecycle. This is easier to keep compatible than copying the entire engine into an application component.

Override a virtual operation and call base when retaining its work. This example scales the engine's evaluated crank torque without copying gearbox or clutch logic.

**Example:** ``LimitedTorqueEngine.cs``

.. raw:: html

   <!-- example: LimitedTorqueEngine.cs -->

.. code-block:: csharp

   using UnityEngine;
   using EasyVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class LimitedTorqueEngine : Engine
       {
           [Range(0, 1)] public float availablePower = 1;

           protected override float EvaluateCrankTorque(float rpm)
               => base.EvaluateCrankTorque(rpm) * availablePower;
       }
   }

This hook affects gearbox combustion paths; Direct drive uses ``Settings.motorTorque``. Use it in place of the configured ``Engine`` and update ``Transmission``, audio and other explicit engine references. The :doc:`module reference </Scripting/Modules>` explains registration, replacement and reference connection.

.. _evs-scripting--replacement-contracts:

Replacement contracts
---------------------

Install a replacement as a handover, not as an additional writer. Resolve the old implementation's explicit consumers, retire its scheduled/independent work and point those consumers at the replacement. Registry lookup does not automatically rewrite fields already assigned to a component.

Before changing a virtual operation, inspect what its callers rely on: return values, accepted-state changes, event timing and resource cleanup. A subclass can preserve a method signature while breaking its behavioral contract. Check the application-facing behavior, especially rejected requests and disable/re-enable boundaries.

-  Use ``override``, rather than hiding an operation with ``new``, for dispatch through built-in reference types.
-  Preserve base lifecycle cleanup when extending a component. A full replacement owns any cleanup, state and validation it omits.
-  Protected state setters and ``Raise<EventName>`` helpers support publishing replacement state. Calling a base action already publishes its own events.
-  Public fields configure components; they are not override points. Extra fields in a runtime subtype do not automatically persist through an inline field serialized as its concrete base type.
-  Specialized inspectors apply to subclasses. Additional serialized fields appear with the base inspector or its Custom fields area.

Fixed nested-scheduler entry points, value snapshots and private caches remain implementation contracts. See :doc:`Architecture </Architecture>` for ownership boundaries.

.. _evs-scripting--follow-a-worked-integration:

Follow a worked integration
---------------------------

Use :doc:`Events reference </Scripting/EventsReference>` to find notifications by name, owner and firing boundary.

:doc:`Input handover </Scripting/Input>`, :doc:`profile creation </Scripting/DriveProfiles>`, :doc:`handle contacts </Scripting/Handles>`, :doc:`custom passengers </Scripting/PassengerControllers>`, :doc:`water adapter </Scripting/Water>`, :doc:`events and telemetry </Scripting/Events>`, :doc:`timed interactions </Scripting/Interactions>` and :doc:`weapon control </Scripting/Weapons>` each provide a complete component example.

.. _evs-scripting--profiling-and-debugging:

Profiling and debugging
-----------------------

See :doc:`Profiling and debugging </Scripting/ProfilingAndDebugging>` for the capture workflow, built-in markers and a complete custom-marker example.
