.. _evs-api-weapons--weapons-and-payloads-api:

Weapons and payloads API
========================

Read :doc:`the system explanation </Scripting/Weapons>` for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from ``MonoBehaviour``, ``Object`` or ``ScriptableObject`` are documented by Unity.

.. _evs-api-weapons--types:

Types
-----

-  :ref:`DroppableObject <evs-api-weapons--droppableobject>`
-  :ref:`IWeaponProjectile <evs-api-weapons--iweaponprojectile>`
-  :ref:`ObjectDropper <evs-api-weapons--objectdropper>`
-  :ref:`Rocket <evs-api-weapons--rocket>`
-  :ref:`RocketLauncher <evs-api-weapons--rocketlauncher>`
-  :ref:`WeaponBarrel <evs-api-weapons--weaponbarrel>`
-  :ref:`WeaponEffects <evs-api-weapons--weaponeffects>`
-  :ref:`WeaponFireMode <evs-api-weapons--weaponfiremode>`
-  :ref:`WeaponRecoil <evs-api-weapons--weaponrecoil>`

.. _evs-api-weapons--droppableobject:

DroppableObject
---------------

**Runtime/World/Weapons/DroppableObject.cs**

Detaches the actual payload and establishes released physics.

**Inherits / implements:** ``MonoBehaviour``.

.. _evs-api-weapons--methods:

Methods
~~~~~~~

+-------------------------------------------------------+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                             | Role and behavior                                                                         | Arguments and result                                                                                                                                                                                                     |
+=======================================================+===========================================================================================+==========================================================================================================================================================================================================================+
| ``public virtual bool Drop(VehicleController owner)`` | Detaches this actual payload, establishes released-body motion and publishes its release. | ``owner`` — Unity/application owner whose identity controls this relationship or resource. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
+-------------------------------------------------------+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-weapons--events-and-inspector-callbacks:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Declaration                                      | Trigger, payload and meaning                                                                                             |
+==================================================+==========================================================================================================================+
| ``public event Action<DroppableObject> Dropped`` | After accepted payload release. Payload: released ``DroppableObject``; ``ObjectDropper`` also includes its own instance. |
+--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-weapons--state-and-configuration:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| Member                                                             | Meaning                                                                                     |
+====================================================================+=============================================================================================+
| ``public float mass``                                              | Authored mass used by ``DroppableObject``. Initial value: ``10``.                           |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| ``public bool inheritVelocity``                                    | Retains the carrier's point velocity when releasing this payload.                           |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| ``public Vector3 localReleaseVelocity``                            | Optional separation velocity in this object's local axes, in metres per second.             |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| ``public virtual bool IsDropped { get; protected set; }``          | Current is dropped predicate; read it instead of maintaining a second application flag.     |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| ``public virtual Rigidbody Body { get; protected set; }``          | The released projectile/payload's own ``Rigidbody``, used for its flight and impact motion. |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| ``public virtual VehicleController Owner { get; protected set; }`` | Read-only/resolved owner for ``DroppableObject``.                                           |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------+

.. _evs-api-weapons--iweaponprojectile:

IWeaponProjectile
-----------------

**Runtime/World/Weapons/WeaponBarrel.cs**

Projectile handover contract invoked after a barrel admits/spawns a shot.

.. _evs-api-weapons--methods-1:

Methods
~~~~~~~

+----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                                                  | Role and behavior                                                                                                     | Arguments and result                                                                                                                                                                                                                                                                                                                                                                             |
+============================================================================================================================+=======================================================================================================================+==================================================================================================================================================================================================================================================================================================================================================================================================+
| ``void Initialize(VehicleController owner, Vector3 velocity, float impulse, float lifetime, Collider[] ignoredColliders)`` | Accepts the projectile handover: owner, initial world velocity, impact impulse, lifetime and ignored owner colliders. | ``owner`` — Unity/application owner whose identity controls this relationship or resource. ``velocity`` — World velocity in m/s. ``impulse`` — Impact or recoil impulse; use ``ForceMode.Impulse`` when applying the supplied impulse. ``lifetime`` — Projectile lifetime in seconds. ``ignoredColliders`` — Owner colliders that the projectile must exclude from its initial collision policy. |
+----------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-weapons--objectdropper:

