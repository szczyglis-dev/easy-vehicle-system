# Cameras, passengers, water, towing and weapons

[Back to the complete Inspector reference](../InspectorReference.md).

| Component or data block | Settings declared here |
| --- | --- |
| [AccessAnimationEvents](#accessanimationevents) | 0 |
| [AccessAnimationProfile](#accessanimationprofile) | 37 |
| [AccessMotion](#accessmotion) | 0 |
| [AdaptiveHandGrip](#adaptivehandgrip) | 9 |
| [AdaptiveHandGrip.Finger](#adaptivehandgripfinger) | 10 |
| [AnchorHandle](#anchorhandle) | 8 |
| [BalanceRider](#balancerider) | 18 |
| [CameraModule](#cameramodule) | 4 |
| [Cameras](#cameras) | 5 |
| [ControlHandle](#controlhandle) | 1 |
| [Coupler](#coupler) | 13 |
| [CustomPassengerBody](#custompassengerbody) | 0 |
| [DroppableObject](#droppableobject) | 3 |
| [GearLeverHandle](#gearleverhandle) | 0 |
| [GearPaddleHandle](#gearpaddlehandle) | 0 |
| [HandGrip](#handgrip) | 5 |
| [HandGrip.FingerPose](#handgripfingerpose) | 3 |
| [HandleAnimatorBinding](#handleanimatorbinding) | 15 |
| [HandleFingerPosition](#handlefingerposition) | 7 |
| [HandleHandPose](#handlehandpose) | 19 |
| [HandleHandPosition](#handlehandposition) | 5 |
| [HandleHandPositionPreset](#handlehandpositionpreset) | 3 |
| [HandlePoseSettings](#handleposesettings) | 9 |
| [HandleUseSettings](#handleusesettings) | 16 |
| [HumanoidAccessMotion](#humanoidaccessmotion) | 2 |
| [HumanoidIK](#humanoidik) | 16 |
| [HumanoidJointDefinition](#humanoidjointdefinition) | 5 |
| [HumanoidPassenger](#humanoidpassenger) | 14 |
| [InteriorCamera](#interiorcamera) | 6 |
| [JoystickHandle](#joystickhandle) | 0 |
| [MotorcycleHandle](#motorcyclehandle) | 4 |
| [ObjectDropper](#objectdropper) | 2 |
| [OrbitCamera](#orbitcamera) | 12 |
| [PassengerAccess](#passengeraccess) | 13 |
| [PassengerBehaviour](#passengerbehaviour) | 1 |
| [PassengerBody](#passengerbody) | 0 |
| [PassengerBodyPartConfig](#passengerbodypartconfig) | 5 |
| [PassengerFootConfig](#passengerfootconfig) | 11 |
| [PassengerGForceLimits](#passengergforcelimits) | 11 |
| [PassengerHandConfig](#passengerhandconfig) | 22 |
| [PassengerJointSupport](#passengerjointsupport) | 12 |
| [PassengerModule](#passengermodule) | 0 |
| [PassengerRestraints](#passengerrestraints) | 38 |
| [Passengers](#passengers) | 1 |
| [PassengerSeat](#passengerseat) | 34 |
| [PassengerTransformSupport](#passengertransformsupport) | 14 |
| [PedalFootMode](#pedalfootmode) | 0 |
| [PedalHandle](#pedalhandle) | 2 |
| [RagdollCollisionHelper](#ragdollcollisionhelper) | 13 |
| [RagdollCollisionRelay](#ragdollcollisionrelay) | 0 |
| [Rocket](#rocket) | 23 |
| [RocketLauncher](#rocketlauncher) | 4 |
| [RotaryHandle](#rotaryhandle) | 0 |
| [SeatAccess](#seataccess) | 27 |
| [SteeringHandRegrip](#steeringhandregrip) | 2 |
| [SteeringHandRegripSettings](#steeringhandregripsettings) | 7 |
| [SteeringWheelHandle](#steeringwheelhandle) | 20 |
| [SteeringWheelHandle.RimSample](#steeringwheelhandlerimsample) | 2 |
| [SwitchHandle](#switchhandle) | 0 |
| [ThrottleHandle](#throttlehandle) | 0 |
| [Trailer](#trailer) | 5 |
| [VehicleHandle](#vehiclehandle) | 32 |
| [WaterInteraction](#waterinteraction) | 4 |
| [WaterProvider](#waterprovider) | 0 |
| [WaterStyle](#waterstyle) | 12 |
| [WaterSurface](#watersurface) | 11 |
| [WeaponBarrel](#weaponbarrel) | 10 |
| [WorldModule](#worldmodule) | 0 |
| [YokeHandle](#yokehandle) | 0 |

## AccessAnimationEvents

Relays animation access markers into the sequence.

**Source:** `Runtime/World/Passengers/Access/AccessAnimationEvents.cs`. Component / asset.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

## AccessAnimationProfile

Stores animation states, references and timing configuration.

**Source:** `Runtime/World/Passengers/Access/AccessAnimationProfile.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `completionTimeout` | `float` | Additional time allowed before an unfinished access operation is cancelled, in seconds. | `2`; Minimum: .1f |
| `controller` | `RuntimeAnimatorController` | Animator controller containing the standing, seated, entry and exit states named below. The profile's bindings must match this controller for boarding animation to start. | `None / unassigned` |
| `enterClip` | `AnimationClip` | Humanoid reference clip used to measure the entry trajectory. It must match the motion played by Enter State so placement correction follows the visible animation. | `None / unassigned` |
| `enterLeftFootContact` | `AnimationCurve` | Contact weight over normalized clip time. Zero releases the foot; used with Manual Foot Contacts. | `AnimationCurve.Linear(0, 0, 1, 0)` |
| `enterPlacement` | `AnimationCurve` | Weight of the outside alignment during entry; fades before the character sits. | `AnimationCurve.EaseInOut(0, 1, .65, 0)` |
| `enterRange` | `Vector2` | Start and end of the usable entry motion as fractions of the reference clip, from 0 to 1. Trim idle frames so placement is calibrated over the actual boarding movement. | `new Vector2(0, 1)` |
| `enterRightFootContact` | `AnimationCurve` | Contact weight over normalized clip time. Zero releases the foot; used with Manual Foot Contacts. | `AnimationCurve.Linear(0, 0, 1, 0)` |
| `enterState` | `string` | Animator state path played while the character boards. Use the state containing the entry motion calibrated by Enter Clip and Enter Range. | `"Base Layer.Enter In"` |
| `enterTrigger` | `string` | Trigger parameter sent to the Animator to request the entry animation. The exact trigger name must exist in Controller. | `"EnterIn"` |
| `exitBlendSeconds` | `float` | Blend from the current seated body and hand pose into the exit animation. Zero disables the blend. Ankle rotation remains animated. | `.2`; Minimum: 0 |
| `exitClip` | `AnimationClip` | Humanoid reference clip used to measure the exit trajectory. It must match Exit State so the character is aligned to the doorway and outside position. | `None / unassigned` |
| `exitLeftFootContact` | `AnimationCurve` | Contact weight over normalized clip time. Zero releases the foot; used with Manual Foot Contacts. | `AnimationCurve.Linear(0, 0, 1, 0)` |
| `exitPlacement` | `AnimationCurve` | Outside-alignment weight over normalized exit progress: horizontal axis is progress, vertical axis is weight. Raise the curve earlier to move the character toward the outside placement sooner. | `AnimationCurve.EaseInOut(.2, 0, .85, 1)` |
| `exitRange` | `Vector2` | Start and end of the usable exit motion as fractions of the reference clip. The end must be greater than the start; use this to exclude unrelated frames. | `new Vector2(0, 1)` |
| `exitRightFootContact` | `AnimationCurve` | Contact weight over normalized clip time. Zero releases the foot; used with Manual Foot Contacts. | `AnimationCurve.Linear(0, 0, 1, 0)` |
| `exitState` | `string` | Animator state path played while leaving the seat. Use the state matching Exit Clip and Exit Range. | `"Base Layer.Enter Out"` |
| `exitTrigger` | `string` | Trigger parameter sent to request the exit animation. It must match the transition setup in Controller. | `"EnterOut"` |
| `footBlendSeconds` | `float` | Seconds spent blending foot contact corrections on or off during access motion. Increase to soften foot placement changes; decrease for faster planting/release. | `.16`; Minimum: .01f |
| `handoverBlendSeconds` | `float` | Final seated blend on entry and positional support fade on exit. Exit rotations follow the Animator. Set zero to disable the additional blend. | `.2`; Minimum: 0 |
| `holdFeetWhileIdle` | `bool` | Disable when an application locomotion / ground IK system owns standing feet. | `true` |
| `horizontalScale` | `float` | Scales the horizontal part of the calibrated boarding trajectory. Increase to fit a wider cabin/longer step; vertical placement is adapted separately. | `1`; Range: .5f to 1.5f |
| `layer` | `int` | Animator layer index used to play and inspect boarding/exit states. | `0`; Minimum: 0 |
| `manualFootContacts` | `bool` | Use foot-contact curves instead of automatic height/speed classification. | `false` |
| `plantHeight` | `float` | Maximum foot height above the reference ground, in metres, for considering it planted. Increase to accept more near-ground poses; too high can pin a foot that should be lifting. | `.06`; Minimum: .01f |
| `plantSpeed` | `float` | Maximum foot speed in m/s for considering a near-ground foot planted. Lower values require it to be nearly still; higher values can hold feet during faster motion. | `.3`; Minimum: .01f |
| `playbackSpeed` | `float` | Playback speed multiplier for the boarding and exit motion. | `1`; Minimum: .01f |
| `releaseEntryFeet` | `float` | Normalized boarding progress after which standing foot plants are released. | `.65`; Range: 0 to 1 |
| `rootMotionRotationWeight` | `float` | Weight of extracted root turning. | `1; Range: 0 to 1` |
| `rootMotionScale` | `Vector3` | Local-axis scale of extracted root movement. The seat/outside anchors still define endpoints. | `Vector3.one` |
| `seatedClip` | `AnimationClip` | Humanoid reference clip used to measure the seated pose. Choose a pose matching the end of the boarding sequence and the seat's intended posture. | `None / unassigned` |
| `seatedState` | `string` | Animator state path for the seated pose reached at the end of entry. It supplies the animation-side pose before seated control takes over. | `"Base Layer.Seated"` |
| `seatPose` | `AnimationCurve` | Blend to the physical seat pose. Reach 1 before handing over to seat physics. | `AnimationCurve.EaseInOut(.72, 0, .94, 1)` |
| `standingClip` | `AnimationClip` | Humanoid reference clip used to measure the standing pose for spatial alignment. It calibrates placement; the Animator controller still owns actual playback. | `None / unassigned` |
| `standingState` | `string` | Full Animator state path used for the standing pose, including the layer name when needed. It must match the configured controller exactly. | `"Base Layer.Idle"` |
| `transitionAllowance` | `float` | Extra time allowance in seconds for Animator state transitions during access. | `.2`; Minimum: 0 |
| `useAnimatorRootMotion` | `bool` | Extract translation/turning from Animator root motion; enable for unbaked Root Transform tracks. Disable for movement baked into pose. | `false` |
| `useFootIK` | `bool` | Stabilize grounded feet during access; disable to use the uncorrected animation. | `true` |

## AccessMotion

Replaceable character-motion adapter called by `PassengerAccess` during entry/exit.

**Source:** `Runtime/World/Passengers/Access/AccessMotion.cs`. Abstract base; settings are inherited by derived components.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

## AdaptiveHandGrip

Binds a character to a surface and applies fitted finger poses.

**Source:** `Runtime/World/Passengers/IK/AdaptiveHandGrip.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `digits` | `Finger[]` ([fields](World.md#adaptivehandgripfinger)) | Generated from Mecanim mapping or assigned explicitly for a custom skeleton. | `Empty list` |
| `iterations` | `int` | Finger/contact fitting iteration count. Higher values increase fitting work. | `6`; Range: 2 to 12 |
| `leftHand` | `bool` | Selects the left hand for this grip configuration. | `false` |
| `palmThickness` | `float` | Palm clearance thickness in metres used when fitting the hand to the handle surface. | `.009`; Minimum: .001f |
| `poseRefitAngle` | `float` | Hand rotation change in degrees needed before recalculating finger fit, unless the position threshold is already exceeded. Lower values follow small movements more accurately but refit more often. | `2`; Minimum: 0 |
| `poseRefitDistance` | `float` | Ignore small physical wrist compliance instead of repeatedly re-optimizing finger curls. | `.003`; Minimum: 0 |
| `refitFingersPerFrame` | `int` | Maximum fingers whose contact fit is recalculated in one frame. Lower values spread the work but take more frames to finish a new grip; 5 can update the whole hand together. | `2`; Range: 1 to 5 |
| `showGizmos` | `bool` | Show this component's scene guides and editing handles. Does not change gameplay or physics. Expand **Gizmos** for independent visibility controls; see [Scene gizmo visibility](../Configuration.md#scene-gizmo-visibility) for the controls available on this component. | `true` |
| `wheel` | `SteeringWheelHandle` ([fields](World.md#steeringwheelhandle)) | Steering-wheel surface used to fit this hand's fingers around the rim. For non-wheel grips the general Handle reference supplies the contact instead. | `None / unassigned` |

## AdaptiveHandGrip.Finger

[Grip solving](../API/GripSolving.md)

**Source:** `Runtime/World/Passengers/IK/AdaptiveHandGrip.cs`. Nested configuration data; expand its owning field in the Inspector.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `bones` | `Transform[]` | Three finger bones in order from the palm toward the fingertip. The fitter rotates this chain to wrap the finger around the handle surface. | `new Transform[3]` |
| `flexionAxes` | `Vector3[]` | Local bending axes for the finger joints, in bone order. | `new Vector3[3]` |
| `maximumFlexion` | `Vector3` | Maximum finger-joint flexion angles in degrees for the proximal, intermediate and distal joints. | `new Vector3(85, 110, 80)` |
| `name` | `string` | Readable finger label used to identify this calibration entry, such as Thumb or Index. Bone assignments and calibration determine the actual motion. | `None / unassigned` |
| `openRotations` | `Quaternion[]` | Reference local rotations for the open finger joints, in bone order. | `new Quaternion[3]` |
| `oppositionAxis` | `Vector3` | Local rotation axis used to move the thumb across the palm toward the grip. Set it to the thumb model's opposition direction rather than its curl axis. | `Zero-initialized Vector3` |
| `padRadius` | `float` | Radius in metres representing the finger pad around the sampled finger shape. A larger pad keeps the bones farther from the grip surface and avoids visible penetration. | `.006`; Minimum: .001f |
| `spreadAxis` | `Vector3` | Local rotation axis used to spread or bring together this finger at its base. Calibrate it to the finger bone's actual orientation. | `Zero-initialized Vector3` |
| `thumb` | `bool` | Uses thumb-specific opposition/spread fitting instead of ordinary finger bending. | `false` |
| `tipOffset` | `Vector3` | Offset from the last finger bone to the fingertip in that bone's local coordinates. Set it at the visible tip so contact fitting uses the finger's real length. | `Zero-initialized Vector3` |

## AnchorHandle

Exposes authored hand/foot anchors without control animation.

**Source:** `Runtime/World/Passengers/IK/Handle/AnchorHandle.cs`. Component / asset.

**Inherited settings:** [VehicleHandle](World.md#vehiclehandle). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `anchor` | `Transform` | Palm/ankle contact. Use a stationary grip frame for Closure Change. | `None / unassigned` |
| `closedDistance` | `float` | Distance in metres at full additional closure when multiplier is 1. | `0.03`; minimum 0 |
| `closureAngles` | `Vector3` | Additional base/middle/tip flexion in degrees for the four fingers; excludes thumb. | `(20, 35, 25)` |
| `closureMultiplier` | `float` | Scales normalized closure before clamping to 0–1. | `1`; minimum 0 |
| `controlAnchor` | `Transform` | Moving lever contact measured against Anchor in Closure Change. | `None / unassigned` |
| `followAnchorRotation` | `bool` | When false, resolved contact rotation stays in the vehicle frame while position follows the anchor. | `true` |
| `mode` | `AnchorHandleMode` | Follow the anchor normally, or use ClosureChange to add four-finger flexion from control distance. Requires Adaptive Grip for finger closure. | `Follow` |
| `openDistance` | `float` | World-space distance in metres at zero additional closure. Must exceed Closed Distance. | `0.06`; minimum 0.0001 |

## BalanceRider

Configurable foot poses and optional physical rider support for seated or standing riders on motorcycles, bicycles, scooters and other vehicles.

**Source:** `Runtime/World/Passengers/Seats/BalanceRider.cs`. Component / asset.

**Inherited settings:** [PassengerBehaviour](World.md#passengerbehaviour). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `balanceDamper` | `float` | Damping relative to the chassis in Nm per rad/s. | `25`; Minimum: 0 |
| `balanceSpring` | `float` | Pelvis support stiffness in Nm/rad. | `250`; Minimum: 0 |
| `blendSource` | `RiderBlendSource` | Speed uses vehicle speed magnitude. Manual uses Manual Riding Blend, which your input/animation code can update. Options: `Speed`, `Manual`. | `Speed` |
| `blendSpeed` | `float` | Maximum change in Riding Blend per second, for both Speed and Manual sources. A value of 4 takes 0.25 seconds to cover the full Ground-to-Riding range. | `4`; Minimum: .01f |
| `forwardLean` | `float` | Desired forward lean relative to the Seat frame. Positive leans forward; negative leans backward. | `0`; Range: -60 to 60 |
| `fullyRaisedAtKph` | `float` | Speed magnitude where feet in Speed Blend fully request the Riding pose. The transition is still smoothed by Blend Speed. Ignored for Manual source. | `8`; Speed field; stored in km/h, displayed in the selected speed unit |
| `leftFootGround` | `Transform` | Left-foot Ground target. Used by Ground mode or as the start of Speed Blend. This is an authored transform, not an automatic ground raycast; it is optional in Riding/Unchanged modes. | `None / unassigned` |
| `leftFootMode` | `RiderFootMode` | How each foot uses Ground/Riding poses. Unchanged leaves the Seat binding alone; Riding can follow a moving pedal or scooter deck anchor. Options: `SpeedBlend`, `Riding`, `Ground`, `Unchanged`. | `SpeedBlend` |
| `leftFootRiding` | `Transform` | Left-foot Riding target. Place on a peg/deck or under an animated pedal. Riding mode follows it directly; Speed Blend uses it as its raised endpoint. | `None / unassigned` |
| `liftStartsAtKph` | `float` | Speed magnitude where Ground-to-Riding blending begins when Blend Source is Speed. Reverse speed uses the same magnitude. Ignored for Manual source and fixed-foot modes. | `1`; Speed field; stored in km/h, displayed in the selected speed unit |
| `manualRidingBlend` | `float` | Requested transition from Ground (0) to Riding (1) when Blend Source is Manual. | `0`; Range: 0 to 1 |
| `maximumBalanceTorque` | `float` | Maximum artificial pelvis torque in Nm. Zero applies no torque. | `120`; Minimum: 0 |
| `motorcycleProfileOnly` | `bool` | Run this rider behaviour only while the vehicle uses MotorcycleProfile. Disable to use it with another drive profile. | `false` |
| `rightFootGround` | `Transform` | Right-foot Ground target, independent of the left foot. Ground mode follows it directly; Speed Blend interpolates from it to Right Foot Riding. | `None / unassigned` |
| `rightFootMode` | `RiderFootMode` | Right-foot pose policy, independent of the left foot. Unchanged preserves the Seat binding. Options: `SpeedBlend`, `Riding`, `Ground`, `Unchanged`. | `SpeedBlend` |
| `rightFootRiding` | `Transform` | Right-foot Riding target. Can follow a moving pedal or define the return pose for a scooter pushing foot. Required in Riding and Speed Blend modes. | `None / unassigned` |
| `steeringLean` | `float` | Additional rider lean into commanded steering at full input. Negative reverses lean direction. Zero disables turn lean. | `0`; Range: -45 to 45 |
| `supportBalance` | `bool` | Apply bounded pelvis torque toward the seat-forward stance. Supports the rider only; does not balance the vehicle or animate bicycle pedalling. | `false` |

## CameraModule

Base class for a Cameras submodule. Cameras renders its selected enabled submodule once per frame.

**Source:** `Runtime/World/Camera/CameraModule.cs`. Abstract base; settings are inherited by derived components.

**Inherited settings:** [WorldModule](World.md#worldmodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `active` | `bool` | Activate this view after assigning a camera. Inactive views never move the camera or change its lens. | `false` |
| `anchor` | `Transform` | Explicit position and rotation reference. If unassigned, the vehicle root is used. | `None / unassigned` |
| `requirePointerLock` | `bool` | Only read mouse movement while the cursor is locked. Your game controls cursor capture. | `false` |
| `sensitivity` | `float` | Degrees of camera look change per mouse-delta unit. Increase for faster mouse looking; decrease for finer aim around the same allowed view range. | `.15` |

## Cameras

Optional vehicle camera owner. It moves an explicitly assigned camera only while the selected submodule is Active. It releases ownership when inactive, detached or disabled.

**Source:** `Runtime/World/Camera/Cameras.cs`. Component / asset.

**Inherited settings:** [WorldModule](World.md#worldmodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `customModule` | `CameraModule` ([fields](World.md#cameramodule)) | Selected custom CameraModule on this GameObject. Used when mode is Custom. | `None / unassigned` |
| `enableControls` | `bool` | Allows the camera system to process look/zoom input. Use SetControlsEnabled(false) from code to disable controls and clear pending input immediately. | `true` |
| `mode` | `ViewMode` | Orbit uses the exterior orbit module; Interior uses the cabin module; Custom uses Custom Module. Selecting a mode changes which module controls the assigned view camera. Options: `Orbit`, `Interior`, `Custom`. | `Orbit` |
| `readMouseInput` | `bool` | Reads mouse movement/scroll for look and zoom. Turn off when another input adapter calls the camera API, so mouse input is not also added. | `true` |
| `viewCamera` | `Camera` | Optional camera to control. Leave empty when using your own camera system. | `None / unassigned` |

## ControlHandle

**Source:** `Runtime/World/Passengers/IK/Handle/ControlHandle.cs`. Shared IK contact for an animated control. Inherits AnchorHandle; supplies limb permissions, palm/finger poses and a reference to the controlling animator. It never moves the control model.

**Inherited settings:** `AnchorHandle`.

| Setting | Type | Meaning |
| --- | --- | --- |
| `animator` | `ControlAnimator` | Visual controller paired with this IK contact. Its InteractionValue is observed for generic contact value events; the handle never writes control geometry. |

## Coupler

Validates and owns one hitch relationship, joint and changed collision pairs.

**Source:** `Runtime/World/Towing/Coupler.cs`. Component / asset.

**Inherited settings:** [WorldModule](World.md#worldmodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `allowJointBreak` | `bool` | Allow physical forces to break the hitch. Disable for an unbreakable connection. | `true` |
| `attachDistance` | `float` | Maximum separation in metres between the towing hitch and trailer hitch for attachment. Increase to allow coupling from farther away. | `1.2`; Minimum: .05f |
| `attachmentAlignmentTime` | `float` | Seconds to bring accepted nearby hitches together without an instantaneous correction impulse. | `1.5`; Minimum: .05f |
| `attachOnStart` | `bool` | Attach Initial Trailer at startup. Manual TryAttach remains available when disabled. | `true` |
| `breakForce` | `float` | Force in newtons above which the native hitch joint may break when Allow Joint Break is on. Increase for a stronger coupling; turn breaking off for an unbreakable joint. | `200000`; Minimum: 0 |
| `breakTorque` | `float` | Torque in N·m above which the hitch joint may break when Allow Joint Break is on. Lower values let severe twisting separate the trailer sooner. | `200000`; Minimum: 0 |
| `hitch` | `Transform` | World-space coupling point used to align the trailer connection. | `None / unassigned` |
| `initialTrailer` | `Trailer` ([fields](World.md#trailer)) | Trailer to attach at startup when Attach On Start is enabled. It must still satisfy hitch distance and normal attachment eligibility checks. | `None / unassigned` |
| `longitudinalDamper` | `float` | Fore/aft hitch damping in N·s/m. | `50000`; Minimum: 0 |
| `longitudinalSpring` | `float` | Fore/aft hitch stiffness in N/m. A compliant drawbar prevents parked tire constraints from fighting a perfectly rigid longitudinal lock. | `1000000`; Minimum: 1 |
| `pitchLimit` | `float` | Maximum hitch pitch articulation in degrees. | `30`; Range: 1 to 80 |
| `rollLimit` | `float` | Maximum hitch roll articulation in degrees. | `20`; Range: 1 to 80 |
| `vehicle` | `VehicleController` ([fields](Controller.md#vehiclecontroller)) | Towing vehicle whose Rigidbody receives the hitch connection and supplies commands to the trailer. If empty, the component looks on the same GameObject. | `None / unassigned` |

## CustomPassengerBody

Minimal body for application-owned Custom occupancy.

**Source:** `Runtime/World/Passengers/Bodies/CustomPassengerBody.cs`. Component / asset.

**Inherited settings:** [PassengerBody](World.md#passengerbody). These settings also appear on this type.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

## DroppableObject

Detaches the actual payload and establishes released physics.

**Source:** `Runtime/World/Weapons/DroppableObject.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `inheritVelocity` | `bool` | Retains the carrier's point velocity when releasing this payload. | `true` |
| `localReleaseVelocity` | `Vector3` | Optional separation velocity in this object's local axes, in metres per second. | `Zero-initialized Vector3` |
| `mass` | `float` | Mass in kilograms of the released payload. It affects inertia and collision response after the object separates from its carrier. | `10`; Minimum: .01f |

## GearLeverHandle

**Source:** `Runtime/World/Passengers/IK/Handle/GearLeverHandle.cs`. IK-only palm contact on a gear lever. Inherits ControlHandle; default authoring selects the right hand.

**Inherited settings:** `ControlHandle`.

Configure inherited contact/pose settings on this component; visual motion belongs to its animator.

## GearPaddleHandle

**Source:** `Runtime/World/Passengers/IK/Handle/GearPaddleHandle.cs`. IK-only palm contact on a moving gear paddle. Inherits ControlHandle; choose allowed limb, occupant and reach/return timing here.

**Inherited settings:** `ControlHandle`.

Configure inherited contact/pose settings on this component; visual motion belongs to its animator.

## HandGrip

Stores character hand frames and fallback finger poses.

**Source:** `Runtime/World/Passengers/IK/HandGrip.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `angularDamper` | `float` | Damping of wrist rotation for an external grip. Increase to reduce wobble around the target palm orientation; ordinary handles can supply their own damping. | `35`; Minimum: 0 |
| `angularSpring` | `float` | Strength pulling an externally driven physical wrist toward the grip orientation. Higher values hold the palm angle more firmly; an ordinary VehicleHandle can supply its own wrist drive settings instead. | `1200`; Minimum: 0 |
| `contactPoint` | `Transform` | Palm-contact marker on the hand, separate from the wrist bone origin. Its position and orientation are aligned to the target grip so the palm touches the handle correctly. | `None / unassigned` |
| `fingers` | `FingerPose[]` ([fields](World.md#handgripfingerpose)) | Finger-bone pose entries switched between relaxed and gripping rotations. Add each bone that should change when the hand grips or releases. | `Empty list` |
| `maximumTorque` | `float` | Maximum wrist-orientation torque in N·m for an external grip. Lower values let the palm yield under load even with a strong angular spring. | `250`; Minimum: 0 |

## HandGrip.FingerPose

Value data for finger pose; its fields are listed below.

**Source:** `Runtime/World/Passengers/IK/HandGrip.cs`. Nested configuration data; expand its owning field in the Inspector.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `bone` | `Transform` | Individual finger bone receiving the configured grip or relaxed local rotation. Add multiple entries to pose a full finger chain. | `None / unassigned` |
| `gripRotation` | `Quaternion` | Bone's local rotation when the hand grips. Adjust each finger bone so the closed hand wraps around the intended control. | `Zero-initialized Quaternion` |
| `relaxedRotation` | `Quaternion` | Bone's local rotation when the hand is not gripping. Set it to the finger's natural open/resting pose. | `Zero-initialized Quaternion` |

## HandleAnimatorBinding

**Source:** `Runtime/World/Passengers/IK/Handle/Core/HandleAnimatorBinding.cs`. Component binding for animation/Timeline and handle feedback.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `animator` | `Animator` | Optional Animator receiving configured output parameters. | Unassigned |
| `changingParameter` | `string` | Optional Animator bool receiving IsValueChanging. | Unassigned |
| `contactParameter` | `string` | Optional Animator bool receiving this occupant last sampled contact state. | Unassigned |
| `contactTransform` | `Transform` | Application palm/fingertip frame overriding automatic contact tracking while this binding applies. | Unassigned |
| `drivePoseWeights` | `bool` | Write configured pose weights to the resolved handle each Apply. | `true` |
| `driveTargetOverride` | `bool` | Write Target Override on Apply, including clearing it when unassigned. | `false` |
| `fingerWeight` | `float` | Finger overlay weight. | `1`; range 0–1 |
| `handle` | `VehicleHandle` | Explicit handle; empty resolves the selected seat limb current handle, including transfers/selectors. | Unassigned |
| `part` | `PassengerBodyPart` | Seat limb controlled by this binding. | `RightHand` |
| `physicalWeight` | `float` | Independent physical palm support weight. | `1`; range 0–1 |
| `positionWeight` | `float` | Position overlay weight. | `1`; range 0–1 |
| `rotationWeight` | `float` | Rotation overlay weight. | `1`; range 0–1 |
| `seat` | `PassengerSeat` | Seat supplying the selected occupant/limb and contact state. | Unassigned |
| `targetOverride` | `Transform` | World-space pose target written when Drive Target Override is enabled. | Unassigned |
| `valueParameter` | `string` | Optional Animator float receiving InteractionValue.x. | Unassigned |

## HandleFingerPosition

| Setting | Type | Default | Description |
| --- | --- | --- | --- |
| `baseRotation` / `middleRotation` / `tipRotation` | `Vector3` | Zero | Additional XYZ segment rotation; each axis has a degree slider. |
| `closure` | `float` | `1`; Range: 0–1 | Saved per-finger helper value. Auto-apply closure controls whether moving it rewrites the pose. Ignored by gameplay. |
| `curlAngles` | `Vector3` | `(85, 110, 80)` | Signed base/middle/tip flexion about the selected axis, bounded anatomically; thumb Middle/Tip follow the Base hinge. |
| `curlAxis` | `HandleCurlAxis` | `Default` | Independent thumb Base hinge; Default uses mirrored Base Z. Middle/Tip derive axes through their neutral rotations. Non-thumb fingers use the hand-level selector. |
| `surfaceFit` | `float` | `1`; Range: 0–1 | Blend from authored curl to adaptive surface IK fit. |

## HandleHandPose

| Setting | Type | Default | Description |
| --- | --- | --- | --- |
| `closure` | `float` | `1`; Range: 0–1 | Saved four-finger editor helper value; excludes the thumb. Applies pose changes only with Auto-apply closure enabled. Ignored by gameplay. |
| `constrainThumbToRim` | `bool` | `false` | Enable wheel pinch contact constraints. |
| `curlAxis` | `HandleCurlAxis` | `Default` | Shared curl axis for the four non-thumb fingers: calibrated flexion by default or explicit X/Y/Z. |
| `maximumFingerSpeed` | `float` | `300` | Maximum finger rotation speed for pose changes within one bound handle, degrees per second. Cross-handle transitions use Finger Blend Duration. |
| `position` / `rotation` | `Vector3` | Zero | Anchor-local palm offset in metres and XYZ degrees; rotation has per-axis sliders. |
| `thumb` / `index` / `middle` / `ring` / `little` | `HandleFingerPosition` | New finger | Five independently configurable fingers. |
| `thumbAim` | `HandleThumbAim` | `SurfaceFit` | Surface fit, palm-forward or index-direction thumb aiming. |
| `thumbAimLimit` | `float` | `100`; Range: 0–180 | Maximum calibrated thumb base aim rotation. |
| `thumbBaseCone` | `float` | `50` | Surface-fitting thumb base cone limit. |
| `thumbDepthRatio` / `thumbInwardRatio` | `float` | `.8` / `.25`; Range: 0–2 | Minimum thumb-tip distance ratios relative to rim depth/radius. |
| `thumbInwardAngle` | `float` | `0`; Range: 0–60 | Extra thumb aim towards wheel centre. |
| `thumbOppositionLimit` | `float` | `12` | Surface-fitting thumb opposition limit. |
| `thumbSpreadLimit` | `float` | `5` | Surface-fitting thumb spread limit. |

## HandleHandPosition

Reusable named position on every VehicleHandle. The Inspector supplies Copy/Paste, Save-as-asset and Make-local controls.

| Setting | Type | Default | Description |
| --- | --- | --- | --- |
| `autoApplyClosure` | `bool` | `true` | Editor-only local setting. When false, Closure edits save only their own helper value. A linked preset supplies its own setting instead. |
| `left` / `right` | `HandleHandPose` | New pose | Independent local hand data when no shared asset is assigned. |
| `name` | `string` | `Grip` | Display name in position selectors. |
| `preset` | `HandleHandPositionPreset` | Unassigned | Shared left/right data and Auto-apply closure setting. The Inspector labels shared hand sections with the position name. |

## HandleHandPositionPreset

ScriptableObject created with **Create > EasyVehicleSystem > Controls > Hand Position Preset**. Its `left` and `right` HandleHandPose blocks are shared by every referencing handle; **Local** makes an independent copy. See [Reusable hand positions](../HandPositions.md).

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `autoApplyClosure` | `bool` | `true` | Shared editor-only checkbox below the preset information box. When false, Closure sliders save only their own helper values. |
| `left` | `Wheel` ([fields](Physics.md#wheel)) | Left Wheel on this axle. Its suspension compression is compared with Right to calculate the force opposing body roll. | `None / unassigned` |
| `right` | `Wheel` ([fields](Physics.md#wheel)) | Right Wheel on this axle. Assign its matching left wheel in Left; both wheels must be operational and grounded for this axle's anti-roll force. | `None / unassigned` |

## HandlePoseSettings

**Source:** `Runtime/World/Passengers/IK/Handle/Core/HandleInteraction.cs`. Referenced configuration block; expand its owning field.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `contactAngle` | `float` | Maximum orientation difference in degrees for automatic contact. | `180`; range 0–180 |
| `contactDistance` | `float` | Contact acquisition distance in metres. | `0.03`; minimum 0 |
| `contactSource` | `HandleContactSource` | Automatic samples contact distance/angle; Manual uses application-reported contact. | `Automatic` |
| `fingerWeight` | `float` | Finger pose overlay weight. | `1`; range 0–1 |
| `physicalWeight` | `float` | Independent physical palm support weight. Zero releases the palm constraint while retaining ragdoll anatomy. | `1`; range 0–1 |
| `positionWeight` | `float` | Limb position overlay weight. | `1`; range 0–1 |
| `releaseDistance` | `float` | Larger release distance adds hysteresis to contact events. | `0.05`; minimum 0 |
| `rotationWeight` | `float` | Limb rotation overlay weight. | `1`; range 0–1 |
| `targetOverride` | `Transform` | Optional final world-space IK target supplied by animation, Timeline or application code. | Unassigned |

## HandleUseSettings

**Source:** `Runtime/World/Passengers/IK/Handle/Core/HandleUseSettings.cs`. Referenced settings on every VehicleHandle.

| Setting | Meaning |
| --- | --- |
| `allowOtherLimbs` | If the preferred limb is unavailable, try other allowed limbs in left hand, right hand, left foot, right foot order. |
| `allowUnsupportedDeparture` | Default false. Allows departure even when the source would fall below Minimum Attachments. Independent of priority; does not cancel another limb's request. |
| `input` | Command channel observed when Source is Command. Signed axes use their absolute magnitude. |
| `interruptLowerPriority` | Default false. Allows strictly higher-priority timed requests to interrupt timed ownership on the same limb; persistent and Animator ownership remain protected. |
| `liftHeight` | Clearance arc height in metres along vehicle-local up during each trip. Zero follows a straight path. |
| `preferredLimb` | First limb attempted for automatic actions and TryUse(seat, target). It must also be enabled in Allowed limbs. |
| `priority` | Higher values try first for simultaneous automatic requests. Interruption additionally requires Interrupt Lower Priority. |
| `releaseDuration` | Seconds used to release physical hand contact before each trip. Guidance remains active. |
| `releaseThreshold` | Lower action release threshold used while this rule owns a token, preventing chatter near the activation point. |
| `returnDelay` | Seconds held at the destination after arrival or the last active automatic action before return starts. |
| `returnDuration` | Seconds to return to the original handle or anchor. Independent of outbound travel; zero completes on the next controller step. |
| `seat` | Explicit seat whose occupant may use this control. |
| `source` | ValueChange observes handle value events; Command reads the selected command channel; ServiceBrake reads resolved service braking. |
| `threshold` | Action activation magnitude. Larger values require more input before requesting a limb. |
| `travelDuration` | Seconds to reach the handle (Outbound Duration). Independent of returnDuration; zero reaches the endpoint on the next controller step. |
| `useOnAction` | Request the configured seat limb while this action is active. |

## HumanoidAccessMotion

Built-in Animator-based humanoid access implementation.

**Source:** `Runtime/World/Passengers/Access/HumanoidAccessMotion.cs`. Component / asset.

**Inherited settings:** [AccessMotion](World.md#accessmotion). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `defaultProfile` | `AccessAnimationProfile` ([fields](World.md#accessanimationprofile)) | Fallback profile; a SeatAccess profile takes precedence for each request. | `None / unassigned` |
| `seatedPoseController` | `RuntimeAnimatorController` | Optional controller sampled for the actual Animator/Animator + IK seated destination and restored after entry, including steering hands. Match the controller used after seating. Null retains the IK/reference target. | `None / unassigned` |

## HumanoidIK

Uses character frames to resolve limb targets.

**Source:** `Runtime/World/Passengers/IK/HumanoidIK.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `leftElbowHint` | `Transform` | Left side: Optional marker choosing which way the elbow bends when reaching. Move it to the desired elbow side to avoid an unnatural arm fold. Humanoid Animator mapping can fill this reference automatically. | `None / unassigned` |
| `leftFoot` | `Transform` | Left side: Ankle/foot bone placed at the seat or pedal target. Its rotation can also follow the configured foot contact. Humanoid Animator mapping can fill this reference automatically. | `None / unassigned` |
| `leftHand` | `Transform` | Left side: Wrist/hand bone placed at the palm target. HandGrip can offset this bone so the visible palm, rather than the wrist origin, touches the control. Humanoid Animator mapping can fill this reference automatically. | `None / unassigned` |
| `leftLowerArm` | `Transform` | Left side: Forearm bone at the elbow; bends the arm so the wrist can reach its target within the joint limits. Humanoid Animator mapping can fill this reference automatically. | `None / unassigned` |
| `leftLowerLeg` | `Transform` | Left side: Shin bone at the knee; bends the leg between the hip and the foot target. Humanoid Animator mapping can fill this reference automatically. | `None / unassigned` |
| `leftUpperArm` | `Transform` | Left side: Upper-arm bone at the shoulder; starts the two-bone arm solve toward the hand target. Humanoid Animator mapping can fill this reference automatically. | `None / unassigned` |
| `leftUpperLeg` | `Transform` | Left side: Thigh bone at the hip; starts the leg solve toward the configured foot target. Humanoid Animator mapping can fill this reference automatically. | `None / unassigned` |
| `matchTargetRotation` | `bool` | Also aligns solved hand/foot orientation with the target where that solver path supports it. Turn off when IK should reach the target position while retaining its existing end-bone orientation. | `false` |
| `maximumForearmRoll` | `float` | Forearm roll for standalone IK without passenger anatomy. Passenger rigs use the saved elbow twist range instead. | `80`; Range: 0 to 90 |
| `rightElbowHint` | `Transform` | Right side: Optional marker choosing which way the elbow bends when reaching. Move it to the desired elbow side to avoid an unnatural arm fold. Humanoid Animator mapping can fill this reference automatically. | `None / unassigned` |
| `rightFoot` | `Transform` | Right side: Ankle/foot bone placed at the seat or pedal target. Its rotation can also follow the configured foot contact. Humanoid Animator mapping can fill this reference automatically. | `None / unassigned` |
| `rightHand` | `Transform` | Right side: Wrist/hand bone placed at the palm target. HandGrip can offset this bone so the visible palm, rather than the wrist origin, touches the control. Humanoid Animator mapping can fill this reference automatically. | `None / unassigned` |
| `rightLowerArm` | `Transform` | Right side: Forearm bone at the elbow; bends the arm so the wrist can reach its target within the joint limits. Humanoid Animator mapping can fill this reference automatically. | `None / unassigned` |
| `rightLowerLeg` | `Transform` | Right side: Shin bone at the knee; bends the leg between the hip and the foot target. Humanoid Animator mapping can fill this reference automatically. | `None / unassigned` |
| `rightUpperArm` | `Transform` | Right side: Upper-arm bone at the shoulder; starts the two-bone arm solve toward the hand target. Humanoid Animator mapping can fill this reference automatically. | `None / unassigned` |
| `rightUpperLeg` | `Transform` | Right side: Thigh bone at the hip; starts the leg solve toward the configured foot target. Humanoid Animator mapping can fill this reference automatically. | `None / unassigned` |

## HumanoidJointDefinition

Saved native joint reference with neutral-frame/flexion metadata used by passenger physics and IK.

**Source:** `Runtime/World/Passengers/Physics/HumanoidJointLimits.cs`. Nested configuration data; expand its owning field in the Inspector.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `connectedReferenceRotation` | `Quaternion` | Reference connected body rotation relative to the passenger root. | `Quaternion.identity` |
| `joint` | `ConfigurableJoint` | Saved `ConfigurableJoint` supplying native axes, anchors, connections and angular limits. | `None / unassigned` |
| `jointId` | `string` | Unique, case-sensitive identifier used by HumanoidPassenger anatomical joint lookup/update APIs. Generated from the connected bones during authoring; freely editable. | `None / unassigned` |
| `referenceFlexion` | `float` | Joint bend in degrees corresponding to the captured reference pose. The IK hinge solver uses this offset to interpret native joint limits correctly; it does not widen those limits. | `0` |
| `referenceRotation` | `Quaternion` | Reference body rotation relative to the passenger root. | `Quaternion.identity` |

## HumanoidPassenger

Connects humanoid rig, pose and physical passenger behavior.

**Source:** `Runtime/World/Passengers/Bodies/HumanoidPassenger.cs`. Component / asset.

**Inherited settings:** [PassengerBody](World.md#passengerbody). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `anatomicalJoints` | `HumanoidJointDefinition[]` ([fields](World.md#humanoidjointdefinition)) | Skeletal joint definitions used to read the body's actual axes, reference pose and bend limits. Edit physical limits on each referenced ConfigurableJoint; this list connects them to the passenger solver. | `System.Array.Empty<HumanoidJointDefinition>()` |
| `animator` | `Animator` | Character Animator providing humanoid bone mapping and animated poses. A valid humanoid avatar lets setup locate the skeleton for IK and hand animation/physics transitions. | `None / unassigned` |
| `automaticSeatedIK` | `bool` | Apply the Animator + IK overlay in LateUpdate. Disable to call SolveSeatedIK from your own animation pipeline. | `true` |
| `exitCollisionClearance` | `float` | Keep the previous vehicle excluded until the departing character clears its combined collider bounds by this distance. Prevents animated kinematic limbs from blocking the doors/chassis. | `.25`; Minimum: 0 |
| `freeRagdollAngularDamping` | `float` | Passive rotational damping while falling or lying down. Does not hold a pose or freeze bones. | `1.5`; Minimum: 0 |
| `freeRagdollCollisionDetection` | `CollisionDetectionMode` | Collision detection used by released ragdoll bodies. Continuous Dynamic prevents fast limbs from stepping through the ground before contact is resolved. The previous mode is restored on attachment. | `CollisionDetectionMode.ContinuousDynamic` |
| `freeRagdollInertiaScale` | `float` | Rotational inertia multiplier for released bones. Reduces abrupt limb rotation from ground impulses without changing body mass, gravity or linear momentum. Restored on attachment. | `4`; Minimum: 1 |
| `freeRagdollJointDamping` | `float` | Passive damping of relative bone rotation. The pose spring stays zero, so joints never return to a riding/idle pose. | `1`; Minimum: 0 |
| `freeRagdollMaximumAngularSpeed` | `float` | Maximum angular speed in radians/second for released bones. Preserves lower per-body limits and restores the previous limit on attachment. | `18`; Minimum: 0.1 |
| `freeRagdollMaximumDampingTorque` | `float` | Maximum stabilizing torque in N·m for each free-ragdoll joint's relative-motion damping. Increase to resist violent limb spin more strongly; it does not pull the body back into a seated pose. | `20`; Minimum: 0 |
| `freeRagdollMaximumDepenetrationVelocity` | `float` | Maximum separation speed in m/s for overlapping free-ragdoll colliders. Caps abrupt push-out after contact while preserving ordinary flight and rolling velocity. Lower per-body limits are preserved, and previous limits return on attachment. | `3`; Minimum: 0.01 |
| `freeRagdollPreprocessing` | `bool` | Enable joint preprocessing for free ragdolls. Leave off when impacts pin bones against the ground: preprocessing incompatible contact/joint constraints can sustain head oscillations. | `false` |
| `freeRagdollSolverIterations` | `int` | Minimum positional solver passes for a released ragdoll. Increase for more stable joint/contact solving at additional physics cost; higher per-body settings are preserved. | `24`; Minimum: 1 |
| `freeRagdollSolverVelocityIterations` | `int` | Minimum velocity solver passes for a free ragdoll. Increase to improve impulse/velocity constraint solving at extra physics cost; this does not stiffen anatomical angle limits. | `8`; Minimum: 1 |
| `ik` | `HumanoidIK` ([fields](World.md#humanoidik)) | Bone solver used to place hands and feet on seat targets. Setup finds an existing HumanoidIK or creates one for a valid humanoid Animator and maps its bones. | `None / unassigned` |
| `pelvis` | `Transform` | Pelvis bone used to place the character on the seat and attach physical seat support. Choose the skeleton's actual hip/pelvis transform. | `None / unassigned` |
| `physicalWhileSeated` | `bool` | Keeps the seated skeleton physically simulated rather than attaching it as a kinematic character. | `true` |
| `ragdollBodies` | `Rigidbody[]` | Rigidbodies belonging to this character's physical skeleton. Seating/release changes their physics state; setup discovers child rigidbodies when the list is empty. | `System.Array.Empty<Rigidbody>()` |

## InteriorCamera

Exact cabin-anchor follow with bounded mouse look and configurable camera lens.

**Source:** `Runtime/World/Camera/InteriorCamera.cs`. Component / asset.

**Inherited settings:** [CameraModule](World.md#cameramodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `fieldOfView` | `float` | Vertical field of view in degrees while interior is active. The core restores the previous lens on release. | `72`; Range: 1 to 179 |
| `nearClipPlane` | `float` | Distance in metres below which geometry is clipped in the cockpit view. The 0.04 default keeps nearby dashboard parts visible; increasing it cuts away more nearby geometry. | `.04`; Minimum: .001f |
| `pitchLimits` | `Vector2` | Minimum/maximum up-down look angles in degrees relative to the cabin view. Tighten them to prevent looking through the roof or the driver's body. | `new Vector2(-55, 65)` |
| `positionOffset` | `Vector3` | Camera displacement in metres in the cabin anchor's local axes. Use it to place the driver's eye position without moving the anchor object. | `Zero-initialized Vector3` |
| `rotationOffset` | `Vector3` | Extra camera orientation in degrees relative to the cabin anchor. Use it to align the default view with the windshield or cockpit forward direction. | `Zero-initialized Vector3` |
| `yawLimits` | `Vector2` | Minimum/maximum left-right look angles in degrees around the cabin's default heading. Widen them to let the driver look farther sideways or behind. | `new Vector2(-180, 180)` |

## JoystickHandle

**Source:** `Runtime/World/Passengers/IK/Handle/JoystickHandle.cs`. Joystick grip and steering-contact geometry. Inherits SteeringWheelHandle; pitch/roll model motion belongs to SteeringStickAnimator.

**Inherited settings:** `SteeringWheelHandle`.

Configure inherited contact/pose settings on this component; visual motion belongs to its animator.

## MotorcycleHandle

Supplies fixed left/right contacts with prepared finger poses.

**Source:** `Runtime/World/Passengers/IK/Handle/MotorcycleHandle.cs`. Component / asset.

**Inherited settings:** [VehicleHandle](World.md#vehiclehandle). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `gripLength` | `float` | Length in metres of the cylindrical grip surface used for hand/finger fitting. Match the usable rubber grip rather than the full handlebar width. | `.11`; Minimum: .01f |
| `gripRadius` | `float` | Tube radius in local metres. Grip centres stay fixed; the editor updates the palm contacts and prepares the fingers. | `.025`; Minimum: .002f |
| `leftGrip` | `Transform` | Centre of the left grip. Local X runs along the tube; local Y points from the palm towards the tube centre. | `None / unassigned` |
| `rightGrip` | `Transform` | Independent right-hand grip frame. Place and orient it on the throttle grip so each hand gets its own handlebar contact pose. | `None / unassigned` |

## ObjectDropper

Validates selected payload release and cooldown.

**Source:** `Runtime/World/Weapons/ObjectDropper.cs`. Component / asset.

**Inherited settings:** [WorldModule](World.md#worldmodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `dropInterval` | `float` | Minimum seconds between accepted object releases. Increase to space drops farther apart; it does not change a released object's falling speed. | `.4`; Minimum: 0 |
| `droppingEnabled` | `bool` | Allows drop requests to release mounted objects. Turn off to keep the payload attached without clearing its configuration. | `true` |

## OrbitCamera

Mouse orbit, scroll zoom, smoothed framing and obstruction avoidance around an explicit anchor.

**Source:** `Runtime/World/Camera/OrbitCamera.cs`. Component / asset.

**Inherited settings:** [CameraModule](World.md#cameramodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `avoidObstacles` | `bool` | Pulls the camera closer when scenery blocks the view from the target. The vehicle itself and its detached damage parts are ignored, so they do not push the camera inward. | `true` |
| `distance` | `float` | Requested distance in metres from the orbit focus. Zoom changes this value within Minimum/Maximum Distance, and obstacle avoidance can temporarily pull the camera closer. | `7`; Minimum: .1f |
| `focusOffset` | `Vector3` | Focus-point offset in metres in Anchor's local coordinates. Raise Y to orbit around the cabin/rider rather than the vehicle root. | `new Vector3(0, 1.1, 0)` |
| `followResponse` | `float` | Speed at which camera rotation and distance settle toward the requested orbit. Increase for a tighter response; decrease for softer camera movement. | `12`; Minimum: .01f |
| `initialPitch` | `float` | Starting vertical orbit angle in degrees relative to the anchor. Adjust it to begin higher above or closer to the vehicle's horizon. | `22` |
| `initialYaw` | `float` | Starting horizontal orbit angle in degrees added to the anchor heading. Use it to start behind or beside the vehicle before mouse look changes the view. | `0` |
| `maximumDistance` | `float` | Farthest orbit zoom in metres. Increase to show a wider area around the vehicle. | `65`; Minimum: .1f |
| `minimumDistance` | `float` | Closest orbit zoom in metres. Increase to prevent zooming into the model; obstacle avoidance can still retract the camera when scenery blocks the view. | `1.5`; Minimum: .1f |
| `obstructionMask` | `LayerMask` | Layers allowed to obstruct the orbit camera. Triggers and owned vehicle geometry are ignored; exclude scenery layers that should not retract the camera. | `~0` |
| `obstructionRadius` | `float` | Radius in metres of the collision probe between focus and camera. Increase to leave more room around the camera when moving past walls. | `.2`; Minimum: .01f |
| `pitchLimits` | `Vector2` | Lowest/highest allowed vertical orbit angles in degrees. Use the range to prevent viewing from below the ground or directly over the roof. | `new Vector2(-5, 70)` |
| `zoomSensitivity` | `float` | Metres of orbit-distance change per normalized scroll input. Increase to zoom faster with the same wheel movement. | `.6`; Minimum: .01f |

## PassengerAccess

Owns the entry/exit state machine, reservation and cancellation.

**Source:** `Runtime/World/Passengers/Access/PassengerAccess.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `cancelled` | `UnityEvent` | Event invoked when an active access operation is aborted. Use it to restore application UI or input state; it does not report successful boarding. | `No listeners` |
| `completed` | `UnityEvent` | Event invoked after successful entry or exit. At this point the occupant/seat assignment has been updated, so gameplay can switch driving or walking controls. | `No listeners` |
| `motion` | `AccessMotion` ([fields](World.md#accessmotion)) | Access-motion component that animates and aligns this character while boarding or leaving. The sequencer starts it after the door is ready and waits for its result before completing access. | `None / unassigned` |
| `onEnterBegin` | `UnityEvent` | Once an admitted entry starts in Opening, after Before checks; seat reservation is held. | `No listeners` |
| `onEnterCancelled` | `UnityEvent` | After a reserved entry is cancelled or fails and cleanup finishes; an immediately rejected request emits nothing. | `No listeners` |
| `onEnterFinish` | `UnityEvent` | Only after the entire entry succeeds, including the required door state and reservation/Target cleanup. | `No listeners` |
| `onEnterInProgress` | `UnityEvent<float>` | After each entry motion sample in Moving, starting at zero; progress one is not whole-sequence completion. Dynamic float argument: normalized motion progress 0..1. | `No listeners` |
| `onExitBegin` | `UnityEvent` | Once an admitted exit starts in Opening, after Before checks; seat reservation is held. | `No listeners` |
| `onExitCancelled` | `UnityEvent` | After a reserved exit is cancelled or fails and cleanup finishes; an immediately rejected request emits nothing. | `No listeners` |
| `onExitFinish` | `UnityEvent` | Only after the entire exit succeeds, including the required door state and reservation/Target cleanup. | `No listeners` |
| `onExitInProgress` | `UnityEvent<float>` | After each exit motion sample in Moving, starting at zero; progress one is not whole-sequence completion. Dynamic float argument: normalized motion progress 0..1. | `No listeners` |
| `passenger` | `PassengerBody` ([fields](World.md#passengerbody)) | Character entering or leaving the vehicle. If empty, this component finds PassengerBody on the same GameObject; the referenced body is handed to the selected seat on entry. | `None / unassigned` |
| `started` | `UnityEvent` | Event invoked when an access request starts sequencing the door and character movement. Use it to block conflicting controls while entry/exit is in progress. | `No listeners` |

## PassengerBehaviour

Configuration/implementation type for passenger behaviour within seats, bodies and controller strategies.

**Source:** `Runtime/World/Passengers/Core/PassengerBehaviour.cs`. Abstract base; settings are inherited by derived components.

**Inherited settings:** [PassengerModule](World.md#passengermodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `seat` | `PassengerSeat` ([fields](World.md#passengerseat)) | Seat this behaviour operates on, such as the driver or rider seat. The behaviour runs only for a valid seat and a compatible vehicle. | `None / unassigned` |

## PassengerBody

Base character adapter used by seats and controller strategies.

**Source:** `Runtime/World/Passengers/Bodies/PassengerBody.cs`. Abstract base; settings are inherited by derived components.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

## PassengerBodyPartConfig

Describes each limb's mode, target and support choices.

**Source:** `Runtime/World/Passengers/Seats/PassengerBodyPartConfig.cs`. Nested configuration data; expand its owning field in the Inspector.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `anchor` | `Transform` | Direct target transform used when no Handle is assigned. Its pose sets where this hand or foot reaches/rests; a handle supplies its own target instead. | `None / unassigned` |
| `enableSelfCollidersOnRelease` | `bool` | Enable contacts between this Free limb and the ragdoll's own body. Neighboring skeletal bodies keep collisions disabled. | `false` |
| `enableVehicleCollidersOnRelease` | `bool` | Enable contacts with the vehicle when this limb enters Free. The seat-wide setting also enables this for released limbs. | `false` |
| `handle` | `VehicleHandle` ([fields](World.md#vehiclehandle)) | Interactive grip or pedal supplying this limb's target and support settings. When assigned, it replaces the direct Anchor; a disabled handle supplies no valid target. | `None / unassigned` |
| `mode` | `PassengerBodyPartMode` | IKHandle places/supports the limb at its resolved target. Animator leaves it to character animation. Free releases target control so physical limbs can hang; free-arm options can still set an initial pose. Options: `IKHandle`, `Animator`, `Free`. | `IKHandle` |

## PassengerFootConfig

Per-foot mode, target and pinning/rotation configuration used by the seat.

**Source:** `Runtime/World/Passengers/Seats/PassengerBodyPartConfig.cs`. Nested configuration data; expand its owning field in the Inspector.

**Inherited settings:** [PassengerBodyPartConfig](World.md#passengerbodypartconfig). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `alignRotation` | `bool` | Guide the ankle orientation towards the authored target rotation, including moving pedals. Disabled by default. | `false` |
| `damper` | `float` | Position damping for a spring-supported foot. Increase to reduce bouncing around the pedal/peg; it does not control ankle rotation. | `70`; Minimum: 0 |
| `hold` | `bool` | Keeps a physical foot supported at its resolved target in IKHandle mode. Pin To Anchor can lock the position; otherwise spring/travel settings determine how much it yields. | `true` |
| `limitTravel` | `bool` | Adds a native distance limit around the foot target for spring-supported feet. Turn off to let the spring yield farther under load. Pin To Anchor overrides this with a locked foot position. | `false` |
| `maximumAcceleration` | `float` | Foot-support force cap in m/s², multiplied by supported leg mass. A positive value enables mass-based support; zero uses the simpler default capped drive. Pin To Anchor overrides spring support. | `0`; Minimum: 0 |
| `maximumRotationTorque` | `float` | Torque cap in N·m for foot-orientation support. Reduce to let the ankle twist under load; increase for a firmer sole orientation. | `25`; Minimum: 0 |
| `pinToAnchor` | `bool` | Physically lock the foot position to its resolved anchor while Hold and IK Handle mode are enabled. Requires a physical seated passenger. Overrides spring and travel settings; ankle rotation remains free unless Align Rotation is enabled. | `false` |
| `rotationDamper` | `float` | Damping of foot rotation around its target angle. Increase to reduce ankle wobble while Align Rotation is enabled. | `12`; Minimum: 0 |
| `rotationSpring` | `float` | Spring turning the physical foot toward the target orientation when Align Rotation is enabled. Increase to keep the sole aligned more firmly. | `160`; Minimum: 0 |
| `spring` | `float` | Position spring holding an unpinned foot at its target. Increase for firmer support under acceleration; Pin To Anchor locks position instead and overrides this spring. | `1200`; Minimum: 0 |
| `travel` | `float` | Maximum positional slack in metres around the pinned foot target when travel limiting is enabled. | `.035`; Minimum: .001f |

## PassengerGForceLimits

Live settings in the Passenger Seat **G-force limits** foldout. See [G-force limits](../Seats.md#g-force-limits) for detection, timing and controller exclusions.

| Setting | Type | Default and constraints | Description |
| --- | --- | --- | --- |
| `enabled` | `bool` | `true` | Enable transient protection for an occupied physical ragdoll. |
| `maximumJointSeparation` | `float` | `.025; minimum .001` | Maximum anatomical anchor separation while active, metres. Authored angular ranges are retained; soft limit springs are restored after protection. |
| `maximumRelativeAngularSpeed` | `float` | `360; minimum 1` | Maximum bone angular speed and rotation per physics step relative to the moving vehicle, based on the live pre-solve pose, degrees/second. |
| `maximumRelativeSpeed` | `float` | `3; minimum .1` | Maximum dynamic bone speed relative to the local vehicle point velocity, m/s. |
| `maximumSeatDisplacement` | `float` | `.15; minimum .01` | Maximum pelvis displacement from the seated spine origin while active, metres. |
| `minimumForce` | `float` | `0; minimum 0` | Optional minimum passenger inertial load in N, not vehicle contact force. Zero disables this additional test. |
| `minimumGForce` | `float` | `8; minimum 1` | Minimum gravity-compensated seat acceleration in standard G. |
| `minimumVelocityChange` | `float` | `1; minimum 0` | Minimum gravity-compensated change of seat velocity per physics step, m/s. |
| `monitorAfterPhysics` | `bool` | `true` | Observe overloads immediately after every physics solve, including wheel/suspension impulses without a body collision callback. Disable to retain pre-solve and collision-only detection; already active protection is still enforced after physics. |
| `protectConstraintFailure` | `bool` | `true` | Independently contain gross ragdoll failure above twice the relative speed limits or 125% of seat displacement; does not require a G/force spike. Main Enabled still applies. |
| `protectionTime` | `float` | `.15; minimum 0` | Minimum hold after an overload, at least one physics step; extended until relative bone motion settles. |

## PassengerHandConfig

Configuration/implementation type for passenger hand config within physical passengers and limb configuration.

**Source:** `Runtime/World/Passengers/Seats/PassengerBodyPartConfig.cs`. Nested configuration data; expand its owning field in the Inspector.

**Inherited settings:** [PassengerBodyPartConfig](World.md#passengerbodypartconfig). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `alignRestRotation` | `bool` | Let the physical resting wrist follow its anchor rotation with a bounded angular spring. Uses the calibrated palm frame when a HandGrip is present, otherwise the wrist frame. Reapply seated tuning after enabling; anchor rotation then updates live. | `false` |
| `animateThumb` | `bool` | Allow grip solvers to pose the thumb. Disable to keep its authored local pose across handle changes. | `true` |
| `damper` | `float` | Position damping for the basic held-hand support. Increase to reduce oscillation around the anchor; handle and relaxed-rest support can use separate damping. | `180`; Minimum: 0 |
| `freeArmDamper` | `float` | Damping of relative arm-joint rotation in Free mode. It reduces flailing without pulling the arm back toward an anchor or fixed pose. | `3`; Minimum: 0 |
| `freeArmMaximumDampingTorque` | `float` | Maximum damping torque in N·m on a free arm. Higher values resist rapid limb rotation more strongly while still allowing the arm to hang. | `15`; Minimum: 0 |
| `freeWristRotation` | `Vector3` | Reference wrist Euler rotation in degrees for the optional initialized free-arm pose. | `Zero-initialized Vector3` |
| `hold` | `bool` | Keeps a physical hand supported at its resolved target while in IKHandle mode. Turn off to remove that support; handle/grip and relaxed-rest settings determine the support style. | `true` |
| `limitRestTravel` | `bool` | Bound wrist distance from the rest anchor using a native joint limit. Disable for force-limited spring support only, allowing the hand to yield under larger loads. Reapply seated tuning after editing. | `true` |
| `maximumRestForce` | `float` | Maximum force in newtons holding a relaxed-rest wrist at its anchor. Lower values let impacts pull the hand away more easily. | `80`; Minimum: 0 |
| `maximumRestRotationTorque` | `float` | Maximum torque in N·m for relaxed-rest wrist alignment. Lower values let the palm rotate more freely under load. | `8`; Minimum: 0 |
| `palmContact` | `bool` | HandGrip calibration identifying the palm contact and finger poses for this hand. Use it when the wrist bone's origin does not coincide with the palm touching the control. | `false` |
| `poseFreeArm` | `bool` | In Free mode, pose this arm toward its direct anchor once on entry, then let it hang. No car-to-hand support or angular position spring is created. Reapply seated tuning to change the initial pose. | `false` |
| `relaxedRest` | `bool` | Soft support around a direct hand anchor, with weaker arm pose motors and free wrist rotation. Reapply seated tuning after editing. Handles and palm grips retain their own support. | `false` |
| `restArmDamper` | `float` | Damping of shoulder/elbow movement in the relaxed-rest arm. Increase to reduce flailing without making the wrist grip rigid. | `1.5`; Minimum: 0 |
| `restArmMaximumTorque` | `float` | Torque cap in N·m for the relaxed arm's pose spring and damping. Increase only if the arm support should resist stronger disturbances. | `15`; Minimum: 0 |
| `restArmSpring` | `float` | Weak angular pose spring on the relaxed arm's joints. Increase to retain the initial shoulder/elbow pose more firmly while the wrist rests at its anchor. | `6`; Minimum: 0 |
| `restDamper` | `float` | Damping of wrist movement around the direct rest anchor in Relaxed Rest. Increase to reduce bouncing or vibration while keeping the support soft. | `24`; Minimum: 0 |
| `restRotationDamper` | `float` | Damping of wrist twisting around the relaxed-rest orientation. Increase to settle rotational wobble when rotation alignment is enabled. | `2`; Minimum: 0 |
| `restRotationSpring` | `float` | Spring aligning a relaxed-rest wrist to the anchor rotation when Rest Align Rotation is on. Increase for firmer palm orientation; position support is configured separately. | `12`; Minimum: 0 |
| `restSpring` | `float` | Spring pulling the wrist toward its direct rest anchor when Relaxed Rest is active. Increase for firmer support; it does not replace a VehicleHandle's grip spring. | `300`; Minimum: 0 |
| `restTravel` | `float` | Allowed wrist displacement in metres from the relaxed-rest anchor when Limit Rest Travel is enabled. A larger value lets the resting hand wander farther under load. | `.12`; Minimum: .01f |
| `spring` | `float` | Position spring for a held hand using the basic seat-anchor support. Increase for a firmer attachment; relaxed-rest and VehicleHandle grip paths have their own spring settings. | `2200`; Minimum: 0 |

## PassengerJointSupport

Serializable seat-owned support settings. Anatomical constraints remain active; these settings add forces rather than editing limits or creating another native joint.

**Source:** `Runtime/World/Passengers/Seats/PassengerJointSupport.cs`. Nested configuration data; expand its owning field in the Inspector.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `active` | `bool` | Apply this additional support while this seat has an active physical ragdoll occupant. | `true` |
| `anchor` | `Transform` | Target pose, normally an empty Transform under the vehicle. No target means no support. | `None / unassigned` |
| `damper` | `float` | Damping in N per m/s of relative point velocity. Resists oscillation while allowing the target to move with the vehicle. | `30`; Minimum: 0 |
| `holdRotation` | `bool` | Also align the joint body's orientation with the target. Leave off to hold only a point and retain anatomical angular freedom. | `false` |
| `jointId` | `string` | Exact, case-sensitive Joint ID from the occupant's Anatomical Joints list. One support per ID in this seat. | `None / unassigned` |
| `localOffset` | `Vector3` | Offset from the anatomical joint's anchor, in the joint body's local coordinates. Zero holds the joint pivot, for example the knee. | `Zero-initialized Vector3` |
| `maximumForce` | `float` | Maximum total position support force in N, including damping. Zero disables position support. | `300`; Minimum: 0 |
| `maximumTorque` | `float` | Maximum total rotation support torque in Nm. Zero disables angular support. | `40`; Minimum: 0 |
| `rotationDamper` | `float` | Angular damping in Nm per rad/s relative to the moving target. | `10`; Minimum: 0 |
| `rotationOffset` | `Vector3` | Desired joint-body rotation relative to the anchor, in degrees. Used only when Hold Rotation is enabled. | `Zero-initialized Vector3` |
| `rotationSpring` | `float` | Angular restoring torque in Nm per radian of orientation error. | `100`; Minimum: 0 |
| `spring` | `float` | Position restoring force in N per metre of error. Higher values pull the joint pivot toward the target more strongly. | `500`; Minimum: 0 |

## PassengerModule

Configuration/implementation type for passenger module within seats, bodies and controller strategies.

**Source:** `Runtime/World/Passengers/Core/PassengerModule.cs`. Abstract base; settings are inherited by derived components.

**Inherited settings:** [WorldModule](World.md#worldmodule). These settings also appear on this type.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

## PassengerRestraints

Stores harness, release, damping and ejection configuration.

**Source:** `Runtime/World/Passengers/Physics/PassengerRestraints.cs`. Nested configuration data; expand its owning field in the Inspector.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `chestSupportStrength` | `float` | Scales chest support independently of the pelvis. Reapply seated tuning or re-enter the seat after editing. One preserves the original support. | `1`; Range: .25f to 4 |
| `ejectionTiltDelay` | `float` | Time in seconds that the ejection tilt must be sustained before releasing the occupant. | `.1`; Minimum: 0 |
| `ejectPassengerOnCollision` | `bool` | Whole occupant release after a sufficiently strong new contact. | `false` |
| `ejectPassengerOnSpin` | `bool` | Whole occupant release after sustained roll/pitch tilt. | `true` |
| `enablePassengerEjection` | `bool` | Allow the whole occupant to detach from the seat into a free ragdoll. Removes every hand, foot, pelvis and chest restraint. Independent of the limb-only options above. | `false` |
| `harnessAngularDamper` | `float` | Mass-scaled damping resisting pelvis/chest rotation relative to the seated pose. Increase to reduce rocking without narrowing the allowed lean angles. | `3`; Minimum: 0 |
| `harnessAngularSpring` | `float` | Mass-scaled spring turning pelvis/chest back toward the captured seated orientation. Increase for a more upright, firmly held posture; reduce for freer torso movement. | `16`; Minimum: 0 |
| `harnessChestTravel` | `float` | Maximum chest displacement in metres from its support point when Limit Harness Travel is on. Increase to let the upper body sway farther independently of the pelvis. | `.06`; Minimum: .001f |
| `harnessDampingRatio` | `float` | Damping of the soft harness relative to its spring and supported mass. Around 1 settles without much bounce; lower values allow oscillation, higher values make the return more heavily damped. | `1`; Range: .5f to 1.5f |
| `harnessForwardLean` | `float` | Seat-relative forward/backward angular travel in degrees around the captured seated pose. | `22`; Range: 5 to 40 |
| `harnessFrequency` | `float` | Natural frequency in Hz used to calculate soft-harness positional springs from supported mass. Increase for quicker, firmer pelvis/chest support; decrease for softer, slower movement. | `3`; Range: 1 to 5 |
| `harnessLimitDamperPerKg` | `float` | Mass-scaled damping at the harness's angular travel stops. Increase to reduce bounce when the occupant reaches a lean/twist limit. | `6`; Minimum: 0 |
| `harnessLimitSpringPerKg` | `float` | Mass-scaled stiffness of the soft harness's angular travel stops. Increase to resist going beyond the lean/twist envelope more firmly. | `60`; Minimum: .1f |
| `harnessMaximumAcceleration` | `float` | Force cap for soft harness support expressed as m/s² and multiplied by the supported mass. Increase to hold the occupant through stronger acceleration; reduce to let the support yield. | `80`; Minimum: 5 |
| `harnessMaximumTorquePerKg` | `float` | Angular-support torque cap per kilogram of supported mass. Increase to let the soft harness hold torso orientation through stronger forces; this does not narrow the lean limits. | `8`; Minimum: 0 |
| `harnessSideLean` | `float` | Allowed side-to-side tilt in degrees around the captured seated pose. Increase to let the ragdoll lean sideways more before the soft limit pushes back. | `12`; Range: 5 to 30 |
| `harnessTwist` | `float` | Seat-relative twist travel in degrees around the captured seated pose. | `28`; Range: 5 to 45 |
| `limitHarnessTravel` | `bool` | Keep the pelvis inside Seat Travel and the chest inside Chest Travel using native joint limits. Angular sway stays physical. | `true` |
| `minimumEjectionAngle` | `float` | Gravity-relative tilt angle in degrees required for the spin/overturn ejection policy. | `90`; Range: 0 to 180 |
| `minimumEjectionCollisionForce` | `float` | Minimum average contact force in N: impulse divided by the physics timestep. | `20000`; Minimum: 0 |
| `minimumEjectionCollisionSpeed` | `float` | Minimum relative collision speed in m/s; force and speed thresholds must both be met. | `3`; Minimum: 0 |
| `minimumReleaseAngle` | `float` | Vehicle up angle from gravity up. 90 degrees means on its side; this detects roll/pitch, not ordinary yaw turns. | `90`; Range: 0 to 180 |
| `minimumReleaseCollisionForce` | `float` | Minimum average collision force in newtons (contact impulse divided by the physics timestep). Both force and speed thresholds must be met. | `20000`; Minimum: 0 |
| `minimumReleaseCollisionSpeed` | `float` | Minimum relative collision speed in m/s. Filters small support contacts even on heavy vehicles. | `3`; Minimum: 0 |
| `passengerEjectionVelocity` | `Vector3` | Optional additional velocity in vehicle-local m/s. Existing ragdoll linear/angular motion is preserved. | `Zero-initialized Vector3` |
| `releaseFeetOnCollision` | `bool` | Release pedal/rest pins after a sufficiently strong contact. | `false` |
| `releaseFeetOnSpin` | `bool` | Releases foot supports after sustained vehicle tilt beyond the configured angle. Enable to let the legs fall away during overturns; whole-passenger ejection has separate settings. | `false` |
| `releaseHandsOnCollision` | `bool` | Let arms fall after a sufficiently strong vehicle contact. | `false` |
| `releaseHandsOnSpin` | `bool` | Releases the hand supports after the vehicle remains beyond Minimum Release Angle for Release Tilt Delay. This reacts to roll/pitch tilt, not an ordinary horizontal turn. | `false` |
| `releaseTiltDelay` | `float` | Seconds continuously beyond the tilt angle before releasing limbs. | `.1`; Minimum: 0 |
| `reseatEjectedOnReset` | `bool` | Allows vehicle reset to restore an eligible occupant previously ejected from this seat. | `true` |
| `seatDamper` | `float` | Damping on pelvis movement in the regular seat-support path. Increase to reduce bouncing. Soft Harness uses Harness Damping Ratio instead. | `1300`; Minimum: 0 |
| `seatSpring` | `float` | Positional spring holding the pelvis to the seat in the regular support path. Higher values hold it more firmly; Soft Harness calculates its own mass-based spring from Harness Frequency instead. | `14000`; Minimum: 0 |
| `seatTravel` | `float` | Maximum pelvis displacement in metres from its seat support point when linear travel is limited. A smaller value keeps the hips closer to the saddle or seat. | `.025`; Minimum: .001f |
| `softHarness` | `bool` | Bounded native spring drives support pelvis and chest without bone pose overrides. Foot pins are configured separately on each foot. | `true` |
| `solverIterations` | `int` | Minimum solver iterations on seated bones only. Zero preserves the body's setting; higher authored values are retained. Restored on release. | `12`; Range: 0 to 255 |
| `solverVelocityIterations` | `int` | Minimum velocity solver iterations while seated; higher per-body settings are preserved. | `4`; Range: 0 to 255 |
| `torsoSwayDegrees` | `float` | Angular freedom in degrees around the seated torso pose in the regular support path. Increase for more body sway; Soft Harness uses its separate side, forward and twist limits. | `12`; Range: 0 to 35 |

## Passengers

Discovers owned handles and supplies input before seat work.

**Source:** `Runtime/World/Passengers/Core/Passengers.cs`. Component / asset.

**Inherited settings:** [WorldModule](World.md#worldmodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `spawnOnStart` | `bool` | Lets enabled seats create/adopt their starting occupants when the vehicle starts. Each seat must also have Spawn On Start enabled; turn this off to populate seats through gameplay code. | `true` |

## PassengerSeat

`Entered`, `Exited`, `ControllerChanged` and custom `ResetRequested`

**Source:** `Runtime/World/Passengers/Seats/PassengerSeat.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `attachmentDamper` | `float` | Damping for main Spring support without physical seat restraints. | `20`; minimum 0 |
| `attachmentMode` | `PassengerAttachmentMode` | Independent main attachment policy: Spring retains controller support; Parent holds the seating origin at Spine Anchor. Other ragdoll bones keep simulating. | `Spring` |
| `attachmentSpring` | `float` | Main Spring support strength for occupants without physical seat restraints; does not retune ragdoll restraints. | `120`; minimum 0 |
| `body` | `PassengerBody` ([fields](World.md#passengerbody)) | Optional pre-placed body. Leave empty to spawn the prefab. | `None / unassigned` |
| `bodyPrefab` | `PassengerBody` ([fields](World.md#passengerbody)) | Passenger prefab instantiated when this seat needs to spawn an occupant. It must contain the compatible PassengerBody implementation for the selected controller mode. | `None / unassigned` |
| `customTypeId` | `string` | Application-defined type for Custom occupants; avoids changing the enum. | `None / unassigned` |
| `enableSelfCollidersOnRelease` | `bool` | Enable self contacts for every Free limb, and for the whole mannequin when ejected. Individual limb settings can also enable contacts independently. Neighboring skeletal bodies keep collisions disabled. | `false` |
| `enableVehicleCollidersOnRelease` | `bool` | Enable vehicle contacts for every Free limb, and for the whole mannequin when ejected. Individual limb settings can also enable contacts independently. | `false` |
| `releaseColliders` | `Collider[]` | Selected cabin and door surfaces enabled for Free limbs and the ejected body. Held limbs ignore these contacts. | Empty |
| `ignoreReleaseCollidersAgainstWorld` | `bool` | Permanently ignore free release-surface solver contacts with the world, preserving released/ejected passenger contacts and managed parts. | `false` |
| `ignoreReleaseCollidersAgainstVehicle` | `bool` | Permanently ignore free release-surface solver contacts against other free vehicle colliders. Managed part collisions remain unchanged. | `false` |
| `excludeSelfCollisionsOnEnter` | `bool` | Exclude self contacts on entry and while held. Release options may restore them. Disable to keep self contacts enabled, including after regrip and reseating. Native joint collision settings still apply. | `true` |
| `excludeVehicleCollisionsOnEnter` | `bool` | Exclude contacts with the vehicle on entry and while held. Release options may restore them. Disable to keep vehicle contacts enabled, including after regrip and reseating. | `true` |
| `exitAnchor` | `Transform` | Seat-associated exit placement marker available to passenger exit/reset workflows. For animated boarding, configure the detailed outside placement and clearance on SeatAccess as well. | `None / unassigned` |
| `gForceLimits` | `PassengerGForceLimits` ([fields](World.md#passengergforcelimits)) | Emergency overload detector and transient containment. Ordinary ragdoll motion remains unmodified below the activation thresholds. | New settings; enabled |
| `headDamper` | `float` | Damping of the head's rotation relative to the vehicle, in N·m per rad/s. Increase to reduce nodding around the supported angle. | `20`; Minimum: 0 |
| `headPitch` | `float` | Head pitch relative to the seat's neutral forward pose, in degrees. Negative looks up; positive looks down. | `0`; Range: -60 to 60 |
| `headSpring` | `float` | Strength of the optional ragdoll head support in N·m per radian of angle error. Increase to hold the chosen pitch more firmly; the neck's anatomical limits still apply. | `250`; Minimum: 0 |
| `holdHeadForward` | `bool` | Artificial spring support facing the seat's forward direction. Only affects an occupied, active Ragdoll Physics seat; stops on exit/ejection. | `false` |
| `jointSupports` | `List<PassengerJointSupport>` ([fields](World.md#passengerjointsupport)) | Optional extra position/rotation springs resolved by the seated occupant's Anatomical Joint IDs. Active only with a physical Ragdoll Physics occupant; empty by default. | `Empty list` |
| `leftFoot` | `PassengerFootConfig` ([fields](World.md#passengerfootconfig)) | Left foot's target, hold/pin and ankle alignment settings. Use them to place the foot on a pedal, peg or floor support. | `new PassengerFootConfig()` |
| `leftHand` | `PassengerHandConfig` ([fields](World.md#passengerhandconfig)) | Left hand's control mode, target/grip and physical support. Expand to choose whether it holds a control, rests softly, follows animation or hangs free. | `new PassengerHandConfig()` |
| `maximumHeadTorque` | `float` | Torque cap in N·m for artificial head support. A low cap lets the head yield under acceleration or impact even when Head Spring is high. | `80`; Minimum: 0 |
| `parentMakeKinematic` | `bool` | Parent mode makes only the held pelvis Rigidbody kinematic; other bones retain physics. | `true` |
| `parentPositionOffset` | `Vector3` | Parent-mode position offset in Spine Anchor local metres. | `Vector3.zero` |
| `parentRotationOffset` | `Vector3` | Parent-mode rotation offset in Spine Anchor local degrees. | `Vector3.zero` |
| `parentWhileSeated` | `bool` | Places the occupant under the seat hierarchy while attached. This changes transform ownership; physical ragdoll support still comes from the selected passenger controller and restraints. | `true` |
| `passengerController` | `PassengerControllerType` | Ragdoll Physics uses the package physics/IK. Animator leaves animation to application code. Animator + IK overlays configured limb handles on application animation without ragdoll. Attach Only parents and positions the occupant without posing it. Custom only records occupancy; application code owns spawning, hierarchy, pose, animation and physics. Options: `RagdollPhysics`, `Animator`, `AnimatorIK`, `AttachOnly`, `Custom`. | `PassengerControllerType.RagdollPhysics` |
| `passengerType` | `PassengerType` | Category assigned to the seat's occupant: humanoid driver, humanoid passenger or application-defined Custom. Use Custom Type ID for your own category; this does not itself select the physics controller. Options: `HumanoidDriver`, `HumanoidPassenger`, `Custom`. | `PassengerType.HumanoidPassenger` |
| `restraints` | `PassengerRestraints` ([fields](World.md#passengerrestraints)) | Pelvis/chest support, damping, release and ejection settings. Expand to configure each policy. | `new PassengerRestraints()` |
| `rightFoot` | `PassengerFootConfig` ([fields](World.md#passengerfootconfig)) | Right foot's target and physical support settings. Configure independently from the left foot for separate pedals or riding contacts. | `new PassengerFootConfig()` |
| `rightHand` | `PassengerHandConfig` ([fields](World.md#passengerhandconfig)) | Right hand's control mode, target/grip and support. Configure independently so one hand can hold the wheel while the other operates a lever. | `new PassengerHandConfig()` |
| `seatId` | `string` | Identifier used by application code to choose this seat. Use distinct values such as driver or rearLeft; it does not place the seat or automatically grant driver controls. | `"passenger"` |
| `showGizmos` | `bool` | Show this component's scene guides and editing handles. Does not change gameplay or physics. Expand **Gizmos** for independent visibility controls; see [Scene gizmo visibility](../Configuration.md#scene-gizmo-visibility) for the controls available on this component. | `true` |
| `spawnOnStart` | `bool` | Lets this seat spawn/adopt its starting occupant when the parent Passengers hub also allows startup spawning. Turn off for a seat that should begin empty. | `true` |
| `spineAnchor` | `Transform` | Pelvis / seated spine origin, facing forward, Y up. | `None / unassigned` |
| `transformSupports` | `List<PassengerTransformSupport>` | Independent Spring/Parent bone-to-anchor supports for any controller or physics state. Original hierarchy/local pose restore on release. Call RefreshTransformSupports after runtime edits; see [support settings](World.md#passengertransformsupport). | Empty list |

## PassengerTransformSupport

**Source:** `Runtime/World/Passengers/Seats/PassengerTransformSupport.cs`. Referenced configuration block; expand its owning field.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `active` | `bool` | Enable this support entry. | `true` |
| `anchor` | `Transform` | Vehicle target outside the occupant hierarchy. | Unassigned |
| `bodyTransform` | `Transform` | Occupant root/bone/child from a pre-placed Body or Body Prefab; prefab references resolve on the spawned occupant. | Unassigned |
| `damper` | `float` | Position support damping. | `20`; minimum 0 |
| `followAnchorRotation` | `bool` | Follow live anchor rotation. False retains target world rotation captured on attach/refresh, with Preserve World Pose and Rotation Offset applied. | `true` |
| `id` | `string` | Optional case-sensitive ID/label unique within this seat; empty permits transform-only lookup. | Unassigned |
| `makeKinematic` | `bool` | Parent only: temporarily make this transform Rigidbody kinematic, leaving other bones simulated. | `true` |
| `mode` | `PassengerAttachmentMode` | Parent holds this transform; Spring uses position/rotation support. | `Parent` |
| `positionOffset` | `Vector3` | Position offset in anchor-local metres. | `Vector3.zero` |
| `preserveWorldPose` | `bool` | Capture current world pose relative to the anchor instead of snapping; offsets apply afterwards. | `false` |
| `rotationDamper` | `float` | Rotation support damping. | `20`; minimum 0 |
| `rotationOffset` | `Vector3` | Rotation offset in anchor-local degrees. | `Vector3.zero` |
| `rotationSpring` | `float` | Rotation support spring strength. | `120`; minimum 0 |
| `spring` | `float` | Position support spring strength. | `120`; minimum 0 |

## PedalFootMode

**Source:** `Runtime/World/Passengers/IK/Handle/PedalHandle.cs`. Component configuration.

Configure inherited contact/pose settings on this component; visual motion belongs to its animator.

## PedalHandle

**Source:** `Runtime/World/Passengers/IK/Handle/PedalHandle.cs`. IK-only pedal contact. Press follows the moving contact; Rotation keeps the ankle fixed and aims the foot towards the pedal. Input and travel settings belong to PedalAnimator.

**Inherited settings:** `ControlHandle`.

| Setting | Type | Meaning |
| --- | --- | --- |
| `ankleAnchor` | `Transform` | Fixed ankle position and reference frame for Rotation. Local Z points towards the toes, X is the pitch axis. |
| `footMode` | `PedalFootMode` | Press (default) follows the pedal contact; Rotation pivots the foot at a fixed ankle. |

## RagdollCollisionHelper

Configuration/implementation type for ragdoll collision helper within physical passengers and limb configuration.

**Source:** `Runtime/World/Damage/RagdollCollisionHelper.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `disableJointProjection` | `bool` | Disables native joint projection on the activated ragdoll to avoid projection-driven impact corrections. | `true` |
| `maximumAngularSpeed` | `float` | Maximum bone angular speed in radians/second. | `18`; Minimum: .1f |
| `maximumBoneSpeed` | `float` | Free-flight bone speed cap in metres/second; moving contacts temporarily raise this budget. | `12`; Minimum: .1f |
| `maximumCarrySpeed` | `float` | Maximum retained carry speed after contact ends, plus 2 m/s slack. During contact, the budget permits the actual surface speed so the car cannot overtake a capped bone. Fades after release; never applies a force. | `18`; Minimum: 0 |
| `maximumContactVelocityChange` | `float` | Additional normal impulse budget beyond closing speed, in units of bone mass times this velocity change. | `4`; Minimum: .01f |
| `maximumDepenetrationSpeed` | `float` | Free-ragdoll overlap correction cap in metres/second. During a moving-body contact the cap is at least the surface speed, bounded at 12 m/s for this temporary increase; the upward launch cap still applies. | `3`; Minimum: .1f |
| `maximumUpwardSpeed` | `float` | Upward speed cap prevents launch impulses while allowing the body to climb a hood. | `5`; Minimum: .1f |
| `minimumImpactSpeed` | `float` | Minimum incoming normal speed of the contacting body and relative impact required to knock down a standing character. Idle animation touching a parked body is not an impact. | `.1`; Minimum: 0 |
| `ragdollCollisionDetection` | `CollisionDetectionMode` | Native collision detection mode used by the dynamic ragdoll. | `CollisionDetectionMode.ContinuousDynamic` |
| `useSpeculativeContacts` | `bool` | Speculative contacts while standing/animated. Dynamic ragdolls keep Ragdoll Collision Detection to avoid ghost contacts at rest and preserve vehicle panel sweeps. | `true` |
| `vehicleContactFriction` | `float` | Friction used for the helper's bounded contacts with external dynamic bodies. | `.45`; Range: 0 to 1 |
| `vehicleDamageScale` | `float` | Scales collision speed used for vehicle damage; normal environment collisions remain unchanged. | `.05`; Range: 0 to 1 |
| `vehicleResponse` | `float` | Inverse-mass/inertia response of the other dynamic body for this contact only. Zero makes the contact one-way. | `0`; Range: 0 to 1 |

## RagdollCollisionRelay

Configuration/implementation type for ragdoll collision relay within physical passengers and limb configuration.

**Source:** `Runtime/World/Damage/RagdollCollisionRelay.cs`. Component / asset.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

## Rocket

Owns launched-rocket motor, collision and lifetime behavior.

**Source:** `Runtime/World/Weapons/Rocket.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `acceleration` | `float` | Motor acceleration in m/s² along the captured launch direction while the motor is burning. Increase for faster speed buildup; Burn Seconds sets how long thrust lasts. | `80`; Minimum: 0 |
| `applyExplosionForce` | `bool` | Apply explosion impulse to rigidbodies. Effects and Exploded notification are independent. | `true` |
| `burnSeconds` | `float` | Seconds the rocket motor produces thrust after launch. Zero disables the powered burn; a longer burn keeps accelerating the rocket for longer. | `3`; Minimum: 0 |
| `detonateOnCollision` | `bool` | Automatically detonate on contact. Explicit Detonate calls remain available. | `true` |
| `engineLoop` | `AudioClip` | Continuous motor recording played on the launched rocket during its powered burn. It follows the rocket rather than staying at the launcher. | `None / unassigned` |
| `exhaustAnchor` | `Transform` | Engine nozzle: local +Z points out of the exhaust. Optional; defaults to the launch direction reversed. | `None / unassigned` |
| `exhaustPrefab` | `ParticleSystem` | Particle effect attached to the launched rocket for motor exhaust. It follows the rocket while the motor burns. | `None / unassigned` |
| `explosionImpulse` | `float` | Explosion impulse passed to nearby rigidbodies, in N·s. Higher values throw objects harder; distance within Explosion Radius affects the applied impulse. | `80000`; Minimum: 0 |
| `explosionMask` | `LayerMask` | Layers eligible for this rocket's blast overlap query. | `~0` |
| `explosionPrefab` | `ParticleSystem` | Particle effect spawned at detonation. This controls the visible blast; physical blast impulse and radius are configured separately. | `None / unassigned` |
| `explosionRadius` | `float` | Blast radius in metres used to find nearby rigidbodies when explosion force is enabled. Increase to affect a wider area around detonation. | `12`; Minimum: 0 |
| `explosionSound` | `AudioClip` | One-shot played at the rocket's detonation point. It accompanies the explosion effect and remains separate from physical blast force. | `None / unassigned` |
| `explosionUpwardModifier` | `float` | Downward shift in metres of the effective blast origin used for force direction. Larger values make the explosion throw objects upward more strongly; the visual explosion remains at the hit point. | `.5`; Minimum: 0 |
| `inheritVehicleVelocity` | `bool` | Adds the launch point's vehicle velocity to the rocket's launch velocity. Enable so a rocket fired from a moving/rotating vehicle starts with that motion. | `true` |
| `launchDirection` | `Transform` | Optional transform whose forward axis aims the rocket at launch. If empty, the rocket object's own forward axis is used. | `None / unassigned` |
| `launchSound` | `AudioClip` | One-shot played when the rocket launches. Use it for the initial ignition or launch blast, separately from the sustained motor loop. | `None / unassigned` |
| `launchSpeed` | `float` | Initial forward launch speed in metres per second, before any inherited vehicle velocity. | `65`; Minimum: 0 |
| `lifetime` | `float` | Maximum seconds a launched rocket can remain in the scene. It is removed after this time even if it has not hit anything, preventing missed rockets from accumulating. | `12`; Minimum: .1f |
| `mass` | `float` | Rigidbody mass in kilograms of the launched rocket. It affects collision and impulse response; motor acceleration is configured separately. | `35`; Minimum: .01f |
| `useGravity` | `bool` | Enables gravity on the launched rocket's Rigidbody. Turn off for a rocket that should not drop under gravity after motor burnout. | `true` |


### Audio Settings groups

| Field | Type | Behavior |
| --- | --- | --- |
| `audioSettings` | `VehicleAudioSettings` | Reusable [VehicleAudioSettings](Effects.md#vehicleaudiosettings) for this sound or mix stage; expand the group in the Inspector to configure playback and emitter routing. |
| `explosionAudioSettings` | `VehicleAudioSettings` | Reusable [VehicleAudioSettings](Effects.md#vehicleaudiosettings) for this sound or mix stage; expand the group in the Inspector to configure playback and emitter routing. |
| `launchAudioSettings` | `VehicleAudioSettings` | Reusable [VehicleAudioSettings](Effects.md#vehicleaudiosettings) for this sound or mix stage; expand the group in the Inspector to configure playback and emitter routing. |

## RocketLauncher

Selects and launches configured mounted rocket stores.

**Source:** `Runtime/World/Weapons/RocketLauncher.cs`. Component / asset.

**Inherited settings:** [WorldModule](World.md#worldmodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `automatic` | `bool` | Repeats firing while the firing request remains active; otherwise uses discrete launch requests. | `false` |
| `fireInterval` | `float` | Minimum seconds between rocket launches. Increase for a slower salvo; decrease to launch the remaining rockets more rapidly. | `.4`; Minimum: 0 |
| `firingEnabled` | `bool` | Allows this launcher to accept fire requests. Turn off to keep the rockets mounted and stop held-trigger firing. | `true` |
| `rockets` | `Rocket[]` ([fields](World.md#rocket)) | Mounted rockets available for launch, checked in list order. Fired or unavailable entries are skipped; each Rocket supplies its own motor and explosion settings. | `Empty list` |

## RotaryHandle

**Source:** `Runtime/World/Passengers/IK/Handle/RotaryHandle.cs`. IK palm contact for a rotary knob or hand lever. Inherits ControlHandle. Set its anchor on the moving grip; configure value and motion on the animator.

**Inherited settings:** `ControlHandle`.

Configure inherited contact/pose settings on this component; visual motion belongs to its animator.

## SeatAccess

Describes the seat endpoint, outside marker, door and admission settings.

**Source:** `Runtime/World/Passengers/Access/SeatAccess.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `animationProfile` | `AccessAnimationProfile` ([fields](World.md#accessanimationprofile)) | Boarding animation calibration for this seat. Use it to select clips, state names and placement adaptation suitable for this cabin and approach side. | `None / unassigned` |
| `clearanceHeight` | `float` | Height in metres of the exit-clearance capsule. Match it to the standing character so a low ceiling can block an unsafe exit. | `1.7`; Minimum: .5f |
| `clearanceMask` | `LayerMask` | Layers tested when checking whether access space is blocked. | `~0` |
| `clearanceRadius` | `float` | Radius in metres of the standing-space capsule checked at the exit point. Increase to reserve more sideways space around the exiting character. | `.25`; Minimum: .1f |
| `closedDoorTolerance` | `float` | Allowed angle difference in degrees from fully closed when checking door completion. A small tolerance avoids waiting forever for a physical hinge to settle exactly at zero. | `3`; Range: 0 to 180 |
| `door` | `VehicleBodyPart` ([fields](Exterior.md#vehiclebodypart)) | Optional door opened before entry/exit and checked against its target angle. Leave empty for an open vehicle with no door to wait for. | `None / unassigned` |
| `doorTimeout` | `float` | Maximum time in seconds allowed for the door to reach the required access position. | `2`; Minimum: .1f |
| `doorway` | `Transform` | Optional intermediate doorway marker for adapting the path between the outside position and the seated pose. Place it in the opening the character should pass through. | `None / unassigned` |
| `duration` | `float` | Fallback access duration in seconds for the seat's entry/exit sequence. The assigned access-motion implementation may use calibrated clip timing instead. | `1.6`; Minimum: .1f |
| `groundProbeDistance` | `float` | Length in metres of the downward ray used to ground the outside position. It must reach from the raised probe origin to the expected terrain. | `5`; Minimum: .1f |
| `groundProbeHeight` | `float` | Height in metres above the outside point at which the downward ground ray starts. Increase when terrain beside the vehicle can lie above that point. | `2`; Minimum: .1f |
| `interactionDistance` | `float` | Maximum character-to-outside-point distance in metres for starting entry. Increase to allow boarding from farther away; exit still checks its own free-space conditions. | `2`; Minimum: .1f |
| `maximumAngularSpeed` | `float` | Maximum vehicle angular speed in radians per second during entry/exit. | `.5`; Minimum: 0 |
| `maximumGroundDrop` | `float` | Largest permitted downward projection from the authored outside point, in metres. | `2`; Minimum: 0 |
| `maximumGroundRise` | `float` | Largest permitted upward projection from the authored outside point, in metres. | `.5`; Minimum: 0 |
| `maximumSpeed` | `float` | Maximum vehicle point speed in m/s during entry/exit. | `.5`; Speed field; stored in m/s, displayed in the selected speed unit |
| `minimumGroundNormal` | `float` | Minimum upward ground normal for outside placement; 0.5 accepts slopes up to 60 degrees. | `.5`; Range: 0 to 1 |
| `openDoorAnimationProfile` | `AccessAnimationProfile` ([fields](World.md#accessanimationprofile)) | Optional profile for a door already open at admission. Falls back to Animation Profile. The door remains open and clips need no door events. | `None / unassigned` |
| `openDoorTolerance` | `float` | Allowed angle difference in degrees from the door's fully open angle before access may proceed. Increase to let boarding begin before the door reaches its exact stop. | `8`; Range: 0 to 180 |
| `outside` | `Transform` | Feet-level endpoint. Runtime never moves this transform. | `None / unassigned` |
| `outsideGroundClearance` | `float` | Height in metres added above the sampled ground for the outside standing point. A small positive value keeps the character from starting inside the floor. | `.02`; Minimum: 0 |
| `projectOutsideToGround` | `bool` | Projects the outside access pose onto acceptable ground using the configured ground probe. | `true` |
| `seat` | `PassengerSeat` ([fields](World.md#passengerseat)) | Seat reached through this access route. It supplies the occupant, seated anchor and eligibility checks; if empty, the component looks on the same GameObject. | `None / unassigned` |
| `showGizmos` | `bool` | Show this component's scene guides and editing handles. Does not change gameplay or physics. Expand **Gizmos** for independent visibility controls; see [Scene gizmo visibility](../Configuration.md#scene-gizmo-visibility) for the controls available on this component. | `true` |
| `side` | `AccessSide` | Descriptive side label; the assigned profile selects the actual clips and triggers. Options: `Left`, `Right`, `Custom`. | `Left` |
| `standingOffset` | `Vector3` | Optional offset from Outside in this seat's local axes. | `Zero-initialized Vector3` |
| `useOutsideRotation` | `bool` | Uses Outside's orientation when aligning the character beside the vehicle. Turn off when the access motion should derive its approach orientation without this authored rotation. | `true` |

## SteeringHandRegrip

Coordinates steering contacts, availability and external reservations.

**Source:** `Runtime/World/Passengers/IK/Regrip/SteeringHandRegrip.cs`. Component / asset.

**Inherited settings:** [PassengerBehaviour](World.md#passengerbehaviour). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `surface` | `SteeringWheelHandle` ([fields](World.md#steeringwheelhandle)) | SteeringWheelHandle describing the rim and palm contacts to regrip. It must describe the same wheel transform animated by Wheel Animator. | `None / unassigned` |
| `wheelAnimator` | `SteeringWheelAnimator` ([fields](Interior.md#steeringwheelanimator)) | Animator supplying the wheel's actual displayed angle and steering demand. These values decide when a hand must release and catch a new part of the rim. | `None / unassigned` |

## SteeringHandRegripSettings

Configuration/implementation type for steering hand regrip settings within grip fitting and steering ownership.

**Source:** `Runtime/World/Passengers/IK/Regrip/SteeringHandRegripSettings.cs`. Nested configuration data; expand its owning field in the Inspector.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `guideAdjustmentSpeed` | `float` | Maximum guide grasp adjustment along the rim, in degrees per second. Wheel-following itself is never filtered. | `240`; Minimum: 30 |
| `leftRestAngle` | `float` | Lower rim angles for the relaxed thumb/index support; measured in the unturned wheel plane. | `250` |
| `minimumHandSeparation` | `float` | Minimum angular spacing in degrees kept between hand contacts around the rim. | `75`; Range: 0 to 180 |
| `palmReturnTime` | `float` | Minimum time for a full palm-pressure-to-wrapped-grip blend while the released wheel unwinds. | `.35`; Minimum: .1f |
| `reachAdjustment` | `float` | Search around each preferred angle for a reachable wrist pose. | `20`; Range: 0 to 35 |
| `reachMargin` | `float` | Safety margin subtracted from the hand's measured arm reach, in metres. | `.012`; Minimum: 0 |
| `rightRestAngle` | `float` | Right hand's preferred resting position around the rim, in degrees. The regrip planner uses it when returning that hand to its normal grip. | `290` |

## SteeringWheelHandle

Describes steering contacts, surface geometry and hand participation.

**Source:** `Runtime/World/Passengers/IK/Handle/SteeringWheelHandle.cs`. Component / asset.

**Inherited settings:** [VehicleHandle](World.md#vehiclehandle). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `allowHandRegrip` | `bool` | Allow automatic hand repositioning and column support while steering. Disable for fixed handlebar grips. | `true` |
| `authoredTargets` | `bool` | Keep manually authored palm anchors instead of regenerating wheel-rim contacts. Use for control sticks. | `false` |
| `center` | `Vector3` | Steering-wheel rim centre in the handle's local space. | `Zero-initialized Vector3` |
| `customRim` | `RimSample[]` ([fields](World.md#steeringwheelhandlerimsample)) | Optional closed centerline for flat-bottomed or irregular wheels. At least three samples. | `Empty list` |
| `gripMode` | `SteeringGripMode` | Chooses which hands may use this wheel: both, only left, only right, or neither. Released removes wheel targets without disabling the steering-wheel visual. Options: `BothHands`, `LeftHand`, `RightHand`, `Released`. | `SteeringGripMode.BothHands` |
| `leftAngle` | `float` | Left hand's contact angle around the wheel rim in degrees. Adjust to choose where that hand initially holds the wheel; regripping can move it during play. | `180`; Range: 0 to 360 |
| `leftTarget` | `Transform` | Transform updated to the calculated left palm contact pose. One is created when empty; the passenger's left hand can use it as its reach target. | `None / unassigned` |
| `pinchHandPosition` | `int` | Hand Positions entry used for the thumb/index pinch. | `2`; Minimum: 0 |
| `pressureHandPosition` | `int` | Hand Positions entry used for palm pressure, blended by the steering policy. | `1`; Minimum: 0 |
| `regrip` | `SteeringHandRegripSettings` ([fields](World.md#steeringhandregripsettings)) | Timing and contact rules for lifting and repositioning hands during large steering-wheel turns. Expand to tune when each hand lets go and catches the rim again. | `new SteeringHandRegripSettings()` |
| `reverseApproach` | `bool` | The wheel-local direction away from the driver is +Z. Reverse for a backwards pivot. | `false` |
| `rightAngle` | `float` | Right hand's contact angle around the wheel rim in degrees. Set independently from Left Angle for a natural two-hand starting grip. | `0`; Range: 0 to 360 |
| `rightTarget` | `Transform` | Transform updated to the calculated right palm contact pose. One is created when empty; the passenger's right hand uses it when the grip mode permits. | `None / unassigned` |
| `rimRadius` | `float` | Distance in metres from the wheel centre to the centre of its rim tube. Match the visible rim so generated palm and finger contacts lie on it. | `.1744`; Minimum: .02f |
| `showFingerContacts` | `bool` | Draws finger contact guides in the Scene view for grip calibration. Turning it off hides these guides without disabling finger fitting. | `true` |
| `stickGrip` | `bool` | Fit fingers and thumb around Grip Diameter at the authored palm anchors. | `false` |
| `tubeDepthRadius` | `float` | Fore/aft tube radius. Zero uses a circular section equal to Tube Radius. | `0`; Minimum: 0 |
| `tubeRadius` | `float` | Radius of the rim tube, not its diameter. | `.016`; Minimum: .002f |
| `useAnchorStartPosition` | `bool` | Use assigned anchors as starting and return grips while allowing regrip. Preserves position and rotation offsets, skips reach adjustment, and takes precedence over Authored Targets. | `false` |
| `varyGripWithSteering` | `bool` | Select or blend the saved pressure/pinch poses while steering; no runtime closure factor is applied. | `true` |

## SteeringWheelHandle.RimSample

Value data for rim sample; its fields are listed below.

**Source:** `Runtime/World/Passengers/IK/Handle/SteeringWheelHandle.cs`. Nested configuration data; expand its owning field in the Inspector.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `position` | `Vector3` | Point on the custom rim centreline in the steering-wheel transform's local coordinates. Order the points around the rim; the closed path replaces the normal circular rim. | `Zero-initialized Vector3` |
| `radius` | `float` | Rim tube radius in metres at this custom centreline point. It controls the thickness fingers fit around; it is separate from the overall steering-wheel radius. | `0`; Minimum: .001f |

## SwitchHandle

**Source:** `Runtime/World/Passengers/IK/Handle/SwitchHandle.cs`. IK-only hand contact for a switch. Inherits ControlHandle. Detents, events and motion belong to SwitchAnimator.

**Inherited settings:** `ControlHandle`.

Configure inherited contact/pose settings on this component; visual motion belongs to its animator.

## ThrottleHandle

**Source:** `Runtime/World/Passengers/IK/Handle/ThrottleHandle.cs`. IK-only contact for a throttle grip. Inherits ControlHandle; all geometry and value writes belong to ThrottleAnimator.

**Inherited settings:** `ControlHandle`.

Configure inherited contact/pose settings on this component; visual motion belongs to its animator.

## Trailer

Stores the towed-body connection and brake-following behavior.

**Source:** `Runtime/World/Towing/Trailer.cs`. Component / asset.

**Inherited settings:** [WorldModule](World.md#worldmodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `followHandbrake` | `bool` | Forward the towing vehicle's handbrake. Detached parking is controlled separately. | `true` |
| `followServiceBrake` | `bool` | Forward the towing vehicle's resolved service brake to this trailer. | `true` |
| `hitch` | `Transform` | World-space coupling point used to align the trailer connection. | `None / unassigned` |
| `parkWhenDetached` | `bool` | Applies the trailer's parking request while no towing vehicle is connected. Turn off if an uncoupled trailer should be free to roll. | `true` |
| `serviceBrakeMultiplier` | `float` | Multiplier for forwarded service braking; final demand is clamped to 0–1. | `1`; Minimum: 0 |

## VehicleHandle

**Source:** `Runtime/World/Passengers/IK/Handle/VehicleHandle.cs`. Component configuration.

**Inherited settings:** `MonoBehaviour`, `IHandle`.

| Setting | Type | Meaning |
| --- | --- | --- |
| `adaptiveGrip` | `bool` | Fit fingers around this handle. Applies to hands only; foot anchors are unaffected. |
| `allowedLimbs` | `HandleLimbs` | Flags selecting the hands/feet allowed to use this handle. |
| `angularDamper` | `float` | Damping for angular damper. Higher values oppose relative motion more strongly. Initial value: `20`. |
| `angularSpring` | `float` | Restoring stiffness for angular spring. Higher values resist displacement more strongly. Initial value: `500`. |
| `animationValue` | `Vector3` | Vector signal writable by animation/Timeline/application code. Its meaning and units belong to the application. |
| `defaultHandPosition` | `int` | Index of the normal grip configuration. |
| `fingerBlendDuration` | `float` | Seconds to blend displayed finger rotations from the previous handle to this handle after rebind. Default 0.12; zero opts out. Controller travel retains the current pose. Initial seating and editor previews apply immediately. |
| `gripDiameter` | `float` | Grip diameter in metres in the palm anchor's local space. The cylinder runs along anchor X, with its centre towards +Y from the palm contact. |
| `handPositions` | `HandleHandPosition[]` | Named local/shared configurations. Empty older data is initialized from type-specific defaults. |
| `id` | `string` | Unique, case-sensitive ID used by EngineAudio's runtime API. |
| `leftFootPose` | `HandlePoseSettings` | Independent left-foot pose, target and contact settings. Finger weight is unused for feet. |
| `leftHandPose` | `HandlePoseSettings` | Independent left-hand pose, target and contact settings. Weights default to one. |
| `maximumPalmForce` | `float` | Force/torque budget for maximum palm force; this limits or scales how strongly the mechanism changes physical motion. See the owning system guide for its application frame. Initial value: `90`. |
| `maximumTorque` | `float` | Force/torque budget for maximum torque; this limits or scales how strongly the mechanism changes physical motion. See the owning system guide for its application frame. Initial value: `25`. |
| `minimumAttachments` | `int` | Minimum other held limbs left on this source before borrowing one, evaluated separately for each seat. |
| `observeRotation` | `bool` | Observe local Euler degrees (true, default) or local position units (false). Euler values wrap at 360 degrees. |
| `onContactEnded` | `UnityEvent<HandleContactContext>` | Inspector-configurable counterpart of ContactEnded. Runs after the C# event for the same phase. |
| `onContactStarted` | `UnityEvent<HandleContactContext>` | Inspector-configurable counterpart of ContactStarted. Runs after the C# event for the same phase. |
| `onContactUpdated` | `UnityEvent<HandleContactContext>` | Inspector-configurable counterpart of ContactUpdated. Runs after the C# event for the same phase. |
| `onValueChangeStarted` | `UnityEvent<HandleValueContext>` | Inspector-configurable counterpart of ValueChangeStarted. Runs after the C# event for the same phase. |
| `onValueChangeStopped` | `UnityEvent<HandleValueContext>` | Inspector-configurable counterpart of ValueChangeStopped. Runs after the C# event for the same phase. |
| `onValueChanging` | `UnityEvent<HandleValueContext>` | Inspector-configurable counterpart of ValueChanging. Runs after the C# event for the same phase. |
| `positionDamper` | `float` | Damping for position damper. Higher values oppose relative motion more strongly. Initial value: `60`. |
| `positionSpring` | `float` | Restoring stiffness for position spring. Higher values resist displacement more strongly. Initial value: `2000`. |
| `rightFootPose` | `HandlePoseSettings` | Independent right-foot pose, target and contact settings. Finger weight is unused for feet. |
| `rightHandPose` | `HandlePoseSettings` | Independent right-hand pose, target and contact settings. Weights default to one. |
| `showGizmos` | `bool` | Shows this component’s scene guides and editing handles. Enabled by default; Inspector: **Gizmos > Show gizmos**. Does not change gameplay or physics. |
| `use` | `HandleUseSettings` | Automatic action policy and explicit/automatic transfer timing for this destination. |
| `useAnimationValue` | `bool` | Observe animationValue instead of the built-in/transform value source; default false. |
| `valueChangeThreshold` | `float` | Euclidean change threshold in source-value units, default 0.0001. Small changes accumulate against the last significant sample. |
| `valueStopDelay` | `float` | Seconds without significant change before automatic Stop; default 0.08. Explicit manual activity ends through EndValueChange. |
| `valueTransform` | `Transform` | Optional externally animated transform to observe when useAnimationValue is false; otherwise use the concrete handle source. |

## WaterInteraction

Connects vehicle water sampling and hull contact state.

**Source:** `Runtime/World/Water/WaterInteraction.cs`. Component / asset.

**Inherited settings:** [WorldModule](World.md#worldmodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `hullHalfSize` | `Vector2` | Half-width / half-length in metres, shared by water audio and particle contact points. | `new Vector2(1, 2.5)` |
| `useProfileFallback` | `bool` | Allow the Boat profile's flat water when no explicit provider is assigned. | `true` |
| `waterInteractionEnabled` | `bool` | Master switch for water interaction: buoyancy, water audio and water particles. | `true` |
| `waterProvider` | `WaterProvider` ([fields](World.md#waterprovider)) | Explicit source of water height and motion samples for this vehicle. Assign it to use a particular water body instead of automatic provider selection. | `None / unassigned` |

## WaterProvider

Abstract sampling adapter and `WaterSample` data contract.

**Source:** `Runtime/World/Water/WaterProvider.cs`. Abstract base; settings are inherited by derived components.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

## WaterStyle

Configuration/implementation type for water style within water sampling and movement.

**Source:** `Runtime/World/Water/WaterStyle.cs`. Component / asset.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `deepColor` | `Color` | Water colour used for deeper-looking areas. Its alpha also participates in the material's transparency; it changes appearance, not physical depth. | `new Color(.025, .15, .34, 1)` |
| `depthAbsorption` | `float` | Strength of depth-based water-color absorption. | `.3`; Minimum: .01f |
| `foamColor` | `Color` | Tint and transparency of surface/shoreline foam drawn by the water material. It does not change separate foam particle systems. | `new Color(.7, .88, .87, 1)` |
| `reflectionStrength` | `float` | Multiplier for the water material's reflection contribution. | `.8`; Range: 0 to 1 |
| `rippleScale` | `float` | Spatial scale passed to the water shader for its small surface ripple pattern. It changes the visible pattern rather than the sampled buoyancy wave height. | `.055`; Minimum: .001f |
| `rippleStrength` | `float` | Visible small-ripple contribution to the water surface. | `.13`; Range: 0 to 1 |
| `roughness` | `float` | Shader roughness controlling how sharp the water's reflected highlights appear. Increase for softer, duller reflections; decrease for a smoother, glossier surface. | `.34`; Range: 0 to 1 |
| `shallowColor` | `Color` | Water colour used where the depth shader sees nearby ground. Use a lighter or clearer colour to make shallow shore areas distinct. | `new Color(.065, .32, .52, 1)` |
| `shorelineFoam` | `float` | Amount of depth/shoreline foam produced by the water shader. | `.55`; Range: 0 to 1 |
| `waveA` | `Vector4` | Direction X/Z, wavelength in metres, amplitude in metres. Shared by CPU sampling and shader. | `new Vector4(.85, .52, 22, .09)` |
| `waveB` | `Vector4` | Second wave: X/Z direction in the first two components, wavelength in metres in Z, and amplitude in metres in W. | `new Vector4(-.4, .92, 11, .045)` |
| `waveSpeed` | `float` | Multiplier for wave phase speed shared by CPU surface sampling and shader animation. | `.65`; Minimum: 0 |

## WaterSurface

Built-in water-surface provider implementation.

**Source:** `Runtime/World/Water/WaterSurface.cs`. Component / asset.

**Inherited settings:** [WaterProvider](World.md#waterprovider). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `animateWaves` | `bool` | Enables time-varying wave height and normal instead of a flat surface. | `true` |
| `depthEffectsEnabled` | `bool` | Uses existing camera depth if available; no camera/depth/opaque passes are requested by this component. | `true` |
| `generateGrid` | `bool` | Generate a bounded grid for vertex waves. Disable to retain your authored mesh. | `true` |
| `gridCellSize` | `float` | Grid-cell size in metres for the generated water mesh; smaller cells create a denser mesh. | `5`; Minimum: .5f |
| `materialOverride` | `Material` | Explicit water material; leave empty to retain the material authored on the renderer. | `None / unassigned` |
| `reflectionsEnabled` | `bool` | Allows the material's reflection contribution. Turn off to remove that appearance while keeping water sampling, waves and the surface itself active. | `true` |
| `renderSurface` | `bool` | Shows the water mesh while Water Enabled is on. Turn off for invisible water that still supplies physical water samples. | `true` |
| `size` | `Vector2` | Water surface width and length in metres. | `new Vector2(400, 640)` |
| `style` | `WaterStyle` ([fields](World.md#waterstyle)) | Shared asset defining water colours, ripple appearance and other surface styling. Use it to keep several water surfaces visually consistent. | `None / unassigned` |
| `surfaceRenderer` | `MeshRenderer` | MeshRenderer used to display this water body's material. The component controls its visibility and material properties while active. | `None / unassigned` |
| `waterEnabled` | `bool` | Enables this water provider's sampling and visible surface. Turn off to make it unavailable to buoyancy/water-contact queries as well as hide its renderer. | `true` |

## WeaponBarrel

Owns muzzle aiming, trigger/cooldown admission and projectile initialization.

**Source:** `Runtime/World/Weapons/WeaponBarrel.cs`. Component / asset.

**Inherited settings:** [WorldModule](World.md#worldmodule). These settings also appear on this type.

| Setting | Type | Description | Declared default and constraints |
| --- | --- | --- | --- |
| `fireMode` | `WeaponFireMode` | Single fires on a new trigger press; Automatic continues requesting shots while the trigger is held, respecting the reload interval. Options: `Single`, `Automatic`. | `Single` |
| `firingEnabled` | `bool` | Allows projectile creation when the weapon is ready. Turn off to block fire requests without disabling its aiming mechanism. | `true` |
| `impactImpulse` | `float` | Impact impulse in N·s passed to each spawned projectile. The projectile uses it to push the Rigidbody it hits; it does not set muzzle velocity or recoil. | `20000`; Minimum: 0 |
| `inheritVehicleVelocity` | `bool` | Adds the vehicle's velocity at the muzzle to the shot's initial velocity. This keeps shots consistent when the vehicle is moving or turning. | `true` |
| `movement` | `MovingPart` ([fields](Exterior.md#movingpart)) | MovingPart used to aim/elevate this barrel. Rotation input and aiming requests are forwarded to it; firing still uses the Muzzle transform's actual pose. | `None / unassigned` |
| `muzzle` | `Transform` | Projectile spawn point and firing direction. Place it at the barrel exit with local forward pointing along the shot. | `None / unassigned` |
| `muzzleSpeed` | `float` | Initial projectile speed at the muzzle in metres per second. | `110`; Minimum: .1f |
| `projectileLifetime` | `float` | Maximum seconds a spawned projectile can remain alive without a hit. Increase for long-range shots; decrease to remove missed projectiles sooner. | `12`; Minimum: .01f |
| `projectilePrefab` | `MonoBehaviour` | A prefab component implementing IWeaponProjectile. Projectile behavior belongs to your game. | `None / unassigned` |
| `shotsPerSecond` | `float` | Maximum firing cadence in shots per second. | `.4`; Minimum: .01f |

## WorldModule

Configuration/implementation type for world module within module lifecycle and scheduling.

**Source:** `Runtime/World/Core/WorldModule.cs`. Abstract base; settings are inherited by derived components.

**Inherited settings:** [VehicleModule](Common.md#vehiclemodule). These settings also appear on this type.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

## YokeHandle

Describes steering contacts, surface geometry and hand participation.

**Source:** `Runtime/World/Passengers/IK/Handle/YokeHandle.cs`. Component / asset.

**Inherited settings:** [SteeringWheelHandle](World.md#steeringwheelhandle). These settings also appear on this type.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.
