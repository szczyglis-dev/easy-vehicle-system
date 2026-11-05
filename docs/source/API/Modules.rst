.. _evs-api-modules--module-lifecycle-and-scheduling-api:

Module lifecycle and scheduling API
===================================

Read :doc:`the system explanation </Scripting/Modules>` for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from ``MonoBehaviour``, ``Object`` or ``ScriptableObject`` are documented by Unity.

.. _evs-api-modules--types:

Types
-----

-  :ref:`CategoryCore <evs-api-modules--categorycore>`
-  :ref:`ExecutionPhase <evs-api-modules--executionphase>`
-  :ref:`ExteriorCore <evs-api-modules--exteriorcore>`
-  :ref:`ExteriorModule <evs-api-modules--exteriormodule>`
-  :ref:`ExternalReferenceAttribute <evs-api-modules--externalreferenceattribute>`
-  :ref:`IControllerModule <evs-api-modules--icontrollermodule>`
-  :ref:`IDriveModule <evs-api-modules--idrivemodule>`
-  :ref:`IEffectsModule <evs-api-modules--ieffectsmodule>`
-  :ref:`IEngineModule <evs-api-modules--ienginemodule>`
-  :ref:`IExteriorModule <evs-api-modules--iexteriormodule>`
-  :ref:`IInteriorModule <evs-api-modules--iinteriormodule>`
-  :ref:`IPhysicsModule <evs-api-modules--iphysicsmodule>`
-  :ref:`IVehicleModule <evs-api-modules--ivehiclemodule>`
-  :ref:`IVehicleResetHandler <evs-api-modules--ivehicleresethandler>`
-  :ref:`IWorldModule <evs-api-modules--iworldmodule>`
-  :ref:`ModuleCatalog <evs-api-modules--modulecatalog>`
-  :ref:`ModuleCategory <evs-api-modules--modulecategory>`
-  :ref:`ModuleSetupAttribute <evs-api-modules--modulesetupattribute>`
-  :ref:`PhysicsCore <evs-api-modules--physicscore>`
-  :ref:`PhysicsModule <evs-api-modules--physicsmodule>`
-  :ref:`VehicleModule <evs-api-modules--vehiclemodule>`
-  :ref:`VehicleResetReason <evs-api-modules--vehicleresetreason>`
-  :ref:`WorldCore <evs-api-modules--worldcore>`
-  :ref:`WorldModule <evs-api-modules--worldmodule>`

.. _evs-api-modules--categorycore:

CategoryCore
------------

**Runtime/Core/CategoryCore.cs**

Groups and orders registered modules within one category.

.. _evs-api-modules--state-and-configuration:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------+--------------------------------------------------------------------------------------+
| Member                                                   | Meaning                                                                              |
+==========================================================+======================================================================================+
| ``public abstract ModuleCategory Category { get; }``     | Module responsibility category; it does not independently determine execution phase. |
+----------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public int ExecutionOrder { get; internal set; }``     | Default local priority within phase/category.                                        |
+----------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public IReadOnlyList<VehicleModule> Modules { get; }`` | Read-only/resolved modules for ``CategoryCore``.                                     |
+----------------------------------------------------------+--------------------------------------------------------------------------------------+

.. _evs-api-modules--executionphase:

ExecutionPhase
--------------

**Runtime/Core/IVehicleModule.cs**

Defines the allowed execution phase choices used by this topic.

.. _evs-api-modules--values:

Values
~~~~~~

-  ``Contact``
-  ``Transmission``
-  ``Braking``
-  ``TrailerBraking``
-  ``Clutch``
-  ``Power``
-  ``Differential``
-  ``Steering``
-  ``Drive``
-  ``Friction``
-  ``Assistance``
-  ``Suspension``
-  ``Balance``
-  ``Presentation``
-  ``Coasting``
-  ``Parking``
-  ``WheelDynamics``
-  ``Feedback``
-  ``Collision``

.. _evs-api-modules--exteriorcore:

ExteriorCore
------------

**Runtime/Exterior/Core/ExteriorCore.cs**

Configuration/implementation type for exterior core within module lifecycle and scheduling.

