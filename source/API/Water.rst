.. _evs-api-water--water-sampling-and-movement-api:

Water sampling and movement API
===============================

Read :doc:`the system explanation </Scripting/Water>` for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from ``MonoBehaviour``, ``Object`` or ``ScriptableObject`` are documented by Unity.

.. _evs-api-water--types:

Types
-----

-  :ref:`SubmarineProfile <evs-api-water--submarineprofile>`
-  :ref:`WaterContact <evs-api-water--watercontact>`
-  :ref:`WaterInteraction <evs-api-water--waterinteraction>`
-  :ref:`WaterProvider <evs-api-water--waterprovider>`
-  :ref:`WaterSample <evs-api-water--watersample>`
-  :ref:`WaterStyle <evs-api-water--waterstyle>`
-  :ref:`WaterSurface <evs-api-water--watersurface>`

.. _evs-api-water--submarineprofile:

SubmarineProfile
----------------

**Runtime/Drive/Profiles/SubmarineProfile.cs**

Consumes water state for underwater movement.

**Inherits / implements:** :ref:`FreeProfile <evs-api-driveprofiles--freeprofile>`.

.. _evs-api-water--methods:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                  | Role and behavior                                                                                              | Arguments and result                                                                                                                                                                                                       |
+============================================================================================+================================================================================================================+============================================================================================================================================================================================================================+
| ``public SubmarineProfile()``                                                              | Constructs ``SubmarineProfile`` with the supplied initial state.                                               | **Returns:** New instance initialized from the supplied arguments.                                                                                                                                                         |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Samples valid water, applies immersion-dependent buoyancy/resistance and powered movement/depth-hold response. | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop.   |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool ContainsWater(Vector3 position)``                                    | Checks whether a position lies inside this profile's fallback water region.                                    | ``position`` — Requested point or switch detent; see its declared type and owning operation. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-water--state-and-configuration:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| Member                                     | Meaning                                                                                                                            |
+============================================+====================================================================================================================================+
| ``public override string Medium { get; }`` | Movement-family label used by the profile contract.                                                                                |
+--------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public float waterLevel``                | Flat fallback water-surface height in world metres.                                                                                |
+--------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector2 waterCenter``             | Authored water center used by ``SubmarineProfile``. Initial value: ``new Vector2(-280, 80)``.                                      |
+--------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector2 waterSize``               | Authored water size used by ``SubmarineProfile``. Initial value: ``new Vector2(400, 640)``.                                        |
+--------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public float hullHalfHeight``            | Authored hull half height used by ``SubmarineProfile``. Initial value: ``1.5f``.                                                   |
+--------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool holdDepth``                  | Hold the current world height after releasing ascend/dive controls. Requires propulsion power; disable for passive vertical drift. |
+--------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public float verticalAcceleration``      | Authored vertical acceleration used by ``SubmarineProfile``. Initial value: ``2``.                                                 |
+--------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public float lateralResistance``         | Authored lateral resistance used by ``SubmarineProfile``. Initial value: ``1.8f``.                                                 |
+--------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public float verticalResistance``        | Authored vertical resistance used by ``SubmarineProfile``. Initial value: ``2``.                                                   |
+--------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public float quadraticResistance``       | Authored quadratic resistance used by ``SubmarineProfile``. Initial value: ``.025f``.                                              |
+--------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public float yawRate``                   | Authored yaw rate used by ``SubmarineProfile``. Initial value: ``.42f``.                                                           |
+--------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public float turnResponse``              | Authored turn response used by ``SubmarineProfile``. Initial value: ``2``.                                                         |
+--------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumPitch``              | Authored maximum pitch used by ``SubmarineProfile``. Initial value: ``18``.                                                        |
+--------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public float levelingStrength``          | Authored leveling strength used by ``SubmarineProfile``. Initial value: ``4``.                                                     |
+--------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-water--watercontact:

WaterContact
------------

**Runtime/World/Water/WaterInteraction.cs**

Value data for water contact; its fields are listed below.

