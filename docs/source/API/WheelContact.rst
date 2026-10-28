.. _evs-api-wheelcontact--wheel-definitions-and-contact-api:

Wheel definitions and contact API
=================================

Read :doc:`the system explanation </Scripting/WheelContact>` for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from ``MonoBehaviour``, ``Object`` or ``ScriptableObject`` are documented by Unity.

.. _evs-api-wheelcontact--types:

Types
-----

-  :ref:`Coasting <evs-api-wheelcontact--coasting>`
-  :ref:`ContactEnvelope <evs-api-wheelcontact--contactenvelope>`
-  :ref:`TireCollision <evs-api-wheelcontact--tirecollision>`
-  :ref:`Wheel <evs-api-wheelcontact--wheel>`
-  :ref:`WheelDynamics <evs-api-wheelcontact--wheeldynamics>`
-  :ref:`WheelSetup <evs-api-wheelcontact--wheelsetup>`

.. _evs-api-wheelcontact--coasting:

Coasting
--------

**Runtime/Physics/Wheels/Coasting.cs**

Configuration/implementation type for coasting within wheel definitions and contact.

**Inherits / implements:** :ref:`PhysicsModule <evs-api-modules--physicsmodule>`.

.. _evs-api-wheelcontact--methods:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                  | Role and behavior                                                                                                | Arguments and result                                                                                                                                                                                                     |
+============================================================================================+==================================================================================================================+==========================================================================================================================================================================================================================+
| ``public override void Configure(VehicleController vehicle)``                              | Resolves the local Trailer so towing propulsion intent can participate in coasting policy.                       | ``vehicle`` — Vehicle context/owner receiving the operation.                                                                                                                                                             |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Releases native zero-torque holding according to propulsion intent while preserving service/handbrake ownership. | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool SupportsProfile(DriveProfile profile)``                             | Checks movement-family compatibility; this is independent of the Unity enabled flag.                             | ``profile`` — Movement/surface configuration, according to its declared type. **Returns:** ``true`` when the described condition holds; ``false`` otherwise.                                                             |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-wheelcontact--state-and-configuration:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------+-----------------------------------------------------------------------------------------------+
| Member                                            | Meaning                                                                                       |
+===================================================+===============================================================================================+
| ``public float contactReleaseTorque``             | Tiny intent torque in N·m. It releases native static tire constraints, not engine propulsion. |
+---------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``public float releaseBelowRpm``                  | Authored release below rpm used by Coasting. Initial value: ``15``.                           |
+---------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``public float minimumSlopeDegrees``              | Authored minimum slope degrees used by Coasting. Initial value: ``1``.                        |
+---------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``public override int ExecutionOrder { get; }``   | Default local priority within phase/category.                                                 |
+---------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }`` | Cross-category execution barrier used by the module pipeline.                                 |
+---------------------------------------------------+-----------------------------------------------------------------------------------------------+

.. _evs-api-wheelcontact--contactenvelope:

ContactEnvelope
---------------

**Runtime/Drive/Suspension/ContactEnvelope.cs**

Samples tire-shaped support and adjusts effective native support radius.

**Inherits / implements:** :ref:`DriveModule <evs-api-driveprofiles--drivemodule>`.

