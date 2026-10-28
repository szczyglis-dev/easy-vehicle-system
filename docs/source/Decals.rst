.. _evs-decals--tire-marks:

Tire marks
==========

``Skidmarks`` draws bounded wheel trails from vehicle contact feedback. Configure it independently of tire friction and damage.

.. _evs-decals--configure:

Configure
---------

1. Add Feedback and Skidmarks to the vehicle.
2. Assign the mark material and configure width, spacing, intensity and lifetime.
3. Set capacity for the amount of visible history your game needs.
4. Assign :doc:`surface profiles </Surfaces>` when materials need different mark colors or lifetimes.
5. Check sliding, loss of contact, teleport and surface changes.

Use ``ClearMarks()`` to clear the trails and ``SegmentCount`` to observe pool use. Trails break when contact or surface continuity is lost. Moving surfaces are not tracked after emission; use static ground for stable marks.

For buffer layout, upload bounds and ownership, see :doc:`Presentation reference </Scripting/Presentation>`.
