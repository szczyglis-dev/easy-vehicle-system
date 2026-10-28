.. _evs-api-presentation--particles-and-tire-marks-api:

Particles and tire marks API
============================

Read :doc:`the system explanation </Scripting/Presentation>` for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from ``MonoBehaviour``, ``Object`` or ``ScriptableObject`` are documented by Unity.

.. _evs-api-presentation--types:

Types
-----

-  :ref:`BoatWaterParticles <evs-api-presentation--boatwaterparticles>`
-  :ref:`EffectsCore <evs-api-presentation--effectscore>`
-  :ref:`EffectsModule <evs-api-presentation--effectsmodule>`
-  :ref:`ExhaustSmoke <evs-api-presentation--exhaustsmoke>`
-  :ref:`ParticleFactory <evs-api-presentation--particlefactory>`
-  :ref:`PropulsionJets <evs-api-presentation--propulsionjets>`
-  :ref:`SkidmarkBuffer <evs-api-presentation--skidmarkbuffer>`
-  :ref:`Skidmarks <evs-api-presentation--skidmarks>`
-  :ref:`TireSmoke <evs-api-presentation--tiresmoke>`
-  :ref:`WaterParticleFactory <evs-api-presentation--waterparticlefactory>`

.. _evs-api-presentation--boatwaterparticles:

BoatWaterParticles
------------------

**Runtime/Effects/Particles/BoatWaterParticles.cs**

Uses hull-water contact for surface-water presentation.

**Inherits / implements:** :ref:`EffectsModule <evs-api-presentation--effectsmodule>`.

.. _evs-api-presentation--methods:

Methods
~~~~~~~

+-------------------------------------------------------------+-----------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| Signature                                                   | Role and behavior                                                                 | Arguments and result                                                                       |
+=============================================================+===================================================================================+============================================================================================+
| ``public override void Configure(VehicleController owner)`` | Caches the vehicle and resolves an unassigned engine reference.                   | ``owner`` — Unity/application owner whose identity controls this relationship or resource. |
+-------------------------------------------------------------+-----------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| ``public virtual void RenderWater(float deltaTime)``        | Updates water particles from resolved hull-water contact.                         | ``deltaTime`` — Elapsed time in seconds supplied by the owning loop.                       |
+-------------------------------------------------------------+-----------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| ``public virtual void Suspend()``                           | Stops owned water-particle presentation according to the module's cleanup policy. | No arguments; no returned value.                                                           |
+-------------------------------------------------------------+-----------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+

