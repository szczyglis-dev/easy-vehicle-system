.. _evs-movingparts--move-a-model-part:

Move a model part
=================

Use MovingPart for a configurable hinge, turret axis, window or slider. BodyPart is the alternative when you need an identified opening body part with its opening/physical-hinge policy.

.. _evs-movingparts--configure-motion:

Configure motion
----------------

1. Add MovingPart under the vehicle and assign the transform to move.
2. Place the part in its neutral pose and capture that pose.
3. Choose Rotation or Translation.
4. For rotation, assign the hinge/axis, angular limits and speed. For translation, set direction, space, metre limits and speed.
5. Preview both ends and check collision clearance throughout travel.

Choose Parent translation space for a slider that should follow a moving door, World for a global direction, or Anchor for an independent direction frame. Do not use the moving object or its descendant as its own neutral anchor.

.. _evs-movingparts--operate-it:

Operate it
----------

Connect held input to movement and release it when the button is released. Use a target position/angle for open/close actions, or AimAt for an allowed aiming axis. Disabling motion pauses at the current pose; detached debris stops accepting model motion.

For a hold-button window, combine lower/raise input into a signed value. The :doc:`moving-part reference </Scripting/MovingParts>` provides a complete UI binding and explains immediate versus target commands, scaling and state.
