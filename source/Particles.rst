.. _evs-particles--vehicle-particles:

Vehicle particles
=================

Particle modules read vehicle state and contact feedback. Assign materials, prefabs or custom systems explicitly; tune effects after the physical handling is correct.

.. _evs-particles--tire-smoke-and-loose-ground:

Tire smoke and loose ground
---------------------------

Add TireSmoke and assign one system per wheel, a prefab for missing slots, or a material for generated systems. Set maximum rate and emission response, then check skids and loss of contact.

Use :doc:`surface profiles </Surfaces>` for rolling dust and granular loose-ground particles. Supplied systems retain their authored appearance.

.. _evs-particles--exhaust:

Exhaust
-------

Add ExhaustSmoke and assign Exhaust Points at the pipe outlets. Each point's local +Z is the emission direction. Configure idle/loaded rates, intensity and response.

Assign a custom prefab/system for another effect. **Animate Custom Particles** allows the module to alter its appearance; otherwise it controls emission and outlet pose. Ordinary exhaust stops in hover/airplane modes.

.. _evs-particles--propulsion-jets:

Propulsion jets
---------------

Add PropulsionJets and assign separate hover/aircraft outlet arrays. Set rates, speed, color and material, or supply a particle prefab. ``SetJetsEnabled`` provides a runtime switch.

Jets are visual effects; propulsion forces belong to the drive mode. Rotor/propeller mesh animation uses ``Propulsion.propellers``.

For generated-system ownership, budgets and update behavior, see :doc:`Presentation reference </Scripting/Presentation>`. For bundled assets, see :doc:`Demo resources </DemoResources>`.