.. _evs-api-presentation--state-and-configuration:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| Member                                                                 | Meaning                                                                                          |
+========================================================================+==================================================================================================+
| ``public VehicleController vehicle``                                   | Authored vehicle used by ``BoatWaterParticles``.                                                 |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public Engine engine``                                               | Authored engine used by ``BoatWaterParticles``.                                                  |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public bool waterParticlesEnabled``                                  | Authored water particles enabled used by ``BoatWaterParticles``. Initial value: ``true``.        |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public bool propellerEnabled``                                       | Authored propeller enabled used by ``BoatWaterParticles``. Initial value: ``true``.              |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public bool wakeEnabled``                                            | Authored wake enabled used by ``BoatWaterParticles``. Initial value: ``true``.                   |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public bool splashesEnabled``                                        | Authored splashes enabled used by ``BoatWaterParticles``. Initial value: ``true``.               |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public bool hullRipplesEnabled``                                     | Authored hull ripples enabled used by ``BoatWaterParticles``. Initial value: ``true``.           |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public float hullRippleRate``                                        | Base hull-ripple emission rate, in particles per second.                                         |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public float runningSprayFactor``                                    | Small bow-side droplets produced by forward motion, in addition to real hull impacts.            |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public ParticleSystem propellerPrefab``                              | Authored propeller prefab used by ``BoatWaterParticles``.                                        |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public ParticleSystem wakePrefab``                                   | Authored wake prefab used by ``BoatWaterParticles``.                                             |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public ParticleSystem splashPrefab``                                 | Authored splash prefab used by ``BoatWaterParticles``.                                           |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public Material sprayMaterial``                                      | Authored spray material used by ``BoatWaterParticles``.                                          |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public Material foamMaterial``                                       | Authored foam material used by ``BoatWaterParticles``.                                           |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public Transform motorOutlet``                                       | Optional authored motor outlet; otherwise use ``sternOffset`` relative to the hull.              |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public Vector3 sternOffset``                                         | Fallback propeller-emission point in vehicle-local coordinates, in metres.                       |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public Vector2 hullHalfSize``                                        | Used without a ``WaterInteraction`` component; that component's size takes priority.             |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public float fullEffectSpeed``                                       | Authored full effect speed used by ``BoatWaterParticles``. Initial value: ``20``.                |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public float propellerRate``                                         | Propeller, wake and splash emission rates at full channel activity, in particles per second.     |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public float wakeRate``                                              | Propeller, wake and splash emission rates at full channel activity, in particles per second.     |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public float splashRate``                                            | Propeller, wake and splash emission rates at full channel activity, in particles per second.     |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public float splashEntryThreshold``                                  | Minimum inward hull-point speed eligible for entry splash particles, in m/s.                     |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public float splashFullEntrySpeed``                                  | Authored splash full entry speed used by ``BoatWaterParticles``. Initial value: ``.45f``.        |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public float cullDistance``                                          | Distance beyond which this effect suspends rendering, in metres; zero disables distance culling. |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public int propellerBudget``                                         | Authored propeller budget used by ``BoatWaterParticles``. Initial value: ``384``.                |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public int wakeBudget``                                              | Authored wake budget used by ``BoatWaterParticles``. Initial value: ``256``.                     |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public int splashBudget``                                            | Authored splash budget used by ``BoatWaterParticles``. Initial value: ``192``.                   |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public virtual float CurrentPropellerRate { get; protected set; }``  | Current resolved propeller emission rate, in particles per second.                               |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public virtual float CurrentWakeRate { get; protected set; }``       | Current resolved wake emission rate, in particles per second.                                    |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public virtual float CurrentHullRippleRate { get; protected set; }`` | Current resolved hull-ripple emission rate, in particles per second.                             |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public virtual int EmittedSplashCount { get; protected set; }``      | Read-only/resolved emitted splash count for ``BoatWaterParticles``.                              |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public virtual int SystemCount { get; }``                            | Read-only/resolved system count for ``BoatWaterParticles``.                                      |
+------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+

.. _evs-api-presentation--effectscore:

EffectsCore
-----------

**Runtime/Effects/Core/EffectsCore.cs**

Configuration/implementation type for effects core within particles and tire marks.

**Inherits / implements:** :ref:`CategoryCore <evs-api-modules--categorycore>`.

.. _evs-api-presentation--methods-1:

Methods
~~~~~~~

+--------------------------+-------------------------------------------------------------+--------------------------------------------------------------------+
| Signature                | Role and behavior                                           | Arguments and result                                               |
+==========================+=============================================================+====================================================================+
| ``public EffectsCore()`` | Constructs ``EffectsCore`` with the supplied initial state. | **Returns:** New instance initialized from the supplied arguments. |
+--------------------------+-------------------------------------------------------------+--------------------------------------------------------------------+

.. _evs-api-presentation--state-and-configuration-1:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------+--------------------------------------------------------------------------------------+
| Member                                               | Meaning                                                                              |
+======================================================+======================================================================================+
| ``public override ModuleCategory Category { get; }`` | Module responsibility category; it does not independently determine execution phase. |
+------------------------------------------------------+--------------------------------------------------------------------------------------+

.. _evs-api-presentation--effectsmodule:

EffectsModule
-------------

**Runtime/Effects/Core/EffectsModule.cs**

Configuration/implementation type for effects module within particles and tire marks.