ObjectDropper
-------------

**Runtime/World/Weapons/ObjectDropper.cs**

Validates selected payload release and cooldown.

**Inherits / implements:** :ref:`WorldModule <evs-api-modules--worldmodule>`.

.. _evs-api-weapons--methods-2:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                  | Role and behavior                                                                                | Arguments and result                                                                                                                                                                                                     |
+============================================================================================+==================================================================================================+==========================================================================================================================================================================================================================+
| ``public override void Configure(VehicleController vehicle)``                              | Assigns the vehicle owner used to validate payload release.                                      | ``vehicle`` — Vehicle context/owner receiving the operation.                                                                                                                                                             |
+--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Decrements payload-release cooldown; selection and release remain explicit ``TryDrop`` requests. | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetDroppingEnabled(bool value)``                                     | Changes payload-release availability through the dropper's action/event path.                    | ``value`` — Requested bool state for this operation.                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryDrop(DroppableObject item)``                                      | Requests release of a selected eligible payload, respecting owner, enable and cooldown policy.   | ``item`` — Item, interpreted by this operation in the declared type. **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values.                                            |
+--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-weapons--events-and-inspector-callbacks-1:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| Declaration                                                     | Trigger, payload and meaning                                                                                             |
+=================================================================+==========================================================================================================================+
| ``public event Action<ObjectDropper, DroppableObject> Dropped`` | After accepted payload release. Payload: released ``DroppableObject``; ``ObjectDropper`` also includes its own instance. |
+-----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<bool> DroppingEnabledChanged``            | When dropper availability changes. Payload: bool.                                                                        |
+-----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-weapons--state-and-configuration-1:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| Member                                                             | Meaning                                                                               |
+====================================================================+=======================================================================================+
| ``public float dropInterval``                                      | Authored drop interval used by ``ObjectDropper``. Initial value: ``.4f``.             |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| ``public bool droppingEnabled``                                    | Authored dropping enabled used by ``ObjectDropper``. Initial value: ``true``.         |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| ``public virtual VehicleController Owner { get; protected set; }`` | Read-only/resolved owner for ``ObjectDropper``.                                       |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| ``public virtual float CooldownRemaining { get; }``                | Seconds remaining before the next operation is allowed.                               |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| ``public virtual bool CanDrop { get; }``                           | Current can drop predicate; read it instead of maintaining a second application flag. |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------+

.. _evs-api-weapons--rocket:

Rocket
------

**Runtime/World/Weapons/Rocket.cs**

Owns launched-rocket motor, collision and lifetime behavior.

**Inherits / implements:** ``MonoBehaviour``.

.. _evs-api-weapons--methods-3:

Methods
~~~~~~~

+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                 | Role and behavior                                                                                     | Arguments and result                                                                                                                                                                      |
+===========================================================+=======================================================================================================+===========================================================================================================================================================================================+
| ``public virtual Rocket Launch(VehicleController owner)`` | Creates/initializes launched-rocket behavior from the mounted store and carrier state.                | ``owner`` — Unity/application owner whose identity controls this relationship or resource. **Returns:** Returned Rocket; ownership remains as specified by the creating/lookup operation. |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void StopMotor()``                       | Stops the rocket motor and its owned loop/emission without implying immediate projectile destruction. | No arguments; no returned value.                                                                                                                                                          |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Detonate(Vector3 point)``           | Ends the rocket through its explosion path at the supplied world point.                               | ``point`` — Geometry point in the declared coordinate frame.                                                                                                                              |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-weapons--events-and-inspector-callbacks-2:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------+--------------------------------------------------------------------------------+
| Declaration                                       | Trigger, payload and meaning                                                   |
+===================================================+================================================================================+
| ``public event Action<Rocket, Vector3> Exploded`` | At the rocket's explosion boundary. Payload: Rocket and world explosion point. |
+---------------------------------------------------+--------------------------------------------------------------------------------+

