.. _evs-surfaces--ground-grip-and-tire-effects:

Ground grip and tire effects
============================

Configure physical grip and presentation separately. Changing a tire effect profile does not change the vehicle's traction.

.. _evs-surfaces--change-physical-grip:

Change physical grip
--------------------

1. Add **Surface** to the exact ground collider object.
2. Set Grip to scale the vehicle's base tire grip on that collider.
3. Check acceleration, braking and cornering with the same vehicle.

Surface lookup for physical grip uses the hit collider itself. A Surface only on its parent is not used by Friction.

.. _evs-surfaces--give-the-ground-sound-dust-and-marks:

Give the ground sound, dust and marks
-------------------------------------

1. Create a **Tire Surface Profile** asset from the Create menu.
2. Add **Tire Surface** to the collider object or a parent and assign the profile.
3. Assign tire audio, particle material and mark appearance; configure rolling activity if effects should appear without skidding.
4. Set Feedback's Default Surface for unmarked ground.
5. Check a transition between two ground types while rolling and skidding.

A nearer TireSurface overrides a parent mapping. A selected profile with an empty tire loop is silent. No profile uses the vehicle’s general effect settings.

For Terrain, put TireSurface on the TerrainCollider object and map its Terrain Layers to effect profiles. Refresh the terrain surface cache after changing painted layers at runtime. This mapping classifies effects; painted grip needs a custom friction integration if you require it.

.. _evs-surfaces--example-gravel:

Example: gravel
---------------

Use Surface on the ground collider for lower grip. Separately assign a TireSurfaceProfile with a gravel loop, rolling dust or granular particles, and loose marks. Tune the driving response before balancing these effects.

See :doc:`surface reference </Scripting/SurfaceFeedback>` for lookup precedence, terrain caching and feedback lifetimes.
