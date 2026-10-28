.. _evs-scripting-anatomy--authored-joint-and-ik-frames:

Authored joint and IK frames
============================

Anatomy defines the coordinate frames and motion limits that make a humanoid rig usable by passenger physics and IK. The runtime needs to know not just where a bone is, but which axis bends it, how it connects to its parent and what motion is physically or anatomically permitted.

The workflow has two stages: author and save native joints for the character, then use that character from seats and handles. A vehicle seat changes posture and support; it does not replace the character's anatomical setup.

.. _evs-scripting-anatomy--implementation-map:

Implementation map
------------------

+-------------------------------+----------------------------------------------------------------------------------------+
| Class                         | Responsibility                                                                         |
+===============================+========================================================================================+
| ``HumanoidJointLimits``       | Contains ``HumanoidJointDefinition`` metadata and internal native frame/limit helpers. |
+-------------------------------+----------------------------------------------------------------------------------------+
| ``HumanoidAnatomyAuthoring``  | Editor utility that configures the mapped rig's native joints.                         |
+-------------------------------+----------------------------------------------------------------------------------------+
| ``HumanoidAnatomyPresets``    | Supplies authoring presets used while preparing a rig.                                 |
+-------------------------------+----------------------------------------------------------------------------------------+
| ``HumanoidIK``                | Uses character frames to resolve limb targets.                                         |
+-------------------------------+----------------------------------------------------------------------------------------+
| ``HumanoidFingerCalibration`` | Prepares finger-frame and geometry information for grip fitting.                       |
+-------------------------------+----------------------------------------------------------------------------------------+

.. _evs-scripting-anatomy--authoring-versus-runtime:

Authoring versus runtime
------------------------

For each physical link, verify the intended parent body and joint frame in the character's neutral pose. A correct transform hierarchy alone does not guarantee that the native joint's axis corresponds to anatomical flexion. Errors here appear later as a knee bending sideways or a wrist resisting a reachable handle.

Keep the saved character prefab as the source of anatomical tuning. This makes the same body usable in several vehicles without copying a different skeleton configuration into each seat. Seat-specific support belongs on the vehicle; body proportions, bone colliders and skeletal connections belong on the character.

``HumanoidAnatomyAuthoring`` / ``HumanoidAnatomyPresets`` are editor authoring utilities. They prepare ``ConfigurableJoint`` components and ``HumanoidJointDefinition`` references from the mapped rig. Avatar reference rotations support Humanoid characters; manually mapped rigs need an appropriate neutral pose.

Runtime reads the saved native joint axes, anchors, connections and angular limits. Definition reference rotations/flexion support IK frame conversion. Seats and handles own vehicle support, not a separate per-seat anatomical skeleton.

.. _evs-scripting-anatomy--tuning-authority:

Tuning authority
----------------

``HumanoidJointDefinition`` stores a reference to the actual ``ConfigurableJoint`` plus the reference rotations/flexion needed by runtime conversion. It is not a second independent set of native angular limits competing with that joint. The runtime reads the saved joint's frame and bounds before using them for physical/IK work.

The editor authoring utilities build a useful starting skeleton from the mapped rig and selected preset. After that, inspect and tune the real joint components on the character prefab. Re-running authoring is an explicit replacement of those authored values, so use it as a rig-preparation operation rather than a runtime seat adjustment.

For a new humanoid variant, validate pelvis orientation, limb lengths, joint axes and collision geometry before preparing grips. Then check the character in more than one seat. A rig that works only because one seat places its targets on an unusual compensating offset is difficult to reuse.

Use a simple validation progression: inspect the neutral pose, move one joint through its intended range, then check a seated pose and finally a moving physical vehicle. Diagnose the frame before widening limits. A very wide limit can hide a rotated axis during setup but produces implausible motion when the body is released.

