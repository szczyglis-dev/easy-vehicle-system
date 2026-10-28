.. _evs-scripting-interior--interior-presentation-contracts:

Interior presentation contracts
===============================

Interior presentation translates mechanical state into instruments, cockpit controls and driver-visible systems. A value source reads a mechanic; a needle or rotary control maps that value to a pose; a binding connects accepted actions to the appropriate presentation. Mirrors and wipers add their own rendering and motion lifecycles.

The central design rule is one owner for each value and transform. A bound instrument follows its source. An API-driven instrument follows explicit requests. A moving pivot follows one animator. Keeping these ownership choices explicit makes it possible to replace a dashboard or integrate another UI without changing the mechanics.

.. _evs-scripting-interior--implementation-map:

Implementation map
------------------

+-------------------------+------------------------------------------------------------------------+
| Class                   | Responsibility                                                         |
+=========================+========================================================================+
| ``AnchoredRotation``    | Preserves a neutral pose relative to an independent pivot frame.       |
+-------------------------+------------------------------------------------------------------------+
| ``RotaryHandle``        | Maps requested/source values to rotary presentation.                   |
+-------------------------+------------------------------------------------------------------------+
| ``InstrumentNeedle``    | Specializes value-driven rotation for instruments.                     |
+-------------------------+------------------------------------------------------------------------+
| ``InteriorValueSource`` | Base adapter for an ``IInteriorValueSource`` value producer.           |
+-------------------------+------------------------------------------------------------------------+
| ``GearShiftBinding``    | Synchronizes shift presentation with accepted mechanical gear changes. |
+-------------------------+------------------------------------------------------------------------+
| ``RearMirrors``         | Owns mirror eligibility, camera rendering and generated textures.      |
+-------------------------+------------------------------------------------------------------------+
| ``Wipers``              | Owns wiper cycle timing, running state and blade dispatch.             |
+-------------------------+------------------------------------------------------------------------+
| ``WiperBlade``          | Maps normalized stroke to authored blade geometry.                     |
+-------------------------+------------------------------------------------------------------------+
| ``FuelTank``            | Owns fuel quantity, consumption and ignition-empty policy.             |
+-------------------------+------------------------------------------------------------------------+

.. _evs-scripting-interior--neutral-frames-and-value-sources:

Neutral frames and value sources
--------------------------------

A neutral frame describes what “zero” means for a particular model. Capture it with the part in its authored neutral position, before any runtime control has turned it. If configuration recaptured the current animated pose as neutral, each reconfiguration could move the baseline and accumulate an offset.

A source value should have a clear unit. A speed source may report a physical speed range; the fuel source below reports a fraction from zero to one. ``Configure`` the consumer's value range to that unit, then configure its angle range from the mesh. Keeping units explicit avoids putting dashboard-specific angle conversions inside the fuel mechanic.

``AnchoredRotation`` stores a moving part's neutral position/orientation in an independent anchor frame. Both position and orientation orbit that anchor. The anchor must not be the part or its descendant. Capture neutral poses while authored neutral; repeated enable/configure must not recapture a turned control.

``InstrumentNeedle`` and ``RotaryHandle`` map a physical value range to signed degrees. ``SetValue`` requests a smoothed value; ``SetNormalizedValue`` maps a fraction; ``SetImmediate`` bypasses smoothing. A bound ``IInteriorValueSource`` owns ongoing values. ``Bind``\ (``null``) releases it for API control. ``ValueChanged`` reports the requested value, not arrival.

.. _evs-scripting-interior--add-a-fuel-needle-source:

Add a fuel needle source
------------------------

Derive from ``InteriorValueSource`` when the missing piece is only a reading. ``ReadValue()`` should read and return a value without changing the underlying mechanic. The needle owns smoothing and angle mapping, so the source does not need another ``Update`` or its own rotation code.

This sample returns zero when the tank reference is absent. An application that must distinguish “empty” from “unavailable” can add its own display status alongside the numeric source rather than assigning special out-of-range values to the needle.

Put this source beside the instrument, assign ``FuelTank``, then drag it into the needle Source field. Set the needle range to 0–1 and its angle range for the model.

**Example: ``FuelNeedleSource.cs``**

.. raw:: html

   <!-- example: FuelNeedleSource.cs -->