.. _evs-api-water--state-and-configuration-1:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------+---------------------------------------------------------------------+
| Member                              | Meaning                                                             |
+=====================================+=====================================================================+
| ``public bool wet``                 | Authored wet used by ``WaterContact``.                              |
+-------------------------------------+---------------------------------------------------------------------+
| ``public WaterSample surface``      | Copied water height, normal and flow at the hull sample.            |
+-------------------------------------+---------------------------------------------------------------------+
| ``public Vector2 halfSize``         | Authored half size used by ``WaterContact``.                        |
+-------------------------------------+---------------------------------------------------------------------+
| ``public Vector3 position``         | Authored position used by ``WaterContact``.                         |
+-------------------------------------+---------------------------------------------------------------------+
| ``public Vector3 forward``          | Authored forward used by ``WaterContact``.                          |
+-------------------------------------+---------------------------------------------------------------------+
| ``public Vector3 right``            | Authored right used by ``WaterContact``.                            |
+-------------------------------------+---------------------------------------------------------------------+
| ``public Vector3 relativeVelocity`` | Authored relative velocity used by ``WaterContact``.                |
+-------------------------------------+---------------------------------------------------------------------+
| ``public float speed``              | Authored speed used by ``WaterContact``.                            |
+-------------------------------------+---------------------------------------------------------------------+
| ``public float forwardSpeed``       | Authored forward speed used by ``WaterContact``.                    |
+-------------------------------------+---------------------------------------------------------------------+
| ``public float roll``               | Authored roll used by ``WaterContact``.                             |
+-------------------------------------+---------------------------------------------------------------------+
| ``public float pitch``              | Authored pitch used by ``WaterContact``.                            |
+-------------------------------------+---------------------------------------------------------------------+
| ``public float hullMotion``         | Authored hull motion used by ``WaterContact``.                      |
+-------------------------------------+---------------------------------------------------------------------+
| ``public float impact``             | Authored impact used by ``WaterContact``.                           |
+-------------------------------------+---------------------------------------------------------------------+
| ``public float leftEntry``          | Inward water-entry speeds at the hull sides, bow and stern, in m/s. |
+-------------------------------------+---------------------------------------------------------------------+
| ``public float rightEntry``         | Inward water-entry speeds at the hull sides, bow and stern, in m/s. |
+-------------------------------------+---------------------------------------------------------------------+
| ``public float bowEntry``           | Inward water-entry speeds at the hull sides, bow and stern, in m/s. |
+-------------------------------------+---------------------------------------------------------------------+
| ``public float sternEntry``         | Inward water-entry speeds at the hull sides, bow and stern, in m/s. |
+-------------------------------------+---------------------------------------------------------------------+

.. _evs-api-water--waterinteraction:

WaterInteraction
----------------

**Runtime/World/Water/WaterInteraction.cs**

Connects vehicle water sampling and hull contact state.

**Inherits / implements:** :ref:`WorldModule <evs-api-modules--worldmodule>`.

