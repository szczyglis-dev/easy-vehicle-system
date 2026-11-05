.. _evs-seats--seats:

Seats
=====

A seat defines the occupant's position, attachment and body support. This page covers seated fitting, restraints, rider support and collision response. Create the seat/body association in :doc:`Passengers </Passengers>` first. Configure hand and foot targets in :doc:`Handles </Handles>`, and prepare the character's joints in :doc:`Human anatomy </HumanAnatomy>`.

.. _evs-seats--inspector-quick-start:

Inspector quick start
---------------------

1. Select the root and open **Vehicle Controller > Seats**. Enable passengers if missing and use **Add passenger seat**, or select an existing seat child in the Hierarchy.
2. Assign its prepared **Body** or **Body Prefab** and choose the passenger controller/attachment policy described in :doc:`Passengers </Passengers>`. Begin with one occupant; an arbitrary character mesh is not automatically a configured ragdoll.
3. Create/position the **Spine Anchor** at the seated pelvis origin and drag it into the field. Use the seat's pose/preview tools to fit the character before raising physical restraint strengths.
4. Configure limb modes and assign hand/foot anchors or handles using :doc:`Handles </Handles>`. Set the collision/tilt response and g-force policy on the seat independently of its initial pose.
5. Save scene/prefab references and test boarding or initial occupancy, normal driving, one hard landing and exit. Tune support only after verifying that each reference belongs to the intended seat/vehicle.

.. _evs-seats--fit-the-seated-body:

Fit the seated body
-------------------

1. Use a pre-placed prepared body for initial fitting so the seat preview can show the actual character proportions.
2. Put **Spine Anchor** at the intended seated pelvis origin, facing along the occupant's seated forward direction. It is not a camera position or a marker at the top of the spine.
3. Adjust pelvis/backrest fit with the seat's **Seated Pose** tools. Check that hips sit above the cushion and the torso has space to move.
4. Place the hands and feet near their natural destinations before applying strong restraints. Bent elbows/knees need room through the full control range.
5. Use **Preview seated pose** and inspect from the front, side and top. Check both sides rather than mirroring a target visually without checking orientation.
6. Test stationary in Play Mode, then accelerate, brake and steer. For occupied support changes, use **Apply seated tuning** to rebuild affected restraints. Save persistent tuning outside Play Mode.

A target beyond limb length cannot be corrected with more spring force. Adjust the seat, contact or model proportions first. Anatomical joint limits remain on the character's saved joints; the seat does not regenerate them.

.. _evs-seats--main-attachment-and-rigid-transform-supports:

Main attachment and rigid transform supports
--------------------------------------------

**Attachment Mode** selects the main seating origin's ``Spring`` (default) or ``Parent`` independently from the passenger controller. A physical humanoid using Parent keeps its ragdoll active: only the pelvis is attached to Spine Anchor; torso springs are omitted and limb settings remain independent. **Parent Make Kinematic** (default true) parks only the held pelvis Rigidbody, not the remaining ragdoll. Turn it off to retain that Rigidbody's dynamic simulation too. Characters without a physical rig use controlled root attachment; Animator and Animator + IK still select animation ownership.

**Parent Position Offset** and **Parent Rotation Offset** use Spine Anchor local coordinates/degrees. For non-physical Spring attachment, **Attachment Spring** and **Attachment Damper** drive a world-space simulated root pose; physical main springs retain the existing restraint tuning. Changing modes through ``SetAttachmentMode`` keeps occupancy. **Custom** still leaves the automatic main attachment to application code, but explicitly configured additional supports apply with any controller, including Custom.

Each **Custom Transform Supports** entry independently selects **Mode: Spring / Parent**, plus **Body Transform**, **Anchor**, **Active**, **Preserve World Pose**, **Position Offset** and **Rotation Offset**. Mix modes freely with either main attachment mode, with animation, without a ragdoll or with an active ragdoll. Parent is the default for a new transform entry.