.. _evs-api-wheelcontact--methods-1:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                  | Role and behavior                                                                                                                  | Arguments and result                                                                                                                                                                                                     |
+============================================================================================+====================================================================================================================================+==========================================================================================================================================================================================================================+
| ``public override void Configure(VehicleController vehicle)``                              | Restores prior radii, stores the new owner, clears sampling history and resolves Suspension.                                       | ``vehicle`` — Vehicle context/owner receiving the operation.                                                                                                                                                             |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Samples supported circular tire geometry and updates effective native support radii; sleeping idle bodies use periodic resampling. | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool SupportsProfile(DriveProfile profile)``                             | Checks movement-family compatibility; this is independent of the Unity enabled flag.                                               | ``profile`` — Movement/surface configuration, according to its declared type. **Returns:** ``true`` when the described condition holds; ``false`` otherwise.                                                             |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-wheelcontact--state-and-configuration-1:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| Member                                                             | Meaning                                                                              |
+====================================================================+======================================================================================+
| ``public int longitudinalSamples``                                 | Authored longitudinal samples used by ``ContactEnvelope``. Initial value: ``9``.     |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public int widthSamples``                                        | Authored width samples used by ``ContactEnvelope``. Initial value: ``3``.            |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public float tireHalfWidth``                                     | Authored tire half width used by ``ContactEnvelope``. Initial value: ``.12f``.       |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public float maximumLiftRadius``                                 | Authored maximum lift radius used by ``ContactEnvelope``. Initial value: ``.8f``.    |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public LayerMask groundLayers``                                  | Authored ground layers used by ``ContactEnvelope``. Initial value: ``~0``.           |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public float minimumGroundNormal``                               | Authored minimum ground normal used by ``ContactEnvelope``. Initial value: ``.35f``. |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public virtual float MaximumCorrection { get; protected set; }`` | Largest active wheel-radius correction, in metres.                                   |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public override int ExecutionOrder { get; }``                    | Default local priority within phase/category.                                        |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }``                  | Cross-category execution barrier used by the module pipeline.                        |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public float supportRiseRate``                                   | Authored support rise rate used by ``ContactEnvelope``. Initial value: ``2``.        |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------+

.. _evs-api-wheelcontact--tirecollision:

TireCollision
-------------

**Runtime/Physics/Wheels/TireCollision.cs**

Adds supplemental solid tire contacts.

**Inherits / implements:** :ref:`PhysicsModule <evs-api-modules--physicsmodule>`.

.. _evs-api-wheelcontact--methods-2:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                  | Role and behavior                                                                                                                     | Arguments and result                                                                                                                                                                                                     |
+============================================================================================+=======================================================================================================================================+==========================================================================================================================================================================================================================+
| ``public override void Configure(VehicleController vehicle)``                              | During Play Mode, rebuilds owned transient tire proxies, clears pose history and resolves ``ContactEnvelope``.                        | ``vehicle`` — Vehicle context/owner receiving the operation.                                                                                                                                                             |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Advances supplemental tire proxies/contacts, detects discontinuous vehicle motion and preserves the primary rolling-support boundary. | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool SupportsProfile(DriveProfile profile)``                             | Checks movement-family compatibility; this is independent of the Unity enabled flag.                                                  | ``profile`` — Movement/surface configuration, according to its declared type. **Returns:** ``true`` when the described condition holds; ``false`` otherwise.                                                             |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-wheelcontact--state-and-configuration-2:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| Member                                                           | Meaning                                                                               |
+==================================================================+=======================================================================================+
| ``public float radiusScale``                                     | Authored radius scale used by ``TireCollision``. Initial value: ``.99f``.             |
+------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| ``public int cylinderSides``                                     | Authored cylinder sides used by ``TireCollision``. Initial value: ``32``.             |
+------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| ``public float supportNormalThreshold``                          | Authored support normal threshold used by ``TireCollision``. Initial value: ``.55f``. |
+------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| ``public float treadFriction``                                   | Authored tread friction used by ``TireCollision``. Initial value: ``1``.              |
+------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| ``public virtual int TreadContactCount { get; protected set; }`` | Read-only/resolved tread contact count for ``TireCollision``.                         |
+------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| ``public virtual float TreadImpulse { get; protected set; }``    | Read-only/resolved tread impulse for ``TireCollision``.                               |
+------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| ``public override int ExecutionOrder { get; }``                  | Default local priority within phase/category.                                         |
+------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }``                | Cross-category execution barrier used by the module pipeline.                         |
+------------------------------------------------------------------+---------------------------------------------------------------------------------------+

