.. _evs-tirecollision--solid-tire-contacts:

Solid tire contacts
===================

``TireCollision`` supplements WheelCollider with sidewall and obstacle contact. Native suspension and road traction remain responsible for supported rolling contact.

.. _evs-tirecollision--configure:

Configure
---------

1. Set radius, width and mass for every wheel in **Wheel Setup**.
2. Add TireCollision to the vehicle and enable the required contacts.
3. Check chassis and wheel-arch colliders for overlap with the tire volume throughout steering and suspension travel.
4. Check curbs, walls, landing and high-speed impacts. Tune the physics timestep and solver settings for the scene.
5. Combine with :doc:`ContactEnvelope </ContactEnvelope>` when smoother lower rolling support is needed.

Use compound chassis colliders that leave actual wheel clearance. A single large box or convex hull can fill an open wheel arch. TireCollision does not model tire deformation, tread blocks or independently articulated unsprung wheel bodies.

``Wheel.Grounded`` includes recent loaded supplemental tread contacts. Automatic gearbox shifts still require loaded native road contacts. ``WheelDynamics`` separately configures airborne spin losses.

For supplemental contact resolution, traction ownership, collision exclusions and force application, see :doc:`Wheel contact reference </Scripting/WheelContact>`.
