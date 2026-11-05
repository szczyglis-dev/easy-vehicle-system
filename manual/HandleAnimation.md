# Custom handle animation and IK

Use the common settings on `VehicleHandle` to combine your Animator, animation layers, Timeline or scripts with package IK. Steering wheels, yokes, sticks, switches, throttles, pedals, motorcycle grips and target/transfer helpers inherit the same pose weights, target override and interaction signals. Existing handle geometry, switch commands and vehicle input keep their own responsibilities.

Start with a working [passenger/controller setup](Passengers.md#passenger-mode-tutorials) and [control](InteriorControls.md). For a timed gameplay action with automatic completion/cancellation, see [ControlInteraction](ControlInteractions.md). This guide covers the lower-level common tools and how to combine them.

## Inspector quick start: blend an authored target with IK

1. Fit the seat and assign its limb to an existing handle using [Handles](Handles.md#bind-a-limb-to-a-control). Use **Animator + IK** when animation and package limb solving should cooperate.
2. Select the handle's GameObject, expand the relevant hand/foot pose settings, and configure **Position**, **Rotation** and **Finger** weights for the result you want. A zero weight yields that part of the pose to the other owner.
3. Create/select an animated target Transform and assign **Target Override** when the clip/Timeline should supply the destination. Keep it in the correct moving control hierarchy and within reach of the seated character.
4. If your animation owns the visible control mesh, disable the handle's **Automatic Motion** instead of letting two writers rotate it. Add/configure **Handle Animator Binding** only for the authored contact/value/animation-event path described below; its runtime helper classes are not components to add.
5. Save the vehicle/character assets and preview in Play Mode. Test reaching, returning and interruption with one limb before extending to several controls. A custom character solver still needs an application adapter; Inspector weights do not create one.

## Code responsibilities and extension points

`VehicleHandle` is the scene-facing facade: it retains serialized settings, public methods, events and lifecycle hooks. Its runtime helpers are ordinary internal objects, owned by each handle; they require no extra scene components or configuration.

| Class | Responsibility |
| --- | --- |
| `VehicleHandle` and concrete handle subclasses | Configuration, native control input/value sources, contact geometry and public event publication. |
| `HandlePoseBinding` | Stable configured palm targets, saved hand-position offsets, final target overrides, adaptive IK binding and generated-target cleanup. |
| `HandleContactTracker` | Per-seat/occupant/limb contact state, automatic/manual sampling, hysteresis and release events. |
| `HandleValueTracker` | Value sampling history, movement thresholds, idle delay, manual begin/end and value-event transitions, independent of the value source. |
| `HandleAnimatorBinding` | Clip/Timeline fields and Animation Event entry points; applies pose settings, contact reports and custom values through the handle API. |
| `HandleAnimatorParameters` | Optional Animator parameter writes and parameter/controller cache. |
| `SteeringAnchorStarts` | Captures authored steering grip starts once per target and restores their offsets during rim regrip. |

For a new control, derive from the appropriate handle, implement its geometry/input and override `ReadInteractionValue()` for its native signal. For authored animation, use `HandleAnimatorBinding` or call the public pose/contact/value methods. Both paths share observation and pose settings; changing the value source does not replace the event state machine. Keep solver changes in the pose helpers and Animator output changes in the Animator adapter.

The handle samples values in `LateUpdate`; the binding applies at execution order 90, and the passenger pipeline owns solving/contact sampling. Disable clears contacts, ends a value change and resets sampling; destruction also disposes generated palm targets.

## Choose what owns each part

| Goal | Passenger setup | Handle settings |
| --- | --- | --- |
| Existing automatic hand/foot behavior | Ragdoll Physics or Animator + IK; selected limb uses IK Handle | Default weights 1; Automatic Motion on |
| Your Animator owns the whole character | Animator; selected limb can use Animator ownership | Position/Rotation/Finger weights 0 for any package pose path you also invoke; assign the handle for contact observation |
| Your clip/layer plus partial IK | Animator + IK; limb uses IK Handle | Animate Position/Rotation weights between 0 and 1 |
| Package arm follow, your finger animation | Animator + IK; limb uses IK Handle | Position/Rotation 1, Finger 0 |
| External animated target with package solving | Animator + IK; limb uses IK Handle | Set Target Override to an animated transform; choose weights independently |
| Your Animator/Timeline owns the control mesh | Any passenger mode | Automatic Motion off; anchors follow your animated mesh; observe Value Transform or Animation Value if needed |
| Custom character/IK framework | Custom or your own body adapter | Read final targets; use TrackContact/ReportContact and base events; apply weights in your own solver |

The seat's controller chooses the broad character ownership. Handle weights do not activate IK on a plain Animator seat: use Animator + IK or explicitly call your own solver. Extra [transform supports](Seats.md#main-attachment-and-rigid-transform-supports) still run independently and can override bones after the ordinary IK pass.

## Shared settings on every handle

Expand the desired **Left Hand Pose**, **Right Hand Pose**, **Left Foot Pose** or **Right Foot Pose** on the handle. Each has independent settings:

| Setting | Effect |
| --- | --- |
| Target Override | Optional final world-space IK target. Null returns to normal handle contact geometry and hand-position offsets. The override itself receives no extra hand-position offset. |
| Position Weight | 0 keeps incoming animated upper/lower limb rotations; 1 solves to the contact; intermediate values blend those rotations. |
| Rotation Weight | Independent wrist/ankle rotation blend; 0 retains its incoming local rotation under the blended arm/leg. Existing palm/foot rotation settings still decide whether a target rotation is requested. |
| Finger Weight | 0 leaves fingers to your animation; 1 applies package grip posing; intermediate values blend from the incoming pose. Feet ignore this field. |
| Physical Weight | Independent native physical **palm** support strength. Zero frees its positional lock and clears the palm support drives. It does not disable anatomical joints, physical arm motors, foot pins or separately configured transform supports. |
| Contact Source | Automatic geometry sampling, or explicit Manual reports from your application/clip. |
| Contact Distance / Release Distance | Entry/release distances in metres. The larger release distance provides hysteresis. |
| Contact Angle | Maximum contact-frame rotation difference; 180 degrees accepts any angle. |

Weights default to 1, contact detection defaults to Automatic, and target overrides default to empty. Existing scenes retain automatic behavior. Weights are live: `handle.SetPoseWeights(part, position, rotation, fingers)` and `GetPoseSettings(part).physicalWeight` take effect without reseating. `SetPoseTarget(part, target)` changes the final target.

Transform IK weights are evaluated by the non-physical humanoid solver. They are not a replacement for physical motor/constraint settings on an active ragdoll. Select the appropriate limb mode or release/tune its physical supports when handing a physical limb to a different strategy.

## Tutorial: keep automatic IK

1. Configure a seated humanoid with Animator + IK (or the prepared physical Ragdoll Physics path).
2. Set the desired seat limb to **IK Handle** and assign the handle.
3. Keep pose weights at 1 and Target Override empty. Keep Automatic Motion enabled on controls using package visual motion.
4. Fit the contacts using the ordinary [seat](Handles.md#bind-a-limb-to-a-control) and [grip](SteeringHandGrip.md) tools.
5. Test contact and control motion in Play Mode before adding custom animation. Contact events observe the resulting pose; they do not move the hand or generate a gameplay action by themselves.

## Tutorial: own animation with contact events

Use this when a reach/press clip should own the arm and fingers completely, while code still needs to know when the hand reaches a control.

1. Select **Passenger Controller → Animator**, supply your seated/reach animation and configure its transitions/layers.
2. Assign the destination handle to the desired seat hand even if that limb's mode is **Animator**. This assignment identifies which contact to observe; it does not enable IK on this controller.
3. Keep package pose weights at zero on that hand if you also invoke a package pose path elsewhere. Keep Finger Weight at zero for your finger clips. Physical Weight is separate and matters only if a native physical palm support exists.
4. Choose Automatic contact detection if the animation brings the mapped hand/palm frame within the configured distance/angle. If you use Palm Contact, prepare the hand's HandGrip contact frame; otherwise the mapped hand bone is sampled.
5. For exact clip timing instead, choose Manual and add a **Handle Animator Binding** on the GameObject receiving Animation Events. Assign Seat and Part; leave Handle empty to use the seat's current handle. With **Drive Pose Weights** on, set its three pose weights to zero too, or turn that option off for an observation/event-only binding.
6. Put `ContactEnter` on the actual contact frame and `ContactExit` when the hand leaves. These methods select Manual contact mode and report the current occupant's contact. Events are emitted in the subsequent contact sample.
7. Connect **On Contact Started / Updated / Ended** on the handle, or subscribe to the C# events. Filter their Seat/Passenger/Part when a handle serves several limbs/occupants.
8. Start an action from the contact only when your application has requested it. The example below arms a switch action once per request; incidental contact alone does not toggle the switch.

For a non-humanoid Custom body, register your own fingertip/palm transform with `TrackContact(seat, part, transform)`. Manual reports can operate without any contact transform. The seat limb must reference that handle and the seat must have an admitted occupant.

## Tutorial: blend a reach layer with IK

1. Start with a working **Animator + IK** passenger and a limb set to **IK Handle**.
2. Add **Handle Animator Binding** to a character helper. Assign Seat, Part and optionally an explicit Handle. An empty Handle follows the selected seat limb's current assignment during transfers.
3. Put the reach animation on an Animator layer with the Avatar Mask appropriate for that arm. Your Animator owns layer weights and transitions; the binding does not choose layers/states or create an Animator Controller.
4. Animate the binding's **Position Weight** from 0 during the authored reach to 1 as the hand settles onto the contact. Animate **Rotation Weight** separately if the wrist should align later. Keep **Finger Weight** at 0 for an authored finger gesture, or blend it toward 1 for a package grip.
5. Animate the component fields through clip curves/Timeline, call `SetIKWeight` / `SetFingerWeight` from Animation Events, or update them from application code. For two independently animated hands, use separate child helper objects so each component has its own animation path. Animation Events are delivered to components on the Animator's receiving GameObject; use an application relay when the binding is on another helper.
6. To follow a moving intermediate target instead of the native control contact, enable **Drive Target Override** and assign an animated transform. Its world pose is the final solver target. Clear it while Drive Target Override is enabled to restore the native target.
7. If the hand changes controls, request ownership through vehicle.handles.TryAcquire for an application-controlled target, or use [HandleController/ControlInteraction](ControlInteractions.md#example-reach-for-the-wiper-switch) for the built-in automatic transfer. Do not run two competing hand-transfer owners at the same time.
8. Test weights 0, intermediate and 1. Zero must preserve the clip pose; the middle should smoothly combine it with IK; 1 should reach the fitted target. Existing wheel HandDriven/HandSteering/regrip policies still apply. Disable the automatic regrip module when your strategy owns those gestures.

`ControlInteraction` **Animator** mode deliberately gives the hand to Animator ownership during its gesture; weighted package IK is then not run for that limb. For a sequential reach → authored gesture → IK return, use **IK then Animator** in [ControlInteraction](ControlInteractions.md#inspector-reach-with-ik-then-animate-a-switch-gesture); it also supports a physical seated ragdoll. For a continuously mixed animation/IK gesture, keep the limb in IK Handle mode and use your own sequence or the existing **Custom** interaction driver contract. Use one owner for the action's commit/completion/cancellation; do not wire a second toggle to contact if ControlInteraction.OnCommit already owns it.

## Tutorial: animate only the fingers

1. Keep the arm in **Animator + IK**, with the seat limb in IK Handle mode and Position/Rotation weights at the desired follow strengths.
2. Set that handle hand's **Finger Weight** to 0. The package leaves finger pose writes to your clip rather than forcing its adaptive/fixed grip pose.
3. Add the finger animation on your Animator, commonly with a hand/finger Avatar Mask. Start it with your own input, a contact event, a value-change event or an Animation Event relay.
4. Use ContactEnter/ContactExit for explicit fingertip timing, or assign the binding’s **Contact Transform** to a fingertip for geometric detection (or call TrackContact in your custom pipeline). Automatic humanoid tracking normally uses the mapped hand/palm; assign **Contact Transform** on HandleAnimatorBinding for a different frame.
5. Optionally blend Finger Weight back toward 1 after the press to recover the saved package grip. The arm/wrist weights remain independent.

## Tutorial: own the steering wheel or switch mesh

1. Put the desired VehicleHandle on the control as usual and set **Automatic Motion** off.
2. Animate the control mesh/pivot with your own Animator, Timeline or script. Keep its passenger contact anchors below the moving part when they should follow it.
3. On a wheel animated by **SteeringWheelAnimator**, place the handle on the same transform assigned as **Steering Wheel**. That animator honors the handle's Automatic Motion flag. If you put the handle elsewhere, disable/configure the separate visual writer yourself.
4. For authored wheel contacts, use **Authored Targets** and suitable targets; disable automatic hand regrip if your clip owns those movements. Target Override is also available for independently animated contact targets.
5. Switch, throttle, joystick and pedal helpers keep their native logical values/requests while refraining from their package mesh write. Coordinating hand/foot helpers can pause their automatic target travel; retain explicit ownership of selection/cancellation in your sequence.
6. To observe the actual custom mesh, assign **Value Transform**. Choose Observe Rotation for local Euler degrees, or disable it for local position units. To publish a normalized/custom signal instead, enable **Use Animation Value** and animate **Animation Value**, or call `SetAnimationValue` / the binding's `SetControlValue`.
7. Use **Value Change Started / Value Changing / Value Change Stopped** for animation/UI responses. A signal or mesh animation does not drive engine throttle, steering input or a switch command. Call the native control/mechanic API at your chosen commit frame.

## Events and timing

| Signal | Meaning |
| --- | --- |
| Contact Started | Not touching → touching for one tracked seat/occupant/limb |
| Contact Updated | Every contact sample while touching, including the start sample |
| Contact Ended | Contact lost, limb released/rebound, occupant exits or handle disables |
| Value Change Started | Significant sampled value movement begins, or BeginValueChange is called |
| Value Changing | A changed sample while activity is active; explicit manual activity also progresses at constant value |
| Value Change Stopped | Stable for Value Stop Delay, explicit EndValueChange, or handle shutdown |

Contact is a geometric/manual interaction signal, not a physics collision callback or proof of a closed finger grip. Position/rotation weights do not themselves imply contact. Automatic contact uses entry/release hysteresis; Manual uses the last report. A missing target/contact cannot pass automatic geometry detection, but Manual can still report a timed clip event.

Contacts are tracked separately per seat/limb and carry the original Passenger identity on release. Pose settings belong to the handle/part: occupants sharing the same handle and part share those settings. Use separate handle adapters/targets when their weights must differ. A binding writes settings while enabled and does not restore a previous writer's values when disabled; your strategy owns handover/restoration.

Normal order: application animation evaluates → HandleAnimatorBinding applies its fields at LateUpdate order 90 → HumanoidPassenger solves its ordinary IK at 100 → PassengerSeat applies independent transform supports and samples contact at 10000. Generic control values sample in handle LateUpdate (pedals advance their presentation first). The binding's Contact Bool output normally reads the previous late contact sample; contact events carry the new sample directly. Custom scripts with different execution order must coordinate their own final pose/sample.

For a manual graph/IK pipeline, disable **Automatic Seated IK**, evaluate your animation, call the binding's `Apply()`, then `HumanoidPassenger.SolveSeatedIK()`. If immediate contact results are needed there, register/update the chosen contact and call `SampleContact` after your final pose; avoid sampling again elsewhere for the same logical tick.

The first value sample establishes a silent baseline. **Value Change Threshold** compares against the last significant sample, so small movements accumulate. **Value Stop Delay** defaults to 0.08 seconds. Call `BeginValueChange` / `EndValueChange` for an explicit press/hold sequence, even when its reported value is constant. Started/Stopped are transitions; progress is per sample, not a coroutine completion percentage.

ControlHandle reads InteractionValue from its paired ControlAnimator. Switches, pedals, rotary controls, gear paddles and throttles report their displayed scalar in X; gear levers report the displayed gear in X. Steering contacts retain their geometric observation. Other/custom handles use Animation Value unless a Value Transform is assigned. Euler values wrap at 360 degrees; supply a continuous value when a multi-turn animation needs unwrapped angles.

Events are available as C# delegates and Inspector UnityEvents. Each phase invokes its C# event before the corresponding UnityEvent. Keep callbacks short, unsubscribe on teardown and avoid throwing from them; exceptions propagate. Concrete events such as SwitchAnimator.PositionReached still describe native detent arrival and remain separate from the common observed-value lifecycle.

## Example: commit a requested press on contact

Configure the seat hand to observe the switch and use Automatic contact or the binding's ContactEnter/ContactExit events. Call Arm from your input/gesture start. The first matching contact sample toggles once. Use this action owner instead of a second ControlInteraction.OnCommit toggle.

<!-- example: ContactCommittedSwitch.cs -->
```csharp
using UnityEngine;
using EasyVehicleSystem;

namespace VehicleDocumentationExamples
{
    public class ContactCommittedSwitch : MonoBehaviour
    {
        public SwitchHandle control;
        public SwitchAnimator switchAnimator;
        public PassengerSeat seat;
        public PassengerBodyPart hand = PassengerBodyPart.RightHand;
        private SwitchHandle subscribed;
        private PassengerBody requestedPassenger;
        private bool armed;

        private void OnEnable()
        {
            subscribed = control;
            if (!subscribed) return;
            subscribed.ContactStarted += OnContact;
            subscribed.ContactUpdated += OnContact;
        }

        private void OnDisable()
        {
            if (subscribed) {
                subscribed.ContactStarted -= OnContact;
                subscribed.ContactUpdated -= OnContact;
            }
            subscribed = null;
            CancelPress();
        }

        public void Arm()
        {
            requestedPassenger = seat ? seat.Occupant : null;
            armed = requestedPassenger && subscribed;
        }

        public void CancelPress() { armed = false; requestedPassenger = null; }

        private void OnContact(HandleContactContext context)
        {
            if (!armed || context.Seat != seat || context.Passenger != requestedPassenger ||
                context.Part != hand || !context.IsTouching) return;
            armed = false;
            if (switchAnimator) switchAnimator.Toggle();
        }
    }
}
```

## Extension and API

A custom handle inherits the settings/events automatically. Override protected `ReadInteractionValue` to expose its own signal, or use the common external signal/transform fields. If you override LateUpdate/OnDisable/OnDestroy, call the base lifecycle so sampling, cleanup and contact release remain active. A custom pose solver can read GetPoseSettings and GetHandAnchor without using the built-in humanoid solver.

See [VehicleHandle, settings, event contexts and binding API](API/Handles.md#vehiclehandle) and [the scripting method/event index](Scripting/Handles.md#complete-public-method-and-event-index). For character-layer ownership and initial setup, return to [passenger mode tutorials](Passengers.md#passenger-mode-tutorials).