-  **Parent** actually reparents the transform and enforces its anchor-local pose after ordinary animation/IK. **Make Kinematic** optionally makes only that transform's Rigidbody kinematic while held (default true); its previous setting is restored on release. Disable it to retain dynamic simulation while enforcing the pose. Other bones keep their own physics state.
-  **Spring** preserves the original hierarchy. A dynamic Rigidbody receives position forces and rotation torques during passenger physics updates. A kinematic Rigidbody or plain Transform follows a simulated spring pose after animation, so Rigidbody and ragdoll are optional. **Spring / Damper** and **Rotation Spring / Rotation Damper** tune the response; the transform simulation uses unit virtual mass. Spring pose integration caps catch-up at 0.25 seconds per rendered frame.

**Follow Anchor Rotation** is enabled by default. Disable it to capture the target world rotation at attachment/refresh instead of following subsequent anchor rotation. Parent holds that world orientation; both Rigidbody and transform Spring modes spring toward the same fixed world orientation. Preserve World Pose and Rotation Offset still determine the initial target. Position always follows the anchor, including rotation of its local position offset. Refresh recaptures the reference rotation.

**ID / Label** is one optional field: it names the Inspector entry and identifies it through the seat API. IDs are unique within a seat and use exact, case-sensitive matching. Empty IDs keep transform-based access available. ``GetTransformSupport("left-hand")``, ``TryGetTransformSupport``, ``SetTransformSupportActive``, ``UpdateTransformSupport`` and ``RemoveTransformSupport`` have string-ID overloads. Add rejects duplicate nonblank IDs; duplicate IDs introduced through direct edits are ambiguous and ID lookup/mutation returns null/false. IDs do not affect prefab transform resolution or which supports physically run.

Assign Body Transform from Body or Body Prefab; prefab children resolve by child indices on the spawned occupant. Foreign transforms, missing references and anchors inside the passenger hierarchy are skipped. Duplicate body transforms use the first valid active entry. An explicit pelvis/root entry overrides the corresponding automatic main binding. Preserve World Pose captures the current anchor-relative pose before adding offsets; otherwise the target is the anchor plus offsets.

Bindings deliberately override animation/IK for the selected transforms. Choose compatible skeletal constraints and competing scripts yourself; attachment settings do not silently change the controller or remove anatomical joints. Physics requires a dynamic Rigidbody to respond to forces; use transform springs for rigs without physical bodies.

Original parent, sibling order, local pose/scale and any changed kinematic setting are restored on release, handover, reset or disable. Runtime list/settings edits require ``RefreshTransformSupports()``; add/remove/update/active API methods refresh automatically. Main spring tuning is captured on refresh. Custom seats also show the support lists, although their automatic main attachment remains application-owned.

.. _evs-seats--pelvis-and-chest-support:

Pelvis and chest support
~~~~~~~~~~~~~~~~~~~~~~~~

Seat restraints support the body around the captured seated pose. **Seat Travel** and **Chest Travel** bound translation when the harness travel limit is enabled. **Chest Support Strength** scales chest support independently from the pelvis. The compliant harness's frequency/damping, maximum acceleration and angular torque settings determine how strongly it follows the vehicle.

Use lean/twist limits to allow controlled body movement around the seated frame. These limit the seated support envelope, not individual hip/shoulder anatomy. Relative linear/angular damping suppresses motion relative to the vehicle; it is separate from ordinary world-space Rigidbody damping.

Start with the supplied settings and change one group at a time. Too much stiffness with insufficient damping can oscillate; too much damping makes the body look rigid. If only the chest sags, inspect chest support rather than increasing every hand/foot spring. Reapply seated tuning after changing settings that rebuild restraints.

.. _evs-seats--g-force-limits:

G-force limits
--------------

Expand **G-force limits** on a Passenger Seat to protect an occupied **Ragdoll Physics** passenger against sudden vehicle acceleration or a hard stop against a wall. The limiter is enabled by default, including on existing seats that have no saved override. Animator, Animator + IK, Attach Only, Custom, empty seats, free/ejected ragdolls and kinematic vehicles are excluded.

