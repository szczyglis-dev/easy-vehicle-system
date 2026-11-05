# Handles

A **handle** defines where and how a passenger's hand or foot contacts a vehicle control. It supplies the target anchor, supported limbs and grip settings. The vehicle's handle controller coordinates temporary reaches and returns between these contacts.

An **Interior animator** moves the visible control: for example, a steering wheel, pedal, switch or gear lever. The handle positions the limb at that control; it does not replace the animator. A moving control normally uses both, with the handle's contact anchor attached to the animated part. A fixed hand rest can use a handle or a direct seat anchor without an animator.

> [!TIP]
> In the interior-control setup below, **animator** means an Easy Vehicle System component such as `SwitchAnimator`, `PedalAnimator` or `SteeringWheelAnimator`. It moves the vehicle control directly. It is separate from Unity's `Animator` component, which plays character/model animations through an Animator Controller. References to Unity's component or the seat's Animator mode are named explicitly.

Create and fit the occupant in [Seats](Seats.md), then bind the required limbs below. See [Interior controls](InteriorControls.md) for animator selection and [Hand grips](SteeringHandGrip.md) for finger fitting.

## Vehicle handle management

Each vehicle owns `vehicle.handles`, the registry and scheduler for all its handles. Put a unique **ID** at the top of each handle Inspector, then select **Allowed limbs** using the four checkboxes. IDs are case-sensitive and scoped to the nearest vehicle; duplicates are reported and cannot be resolved by ID.

The seat's configured handles remain the home destinations. On a temporary control, **Use limb on action** configures an explicit seat, preferred limb, optional fallback limbs, action source, priority and travel/return timing. **Minimum Attachments** protects controls that must retain support: normally one for a wheel/yoke and zero for pedals. By default, automatic actions wait for an existing request. **Interrupt Lower Priority** lets a strictly higher-priority handle interrupt a timed request on its limb, continuing from the current contact and retaining the original home destination. Persistent and Animator ownership remain protected; attachment limits still apply unless **Allow Unsupported Departure** is enabled on the requesting handle. This separate option permits borrowing the last supporting limb without cancelling requests on other limbs. The demo Car handbrake enables both options with Priority 10, so a left-hand paddle request does not block its right-hand reach. Use the same [public API](Scripting/Handles.md#runtime-handover) for future gear-change events and custom targets.

## Bind a limb to a control

1. **Create the control animator.** Add the appropriate Interior component, such as `SwitchAnimator`, `PedalAnimator` or `SteeringWheelAnimator`, to the control hierarchy. Assign its moving transform, motion axis/range and data source or mechanic binding. Preview the control's movement before adding the passenger contact.
2. **Add the matching handle.** For example, pair `SwitchAnimator` with `SwitchHandle` or `PedalAnimator` with `PedalHandle`. You can use **Tools → Interior → Control Pairs** to create and connect supported pairs, or add the components separately.
3. **Connect the pair.** On handles exposing an **Animator** field, assign the control animator there. Set the handle's **ID** and **Allowed limbs**. Other handle types use their own control/geometry references; follow the [component selection table](InteriorControls.md#component-selection).
4. **Place the contact target.** Create and assign the handle's hand/foot anchor or configure its generated grip geometry. A contact that follows the control belongs under its moving part; keep the neutral motion reference independent. Check position, orientation and reach from the fitted seat.
5. **Assign the home control on the seat.** In **VehicleController > Seats**, expand the desired hand or foot, choose **IK Handle** mode and assign the prepared handle to **Handle**. This is the limb's normal destination, such as a steering wheel or accelerator.
6. **Configure support and grip.** Set **Hold** and the relevant hand/foot options, then fit the palm/fingers or foot contact using the preview tools below.
7. **Test the complete flow.** Preview the seated pose, then test control motion and limb following in Play Mode, including release and return where applicable.

For a **temporary control**, such as a stalk, gear paddle or handbrake, keep the seat's home handle assigned. Configure **Use limb on action** on the temporary handle, selecting the seat, limb, action source and travel/return settings. The handle controller borrows the limb and returns it to its home control; do not replace the seat's home binding for every action.

A **fixed rest** does not need an animator. Use an `AnchorHandle`, or leave the seat's **Handle** empty and assign a direct **Anchor**.

When a Handle is assigned, the handle takes precedence over the direct Anchor. A disabled handle supplies no target; the direct Anchor is not an automatic fallback for that assigned handle. Clear Handle when switching to a direct anchor.