.. code-block:: csharp

   using UnityEngine;
   using EasyVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class FuelNeedleSource : InteriorValueSource
       {
           public FuelTank tank;
           public override float ReadValue() => tank ? tank.Fraction : 0;
       }
   }

This source only reads fuel. Turning a presentation knob does not refuel the tank unless application code explicitly connects that action.

.. _evs-scripting-interior--gear-and-switch-bindings:

Gear and switch bindings
------------------------

ProfileSwitchBinding selects explicit On Profile Id and Off Profile Id registrations from ProfileSwitcher. SetOn(true) selects the on ID; SetOn(false) selects the off ID. It supports any two entries from a larger profile list.

A binding keeps a presentation control synchronized with a mechanic. It sits between two owners: the mechanic knows the accepted state, and the handle knows how the model moves. The binding should translate between them without taking over either simulation.

``GearShiftBinding`` resolves a gearbox and drives an ``IGearShiftHandle``; a paddle can animate an accepted up/down shift without becoming the gearbox itself. ``IndicatorSwitchBinding``, ``WiperSwitchBinding`` and ``ProfileSwitchBinding`` connect their corresponding switches. Their ``Synchronize`` operations display the current mechanic state without issuing another user request, preventing a feedback loop between a switch event and its own display update.

For a custom binding, subscribe to the mechanic that owns the result, retain the exact subscribed instance, and release it when rebinding or disabling. Use silent/immediate presentation synchronization when restoring a pooled vehicle. Put player intent in the request path, and let the mechanic's result bring the displayed state back into agreement.

Observe the accepted mechanic state when the display should tell the driver what actually happened. Animating a gear paddle from input can show the driver's gesture; animating the gear indicator from accepted gearbox state shows the selected gear. They are useful but different signals.

When replacing a control animator, preserve its neutral-frame convention and remove the old transform writer. A correct custom animation can still jitter if a passenger binding or another animator writes the same pivot later in the frame.

When ``Passengers`` advances a switch, disable duplicate animation in a separate binding. A binding owns synchronization, not another physics or input loop.

.. _evs-scripting-interior--rearmirrors:

RearMirrors
-----------

A mirror needs a camera view, an output texture and a visible surface using that texture. The module manages eligibility and refresh so every mirror does not need a full camera render every frame. Choose texture dimensions and refresh budget for the screen area and number of simultaneously visible mirrors.

Ownership matters for pooling: a texture created by the module can be released with it, while a supplied texture may be shared by another application system. Do not destroy supplied resources when replacing the mirror implementation. For a custom render pipeline, provide the compatible rendering path rather than changing the mirror's physical surface geometry.

Each ``RearMirror`` entry has one dedicated camera, surface and optional caller-owned texture. The observer/frustum/range and refresh budget decide eligibility. This is not occlusion checking; application knowledge can disable a hidden mirror explicitly.

Generated textures/sources are module-owned. Supplied textures remain caller-owned. Disabling restores captured camera state/property blocks. Re-enable after changing dimensions. Camera.Render is used on Built-in; supported SRPs use ``StandardRequest``. Unsupported rendering pipelines need an integration.

.. _evs-scripting-interior--gate-mirror-rendering-from-a-quality-policy:

Gate mirror rendering from a quality policy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An application quality setting can disable mirror work through the module rather than disabling individual cameras behind its back. The action updates eligibility while preserving the module's ownership and events. When enabled again, normal observer/frustum/range policy still decides whether a mirror renders.

**Example: ``MirrorQualityPolicy.cs``**

.. raw:: html

   <!-- example: MirrorQualityPolicy.cs -->

.. code-block:: csharp

   using UnityEngine;
   using EasyVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class MirrorQualityPolicy : MonoBehaviour
       {
           public RearMirrors mirrors;

           public void SetMirrorRendering(bool allowed)
           {
               if (mirrors) mirrors.SetMirrorsEnabled(allowed);
           }
       }
   }

Use ``SetMirrorEnabled(index, value)`` for one configured mirror. Its index belongs to the current mirror array; if the application rebuilds that array, resolve its own stable entry identity first. Camera pose authoring and texture-size changes remain separate configuration operations.

.. _evs-scripting-interior--wipers:

Wipers
------

Treat the module as the clock and the blade as geometry. Several blades can share one cycle while using different spindle positions and angle ranges. A custom blade geometry adapter should consume that phase; it should not run another independent timer that gradually drifts from the opposite blade.