Detection samples the vehicle's velocity at the seat, including angular motion, using :doc:`PhysicsSensors </API/PhysicsSensors>` and an independent motion history for that seat. Shared chassis/ground readings are available through ``vehicle.sensors``; the passenger retains point-specific acceleration history. It uses the gravity-compensated velocity change per physics step: acceleration is expressed in standard G (9.81 m/s²). Free fall alone does not trigger protection; a stationary supported seat reads about 1 G. Both the G threshold and the minimum velocity change must be exceeded. Overload activation additionally requires at least one dynamic bone to exceed the configured relative speed or angular speed. **Protect Constraint Failure** provides a separate safety path for sustained contacts: it admits the same containment if any dynamic bone exceeds twice its configured relative linear/angular speed, or the pelvis exceeds 125% of Maximum Seat Displacement. These failures can occur after light-object impacts without a high chassis G spike. The safety path is checked after physics and before rendering, uses live physics positions/point velocities, and is disabled by either its own option or the main Enabled switch. It does not force a rest pose or release/eject the occupant. A brief suspension landing with the skeleton still following the cabin does not activate protection merely because its measured G is high. The optional force threshold is an **estimated passenger inertial load**, computed from acceleration and physical passenger mass; it is not the vehicle collision contact force.

+--------------------------------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Setting                        | Default | Meaning                                                                                                                                                                                                      |
+================================+=========+==============================================================================================================================================================================================================+
| Enabled                        | On      | Allow emergency protection for this seat.                                                                                                                                                                    |
+--------------------------------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Protect Constraint Failure     | On      | Independently admit containment if relative bone speed/angular speed exceeds twice its limit or pelvis displacement exceeds 125% of its envelope. Does not require the G, delta-v or force thresholds.       |
+--------------------------------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Monitor After Physics          | On      | Detect resolved wheel/suspension impulses in the same physics step, even without a chassis collision callback. Off restores pre-solve/collision-only detection; active containment still runs after physics. |
+--------------------------------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Minimum G Force                | 8 G     | Minimum measured acceleration.                                                                                                                                                                               |
+--------------------------------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Minimum Velocity Change        | 1 m/s   | Minimum gravity-compensated velocity change in one physics step; rejects small high-frequency impulses.                                                                                                      |
+--------------------------------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Minimum Force                  | 0 N     | Optional additional passenger inertial-force threshold; zero disables this extra test.                                                                                                                       |
+--------------------------------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Protection Time                | 0.15 s  | Minimum hold after excessive acceleration, at least one physics step; extended until relative bone motion settles.                                                                                           |
+--------------------------------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Maximum Relative Speed         | 3 m/s   | Maximum dynamic bone speed relative to the vehicle's velocity at that bone while protection is active.                                                                                                       |
+--------------------------------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Maximum Seat Displacement      | 0.15 m  | Pelvis travel around its seated spine origin during protection. An excessive displacement translates the dynamic body together.                                                                              |
+--------------------------------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Maximum Relative Angular Speed | 360°/s  | Maximum bone spin and rotation per physics step relative to the moving vehicle, using live pre-solve rotations.                                                                                              |
+--------------------------------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Maximum Joint Separation       | 0.025 m | Allowed separation between anatomical joint anchors during protection.                                                                                                                                       |
+--------------------------------+---------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

While below the overload thresholds and the optional constraint-failure safety thresholds, detection does not write body poses, velocities, joint settings or spring values. The ordinary sampling path allocates no managed memory and does not scan skeletal joints. A small rotation-history buffer is allocated once per occupant and refreshed before physics, without changing any bodies. Emergency pose buffers and the ordered joint cache are created only when protection first activates.