**Inherits / implements:** :ref:`Module <evs-api-modules--module>`, :ref:`IEffectsModule <evs-api-modules--ieffectsmodule>`.

.. _evs-api-presentation--state-and-configuration-2:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------+--------------------------------------------------------------------------------------+
| Member                                                      | Meaning                                                                              |
+=============================================================+======================================================================================+
| ``public sealed override ModuleCategory Category { get; }`` | Module responsibility category; it does not independently determine execution phase. |
+-------------------------------------------------------------+--------------------------------------------------------------------------------------+

.. _evs-api-presentation--exhaustsmoke:

ExhaustSmoke
------------

**Runtime/Effects/Particles/ExhaustSmoke.cs**

Controls emission from configured exhaust outlets.

**Inherits / implements:** :ref:`EffectsModule <evs-api-presentation--effectsmodule>`.

.. _evs-api-presentation--state-and-configuration-3:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| Member                                                           | Meaning                                                                                          |
+==================================================================+==================================================================================================+
| ``public VehicleController vehicle``                             | Authored vehicle used by ``ExhaustSmoke``.                                                       |
+------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public Engine engine``                                         | Authored engine used by ``ExhaustSmoke``.                                                        |
+------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public Transform[] exhaustPoints``                             | Authored exhaust points used by ``ExhaustSmoke``.                                                |
+------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public ParticleSystem[] particles``                            | Authored particles used by ``ExhaustSmoke``.                                                     |
+------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public ParticleSystem particlePrefab``                         | Authored particle prefab used by ``ExhaustSmoke``.                                               |
+------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public Material defaultMaterial``                              | Authored default material used by ``ExhaustSmoke``.                                              |
+------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public bool createDefaultParticles``                           | Authored create default particles used by ``ExhaustSmoke``. Initial value: ``true``.             |
+------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public float idleRate``                                        | Emission rate at idle activity, in particles per second.                                         |
+------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public float loadedRate``                                      | Emission rate at full propulsion load, in particles per second.                                  |
+------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public float intensityMultiplier``                             | Authored intensity multiplier used by ``ExhaustSmoke``. Initial value: ``4``.                    |
+------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public float response``                                        | Authored response used by ``ExhaustSmoke``. Initial value: ``12``.                               |
+------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public bool animateCustomParticles``                           | Animate speed, size and tint on supplied particle prefabs/systems as well as generated defaults. |
+------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public virtual float CurrentActivity { get; protected set; }`` | Read-only/resolved current activity for ``ExhaustSmoke``.                                        |
+------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public virtual float CurrentRate { get; protected set; }``     | Current resolved emission rate, in particles per second.                                         |
+------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+

.. _evs-api-presentation--particlefactory:

ParticleFactory
---------------

**Runtime/Effects/Particles/ParticleFactory.cs**

Configuration/implementation type for particle factory within particles and tire marks.

.. _evs-api-presentation--methods-2:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                                    | Role and behavior                                                                     | Arguments and result                                                                                                                                                                                                                                                                                                                                                                                              |
+==============================================================================================================+=======================================================================================+===================================================================================================================================================================================================================================================================================================================================================================================================================+
| ``public static ParticleSystem CreateSmoke(string name, Transform parent, Material material, bool exhaust)`` | Creates a smoke particle system using the supplied material and owned parent.         | ``name`` — Diagnostic name for the generated source/object. ``parent`` — Owner transform for a newly created presentation resource. ``material`` — Assigned presentation material; ownership is not transferred implicitly. ``exhaust`` — Exhaust, interpreted by this operation in the declared type. **Returns:** Returned ``ParticleSystem``; ownership remains as specified by the creating/lookup operation. |
+--------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public static ParticleSystem CreateSand(string name, Transform parent, Material material)``                | Creates a granular tire-particle system using the supplied material and owned parent. | ``name`` — Diagnostic name for the generated source/object. ``parent`` — Owner transform for a newly created presentation resource. ``material`` — Assigned presentation material; ownership is not transferred implicitly. **Returns:** Returned ``ParticleSystem``; ownership remains as specified by the creating/lookup operation.                                                                            |
+--------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public static void SetRate(ParticleSystem system, float rate)``                                            | Sets a particle emission rate on an existing system.                                  | ``system`` — Existing ``ParticleSystem`` to update. ``rate`` — Requested particle emission rate.                                                                                                                                                                                                                                                                                                                  |
+--------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-presentation--propulsionjets:

