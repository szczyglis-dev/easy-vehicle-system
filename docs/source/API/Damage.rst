.. _evs-api-damage--body-operation-and-damage-api:

Body operation and damage API
=============================

Read :doc:`the system explanation </Scripting/Damage>` for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from ``MonoBehaviour``, ``Object`` or ``ScriptableObject`` are documented by Unity.

.. _evs-api-damage--types:

Types
-----

-  :ref:`Body <evs-api-damage--body>`
-  :ref:`BodyPart <evs-api-damage--bodypart>`
-  :ref:`Damage <evs-api-damage--damage>`
-  :ref:`DamageCollisionRelay <evs-api-damage--damagecollisionrelay>`
-  :ref:`DamageHit <evs-api-damage--damagehit>`
-  :ref:`DamagePart <evs-api-damage--damagepart>`
-  :ref:`ICollisionDamageResponse <evs-api-damage--icollisiondamageresponse>`
-  :ref:`MeshDeformation <evs-api-damage--meshdeformation>`
-  :ref:`PartType <evs-api-damage--parttype>`
-  :ref:`PartMaterial <evs-api-damage--partmaterial>`

.. _evs-api-damage--body:

Body
----

**Runtime/Exterior/Parts/Body.cs**

Finds and operates authored ``BodyPart`` entries.

**Inherits / implements:** :ref:`ExteriorModule <evs-api-modules--exteriormodule>`.

.. _evs-api-damage--methods:

Methods
~~~~~~~

+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                   | Role and behavior                                                                                                                | Arguments and result                                                                                                                                                                                 |
+=============================================================+==================================================================================================================================+======================================================================================================================================================================================================+
| ``public virtual BodyPart GetPart(string id)``              | Finds the authored body part by its case-sensitive ID.                                                                           | ``id`` — Case-sensitive authored body-part identifier. **Returns:** Returned ``BodyPart``; ownership remains as specified by the creating/lookup operation.                                          |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool Open(string id)``                     | Requests opening of this part or the body part selected by ID.                                                                   | ``id`` — Case-sensitive authored body-part identifier. **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values.                                      |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool Close(string id)``                    | Requests closure of this part or the body part selected by ID.                                                                   | ``id`` — Case-sensitive authored body-part identifier. **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values.                                      |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool Toggle(string id)``                   | Requests the opposite current body/switch/wiper/profile/gear state through the declaring component.                              | ``id`` — Case-sensitive authored body-part identifier. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated.                 |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SetPhysics(string id, bool enabled)`` | Looks up the case-sensitive part ID and requests that part's physics policy, returning ``false`` when no eligible target exists. | ``id`` — Case-sensitive authored body-part identifier. ``enabled`` — Requested enable flag. **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values. |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SetOpen(string id, bool open)``       | Requests a body part's open/closed target.                                                                                       | ``id`` — Case-sensitive authored body-part identifier. ``open`` — Requested open state. **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values.     |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void OpenAll()``                           | Requests opening of every eligible authored body part.                                                                           | No arguments; no returned value.                                                                                                                                                                     |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void CloseAll()``                          | Requests closure of every eligible authored body part.                                                                           | No arguments; no returned value.                                                                                                                                                                     |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-damage--state-and-configuration:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------+--------------------------------------------------------------------------+
| Member                      | Meaning                                                                  |
+=============================+==========================================================================+
| ``public BodyPart[] parts`` | Authored parts used by Body. Initial value: ``Array.Empty<BodyPart>()``. |
+-----------------------------+--------------------------------------------------------------------------+

.. _evs-api-damage--bodypart:

BodyPart
--------

**Runtime/Exterior/Parts/BodyPart.cs**

Defines a named opening/moving body element.

**Inherits / implements:** ``MonoBehaviour``.

.. _evs-api-damage--methods-1:

Methods
~~~~~~~

