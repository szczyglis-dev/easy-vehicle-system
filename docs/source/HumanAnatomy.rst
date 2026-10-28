.. _evs-humananatomy--prepare-a-humanoid-ragdoll:

Prepare a humanoid ragdoll
==========================

Prepare the character in this order: **rig and Avatar → ragdoll bodies/colliders → reference auto-fill → anatomical joint conversion → seat and contact setup**. Work outside Play Mode and save the completed character as a reusable prefab.

The package's anatomical parts are the physical bones and their saved ``ConfigurableJoint`` connections, listed under **Humanoid Passenger → Anatomical Joints**. Hand/foot anchors on a vehicle are separate: they tell the seated character where to reach, rather than defining its skeleton.

.. _evs-humananatomy--1-prepare-the-rig:

1. Prepare the rig
------------------

1. Import a skinned character with a bone hierarchy. Select the model asset in the Project window and open its **Rig** import settings.
2. Set **Animation Type** to **Humanoid**, create or assign a valid Avatar, and apply the import settings. Use **Configure** to review hips, spine, head, arms and legs; correct left/right mapping and the reference pose before continuing.
3. Keep the bones needed for ragdoll bodies and IK accessible in the hierarchy. If import optimization hides them, expose the required transforms or disable **Optimize Game Objects** for this setup.
4. Drag the character into a scene and create your own character prefab or prefab variant. Make changes on this instance or in Prefab Mode, rather than attempting to modify the imported model file itself.
5. Check the character's real size and forward direction. Keep its working root at unit scale and avoid nonuniform scaling of physical bones. Finish proportion changes before authoring the joints.

A valid Humanoid Avatar supplies the reference mapping automatically. A custom/manual rig can also be configured, but its pelvis, limb bones and body connections must be assigned explicitly, and it must be placed in a neutral pose before anatomical configuration.

.. _evs-humananatomy--2-create-the-physical-ragdoll:

2. Create the physical ragdoll
------------------------------

1. Expand the character instance's skeleton in the Hierarchy.
2. Open **GameObject → 3D Object → Ragdoll...**. This is Unity's built-in `Ragdoll Wizard <https://docs.unity.com/en-us/engine/6000.0/manual/physics-section/physics-overview/ragdoll/wizard-ragdoll-wizard>`__.
3. Assign the instance's bone transforms to the wizard's body-part fields. If your Unity version provides an Animator field and **Auto-Fill**, assign this character's Animator first and review the generated mapping; otherwise drag the bones from the Hierarchy.
4. Check pelvis/root, torso/head and both arm/leg chains, set the intended body mass, then choose **Create**.
5. Inspect the generated ``Rigidbody``, collider and ``CharacterJoint`` components on the bones. Fit the colliders to the limbs and torso, check the mass distribution, and confirm that joints connect to the intended parent bodies.
6. Keep this skeleton separate from the vehicle hierarchy while preparing it. The ragdoll body list should contain the character's physical bones, not the car's Rigidbody or unrelated props.

If your character already has a suitable physical ragdoll, keep its existing bodies/colliders and continue below. The package's Auto-fill does not create them.

.. _evs-humananatomy--3-add-passenger-components-and-auto-fill-references:

3. Add passenger components and auto-fill references
----------------------------------------------------

1. Select the character's working root, above its complete skeleton. Add **Humanoid Passenger** and **Humanoid IK** through Add Component; both are under **EasyVehicleSystem → Passengers → IK**.
2. In Humanoid Passenger, assign the character's **Animator** and **IK** if they are not found automatically.
3. Press **Auto-fill** on Humanoid Passenger. It fills missing Animator, IK and pelvis references and collects existing ragdoll Rigidbodies. It uses the Humanoid Avatar where available, then bone names and existing components.
4. Press **Auto-fill** on Humanoid IK and review both upper/lower arms, hands, upper/lower legs and feet. Assign unresolved references manually.
5. Review **Pelvis**, **Ragdoll Bodies** and the IK limb mapping. Existing assignments are preserved by Auto-fill, so correct or clear an incorrect reference yourself before filling it again.

There are two different auto-fill operations: the Unity wizard helps prepare the initial physical ragdoll; the package buttons connect that existing rig to its passenger and IK components. Neither package button converts joint types.

.. _evs-humananatomy--4-convert-to-anatomical-configurablejoints:

4. Convert to anatomical ConfigurableJoints
-------------------------------------------

1. Keep the source character outside Play Mode. For a manual rig, put the skeleton into its neutral reference pose.
2. On **Humanoid Passenger**, press **Configure anatomical joints**.
3. Read the overwrite confirmation and choose **Overwrite settings** when you are ready to replace the rig's joint tuning.
4. The operation creates or updates the anatomical ``ConfigurableJoint`` connections, converts the corresponding ``CharacterJoint`` components, and saves their references and IK reference data in **Anatomical Joints**. Existing Rigidbodies and colliders are preserved.
5. Expand Anatomical Joints and follow each joint reference to its bone. Inspect **Connected Body**, anchors, axes and angular limits on the actual ConfigurableJoint component. The root pelvis may have no parent-body joint; not every Rigidbody needs a list entry.
6. Refine the saved joints for your character's proportions. Elbows and knees should bend in the expected direction; shoulders, hips, wrists and torso should have appropriate travel without pulling connected bones apart.
7. Save the prefab, or apply the intended instance overrides to your own prefab.

**Configure anatomical joints overwrites existing axes, limits and anatomical tuning.** Use it for initial authoring or an intentional rebuild after changing the skeleton. Once tuned, edit the saved ConfigurableJoint components directly instead of regenerating them every time a seat or grip changes. A physical humanoid needs valid saved anatomical joint references before Play Mode; seating does not generate this anatomy for you.

.. _evs-humananatomy--5-connect-the-character-to-a-seat:

5. Connect the character to a seat
----------------------------------

1. Add/configure the vehicle's **Passengers** and **Passenger Seat** components as described in :doc:`Passengers </Passengers>`.
2. Assign the prepared character body or prefab to the seat. For physical seated behavior, choose **Ragdoll Physics** and keep the character's **Physical While Seated** enabled as required by your setup.
3. Place the seat's pelvis/spine anchor and assign hand/foot handles or anchors within natural reach. Keep the character's bone proportions unchanged when fitting the vehicle.
4. Use **Preview seated pose** to review the fit, then enter Play Mode and check seated movement, restraint behavior and release/ejection with the intended character mass.

Tune seat support and limb targets separately from the anatomical joint limits. Stronger seat springs do not fix an incorrectly connected joint or an unreachable handle. Recheck body mass distribution, joint limits, palm thickness and finger pads when replacing the character.

See :doc:`Seats and handles </SeatsAndHandles>`, :doc:`Hand grips </SteeringHandGrip>` and :doc:`Anatomy scripting </Scripting/Anatomy>` for contact fitting and custom integrations.
