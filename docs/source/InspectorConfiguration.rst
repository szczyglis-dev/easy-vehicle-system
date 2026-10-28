.. _evs-inspectorconfiguration--inspector-controls-by-system:

Inspector controls by system
============================

Use a component's enabled checkbox to disable a whole responsibility. Use its behavior switches to change part of an enabled system. Configure drive profiles in Setup/ProfileSwitcher, and model-mounted helpers on their objects. Public authoring fields are configuration; transient read-only state is for observation.

+-------------------+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| System            | Main configuration choices                                                                        | Guide                                                                                    |
+===================+===================================================================================================+==========================================================================================+
| Controller/input  | Input source, category/local order, action references, analog/digital channel metadata            | :doc:`Configuration </Configuration>`, :doc:`Input </Input>`                             |
+-------------------+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| Wheels/suspension | Radius/width/mass, independent roles, springs/damping/travel, anti-roll, envelope/contact helpers | :doc:`Suspension </Suspension>`, :doc:`Tire collision </TireCollision>`                  |
+-------------------+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| Engine/gearbox    | RPM/torque curve, power/acceleration caps, ratios, shift timing and direction guards              | :doc:`Vehicle tuning </VehicleTuning>`, :doc:`Gearbox </Gearbox>`                        |
+-------------------+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| Clutch/assists    | Pedal/automatic operation, torque capacity/inertia, slip/stability policies                       | :doc:`Clutch </Clutch>`, :doc:`Traction control </TractionControl>`                      |
+-------------------+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| Brakes/parking    | Digital rise ramp, handbrake/rolling torque, slope release window, service/parking assistance     | :doc:`Gearbox </Gearbox>`, :doc:`Clutch </Clutch>`                                       |
+-------------------+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| Ground strategies | Wheel setup, motorcycle balance, tracked side slots/pivot/grip                                    | :doc:`Drive profiles </DriveProfiles>`, :doc:`Tracked </Tracked>`                        |
+-------------------+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| Air strategies    | Support/leveling, input/rate/attitude response, limits, gear protection, propulsion visuals       | :doc:`Ground, air and water </Media>`, :doc:`Aircraft </Aircraft>`                       |
+-------------------+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| Water             | Provider/fallback, hull sample dimensions, resistance/rocking/depth hold and effect switches      | :doc:`Water </Water>`, :doc:`Boat </Boat>`, :doc:`Submarine </Submarine>`                |
+-------------------+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| Passengers        | Body/controller, per-limb mode/anchor/handle, contact/hold, harness and ejection/reseat policy    | :doc:`Passengers </Passengers>`, :doc:`Seats and handles </SeatsAndHandles>`             |
+-------------------+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| Boarding          | Access point, speed/clearance checks, door references, animation profile and timing               | :doc:`Passenger access </PassengerAccess>`                                               |
+-------------------+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| Interior          | Control axes/ranges, interaction mode, wiper speed/audio, mirror budgets and HUD binding          | :doc:`Interior controls </InteriorControls>`, :doc:`Interior systems </InteriorSystems>` |
+-------------------+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| Body/damage       | Part IDs/hinges, damage/deformation/detachment switches, thresholds and collision-release policy  | :doc:`Damage </Damage>`, :doc:`Moving parts </MovingParts>`                              |
+-------------------+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| Lights            | Channel availability, sources/lenses, beam/indicator state, automatic/explicit overrides          | :doc:`Lights </Lights>`                                                                  |
+-------------------+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| Audio/effects     | Mixer/spatial response, clips/profiles, event mappings, particle assets/rates and bounded pools   | :doc:`Audio </Audio>`, :doc:`Particles </Particles>`, :doc:`Tire marks </Decals>`        |
+-------------------+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| Towing            | Attach distance/alignment, break policy, hitch motion, forwarded/detached brakes                  | :doc:`Towing </Towing>`                                                                  |
+-------------------+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+
| Weapons           | Firing/drop enable, cadence, payload references, launch/motor/blast and presentation              | :doc:`Weapons </Weapons>`                                                                |
+-------------------+---------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+

.. _evs-inspectorconfiguration--selected-policy-switches:

Selected policy switches
------------------------

-  **FuelTank:** ``consumeFuel`` and ``stopEngineWhenEmpty`` are independent. Turning consumption off keeps gauge/refuelling APIs; turn the empty-tank interlock off too if an empty tank should permit ignition.
-  **Coupler/Trailer:** configure startup attachment and joint-break policy independently of explicit Detach. Trailer service/handbrake forwarding and detached parking are separate.
-  **LandingGear:** ``preventGroundRetraction`` and its ground mask control the retraction interlock. Retraction can still depend on suspension alignment.
-  **PassengerSeat:** restraints configure release/ejection thresholds, delays, optional velocity and reseating on reset. Limb mode and hold settings determine each hand/foot's ownership.
-  **Damage/Rocket:** choose physical and visual effects independently. Explicit API actions can have different policy from collision-triggered actions; consult the relevant guide.

.. _evs-inspectorconfiguration--editors-and-subclass-configuration:

Editors and subclass configuration
----------------------------------

Root modules can be edited through the controller's grouped inspectors. **Show standalone module inspectors** exposes their ordinary Unity inspectors as well. Seats has a collapsible **Handles** group. These editor preferences do not change simulation membership or enabled state.

Specialized inspectors apply to component subclasses. Manually drawn inspectors show additional serialized subclass configuration under **Custom fields**. Use :doc:`Scripting </Scripting>` to override behavior rather than adding a second configuration path for an existing responsibility.