On activation, the limiter bounds bone velocities and angular velocities relative to the vehicle. It temporarily increases native solver iterations and makes the existing anatomical and vehicle-to-body angular stops hard by removing their soft limit springs. PhysX uses the joints' actual captured frames, limits and connections. Angular speed is bounded both in velocity and in actual rotation per physics step, using the last live pre-solve bone rotations relative to the moving cabin. This catches an excessive rotation introduced within a single solve; it does not compute substitute Euler limits or return the mannequin to an authored pose. Positional projection and last-resort excessive anchor/pelvis displacement repair keep the skeleton connected. Protection Time is a minimum hold: if relative bone motion is still above one quarter of the configured speed limits when the hold expires, protection is extended until the skeleton slows down. Ordinary spring values, solver settings and projection settings are restored afterwards. With Monitor After Physics enabled, one coroutine per eligible occupied physical seat samples the resolved seat velocity after every native physics solve. This includes WheelCollider and predictive suspension impulses that do not emit a chassis collision callback; overload protection no longer waits for the next pre-solve update. It also runs directly after a new collision and before rendering. Disabling this option restores pre-solve/collision-only detection, while already active protection continues to be enforced after physics. Original joint projection settings are restored when the interval ends, the feature is disabled, the seat changes controller or the occupant exits/ejects. During protection, chassis and affected ragdoll interpolation is temporarily disabled and corrected physics poses are published before rendering, preventing an old stretched pose from lingering in the image. With multiple seats, every observed physical occupant joins the protected chassis display frame, even if its own protection is inactive. This prevents one-frame road-speed displacement between an unprotected seat and a chassis whose interpolation was temporarily disabled. Original interpolation is restored for all joined occupants when the last active interval ends. Exiting restores that occupant immediately. Explicit ejection and configured damage ejection take precedence over containment.

**Measured G-force** and **G-force protection active** are read-only Play Mode indicators shown when the group is expanded. Lower the activation thresholds to cover weaker impacts, or raise them if protection engages on intended rough-terrain motion. These settings are live; they do not rebuild the seat's ordinary restraints. Teleport/reset and entry clear the velocity history so a deliberate reset is not treated as a collision.

Implementation is isolated in the static ``PassengerGForceLimiter`` helper, with separate runtime state owned by each seat. Serialized tuning lives in ``PassengerGForceLimits``; seats do not share detection history.

.. _evs-seats--collision-and-tilt-response:

Collision and tilt response
---------------------------

Configure these policies under the seat's **Damage TireFeedback**/restraints. They operate on compatible occupied physical ragdolls, not as a generic animation event for every controller mode.

.. _evs-seats--limb-release-and-whole-passenger-ejection:

Limb release and whole-passenger ejection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Limb release frees hands and/or feet while the occupant remains seated. Whole-passenger ejection removes seat, chest, hand and foot restraints and ends occupancy. **Enable Passenger Ejection** and its collision/tilt options are independent of limb-only release options.

Collision thresholds require both the configured average force and relative speed. Force is contact impulse divided by the fixed timestep, in newtons; it is not the vehicle's mass or a permanent sustained force sensor. Speed is relative contact speed in m/s. Test the actual vehicle/character masses rather than reusing a threshold solely because a model looks similar.

The options named On Spin detect roll/pitch tilt against gravity up. The configured angle and continuous delay filter a brief bump; an ordinary yaw turn while upright is not the same condition. Release and ejection have separate angles/delays. Additional ejection velocity is vehicle-local before being applied; ordinary physical motion is preserved.

.. _evs-seats--contact-exclusions:

Contact exclusions
~~~~~~~~~~~~~~~~~~

**Exclude Vehicle Collisions On Enter** and **Exclude Self Collisions On Enter** suppress contacts while the character is supported. Seat-wide release flags can restore those contacts for Free limbs/ejection; each limb can enable its own release contacts too. Neighboring skeletal bodies retain their adjacent-body exclusion, and native joint collision rules still apply.

For a physically intersecting seated model, first correct geometry. Enabling every self/vehicle collision while strong restraints pull bones through the seat can create jitter. Conversely, a released limb may pass through the vehicle if its release-contact policy remains off. Choose the intended release behavior explicitly.

.. _evs-seats--restore-after-damage:

Restore after damage
~~~~~~~~~~~~~~~~~~~~

Damage release is latched until restored/reset; returning upright does not necessarily reattach the hands automatically. ``RestoreDamageFeedback`` clears release state and restores the built-in seated pose/support, or raises the Custom occupant's reset request. **Reseat Ejected On Reset** can return the same damage-ejected body if still available; it must not steal a character that has entered another seat.

Use ``IsReleasedByDamage``, ``HandsReleasedByDamage``, ``FeetReleasedByDamage`` and ``PassengerReleasedByDamage`` for diagnosis. An empty seat and a seated occupant with released hands require different recovery/UI behavior.

