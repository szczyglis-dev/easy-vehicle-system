.. _evs-interiorsystems--mirrors-wipers-displays-and-fuel:

Mirrors, wipers, displays and fuel
==================================

Add these modules to the vehicle independently. Use their public actions or connect them to :doc:`interior controls </InteriorControls>`.

.. _evs-interiorsystems--rearmirrors:

RearMirrors
-----------

1. Add RearMirrors and create an entry for each mirror.
2. Assign its surface renderer, a dedicated camera and the observing camera.
3. Place the mirror camera and set its view, clipping range, layer mask and texture resolution.
4. Exclude mirror surfaces from the rendered layers and set an update rate/render budget for the target hardware.

Use ``SetMirrorsEnabled`` or ``SetMirrorEnabled`` to switch rendering. Re-enable after changing texture dimensions. Rendering support, culling and texture ownership are documented in the :ref:`interior reference <evs-scripting-interior--rearmirrors>`.

.. _evs-interiorsystems--wipers:

Wipers
------

1. Add Wipers to the vehicle.
2. Add WiperBlade to each blade mesh. Assign its independent spindle anchor, axis and minimum/maximum angles.
3. Add the helpers to the module's Wipers list.
4. Set cycles per minute and assign the outward/return audio clips.
5. Preview the sweep and check windshield clearance.

``SetRunning``, ``Toggle`` and ``SetSpeed`` control wiping. Stopping finishes the cycle; disabling parks the blades. Use the module's **Legacy pivot settings** only for entries authored directly with pivots. See the :ref:`wiper reference <evs-scripting-interior--wipers>` for geometry and stepping contracts.

.. _evs-interiorsystems--carhud:

CarHud
------

Bind CarHud to a VehicleController and subscribe to ``Changed`` for telemetry updates. Use its snapshot to drive your own screen, UI or instruments. :doc:`API </API>` lists the available values; :doc:`Interior controls </InteriorControls>` describes model-mounted needles.

.. _evs-interiorsystems--fueltank:

FuelTank
--------

Add FuelTank, set capacity and consumption rates, then set the initial fuel. Consume Fuel controls depletion; Stop Engine When Empty controls the ignition/empty-tank rule independently. With Stop Engine When Empty enabled, an empty tank blocks ignition; refueling does not restart the engine automatically.

Use ``Refuel``, ``Fill``, ``Drain`` or ``SetFuel`` and subscribe to fuel events for gauges and gameplay. Persist fuel in your application's save system. See the :ref:`fuel reference <evs-scripting-interior--fuel-and-assists>` for consumption and action semantics.

.. _evs-interiorsystems--drivingassists:

DrivingAssists
--------------

Use DrivingAssists to configure and switch TractionControl and steering stability together. While enabled, it owns the corresponding settings; configure the underlying modules directly if you do not use the facade.

Use ``SetTractionControl``, ``SetStabilityControl`` or ``SetAssistsEnabled`` for runtime switches. Stability is yaw/lateral assistance. See :doc:`Traction control </TractionControl>` and the :ref:`assist reference <evs-scripting-interior--fuel-and-assists>` for tuning.