.. _evs-api-wheelcontact--wheel:

Wheel
-----

**Runtime/Physics/Wheels/Wheel.cs**

:doc:`Wheel contact </API/WheelContact>`

**Inherits / implements:** ``MonoBehaviour``.

.. _evs-api-wheelcontact--methods-3:

Methods
~~~~~~~

+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Signature                           | Role and behavior                                                                                                            | Arguments and result             |
+=====================================+==============================================================================================================================+==================================+
| ``public virtual void Configure()`` | Applies clamped native radius/mass, captures contact radius and configures native substeps when attached to a ``Rigidbody``. | No arguments; no returned value. |
+-------------------------------------+------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _evs-api-wheelcontact--state-and-configuration-3:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| Member                                                       | Meaning                                                                                                          |
+==============================================================+==================================================================================================================+
| ``public Transform visual``                                  | Authored visual used by Wheel.                                                                                   |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``public Transform caliper``                                 | Authored caliper used by Wheel.                                                                                  |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``public bool steering``                                     | Authored steering used by Wheel.                                                                                 |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``public bool driven``                                       | Authored driven used by Wheel. Initial value: ``true``.                                                          |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``public bool brake``                                        | Authored brake used by Wheel. Initial value: ``true``.                                                           |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``public bool handbrake``                                    | Authored handbrake used by Wheel.                                                                                |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``public float width``                                       | Authored width used by Wheel. Initial value: ``.2f``.                                                            |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``public float mass``                                        | Authored mass used by Wheel. Initial value: ``25``.                                                              |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``public float radius``                                      | Authored radius used by Wheel. Initial value: ``.34f``.                                                          |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``public float steeringMultiplier``                          | Authored steering multiplier used by Wheel. Initial value: ``1``.                                                |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``public float driveWeight``                                 | Authored drive weight used by Wheel. Initial value: ``1``.                                                       |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``public float brakeMultiplier``                             | Authored brake multiplier used by Wheel. Initial value: ``1``.                                                   |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``public Quaternion visualRotationOffset``                   | Authored visual rotation offset used by Wheel. Initial value: ``Quaternion.identity``.                           |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``public Quaternion caliperRotationOffset``                  | Authored caliper rotation offset used by Wheel. Initial value: ``Quaternion.identity``.                          |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``public float visualSuspensionSmoothTime``                  | Visual suspension settling time in seconds. Zero follows the native hub directly; tire forces are unaffected.    |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``public virtual WheelCollider Collider { get; }``           | Native ``WheelCollider`` used by this adapter.                                                                   |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool IsOperational { get; }``               | Whether this wheel adapter/native collider is currently available for operation.                                 |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool Grounded { get; }``                    | Whether the wheel reports applicable loaded tread contact; not a substitute for every native-road-contact check. |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``public virtual float Compression { get; protected set; }`` | Resolved suspension compression of the configured wheel.                                                         |
+--------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+

.. _evs-api-wheelcontact--wheeldynamics:

WheelDynamics
-------------

**Runtime/Physics/Wheels/WheelDynamics.cs**

Applies wheel rotational behavior including airborne losses.

**Inherits / implements:** :ref:`PhysicsModule <evs-api-modules--physicsmodule>`.

