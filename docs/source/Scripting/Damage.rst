.. _evs-scripting-damage--body-opening-damage-and-repair:

Body opening, damage and repair
===============================

``Body`` operation, damage accumulation and mesh deformation are separate layers. A body part can open around a hinge; a damage part can receive hits and detach; a deformation component can dent readable mesh geometry. Combining these layers produces a damaged vehicle without making every opening mechanism responsible for health or rendering.

Use the layer that matches the action. ``Open`` a door through ``Body``, report a gameplay impact through ``Damage``, and restore geometry through ``MeshDeformation``. A complete repair/respawn operation may need to coordinate all three as well as detached objects owned by the application.

.. _evs-scripting-damage--implementation-map:

Implementation map
------------------

+------------------------------+----------------------------------------------------------------------+
| Class                        | Responsibility                                                       |
+==============================+======================================================================+
| ``Body``                     | Finds and operates authored ``BodyPart`` entries.                    |
+------------------------------+----------------------------------------------------------------------+
| ``BodyPart``                 | Defines a named opening/moving body element.                         |
+------------------------------+----------------------------------------------------------------------+
| ``Damage``                   | Accepts impacts and routes them to damage/deformation boundaries.    |
+------------------------------+----------------------------------------------------------------------+
| ``DamagePart``               | ``Tracks`` a part's damage and detachment behavior.                  |
+------------------------------+----------------------------------------------------------------------+
| ``MeshDeformation``          | Owns readable mesh instances, dent buffers and geometry restoration. |
+------------------------------+----------------------------------------------------------------------+
| ``ICollisionDamageResponse`` | Lets a target alter collision damage severity.                       |
+------------------------------+----------------------------------------------------------------------+
| ``DamageCollisionRelay``     | Relays relevant native collisions into damage handling.              |
+------------------------------+----------------------------------------------------------------------+

.. _evs-scripting-damage--independent-ownership:

Independent ownership
---------------------

``Collision`` damage needs an impact measure rather than simply the vehicle's speed. ``Contact``-normal relative motion distinguishes a head-on impact from moving quickly along a wall. Scripted damage already supplies an amount, so it should not be accidentally scaled again by a response intended only for native collisions.

Keep presentation and gameplay state separate in consumers too. A dent is a mesh change, a hit is an accepted damage event and detachment is an ownership change. A hit effect may happen before the mesh upload, while a repair screen may need to inspect the final geometry.

``Body`` operates ``BodyPart`` entries by case-sensitive ID. ``Damage`` routes copied collision/scripted impacts to ``DamagePart`` boundaries and optional ``MeshDeformation``. An opening hinge is not itself a health/detachment policy.

``Collision`` severity uses contact-normal relative speed above threshold, not tangential travel speed. Scripted ``ApplyImpact`` supplies its own amount and does not pass through collision-only target response scaling. ``damageEnabled``, ``deformationEnabled`` and ``detachmentEnabled`` are independent policy gates for accepted hits.

.. _evs-scripting-damage--open-a-named-part:

Open a named part
-----------------

Treat a part ID as an authored contract between the vehicle prefab and application interaction. The adapter returns the action result so a missing, disabled or released door does not appear to open successfully. Keep door-specific UI text and interaction selection outside the body mechanism.

When creating reusable prefabs, choose consistent IDs for equivalent parts. This lets the same application adapter operate several vehicles through configuration rather than searching transform names or hard-coding mesh hierarchy paths.

Assign the ``Body`` and the ID configured on a ``BodyPart``. Missing/disabled/released targets return ``false``.

**Example: ``BodyPartControl.cs``**

.. raw:: html

   <!-- example: BodyPartControl.cs -->

.. code-block:: csharp

   using UnityEngine;
   using EasyVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class BodyPartControl : MonoBehaviour
       {
           public EasyVehicleSystem.Body body;
           public string partId = "Door";
           public bool Open() => body && body.Open(partId);
           public bool Close() => body && body.Close(partId);
       }
   }

.. _evs-scripting-damage--observe-accepted-damage:

Observe accepted damage
-----------------------

