# Demo

Keep **Demo** selected when importing the package from **Package Manager → My Assets**. Open `Assets/Szczyglis/EasyVehicleSystem/Demo/Demo.unity`.

## Select a vehicle

| Key | Demo vehicle | Example systems |
| --- | --- | --- |
| F1 | Car | Rear-wheel drive, physical occupants, opening body parts, damage, windows, road/hover switching |
| F2 | Monster Truck | Large tires, all-wheel drive and modular suspension |
| F3 | Military 6×6 | Six wheel contacts and all-wheel drive |
| F4 | Bus | Rear drive, cabin controls and commercial audio |
| F5 | Tractor | Articulated Semi Trailer and independent trailer brakes |
| F6 | Motorcycle | Assisted balance and physical rider |
| F7 | Helicopter | Rotor spool, flight assistance and pilot controls |
| F8 | Airplane | Assisted flight, propeller and landing gear |
| F9 | Drone | Hover, tilting rotor mounts and RPM-driven rotors |
| 6 | Boat | Buoyancy, rudder/helm, water effects and physical driver |
| 7 | Tank | Tracked drive, turret and physical projectiles |
| 8 | Jet | Aerobatic flight, retractable gear, stores and cockpit gestures |
| 9 | Submarine | Underwater propulsion, depth hold and dive controls |
| F11 | Car (Animator, IK, ragdoll example) | Animated steering and cockpit gestures; compare Animator, Animator + IK and seated ragdoll |

Page Up / Page Down cycles through the vehicles.

## Common controls

| Control | Action |
| --- | --- |
| W / S, A / D | Ground driving, or profile-specific flight/water axes |
| Space | Ground handbrake or airplane wheel brakes |
| I | Selected engine ignition |
| F | Enter / exit the driver seat when stopped, where Seat Access is configured |
| R | Full reset: repair selected vehicle and restore its recorded spawn/passenger pose |
| Tab | Cycle Orbit, Interior, Cinematic, FREE PARENT and FREE LOOK cameras |
| Mouse / wheel | Camera look/orbit and zoom |
| Escape / click | Release / capture pointer |
| N | Day/night lighting |
| L / H | Headlights / high beams |
| J / K / V | Left indicator / right indicator / hazards |
| X | Wipers where installed |
| U | Driving assists |
| T, Q / E, numpad gear keys | Transmission mode, shifting and gear selection on ground vehicles |
| Left Shift | Ground-vehicle clutch |
| C (hold), gamepad east face button (B/Circle) | Horn on road vehicles |
| C | Tractor/trailer attachment |
| Backquote (~) | Show/hide vehicle and control hint panels |

## Vehicle controls

| Vehicle | Controls |
| --- | --- |
| Car | Enter: Nitro with automatic throttle; Left Ctrl: burnout launch (hold); B: next drive profile (drive/hover); O: opening body parts; F: entry/exit; Y: cycle aiming hand; left mouse: fire while aiming |
| Airplane / Jet | Shift/Ctrl: increase/decrease throttle; W/S: pitch; A/D: roll or taxi steering; Q/E: yaw; Space: wheel brakes; G: landing gear; Right Alt: Nitro; C: Burnout / propulsion boost (hold; automatic throttle) |
| Jet stores | Enter: launch rocket; M: drop payload |
| Hover | Shift/Ctrl: ascend/descend; Q/E: strafe; Enter: Nitro; C: propulsion boost (hold) |
| Helicopter | Shift/Ctrl: ascend/descend; use the displayed attitude/yaw bindings; Enter: Nitro; C: propulsion boost (hold with collective/pitch/roll demand) |
| Tank | Brackets: turret rotation; Insert/Delete: elevation; Enter: fire; Right Alt: Nitro; Left Ctrl: Burnout |
| Submarine | W/S: thrust; A/D: turn; Shift/Ctrl: ascend/dive; Q/Z: pitch; Space: brake; Enter: Nitro; C: propulsion boost (hold) |
| AI route examples | P: cycle Manual → AI (physics) → AI (direct) → Manual |
| Other powered vehicles / Motorboat | Enter: Nitro; Left Ctrl: Burnout (hold). Boats require immersion; Nitro and Burnout supply forward throttle automatically. Release Nitro to refill. |

Reset clears boost requests, retained flight throttle, engine output and wheel spin, then repairs retained damaged/detached parts and dents before restoring the vehicle pose. Use the common R reset key; there are no separate repair buttons/shortcuts. EVS Car’s front-left WheelPart has Damage Enabled off in both prefab and scene. Destroyed debris still needs application respawning.

## Cameras

Tab cycles **Orbit → Interior → Cinematic → Free Parent → Free Look**. Orbit and Interior use the selected vehicle's `Cameras` component and its explicitly assigned `OrbitCamera.anchor` and `InteriorCamera.anchor`. `DemoCameraRig` switches and explicitly activates the attached scene camera between these submodules; Cinematic follows its heading through the Demo-only `DemoCinematicCamera` submodule. Free Parent and Free Look are custom `CameraModule` examples included only in the Demo, selected through the same `Cameras` core. Free Parent moves relative to the vehicle and remembers a local pose per vehicle; Free Look moves in world space. See [custom camera setup](Cameras.md#custom-camera-submodules) for extending and activating a view.

Free-camera movement: numpad 8 forward, 2/5 backward, 4/6 sideways, 9/3 up/down. Arrow keys provide horizontal movement; Shift increases speed.

## Reuse the examples