Stopping through the public running action allows a natural finish. Disabling the component is a lifecycle operation with parking behavior. Use the action for a dashboard switch and the lifecycle operation when removing or suspending the system.

``Wipers`` owns the blade list, running request, cycle phase, speed and stroke audio. ``WiperBlade`` only applies normalized geometry around its lower spindle. Helpers must be listed on the module; they do not schedule themselves. Pivot-only ``Wiper`` entries are an alternative setup, not a second animation to run on the same mesh.

``SetRunning``\ (``false``) completes the current cycle; disable parks. Zero speed pauses. ``SetSpeed``, ``Toggle`` and state/events provide control. ``SetValue``/``ParkImmediate``/``CaptureRestPose`` on the blade are geometry operations for custom integration.

.. _evs-scripting-interior--fuel-and-assists:

Fuel and assists
----------------

``FuelTank`` is the quantity and consumption mechanic. It stores fuel independently of a gauge, so replacing a dashboard does not change available fuel. Consumption uses running state and engine activity; an instrument source only reads the resulting quantity or fraction.

``consumeFuel`` chooses whether running consumes fuel, using idle/load/RPM consumption rates in litres per hour. ``stopEngineWhenEmpty`` separately chooses whether an empty tank stops/blocks the engine. ``Configure`` both deliberately for a vehicle that should have an actual fuel constraint. A decorative gauge can read a tank even when consumption is disabled.

``DrivingAssists`` is a different responsibility: it coordinates traction/stability assist choices. Its public setters are the preferred application boundary when it owns those settings. Disabling it stops synchronization; it does not reconstruct whatever values the underlying modules had before. A workshop or save system should therefore store its intended assist configuration rather than infer a previous state from enable/disable.

``DrivingAssists`` writes its shared TCS/``Steering`` settings while enabled; disabling stops synchronization but does not roll values back. Stability is bounded yaw/lateral assistance, not brake-based ESP.

For controls setup see :doc:`Interior controls </InteriorControls>`; for backend-independent subscriptions see :doc:`Events </Scripting/Events>`.

.. _evs-scripting-interior--refuel-through-a-service-action:

Refuel through a service action
-------------------------------

Use the actual transferred quantity when connecting a tank to a garage or supply system. ``Refuel`` can accept less than requested when the tank approaches capacity. The component below exposes that amount so an application can charge for actual litres or subtract the same amount from a supply inventory.

**Example: ``FuelServiceAction.cs``**

.. raw:: html

   <!-- example: FuelServiceAction.cs -->

.. code-block:: csharp

   using UnityEngine;
   using EasyVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class FuelServiceAction : MonoBehaviour
       {
           public FuelTank tank;
           [Min(0)] public float requestedLitres = 10;
           public float LastTransferredLitres { get; private set; }

           public void Refuel()
           {
               LastTransferredLitres = tank ? tank.Refuel(requestedLitres) : 0;
           }
       }
   }

Refuelling does not itself request ignition. Keep the service operation and engine-start action separate so a vehicle can remain parked after receiving fuel. For a finite supply, calculate the permitted request before the call, then debit only the returned amount.

.. _evs-scripting-interior--complete-public-method-and-event-index:

Complete public method and event index
--------------------------------------

The lists below cover public methods and events for this topic and their package base contracts. Signatures include overloads. See :doc:`the detailed cockpit instruments and bindings API </API/Interior>` for arguments, return semantics, state and configuration. An override replaces the matching inherited implementation; it is not an additional call to make.

.. _evs-scripting-interior--aircraftcontrolmotion:

AircraftControlMotion
~~~~~~~~~~~~~~~~~~~~~

:ref:`AircraftControlMotion <evs-api-interior--aircraftcontrolmotion>` gives the full declared contract.

+----------------------------------------------------+------------------------------------------------------------------------------------------+
| Method                                             | Role                                                                                     |
+====================================================+==========================================================================================+
| ``public virtual void SetValue(float normalized)`` | Applies normalized aircraft-control travel to its authored rotation/translation mapping. |
+----------------------------------------------------+------------------------------------------------------------------------------------------+

.. _evs-scripting-interior--aircrafthud:

AircraftHud
~~~~~~~~~~~