**Inherits / implements:** :ref:`CategoryCore <evs-api-modules--categorycore>`.

.. _evs-api-modules--state-and-configuration-1:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------+--------------------------------------------------------------------------------------+
| Member                                               | Meaning                                                                              |
+======================================================+======================================================================================+
| ``public override ModuleCategory Category { get; }`` | Module responsibility category; it does not independently determine execution phase. |
+------------------------------------------------------+--------------------------------------------------------------------------------------+

.. _evs-api-modules--methods:

Methods
~~~~~~~

+---------------------------+--------------------------------------------------------------+--------------------------------------------------------------------+
| Signature                 | Role and behavior                                            | Arguments and result                                               |
+===========================+==============================================================+====================================================================+
| ``public ExteriorCore()`` | Constructs ``ExteriorCore`` with the supplied initial state. | **Returns:** New instance initialized from the supplied arguments. |
+---------------------------+--------------------------------------------------------------+--------------------------------------------------------------------+

.. _evs-api-modules--exteriormodule:

ExteriorModule
--------------

**Runtime/Exterior/Core/ExteriorModule.cs**

Base integration with the vehicle module lifecycle.

**Inherits / implements:** :ref:`VehicleModule <evs-api-modules--vehiclemodule>`, :ref:`IExteriorModule <evs-api-modules--iexteriormodule>`.

.. _evs-api-modules--state-and-configuration-2:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------+--------------------------------------------------------------------------------------+
| Member                                                      | Meaning                                                                              |
+=============================================================+======================================================================================+
| ``public sealed override ModuleCategory Category { get; }`` | Module responsibility category; it does not independently determine execution phase. |
+-------------------------------------------------------------+--------------------------------------------------------------------------------------+

.. _evs-api-modules--externalreferenceattribute:

ExternalReferenceAttribute
--------------------------

**Runtime/Core/ModuleSetupAttribute.cs**

Configuration/implementation type for external reference attribute within module lifecycle and scheduling.

**Inherits / implements:** ``Attribute``.

.. _evs-api-modules--icontrollermodule:

IControllerModule
-----------------

**Runtime/Core/IVehicleModule.cs**

Configuration/implementation type for icontroller module within module lifecycle and scheduling.

**Inherits / implements:** :ref:`IVehicleModule <evs-api-modules--ivehiclemodule>`.

.. _evs-api-modules--idrivemodule:

IDriveModule
------------

**Runtime/Core/IVehicleModule.cs**

Configuration/implementation type for idrive module within module lifecycle and scheduling.

**Inherits / implements:** :ref:`IVehicleModule <evs-api-modules--ivehiclemodule>`.

.. _evs-api-modules--ieffectsmodule:

IEffectsModule
--------------

**Runtime/Core/IVehicleModule.cs**

Configuration/implementation type for ieffects module within module lifecycle and scheduling.

**Inherits / implements:** :ref:`IVehicleModule <evs-api-modules--ivehiclemodule>`.

.. _evs-api-modules--ienginemodule:

IEngineModule
-------------

**Runtime/Core/IVehicleModule.cs**

Configuration/implementation type for iengine module within module lifecycle and scheduling.

**Inherits / implements:** :ref:`IVehicleModule <evs-api-modules--ivehiclemodule>`.

.. _evs-api-modules--iexteriormodule:

IExteriorModule
---------------

**Runtime/Core/IVehicleModule.cs**

Configuration/implementation type for iexterior module within module lifecycle and scheduling.

**Inherits / implements:** :ref:`IVehicleModule <evs-api-modules--ivehiclemodule>`.

.. _evs-api-modules--iinteriormodule:

IInteriorModule
---------------

**Runtime/Core/IVehicleModule.cs**

Configuration/implementation type for iinterior module within module lifecycle and scheduling.

**Inherits / implements:** :ref:`IVehicleModule <evs-api-modules--ivehiclemodule>`.

.. _evs-api-modules--iphysicsmodule:

IPhysicsModule
--------------

**Runtime/Core/IVehicleModule.cs**

Configuration/implementation type for iphysics module within module lifecycle and scheduling.