.. _evs-api-wheelcontact--methods-4:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                  | Role and behavior                                                                                      | Arguments and result                                                                                                                                                                                                     |
+============================================================================================+========================================================================================================+==========================================================================================================================================================================================================================+
| ``public override void Configure(VehicleController vehicle)``                              | Caches owner/Suspension and captures each wheel's grounded damping baseline.                           | ``vehicle`` — Vehicle context/owner receiving the operation.                                                                                                                                                             |
+--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Updates native rotational damping, including airborne bearing losses independently of service braking. | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool SupportsProfile(DriveProfile profile)``                             | Checks movement-family compatibility; this is independent of the Unity enabled flag.                   | ``profile`` — Movement/surface configuration, according to its declared type. **Returns:** ``true`` when the described condition holds; ``false`` otherwise.                                                             |
+--------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-wheelcontact--state-and-configuration-4:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------+-----------------------------------------------------------------------------------+
| Member                                            | Meaning                                                                           |
+===================================================+===================================================================================+
| ``public float airborneSpinHalfLife``             | Authored airborne spin half life used by ``WheelDynamics``. Initial value: ``2``. |
+---------------------------------------------------+-----------------------------------------------------------------------------------+
| ``public override int ExecutionOrder { get; }``   | Default local priority within phase/category.                                     |
+---------------------------------------------------+-----------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }`` | Cross-category execution barrier used by the module pipeline.                     |
+---------------------------------------------------+-----------------------------------------------------------------------------------+

.. _evs-api-wheelcontact--wheelsetup:

WheelSetup
----------

**Runtime/Physics/Wheels/WheelSetup.cs**

Persists collider, geometry, visual and wheel-role authoring data.

.. _evs-api-wheelcontact--methods-5:

Methods
~~~~~~~

+-----------------------------------------------------+---------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                           | Role and behavior                                                   | Arguments and result                                                                                                                                                       |
+=====================================================+=====================================================================+============================================================================================================================================================================+
| ``public static WheelSetup FromWheel(Wheel wheel)`` | Builds an authored wheel definition from an existing wheel adapter. | ``wheel`` — Native wheel or wheel adapter being configured/queried. **Returns:** Returned ``WheelSetup``; ownership remains as specified by the creating/lookup operation. |
+-----------------------------------------------------+---------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-wheelcontact--state-and-configuration-5:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------+--------------------------------------------------------------------------------------------------+
| Member                                      | Meaning                                                                                          |
+=============================================+==================================================================================================+
| ``public string label``                     | Authored label used by ``WheelSetup``. Initial value: ``"Wheel"``.                               |
+---------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public bool enabled``                     | Authored enabled used by ``WheelSetup``. Initial value: ``true``.                                |
+---------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public WheelCollider wheelCollider``      | Authored wheel collider used by ``WheelSetup``.                                                  |
+---------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public Transform wheelTransform``         | Authored wheel transform used by ``WheelSetup``.                                                 |
+---------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public Transform caliperTransform``       | Authored caliper transform used by ``WheelSetup``.                                               |
+---------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public bool steer``                       | Authored steer used by ``WheelSetup``.                                                           |
+---------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public bool drive``                       | Authored drive used by ``WheelSetup``. Initial value: ``true``.                                  |
+---------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public bool brake``                       | Authored brake used by ``WheelSetup``. Initial value: ``true``.                                  |
+---------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public bool handbrake``                   | Authored handbrake used by ``WheelSetup``.                                                       |
+---------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public float width``                      | Authored width used by ``WheelSetup``. Initial value: ``.2f``.                                   |
+---------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public float mass``                       | Authored mass used by ``WheelSetup``. Initial value: ``25``.                                     |
+---------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public float radius``                     | Authored radius used by ``WheelSetup``. Initial value: ``.45f``.                                 |
+---------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public float steeringMultiplier``         | Use negative values for counter-steering axles.                                                  |
+---------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public float driveWeight``                | Authored drive weight used by ``WheelSetup``. Initial value: ``1``.                              |
+---------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public float brakeMultiplier``            | Authored brake multiplier used by ``WheelSetup``. Initial value: ``1``.                          |
+---------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public Quaternion wheelRotationOffset``   | Authored wheel rotation offset used by ``WheelSetup``. Initial value: ``Quaternion.identity``.   |
+---------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public Quaternion caliperRotationOffset`` | Authored caliper rotation offset used by ``WheelSetup``. Initial value: ``Quaternion.identity``. |
+---------------------------------------------+--------------------------------------------------------------------------------------------------+