PropulsionJets
--------------

**Runtime/Effects/Particles/PropulsionJets.cs**

Presents propulsion exhaust/jet outlets.

**Inherits / implements:** :ref:`EffectsModule <evs-api-presentation--effectsmodule>`.

.. _evs-api-presentation--methods-3:

Methods
~~~~~~~

+----------------------------------------------------+-------------------------------------------------------------------------------------+------------------------------------------------------+
| Signature                                          | Role and behavior                                                                   | Arguments and result                                 |
+====================================================+=====================================================================================+======================================================+
| ``public virtual void SetJetsEnabled(bool value)`` | Changes propulsion-jet presentation availability without setting mechanical thrust. | ``value`` — Requested bool state for this operation. |
+----------------------------------------------------+-------------------------------------------------------------------------------------+------------------------------------------------------+

.. _evs-api-presentation--events-and-inspector-callbacks:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------+----------------------------------------------------------------------------------------------------+
| Declaration                                      | Trigger, payload and meaning                                                                       |
+==================================================+====================================================================================================+
| ``public event Action<bool> JetsEnabledChanged`` | When jet presentation availability changes. Payload: bool; this does not report mechanical thrust. |
+--------------------------------------------------+----------------------------------------------------------------------------------------------------+

.. _evs-api-presentation--state-and-configuration-4:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Member                                                       | Meaning                                                                                           |
+==============================================================+===================================================================================================+
| ``public VehicleController vehicle``                         | Authored vehicle used by ``PropulsionJets``.                                                      |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| ``public Engine engine``                                     | Authored engine used by ``PropulsionJets``.                                                       |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| ``public Transform[] hoverPoints``                           | Authored hover points used by ``PropulsionJets``. Initial value: ``Array.Empty<Transform>()``.    |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| ``public Transform[] aircraftPoints``                        | Authored aircraft points used by ``PropulsionJets``. Initial value: ``Array.Empty<Transform>()``. |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| ``public ParticleSystem particlePrefab``                     | Authored particle prefab used by ``PropulsionJets``.                                              |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| ``public Material defaultMaterial``                          | Authored default material used by ``PropulsionJets``.                                             |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| ``public Color color``                                       | Authored color used by ``PropulsionJets``. Initial value: ``new Color(.25f, .65f, 1, .7f)``.      |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| ``public float idleRate``                                    | Emission rate at idle activity, in particles per second.                                          |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| ``public float loadedRate``                                  | Emission rate at full propulsion load, in particles per second.                                   |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| ``public float jetSpeed``                                    | Authored jet speed used by ``PropulsionJets``. Initial value: ``4``.                              |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| ``public bool jetsEnabled``                                  | Authored jets enabled used by ``PropulsionJets``. Initial value: ``true``.                        |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| ``public bool followPropulsionSpool``                        | Scale emission by the shared aircraft engine spool. Custom particle prefabs remain untouched.     |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| ``public virtual float CurrentRate { get; protected set; }`` | Current resolved emission rate, in particles per second.                                          |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------+

.. _evs-api-presentation--skidmarkbuffer:

SkidmarkBuffer
--------------

**Runtime/Effects/Decals/SkidmarkBuffer.cs**

Stores bounded world-space ribbon geometry.

.. _evs-api-presentation--methods-4:

Methods
~~~~~~~