.. _evs-api-water--methods-1:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                                    | Role and behavior                                                                                                                                      | Arguments and result                                                                                                                                                                                                                                                                                                                              |
+==============================================================================================================+========================================================================================================================================================+===================================================================================================================================================================================================================================================================================================================================================+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)``                   | Samples the root center of mass and publishes a changed submerged/not-submerged state.                                                                 | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop.                                                                                                                          |
+--------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetInteractionEnabled(bool value)``                                                    | Changes the vehicle's water-interaction gate, affecting sampling/physics as well as its contact state.                                                 | ``value`` — Requested bool state for this operation.                                                                                                                                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetWaterProvider(WaterProvider provider)``                                             | Replaces the assigned water adapter and publishes the provider change.                                                                                 | ``provider`` — Assigned water adapter; ``null`` selects the configured fallback policy where supported.                                                                                                                                                                                                                                           |
+--------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TrySample(Vector3 worldPosition, out WaterSample sample)``                             | Queries valid water at a world position; ``false`` means no sample, not height zero.                                                                   | ``worldPosition`` — World-space query position in Unity metres. ``sample`` — Output water sample; read it only when sampling returns ``true``. **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values.                                                                                           |
+--------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public static bool TrySampleSurface(VehicleController vehicle, Vector3 position, out WaterSample sample)`` | Queries the provider's surface sample through vehicle water policy.                                                                                    | ``vehicle`` — Vehicle context/owner receiving the operation. ``position`` — Requested point or switch detent; see its declared type and owning operation. ``sample`` — Output water sample; read it only when sampling returns ``true``. **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values. |
+--------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public static WaterContact Read(VehicleController vehicle, Vector2 fallbackHalfSize)``                     | Builds surface-boat hull contact from the vehicle's water sampling and configured hull dimensions; non-Boat/dry/invalid vehicles return a dry contact. | ``vehicle`` — Vehicle context/owner receiving the operation. ``fallbackHalfSize`` — Half-width/half-length used when building fallback hull contact. **Returns:** Returned ``WaterContact``; ownership remains as specified by the creating/lookup operation.                                                                                     |
+--------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-water--events-and-inspector-callbacks:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| Declaration                                                    | Trigger, payload and meaning                                                                                     |
+================================================================+==================================================================================================================+
| ``public event System.Action<bool> InteractionEnabledChanged`` | When the master water-interaction gate changes. Payload: bool; the gate affects water physics, not just effects. |
+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``public event System.Action<WaterProvider> ProviderChanged``  | When assigned water provider changes. Payload: ``WaterProvider``, possibly ``null``.                             |
+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``public event System.Action<bool> SubmergedChanged``          | When sampled body-center submergence changes. Payload: bool; this is not an arbitrary hull wetness percentage.   |
+----------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+

.. _evs-api-water--state-and-configuration-2:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------+-------------------------------------------------------------------------------------------+
| Member                                                      | Meaning                                                                                   |
+=============================================================+===========================================================================================+
| ``public bool waterInteractionEnabled``                     | Master switch for water interaction: buoyancy, water audio and water particles.           |
+-------------------------------------------------------------+-------------------------------------------------------------------------------------------+
| ``public WaterProvider waterProvider``                      | Authored water provider used by ``WaterInteraction``.                                     |
+-------------------------------------------------------------+-------------------------------------------------------------------------------------------+
| ``public bool useProfileFallback``                          | Allow the Boat profile's flat water when no explicit provider is assigned.                |
+-------------------------------------------------------------+-------------------------------------------------------------------------------------------+
| ``public Vector2 hullHalfSize``                             | Half-width / half-length in metres, shared by water audio and particle contact points.    |
+-------------------------------------------------------------+-------------------------------------------------------------------------------------------+
| ``public virtual bool IsSubmerged { get; protected set; }`` | Current is submerged predicate; read it instead of maintaining a second application flag. |
+-------------------------------------------------------------+-------------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }``           | Cross-category execution barrier used by the module pipeline.                             |
+-------------------------------------------------------------+-------------------------------------------------------------------------------------------+

.. _evs-api-water--waterprovider:

WaterProvider
-------------

**Runtime/World/Water/WaterProvider.cs**

Abstract sampling adapter and ``WaterSample`` data contract.

**Inherits / implements:** ``MonoBehaviour``.

.. _evs-api-water--methods-2:

Methods
~~~~~~~

+-----------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                         | Role and behavior                                                                    | Arguments and result                                                                                                                                                                                                                                    |
+===================================================================================+======================================================================================+=========================================================================================================================================================================================================================================================+
| ``public abstract bool TrySample(Vector3 worldPosition, out WaterSample sample)`` | Queries valid water at a world position; ``false`` means no sample, not height zero. | ``worldPosition`` — World-space query position in Unity metres. ``sample`` — Output water sample; read it only when sampling returns ``true``. **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values. |
+-----------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-water--watersample:

WaterSample
-----------

**Runtime/World/Water/WaterProvider.cs**

Value data for water sample; its fields are listed below.

.. _evs-api-water--methods-3:

Methods
~~~~~~~