:ref:`AircraftHud <evs-api-interior--aircrafthud>` gives the full declared contract.

+-------------------------------------------------------------+-------------------------------------------------------------------------------------------+
| Method                                                      | Role                                                                                      |
+=============================================================+===========================================================================================+
| ``public override void Configure(VehicleController owner)`` | Binds the HUD to this vehicle's telemetry source.                                         |
+-------------------------------------------------------------+-------------------------------------------------------------------------------------------+
| ``public virtual void Bind(VehicleController owner)``       | Binds the HUD to a vehicle/telemetry source and releases its previous owned subscription. |
+-------------------------------------------------------------+-------------------------------------------------------------------------------------------+

+--------------------------------------------+-------------------------------------------------------------------------+
| Event / callback                           | Role                                                                    |
+============================================+=========================================================================+
| ``public event Action<Telemetry> Changed`` | After the HUD receives an updated reading. Payload: Telemetry snapshot. |
+--------------------------------------------+-------------------------------------------------------------------------+

.. _evs-scripting-interior--anchoredrotation:

AnchoredRotation
~~~~~~~~~~~~~~~~

:ref:`AnchoredRotation <evs-api-interior--anchoredrotation>` gives the full declared contract.

+-----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+
| Method                                                                                              | Role                                                                                      |
+=====================================================================================================+===========================================================================================+
| ``public virtual void CaptureRestPose()``                                                           | Captures the currently authored rest pose for this geometry mapper or blade.              |
+-----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+
| ``public virtual bool TryGetPose(float degrees, out Vector3 position, out Quaternion orientation)`` | Computes a pose from the captured anchored rest frame when geometry references are valid. |
+-----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+
| ``public virtual Vector3 GetPointAtAngle(Vector3 meshLocalPoint, float degrees)``                   | Returns the neutral-frame point after applying a specified rotation angle.                |
+-----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+
| ``public virtual void SetAngle(float degrees)``                                                     | Immediately applies a moving-part/geometry rotation in degrees.                           |
+-----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+

.. _evs-scripting-interior--carhud:

CarHud
~~~~~~

:ref:`CarHud <evs-api-interior--carhud>` gives the full declared contract.

+----------------------------------------------------------+-------------------------------------------------------------------------------------------+
| Method                                                   | Role                                                                                      |
+==========================================================+===========================================================================================+
| ``public virtual void Bind(VehicleController selected)`` | Binds the HUD to a vehicle/telemetry source and releases its previous owned subscription. |
+----------------------------------------------------------+-------------------------------------------------------------------------------------------+

+--------------------------------------------+-------------------------------------------------------------------------+
| Event / callback                           | Role                                                                    |
+============================================+=========================================================================+
| ``public event Action<Telemetry> Changed`` | After the HUD receives an updated reading. Payload: Telemetry snapshot. |
+--------------------------------------------+-------------------------------------------------------------------------+

.. _evs-scripting-interior--enginerpmsource:

EngineRpmSource
~~~~~~~~~~~~~~~

:ref:`EngineRpmSource <evs-api-interior--enginerpmsource>` gives the full declared contract.

+---------------------------------------+----------------------------------------------------------------------------------------+
| Method                                | Role                                                                                   |
+=======================================+========================================================================================+
| ``public override float ReadValue()`` | Reads a numeric instrument source in the source's documented physical/normalized unit. |
+---------------------------------------+----------------------------------------------------------------------------------------+

.. _evs-scripting-interior--fueltank:

FuelTank
~~~~~~~~

:ref:`FuelTank <evs-api-interior--fueltank>` gives the full declared contract.

+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| Method                                                                                     | Role                                                                                                                       |
+============================================================================================+============================================================================================================================+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Stops an empty constrained engine, otherwise consumes running idle/load fuel and publishes actual quantity transitions.    |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float Drain(float litres)``                                               | Removes a finite nonnegative requested number of litres, bounded by available fuel, and returns the actual litres removed. |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Fill()``                                                             | Sets quantity to capacity through ``SetFuel``, with normal actual-change notifications.                                    |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float Refuel(float litres)``                                              | Adds up to the requested litres, limited by capacity, and returns actual transfer.                                         |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetFuel(float litres)``                                              | Sets fuel quantity within capacity and publishes actual quantity/empty/refuel transitions.                                 |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+