.. _evs-seats--motorcycle-rider-support:

Motorcycle rider support
------------------------

Fit the pelvis, foot pegs and handlebar contacts before tuning extra rider support. Keep the knees outside the motorcycle using reachable foot/hip geometry; do not use seat springs to conceal incorrect anatomical hip limits.

On ``PassengerSeat``, **Hold Head Forward** adds artificial angular spring support to the seated ragdoll head. A runtime PhysX angular drive evaluates its spring and damping together with the native constraints; it does not apply an explicit PD torque on each physics step. All three linear axes of this support remain free, so only the anatomical neck locates the head. **Head Pitch** is relative to the seat's neutral forward pose: zero faces forward, negative looks up and positive looks down. **Head Spring**, **Head Damper** and **Maximum Head Torque** control stiffness, damping relative to the chassis and the torque cap. They can be adjusted in Play Mode.

This requires a Humanoid Avatar, a saved anatomical joint on the mapped head and a dynamic head Rigidbody. It runs only for an occupied enabled Ragdoll Physics seat. Animator, Animator + IK, Attach Only, Custom, empty seats and ejected bodies receive no head torque. Disabling support immediately clears its runtime drive and removes the temporary angular support; saved anatomy remains intact. The demo uses zero-degree pitch. The same settings work for a quad, car, boat or aircraft without a BalanceRider component. Support is off by default on new seats; older enabled rider support is transferred to its assigned seat.

.. _evs-seats--balance-rider-motorcycles-bicycles-and-scooters:

Balance rider: motorcycles, bicycles and scooters
-------------------------------------------------

**Balance Rider** is an optional passenger behaviour, independent of the drive profile. Add it through **Tools > EasyVehicleSystem > Add Component > Passengers > Seats > Balance Rider** or Unity’s Add Component menu, then assign its **Seat**. New components work with any profile; **Motorcycle Profile Only** is an optional restriction. The demo motorcycle keeps that restriction and its existing foot motion.

A **Passenger Seat** represents an occupancy and body-support frame; it can support a standing character as well as a seated one. For a scooter, place its pelvis/backrest anchor at the rider’s standing hip height above the deck, with suitable orientation, and place the foot targets on the deck. Fit hands to the handlebar and preview the pose. Adjust foot pinning and the seat’s compliant harness to the intended stance. For a bicycle or motorcycle, put the same anchor over the saddle. Do not enable speed-dependent foot placement merely because a vehicle has handlebars: choose each foot’s policy explicitly.

.. _evs-seats--independent-foot-policies:

Independent foot policies
~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Setting     | Behavior and required poses                                                                                                                                                               |
+=============+===========================================================================================================================================================================================+
| Speed Blend | Interpolates from Ground to Riding using Riding Blend. Requires both transforms.                                                                                                          |
+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Riding      | Follows the Riding transform continuously. Use it for the scooter’s planted foot, both feet on a deck, or foot targets parented beneath animated bicycle pedals. Only Riding is required. |
+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Ground      | Follows the Ground transform continuously; only Ground is required.                                                                                                                       |
+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Unchanged   | Leaves this foot’s ordinary Seat binding intact.                                                                                                                                          |
+-------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Left and right policies are independent. A foot with an assigned Handle keeps that Handle’s priority; Balance Rider does not replace it. Missing required poses leave the Seat’s existing anchor intact. Disabling the behaviour, changing its seat or making it inapplicable releases its generated anchors and restores the original direct bindings. It does not remove targets assigned by another system after it released ownership.

**Blend Source = Speed** uses speed magnitude, including reverse motion, between **Lift Starts At** and **Fully Raised At**. **Blend Speed** limits how quickly progress changes, in normalized units per second. **Manual** uses **Manual Riding Blend** instead: zero requests Ground, one requests Riding. This lets custom controls or an animation request a push-off/return pose without changing the vehicle input interface. Only feet in Speed Blend use this progress; Riding and Ground follow their transforms directly. Ground poses are authored transforms, not terrain raycasts.

