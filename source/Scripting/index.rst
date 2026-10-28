.. _evs-scripting-index--scripting-reference:

Scripting reference
===================

Use the setup guide to build and check a system first. These chapters explain implementation contracts and provide complete C# components. Examples use the ``VehicleDocumentationExamples`` namespace; save a component in the named file, reference the runtime assembly and assign the listed scene references before use.

.. _evs-scripting-index--reading-a-technical-chapter:

Reading a technical chapter
---------------------------

Each topic starts with the system's purpose and the relationship between its parts. **Implementation map** names the classes responsible for each role. Individual component sections explain purpose and cooperation first, then configuration, technical behavior and integration points. They cover data flow, configuration authority and public operations together. Examples appear beside the behavior they illustrate, with setup, expected results and lifetime considerations. API identifiers use ``code formatting``; values include units or normalized conventions where those affect integration.

For a new extension, read :doc:`Architecture </Architecture>`, then :doc:`Scripting </Scripting>` and the relevant topic. For an existing integration, use the :doc:`API map </API>` to reach the owner of the operation. Each topic ends with a complete public method/event index, including package base contracts. The :doc:`API reference </API>` adds exact arguments, results, event payloads and declared state/configuration.

.. _evs-scripting-index--integrate-with-the-vehicle:

Integrate with the vehicle
--------------------------

+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| Task                                                                 | Read                                                                                                  |
+======================================================================+=======================================================================================================+
| Understand category/phase ownership                                  | :doc:`Architecture </Architecture>`                                                                   |
+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| Choose an extension point                                            | :doc:`Scripting </Scripting>`                                                                         |
+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| Install a custom module on the root or a child                       | :ref:`Step-by-step installation <evs-scripting--install-your-component-on-a-vehicle-step-by-step>`    |
+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| Find public operations                                               | :doc:`API map </API>`                                                                                 |
+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| Register, find or replace modules                                    | :doc:`Module lifecycle </Scripting/Modules>`                                                          |
+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| Supply commands and switch providers                                 | :doc:`Input </Scripting/Input>`                                                                       |
+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| Observe without polling physics                                      | :doc:`Events and telemetry </Scripting/Events>`                                                       |
+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| Add or switch movement modes                                         | :doc:`Drive profiles </Scripting/DriveProfiles>`                                                      |
+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| Write an independent movement profile and select it in the Inspector | :ref:`Profile from scratch <evs-scripting-driveprofiles--create-an-independent-profile-from-scratch>` |
+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+

.. _evs-scripting-index--events-and-subscriptions:

Events and subscriptions
------------------------

Use events to connect UI, audio and application rules to accepted vehicle state changes. Subscribe to the owning component with ``+=``, remove the same handler with ``-=``, and read current state once when binding. For continuous readings, use telemetry snapshots.

:ref:`Events and telemetry <evs-scripting-events--subscribe-to-a-components-events>` explains handler arguments, initial state, safe source changes and cleanup with a complete engine/seat example. It also covers :ref:`Inspector callbacks <evs-scripting-events--inspector-callbacks-and-c-events>`, which use ``UnityEvent.AddListener`` / ``RemoveListener`` instead of C# event syntax. Exact payloads and firing conditions are listed in the corresponding :doc:`API topic </API>`.

.. _evs-scripting-index--mechanics-and-environment:

Mechanics and environment
-------------------------