Use `SteeringWheelHandle`, `YokeHandle`, `JoystickHandle`, `ThrottleHandle`, `SwitchHandle`, `PedalHandle` or a fixed `AnchorHandle` according to the destination. InstrumentNeedle and RotaryAnimator are visual controllers; RotaryHandle is their optional passenger contact. The [control selection table](InteriorControls.md#component-selection) explains the model components; do not duplicate their motion setup on the seat.

## Choose limb ownership

| Mode | What owns the limb |
| --- | --- |
| IK Handle | Package target following; physical support also applies for a physical occupant when configured |
| Animator | Character animation owns the limb |
| Free | Target following and vehicle support are released for that limb |

Both hands and both feet are independent. For example, one hand can steer while the other rests on an armrest and both feet use fixed anchors. The seat's controller still determines whether these limbs are physical or animation/IK-driven; limb settings do not turn an Animator occupant into a ragdoll.

Change mode/handle/anchor through the [runtime handover contract](Scripting/Handles.md#runtime-handover). Avoid a second IK system or animation pass overwriting the same limb after the package has solved it. Damage release adds a runtime Free state without overwriting the configured mode; inspect effective/released state when diagnosing this.

## Temporarily force one limb to IK

Enable **Force IK** in a handle's use settings, or pass `forceIK: true` when acquiring it at runtime.
The request temporarily controls just its selected hand or foot, even when the seat uses **Animator**.
The seat controller and the saved limb mode stay unchanged; other limbs keep their animation.
The override lasts through return travel and is released on completion, cancellation, target disable or seat exit.
See the [runtime example](Scripting/Handles.md#temporary-ik-in-animator-seats).

## Hands: grips, rests and free arms

### A held control

Assign the control handle, enable **Hold** and choose palm-contact settings appropriate to the physical passenger. The handle supplies palm/arm support and geometry; the seat supplies the limb ownership. Physical spring/damper/force settings matter for a ragdoll, while nonphysical IK primarily follows the target pose.

**Animate Thumb** allows a compatible grip solver to pose the thumb. Disable it to retain its configured pose through handle changes. For contact orientation, finger mapping, grip diameter and preview tools, use [Fit hand grips](SteeringHandGrip.md).

### A compliant hand rest

For an armrest or lap target, leave Handle empty and assign a direct Anchor. Use IK Handle mode and Hold, enable **Relaxed Rest**, and leave **Palm Contact** off. This selects the weaker rest support rather than treating the surface as a firmly gripped handle.

**Rest Spring/Damper** and **Maximum Rest Force** determine how the wrist yields under load. **Limit Rest Travel** adds a bounded distance from the anchor; without it, support is force-limited only. Rest arm settings guide the upper/lower arm more softly. **Align Rest Rotation** optionally guides the resting wrist orientation with its own bounded angular support.

Reapply seated tuning after changing the rest configuration. After rotation support is enabled, the rest anchor's rotation can guide the wrist live. Rotating the target is preferable to forcing an unrelated bone rotation after solving.

### A freely hanging arm

Use Free mode when the arm should no longer be attached to the vehicle. For a deliberate initial hanging pose, leave Handle empty, assign the direct Anchor and enable **Pose Free Arm**. The arm is placed toward that target once on entry/reapply, then allowed to hang; it does not remain pinned there. Free-arm damping limits motion without adding a positional tether.

Automatic collision release is different from this deliberate initial pose: it releases the current limb without replacing its configured mode. For collision options, see [Seat collision and tilt response](Seats.md#collision-and-tilt-response).

## Fit a hand grip

Once the wrist can reach its target, continue with [Hand grips](SteeringHandGrip.md). That page owns rim/tube dimensions, palm calibration, adaptive fingers, motorcycle preparation and regrip. Keep seat-position changes separate from finger-fitting changes so you can identify which fixes the problem.

## Feet and pedal contacts

For a stationary footrest, assign a direct ankle Anchor or an `AnchorHandle`. For a pedal rotating the foot about a fixed ankle, choose **Rotation** on `PedalHandle` and configure its ankle pivot as described in [foot operation mode](InteriorControls.md#foot-operation-mode). The pedal contact then steers foot pitch rather than placing the ankle directly. For a moving pedal in the default **Press** mode, configure its visual motion in [Interior controls](InteriorControls.md#pedals-and-foot-movement), then parent its **Contact Anchor** beneath the moving pedal and assign that `PedalHandle` to the seat foot.

Place the target for the character's ankle/contact frame, not merely at the pedal mesh's geometric centre. Use IK Handle mode and **Hold**. First verify reach and orientation in preview, then choose support:

| Foot option | Physical behavior |
| --- | --- |
| Spring/damper support | Compliant translation toward the target |
| Limit Travel | Adds a bounded positional range around it |
| Pin To Anchor | Locks foot translation while Hold and IK Handle are active; overrides spring/travel translation tuning |
| Align Rotation | Adds angular guidance to the target; otherwise ankle rotation stays free |

Pinning requires a physical seated passenger. It does not change anatomical leg lengths or guarantee an unreachable target. Tune rotation spring/damper and maximum torque separately from positional support.

### Move one foot between accelerator and brake

Bind the seat foot directly to the accelerator `PedalHandle`. Set both pedals' Allowed limbs to Right foot. On the brake, enable **Use On Action**, assign the seat, select **RightFoot** and **Source: ServiceBrake**. The per-vehicle controller owns admission, travel and return to the accelerator.

Use **Threshold / Release Threshold** for brake hysteresis. Start with **Travel Duration: 0.18 s**, **Release Duration: 0**, **Return Delay: 0**, **Lift Height: 0.035 m**. A pedal may remain unsupported: keep Minimum Attachments at zero. The same settings work for a left foot or another control.

For ID access, explicit reaches, competing actions and cancellation, see [runtime handover](Scripting/Handles.md#runtime-handover).

## Temporary interactions and custom controls

A temporary reach should preserve and restore the ordinary limb binding. Follow [Timed control interactions](ControlInteractions.md) for `vehicle.handles`, action commitment, animation ownership and cancellation. Do not permanently reassign the seat's normal hand just to play one button-press gesture.

Derive from `VehicleHandle` for another contact type. Its target frame, contact availability and input timing are described in [Handle scripting](Scripting/Handles.md). For restraint calculations and release collision details, see [Passenger physics](Scripting/PassengerPhysics.md).

## Smooth return to a wheel contact

A temporary handle transfer saves the hand's current contact on the wheel material. Return travel follows that point as the wheel rotates, with reach sectors and **Minimum Hand Separation** constraining the destination. At arrival, steering continues from the contact reached by the transfer. Explicit cancellation or external release uses the normal contact-acquisition policy.

The physical palm follows the transit target during return. Displayed finger rotations blend toward the destination grip in both directions; **Finger Blend Duration** controls the transition and **Animate Thumb** determines whether the thumb participates. **Palm Return Time** separately controls steering regrip transitions.