+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Vehicle / stance               | Starting configuration                                                                                                                                                                                                                                     |
+================================+============================================================================================================================================================================================================================================================+
| Motorcycle                     | Both feet Speed Blend between low-speed ground poses and pegs. Keep the demo’s 1–8 km/h blend as a starting point and fit the poses to the model.                                                                                                          |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Bicycle                        | For simple feet-down/feet-up transitions, use Speed Blend. For pedalling, choose Riding and parent targets under pedals animated by your own crank/animation logic. Balance Rider follows these targets; it does not generate a pedal cycle or propulsion. |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Scooter with both feet on deck | Fit a standing pelvis anchor and use Riding for both feet, with targets on the deck.                                                                                                                                                                       |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Scooter with one pushing foot  | Use Riding for the planted foot and Speed Blend for the other. Select Manual and animate Manual Riding Blend plus the Ground/Riding transforms for a push gesture. The gesture does not itself accelerate the vehicle.                                     |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Quad / fixed riding stance     | Keep feet on riding rests with Riding or leave their Seat anchors unchanged. Use Wheeled drive mode.                                                                                                                                                       |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-seats--optional-physical-torso-support:

Optional physical torso support
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Support Balance** applies a bounded spring torque to the seated/standing humanoid ragdoll pelvis. **Forward Lean** sets the target forward/backward lean relative to the pelvis/backrest frame. **Steering Lean** adds signed side lean from steering input; zero disables steering-dependent lean. **Balance Spring**, **Balance Damper** and **Maximum Balance Torque** set stiffness, damping relative to the chassis and the torque cap. Support is off by default. Start with modest values and a reachable stance; excessive support can oppose the neck, hip or harness limits.

This supports the rider’s body, not the vehicle chassis. Two-wheel vehicle upright/lean assistance remains part of MotorcycleProfile. Four-wheel vehicles continue to use Wheeled. The support requires an occupied active Ragdoll Physics seat and a dynamic humanoid pelvis; Animator/IK/Attach Only/Custom controllers and ejected occupants receive no balancing torque. Disabling the behaviour or support stops added torque without changing the skeleton’s joint limits. Head support remains separately configurable on Passenger Seat.

.. _evs-seats--runtime-posture-input:

Runtime posture input
~~~~~~~~~~~~~~~~~~~~~

Change these public settings on the existing component; no special vehicle input source is needed:

**Example:** ``BalanceRiderPostureInput.cs``

.. raw:: html

   <!-- example: BalanceRiderPostureInput.cs -->

.. code-block:: csharp

   using EasyVehicleSystem;
   using UnityEngine;

   public sealed class BalanceRiderPostureInput : MonoBehaviour
   {
       [SerializeField] private BalanceRider rider;

       // Call from your animation/input code: 0 = ground, 1 = riding/deck.
       public void SetFootReturn(float progress)
       {
           if (!rider) return;
           rider.leftFootMode = RiderFootMode.Riding;
           rider.rightFootMode = RiderFootMode.SpeedBlend;
           rider.blendSource = RiderBlendSource.Manual;
           rider.manualRidingBlend = Mathf.Clamp01(progress);
       }
   }

.. _evs-seats--quads-and-other-straddled-wheeled-vehicles:

Quads and other straddled wheeled vehicles
------------------------------------------

A quad uses **Wheeled** drive mode. It does not require MotorcycleProfile or a special quad profile: four-wheel contact, braking, engine/transmission, differential and steering use the same modules as a car.