+----------------------------------------------------+------------------------------------------------------+
| Topic                                              | Reference                                            |
+====================================================+======================================================+
| ``Wheel`` authoring, native/envelope/solid contact | :doc:`Wheel contact </Scripting/WheelContact>`       |
+----------------------------------------------------+------------------------------------------------------+
| Springs, shock overrides and linkage               | :doc:`Suspension </Scripting/Suspension>`            |
+----------------------------------------------------+------------------------------------------------------+
| ``Engine``, gears, clutch, differential and TCS    | :doc:`Drivetrain </Scripting/DriveDynamics>`         |
+----------------------------------------------------+------------------------------------------------------+
| Boat resistance and rocking                        | :doc:`Boat </Scripting/Boat>`                        |
+----------------------------------------------------+------------------------------------------------------+
| Track sides and belt paths                         | :doc:`Tracks </Scripting/Tracks>`                    |
+----------------------------------------------------+------------------------------------------------------+
| Flight, gear and instruments                       | :doc:`Aircraft </Scripting/Aircraft>`                |
+----------------------------------------------------+------------------------------------------------------+
| Providers, depth hold and propeller presentation   | :doc:`Water </Scripting/Water>`                      |
+----------------------------------------------------+------------------------------------------------------+
| Physical grip versus effect surfaces               | :doc:`Surface feedback </Scripting/SurfaceFeedback>` |
+----------------------------------------------------+------------------------------------------------------+
| Physical hitch lifecycle                           | :doc:`Towing </Scripting/Towing>`                    |
+----------------------------------------------------+------------------------------------------------------+
| Hits, detachment and restoration                   | :doc:`Damage </Scripting/Damage>`                    |
+----------------------------------------------------+------------------------------------------------------+
| Aiming, projectiles, rockets and payloads          | :doc:`Weapons </Scripting/Weapons>`                  |
+----------------------------------------------------+------------------------------------------------------+

.. _evs-scripting-index--characters-and-presentation:

Characters and presentation
---------------------------

+-----------------------------------------------------+----------------------------------------------------------------+
| Topic                                               | Reference                                                      |
+=====================================================+================================================================+
| Occupancy, custom characters and controller factory | :doc:`Passenger controllers </Scripting/PassengerControllers>` |
+-----------------------------------------------------+----------------------------------------------------------------+
| Dynamic supports, release and collision policy      | :doc:`Passenger physics </Scripting/PassengerPhysics>`         |
+-----------------------------------------------------+----------------------------------------------------------------+
| Authored skeletal frames                            | :doc:`Anatomy </Scripting/Anatomy>`                            |
+-----------------------------------------------------+----------------------------------------------------------------+
| ``Contact`` targets and transfer actions            | :doc:`Handles </Scripting/Handles>`                            |
+-----------------------------------------------------+----------------------------------------------------------------+
| ``Finger`` fit, steering mapping and reservations   | :doc:`Grip solving </Scripting/GripSolving>`                   |
+-----------------------------------------------------+----------------------------------------------------------------+
| Animated boarding and reservations                  | :doc:`Passenger access </Scripting/PassengerAccess>`           |
+-----------------------------------------------------+----------------------------------------------------------------+
| Committed IK/Animator/custom gestures               | :doc:`Interactions </Scripting/Interactions>`                  |
+-----------------------------------------------------+----------------------------------------------------------------+
| Instruments, mirrors, wipers and fuel               | :doc:`Interior </Scripting/Interior>`                          |
+-----------------------------------------------------+----------------------------------------------------------------+
| Rotation/translation actions                        | :doc:`Moving parts </Scripting/MovingParts>`                   |
+-----------------------------------------------------+----------------------------------------------------------------+
| Channel output and indicator timing                 | :doc:`Lights </Scripting/Lights>`                              |
+-----------------------------------------------------+----------------------------------------------------------------+
| ``Audio`` sources and custom channels               | :doc:`Audio </Scripting/Audio>`                                |
+-----------------------------------------------------+----------------------------------------------------------------+
| Particle/mark resource ownership                    | :doc:`Presentation </Scripting/Presentation>`                  |
+-----------------------------------------------------+----------------------------------------------------------------+

.. toctree::
   :maxdepth: 1
   :caption: Scripting topics

   Aircraft
   Anatomy
   Audio
   Boat
   Damage
   DriveDynamics
   DriveProfiles
   Events
   GripSolving
   Handles
   Input
   Interactions
   Interior
   Lights
   Modules
   MovingParts
   PassengerAccess
   PassengerControllers
   PassengerPhysics
   Presentation
   SurfaceFeedback
   Suspension
   Towing
   Tracks
   Water
   Weapons
   WheelContact