The sample captures the subscribed publisher separately from its editable reference and removes that exact subscription on disable. ``DamageHit`` supplies the accepted amount, so the observer does not attempt to recompute collision severity from vehicle speed.

Use ``Hit`` for gameplay notifications or accumulated statistics. Use the geometry-change notification when a consumer must inspect uploaded vertices. Keeping those consumers on the appropriate event avoids forcing an immediate mesh upload for every accepted collision.

``Damage.Hit`` provides ``DamageHit`` (part, point, direction and amount). It occurs when damage is accepted; a mesh upload can occur later in ``LateUpdate``. Use ``DeformationChanged`` when inspecting uploaded geometry. Subscribe with a named handler and release the same captured source.

**Example: ``DamageObserver.cs``**

.. raw:: html

   <!-- example: DamageObserver.cs -->

.. code-block:: csharp

   using UnityEngine;
   using EasyVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class DamageObserver : MonoBehaviour
       {
           public Damage damage;
           public float AcceptedDamage { get; private set; }
           private Damage subscribed;

           private void OnEnable()
           {
               subscribed = damage;
               if (subscribed) subscribed.Hit += OnHit;
           }

           private void OnDisable()
           {
               if (subscribed) subscribed.Hit -= OnHit;
               subscribed = null;
           }

           private void OnHit(DamageHit hit) => AcceptedDamage += hit.Amount;
       }
   }

.. _evs-scripting-damage--geometry-and-restoration:

Geometry and restoration
------------------------

``MeshDeformation`` owns runtime copies of readable ``MeshFilter`` meshes and changes vertices around accepted impacts. It retains rest geometry so a dent is bounded relative to the original shape and can be restored later. This avoids progressively treating an already-dented mesh as a new unbounded baseline. Reused vertex buffers are uploaded in ``LateUpdate``; native collision proxies do not continuously deform with every visual vertex, and skinned meshes are outside this path.

Use ``Deform`` when supplying a custom local mesh impact and ``RestoreShape`` when resetting the owned geometry. A ``Damage`` integration normally routes accepted hits to it. ``DeformationChanged`` follows geometry update; ``Restored`` reports restoration. Choose these events when a renderer/tool must inspect shape rather than reacting merely to a hit.

``DamagePart`` owns the part's counter and detachment threshold. ``ReceiveDamage`` evaluates that counter, ``Repair(amount)`` removes damage and returns the actual repaired amount, and ``Detach`` changes object ownership. A workshop action may coordinate repair and shape restoration, but reattaching lost parts still requires an application reconstruction policy.

A restoration policy should state what “repair” includes. Resetting a counter makes a damage part eligible for future hits but does not recreate a missing object. Restoring vertices removes dents but does not reattach debris. Teleporting a vehicle changes pose without rebuilding its authored hierarchy.

For pooling, retain or recreate the required part instances and restore their ownership before returning the vehicle to play. For a persistent world, the application may instead leave detached debris alive. Those are application lifetime choices; the local damage mechanic cannot infer them.

``DamagePart.Repair`` resets its damage counter. ``MeshDeformation.RestoreShape`` restores visual geometry. Neither reattaches detached parts. Pose reset restores the vehicle/occupants, not a complete damage state. Own a respawn/rebuild/pooling policy for lost objects.

Detached parts inherit motion and remain physical. ``Collision``-clearance policy delays recontact with the former owner. ``ICollisionDamageResponse`` changes collision damage severity only; it does not change scripted amount, target mass or all physical contacts.

.. _evs-scripting-damage--complete-public-method-and-event-index:

Complete public method and event index
--------------------------------------

The lists below cover public methods and events for this topic and their package base contracts. Signatures include overloads. See :doc:`the detailed body operation and damage API </API/Damage>` for arguments, return semantics, state and configuration. An override replaces the matching inherited implementation; it is not an additional call to make.

.. _evs-scripting-damage--body:

Body
~~~~

:ref:`Body <evs-api-damage--body>` gives the full declared contract.

