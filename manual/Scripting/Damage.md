# Body opening, damage and repair

Body operation, damage accumulation and mesh deformation are separate layers. A body part can open around a hinge; a damage part can receive hits and detach; a deformation component can dent readable mesh geometry. Combining these layers produces a damaged vehicle without making every opening mechanism responsible for health or rendering.

Use the layer that matches the action. Open a door through `Body`, report a gameplay impact through `Damage`, and restore geometry through `VehicleMeshDeformation`. VehicleController.RepairAll coordinates retained registered parts, wheel reconnection, body hinges and mesh restoration; ResetVehicle additionally teleports and resets passengers. Destroyed objects still need application respawning.

## Implementation map

| Class | Responsibility |
| --- | --- |
| `Body` | Finds and operates authored `VehicleBodyPart` entries. |
| `Damage` | Accepts impacts and routes them to damage/deformation boundaries. |
| `DamageCollisionRelay` | Relays relevant native collisions into damage handling. |
| `DamagePart` | Tracks a part's damage and detachment behavior. |
| `ICollisionDamageResponse` | Lets a target alter collision damage severity. |
| `VehicleBodyPart` | Defines a named opening/moving body element. |
| `VehicleMeshDeformation` | Owns readable mesh instances, dent buffers and geometry restoration. |

## Independent ownership

Collision damage needs an impact measure rather than simply the vehicle's speed. Contact-normal relative motion distinguishes a head-on impact from moving quickly along a wall. Scripted damage already supplies an amount, so it should not be accidentally scaled again by a response intended only for native collisions.

Keep presentation and gameplay state separate in consumers too. A dent is a mesh change, a hit is an accepted damage event and detachment is an ownership change. A hit effect may happen before the mesh upload, while a repair screen may need to inspect the final geometry.

`Body` operates `VehicleBodyPart` entries by case-sensitive ID. `Damage` routes copied collision/scripted impacts to `DamagePart` boundaries and optional `VehicleMeshDeformation`. An opening hinge is not itself a health/detachment policy.

Collision severity uses contact-normal relative speed above threshold, not tangential travel speed. Scripted `ApplyImpact` supplies its own amount and does not pass through collision-only target response scaling. `damageEnabled`, `deformationEnabled` and `detachmentEnabled` are independent policy gates for accepted hits.

## Open a named part

Treat a part ID as an authored contract between the vehicle prefab and application interaction. The adapter returns the action result so a missing, disabled or released door does not appear to open successfully. Keep door-specific UI text and interaction selection outside the body mechanism.

When creating reusable prefabs, choose consistent IDs for equivalent parts. This lets the same application adapter operate several vehicles through configuration rather than searching transform names or hard-coding mesh hierarchy paths.

Assign the `Body` and the ID configured on a `VehicleBodyPart`. Missing/disabled/released targets return `false`.

**Example: `BodyPartControl.cs`**

<!-- example: BodyPartControl.cs -->
```csharp
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
```

## Observe accepted damage

The sample captures the subscribed publisher separately from its editable reference and removes that exact subscription on disable. `DamageHit` supplies the accepted amount, so the observer does not attempt to recompute collision severity from vehicle speed.

Use `Hit` for gameplay notifications or accumulated statistics. Use the geometry-change notification when a consumer must inspect uploaded vertices. Keeping those consumers on the appropriate event avoids forcing an immediate mesh upload for every accepted collision.

`Damage.Hit` provides `DamageHit` (part, point, direction and amount). It occurs when damage is accepted; a mesh upload can occur later in `LateUpdate`. Use `DeformationChanged` when inspecting uploaded geometry. Subscribe with a named handler and release the same captured source.

**Example: `DamageObserver.cs`**

<!-- example: DamageObserver.cs -->
```csharp
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
```

## Geometry and restoration