+----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------+
| Signature                                          | Role and behavior                                                                                                                     | Arguments and result                                 |
+====================================================+=======================================================================================================================================+======================================================+
| ``public virtual void RefreshIgnoredCollisions()`` | Refreshes collision pairs for a body part after ownership/geometry changes.                                                           | No arguments; no returned value.                     |
+----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------+
| ``public virtual void Open()``                     | Requests opening of this part or the body part selected by ID.                                                                        | No arguments; no returned value.                     |
+----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------+
| ``public virtual void Close()``                    | Requests closure of this part or the body part selected by ID.                                                                        | No arguments; no returned value.                     |
+----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------+
| ``public virtual void Toggle()``                   | Requests the opposite current body/switch/wiper/profile/gear state through the declaring component.                                   | No arguments; no returned value.                     |
+----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------+
| ``public virtual void SetOpen(bool value)``        | Requests a body part's open/closed target.                                                                                            | ``value`` — Requested bool state for this operation. |
+----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------+
| ``public virtual void SetPhysics(bool value)``     | Changes ``usePhysics`` for an unreleased part and emits ``PhysicsChanged`` only on an actual policy change; released parts ignore it. | ``value`` — Requested bool state for this operation. |
+----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------+
| ``public virtual void Release()``                  | Releases this part or hand pose through its declaring type's ownership boundary.                                                      | No arguments; no returned value.                     |
+----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------+

.. _evs-api-damage--events-and-inspector-callbacks:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Declaration                                         | Trigger, payload and meaning                                                                      |
+=====================================================+===================================================================================================+
| ``public event System.Action<bool> OpenChanged``    | When the part's requested open state changes. Payload: bool; this is not a generic arrival event. |
+-----------------------------------------------------+---------------------------------------------------------------------------------------------------+
| ``public event System.Action<bool> PhysicsChanged`` | When the part's ``usePhysics`` policy changes. Payload: bool.                                     |
+-----------------------------------------------------+---------------------------------------------------------------------------------------------------+
| ``public event System.Action Released``             | After the body part is released from vehicle-owned motion. No payload.                            |
+-----------------------------------------------------+---------------------------------------------------------------------------------------------------+

.. _evs-api-damage--state-and-configuration-1:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| Member                                                     | Meaning                                                                                                    |
+============================================================+============================================================================================================+
| ``public string partId``                                   | Authored part id used by ``BodyPart``.                                                                     |
+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public PartType partType``                               | Authored part type used by ``BodyPart``.                                                                   |
+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public Vector3 hingeAxis``                               | Authored hinge axis used by ``BodyPart``. Initial value: ``Vector3.up``.                                   |
+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public Vector3 hingeAnchor``                             | Hinge position in this transform's local mesh coordinates. Zero uses its origin.                           |
+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public float openAngle``                                 | Authored open angle used by ``BodyPart``. Initial value: ``70``.                                           |
+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public float speed``                                     | Authored speed used by ``BodyPart``. Initial value: ``100``.                                               |
+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public float mass``                                      | Authored mass used by ``BodyPart``. Initial value: ``15``.                                                 |
+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public float releasedCollisionDelay``                    | Minimum seconds to ignore former vehicle collisions after release. Overlapping pairs wait until separated. |
+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public bool usePhysics``                                 | Uses a physical hinge instead of directly animating the part transform.                                    |
+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public float spring``                                    | Authored spring used by ``BodyPart``. Initial value: ``300``.                                              |
+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public float damper``                                    | Authored damper used by ``BodyPart``. Initial value: ``50``.                                               |
+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public virtual bool IsOpen { get; }``                    | Current is open predicate; read it instead of maintaining a second application flag.                       |
+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public virtual float CurrentAngle { get; }``             | Read-only/resolved current angle for ``BodyPart``.                                                         |
+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public virtual bool IsReleased { get; protected set; }`` | Current is released predicate; read it instead of maintaining a second application flag.                   |
+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public virtual HingeJoint Joint { get; }``               | Read-only/resolved joint for ``BodyPart``.                                                                 |
+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+

