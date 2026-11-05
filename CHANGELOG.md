# Changelog

## 1.0.2

- Add a held spatial horn with a credited CC0 default clip and keyboard/gamepad bindings on the road demo fleet. Add a dedicated throttle, brake, clutch and parking-brake animators, motorcycle twist throttle/front-brake/clutch levers, and a Car parking-brake lever, with reversible Inspector preview.

- Let automatic low-RPM downshifts bypass minimum gear dwell and skip safe intermediate ratios, so rapid braking reaches first gear promptly instead of stepping through gears after stopping. Retain road-speed/RPM safety and sequential upshift dwell.

- Connect Car gear paddles to exclusive left/right hand contacts, with timed reaching, paddle-following grips and smooth returns through the central handle controller. Coalesce downshift gestures with a configurable 0.25-second quiet period, bypassed by 1/N/R.

- Debounce gear-lever downshifts with a configurable 0.75-second quiet period, bypassed for first gear, neutral and reverse; correct the Bus H-pattern so odd gears move forward and successive pairs move right from the driver.

- Add a Bus floor-mounted gear lever with signed per-gear poses, rotation/translation modes, live Inspector preview and gearbox-driven hand reaches through the central controller. Add timed reach-and-hold ownership for moving controls.

- Separate outbound and return handle travel durations; default to a fast 0.06-second reach and a slower 0.28-second return, including migrated demo actions.

- Blend actual displayed finger rotations across handle handovers, retain their pose during controller travel, restore transient solver-binding writes and resume interrupted transitions continuously. Expose per-handle Finger Blend Duration; speed up the Car stalk/profile-switch reaches.

- Centralize handle discovery and exclusive limb ownership in vehicle.handles, with per-vehicle IDs, allowed limbs, automatic action rules, minimum retained support, timed/persistent/Animator requests and safe cancellation. Migrate pedal sharing, landing-gear reaches, control interactions and the aiming example, plus demo prefabs and documentation. Remove standalone transfer/selection helpers and duplicate switch animation ticks.

- Keep skid marks, smoke and squeal active for locked braking wheels when native slip intermittently reports zero; infer braking slip from road-relative planar motion without bridging airborne contact gaps.

- Use bounded native live-inspector refresh requests, filter property-only module visibility notifications and remove temporary part-gizmo visibility arrays; add Editor profiler markers for inspector work.

- Reduce repeated module, telemetry and feedback reads; reject unrelated water-entry colliders and points outside the stock lake before full sampling while retaining per-step splash detection and immutable telemetry history.

- Avoid per-wheel contact-state dictionary allocations while retaining synchronized support data for physics worker threads.

- Enable demo rear-mirror components only for the selected vehicle in Interior camera mode through a demo-only selection policy; preserve channel settings and restore authored component states when the policy is disabled.

- Cache demo GUI keycap parsing, text metrics and unchanged readouts; skip unused IMGUI layout work and accelerate the flight horizon without changing panel appearance or input behavior.

- Reuse rear-mirror render requests and shader property IDs, skip unnecessary frustum calculations and unchanged camera writes while retaining mirror render quality and cadence.

- Render the aircraft attitude HUD with exact horizon spans, reuse unchanged images and avoid per-refresh digit allocations while retaining the existing refresh rate and telemetry events.

- Avoid temporary wheel/module enumerators, ragdoll limit arrays and empty telemetry wrappers during physics updates; reduce redundant demo water collider/hierarchy queries.

- Add VehicleController.IsMoving and default-on stationary ContactEnvelope probing every ten fixed steps, grouped in a collapsible optimization Inspector; reuse certified native box contacts to avoid an additional centre ray.

- Reduce redundant modular suspension geometry, wheel-pose queries and aircraft leg calculations without changing spring integration or update cadence.

- Cache passenger IK bone Transform references, skip unchanged native wheel outputs, and reuse the car dashboard texture while its displayed values are unchanged.

- Reduce ContactEnvelope probes on certified unobstructed box faces; default to sampling every two fixed steps (set 1 for full frequency), and invalidate cached support on vehicle teleport.

- Add context-bearing Before/After seat entry, exit and ejection hooks on seats and passenger cores, plus whole-sequence access hooks and cancellation context.

- Skip unchanged native wheel-friction and lamp-property writes while retaining external edits and runtime configuration changes.

- Reduce mesh dent CPU work and persistent GPU cost of dynamic damage buffers, redundant audio/joint updates and sleeping ragdoll work; reuse identical tire-centre probes without reducing sampling precision.
- Show the shared package version in the demo footer and vehicle Inspector.
- Allow modest mannequin hip turn and lateral movement.
- Add optional spring-based head support for ragdoll motorcycle riders.

## 1.0.0

First release.
