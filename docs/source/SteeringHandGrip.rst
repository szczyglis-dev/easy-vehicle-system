.. _evs-steeringhandgrip--fit-hand-grips:

Fit hand grips
==============

Configure finger mapping and palm calibration on the character before fitting the control. Keep contact anchors within reach and use positive uniform scale on solving pivots.

.. _evs-steeringhandgrip--steering-wheel-or-yoke:

Steering wheel or yoke
----------------------

1. Add SteeringWheelHandle or YokeHandle to the animated pivot and assign it to the seat's hands.
2. Set the rim centerline radius and tube thickness. Use Custom Rim for an irregular centerline.
3. Set the left/right contact locations and approach direction.
4. With a pre-placed humanoid, run **Preview configured hand contacts**.
5. Inspect contact frames and finger penetration; adjust palm thickness, pad radius and anchors as needed.

Set ``steeringWheelRotationAtFullLock`` to the steering column's degrees per side. Road-wheel steering angle is configured separately. See the :ref:`angle mapping <evs-scripting-gripsolving--steering-angle-mapping>` for conversions.

.. _evs-steeringhandgrip--motorcycle-handlebar:

Motorcycle handlebar
--------------------

Add MotorcycleHandle to the animated handlebar. Assign left/right grip center transforms, radius and length, then assign it to the seat's hands. Local X runs along each tube; +Y points from the palm toward its center.

Use **Prepare hand grip** after changing geometry or character calibration, then save the prepared pose. Prepare spawned character variants before runtime; handlebar fitting is an editor operation. See :ref:`prepared poses <evs-scripting-gripsolving--geometry-and-binding>`.

.. _evs-steeringhandgrip--sticks-throttles-and-fixed-grips:

Sticks, throttles and fixed grips
---------------------------------

On a compatible handle, enable Adaptive Grip, set Grip Diameter and orient the palm anchor. Run the seated grip preview. Use :doc:`Seats and handles </SeatsAndHandles>` for limb binding and motion setup.

.. _evs-steeringhandgrip--regrip-and-troubleshooting:

Regrip and troubleshooting
--------------------------

**Allow Hand Regrip** controls repositioning during steering. **Vary Grip With Steering** controls pressure/opening gestures. Disable the latter for a constant wrapped finger pose.

If the hand cannot reach, correct the seat or target position. If fingers intersect the mesh, check mapping, grip dimensions and palm calibration. Recheck full travel after each adjustment.

The :doc:`grip reference </Scripting/GripSolving>` describes fitting, hand ownership and contact planning. :doc:`Anatomical calibration </HumanAnatomy>` covers the character's joint limits.