+------------------------------------------------------------------------+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                              | Role and behavior                                           | Arguments and result                                                                                                                                                                                                                         |
+========================================================================+=============================================================+==============================================================================================================================================================================================================================================+
| ``public WaterSample(float height, Vector3 normal, Vector3 velocity)`` | Constructs ``WaterSample`` with the supplied initial state. | ``height`` — Height, interpreted by this operation in the declared type. ``normal`` — Contact/surface normal in the declared frame. ``velocity`` — World velocity in m/s. **Returns:** New instance initialized from the supplied arguments. |
+------------------------------------------------------------------------+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-water--state-and-configuration-3:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------+-------------------------------------------------------------------+
| Member                      | Meaning                                                           |
+=============================+===================================================================+
| ``public float height``     | Sampled water surface world height in metres.                     |
+-----------------------------+-------------------------------------------------------------------+
| ``public Vector3 normal``   | World-space unit normal of sampled support/contact surface.       |
+-----------------------------+-------------------------------------------------------------------+
| ``public Vector3 velocity`` | World water-flow velocity including relevant wave motion, in m/s. |
+-----------------------------+-------------------------------------------------------------------+

.. _evs-api-water--waterstyle:

WaterStyle
----------

**Runtime/World/Water/WaterStyle.cs**

Configuration/implementation type for water style within water sampling and movement.

**Inherits / implements:** ``ScriptableObject``.

.. _evs-api-water--methods-4:

Methods
~~~~~~~

+---------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                         | Role and behavior                                                                                                     | Arguments and result                                                                                                                                                                                                                                                                                                                                             |
+===================================================================================================+=======================================================================================================================+==================================================================================================================================================================================================================================================================================================================================================================+
| ``public virtual WaterSample Sample(Vector3 position, float time, float baseHeight, bool waves)`` | Evaluates the configured water-wave style at a world position/time using base height and optional wave participation. | ``position`` — Requested point or switch detent; see its declared type and owning operation. ``time`` — Explicit sample time in seconds. ``baseHeight`` — World water baseline height. ``waves`` — Whether wave displacement participates in the sample. **Returns:** Returned ``WaterSample``; ownership remains as specified by the creating/lookup operation. |
+---------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-water--state-and-configuration-4:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------+----------------------------------------------------------------------------------------------------+
| Member                              | Meaning                                                                                            |
+=====================================+====================================================================================================+
| ``public Color deepColor``          | Authored deep color used by ``WaterStyle``. Initial value: ``new Color(.025f, .15f, .34f, 1)``.    |
+-------------------------------------+----------------------------------------------------------------------------------------------------+
| ``public Color shallowColor``       | Authored shallow color used by ``WaterStyle``. Initial value: ``new Color(.065f, .32f, .52f, 1)``. |
+-------------------------------------+----------------------------------------------------------------------------------------------------+
| ``public Color foamColor``          | Authored foam color used by ``WaterStyle``. Initial value: ``new Color(.7f, .88f, .87f, 1)``.      |
+-------------------------------------+----------------------------------------------------------------------------------------------------+
| ``public Vector4 waveA``            | Direction X/Z, wavelength in metres, amplitude in metres. Shared by CPU sampling and shader.       |
+-------------------------------------+----------------------------------------------------------------------------------------------------+
| ``public Vector4 waveB``            | Authored wave b used by ``WaterStyle``. Initial value: ``new Vector4(-.4f, .92f, 11, .045f)``.     |
+-------------------------------------+----------------------------------------------------------------------------------------------------+
| ``public float waveSpeed``          | Authored wave speed used by ``WaterStyle``. Initial value: ``.65f``.                               |
+-------------------------------------+----------------------------------------------------------------------------------------------------+
| ``public float rippleScale``        | Authored ripple scale used by ``WaterStyle``. Initial value: ``.055f``.                            |
+-------------------------------------+----------------------------------------------------------------------------------------------------+
| ``public float rippleStrength``     | Authored ripple strength used by ``WaterStyle``. Initial value: ``.13f``.                          |
+-------------------------------------+----------------------------------------------------------------------------------------------------+
| ``public float roughness``          | Authored roughness used by ``WaterStyle``. Initial value: ``.34f``.                                |
+-------------------------------------+----------------------------------------------------------------------------------------------------+
| ``public float reflectionStrength`` | Authored reflection strength used by ``WaterStyle``. Initial value: ``.8f``.                       |
+-------------------------------------+----------------------------------------------------------------------------------------------------+
| ``public float depthAbsorption``    | Authored depth absorption used by ``WaterStyle``. Initial value: ``.3f``.                          |
+-------------------------------------+----------------------------------------------------------------------------------------------------+
| ``public float shorelineFoam``      | Authored shoreline foam used by ``WaterStyle``. Initial value: ``.55f``.                           |
+-------------------------------------+----------------------------------------------------------------------------------------------------+