.. _evs-api-damage--damage:

Damage
------

**Runtime/Physics/Damage/Damage.cs**

Accepts impacts and routes them to damage/deformation boundaries.

**Inherits / implements:** :ref:`PhysicsModule <evs-api-modules--physicsmodule>`.

.. _evs-api-damage--methods-2:

Methods
~~~~~~~

+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                           | Role and behavior                                                                     | Arguments and result                                                                                                                                                                                                    |
+=====================================================================================+=======================================================================================+=========================================================================================================================================================================================================================+
| ``public override void Configure(VehicleController vehicle)``                       | Binds collision/impact processing to the supplied vehicle.                            | ``vehicle`` — Vehicle context/owner receiving the operation.                                                                                                                                                            |
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ApplyImpact(Vector3 point, Vector3 direction, float amount)`` | Submits a scripted impact to the damage system, subject to its enabled damage policy. | ``point`` — Geometry point in the declared coordinate frame. ``direction`` — Direction, interpreted by this operation in the declared type. ``amount`` — Requested damage/repair amount in the mechanic's damage units. |
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ReceiveImpact(Impact impact)``                                | Processes a copied impact snapshot through vehicle damage policy.                     | ``impact`` — Impact, interpreted by this operation in the declared type.                                                                                                                                                |
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-damage--events-and-inspector-callbacks-1:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------+-------------------------------------------------------------------------------------------------------+
| Declaration                            | Trigger, payload and meaning                                                                          |
+========================================+=======================================================================================================+
| ``public event Action<DamageHit> Hit`` | When a damage hit is accepted. Payload: ``DamageHit``; mesh upload can occur later in ``LateUpdate``. |
+----------------------------------------+-------------------------------------------------------------------------------------------------------+

.. _evs-api-damage--state-and-configuration-2:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------+------------------------------------------------------------------------------+
| Member                              | Meaning                                                                      |
+=====================================+==============================================================================+
| ``public bool damageEnabled``       | Authored damage enabled used by Damage. Initial value: ``true``.             |
+-------------------------------------+------------------------------------------------------------------------------+
| ``public bool deformationEnabled``  | Authored deformation enabled used by Damage. Initial value: ``true``.        |
+-------------------------------------+------------------------------------------------------------------------------+
| ``public bool detachmentEnabled``   | Authored detachment enabled used by Damage. Initial value: ``true``.         |
+-------------------------------------+------------------------------------------------------------------------------+
| ``public float minimumImpactSpeed`` | Authored minimum impact speed used by Damage. Initial value: ``3``.          |
+-------------------------------------+------------------------------------------------------------------------------+
| ``public float damageMultiplier``   | Authored damage multiplier used by Damage. Initial value: ``1``.             |
+-------------------------------------+------------------------------------------------------------------------------+
| ``public float impactRadius``       | Authored impact radius used by Damage. Initial value: ``.9f``.               |
+-------------------------------------+------------------------------------------------------------------------------+
| ``public float dentPerDamage``      | Visual displacement per accepted damage unit, in metres.                     |
+-------------------------------------+------------------------------------------------------------------------------+
| ``public float maximumDent``        | Largest total vertex displacement from its rest pose, in metres.             |
+-------------------------------------+------------------------------------------------------------------------------+
| ``public DamagePart[] parts``       | Authored parts used by Damage. Initial value: ``Array.Empty<DamagePart>()``. |
+-------------------------------------+------------------------------------------------------------------------------+

.. _evs-api-damage--damagecollisionrelay:

DamageCollisionRelay
--------------------

**Runtime/Physics/Damage/DamageCollisionRelay.cs**

Relays relevant native collisions into damage handling.

**Inherits / implements:** ``MonoBehaviour``.

.. _evs-api-damage--damagehit:

DamageHit
---------

**Runtime/Physics/Damage/Damage.cs**

Value data for damage hit; its fields are listed below.

