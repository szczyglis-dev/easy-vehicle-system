.. _evs-passengeraccess--entering-and-exiting-vehicles:

Entering and exiting vehicles
=============================

Use SeatAccess and PassengerAccess for animated entry/exit coordinated with a seat and optional door. For immediate occupancy changes, use PassengerSeat's ``TryEnter`` and ``TryExit``.

.. _evs-passengeraccess--configure-access:

Configure access
----------------

1. Add SeatAccess to the seat and assign its PassengerSeat and optional BodyPart door.
2. Create an ``outside`` marker at the standing feet position. Set its heading and configure ground projection if needed.
3. Set admission distance, vehicle-speed limits, clearance capsule/mask and door timeout.
4. Create an **Access Animation Profile** and assign it to the seat.
5. Configure PassengerAccess and a compatible motion adapter on the character.
6. Check entry, exit, blocked space and cancellation before connecting player input.

.. _evs-passengeraccess--bind-animations:

Bind animations
---------------

The profile needs an Animator Controller/layer, standing/seated/enter/exit state paths, entry/exit triggers and four matching Humanoid reference clips. Use single-clip access states matching the references.

Configure clip ranges, playback speed, transition allowance and completion timeout. Use the profile's door event bindings when an animation should open or close the door. The Inspector reports missing paths, parameters and clips.

For import settings, root motion, timing and event requirements, see the :doc:`access reference </Scripting/PassengerAccess>`.

.. _evs-passengeraccess--request-and-observe-access:

Request and observe access
--------------------------

Call ``PassengerAccess.TryEnter(seatAccess)`` or ``TryExit()``. A true return value means the request was admitted; observe completion/cancellation before restoring application control. Call ``Cancel()`` when abandoning the action.

Seat occupancy and animation completion occur at different points. The :ref:`lifecycle reference <evs-scripting-passengeraccess--cancellation-and-extension>` describes reservations, clearance and cancellation. Derive from AccessMotion to integrate another character or animation system.
