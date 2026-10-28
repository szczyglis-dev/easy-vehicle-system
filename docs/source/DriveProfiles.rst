.. _evs-driveprofiles--vehicle-types-and-drive-strategies:

Vehicle types and drive strategies
==================================

.. _evs-driveprofiles--choose-a-drive-mode:

Choose a drive mode
-------------------

Select the vehicle root and open **VehicleController → Setup → Drive mode**. Choose the mode that matches its movement, then configure the vehicle settings, wheels and optional modules. Each vehicle stores its own configuration. Choosing a different mode initializes its settings; subsequent configuration and entering Play Mode preserve your authored tuning.

+--------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Drive mode         | Use and behavior                                                                                                                |
+====================+=================================================================================================================================+
| Wheeled            | Cars, buses, trucks and other wheel vehicles. Uses engine, gearbox, differential and per-wheel steering, drive and brake roles. |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Motorcycle         | Two-wheel vehicles with configurable balance and lean assistance.                                                               |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Tracked            | Left/right track drive, differential turning and stationary pivot turns.                                                        |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Hover              | Ground clearance support, forward thrust, lateral strafe and assisted attitude.                                                 |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Helicopter         | Rotor-powered lift, horizontal movement, attitude assistance and optional altitude hold.                                        |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Airplane           | Assisted wing flight, takeoff/landing and ground steering.                                                                      |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Aerobatic Airplane | Aircraft with body-rate controls for rolls, loops and inverted flight.                                                          |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Jet                | Jet flight with aerodynamic drag, lift and body-rate controls; combine with aircraft gear and presentation modules.             |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Boat               | Surface buoyancy, hull resistance, powered thrust and rudder steering.                                                          |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Submarine          | Underwater displacement, forward/reverse thrust, vertical thrusters and depth/trim control.                                     |
+--------------------+---------------------------------------------------------------------------------------------------------------------------------+

Use **Wheeled** for different road vehicle models and tune mass, gearing, suspension and grip per vehicle. The Car in the supplied **Demo** scene also demonstrates a separate Hover configuration. For a towed, unpowered vehicle, use the Trailer setup with its brake and hitch configuration; see :doc:`Towing </Towing>`.

Keep a ``Drive`` component registered to run the selected mode. Assign a sound profile through its audio settings as needed. See :doc:`Ground, air and water </Media>` for controls and transitions.

.. _evs-driveprofiles--configure-the-selected-mode:

Configure the selected mode
---------------------------

Apply the mode's vehicle settings, then configure its supporting systems:

-  Ground: wheel roles, suspension, gearbox and differential.
-  Motorcycle: wheel setup and MotorcycleBalance.
-  Tracked: left/right track slots and optional link animation.
-  Air: thrust, controls and landing gear.
-  Water: hull contact and water provider.

See :doc:`Ground, air and water </Media>` for transitions and presentation, or the individual topic guides in the :doc:`documentation index </Introduction>`.

.. _evs-driveprofiles--add-a-custom-mode:

Add a custom mode
-----------------

Derive a serializable class from ``DriveProfile`` or a built-in profile. Override its behavior and initial settings as required. Custom concrete profiles appear automatically in the Drive mode selector after compilation. See :ref:`Create an independent profile from scratch <evs-scripting-driveprofiles--create-an-independent-profile-from-scratch>` for a complete example and setup, or :ref:`derive from a movement family <evs-scripting-driveprofiles--derive-from-a-movement-family>` to extend built-in handling.