1. Configure four Wheel Colliders in **Vehicle Controller > Wheels**. Enable steering on the front pair; choose rear-wheel drive or all four driven wheels. Set each wheel’s radius, width, travel, drive weight and brake role, then apply the configuration.
2. Fit chassis mass, center of mass, track width, suspension and tire grip to the actual model. Start with a low center of mass and moderate steering travel; a quad can roll over naturally, and it does not use motorcycle lean/balance assistance. Anti Roll is available when additional roll resistance is wanted.
3. Add a **Passenger Seat** with **Ragdoll Physics**. Position the pelvis/backrest anchor over the saddle and author left/right foot anchors on the foot rests. Use **Seated pose** to fit the pelvis, feet and hand targets; preview the pose before increasing restraint springs. Keep feet on their riding rests, including when stopped.
4. Use **Motorcycle Handlebar** for the two grip tubes. Parent its grip centers under the moving handlebar, assign it to both seat hand bindings, and use **Prepare hand grip**. Despite its name, this handle works with Wheeled and does not require BalanceRider or MotorcycleProfile.
5. Animate the handlebar with **Steering Wheel Animator**. Assign the handlebar transform, choose its local hinge axis, enable **Override Steering Angle** and set **Steering Angle At Full Lock** (for example 25–35° as a visual starting point). The angle follows resolved wheel steering, not a keyboard-specific input. This local visual angle does not change tire steering. Use Invert if the model turns the wrong way. Keep the hand grip centers beneath this moving transform so IK follows it.
6. Enable the seat’s **Hold Head Forward** if the leaning torso lets the head fall. Start with zero **Head Pitch** and tune pitch, stiffness, damping and torque cap in Play Mode. The support points along the seat’s forward frame, so fit torso lean through the pelvis/backrest anchor rather than tipping the entire Seat object solely to recline the body.

BalanceRider is optional. Its foot-ground transition is intended for two-wheel riders and is usually unnecessary on a quad. If a custom vehicle needs it, disable **Motorcycle Profile Only** and supply all four foot poses. Head support belongs to the seat and works even when BalanceRider is absent or disabled. Ordinary keyboard, analog, external AI and direct sources can drive the quad through the same Vehicle Controller interfaces used for cars.

.. _evs-seats--check-a-fitted-seat:

Check a fitted seat
-------------------

+-----------------------------------------+-----------------------------------------------------------------------+
| Symptom                                 | Check first                                                           |
+=========================================+=======================================================================+
| Body folds or oscillates                | Reach, original anatomy and support travel before increasing springs  |
+-----------------------------------------+-----------------------------------------------------------------------+
| Direct Anchor seems ignored             | A Handle is still assigned and has priority                           |
+-----------------------------------------+-----------------------------------------------------------------------+
| Wrist is correct but fingers penetrate  | Grip dimensions/calibration in the hand guide                         |
+-----------------------------------------+-----------------------------------------------------------------------+
| Foot follows position but twists freely | Align Rotation is separate from Pin To Anchor                         |
+-----------------------------------------+-----------------------------------------------------------------------+
| Free arm keeps chasing a target         | Another IK/animation writer, wrong effective mode or an active handle |
+-----------------------------------------+-----------------------------------------------------------------------+
| Released hand does not reattach         | Damage release latch and reset policy                                 |
+-----------------------------------------+-----------------------------------------------------------------------+
| Foot transfer stays on accelerator      | Resolved brake demand, helper update owner and thresholds             |
+-----------------------------------------+-----------------------------------------------------------------------+

.. _evs-seats--custom-ragdoll-joint-supports:

Custom ragdoll joint supports
-----------------------------

Use **Passenger Seat > Custom Ragdoll Joint Supports > Joint Supports** for additional support at an arbitrary anatomical joint. For example, use a knee target to keep a rider’s knee outside the fuel tank while retaining a spring response to motion. Each entry holds one joint pivot; the original anatomical joint and its angular limits continue to operate.

1. Find the desired **Joint ID** in the occupant’s **Anatomical Joints** list. A knee is normally the joint connecting the thigh to the lower leg. Copy its exact ID; names depend on that rig’s mapping and can be edited by its author.
2. Create an empty target under the vehicle or seat and place it where the knee should be held. Use a vehicle-owned target rather than parenting the target to the supported limb.
3. Add a Joint Supports entry, set **Joint ID**, **Anchor** and **Active**. Keep **Local Offset** at zero to act at the anatomical pivot; use an offset to hold another point on the same rigidbody.
4. Start with moderate **Spring**, **Damper** and **Maximum Force**. Spring pulls the point toward the target; damper reduces motion relative to that moving target. The cap limits their combined force. Increase stiffness only enough to get the required support, so it can work alongside the existing hand, foot and torso restraints.
5. Leave **Hold Rotation** off for a knee that should still rotate within its anatomical limits. Enable it only when an orientation is also required. Then set the desired body rotation using **Rotation Offset**, and tune **Rotation Spring**, **Rotation Damper** and **Maximum Torque** separately. The target orientation is the anchor rotation plus this offset, not an automatically captured seated pose.