+------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                                                                | Role and behavior                                                                        | Arguments and result                                                                                                                                                                                                                                                                                                                                                                  |
+==========================================================================================================================================+==========================================================================================+=======================================================================================================================================================================================================================================================================================================================================================================================+
| ``public SkidmarkBuffer(int capacity)``                                                                                                  | Constructs ``SkidmarkBuffer`` with the supplied initial state.                           | ``capacity`` — Capacity, interpreted by this operation in the declared type. **Returns:** New instance initialized from the supplied arguments.                                                                                                                                                                                                                                       |
+------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public void Add(Vector3 from, Vector3 to, Vector3 normal, float width, float intensity, float birthTime)``                             | Appends a mark segment to the bounded geometry buffer and returns its buffer identifier. | ``from`` — Source movement profile/state. ``to`` — Target movement profile/state. ``normal`` — Contact/surface normal in the declared frame. ``width`` — Mark/tire width in metres. ``intensity`` — Intensity, interpreted by this operation in the declared type. ``birthTime`` — Mark creation time.                                                                                |
+------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public void Add(Vector3 from, Vector3 to, Vector3 normal, float width, float intensity, float birthTime, Color tint, float lifetime)`` | Appends a mark segment to the bounded geometry buffer and returns its buffer identifier. | ``from`` — Source movement profile/state. ``to`` — Target movement profile/state. ``normal`` — Contact/surface normal in the declared frame. ``width`` — Mark/tire width in metres. ``intensity`` — Intensity, interpreted by this operation in the declared type. ``birthTime`` — Mark creation time. ``tint`` — Recorded mark color. ``lifetime`` — Projectile lifetime in seconds. |
+------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public void Upload()``                                                                                                                 | Uploads changed mark geometry to the owned mesh.                                         | No arguments; no returned value.                                                                                                                                                                                                                                                                                                                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-presentation--state-and-configuration-5:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------+----------------------------------------------------------+
| Member                                            | Meaning                                                  |
+===================================================+==========================================================+
| ``public Mesh Mesh { get; }``                     | Read-only/resolved mesh for ``SkidmarkBuffer``.          |
+---------------------------------------------------+----------------------------------------------------------+
| ``public int SegmentCount { get; private set; }`` | Read-only/resolved segment count for ``SkidmarkBuffer``. |
+---------------------------------------------------+----------------------------------------------------------+

.. _evs-api-presentation--skidmarks:

Skidmarks
---------

**Runtime/Effects/Decals/Skidmarks.cs**

Consumes contact state and controls trail history.

**Inherits / implements:** :ref:`EffectsModule <evs-api-presentation--effectsmodule>`.

.. _evs-api-presentation--methods-5:

Methods
~~~~~~~

+--------------------------------------+-------------------------------------------------------------------------+----------------------------------+
| Signature                            | Role and behavior                                                       | Arguments and result             |
+======================================+=========================================================================+==================================+
| ``public virtual void ClearMarks()`` | Clears this vehicle's recorded mark history and breaks existing trails. | No arguments; no returned value. |
+--------------------------------------+-------------------------------------------------------------------------+----------------------------------+

.. _evs-api-presentation--events-and-inspector-callbacks-1:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------+------------------------------------------------+
| Declaration                            | Trigger, payload and meaning                   |
+========================================+================================================+
| ``public event System.Action Cleared`` | After skidmark history is cleared. No payload. |
+----------------------------------------+------------------------------------------------+

.. _evs-api-presentation--state-and-configuration-6:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------+--------------------------------------------------------------------------------------------------+
| Member                                       | Meaning                                                                                          |
+==============================================+==================================================================================================+
| ``public Feedback feedback``                 | Authored feedback used by Skidmarks.                                                             |
+----------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public Material material``                 | Use Szczyglis/``EasyVehicleSystem``/Skidmarks or a compatible transparent vertex-color material. |
+----------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public float width``                       | Authored width used by Skidmarks. Initial value: ``.24f``.                                       |
+----------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public float minimumIntensity``            | Authored minimum intensity used by Skidmarks. Initial value: ``.12f``.                           |
+----------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public float minimumDistance``             | Authored minimum distance used by Skidmarks. Initial value: ``.12f``.                            |
+----------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public float maximumGap``                  | Largest separation that may be joined by one continuous tire trail, in metres.                   |
+----------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public float groundOffset``                | Authored ground offset used by Skidmarks. Initial value: ``.015f``.                              |
+----------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public int maxSegments``                   | Authored max segments used by Skidmarks. Initial value: ``2048``.                                |
+----------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public float lifetime``                    | Authored lifetime used by Skidmarks. Initial value: ``35``.                                      |
+----------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public virtual int SegmentCount { get; }`` | Read-only/resolved segment count for Skidmarks.                                                  |
+----------------------------------------------+--------------------------------------------------------------------------------------------------+

