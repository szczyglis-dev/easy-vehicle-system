.. _evs-contactenvelope--tire-contact-envelope:

Tire contact envelope
=====================

``ContactEnvelope`` improves support over small steps by sampling the tire's rolling profile around Unity WheelCollider's center ray. Use it alongside the native suspension and, optionally, ``TireCollision``.

.. _evs-contactenvelope--configure:

Configure
---------

1. Add ContactEnvelope to the vehicle's module list.
2. Set each tire's radius and width in **Wheels → Wheel Setup**.
3. Choose eligible Ground Layers and Minimum Ground Normal.
4. Start with the default sample counts, then check curbs, ramps, gaps and landings.
5. Adjust Maximum Lift Radius to limit support correction. Apply vehicle configuration after changing wheel geometry.

+---------------------------------------+--------------------------------------------------------+
| Setting                               | Purpose                                                |
+=======================================+========================================================+
| Longitudinal Samples                  | Rolling-direction resolution; odd values from 3 to 15. |
+---------------------------------------+--------------------------------------------------------+
| Width Samples                         | Across-tire resolution, from 1 to 3.                   |
+---------------------------------------+--------------------------------------------------------+
| Maximum Lift Radius                   | Maximum correction as a fraction of physical radius.   |
+---------------------------------------+--------------------------------------------------------+
| Ground Layers / Minimum Ground Normal | Eligible support surfaces.                             |
+---------------------------------------+--------------------------------------------------------+

Use a suitable chassis collider and suspension settings. The envelope is a finite sampling approximation; it cannot bridge unsupported gaps or replace a complete swept tire collision solver. Disable it to restore authored radii.

For solid sidewall and obstacle contacts, see :doc:`Tire collision </TireCollision>`. For the radius calculation, suspension coupling and force placement, see :doc:`Wheel contact reference </Scripting/WheelContact>`.