`VehicleMeshDeformation` owns runtime copies of readable `MeshFilter` meshes and changes vertices around accepted impacts. It retains rest geometry so a dent is bounded relative to the original shape and can be restored later. This avoids progressively treating an already-dented mesh as a new unbounded baseline. Reused vertex buffers are uploaded in `LateUpdate`; native collision proxies do not continuously deform with every visual vertex, and skinned meshes are outside this path.

Use `Deform` when supplying a custom local mesh impact and `RestoreShape` when resetting the owned geometry. A `Damage` integration normally routes accepted hits to it. `DeformationChanged` follows geometry update; `Restored` reports restoration. Choose these events when a renderer/tool must inspect shape rather than reacting merely to a hit.

Configure `DamagePart.detachedVehicleColliders` before startup to enable permanent chassis shapes when a panel releases. Keep those collider GameObjects active, their colliders disabled, and outside detachable groups, with one owner per collider. Activation precedes `Detached`; full repair restores captured enabled states before `Restored`. Parent-group release also activates nested parts' configured shapes. This performs work on release/repair only. See [exposed chassis setup](../Damage.md#protect-exposed-chassis-after-detachment).

`DamagePart` owns the part's counter and detachment threshold. `ReceiveDamage` evaluates that counter, `Repair(amount)` removes damage and returns the actual repaired amount, and `Detach` changes object ownership. RepairFully coordinates remounting a retained object, restoring its part meshes and clearing damage. Destroyed objects still need an application reconstruction policy.

A restoration policy should state what “repair” includes. Resetting a counter makes a damage part eligible for future hits but does not recreate a missing object. Restoring vertices removes dents but does not reattach debris. Teleporting a vehicle changes pose without rebuilding its authored hierarchy.

For pooling, retain the required part instances and call RepairAll before returning the vehicle to play, or recreate destroyed objects through your pool. For a persistent world, the application may instead leave detached debris alive. Those are application lifetime choices; the local damage mechanic cannot infer them.

`DamagePart.Repair(amount)` reduces an attached part’s counter and VehicleMeshDeformation.RestoreShape restores geometry only. Use RepairFully/RepairAll to remount retained debris, or VehicleController.ResetVehicle for repair plus a pose/passenger reset. Teleport alone remains pose-only.

Detached parts inherit motion and remain physical. Collision-clearance policy delays recontact with the former owner. `ICollisionDamageResponse` changes collision damage severity only; it does not change scripted amount, target mass or all physical contacts.

## Custom impact effect

Implement the callback interface on a component inside the profile's pooled prefab. The pool activates the object before PlayImpact and calls StopImpact before returning or replacing it. The lease is controlled by Effect Lifetime, not by your callback. Keep callbacks allocation-free and reset state for the next hit.

<!-- example: ImpactLight.cs -->
```csharp
using EasyVehicleSystem;
using UnityEngine;

public sealed class ImpactLight : MonoBehaviour, IDamageImpactEffect
{
    [SerializeField] private Light flash;
    public void PlayImpact(DamageHit hit, float intensity)
    {
        if (flash) { flash.intensity = Mathf.Lerp(1f, 5f, intensity); flash.enabled = true; }
    }
    public void StopImpact()
    {
        if (flash) flash.enabled = false;
    }
}
```

DamageHit keeps Part, Point, Direction and Amount and adds HasPhysicalImpact, ImpactSpeed (m/s), Impulse (N·s) and Force (N). The original constructor and ApplyImpact(point, direction, amount) create severity-only hits. The overload with physical values validates finite, nonnegative metadata. Force from Unity collisions is average impulse/timestep, not peak force. Use ResolveImpactProfile(hit) for threshold-aware selection; the part-only overload matches materials without evaluating severity.

On DamageImpactEffects, TryPlayEffect(hit) requests visuals without applying damage. EffectPlayed fires only for an accepted visual lease. ActiveEffectCount reports occupied slots; PlayedEffectCount counts starts and DroppedEffectCount counts requests rejected by the visual pool, including cooldown/capacity. Hit reports gameplay damage independently of whether a presentation response played. WarmUpEffects rebuilds capacity; ClearEffects returns current effects; SetImpactEffectsEnabled toggles presentation only.