**Inherits / implements:** :ref:`IVehicleModule <evs-api-modules--ivehiclemodule>`.

.. _evs-api-modules--ivehiclemodule:

IVehicleModule
--------------

**Runtime/Core/IVehicleModule.cs**

Defines category interfaces and the cross-category ``ExecutionPhase`` sequence.

.. _evs-api-modules--state-and-configuration-3:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------+--------------------------------------------------------------------------------------+
| Member                               | Meaning                                                                              |
+======================================+======================================================================================+
| ``ModuleCategory Category { get; }`` | Module responsibility category; it does not independently determine execution phase. |
+--------------------------------------+--------------------------------------------------------------------------------------+
| ``int ExecutionOrder { get; }``      | Default local priority within phase/category.                                        |
+--------------------------------------+--------------------------------------------------------------------------------------+
| ``ExecutionPhase Phase { get; }``    | Cross-category execution barrier used by the module pipeline.                        |
+--------------------------------------+--------------------------------------------------------------------------------------+

.. _evs-api-modules--methods-1:

Methods
~~~~~~~

+----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                  | Role and behavior                                                                                                           | Arguments and result                                                                                                                                                                                                     |
+============================================================================+=============================================================================================================================+==========================================================================================================================================================================================================================+
| ``void Configure(VehicleController vehicle)``                              | Repeatable setup contract supplied with the owning ``VehicleController``.                                                   | ``vehicle`` — Vehicle context/owner receiving the operation.                                                                                                                                                             |
+----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``void Step(VehicleController vehicle, Command command, float deltaTime)`` | Contract for one owner-supplied fixed tick; implement only the module responsibility and use the supplied Command/timestep. | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-modules--ivehicleresethandler:

IVehicleResetHandler
--------------------

**Runtime/Core/IVehicleResetHandler.cs**

Presentation or lifecycle contract for independent vehicle components.

.. _evs-api-modules--methods-2:

Methods
~~~~~~~

+-------------------------------------------------------+-------------------------------------------------------------------------------------------------+----------------------+
| Signature                                             | Role and behavior                                                                               | Arguments and result |
+=======================================================+=================================================================================================+======================+
| ``void ResetVehicleState(VehicleResetReason reason)`` | Clears transient state for the supplied reset reason without changing persistent configuration. | —                    |
+-------------------------------------------------------+-------------------------------------------------------------------------------------------------+----------------------+

.. _evs-api-modules--iworldmodule:

IWorldModule
------------

**Runtime/Core/IVehicleModule.cs**

Configuration/implementation type for iworld module within module lifecycle and scheduling.

**Inherits / implements:** :ref:`IVehicleModule <evs-api-modules--ivehiclemodule>`.

.. _evs-api-modules--modulecatalog:

ModuleCatalog
-------------

**Runtime/Core/ModuleCatalog.cs**

Configuration/implementation type for module catalog within module lifecycle and scheduling.

.. _evs-api-modules--methods-3:

Methods
~~~~~~~

+----------------------------------------------+--------------------------------------------------------------+------------------------------------------------------------------------------------------------+
| Signature                                    | Role and behavior                                            | Arguments and result                                                                           |
+==============================================+==============================================================+================================================================================================+
| ``public static Type[] GetAvailableTypes()`` | Returns the catalog of eligible module implementation types. | **Returns:** Returned Type[]; ownership remains as specified by the creating/lookup operation. |
+----------------------------------------------+--------------------------------------------------------------+------------------------------------------------------------------------------------------------+

.. _evs-api-modules--modulecategory:

ModuleCategory
--------------

**Runtime/Core/IVehicleModule.cs**

Defines the allowed module category choices used by this topic.

.. _evs-api-modules--values-1:

Values
~~~~~~

-  ``Controller``
-  ``Physics``
-  ``Drive``
-  ``Engine``
-  ``Interior``
-  ``Exterior``
-  ``World``
-  ``Effects``

.. _evs-api-modules--modulesetupattribute:

ModuleSetupAttribute
--------------------

**Runtime/Core/ModuleSetupAttribute.cs**

Declares installation policy for full setup and module menus.