.. _evs-api-water--watersurface:

WaterSurface
------------

**Runtime/World/Water/WaterSurface.cs**

Built-in water-surface provider implementation.

**Inherits / implements:** :ref:`WaterProvider <evs-api-water--waterprovider>`.

.. _evs-api-water--methods-5:

Methods
~~~~~~~

+-----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                     | Role and behavior                                                                    | Arguments and result                                                                                                                                                                                                                                                                                                             |
+===============================================================================================+======================================================================================+==================================================================================================================================================================================================================================================================================================================================+
| ``public virtual void RenderSurface()``                                                       | Updates the built-in water surface's rendered representation.                        | No arguments; no returned value.                                                                                                                                                                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool TrySample(Vector3 position, out WaterSample sample)``                  | Queries valid water at a world position; ``false`` means no sample, not height zero. | ``position`` — Requested point or switch detent; see its declared type and owning operation. ``sample`` — Output water sample; read it only when sampling returns ``true``. **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values.                                             |
+-----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TrySampleAtTime(Vector3 position, float time, out WaterSample sample)`` | Queries the built-in water model at an explicit time for consistent wave evaluation. | ``position`` — Requested point or switch detent; see its declared type and owning operation. ``time`` — Explicit sample time in seconds. ``sample`` — Output water sample; read it only when sampling returns ``true``. **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values. |
+-----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-water--state-and-configuration-5:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| Member                                          | Meaning                                                                                                 |
+=================================================+=========================================================================================================+
| ``public bool waterEnabled``                    | Authored water enabled used by ``WaterSurface``. Initial value: ``true``.                               |
+-------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public bool renderSurface``                   | Authored render surface used by ``WaterSurface``. Initial value: ``true``.                              |
+-------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public bool animateWaves``                    | Enables time-varying wave height and normal instead of a flat surface.                                  |
+-------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public bool reflectionsEnabled``              | Authored reflections enabled used by ``WaterSurface``. Initial value: ``true``.                         |
+-------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public bool depthEffectsEnabled``             | Uses existing camera depth if available; no camera/depth/opaque passes are requested by this component. |
+-------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public WaterStyle style``                     | Authored style used by ``WaterSurface``.                                                                |
+-------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public Vector2 size``                         | Authored size used by ``WaterSurface``. Initial value: ``new Vector2(400, 640)``.                       |
+-------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public bool generateGrid``                    | Generate a bounded grid for vertex waves. Disable to retain your authored mesh.                         |
+-------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public float gridCellSize``                   | Authored grid cell size used by ``WaterSurface``. Initial value: ``5``.                                 |
+-------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public MeshRenderer surfaceRenderer``         | Authored surface renderer used by ``WaterSurface``.                                                     |
+-------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public Material materialOverride``            | Explicit water material; leave empty to retain the material authored on the renderer.                   |
+-------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public virtual int GridVertexCount { get; }`` | Read-only/resolved grid vertex count for ``WaterSurface``.                                              |
+-------------------------------------------------+---------------------------------------------------------------------------------------------------------+
| ``public virtual float SampleTime { get; }``    | Read-only/resolved sample time for ``WaterSurface``.                                                    |
+-------------------------------------------------+---------------------------------------------------------------------------------------------------------+