The sample's Prefabs folder contains the example vehicle configurations. Scripts/Examples contains application integrations such as `LandingGearSwitch`, `AimingHandExample`, `DemoExternalControl` and `DemoDirectWaypointAI`.

See [Getting started](GettingStarted.md) to build a vehicle, [Scripting](Scripting.md) to integrate your game, and [Demo resources](DemoResources.md) for asset bindings and credits.

## Compare physical and direct AI

For road vehicles, press **P** repeatedly to cycle **Manual (physics) → AI (physics) → AI (direct) → Manual (physics)**. The controls panel title reports the active mode and its P hint shows the next transition. Each vehicle retains its selected AI mode when another vehicle is selected. The route examples support Wheeled, Motorcycle and Tracked profiles.

Both AI examples use the same approach checkpoints and driving loop from `DemoExternalControl`. `DemoWaypointAI` submits throttle, steering and brake commands to an `ExternalController`, leaving movement to vehicle physics. `DemoDirectWaypointAI` instead submits a world position and rotation each physics tick through `DirectController.SetPose`. The package animates wheel rotation and steering from that direct movement. Automatic direct steering moves smoothly toward the inferred angle and returns to centre at **Steering Speed** (road-wheel degrees per second) in the vehicle settings. This affects wheel and steering-wheel visuals, without changing the supplied chassis path. Explicit analog steering with Automatic Steering disabled follows the supplied value directly. The demo example does not write wheel forces or move the chassis Transform itself.

The direct example preserves the chassis height relative to the route when activated and follows checkpoint height differences. It follows a look-ahead point along the checkpoint segments using continuous path curvature, starts turning before corners, and maintains cruising speed through the loop instead of stopping at each checkpoint. Look-ahead grows with speed and uses at least twice Arrival Distance; Turn Speed limits heading change. It does not use suspension forces or collision response to choose its path, and it has no obstacle avoidance or terrain sampling: an obstructed route can pass through obstacles. Resetting the vehicle restarts route selection at its current pose. Returning to manual or physical AI restores normal Rigidbody ownership through the controller API.

To reuse the example, assign a vehicle, its DirectController, an ordered loop with at least two valid checkpoint Transforms, and optional approach points. Call `Begin()` when giving it ownership, then select its controller as the vehicle Input Source. Tune **Speed Kph**, **Acceleration**, **Turn Speed** and **Arrival Distance** on the example. With the demo selector, use `SetControlMode(vehicle, DemoControlMode.AIDirect)` or `CycleControlMode(vehicle)` so input ownership stays coordinated.

### Movable boxes

Both the five **Dynamic crate** objects and the separate nine-box **Crash stack** use Rigidbody **Continuous Dynamic** detection and **Interpolate** display through `DynamicObstacle`. The stack retains its authored 150 kg mass per box; the smaller crates retain 60 kg. No additional solver iterations or per-frame helper callbacks are enabled. These settings are included in both Demo and Samples scenes.

## Animator passenger example

Press **F11** to select **Car (Animator, IK, ragdoll example)**. Its prefab is **Demo/Prefabs/CarAnimator.prefab**; supporting clips, Animator Controller and mannequin prefab are in **Demo/Prefabs/CarAnimator**.

1. Start Play Mode and select F11. The driver starts in **Animator** mode: a blend tree supplies both hands' steering poses without live arm IK. The visible wheel uses an 80-degree full-lock range for these fixed-grip clips; tire steering remains unchanged.
2. Press **Escape** to release the mouse. Use **Passenger example** below the vehicle list on the left to press the left/right switches, wave or cancel a gesture. Clicking inside the panel keeps the pointer available.
3. Compare **Animator + IK** for an IK reach, animated finger press and IK return, or **Ragdoll** for physical arm support with animated fingers. `LeftContact` and `RightContact` are separate finger-only layers selected through `ControlInteraction.TrySetAnimationLayer`; complete gestures use the arm layers in Animator mode. The action commits once at its clip marker.
4. Inspect **Driver Seat**: the example selects **Parent** attachment for Animator and Animator + IK so the driver follows the moving seat, and **Spring** for Ragdoll to provide physical support while preserving the skeleton hierarchy for animated limbs.
5. Open the passenger's **PassengerAnimator** controller to inspect the steering blend tree and masked gesture layers. Fit gesture contacts and clips before adapting the example to another cockpit.

The `DemoAnimatorCar` component supplies the example UI and binds its actions through the package's standard `ControlInteraction` and passenger APIs. It belongs to the sample and is not a required runtime module. See [timed control interactions](ControlInteractions.md#inspector-reach-with-ik-then-animate-a-switch-gesture) for building an equivalent setup from the Inspector.

## Animated entry and exit

Car and CarAnimator have left/right access profiles in `Demo/Resources/EVSAccess`. Press **F** while stopped. `LeftAccess` / `RightAccess` use Animator root motion and manually calibrated foot-contact curves. `LeftAccessOpen` / `RightAccessOpen` use shorter clips without the door-opening/closing gestures; a door already open before access stays open. Both Car prefabs assign the matching open-door profile.

The closed-door clips issue **AccessOpenDoor**, **AccessWaitForOpenDoor** and **AccessCloseDoor** Animation Events. Playback waits before passage until the actual door is ready; blocked doors cancel after SeatAccess's Door Timeout. To customize stride, foot contacts or marker timing, follow [Animated access](PassengerAccess.md). Root motion and Foot IK can be configured independently in the profile.