+--------------------------------------------+-------------------------------------------------------------------------------------------------+
| Event / callback                           | Role                                                                                            |
+============================================+=================================================================================================+
| ``public event Action<float> FuelChanged`` | After actual fuel quantity changes. Payload: current litres, not the requested transfer amount. |
+--------------------------------------------+-------------------------------------------------------------------------------------------------+
| ``public event Action Emptied``            | On the transition to empty fuel. No payload.                                                    |
+--------------------------------------------+-------------------------------------------------------------------------------------------------+
| ``public event Action Refuelled``          | After an actual increase in fuel, including ``SetFuel``. No payload; query quantity if needed.  |
+--------------------------------------------+-------------------------------------------------------------------------------------------------+

.. _evs-scripting-interior--gearpaddlehandle:

GearPaddleHandle
~~~~~~~~~~~~~~~~

:ref:`GearPaddleHandle <evs-api-interior--gearpaddlehandle>` gives the full declared contract.

+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Method                                                               | Role                                                                                                                                |
+======================================================================+=====================================================================================================================================+
| ``public virtual void ResetMotion()``                                | Clears presentation requests and restores the released/default motion state.                                                        |
+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Tick(float deltaTime)``                        | Advances the declaring presentation/state machine by elapsed seconds; avoid a second call when its built-in owner already ticks it. |
+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void AnimateShift(int previousGear, int nextGear)`` | Requests a presentation gesture for an accepted change from the previous gear to the next gear.                                     |
+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Press()``                                      | Requests a paddle presentation press in the selected shift direction.                                                               |
+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+

+---------------------------------+------------------------------------------------------------------------------------------------------+
| Event / callback                | Role                                                                                                 |
+=================================+======================================================================================================+
| ``public UnityEvent onPressed`` | Inspector callback for a paddle press; no payload. The configured paddle determines shift direction. |
+---------------------------------+------------------------------------------------------------------------------------------------------+

.. _evs-scripting-interior--gearshiftbinding:

GearShiftBinding
~~~~~~~~~~~~~~~~

:ref:`GearShiftBinding <evs-api-interior--gearshiftbinding>` gives the full declared contract.

+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| Method                                                                                     | Role                                                                                                        |
+============================================================================================+=============================================================================================================+
| ``public virtual void Bind(Engine source)``                                                | Connects a gearbox to an ``IGearShiftHandle`` and refreshes the accepted-shift subscription.                |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| ``public virtual void RefreshBinding()``                                                   | Re-resolves the current gearbox/shift-handle binding and its subscription.                                  |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| ``public override void Configure(VehicleController vehicle)``                              | Refreshes the connected gearbox/shift-handle binding and subscriptions.                                     |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Refreshes its gearbox/handle association so changed explicit references use the correct event subscription. |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+

.. _evs-scripting-interior--handlecommandinput:

HandleCommandInput
~~~~~~~~~~~~~~~~~~

:ref:`HandleCommandInput <evs-api-interior--handlecommandinput>` gives the full declared contract.

+------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| Method                                                           | Role                                                                                        |
+==================================================================+=============================================================================================+
| ``public static float Read(Command command, HandleInput input)`` | Maps one ``HandleInput`` choice to the corresponding Command axis for cockpit presentation. |
+------------------------------------------------------------------+---------------------------------------------------------------------------------------------+

.. _evs-scripting-interior--igearshifthandle:

IGearShiftHandle
~~~~~~~~~~~~~~~~

:ref:`IGearShiftHandle <evs-api-interior--igearshifthandle>` gives the full declared contract.

+-------------------------------------------------------+-------------------------------------------------------------------------------------------------+
| Method                                                | Role                                                                                            |
+=======================================================+=================================================================================================+
| ``void AnimateShift(int previousGear, int nextGear)`` | Requests a presentation gesture for an accepted change from the previous gear to the next gear. |
+-------------------------------------------------------+-------------------------------------------------------------------------------------------------+

.. _evs-scripting-interior--iinteriorvaluesource:

IInteriorValueSource
~~~~~~~~~~~~~~~~~~~~

:ref:`IInteriorValueSource <evs-api-interior--iinteriorvaluesource>` gives the full declared contract.

