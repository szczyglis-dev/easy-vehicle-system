.. _evs-damage--opening-parts-and-collision-damage:

Opening parts and collision damage
==================================

Configure opening motion first, then add damage boundaries. BodyPart can operate without collision damage, and a damage boundary need not be an opening hinge.

.. _evs-damage--add-a-door-or-hatch:

Add a door or hatch
-------------------

1. Put BodyPart on an independent hinge pivot and place its moving geometry/colliders beneath it.
2. Set a unique, case-sensitive ID, axis and opening angle.
3. Choose animated or physical hinge movement. Tune mass, spring/damper and closed latch if physical.
4. Add it to **Body → Parts**.
5. Check full travel and chassis clearance before adding passengers or detachment.

Use simple collision proxies. Keep structural geometry outside a moving group. A released part remains physics-owned; opening it does not reattach it.

.. _evs-damage--add-collision-damage:

Add collision damage
--------------------

1. Add Damage and MeshDeformation to the vehicle.
2. Add DamagePart at each intended damage/detachment boundary and assign those parts on Damage.
3. Keep the root chassis outside detachable groups.
4. Tune minimum impact speed, affected radius and part multipliers.
5. For dents, enable Read/Write on supported MeshFilter meshes and provide enough vertices.
6. Check a moderate impact, a disabled response and a detached part separately.

Damage, deformation and detachment switches are independent. Zero deformation/detachment multipliers suppress the corresponding collision response. Disabling future damage does not undo existing dents/debris.

.. _evs-damage--repair-and-game-rules:

Repair and game rules
---------------------

Decide what repair means in the game: restoring visual shape, resetting health, rebuilding a missing part or respawning the whole vehicle. The package exposes those lower-level actions; position reset is not a full repair/rearm operation.

Use accepted damage events for lamps, health or effects. See :doc:`damage reference </Scripting/Damage>` for ID actions, event timing, scripted impacts and restoration limits.
