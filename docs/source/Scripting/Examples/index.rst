Scripting examples
==================

One hundred standalone examples in ten categories. Each example solves a small application task and includes setup, behavior, comments and a complete C# component. They complement the implementation chapters with UI adapters, policies, measurements and gameplay exercises.

.. rubric:: Before using an example

-  Save each component in the named ``.cs`` file under your own ``Assets`` scripts folder, outside the package. All examples use the ``VehicleDocumentationExamples.Cookbook`` namespace. If you use an assembly definition, reference ``EasyVehicleSystem.Runtime`` and the Unity modules your component needs.
-  Assign scene references before enabling a component. Event examples assume their source reference remains fixed while enabled: disable the component before replacing a source, then enable it again.
-  UI examples expose public methods for buttons, sliders or your own action system. They do not require a particular keyboard binding. Invoke Unity APIs on Unity’s main thread.
-  Each script owns only the request or presentation property described in its setup. Combine scripts deliberately: two input writers, beam policies or FOV writers can overwrite each other. Ordinary MonoBehaviours are not vehicle modules; the custom-module category explains installation and physics timing.
-  Interior animators here are vehicle-system control components, distinct from Unity’s skeletal Animator. Sources supply values; control animators move equipment; handles coordinate limbs.

.. rubric:: Categories

+-----------------------------------------------------+-----------------------+--------------------------------------------------------------------------------------+
| Category                                            | Examples              | Focus                                                                                |
+=====================================================+=======================+======================================================================================+
| :doc:`Commands and input <Input>`                   | 10                    | Adapters for UI, remote control and repeatable driving tests.                        |
+-----------------------------------------------------+-----------------------+--------------------------------------------------------------------------------------+
| :doc:`Configuration and recovery <Lifecycle>`       | 10                    | Runtime configuration, checkpoints and module availability.                          |
+-----------------------------------------------------+-----------------------+--------------------------------------------------------------------------------------+
| :doc:`Custom vehicle modules <Modules>`             | 10                    | Install these components through Add Module or your normal module registration flow. |
+-----------------------------------------------------+-----------------------+--------------------------------------------------------------------------------------+
| :doc:`Driving challenges and gameplay <Gameplay>`   | 10                    | Small challenge rules driven by authoritative telemetry.                             |
+-----------------------------------------------------+-----------------------+--------------------------------------------------------------------------------------+
| :doc:`Engine, fuel and boost <Powertrain>`          | 10                    | Gameplay policies around the existing engine and boost modules.                      |
+-----------------------------------------------------+-----------------------+--------------------------------------------------------------------------------------+
| :doc:`Exterior equipment <Exterior>`                | 10                    | Small policies for lights, wipers and moving model parts.                            |
+-----------------------------------------------------+-----------------------+--------------------------------------------------------------------------------------+
| :doc:`Interior data sources <Interior>`             | 10                    | Custom scalar sources plug into an interior animator’s data source field.            |
+-----------------------------------------------------+-----------------------+--------------------------------------------------------------------------------------+
| :doc:`Passengers and handle interactions <Handles>` | 10                    | Application-level gestures share HandleController ownership with normal controls.    |
+-----------------------------------------------------+-----------------------+--------------------------------------------------------------------------------------+
| :doc:`Presentation and diagnostics <Presentation>`  | 10                    | Observers for camera effects, trails and development tools.                          |
+-----------------------------------------------------+-----------------------+--------------------------------------------------------------------------------------+
| :doc:`Telemetry and measurements <Telemetry>`       | 10                    | Read completed physics snapshots for game rules and presentation.                    |
+-----------------------------------------------------+-----------------------+--------------------------------------------------------------------------------------+

.. rubric:: Example categories

.. toctree::
   :maxdepth: 1

   Input
   Lifecycle
   Modules
   Gameplay
   Powertrain
   Exterior
   Interior
   Handles
   Presentation
   Telemetry