+-----------------------+----------------------------------------------------------------------------------------+
| Method                | Role                                                                                   |
+=======================+========================================================================================+
| ``float ReadValue()`` | Reads a numeric instrument source in the source's documented physical/normalized unit. |
+-----------------------+----------------------------------------------------------------------------------------+

.. _evs-scripting-interior--imodule:

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

.. _evs-scripting-interior--indicatorswitchbinding:

IndicatorSwitchBinding
~~~~~~~~~~~~~~~~~~~~~~

:ref:`IndicatorSwitchBinding <evs-api-interior--indicatorswitchbinding>` gives the full declared contract.

+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Method                                              | Role                                                                                                                                |
+=====================================================+=====================================================================================================================================+
| ``public virtual void Tick(float deltaTime)``       | Advances the declaring presentation/state machine by elapsed seconds; avoid a second call when its built-in owner already ticks it. |
+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Synchronize(bool immediate)`` | Synchronizes presentation/selector state with its source; gearbox synchronization is not a validated driving shift request.         |
+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-scripting-interior--interiorvaluesource:

InteriorValueSource
~~~~~~~~~~~~~~~~~~~

:ref:`InteriorValueSource <evs-api-interior--interiorvaluesource>` gives the full declared contract.

+---------------------------------------+----------------------------------------------------------------------------------------+
| Method                                | Role                                                                                   |
+=======================================+========================================================================================+
| ``public abstract float ReadValue()`` | Reads a numeric instrument source in the source's documented physical/normalized unit. |
+---------------------------------------+----------------------------------------------------------------------------------------+

.. _evs-scripting-interior--module:

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

.. _evs-scripting-interior--profileswitchbinding:

ProfileSwitchBinding
~~~~~~~~~~~~~~~~~~~~

:ref:`ProfileSwitchBinding <evs-api-interior--profileswitchbinding>` gives the full declared contract.

+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Method                                              | Role                                                                                                                                |
+=====================================================+=====================================================================================================================================+
| ``public virtual void Tick(float deltaTime)``       | Advances the declaring presentation/state machine by elapsed seconds; avoid a second call when its built-in owner already ticks it. |
+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SetOn(bool on)``              | Requests onProfileId when on is true, otherwise offProfileId.                                                                       |
+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Synchronize(bool immediate)`` | Synchronizes presentation/selector state with its source; gearbox synchronization is not a validated driving shift request.         |
+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-scripting-interior--rearmirrors-1:

RearMirrors
~~~~~~~~~~~

:ref:`RearMirrors <evs-api-interior--rearmirrors>` gives the full declared contract.

+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| Method                                                                                            | Role                                                                                                              |
+===================================================================================================+===================================================================================================================+
| ``public virtual void SetMirrorsEnabled(bool value)``                                             | Changes the whole mirror system's rendering availability.                                                         |
+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetMirrorEnabled(int index, bool value)``                                   | Changes eligibility of one mirror entry.                                                                          |
+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetCameraPose(int index, Vector3 localPosition, Quaternion localRotation)`` | Sets local camera position/rotation for the indexed mirror. The index must be valid; a missing camera is ignored. |
+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+

+---------------------------------------------------------+------------------------------------------------------------------------+
| Event / callback                                        | Role                                                                   |
+=========================================================+========================================================================+
| ``public event Action<bool> MirrorsEnabledChanged``     | When whole-system mirror eligibility changes. Payload: bool.           |
+---------------------------------------------------------+------------------------------------------------------------------------+
| ``public event Action<int, bool> MirrorEnabledChanged`` | When one mirror's eligibility changes. Payload: mirror index and bool. |
+---------------------------------------------------------+------------------------------------------------------------------------+

.. _evs-scripting-interior--rotaryhandle:

RotaryHandle
~~~~~~~~~~~~

:ref:`RotaryHandle <evs-api-interior--rotaryhandle>` gives the full declared contract.

+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Method                                                       | Role                                                                                                                                                          |
+==============================================================+===============================================================================================================================================================+
| ``public virtual void Bind(MonoBehaviour valueSource)``      | Sets the ongoing instrument value source; ``null`` releases source ownership for explicit value API control.                                                  |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Tick(float deltaTime)``                | Advances the declaring presentation/state machine by elapsed seconds; avoid a second call when its built-in owner already ticks it.                           |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetNormalizedValue(float normalized)`` | Maps a normalized fraction across an instrument's configured physical value range.                                                                            |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetValue(float value)``                | Requests an instrument value in the configured physical/source range and emits ``ValueChanged`` for an actual request change; presentation smooths toward it. |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetImmediate(float value)``            | Applies the requested instrument value without smoothing, using the component's value-range and notification policy.                                          |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