Joint-ID supports run in Play mode on an enabled occupied ``HumanoidPassenger``, independently of controller and ragdoll state. They apply physical forces only to dynamic joint rigidbodies; kinematic bodies cannot respond to forces. For plain transforms or kinematic bones, choose Spring in Custom Transform Supports. An entry with an unknown/ambiguous ID or no anchor is skipped. Exiting, ejection, seat disable and controller handover release tracking; a newly seated occupant is resolved by its own joint IDs.

Custom supports remain active if ordinary hand/foot damage restraints release while the character stays seated. Use ``SetJointSupportActive`` to release those custom supports according to your own damage logic. They apply artificial forces to the passenger without applying an equal opposite force to the vehicle. They cannot override locked anatomical axes or make an unreachable pose physically valid.

Position support uses N/m, N/(m/s) and N; rotation uses Nm/rad, Nm/(rad/s) and Nm. Zero maximum force/torque disables that contribution. Anchors may move during play; damping accounts for their motion. Keep targets near reachable limb positions and move them smoothly for a soft response.

.. _evs-seats--configure-a-knee-target-from-code:

Configure a knee target from code
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Attach this script to an application object, assign a seat and an empty knee target, and copy the knee’s actual Anatomical Joint ID into the Inspector. The setup can run before occupancy.

.. raw:: html

   <!-- example: KneeSeatSupport.cs -->

.. code-block:: csharp

   using EasyVehicleSystem;
   using UnityEngine;

   public sealed class KneeSeatSupport : MonoBehaviour
   {
       public PassengerSeat seat;
       public Transform kneeTarget;
       public string kneeJointId = "LeftUpperLegToLeftLowerLeg";

       private void Start()
       {
           if (!seat || !kneeTarget) return;
           var support = seat.GetJointSupport(kneeJointId);
           if (support == null)
           {
               support = new PassengerJointSupport { jointId = kneeJointId };
               if (!seat.AddJointSupport(support)) return;
           }
           support.anchor = kneeTarget;
           support.spring = 500f;
           support.damper = 30f;
           support.maximumForce = 300f;
           support.holdRotation = false;
           seat.SetJointSupportActive(kneeJointId, true);
       }

       public void ReleaseKnee() => seat.SetJointSupportActive(kneeJointId, false);
       public void HoldKnee() => seat.SetJointSupportActive(kneeJointId, true);
   }

For live changes, ``seat.UpdateJointSupport(kneeJointId, support => support.spring = 700f)`` edits the entry and restarts target tracking. ``TryGetJointSupportState`` exposes the supported world point, target point and last applied force/torque; see the :ref:`API reference <evs-api-passengercontrollers--passengerjointsupportstate>`.

Select the vehicle or seat to show yellow target markers and lines to resolved anatomical pivots. Under the bottom **Gizmos** foldout, **Show anchors**, **Show connections** and **Show labels** control these guides independently. A pre-placed **Body** can supply joint positions for the editor preview; a prefab-only occupant is resolved after spawning.

.. _evs-seats--seated-recovery-without-pose-resets:

Seated recovery without pose resets
-----------------------------------

Physical seated limbs follow their anatomical joints and configured seat/handle supports. A closed palm uses a native point attachment and spring-driven wrist rotation. Explicit vehicle resets, re-entry and ``ResetSeatedPose()`` place the body deliberately.

Strong impacts can temporarily stretch native constraints. **Solver Iterations** and **Solver Velocity Iterations** improve constraint accuracy; a smaller project **Fixed Timestep** reduces movement between physics solves at a higher CPU cost. WheelCollider substeps refine wheel simulation, not the passenger skeleton. The package does not change the project timestep automatically.

Test the timestep, solver settings and collision policy with reachable limb targets and the actual vehicle. See `PhysX joint tuning <https://nvidia-omniverse.github.io/PhysX/physx/5.3.1/docs/Joints.html>`__ for solver convergence and projection tradeoffs.