**Inherits / implements:** ``Attribute``.

.. _evs-api-modules--state-and-configuration-4:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------+---------------------------------------------------------------+
| Member                                         | Meaning                                                       |
+================================================+===============================================================+
| ``public bool EnabledByDefault { get; set; }`` | Configurable enabled by default for ``ModuleSetupAttribute``. |
+------------------------------------------------+---------------------------------------------------------------+
| ``public bool IncludeInFull { get; set; }``    | Configurable include in full for ``ModuleSetupAttribute``.    |
+------------------------------------------------+---------------------------------------------------------------+
| ``public bool ModuleOnly { get; set; }``       | Configurable module only for ``ModuleSetupAttribute``.        |
+------------------------------------------------+---------------------------------------------------------------+

.. _evs-api-modules--physicscore:

PhysicsCore
-----------

**Runtime/Physics/Core/PhysicsCore.cs**

Configuration/implementation type for physics core within module lifecycle and scheduling.

**Inherits / implements:** :ref:`CategoryCore <evs-api-modules--categorycore>`.

.. _evs-api-modules--state-and-configuration-5:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------+--------------------------------------------------------------------------------------+
| Member                                               | Meaning                                                                              |
+======================================================+======================================================================================+
| ``public override ModuleCategory Category { get; }`` | Module responsibility category; it does not independently determine execution phase. |
+------------------------------------------------------+--------------------------------------------------------------------------------------+

.. _evs-api-modules--methods-4:

Methods
~~~~~~~

+--------------------------+-------------------------------------------------------------+--------------------------------------------------------------------+
| Signature                | Role and behavior                                           | Arguments and result                                               |
+==========================+=============================================================+====================================================================+
| ``public PhysicsCore()`` | Constructs ``PhysicsCore`` with the supplied initial state. | **Returns:** New instance initialized from the supplied arguments. |
+--------------------------+-------------------------------------------------------------+--------------------------------------------------------------------+

.. _evs-api-modules--physicsmodule:

PhysicsModule
-------------

**Runtime/Physics/Core/PhysicsModule.cs**

Configuration/implementation type for physics module within module lifecycle and scheduling.

**Inherits / implements:** :ref:`VehicleModule <evs-api-modules--vehiclemodule>`, :ref:`IPhysicsModule <evs-api-modules--iphysicsmodule>`.

.. _evs-api-modules--state-and-configuration-6:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------+--------------------------------------------------------------------------------------+
| Member                                                      | Meaning                                                                              |
+=============================================================+======================================================================================+
| ``public sealed override ModuleCategory Category { get; }`` | Module responsibility category; it does not independently determine execution phase. |
+-------------------------------------------------------------+--------------------------------------------------------------------------------------+

.. _evs-api-modules--vehiclemodule:

VehicleModule
-------------

**Runtime/Core/VehicleModule.cs**

Exposes lifecycle notifications around registered module work.

**Inherits / implements:** ``MonoBehaviour``, :ref:`IVehicleModule <evs-api-modules--ivehiclemodule>`.

.. _evs-api-modules--events-and-inspector-callbacks:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| Member                                                                    | Meaning                                                                                                           |
+===========================================================================+===================================================================================================================+
| ``public event System.Action<VehicleController> Configured``              | After controller-driven module configuration. Payload: the owning ``VehicleController``.                          |
+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public event System.Action<bool> EnabledChanged``                       | After ``SetEnabled`` changes the module flag. Payload: requested enabled bool; no event for an unchanged request. |
+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public event System.Action<VehicleController, Command, float> Stepped`` | After this registered module has stepped. Payload: vehicle, sampled Command, timestep in seconds.                 |
+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+

