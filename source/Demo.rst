.. _evs-demo--demo:

Demo
====

Keep **Demo** selected in the Asset Store import window, or import it from Package Manager's Samples section when using UPM. Open ``Demo.unity`` in the imported folder. With the asset-package installation, open ``Demo/Demo.unity``.

.. _evs-demo--select-a-vehicle:

Select a vehicle
----------------

+-----+---------------+-------------------------------------------------------------------------------------------------+
| Key | Demo vehicle  | Example systems                                                                                 |
+=====+===============+=================================================================================================+
| F1  | Car           | Rear-wheel drive, physical occupants, opening body parts, damage, windows, road/hover switching |
+-----+---------------+-------------------------------------------------------------------------------------------------+
| F2  | Monster Truck | Large tires, all-wheel drive and modular suspension                                             |
+-----+---------------+-------------------------------------------------------------------------------------------------+
| F3  | Military 6×6  | Six wheel contacts and all-wheel drive                                                          |
+-----+---------------+-------------------------------------------------------------------------------------------------+
| F4  | Bus           | Rear drive, cabin controls and commercial audio                                                 |
+-----+---------------+-------------------------------------------------------------------------------------------------+
| F5  | Tractor       | Articulated Semi Trailer and independent trailer brakes                                         |
+-----+---------------+-------------------------------------------------------------------------------------------------+
| F6  | Motorcycle    | Assisted balance and physical rider                                                             |
+-----+---------------+-------------------------------------------------------------------------------------------------+
| F7  | Helicopter    | Rotor spool, flight assistance and pilot controls                                               |
+-----+---------------+-------------------------------------------------------------------------------------------------+
| F8  | Airplane      | Assisted flight, propeller and landing gear                                                     |
+-----+---------------+-------------------------------------------------------------------------------------------------+
| F9  | Drone         | Hover, tilting rotor mounts and RPM-driven rotors                                               |
+-----+---------------+-------------------------------------------------------------------------------------------------+
| 6   | Boat          | Buoyancy, rudder/helm, water effects and physical driver                                        |
+-----+---------------+-------------------------------------------------------------------------------------------------+
| 7   | Tank          | Tracked drive, turret and physical projectiles                                                  |
+-----+---------------+-------------------------------------------------------------------------------------------------+
| 8   | Jet           | Aerobatic flight, retractable gear, stores and cockpit gestures                                 |
+-----+---------------+-------------------------------------------------------------------------------------------------+
| 9   | Submarine     | Underwater propulsion, depth hold and dive controls                                             |
+-----+---------------+-------------------------------------------------------------------------------------------------+

Page Up / Page Down cycles through the vehicles.

.. _evs-demo--common-controls:

Common controls
---------------

+----------------------------+---------------------------------------------------------------------+
| Control                    | Action                                                              |
+============================+=====================================================================+
| W / S, A / D               | Ground driving, or profile-specific flight/water axes               |
+----------------------------+---------------------------------------------------------------------+
| Space                      | Ground handbrake or airplane wheel brakes                           |
+----------------------------+---------------------------------------------------------------------+
| I                          | Selected engine ignition                                            |
+----------------------------+---------------------------------------------------------------------+
| R                          | Reset selected vehicle/passenger pose                               |
+----------------------------+---------------------------------------------------------------------+
| Tab                        | Cycle Orbit, Interior, Cinematic, FREE PARENT and FREE LOOK cameras |
+----------------------------+---------------------------------------------------------------------+
| Mouse / wheel              | Camera look/orbit and zoom                                          |
+----------------------------+---------------------------------------------------------------------+
| Escape / click             | Release / capture pointer                                           |
+----------------------------+---------------------------------------------------------------------+
| N                          | Day/night lighting                                                  |
+----------------------------+---------------------------------------------------------------------+
| L / H                      | Headlights / high beams                                             |
+----------------------------+---------------------------------------------------------------------+
| J / K / V                  | Left indicator / right indicator / hazards                          |
+----------------------------+---------------------------------------------------------------------+
| X                          | Wipers where installed                                              |
+----------------------------+---------------------------------------------------------------------+
| U                          | Driving assists                                                     |
+----------------------------+---------------------------------------------------------------------+
| T, Q / E, numpad gear keys | Transmission mode, shifting and gear selection on ground vehicles   |
+----------------------------+---------------------------------------------------------------------+
| Left Shift                 | Ground-vehicle clutch                                               |
+----------------------------+---------------------------------------------------------------------+
| C                          | Tractor/trailer attachment                                          |
+----------------------------+---------------------------------------------------------------------+
| Backquote (~)              | Show/hide vehicle and control hint panels                           |
+----------------------------+---------------------------------------------------------------------+

.. _evs-demo--vehicle-controls:

Vehicle controls
----------------

+--------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| Vehicle                  | Controls                                                                                                                       |
+==========================+================================================================================================================================+
| Car                      | B: next drive profile (drive/hover); O: opening body parts; F: entry/exit; Y: cycle aiming hand; left mouse: fire while aiming |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| Airplane / Jet           | Shift/Ctrl: increase/decrease throttle; W/S: pitch; A/D: roll or taxi steering; Q/E: yaw; Space: wheel brakes; G: landing gear |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| Jet stores               | Enter: launch rocket; M: drop payload                                                                                          |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| Hover                    | Shift/Ctrl: ascend/descend; Q/E: strafe                                                                                        |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| Helicopter               | Shift/Ctrl: ascend/descend; use the displayed attitude/yaw bindings                                                            |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| Tank                     | Brackets: turret rotation; Insert/Delete: elevation; Enter: fire                                                               |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| Submarine                | W/S: thrust; A/D: turn; Shift/Ctrl: ascend/dive; Q/Z: pitch; Space: brake                                                      |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| External-control example | P: toggle the checkpoint-driving example                                                                                       |
+--------------------------+--------------------------------------------------------------------------------------------------------------------------------+

Reset restores the vehicle pose; it does not repair damage or recreate detached parts.

.. _evs-demo--cameras:

Cameras
-------

Tab cycles **Orbit → Interior → Cinematic → Free Parent → Free Look**. Orbit follows the vehicle, Interior uses its cabin mount, and Cinematic follows its heading. Free Parent moves relative to the vehicle; Free Look moves in world space.

Free-camera movement: numpad 8 forward, 2/5 backward, 4/6 sideways, 9/3 up/down. Arrow keys provide horizontal movement; Shift increases speed.

.. _evs-demo--reuse-the-examples:

Reuse the examples
------------------

The sample's Prefabs folder contains the example vehicle configurations. Scripts/Examples contains application integrations such as ``LandingGearSwitch``, ``AimingHandExample`` and ``DemoExternalControl``.

See :doc:`Getting started </GettingStarted>` to build a vehicle, :doc:`Scripting </Scripting>` to integrate your game, and :doc:`Demo resources </DemoResources>` for asset bindings and credits.
