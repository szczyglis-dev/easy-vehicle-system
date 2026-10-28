.. _evs-weapons--weapons-and-payloads:

Weapons and payloads
====================

Weapon modules provide aiming, firing, recoil and payload release. Your application supplies input, inventory, scoring and replenishment.

.. _evs-weapons--set-up-a-barrel:

Set up a barrel
---------------

1. Configure a MovingPart for turret yaw and a WeaponBarrel for elevation. Place independent anchors at their real rotation axes.
2. Assign the muzzle transform with local +Z pointing along the shot direction.
3. Assign a projectile component implementing ``IWeaponProjectile`` and configure speed, impulse, lifetime and fire interval.
4. Add WeaponEffects for sound/flash/smoke and WeaponRecoil for barrel travel or hull impulse.
5. Check aim limits, ownership filtering, firing cadence and projectile collisions.

Use ``AimAt``, movement input or target-angle actions for aiming. Use ``TryFire`` for a single request, or ``SetTrigger`` for the selected firing mode. Supply a compensated target point for ballistic aiming.

.. _evs-weapons--set-up-rockets:

Set up rockets
--------------

Add Rocket to each mounted store and register it in RocketLauncher's list. Configure launch direction, collision shape, mass, motor, gravity, lifetime and presentation assets.

``TryFire`` launches the next available store. ``SetTrigger`` supports held automatic fire. The base Rocket flies without target guidance; subclass its launch, motor or impact behavior for a different projectile. See the :ref:`rocket reference <evs-scripting-weapons--rocket-and-presentation-ownership>` for copy ownership and detonation semantics.

.. _evs-weapons--drop-an-object:

Drop an object
--------------

1. Add DroppableObject to a payload root and provide a suitable collider.
2. Keep the payload as one rigid body; configure its mass and inherited/separation velocity.
3. Add ObjectDropper to the vehicle and call ``TryDrop(payload)`` with the specific object to release.
4. Handle cleanup, impact behavior and replenishment in application code.

A dropped object remains physical until the application removes it. ObjectDropper supplies cooldown and an enable switch; it does not choose an inventory item. See :ref:`payload contracts <evs-scripting-weapons--drop-a-selected-object>`.

.. _evs-weapons--extend-and-inspect:

Extend and inspect
------------------

Use Scene gizmos to inspect axes, limits, muzzle direction and trajectory previews. Derive from the components or implement ``IWeaponProjectile`` for custom behavior. The :doc:`weapon reference </Scripting/Weapons>` documents actions, events, collision filtering, recoil and lifetimes.