.. _evs-api-weapons--state-and-configuration-2:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| Member                                                             | Meaning                                                                                                 |
+====================================================================+=========================================================================================================+
| ``public Transform launchDirection``                               | Authored launch direction used by Rocket.                                                               |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public float mass``                                              | Authored mass used by Rocket. Initial value: ``35``.                                                    |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public float launchSpeed``                                       | Authored launch speed used by Rocket. Initial value: ``65``.                                            |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public float acceleration``                                      | Authored acceleration used by Rocket. Initial value: ``80``.                                            |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public float burnSeconds``                                       | Authored burn seconds used by Rocket. Initial value: ``3``.                                             |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public float lifetime``                                          | Authored lifetime used by Rocket. Initial value: ``12``.                                                |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public float explosionRadius``                                   | Authored explosion radius used by Rocket. Initial value: ``12``.                                        |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public float explosionImpulse``                                  | Authored explosion impulse used by Rocket. Initial value: ``80000``.                                    |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public bool useGravity``                                         | Authored use gravity used by Rocket. Initial value: ``true``.                                           |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public bool inheritVehicleVelocity``                             | Authored inherit vehicle velocity used by Rocket. Initial value: ``true``.                              |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public bool detonateOnCollision``                                | Automatically detonate on contact. Explicit Detonate calls remain available.                            |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public bool applyExplosionForce``                                | Apply explosion impulse to rigidbodies. Effects and Exploded notification are independent.              |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public LayerMask explosionMask``                                 | Authored explosion mask used by Rocket. Initial value: ``~0``.                                          |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public float explosionUpwardModifier``                           | Upward offset in metres used by Unity's explosion-force calculation.                                    |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public ParticleSystem explosionPrefab``                          | Authored explosion prefab used by Rocket.                                                               |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public ParticleSystem exhaustPrefab``                            | Authored exhaust prefab used by Rocket.                                                                 |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public Transform exhaustAnchor``                                 | Engine nozzle: local +Z points out of the exhaust. Optional; defaults to the launch direction reversed. |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public AudioClip engineLoop``                                    | Authored engine loop used by Rocket.                                                                    |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public float engineVolume``                                      | Authored engine volume used by Rocket. Initial value: ``.8f``.                                          |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public float audioMinDistance``                                  | Distance within which rocket audio retains full volume, in metres.                                      |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public float audioMaxDistance``                                  | Authored audio max distance used by Rocket. Initial value: ``500``.                                     |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public virtual AudioSource EngineAudio { get; protected set; }`` | Read-only/resolved engine audio for Rocket.                                                             |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public virtual ParticleSystem Exhaust { get; protected set; }``  | Read-only/resolved exhaust for Rocket.                                                                  |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public virtual bool MotorBurning { get; protected set; }``       | Read-only/resolved motor burning for Rocket.                                                            |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public AudioClip launchSound``                                   | Authored launch sound used by Rocket.                                                                   |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public AudioClip explosionSound``                                | Authored explosion sound used by Rocket.                                                                |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public virtual bool IsLaunched { get; protected set; }``         | Current is launched predicate; read it instead of maintaining a second application flag.                |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public virtual Rigidbody Body { get; protected set; }``          | The released projectile/payload's own ``Rigidbody``, used for its flight and impact motion.             |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public virtual VehicleController Owner { get; protected set; }`` | Read-only/resolved owner for Rocket.                                                                    |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public virtual Vector3 FlightDirection { get; }``                | Current normalized world-space motor thrust direction.                                                  |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public virtual float RemainingBurnTime { get; }``                | Read-only/resolved remaining burn time for Rocket.                                                      |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public virtual float RemainingLifetime { get; }``                | Seconds of flight remaining before automatic detonation.                                                |
+--------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------+