+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| Method                                                      | Role                                                                                                                             |
+=============================================================+==================================================================================================================================+
| ``public virtual BodyPart GetPart(string id)``              | Finds the authored body part by its case-sensitive ID.                                                                           |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool Open(string id)``                     | Requests opening of this part or the body part selected by ID.                                                                   |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool Close(string id)``                    | Requests closure of this part or the body part selected by ID.                                                                   |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool Toggle(string id)``                   | Requests the opposite current body/switch/wiper/profile/gear state through the declaring component.                              |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SetPhysics(string id, bool enabled)`` | Looks up the case-sensitive part ID and requests that part's physics policy, returning ``false`` when no eligible target exists. |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SetOpen(string id, bool open)``       | Requests a body part's open/closed target.                                                                                       |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void OpenAll()``                           | Requests opening of every eligible authored body part.                                                                           |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void CloseAll()``                          | Requests closure of every eligible authored body part.                                                                           |
+-------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+

.. _evs-scripting-damage--bodypart:

BodyPart
~~~~~~~~

:ref:`BodyPart <evs-api-damage--bodypart>` gives the full declared contract.

+----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| Method                                             | Role                                                                                                                                  |
+====================================================+=======================================================================================================================================+
| ``public virtual void RefreshIgnoredCollisions()`` | Refreshes collision pairs for a body part after ownership/geometry changes.                                                           |
+----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Open()``                     | Requests opening of this part or the body part selected by ID.                                                                        |
+----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Close()``                    | Requests closure of this part or the body part selected by ID.                                                                        |
+----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Toggle()``                   | Requests the opposite current body/switch/wiper/profile/gear state through the declaring component.                                   |
+----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetOpen(bool value)``        | Requests a body part's open/closed target.                                                                                            |
+----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetPhysics(bool value)``     | Changes ``usePhysics`` for an unreleased part and emits ``PhysicsChanged`` only on an actual policy change; released parts ignore it. |
+----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Release()``                  | Releases this part or hand pose through its declaring type's ownership boundary.                                                      |
+----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+

+-----------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Event / callback                                    | Role                                                                                              |
+=====================================================+===================================================================================================+
| ``public event System.Action<bool> OpenChanged``    | When the part's requested open state changes. Payload: bool; this is not a generic arrival event. |
+-----------------------------------------------------+---------------------------------------------------------------------------------------------------+
| ``public event System.Action<bool> PhysicsChanged`` | When the part's ``usePhysics`` policy changes. Payload: bool.                                     |
+-----------------------------------------------------+---------------------------------------------------------------------------------------------------+
| ``public event System.Action Released``             | After the body part is released from vehicle-owned motion. No payload.                            |
+-----------------------------------------------------+---------------------------------------------------------------------------------------------------+

.. _evs-scripting-damage--damage:

Damage
~~~~~~

:ref:`Damage <evs-api-damage--damage>` gives the full declared contract.

+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| Method                                                                              | Role                                                                                  |
+=====================================================================================+=======================================================================================+
| ``public override void Configure(VehicleController vehicle)``                       | Binds collision/impact processing to the supplied vehicle.                            |
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| ``public virtual void ApplyImpact(Vector3 point, Vector3 direction, float amount)`` | Submits a scripted impact to the damage system, subject to its enabled damage policy. |
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| ``public virtual void ReceiveImpact(Impact impact)``                                | Processes a copied impact snapshot through vehicle damage policy.                     |
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+

+----------------------------------------+-------------------------------------------------------------------------------------------------------+
| Event / callback                       | Role                                                                                                  |
+========================================+=======================================================================================================+
| ``public event Action<DamageHit> Hit`` | When a damage hit is accepted. Payload: ``DamageHit``; mesh upload can occur later in ``LateUpdate``. |
+----------------------------------------+-------------------------------------------------------------------------------------------------------+

.. _evs-scripting-damage--damagepart:

DamagePart
~~~~~~~~~~

:ref:`DamagePart <evs-api-damage--damagepart>` gives the full declared contract.