When creating a rig variant, preserve the relation between reference rotations, collider dimensions and bone proportions. Finger pad dimensions and flexion axes need the same attention as the large limbs because grip fitting measures that geometry rather than guessing a pose from bone names.

Tune actual ``ConfigurableJoint`` components after authoring. Running **``Configure`` anatomical joints** again replaces values with the selected authoring preset. Do not leave a second competing ``CharacterJoint`` on the same physical link.

Locked angular axes and limited axes have distinct semantics. A numerical angle range is not an independent Cartesian Euler box; it is interpreted in the joint's configured native frame. Finger fitting additionally uses calibrated phalanx axes and pad geometry.

.. _evs-scripting-anatomy--inspect-saved-native-joint-connections:

Inspect saved native joint connections
--------------------------------------

A useful first diagnostic for a character prefab is to find joints that are not connected to another body. A world-connected joint may be intentional, but it deserves inspection before using the rig as a freely moving passenger. The component below only reports configuration; it does not author or overwrite the skeleton.

**Example: ``PassengerJointInfo.cs``**

.. raw:: html

   <!-- example: PassengerJointInfo.cs -->

.. code-block:: csharp

   using UnityEngine;

   namespace VehicleDocumentationExamples
   {
       public class PassengerJointInfo : MonoBehaviour
       {
           public Transform characterRoot;

           public void InspectConnections()
           {
               if (!characterRoot) return;
               foreach (var joint in characterRoot.GetComponentsInChildren<ConfigurableJoint>(true))
               {
                   if (!joint.connectedBody)
                       Debug.LogWarning($"Inspect world-connected joint: {joint.name}", joint);
               }
           }
       }
   }

Run this on the authored character hierarchy before seating creates temporary vehicle supports. A connected body is only one check: still inspect axes, anchors and limits visually. Automatically assigning the parent rigidbody would hide unusual but deliberate rig layouts and is therefore not part of this diagnostic.

.. _evs-scripting-anatomy--dynamic-and-animation-paths:

Dynamic and animation paths
---------------------------

The physical and animation paths can use the same contact targets while applying them differently. In physical seating, targets guide forces and constraints. In ``AnimatorIK``, animation remains the base pose and selected limbs receive IK overlays. A target that looks plausible in one path still needs validation in the other, especially near reach limits.

For a custom character, decide which path owns the pose before integrating it. Do not allow animation and native dynamic bodies to independently assign the same bone transforms. Use the controller handover boundary when switching between those owners.

A different rig requires validating proportions, collision proxies, mass distribution and reachable contacts. Large support forces do not correct bad frames. See :doc:`passenger physics </Scripting/PassengerPhysics>`, :doc:`controller ownership </Scripting/PassengerControllers>` and :doc:`grip fitting </Scripting/GripSolving>`.

.. _evs-scripting-anatomy--complete-public-method-and-event-index:

Complete public method and event index
--------------------------------------

The lists below cover public methods and events for this topic and their package base contracts. Signatures include overloads. See :doc:`the detailed anatomical references API </API/Anatomy>` for arguments, return semantics, state and configuration. An override replaces the matching inherited implementation; it is not an additional call to make.

.. _evs-scripting-anatomy--editor-authoring:

Editor authoring
~~~~~~~~~~~~~~~~

``HumanoidJointDefinition`` is a data contract with no public methods or events. Its complete fields are listed in :doc:`Anatomical references API </API/Anatomy>`.

+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Method                                                              | Role                                                                                                                                                                               |
+=====================================================================+====================================================================================================================================================================================+
| ``HumanoidAnatomyAuthoring.Configure(HumanoidPassenger passenger)`` | Editor-only authoring operation that configures the mapped character's anatomical native joints. Run it while preparing the character prefab; it can replace tuned joint settings. |
+---------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

``HumanoidAnatomyPresets`` and ``HumanoidJointLimits`` are implementation helpers rather than public extension APIs. For runtime character integration, use the public passenger body/controller and hand-pose contracts instead of calling those helpers.