.. _evs-api-weapons--rocketlauncher:

RocketLauncher
--------------

**Runtime/World/Weapons/RocketLauncher.cs**

Selects and launches configured mounted rocket stores.

**Inherits / implements:** :ref:`WorldModule <evs-api-modules--worldmodule>`.

.. _evs-api-weapons--methods-4:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                  | Role and behavior                                                                                   | Arguments and result                                                                                                                                                                                                     |
+============================================================================================+=====================================================================================================+==========================================================================================================================================================================================================================+
| ``public override void Configure(VehicleController vehicle)``                              | Assigns the vehicle owner used by launched stores.                                                  | ``vehicle`` — Vehicle context/owner receiving the operation.                                                                                                                                                             |
+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Decrements launcher cooldown and requests another shot while automatic held-trigger policy applies. | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetFiringEnabled(bool value)``                                       | Changes weapon firing availability and publishes its state transition.                              | ``value`` — Requested bool state for this operation.                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetTrigger(bool held)``                                              | Supplies held trigger intent; firing mode/cooldown determine actual shots.                          | ``held`` — Held trigger/button intent, distinct from an accepted shot.                                                                                                                                                   |
+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryFire()``                                                          | Requests one shot/store release subject to enable, valid setup and cooldown policy.                 | **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values.                                                                                                                 |
+--------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-weapons--events-and-inspector-callbacks-3:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| Declaration                                           | Trigger, payload and meaning                                                                                          |
+=======================================================+=======================================================================================================================+
| ``public event Action<bool> TriggerChanged``          | When held trigger intent changes. Payload: bool; a ``true`` trigger does not guarantee a shot.                        |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| ``public event Action<bool> FiringEnabledChanged``    | When weapon firing availability changes. Payload: bool.                                                               |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| ``public event Action<RocketLauncher, Rocket> Fired`` | After an admitted shot creates/releases its projectile. Payload: weapon owner and spawned projectile/store component. |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+

.. _evs-api-weapons--state-and-configuration-3:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------+----------------------------------------------------------------------------------------+
| Member                                                      | Meaning                                                                                |
+=============================================================+========================================================================================+
| ``public Rocket[] rockets``                                 | Authored rockets used by ``RocketLauncher``. Initial value: ``Array.Empty<Rocket>()``. |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------+
| ``public float fireInterval``                               | Authored fire interval used by ``RocketLauncher``. Initial value: ``.4f``.             |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------+
| ``public bool firingEnabled``                               | Authored firing enabled used by ``RocketLauncher``. Initial value: ``true``.           |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------+
| ``public bool automatic``                                   | Authored automatic used by ``RocketLauncher``.                                         |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------+
| ``public virtual bool TriggerHeld { get; protected set; }`` | Read-only/resolved trigger held for ``RocketLauncher``.                                |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------+
| ``public virtual float CooldownRemaining { get; }``         | Seconds remaining before the next operation is allowed.                                |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------+
| ``public virtual int Remaining { get; }``                   | Read-only/resolved remaining for ``RocketLauncher``.                                   |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------+
| ``public virtual bool CanFire { get; }``                    | Current can fire predicate; read it instead of maintaining a second application flag.  |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------+

.. _evs-api-weapons--weaponbarrel:

WeaponBarrel
------------

**Runtime/World/Weapons/WeaponBarrel.cs**

Owns muzzle aiming, trigger/cooldown admission and projectile initialization.

**Inherits / implements:** :ref:`WorldModule <evs-api-modules--worldmodule>`.