.. _evs-api-modules--state-and-configuration-7:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                  | Meaning                                                                                                                                                                |
+=========================================================+========================================================================================================================================================================+
| ``public virtual ModuleCategory Category { get; }``     | Module responsibility category; it does not independently determine execution phase.                                                                                   |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual int EffectiveExecutionOrder { get; }`` | Local priority after optional Inspector override.                                                                                                                      |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual int ExecutionOrder { get; }``          | Default local priority within phase/category.                                                                                                                          |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public int localExecutionOrder``                      | Order within the module category and dependency phase when Override Execution Order is enabled. Smaller values run earlier.                                            |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool overrideExecutionOrder``                  | Override the default order inside this category and dependency phase.                                                                                                  |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual ExecutionPhase Phase { get; }``        | Cross-category execution barrier used by the module pipeline.                                                                                                          |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SupportsDirectControl { get; }``  | Allows this module to step while the selected source owns the chassis pose. Base default: interior/exterior/effects categories; force modules require explicit opt-in. |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SupportsReleasedForces { get; }`` | Opt-in for work that may continue during force release. Defaults to Interior/Exterior/Effects presentation; force-producing custom modules should keep false.          |
+---------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-modules--methods-5:

Methods
~~~~~~~

+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                 | Role and behavior                                                                                                                      | Arguments and result                                                                                                                                                                                                     |
+===========================================================================================+========================================================================================================================================+==========================================================================================================================================================================================================================+
| ``public virtual void Configure(VehicleController vehicle)``                              | Empty base setup hook. Derived components may cache references/apply persistent settings; the controller owns lifecycle notifications. | ``vehicle`` — Vehicle context/owner receiving the operation.                                                                                                                                                             |
+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetEnabled(bool value)``                                            | Changes module enabled state and publishes an actual requested-flag change.                                                            | ``value`` — Requested bool state for this operation.                                                                                                                                                                     |
+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Step(VehicleController vehicle, Command command, float deltaTime)`` | Empty base extension point. The controller schedules derived work and emits lifecycle notifications around it.                         | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SupportsProfile(DriveProfile profile)``                             | Checks movement-family compatibility; this is independent of the Unity enabled flag.                                                   | ``profile`` — Movement/surface configuration, according to its declared type. **Returns:** ``true`` when the described condition holds; ``false`` otherwise.                                                             |
+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-modules--vehicleresetreason:

VehicleResetReason
------------------

**Runtime/Core/IVehicleResetHandler.cs**

Reason for clearing transient vehicle state.

.. _evs-api-modules--values-2:

Values
~~~~~~

-  ``Respawn``
-  ``ForceStateChanged``

.. _evs-api-modules--worldcore:

WorldCore
---------

**Runtime/World/Core/WorldCore.cs**

Configuration/implementation type for world core within module lifecycle and scheduling.

**Inherits / implements:** :ref:`CategoryCore <evs-api-modules--categorycore>`.

.. _evs-api-modules--state-and-configuration-8:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------+--------------------------------------------------------------------------------------+
| Member                                               | Meaning                                                                              |
+======================================================+======================================================================================+
| ``public override ModuleCategory Category { get; }`` | Module responsibility category; it does not independently determine execution phase. |
+------------------------------------------------------+--------------------------------------------------------------------------------------+

.. _evs-api-modules--methods-6:

Methods
~~~~~~~

+------------------------+-----------------------------------------------------------+--------------------------------------------------------------------+
| Signature              | Role and behavior                                         | Arguments and result                                               |
+========================+===========================================================+====================================================================+
| ``public WorldCore()`` | Constructs ``WorldCore`` with the supplied initial state. | **Returns:** New instance initialized from the supplied arguments. |
+------------------------+-----------------------------------------------------------+--------------------------------------------------------------------+

.. _evs-api-modules--worldmodule:

WorldModule
-----------

**Runtime/World/Core/WorldModule.cs**

Configuration/implementation type for world module within module lifecycle and scheduling.

**Inherits / implements:** :ref:`VehicleModule <evs-api-modules--vehiclemodule>`, :ref:`IWorldModule <evs-api-modules--iworldmodule>`.

.. _evs-api-modules--state-and-configuration-9:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------+--------------------------------------------------------------------------------------+
| Member                                                      | Meaning                                                                              |
+=============================================================+======================================================================================+
| ``public sealed override ModuleCategory Category { get; }`` | Module responsibility category; it does not independently determine execution phase. |
+-------------------------------------------------------------+--------------------------------------------------------------------------------------+