.. _evs-api-presentation--tiresmoke:

TireSmoke
---------

**Runtime/Effects/Particles/TireSmoke.cs**

Manages wheel smoke and granular emission.

**Inherits / implements:** :ref:`EffectsModule <evs-api-presentation--effectsmodule>`.

.. _evs-api-presentation--methods-6:

Methods
~~~~~~~

+----------------------------------------------------------------+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                      | Role and behavior                                                         | Arguments and result                                                                                                                                                                             |
+================================================================+===========================================================================+==================================================================================================================================================================================================+
| ``public virtual ParticleSystem GetWheelParticles(int index)`` | Returns the smoke/granular particle systems owned for a configured wheel. | ``index`` — Zero-based configured-entry index; use the owner's current list ordering. **Returns:** Returned ``ParticleSystem``; ownership remains as specified by the creating/lookup operation. |
+----------------------------------------------------------------+---------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-presentation--state-and-configuration-7:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| Member                                                            | Meaning                                                                           |
+===================================================================+===================================================================================+
| ``public Feedback feedback``                                      | Authored feedback used by ``TireSmoke``.                                          |
+-------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| ``public ParticleSystem[] wheelParticles``                        | Authored wheel particles used by ``TireSmoke``.                                   |
+-------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| ``public Material sandMaterial``                                  | Authored sand material used by ``TireSmoke``.                                     |
+-------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| ``public ParticleSystem particlePrefab``                          | Authored particle prefab used by ``TireSmoke``.                                   |
+-------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| ``public Material defaultMaterial``                               | Authored default material used by ``TireSmoke``.                                  |
+-------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| ``public bool createDefaultParticles``                            | Authored create default particles used by ``TireSmoke``. Initial value: ``true``. |
+-------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| ``public float maximumRate``                                      | Largest permitted particle emission rate, in particles per second.                |
+-------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| ``public float emissionResponse``                                 | Response of smoke density to changing slip. Zero follows slip immediately.        |
+-------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| ``public float minimumIntensity``                                 | Authored minimum intensity used by ``TireSmoke``. Initial value: ``.12f``.        |
+-------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| ``public virtual float CurrentIntensity { get; protected set; }`` | Read-only/resolved current intensity for ``TireSmoke``.                           |
+-------------------------------------------------------------------+-----------------------------------------------------------------------------------+

.. _evs-api-presentation--waterparticlefactory:

WaterParticleFactory
--------------------

**Runtime/Effects/Particles/WaterParticleFactory.cs**

Configuration/implementation type for water particle factory within particles and tire marks.

.. _evs-api-presentation--methods-7:

Methods
~~~~~~~

+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                                        | Role and behavior                                                                              | Arguments and result                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
+==================================================================================================================+================================================================================================+======================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
| ``public static ParticleSystem Create(Transform parent, string name, Material material, bool foam, int budget)`` | Creates an owned water-particle presentation system with the requested style/material context. | ``parent`` — Owner transform for a newly created presentation resource. ``name`` — Diagnostic name for the generated source/object. ``material`` — Assigned presentation material; ownership is not transferred implicitly. ``foam`` — Foam, interpreted by this operation in the declared type. ``budget`` — Budget, interpreted by this operation in the declared type. **Returns:** Returned ``ParticleSystem``; ownership remains as specified by the creating/lookup operation. |
+------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