+----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Event / callback                                   | Role                                                                                                                                                            |
+====================================================+=================================================================================================================================================================+
| ``public event System.Action<float> ValueChanged`` | When the requested instrument value changes. Payload: value in configured source units; this is not a motion-arrival notification.                              |
+----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent<float> onValueChanged``        | After this control's value changes. Payload: the event's value type; ``PedalHandle`` reports displayed travel, ``SwitchHandle`` reports a changed bool request. |
+----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-scripting-interior--speedvaluesource:

SpeedValueSource
~~~~~~~~~~~~~~~~

:ref:`SpeedValueSource <evs-api-interior--speedvaluesource>` gives the full declared contract.

+---------------------------------------+----------------------------------------------------------------------------------------+
| Method                                | Role                                                                                   |
+=======================================+========================================================================================+
| ``public override float ReadValue()`` | Reads a numeric instrument source in the source's documented physical/normalized unit. |
+---------------------------------------+----------------------------------------------------------------------------------------+

.. _evs-scripting-interior--steeringstickanimator:

SteeringStickAnimator
~~~~~~~~~~~~~~~~~~~~~

:ref:`SteeringStickAnimator <evs-api-interior--steeringstickanimator>` gives the full declared contract.

+----------------------------------------------+--------------------------------------------------------------------------------------+
| Method                                       | Role                                                                                 |
+==============================================+======================================================================================+
| ``public override void PrepareHandPose()``   | Prepares the hand pose associated with this cockpit animator.                        |
+----------------------------------------------+--------------------------------------------------------------------------------------+
| ``public override void CalibrateRestPose()`` | Captures the model's current neutral presentation frame for later control animation. |
+----------------------------------------------+--------------------------------------------------------------------------------------+

.. _evs-scripting-interior--steeringwheelanimator:

SteeringWheelAnimator
~~~~~~~~~~~~~~~~~~~~~

:ref:`SteeringWheelAnimator <evs-api-interior--steeringwheelanimator>` gives the full declared contract.

+-----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| Method                                                                                        | Role                                                                                              |
+===============================================================================================+===================================================================================================+
| ``public virtual void PrepareHandPose()``                                                     | Prepares the hand pose associated with this cockpit animator.                                     |
+-----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)``    | Advances steering presentation/hand targets once in the fixed pipeline before passenger feedback. |
+-----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+
| ``[ContextMenu("Capture steering wheel rest pose")] public virtual void CalibrateRestPose()`` | Captures the model's current neutral presentation frame for later control animation.              |
+-----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+

.. _evs-scripting-interior--sticksetup:

StickSetup
~~~~~~~~~~

:ref:`StickSetup <evs-api-interior--sticksetup>` gives the full declared contract.

+--------------------------------------------------------------+---------------------------------------------------------------------------------+
| Method                                                       | Role                                                                            |
+==============================================================+=================================================================================+
| ``public virtual void SetControls(float pitch, float roll)`` | Applies normalized pitch/roll control presentation to the authored stick setup. |
+--------------------------------------------------------------+---------------------------------------------------------------------------------+

.. _evs-scripting-interior--throttleanimator:

ThrottleAnimator
~~~~~~~~~~~~~~~~

:ref:`ThrottleAnimator <evs-api-interior--throttleanimator>` gives the full declared contract.

+------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| Method                                                                                   | Role                                                                                                             |
+==========================================================================================+==================================================================================================================+
| ``public virtual bool PrepareHandPose()``                                                | Prepares the hand pose associated with this cockpit animator.                                                    |
+------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``public override void Configure(VehicleController owner)``                              | Stores the vehicle supplying throttle presentation.                                                              |
+------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController owner, Command command, float deltaTime)`` | Resolves external or vehicle throttle, smooths lever presentation and updates changed displayed value/hand pose. |
+------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetThrottle(float value)``                                         | Takes external ownership of normalized throttle-lever presentation; ``FollowVehicle`` releases that override.    |
+------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``public virtual void FollowVehicle()``                                                  | Releases external presentation ownership and resumes vehicle-state following.                                    |
+------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+