.. _evs-api-damage--methods-3:

Methods
~~~~~~~

+---------------------------------------------------------------------------------------+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                             | Role and behavior                                         | Arguments and result                                                                                                                                                                                                                                                                                                                                              |
+=======================================================================================+===========================================================+===================================================================================================================================================================================================================================================================================================================================================================+
| ``public DamageHit(DamagePart part, Vector3 point, Vector3 direction, float amount)`` | Constructs ``DamageHit`` with the supplied initial state. | ``part`` — Selected body-part enum or part configuration, as declared. ``point`` — Geometry point in the declared coordinate frame. ``direction`` — Direction, interpreted by this operation in the declared type. ``amount`` — Requested damage/repair amount in the mechanic's damage units. **Returns:** New instance initialized from the supplied arguments. |
+---------------------------------------------------------------------------------------+-----------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-damage--state-and-configuration-3:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Member                                | Meaning                                                                                                                             |
+=======================================+=====================================================================================================================================+
| ``public readonly DamagePart Part``   | Damage boundary selected for this copied hit.                                                                                       |
+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``public readonly Vector3 Point``     | Point: copied world-space contact or impact position; Direction: world-space direction in which the hit deforms or pushes the part. |
+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``public readonly Vector3 Direction`` | Point: copied world-space contact or impact position; Direction: world-space direction in which the hit deforms or pushes the part. |
+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``public readonly float Amount``      | Read-only amount stored by this snapshot/data object.                                                                               |
+---------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-damage--damagepart:

DamagePart
----------

**Runtime/Exterior/Parts/DamagePart.cs**

``Tracks`` a part's damage and detachment behavior.

**Inherits / implements:** ``MonoBehaviour``.

.. _evs-api-damage--methods-4:

Methods
~~~~~~~

+-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                             | Role and behavior                                                                                                                | Arguments and result                                                                                                                                                                                              |
+=======================================================+==================================================================================================================================+===================================================================================================================================================================================================================+
| ``public virtual bool Detach(Rigidbody vehicleBody)`` | Ends the owned character or hitch relationship and releases the state/resources owned by that relationship.                      | ``vehicleBody`` — Vehicle body, interpreted by this operation in the declared type. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
+-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float Repair(float amount)``         | Removes up to the requested nonnegative damage amount and returns the actual repaired amount. Does not reattach a detached part. | ``amount`` — Requested damage/repair amount in the mechanic's damage units. **Returns:** Actual damage removed.                                                                                                   |
+-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ReceiveDamage(float amount)``   | Applies an accepted damage amount to this damage part and evaluates its detachment threshold.                                    | ``amount`` — Requested damage/repair amount in the mechanic's damage units.                                                                                                                                       |
+-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-damage--events-and-inspector-callbacks-2:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------+--------------------------------------------------------------------------------+
| Declaration                                         | Trigger, payload and meaning                                                   |
+=====================================================+================================================================================+
| ``public event Action<DamagePart> Detached``        | After a damage part detaches. Payload: that ``DamagePart``.                    |
+-----------------------------------------------------+--------------------------------------------------------------------------------+
| ``public event Action<DamagePart, float> Damaged``  | After the part accepts damage. Payload: ``DamagePart`` and accepted amount.    |
+-----------------------------------------------------+--------------------------------------------------------------------------------+
| ``public event Action<DamagePart, float> Repaired`` | After damage is actually removed. Payload: ``DamagePart`` and repaired amount. |
+-----------------------------------------------------+--------------------------------------------------------------------------------+