## Body-part opening and closing curves

VehicleBodyPart.openingMotionCurve and closingMotionCurve independently shape normalized time-to-progress. Speed sets average commanded degrees/second. For animated doors the curve controls the pose; for physical doors it controls the spring target, leaving actual motion to the hinge solver. SetOpen restarts from the current actual angle only when the requested state changes. IsOpen remains the request flag, rather than an arrival notification. See [movement curves](../MovingParts.md#shape-movement-speed-with-curves).

## Body-part operation lifecycle

VehicleBodyPart exposes OpeningStarted, OpeningCompleted, ClosingStarted and ClosingCompleted as C# events and matching Inspector callbacks under motionEvents. OpenChanged reports a change to the requested open/closed state. Completion uses CurrentAngle and completionTolerance, so a physical hinge blocked by a collision does not publish success merely because its spring command finished. Release cancels pending completion. See [the moving-parts guide](../MovingParts.md#motion-events-and-four-audio-cues) for interruption, sound and source-ownership rules.

## Repair a wheel or reset the whole vehicle

See [wheel setup and repair tutorials](../Damage.md#detachable-wheels). Repair methods operate on retained components and require no new damage admission. Use the ID on DamagePart/WheelPart, not a GameObject name or Wheel Setup label.

<!-- example: VehicleRepairActions.cs -->
```csharp
using UnityEngine;
using EasyVehicleSystem;

namespace VehicleDocumentationExamples
{
    public class VehicleRepairActions : MonoBehaviour
    {
        public VehicleController vehicle;
        public Transform respawn;
        public string wheelId = "wheel.front-left";

        public bool RepairWheel() => vehicle && vehicle.RepairPart(wheelId);
        public void RepairAll() { if (vehicle) vehicle.RepairAll(); }
        public void FullReset()
        {
            if (vehicle && respawn) vehicle.ResetVehicle(respawn.position, respawn.rotation);
        }
    }
}
```

`WheelPart` is a DamagePart subtype and belongs to the same Damage.Parts / Body.DamageParts registry. Its native Wheel adapter stays on the suspension mount. Read Wheel.Attached and subscribe to Wheel.AttachmentChanged or VehicleController.WheelAttachmentChanged to observe release/reconnection; use the part-level APIs to physically detach/remount it.

## Complete public method and event index

The lists below cover public methods and events for this topic and their package base contracts. Signatures include overloads. See [the detailed body operation and damage API](../API/Damage.md) for arguments, return semantics, state and configuration. An override replaces the matching inherited implementation; it is not an additional call to make.

### Body

[Body](../API/Damage.md#body) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public virtual VehicleBodyPart GetPart(string id)` | Finds the authored body part by its case-sensitive ID. |
| `public virtual bool Open(string id)` | Requests opening of this part or the body part selected by ID. |
| `public virtual bool Close(string id)` | Requests closure of this part or the body part selected by ID. |
| `public virtual bool Toggle(string id)` | Requests the opposite current body/switch/wiper/profile/gear state through the declaring component. |
| `public virtual bool SetPhysics(string id, bool enabled)` | Looks up the case-sensitive part ID and requests that part's physics policy, returning `false` when no eligible target exists. |
| `public virtual bool SetOpen(string id, bool open)` | Requests a body part's open/closed target. |
| `public virtual void OpenAll()` | Requests opening of every eligible authored body part. |
| `public virtual void CloseAll()` | Requests closure of every eligible authored body part. |

### Damage

[Damage](../API/Damage.md#damage) gives the full declared contract.

- `public event Action<DamageHit, float> DeformationRequested` — Accepted hit and radius before part detachment; optional deformation receivers process it synchronously.
- `public event Action EffectsCleared` — Requests clearing optional impact presentation.
- `public event Action FullyRepaired` — Current fully repaired.
- `public event Action<DamageHit> Hit` — // Reports each accepted copied damage hit after its target part and severity are resolved.
- `public event Action PartsChanged` — Reports that the damage boundary list has been refreshed.
- `public virtual void ApplyImpact(Vector3 point, Vector3 direction, float amount)` — Current apply impact.
- `public virtual void ApplyImpact(Vector3 point, Vector3 direction, float amount, float impactSpeed, float impulse, float force)` — Current apply impact.
- `public virtual void ClearEffects()` — Stops all pooled impact effects.
- `public override void Configure(VehicleController vehicle)` — Binds the component to its configured owner and selected source.
- `public virtual DamagePart GetPart(string id)` — Current get part.
- `public virtual void ReceiveImpact(Impact impact)` — // Accepts a copied impact snapshot and routes it through this component's damage policy.
- `public virtual void RefreshParts()` — Current refresh parts.
- `public virtual void RepairAll()` — Current repair all.
- `public virtual bool RepairPart(DamagePart part)` — Current repair part.
- `public virtual bool RepairPart(string id)` — Current repair part.
- `public virtual DamageImpactProfile ResolveImpactProfile(DamageHit hit)` — Current resolve impact profile.
- `public virtual DamageImpactProfile ResolveImpactProfile(DamagePart part)` — Current resolve impact profile.

### DamageImpactEffects

[DamageImpactEffects](../API/Damage.md#damageimpacteffects) gives the full declared contract.

- `public event Action<DamageHit, DamageImpactProfile> EffectPlayed` — Current effect played.
- `public virtual void ClearEffects()` — Stops all pooled impact effects.
- `public override void Configure(VehicleController owner)` — Binds the component to its configured owner and selected source.
- `public virtual void SetImpactEffectsEnabled(bool value)` — Current set impact effects enabled.
- `public virtual bool TryPlayEffect(DamageHit hit)` — Current try play effect.
- `public virtual void WarmUpEffects()` — Current warm up effects.

### DamageImpactProfile

[DamageImpactProfile](../API/Damage.md#damageimpactprofile) gives the full declared contract.

- `public virtual bool Matches(DamagePart part)` — Current matches.
- `public virtual bool TryEvaluate(DamageHit hit, out float intensity)` — Current try evaluate.

### DamagePart

[DamagePart](../API/Damage.md#damagepart) gives the full declared contract.

- `public event Action<DamagePart, float> Damaged` — Current damaged.
- `public event Action<DamagePart> Detached` — // Reports this part after it becomes independent physical debris.
- `public event Action<DamagePart, float> Repaired` — Current repaired.
- `public event Action<DamagePart> Restored` — Current restored.
- `public virtual bool Detach(Rigidbody vehicleBody)` — Current detach.
- `public virtual void ReceiveDamage(float amount)` — // Accumulates finite positive damage only while the part is attached and then publishes the accepted amount.
- `public virtual float Repair(float amount)` — Current repair.
- `public virtual bool RepairFully()` — // Full repair is deliberately separate from incremental Repair(amount).

### IDamageImpactEffect

| Signature | Behavior |
| --- | --- |
| `void PlayImpact(DamageHit hit, float intensity)` | Initializes a leased effect using hit metadata and normalized intensity. |
| `void StopImpact()` | Resets a pooled effect before return or replacement. |

### IVehicleModule

[IVehicleModule](../API/Modules.md#ivehiclemodule) gives the full declared contract.

| Method | Role |
| --- | --- |
| `void Configure(VehicleController vehicle)` | Repeatable setup contract supplied with the owning `VehicleController`. |
| `void Step(VehicleController vehicle, Command command, float deltaTime)` | Contract for one owner-supplied fixed tick; implement only the module responsibility and use the supplied Command/timestep. |

### VehicleBodyPart

[VehicleBodyPart](../API/Damage.md#vehiclebodypart) gives the full declared contract.

- `public event System.Action ClosingCompleted` — Current closing completed.
- `public event System.Action ClosingStarted` — Current closing started.
- `public event System.Action MotionAudioStopped` — Requests stopping movement audio after interruption or disable.
- `public event System.Action<PartMotionEvent> MotionOccurred` — Reports an admitted movement phase to optional presentation receivers.
- `public event System.Action<bool> OpenChanged` — // Reports a changed open/closed request rather than physical hinge arrival.
- `public event System.Action OpeningCompleted` — Current opening completed.
- `public event System.Action OpeningStarted` — Current opening started.
- `public event System.Action<bool> PhysicsChanged` — Current physics changed.
- `public event System.Action Released` — // Notifies observers after hinge ownership is permanently released.
- `public virtual void Close()` — Current close.
- `public virtual void Open()` — Current open.
- `public virtual void RefreshIgnoredCollisions()` — Current refresh ignored collisions.
- `public virtual void Release()` — Current release.
- `public virtual void RepairFully()` — Current repair fully.
- `public virtual void SetOpen(bool value)` — Current set open.
- `public virtual void SetPhysics(bool value)` — Current set physics.
- `public virtual void Toggle()` — Current toggle.
- `public virtual bool TryUnlatchFromImpact(float force, float speed)` — // force: average contact force in N; speed: approach speed along the impact normal in m/s.

### VehicleMeshDeformation

[VehicleMeshDeformation](../API/Damage.md#vehiclemeshdeformation) gives the full declared contract.

- `public event System.Action DeformationChanged` — // Notifies observers after accumulated vertex changes are uploaded.
- `public event System.Action Restored` — // Notifies observers after original mesh shapes are restored.
- `public override void Configure(VehicleController owner)` — Binds the component to its configured owner and selected source.
- `public virtual void Deform(DamageHit hit, float radius, float dentPerDamage, float maximumDent)` — // Displaces vertices near the damage point, caps displacement from their rest positions and defers mesh upload.
- `public virtual void FlushPendingDeformation()` — Current flush pending deformation.
- `public virtual void RestoreShape()` — Current restore shape.
- `public virtual void RestoreShape(DamagePart part)` — Current restore shape.

### VehicleModule

[VehicleModule](../API/Modules.md#vehiclemodule) gives the full declared contract.

| Method | Role |
| --- | --- |
| `public virtual void Configure(VehicleController vehicle)` | Empty base setup hook. Derived components may cache references/apply persistent settings; the controller owns lifecycle notifications. |
| `public virtual void Step(VehicleController vehicle, Command command, float deltaTime)` | Empty base extension point. The controller schedules derived work and emits lifecycle notifications around it. |
| `public virtual void SetEnabled(bool value)` | Changes module enabled state and publishes an actual requested-flag change. |
| `public virtual bool SupportsProfile(DriveProfile profile)` | Checks movement-family compatibility; this is independent of the Unity enabled flag. |

| Event / callback | Role |
| --- | --- |
| `public event System.Action<bool> EnabledChanged` | After `SetEnabled` changes the module flag. Payload: requested enabled bool; no event for an unchanged request. |
| `public event System.Action<VehicleController> Configured` | After controller-driven module configuration. Payload: the owning `VehicleController`. |
| `public event System.Action<VehicleController, Command, float> Stepped` | After this registered module has stepped. Payload: vehicle, sampled Command, timestep in seconds. |

### WheelPart

[WheelPart](../API/Damage.md#wheelpart) gives the full declared contract.

- `public override bool Detach(Rigidbody vehicleBody)` — Current detach.

`Damage.Hit` and `DeformationRequested` include `DamageHit.Telemetry`, the vehicle’s latest completed telemetry snapshot. Check `HasTelemetry` for manually constructed hits. Collision-time speed, force and impulse remain separate impact fields; the cached telemetry can precede the contact callback.