.. _evs-api-weapons--methods-5:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                  | Role and behavior                                                                                                             | Arguments and result                                                                                                                                                                                                     |
+============================================================================================+===============================================================================================================================+==========================================================================================================================================================================================================================+
| ``public override void Configure(VehicleController vehicle)``                              | Assigns the vehicle owner and rebuilds owner-collider exclusions for spawned projectiles.                                     | ``vehicle`` — Vehicle context/owner receiving the operation.                                                                                                                                                             |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void RefreshCollisionFilter()``                                           | Rebuilds the owner-collider exclusion set supplied to subsequently spawned projectiles.                                       | No arguments; no returned value.                                                                                                                                                                                         |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Attempts at most one automatic shot for a positive timestep while the trigger is held.                                        | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetFiringEnabled(bool value)``                                       | Changes weapon firing availability and publishes its state transition.                                                        | ``value`` — Requested bool state for this operation.                                                                                                                                                                     |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetMovementInput(float input)``                                      | Supplies barrel elevation rate input rather than a fixed aim target.                                                          | ``input`` — Command handle channel or normalized rate, according to the signature.                                                                                                                                       |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetAimAngle(float angle)``                                           | Requests a bounded barrel elevation angle in degrees.                                                                         | ``angle`` — Angular coordinate in degrees for this geometry operation.                                                                                                                                                   |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void AimAt(Vector3 point)``                                               | Starts or updates world-target tracking around the configured allowed axis; the overload selects a point or a live transform. | ``point`` — Geometry point in the declared coordinate frame.                                                                                                                                                             |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void AimAt(Transform target)``                                            | Starts or updates world-target tracking around the configured allowed axis; the overload selects a point or a live transform. | ``target`` — Configured target object/point; see declared type and owner.                                                                                                                                                |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void StopAiming()``                                                       | Releases barrel target tracking without inventing a new aim target.                                                           | No arguments; no returned value.                                                                                                                                                                                         |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetFireMode(WeaponFireMode mode)``                                   | Chooses single/automatic firing policy for subsequent trigger input.                                                          | ``mode`` — Mode, interpreted by this operation in the declared type.                                                                                                                                                     |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetTrigger(bool held)``                                              | Supplies held trigger intent; firing mode/cooldown determine actual shots.                                                    | ``held`` — Held trigger/button intent, distinct from an accepted shot.                                                                                                                                                   |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryFire()``                                                          | Requests one shot/store release subject to enable, valid setup and cooldown policy.                                           | **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values.                                                                                                                 |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-weapons--events-and-inspector-callbacks-4:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| Declaration                                                | Trigger, payload and meaning                                                                                          |
+============================================================+=======================================================================================================================+
| ``public event Action<bool> TriggerChanged``               | When held trigger intent changes. Payload: bool; a ``true`` trigger does not guarantee a shot.                        |
+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| ``public event Action<bool> FiringEnabledChanged``         | When weapon firing availability changes. Payload: bool.                                                               |
+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+
| ``public event Action<WeaponBarrel, MonoBehaviour> Fired`` | After an admitted shot creates/releases its projectile. Payload: weapon owner and spawned projectile/store component. |
+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+

.. _evs-api-weapons--state-and-configuration-4:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| Member                                                             | Meaning                                                                                          |
+====================================================================+==================================================================================================+
| ``public MovingPart movement``                                     | Authored movement used by ``WeaponBarrel``.                                                      |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public Transform muzzle``                                        | Authored muzzle used by ``WeaponBarrel``.                                                        |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public bool firingEnabled``                                      | Authored firing enabled used by ``WeaponBarrel``. Initial value: ``true``.                       |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public WeaponFireMode fireMode``                                 | Authored fire mode used by ``WeaponBarrel``.                                                     |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public float shotsPerSecond``                                    | Authored shots per second used by ``WeaponBarrel``. Initial value: ``.4f``.                      |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public MonoBehaviour projectilePrefab``                          | A prefab component implementing ``IWeaponProjectile``. Projectile behavior belongs to your game. |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public float muzzleSpeed``                                       | Authored muzzle speed used by ``WeaponBarrel``. Initial value: ``110``.                          |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public float impactImpulse``                                     | Authored impact impulse used by ``WeaponBarrel``. Initial value: ``20000``.                      |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public float projectileLifetime``                                | Authored projectile lifetime used by ``WeaponBarrel``. Initial value: ``12``.                    |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public bool inheritVehicleVelocity``                             | Authored inherit vehicle velocity used by ``WeaponBarrel``. Initial value: ``true``.             |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public virtual float Angle { get; }``                            | Read-only/resolved angle for ``WeaponBarrel``.                                                   |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public virtual float TargetAngle { get; }``                      | Requested rotation angle before speed-limited travel, in degrees.                                |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public virtual float ReloadRemaining { get; }``                  | Seconds until the barrel's next shot is permitted.                                               |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public virtual bool TriggerHeld { get; protected set; }``        | Read-only/resolved trigger held for ``WeaponBarrel``.                                            |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public virtual VehicleController Owner { get; protected set; }`` | Read-only/resolved owner for ``WeaponBarrel``.                                                   |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public virtual bool CanFire { get; }``                           | Current can fire predicate; read it instead of maintaining a second application flag.            |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+

