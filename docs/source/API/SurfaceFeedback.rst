.. _evs-api-surfacefeedback--ground-surfaces-and-classification-api:

Ground surfaces and classification API
======================================

Read :doc:`the system explanation </Scripting/SurfaceFeedback>` for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from ``MonoBehaviour``, ``Object`` or ``ScriptableObject`` are documented by Unity.

.. _evs-api-surfacefeedback--types:

Types
-----

-  :ref:`Friction <evs-api-surfacefeedback--friction>`
-  :ref:`Surface <evs-api-surfacefeedback--surface>`
-  :ref:`TireSurface <evs-api-surfacefeedback--tiresurface>`
-  :ref:`TireSurface.LayerMapping <evs-api-surfacefeedback--tiresurfacelayermapping>`
-  :ref:`TireSurfaceProfile <evs-api-surfacefeedback--tiresurfaceprofile>`

.. _evs-api-surfacefeedback--friction:

Friction
--------

**Runtime/Physics/Friction/Friction.cs**

Reads physical grip and writes native tire friction behavior.

**Inherits / implements:** :ref:`PhysicsModule <evs-api-modules--physicsmodule>`.

.. _evs-api-surfacefeedback--methods:

Methods
~~~~~~~

+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                               | Role and behavior                                                                                             | Arguments and result                                                                                                                                            |
+=========================================================================+===============================================================================================================+=================================================================================================================================================================+
| ``public override void Step(VehicleController v, Command c, float dt)`` | Reads Surface from exact native hit colliders and writes forward/side friction with handbrake/tracked policy. | ``v`` — V, interpreted by this operation in the declared type. ``c`` — C, interpreted by this operation in the declared type. ``dt`` — Elapsed time in seconds. |
+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool SupportsProfile(DriveProfile profile)``          | Checks movement-family compatibility; this is independent of the Unity enabled flag.                          | ``profile`` — Movement/surface configuration, according to its declared type. **Returns:** ``true`` when the described condition holds; ``false`` otherwise.    |
+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-surfacefeedback--state-and-configuration:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------+-----------------------------------------------------------------------------+
| Member                                            | Meaning                                                                     |
+===================================================+=============================================================================+
| ``public override int ExecutionOrder { get; }``   | Default local priority within phase/category.                               |
+---------------------------------------------------+-----------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }`` | Cross-category execution barrier used by the module pipeline.               |
+---------------------------------------------------+-----------------------------------------------------------------------------+
| ``public float handbrakeLateralGrip``             | Authored handbrake lateral grip used by Friction. Initial value: ``0.55f``. |
+---------------------------------------------------+-----------------------------------------------------------------------------+

.. _evs-api-surfacefeedback--surface:

Surface
-------

**Runtime/Physics/Friction/Surface.cs**

Stores the physical grip multiplier on a contact collider.

**Inherits / implements:** ``MonoBehaviour``.

.. _evs-api-surfacefeedback--state-and-configuration-1:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------+------------------------------------------------------+
| Member                | Meaning                                              |
+=======================+======================================================+
| ``public float grip`` | Authored grip used by Surface. Initial value: ``1``. |
+-----------------------+------------------------------------------------------+

.. _evs-api-surfacefeedback--tiresurface:

TireSurface
-----------

**Runtime/Effects/Surfaces/TireSurface.cs**

Maps a collider/hierarchy or Terrain layers to effect profiles.

**Inherits / implements:** ``MonoBehaviour``.

.. _evs-api-surfacefeedback--methods-1:

Methods
~~~~~~~

+-----------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                               | Role and behavior                                                                                                     | Arguments and result                                                                                                                                                                                                                       |
+=========================================================================================+=======================================================================================================================+============================================================================================================================================================================================================================================+
| ``[ContextMenu("Refresh terrain surface cache")] public virtual void RefreshTerrain()`` | Rebuilds cached painted-Terrain-layer classification after mapping/paint changes.                                     | No arguments; no returned value.                                                                                                                                                                                                           |
+-----------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual TireSurfaceProfile Resolve(Collider collider, Vector3 worldPoint)``    | Resolves the mapped effect profile for a native hit, including dominant Terrain-layer classification when configured. | ``collider`` — Native collider used for ownership/contact classification. ``worldPoint`` — World-space target/sample point. **Returns:** Returned ``TireSurfaceProfile``; ownership remains as specified by the creating/lookup operation. |
+-----------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-surfacefeedback--state-and-configuration-2:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------+-----------------------------------------------------------------------------------+
| Member                                               | Meaning                                                                           |
+======================================================+===================================================================================+
| ``public TireSurfaceProfile profile``                | Authored profile used by ``TireSurface``.                                         |
+------------------------------------------------------+-----------------------------------------------------------------------------------+
| ``public LayerMapping[] terrainLayers``              | Optional dominant painted layer mapping for a ``TerrainCollider`` on this object. |
+------------------------------------------------------+-----------------------------------------------------------------------------------+
| ``public static int Revision { get; private set; }`` | Shared revision invalidating contact surface caches after mapping changes.        |
+------------------------------------------------------+-----------------------------------------------------------------------------------+

.. _evs-api-surfacefeedback--tiresurfacelayermapping:

TireSurface.LayerMapping
------------------------

**Runtime/Effects/Surfaces/TireSurface.cs**

Value data for layer mapping; its fields are listed below.

.. _evs-api-surfacefeedback--state-and-configuration-3:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------+--------------------------------------------+
| Member                                | Meaning                                    |
+=======================================+============================================+
| ``public TerrainLayer layer``         | Authored layer used by ``LayerMapping``.   |
+---------------------------------------+--------------------------------------------+
| ``public TireSurfaceProfile profile`` | Authored profile used by ``LayerMapping``. |
+---------------------------------------+--------------------------------------------+

.. _evs-api-surfacefeedback--tiresurfaceprofile:

TireSurfaceProfile
------------------

**Runtime/Effects/Surfaces/TireSurfaceProfile.cs**

Stores presentation assets and effect multipliers.

**Inherits / implements:** ``ScriptableObject``.

.. _evs-api-surfacefeedback--methods-2:

Methods
~~~~~~~

+-----------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                       | Role and behavior                                                                  | Arguments and result                                                                                                                          |
+=================================================================+====================================================================================+===============================================================================================================================================+
| ``public virtual float Rolling(float speed)``                   | Evaluates this surface profile's rolling-presentation activity.                    | ``speed`` — Speed, interpreted by this operation in the declared type. **Returns:** Computed float in the operation's documented unit/domain. |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float ParticleActivity(WheelContact contact)`` | Evaluates tire-particle activity from rolling/skid inputs and profile multipliers. | ``contact`` — Normalized physical contact participation. **Returns:** Computed float in the operation's documented unit/domain.               |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float MarkActivity(WheelContact contact)``     | Evaluates skidmark activity using this surface profile's presentation multipliers. | ``contact`` — Normalized physical contact participation. **Returns:** Computed float in the operation's documented unit/domain.               |
+-----------------------------------------------------------------+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-surfacefeedback--state-and-configuration-4:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| Member                                  | Meaning                                                                                                                        |
+=========================================+================================================================================================================================+
| ``public float rollingParticles``       | Authored rolling particles used by ``TireSurfaceProfile``.                                                                     |
+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public float rollingMarks``           | Authored rolling marks used by ``TireSurfaceProfile``.                                                                         |
+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public float minimumRollingSpeed``    | Authored minimum rolling speed used by ``TireSurfaceProfile``. Initial value: ``1``.                                           |
+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public float fullRollingSpeed``       | Authored full rolling speed used by ``TireSurfaceProfile``. Initial value: ``12``.                                             |
+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public bool particlesEnabled``        | Authored particles enabled used by ``TireSurfaceProfile``. Initial value: ``true``.                                            |
+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public bool granularParticles``       | Use a separate, bounded grain spray pool instead of the smoke preset. Custom wheel systems/prefabs keep their authored design. |
+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public Material particleMaterial``    | Authored particle material used by ``TireSurfaceProfile``.                                                                     |
+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public Color particleColor``          | Authored particle color used by ``TireSurfaceProfile``. Initial value: ``new Color(.78f, .8f, .82f, .25f)``.                   |
+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector2 particleSize``         | Authored particle size used by ``TireSurfaceProfile``. Initial value: ``new Vector2(.32f, .58f)``.                             |
+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector2 particleLifetime``     | Authored particle lifetime used by ``TireSurfaceProfile``. Initial value: ``new Vector2(1.8f, 3.2f)``.                         |
+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector2 particleSpeed``        | Authored particle speed used by ``TireSurfaceProfile``. Initial value: ``new Vector2(.08f, .22f)``.                            |
+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public float particleGravity``        | Authored particle gravity used by ``TireSurfaceProfile``.                                                                      |
+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public float particleRateMultiplier`` | Authored particle rate multiplier used by ``TireSurfaceProfile``. Initial value: ``1``.                                        |
+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public bool marksEnabled``            | Authored marks enabled used by ``TireSurfaceProfile``. Initial value: ``true``.                                                |
+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public bool looseTracks``             | Draw irregular soil ruts instead of rubber grooves, within the same mesh/material.                                             |
+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public Color markColor``              | Authored mark color used by ``TireSurfaceProfile``. Initial value: ``new Color(.025f, .025f, .025f, .8f)``.                    |
+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public float markWidthMultiplier``    | Authored mark width multiplier used by ``TireSurfaceProfile``. Initial value: ``1``.                                           |
+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public float markLifetime``           | Time before tire marks on this surface fade away, in seconds.                                                                  |
+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public AudioClip tireLoop``           | Authored tire loop used by ``TireSurfaceProfile``.                                                                             |
+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public float tireVolume``             | Authored tire volume used by ``TireSurfaceProfile``. Initial value: ``.5f``.                                                   |
+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public float rollingAudio``           | Authored rolling audio used by ``TireSurfaceProfile``.                                                                         |
+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public float brakeAudioMultiplier``   | Scales the separate Brake Audio loop; use zero on loose ground when it contains tire squeal.                                   |
+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector2 pitchRange``           | Authored pitch range used by ``TireSurfaceProfile``. Initial value: ``new Vector2(.9f, 1.1f)``.                                |
+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
