.. _evs-boat--boat-setup:

Boat setup
==========

Choose **Boat** for surface buoyancy, propeller thrust and rudder steering. Configure water contact independently of sound, particles and model animation.

.. _evs-boat--configure:

Configure
---------

1. Prepare a root Rigidbody and suitable hull collider, then choose **Tools → EasyVehicleSystem → Add Vehicle → Boat**.
2. Assign a provider through WaterInteraction, or set the profile's ``waterLevel``, ``waterCenter`` and ``waterSize`` for a fallback plane.
3. Set mass, ``buoyancyDepth`` and ``verticalDamping``. Check flotation with the engine off, including the intended passenger load.
4. Tune acceleration, forward resistance and lateral resistance. Check forward/reverse motion and coasting.
5. Tune rudder response and stationary maneuvering. Check both digital and analog steering.
6. Add rocking only after basic flotation and handling are stable. Assign the helm, audio and particle assets as required. For a visible boat propeller, use the :ref:`presentation extension <evs-scripting-boat--animate-a-boat-propeller>`.

.. _evs-boat--tune-handling:

Tune handling
-------------

+-------------------------------+------------------------------------------------------------------+
| Goal                          | Settings                                                         |
+===============================+==================================================================+
| More or less forward coasting | ``forwardDragScale``, ``speedResistance``                        |
+-------------------------------+------------------------------------------------------------------+
| Reduce sideways sliding       | ``lateralResistance``, ``speedLateralResistance``                |
+-------------------------------+------------------------------------------------------------------+
| Change underway turning       | ``maximumYawRate``, ``steeringYawResponse``, ``yawDampingScale`` |
+-------------------------------+------------------------------------------------------------------+
| Change low-speed maneuvering  | ``stationaryTurnAcceleration``, ``stationaryYawRate``            |
+-------------------------------+------------------------------------------------------------------+
| Smooth digital steering       | ``steeringRiseTime``, ``steeringReturnTime``                     |
+-------------------------------+------------------------------------------------------------------+
| Change hull rocking           | ``rockingStrength``, spring/damping and maneuver tilt            |
+-------------------------------+------------------------------------------------------------------+
| Change ambient movement       | ``ambientWaveDegrees``, period and idle-wave settings            |
+-------------------------------+------------------------------------------------------------------+

Set ``rockingStrength`` to zero to disable artificial rocking while keeping flotation and propulsion. Engine-off boats still float and coast. Outside finite water bounds, the profile supplies no buoyancy or powered water propulsion.

Use :doc:`Water </Water>` for providers/effects and :doc:`Input </Input>` for custom controls. The :doc:`drive dynamics reference </Scripting/Boat>` describes resistance, rocking, load history and powered trim in detail.
