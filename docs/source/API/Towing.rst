.. _evs-api-towing--coupling-and-trailers-api:

Coupling and trailers API
=========================

Read :doc:`the system explanation </Scripting/Towing>` for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from ``MonoBehaviour``, ``Object`` or ``ScriptableObject`` are documented by Unity.

.. _evs-api-towing--types:

Types
-----

-  :ref:`Coupler <evs-api-towing--coupler>`
-  :ref:`Trailer <evs-api-towing--trailer>`

.. _evs-api-towing--coupler:

Coupler
-------

**Runtime/World/Towing/Coupler.cs**

Validates and owns one hitch relationship, joint and changed collision pairs.

**Inherits / implements:** :ref:`WorldModule <evs-api-modules--worldmodule>`.

.. _evs-api-towing--methods:

Methods
~~~~~~~

+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                          | Role and behavior                                                                                           | Arguments and result                                                                                                                                                                                 |
+====================================================+=============================================================================================================+======================================================================================================================================================================================================+
| ``public virtual void Detach()``                   | Ends the owned character or hitch relationship and releases the state/resources owned by that relationship. | No arguments; no returned value.                                                                                                                                                                     |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryAttach(Trailer trailer)`` | Requests a nearby valid trailer relationship, creating owned hitch constraints only when admitted.          | ``trailer`` — Explicit candidate trailer; selection/proximity UI remains application-owned. **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values. |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-towing--events-and-inspector-callbacks:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------+--------------------------------------------------------------------------------------------------------+
| Declaration                               | Trigger, payload and meaning                                                                           |
+===========================================+========================================================================================================+
| ``public event Action<Trailer> Attached`` | After coupler admission creates the relationship. Payload: Trailer.                                    |
+-------------------------------------------+--------------------------------------------------------------------------------------------------------+
| ``public event Action<Trailer> Detached`` | After explicit detachment/cleanup of this hitch relationship. Payload: the formerly connected Trailer. |
+-------------------------------------------+--------------------------------------------------------------------------------------------------------+

.. _evs-api-towing--state-and-configuration:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                             | Meaning                                                                                                                                  |
+====================================================================+==========================================================================================================================================+
| ``public VehicleController vehicle``                               | Authored vehicle used by Coupler.                                                                                                        |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform hitch``                                         | Authored hitch used by Coupler.                                                                                                          |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Trailer initialTrailer``                                  | Authored initial trailer used by Coupler.                                                                                                |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool attachOnStart``                                      | Attach Initial Trailer at startup. Manual ``TryAttach`` remains available when disabled.                                                 |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool allowJointBreak``                                    | Allow physical forces to break the hitch. Disable for an unbreakable connection.                                                         |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float attachDistance``                                    | Authored attach distance used by Coupler. Initial value: ``1.2f``.                                                                       |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float attachmentAlignmentTime``                           | Seconds to bring accepted nearby hitches together without an instantaneous correction impulse.                                           |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float longitudinalSpring``                                | Fore/aft hitch stiffness in N/m. A compliant drawbar prevents parked tire constraints from fighting a perfectly rigid longitudinal lock. |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float longitudinalDamper``                                | Fore/aft hitch damping in N·s/m.                                                                                                         |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float pitchLimit``                                        | Authored pitch limit used by Coupler. Initial value: ``30``.                                                                             |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float rollLimit``                                         | Authored roll limit used by Coupler. Initial value: ``20``.                                                                              |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float breakForce``                                        | Authored break force used by Coupler. Initial value: ``200000``.                                                                         |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float breakTorque``                                       | Authored break torque used by Coupler. Initial value: ``200000``.                                                                        |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual Trailer AttachedTrailer { get; protected set; }`` | Trailer currently connected to this coupler, or ``null`` when detached.                                                                  |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-towing--trailer:

Trailer
-------

**Runtime/World/Towing/Trailer.cs**

Stores the towed-body connection and brake-following behavior.

**Inherits / implements:** :ref:`WorldModule <evs-api-modules--worldmodule>`.

.. _evs-api-towing--methods-1:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                  | Role and behavior                                                                                         | Arguments and result                                                                                                                                                                                                     |
+============================================================================================+===========================================================================================================+==========================================================================================================================================================================================================================+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Forwards configured towing brake requests, clears trailer propulsion and applies detached-parking policy. | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-towing--events-and-inspector-callbacks-1:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------+----------------------------------------------------------------+
| Declaration                              | Trigger, payload and meaning                                   |
+==========================================+================================================================+
| ``public event Action ConnectionBroken`` | When a trailer's active hitch relationship breaks. No payload. |
+------------------------------------------+----------------------------------------------------------------+

.. _evs-api-towing--state-and-configuration-1:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| Member                                                                    | Meaning                                                                            |
+===========================================================================+====================================================================================+
| ``public Transform hitch``                                                | Authored hitch used by Trailer.                                                    |
+---------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| ``public bool parkWhenDetached``                                          | Authored park when detached used by Trailer. Initial value: ``true``.              |
+---------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| ``public bool followServiceBrake``                                        | Forward the towing vehicle's resolved service brake to this trailer.               |
+---------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| ``public bool followHandbrake``                                           | Forward the towing vehicle's handbrake. Detached parking is controlled separately. |
+---------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| ``public float serviceBrakeMultiplier``                                   | Multiplier for forwarded service braking; final demand is clamped to 0–1.          |
+---------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| ``public virtual VehicleController TowingVehicle { get; internal set; }`` | Read-only/resolved towing vehicle for Trailer.                                     |
+---------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| ``public virtual ConfigurableJoint Connection { get; internal set; }``    | Read-only/resolved connection for Trailer.                                         |
+---------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| ``public override int ExecutionOrder { get; }``                           | Default local priority within phase/category.                                      |
+---------------------------------------------------------------------------+------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }``                         | Cross-category execution barrier used by the module pipeline.                      |
+---------------------------------------------------------------------------+------------------------------------------------------------------------------------+
