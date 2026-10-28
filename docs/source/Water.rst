.. _evs-water--water-providers-and-effects:

Water providers and effects
===========================

Use a water provider to share water height, surface normal and current between vehicle physics, water audio and particles. The provider can use the bundled surface or integrate your own ocean system.

.. _evs-water--set-up-a-water-surface:

Set up a water surface
----------------------

1. Add ``WaterSurface`` to a water GameObject. Set its position to the mean water level and configure ``size`` for the usable bounds.
2. Assign a ``WaterStyle`` to configure waves, ripples, color and foam. Assign ``materialOverride`` for rendering, or keep the material on your authored renderer.
3. Enable ``generateGrid`` to create the surface mesh, or disable it to use your own mesh. Adjust ``gridCellSize`` to balance visual detail and mesh cost.
4. Keep solid colliders off the visible water plane when buoyancy is responsible for support.
5. Add ``WaterInteraction`` to the vehicle, assign the provider and set ``hullHalfSize`` to its contact half-width and half-length in metres.
6. Configure the Boat or Submarine drive mode. Check the water bounds as well as the surface height.

Without a style, WaterSurface samples flat water. Without a material override it uses the renderer's authored material. Rendering and sampling are independently configurable.

.. _evs-water--enable-or-disable-interaction:

Enable or disable interaction
-----------------------------

+-------------------------------------------------+---------------------------------------------------------------------------+
| Setting                                         | Effect                                                                    |
+=================================================+===========================================================================+
| ``WaterSurface.waterEnabled``                   | Enables sampling and the surface as a whole.                              |
+-------------------------------------------------+---------------------------------------------------------------------------+
| ``WaterSurface.renderSurface``                  | Controls rendering while leaving water sampling available.                |
+-------------------------------------------------+---------------------------------------------------------------------------+
| ``animateWaves``                                | Controls animated wave displacement.                                      |
+-------------------------------------------------+---------------------------------------------------------------------------+
| ``reflectionsEnabled``, ``depthEffectsEnabled`` | Control optional surface rendering features.                              |
+-------------------------------------------------+---------------------------------------------------------------------------+
| ``WaterInteraction.waterInteractionEnabled``    | Enables water interaction for that vehicle, including buoyancy.           |
+-------------------------------------------------+---------------------------------------------------------------------------+
| ``useProfileFallback``                          | Allows the drive profile's plane and bounds when no provider is assigned. |
+-------------------------------------------------+---------------------------------------------------------------------------+

An explicitly assigned provider that is disabled or reports dry space does not fall back to another invisible water surface. Keep provider bounds, visible geometry and vehicle settings consistent.

.. _evs-water--add-audio-and-particles:

Add audio and particles
-----------------------

Add ``BoatWaterAudio`` for water sounds and ``BoatWaterParticles`` for propeller spray, wake and hull-entry splashes. Both use WaterInteraction's contact and water-relative velocity.

1. Assign audio clips and spray/foam materials or custom particle prefabs.
2. Set ``motorOutlet`` or ``sternOffset`` to the propulsion outlet.
3. Configure ``fullEffectSpeed``, channel rates and entry thresholds for the hull.
4. Set particle budgets and distance culling for your target hardware.

Use ``waterSoundsEnabled`` and ``waterParticlesEnabled`` for independent sound/visual switches. The particle channels also expose ``propellerEnabled``, ``wakeEnabled`` and ``splashesEnabled``. Turning these off does not disable buoyancy.

``propellerPrefab``, ``wakePrefab`` and ``splashPrefab`` replace individual visual channels. Custom child systems and sub-emitters need their own budgets. Motor spray follows power and throttle; wake can continue while coasting. Hull splashes follow local water-entry velocity.

Use ``hullRipplesEnabled`` and ``hullRippleRate`` for low-speed surrounding ripples. ``wakeEnabled`` controls both wake and ripples. ``runningSprayFactor`` adds speed-dependent bow spray. Tune these alongside the entry thresholds rather than changing the buoyancy settings to adjust appearance.

.. _evs-water--use-another-ocean-or-river:

Use another ocean or river
--------------------------

Assign a WaterProvider adapter for that system to the vehicle's WaterInteraction. Keep the provider's samples aligned with the visible water and use compatible particle materials. The :doc:`water reference </Scripting/Water>` includes a complete adapter example.

.. _evs-water--rendering-and-performance:

Rendering and performance
-------------------------

The bundled renderer uses a finite grid, analytical wave displacement, ripple normals, environment reflection and optional depth-based tint/foam. Supply compatible materials for your render pipeline. Depth effects need camera depth; reflections use the scene's environment or probes.

Reduce grid density, emission rates, budgets and effect distance before adding more systems. Check multiple active boats and rapid water entry/exit. See :doc:`Performance </Performance>` and :doc:`Demo resources </DemoResources>` for profiling and explicit asset bindings.

For detailed runtime behavior, see the :doc:`technical reference </Scripting/Water>`.