.. _evs-api-damage--state-and-configuration-4:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| Member                                                     | Meaning                                                                                                    |
+============================================================+============================================================================================================+
| ``public string partId``                                   | Stable identifier for scripts and damage reactions.                                                        |
+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public PartMaterial material``                           | Authored material used by ``DamagePart``. Initial value: ``PartMaterial.Metal``.                           |
+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public float deformationMultiplier``                     | Zero disables mesh dents. Does not affect detachment.                                                      |
+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public float detachmentMultiplier``                      | Zero prevents collision detachment.                                                                        |
+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public float detachThreshold``                           | Accumulated damage required to detach this group.                                                          |
+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public float mass``                                      | Authored mass used by ``DamagePart``. Initial value: ``15``.                                               |
+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public float releasedCollisionDelay``                    | Minimum seconds to ignore former vehicle collisions after release. Overlapping pairs wait until separated. |
+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public MeshFilter[] deformableMeshes``                   | Authored deformable meshes used by ``DamagePart``. Initial value: ``Array.Empty<MeshFilter>()``.           |
+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public virtual bool IsDetached { get; protected set; }`` | Current is detached predicate; read it instead of maintaining a second application flag.                   |
+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public virtual float Damage { get; protected set; }``    | Read-only/resolved damage for ``DamagePart``.                                                              |
+------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+

.. _evs-api-damage--icollisiondamageresponse:

ICollisionDamageResponse
------------------------

**Runtime/Physics/Damage/ICollisionDamageResponse.cs**

Lets a target alter collision damage severity.

.. _evs-api-damage--state-and-configuration-5:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------+-----------------------------------------------------------------------------+
| Member                                  | Meaning                                                                     |
+=========================================+=============================================================================+
| ``float CollisionDamageScale { get; }`` | Read-only/resolved collision damage scale for ``ICollisionDamageResponse``. |
+-----------------------------------------+-----------------------------------------------------------------------------+

.. _evs-api-damage--meshdeformation:

MeshDeformation
---------------

**Runtime/Physics/Damage/MeshDeformation.cs**

Owns readable mesh instances, dent buffers and geometry restoration.

**Inherits / implements:** :ref:`PhysicsModule <evs-api-modules--physicsmodule>`.

.. _evs-api-damage--methods-5:

Methods
~~~~~~~

+-----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                           | Role and behavior                                                                     | Arguments and result                                                                                                                                                                                                                                                            |
+=====================================================================================================+=======================================================================================+=================================================================================================================================================================================================================================================================================+
| ``public virtual void RestoreShape()``                                                              | Restores owned deformable meshes to their captured rest geometry.                     | No arguments; no returned value.                                                                                                                                                                                                                                                |
+-----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Deform(DamageHit hit, float radius, float dentPerDamage, float maximumDent)`` | Queues a bounded dent in readable mesh geometry around a supplied local impact point. | ``hit`` — Hit, interpreted by this operation in the declared type. ``radius`` — Geometry influence/tube radius in the declared units. ``dentPerDamage`` — Dent displacement scale per accepted damage amount. ``maximumDent`` — Maximum displacement relative to rest geometry. |
+-----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-damage--events-and-inspector-callbacks-3:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Declaration                                       | Trigger, payload and meaning                                                                         |
+===================================================+======================================================================================================+
| ``public event System.Action DeformationChanged`` | After pending deformation geometry is uploaded. No payload; inspect owned geometry at this boundary. |
+---------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public event System.Action Restored``           | After deformable shape is restored to rest geometry. No payload.                                     |
+---------------------------------------------------+------------------------------------------------------------------------------------------------------+

.. _evs-api-damage--parttype:

PartType
--------

**Runtime/Exterior/Parts/BodyPart.cs**

Defines the allowed part type choices used by this topic.

.. _evs-api-damage--values:

Values
~~~~~~

-  ``Door``
-  ``Hood``
-  ``Trunk``
-  ``Tailgate``
-  ``Other``

.. _evs-api-damage--partmaterial:

PartMaterial
------------

**Runtime/Exterior/Parts/DamagePart.cs**

Defines the allowed part material choices used by this topic.

.. _evs-api-damage--values-1:

Values
~~~~~~

-  ``Metal``
-  ``Glass``
-  ``Plastic``
-  ``Rubber``
-  ``Mechanical``