+----------------------------------------------------+--------------------------------------------------------------------------------------------+
| Event / callback                                   | Role                                                                                       |
+====================================================+============================================================================================+
| ``public event System.Action<float> ValueChanged`` | When resolved throttle presentation changes. Payload: normalized displayed throttle value. |
+----------------------------------------------------+--------------------------------------------------------------------------------------------+

.. _evs-scripting-interior--wiperblade:

WiperBlade
~~~~~~~~~~

:ref:`WiperBlade <evs-api-interior--wiperblade>` gives the full declared contract.

+-----------------------------------------------+----------------------------------------------------------------------------------------------------------+
| Method                                        | Role                                                                                                     |
+===============================================+==========================================================================================================+
| ``public virtual void CaptureRestPose()``     | Captures the currently authored rest pose for this geometry mapper or blade.                             |
+-----------------------------------------------+----------------------------------------------------------------------------------------------------------+
| ``public virtual void SetValue(float value)`` | Applies normalized blade stroke using the captured spindle/rest geometry; it does not run a wiper clock. |
+-----------------------------------------------+----------------------------------------------------------------------------------------------------------+
| ``public virtual void ParkImmediate()``       | Places the blade at its parked pose without waiting for a wiper cycle.                                   |
+-----------------------------------------------+----------------------------------------------------------------------------------------------------------+

.. _evs-scripting-interior--wiperswitchbinding:

WiperSwitchBinding
~~~~~~~~~~~~~~~~~~

:ref:`WiperSwitchBinding <evs-api-interior--wiperswitchbinding>` gives the full declared contract.

+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Method                                              | Role                                                                                                                                |
+=====================================================+=====================================================================================================================================+
| ``public virtual void Tick(float deltaTime)``       | Advances the declaring presentation/state machine by elapsed seconds; avoid a second call when its built-in owner already ticks it. |
+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Synchronize(bool immediate)`` | Synchronizes presentation/selector state with its source; gearbox synchronization is not a validated driving shift request.         |
+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-scripting-interior--wipers-1:

Wipers
~~~~~~

:ref:`Wipers <evs-api-interior--wipers>` gives the full declared contract.

+---------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Method                                                        | Role                                                                                                                                |
+===============================================================+=====================================================================================================================================+
| ``public override void Configure(VehicleController vehicle)`` | Applies current blade pose only during Play Mode so Edit Mode configuration does not recapture an animated neutral pose.            |
+---------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Tick(float deltaTime)``                 | Advances the declaring presentation/state machine by elapsed seconds; avoid a second call when its built-in owner already ticks it. |
+---------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetRunning(bool value)``                | Requests the wiper running state; stopping finishes the current cycle before parking.                                               |
+---------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Toggle()``                              | Requests the opposite current body/switch/wiper/profile/gear state through the declaring component.                                 |
+---------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetSpeed(float speed)``                 | Changes wiper cycle speed; zero pauses cycle motion.                                                                                |
+---------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void CaptureRestPoses()``                    | Captures rest poses for the wiper geometry owned by the module.                                                                     |
+---------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+

+----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Event / callback                             | Role                                                                                                                      |
+==============================================+===========================================================================================================================+
| ``public event Action<bool> StrokeStarted``  | When a wiper stroke starts. Payload: returning bool, ``true`` for the return stroke and ``false`` for the outward stroke. |
+----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<bool> RunningChanged`` | When the wiper running request changes. Payload: bool; a stop can still finish the current cycle.                         |
+----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<float> SpeedChanged``  | After ``SetSpeed`` changes requested wiper speed. Payload: configured cycle-speed value; zero pauses motion.              |
+----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public event Action Parked``               | When wipers reach their parked state. No payload.                                                                         |
+----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+

.. _evs-scripting-interior--yokeanimator:

YokeAnimator
~~~~~~~~~~~~

:ref:`YokeAnimator <evs-api-interior--yokeanimator>` gives the full declared contract.

+----------------------------------------------+--------------------------------------------------------------------------------------+
| Method                                       | Role                                                                                 |
+==============================================+======================================================================================+
| ``public override void CalibrateRestPose()`` | Captures the model's current neutral presentation frame for later control animation. |
+----------------------------------------------+--------------------------------------------------------------------------------------+
