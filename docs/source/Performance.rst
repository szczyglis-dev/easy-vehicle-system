.. _evs-performance--performance-tuning:

Performance tuning
==================

Profile the number of active vehicles, occupants and visible effects expected in the game. Include dynamic passengers, mirrors and damage when measuring the cost of your fleet.

.. _evs-performance--establish-a-baseline:

Establish a baseline
--------------------

1. Measure movement with one vehicle and effects disabled.
2. Add the intended occupants and record physics cost.
3. Enable mirrors, particles and audio one system at a time.
4. Repeat with the expected active fleet in a player build.

Keep the workload and camera comparable when measuring a change.

.. _evs-performance--reduce-the-largest-cost-first:

Reduce the largest cost first
-----------------------------

+--------------------------+-------------------------------------------------------------------------------+
| Cost                     | Practical controls                                                            |
+==========================+===============================================================================+
| Wheel/contact physics    | Active vehicles, contact sample counts, collider complexity, physics timestep |
+--------------------------+-------------------------------------------------------------------------------+
| Physical passengers      | Active occupants, character colliders/joints, solver settings                 |
+--------------------------+-------------------------------------------------------------------------------+
| Mirrors                  | View range, resolution, refresh rate and renders-per-frame budget             |
+--------------------------+-------------------------------------------------------------------------------+
| Particles and tire marks | Emission, distance culling, lifetime and bounded capacities                   |
+--------------------------+-------------------------------------------------------------------------------+
| Damage/debris            | Readable mesh complexity, part boundaries and debris lifetime                 |
+--------------------------+-------------------------------------------------------------------------------+

Prepare grips during authoring or binding. Reuse command buffers and unsubscribe observers when disabled. Disable unused systems deliberately; changing a visible material alone does not remove physics work.

The :doc:`Scripting Reference </Scripting/index>` explains ownership and update cost per system.