.. _evs-api-weapons--weaponeffects:

WeaponEffects
-------------

**Runtime/Effects/Weapons/WeaponEffects.cs**

Presents shot sound, flash and smoke.

**Inherits / implements:** :ref:`EffectsModule <evs-api-presentation--effectsmodule>`.

.. _evs-api-weapons--methods-6:

Methods
~~~~~~~

+---------------------------------------------------------------+----------------------------------------------------------------+--------------------------------------------------------------+
| Signature                                                     | Role and behavior                                              | Arguments and result                                         |
+===============================================================+================================================================+==============================================================+
| ``public override void Configure(VehicleController vehicle)`` | Refreshes accepted-shot bindings while this effect is enabled. | ``vehicle`` — Vehicle context/owner receiving the operation. |
+---------------------------------------------------------------+----------------------------------------------------------------+--------------------------------------------------------------+

.. _evs-api-weapons--state-and-configuration-5:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                       | Meaning                                                                                                                                                                                                                            |
+==============================================+====================================================================================================================================================================================================================================+
| ``public WeaponBarrel weapon``               | Authored weapon used by ``WeaponEffects``.                                                                                                                                                                                         |
+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool playAudio``                    | ``playAudio``: plays a shot recording after confirmed barrel fire; ``emitSmoke``: emits the muzzle particle effect after confirmed barrel fire; ``spawnMuzzleFlash``: creates the muzzle-flash visual after confirmed barrel fire. |
+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool emitSmoke``                    | ``playAudio``: plays a shot recording after confirmed barrel fire; ``emitSmoke``: emits the muzzle particle effect after confirmed barrel fire; ``spawnMuzzleFlash``: creates the muzzle-flash visual after confirmed barrel fire. |
+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool spawnMuzzleFlash``             | ``playAudio``: plays a shot recording after confirmed barrel fire; ``emitSmoke``: emits the muzzle particle effect after confirmed barrel fire; ``spawnMuzzleFlash``: creates the muzzle-flash visual after confirmed barrel fire. |
+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float audioMinDistance``            | ``audioMinDistance``: distance within which rocket audio retains full volume, in metres; ``audioMaxDistance``: outer distance used by rocket audio attenuation, in metres.                                                         |
+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float audioMaxDistance``            | ``audioMinDistance``: distance within which rocket audio retains full volume, in metres; ``audioMaxDistance``: outer distance used by rocket audio attenuation, in metres.                                                         |
+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float spatialBlend``                | Blend from nonspatial audio at zero to fully positional audio at one.                                                                                                                                                              |
+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector2 audioPitch``                | Authored audio pitch used by ``WeaponEffects``. Initial value: ``Vector2.one``.                                                                                                                                                    |
+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public GameObject muzzleFlashPrefab``      | Optional flash object instantiated at the muzzle after a shot.                                                                                                                                                                     |
+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float flashLifetime``               | Authored flash lifetime used by ``WeaponEffects``. Initial value: ``2``.                                                                                                                                                           |
+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float smokeLifetime``               | Zero uses the particle duration and maximum lifetime.                                                                                                                                                                              |
+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float effectScale``                 | Authored effect scale used by ``WeaponEffects``. Initial value: ``1``.                                                                                                                                                             |
+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public AudioSource audioSource``           | Authored audio source used by ``WeaponEffects``.                                                                                                                                                                                   |
+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public AudioClip shotSound``               | Authored shot sound used by ``WeaponEffects``.                                                                                                                                                                                     |
+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float volume``                      | Authored volume used by ``WeaponEffects``. Initial value: ``.9f``.                                                                                                                                                                 |
+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public ParticleSystem muzzleEffectPrefab`` | Optional smoke/particle prefab instantiated at the muzzle after a shot.                                                                                                                                                            |
+----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-weapons--weaponfiremode:

WeaponFireMode
--------------

**Runtime/World/Weapons/WeaponBarrel.cs**

Defines the allowed weapon fire mode choices used by this topic.

.. _evs-api-weapons--values:

Values
~~~~~~

-  ``Single``
-  ``Automatic``

.. _evs-api-weapons--weaponrecoil:

WeaponRecoil
------------

**Runtime/Effects/Weapons/WeaponRecoil.cs**

Presents configured visual/hull recoil.

**Inherits / implements:** :ref:`EffectsModule <evs-api-presentation--effectsmodule>`.

.. _evs-api-weapons--methods-7:

Methods
~~~~~~~

+---------------------------------------------------------------+-----------------------------------------------------------------------------+--------------------------------------------------------------+
| Signature                                                     | Role and behavior                                                           | Arguments and result                                         |
+===============================================================+=============================================================================+==============================================================+
| ``public override void Configure(VehicleController vehicle)`` | Refreshes accepted-shot bindings while this recoil presentation is enabled. | ``vehicle`` — Vehicle context/owner receiving the operation. |
+---------------------------------------------------------------+-----------------------------------------------------------------------------+--------------------------------------------------------------+

.. _evs-api-weapons--state-and-configuration-6:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                         | Meaning                                                                                                                                                                         |
+================================================================+=================================================================================================================================================================================+
| ``public WeaponBarrel weapon``                                 | Authored weapon used by ``WeaponRecoil``.                                                                                                                                       |
+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform barrel``                                    | Authored barrel used by ``WeaponRecoil``.                                                                                                                                       |
+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool animateBarrel``                                  | ``animateBarrel``: enables visual barrel kick and return after a confirmed shot; ``applyBodyImpulse``: applies a physical recoil impulse to the vehicle after a confirmed shot. |
+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool applyBodyImpulse``                               | ``animateBarrel``: enables visual barrel kick and return after a confirmed shot; ``applyBodyImpulse``: applies a physical recoil impulse to the vehicle after a confirmed shot. |
+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector3 localRecoilAxis``                             | Authored local recoil axis used by ``WeaponRecoil``. Initial value: ``Vector3.back``.                                                                                           |
+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float barrelTravel``                                  | Recoil travel in world metres; imported barrel scale is accounted for.                                                                                                          |
+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float kickDuration``                                  | Authored kick duration used by ``WeaponRecoil``. Initial value: ``.045f``.                                                                                                      |
+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float returnDuration``                                | Authored return duration used by ``WeaponRecoil``. Initial value: ``.32f``.                                                                                                     |
+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float bodyImpulse``                                   | Authored body impulse used by ``WeaponRecoil``. Initial value: ``1600``.                                                                                                        |
+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector3 angularImpulse``                              | Additional angular impulse in muzzle axes (pitch, yaw, roll). Native physics supplies suspension movement.                                                                      |
+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Transform impulsePoint``                              | Authored impulse point used by ``WeaponRecoil``.                                                                                                                                |
+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float CurrentOffset { get; protected set; }`` | Read-only/resolved current offset for ``WeaponRecoil``.                                                                                                                         |
+----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