+-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| Method                                                | Role                                                                                                                             |
+=======================================================+==================================================================================================================================+
| ``public virtual bool Detach(Rigidbody vehicleBody)`` | Ends the owned character or hitch relationship and releases the state/resources owned by that relationship.                      |
+-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float Repair(float amount)``         | Removes up to the requested nonnegative damage amount and returns the actual repaired amount. Does not reattach a detached part. |
+-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ReceiveDamage(float amount)``   | Applies an accepted damage amount to this damage part and evaluates its detachment threshold.                                    |
+-------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+

+-----------------------------------------------------+--------------------------------------------------------------------------------+
| Event / callback                                    | Role                                                                           |
+=====================================================+================================================================================+
| ``public event Action<DamagePart> Detached``        | After a damage part detaches. Payload: that ``DamagePart``.                    |
+-----------------------------------------------------+--------------------------------------------------------------------------------+
| ``public event Action<DamagePart, float> Damaged``  | After the part accepts damage. Payload: ``DamagePart`` and accepted amount.    |
+-----------------------------------------------------+--------------------------------------------------------------------------------+
| ``public event Action<DamagePart, float> Repaired`` | After damage is actually removed. Payload: ``DamagePart`` and repaired amount. |
+-----------------------------------------------------+--------------------------------------------------------------------------------+

.. _evs-scripting-damage--imodule:

IModule
~~~~~~~

:ref:`IModule <evs-api-modules--imodule>` gives the full declared contract.

+----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Method                                                                     | Role                                                                                                                        |
+============================================================================+=============================================================================================================================+
| ``void Configure(VehicleController vehicle)``                              | Repeatable setup contract supplied with the owning ``VehicleController``.                                                   |
+----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``void Step(VehicleController vehicle, Command command, float deltaTime)`` | Contract for one owner-supplied fixed tick; implement only the module responsibility and use the supplied Command/timestep. |
+----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+

.. _evs-scripting-damage--meshdeformation:

MeshDeformation
~~~~~~~~~~~~~~~

:ref:`MeshDeformation <evs-api-damage--meshdeformation>` gives the full declared contract.

+-----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| Method                                                                                              | Role                                                                                  |
+=====================================================================================================+=======================================================================================+
| ``public virtual void RestoreShape()``                                                              | Restores owned deformable meshes to their captured rest geometry.                     |
+-----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+
| ``public virtual void Deform(DamageHit hit, float radius, float dentPerDamage, float maximumDent)`` | Queues a bounded dent in readable mesh geometry around a supplied local impact point. |
+-----------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+

+---------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Event / callback                                  | Role                                                                                                 |
+===================================================+======================================================================================================+
| ``public event System.Action DeformationChanged`` | After pending deformation geometry is uploaded. No payload; inspect owned geometry at this boundary. |
+---------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public event System.Action Restored``           | After deformable shape is restored to rest geometry. No payload.                                     |
+---------------------------------------------------+------------------------------------------------------------------------------------------------------+

.. _evs-scripting-damage--module:

Module
~~~~~~

:ref:`Module <evs-api-modules--module>` gives the full declared contract.

+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Method                                                                                    | Role                                                                                                                                   |
+===========================================================================================+========================================================================================================================================+
| ``public virtual void Configure(VehicleController vehicle)``                              | Empty base setup hook. Derived components may cache references/apply persistent settings; the controller owns lifecycle notifications. |
+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Step(VehicleController vehicle, Command command, float deltaTime)`` | Empty base extension point. The controller schedules derived work and emits lifecycle notifications around it.                         |
+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetEnabled(bool value)``                                            | Changes module enabled state and publishes an actual requested-flag change.                                                            |
+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SupportsProfile(DriveProfile profile)``                             | Checks movement-family compatibility; this is independent of the Unity enabled flag.                                                   |
+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+

+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| Event / callback                                                          | Role                                                                                                              |
+===========================================================================+===================================================================================================================+
| ``public event System.Action<bool> EnabledChanged``                       | After ``SetEnabled`` changes the module flag. Payload: requested enabled bool; no event for an unchanged request. |
+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public event System.Action<VehicleController> Configured``              | After controller-driven module configuration. Payload: the owning ``VehicleController``.                          |
+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public event System.Action<VehicleController, Command, float> Stepped`` | After this registered module has stepped. Payload: vehicle, sampled Command, timestep in seconds.                 |
+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
