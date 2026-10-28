.. _evs-scripting-input--command-sampling-and-input-ownership:

Command sampling and input ownership
====================================

The input system translates a player, AI or external producer into one ``Command`` for a vehicle tick. The command describes intent; engine, brakes and steering then resolve that intent into mechanical outputs. A keyboard adapter, an Input System adapter and a network adapter can therefore share the same vehicle mechanics.

The integration has two boundaries: a producer fills a command, and ``VehicleController`` samples the currently selected ``IInput``. Input ownership belongs to the application. Installing several adapters does not define which player, AI or replay should control the vehicle.

.. _evs-scripting-input--implementation-map:

Implementation map
------------------

+------------------------+-------------------------------------------------------------------------+
| Class                  | Responsibility                                                          |
+========================+=========================================================================+
| ``Command``            | Defines axes, action requests and analog/digital channel metadata.      |
+------------------------+-------------------------------------------------------------------------+
| ``InputBuffer``        | Buffers axes and pending one-shot actions for fixed-step consumption.   |
+------------------------+-------------------------------------------------------------------------+
| ``ExternalController`` | Provides the buffered command API for external control.                 |
+------------------------+-------------------------------------------------------------------------+
| ``ActionInput``        | Reads configured Unity Input System actions.                            |
+------------------------+-------------------------------------------------------------------------+
| ``InputGate``          | Controls permission to pass input to the vehicle.                       |
+------------------------+-------------------------------------------------------------------------+
| ``VehicleController``  | Selects ``inputSource``, samples commands and publishes resolved state. |
+------------------------+-------------------------------------------------------------------------+

For adapter setup, see :doc:`Input </Input>`.

.. _evs-scripting-input--sampling-contract:

Sampling contract
-----------------

Render frames and physics ticks do not occur at the same rate. Buffer an action pressed between physics ticks so it survives until the next read, then consume it once. A held axis has different semantics: it remains valid until the producer changes or clears it. Repeating a gear-up action as if it were a held axis can produce several shifts from one button press.

``SubmitCommand`` is appropriate when one producer owns the complete command. Partial producers should agree on composition before submission: replacing a command also replaces metadata and can erase another producer's pending request. Use ``ClearControls()`` at handover boundaries so a retained throttle or queued action cannot leak to the next owner.

``VehicleController`` calls the selected enabled ``IInput`` once per fixed tick. Continuous axes remain until the provider changes/clears them. One-shot gear, lighting, ignition and profile requests must be consumed once.

``InputBuffer`` retains pending commands. ``SubmitCommand`` replaces the entire pending command and its channel masks; ``SetAxes`` changes the axis subset. ``ReadCommand`` sanitizes/clamps values and consumes actions. ``ClearControls`` releases all held values and queued actions.

``InputBuffer`` clears on focus loss and disable. ``ExternalController`` retains commands on focus loss and clears on disable. Neither component implements transport, AI decisions or ownership arbitration.

.. _evs-scripting-input--external-controller-and-runtime-ownership:

External controller and runtime ownership
-----------------------------------------

The example below treats external control as a session. It captures the previous provider, clears stale external values and restores the previous provider only if it still owns the slot. That final check matters when another possession system has legitimately taken control in the meantime.

Call ``Drive`` from the system that produces commands, not from a second vehicle simulation. Releasing the session clears the external buffer even if ownership has already changed, so taking control again starts from released controls.

Attach this component outside the vehicle's inactive hierarchy if it must control possession independently. Assign an enabled ``ExternalController`` owned by the vehicle. Call ``TakeControl``, submit ``Drive`` commands from your producer, and ``ReleaseControl`` when done.

**Example: ``ExternalInputSession.cs``**

.. raw:: html

   <!-- example: ExternalInputSession.cs -->

.. code-block:: csharp

   using UnityEngine;
   using EasyVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class ExternalInputSession : MonoBehaviour
       {
           public VehicleController vehicle;
           public ExternalController external;
           private MonoBehaviour previous;
           private bool ownsInput;

           public void TakeControl()
           {
               if (ownsInput || !vehicle || !external || !external.isActiveAndEnabled) return;
               previous = vehicle.inputSource;
               external.ClearControls();
               vehicle.SetInputSource(external);
               ownsInput = true;
           }

           public void Drive(float throttle, float steering, float brake)
           {
               if (ownsInput && vehicle && vehicle.inputSource == external)
                   external.SetAnalogAxes(throttle, steering, brake);
           }

           public void ReleaseControl()
           {
               if (!ownsInput) return;
               if (external) external.ClearControls();
               if (vehicle && vehicle.inputSource == external)
                   vehicle.SetInputSource(previous ? previous : null);
               ownsInput = false;
           }

           private void OnDisable() => ReleaseControl();
       }
   }

Only the selected provider is read by ``VehicleController``, but other enabled keyboard/demo scripts may have their own side effects. Disable or coordinate those at the application possession boundary. Feed producer data before the controller's fixed tick when it must affect that tick.

.. _evs-scripting-input--progressive-keyboard-braking-and-analog-controllers:

Progressive keyboard braking and analog controllers
---------------------------------------------------

Channel metadata tells mechanics whether an axis already represents a proportional control. A trigger at 25% should remain a proportional brake request; a keyboard key may need a ramp from released to full braking. Marking a digital source as analog bypasses shaping that the driver might expect, while marking an analog pedal as digital can apply unwanted smoothing.

Keep units at the input boundary normalized. Vehicle speed, wheel torque and steering-column degrees are outputs or mechanic settings, not substitutes for command axes. Use the steering conversion API when a physical steering device reports column angle, then submit the resulting input according to the adapter's channel convention.

``AnalogControls`` takes precedence over ``DigitalControls`` for a channel. ``SetAnalogAxes`` marks all channels analog. Analog pedal/steering channels bypass the associated digital shaping: progressive brake ramp, engine throttle smoothing and digital steering assistance. Input Action processors still apply.

Signed throttle allows direction-based driving; independent positive throttle/brake pedals use the selected direction and may overlap. The clutch range is zero connected to one disconnected. Boat steering retains analog magnitude; digital/unspecified steering uses the profile's slew times.

.. _evs-scripting-input--input-action-lifecycle:

Input Action lifecycle
----------------------

With ``PlayerInput``, the adapter resolves references through that player's action asset and leaves action enabling to ``PlayerInput``. Otherwise it enables referenced actions unless configured not to. Shared references are retained until their last owner releases them; actions enabled externally stay enabled. Refresh bindings after editing action references at runtime.

.. _evs-scripting-input--aircraft-keyboard-policy:

Aircraft keyboard policy
------------------------

``KeyboardFlightInput`` retains aircraft throttle, rather than using W/S as throttle. Its wheel-brake binding also controls the retained-throttle brake policy. ``Configure`` that adapter or replace it when using another cockpit convention. Independent analog throttle/brake behavior belongs to ``ActionInput`` and the command metadata, not keyboard polling.

.. _evs-scripting-input--complete-public-method-and-event-index:

Complete public method and event index
--------------------------------------

The lists below cover public methods and events for this topic and their package base contracts. Signatures include overloads. See :doc:`the detailed input and commands API </API/Input>` for arguments, return semantics, state and configuration. An override replaces the matching inherited implementation; it is not an additional call to make.

.. _evs-scripting-input--actioninput:

ActionInput
~~~~~~~~~~~

:ref:`ActionInput <evs-api-input--actioninput>` gives the full declared contract.

+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Method                                                                             | Role                                                                                                      |
+====================================================================================+===========================================================================================================+
| ``[ContextMenu("Refresh action bindings")] public virtual void RefreshBindings()`` | Re-resolves Input System action references, including the selected ``PlayerInput`` action asset.          |
+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``[ContextMenu("Use as vehicle input")] public virtual void UseAsVehicleInput()``  | Selects this action adapter as the vehicle's current input source.                                        |
+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public static Command MergeHover(Command keyboard, Command analog)``             | Combines hover-related adapter input into the current command.                                            |
+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public virtual Command ReadCommand()``                                           | Returns a sanitized sampled command and consumes this provider's pending one-shot actions where buffered. |
+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+

.. _evs-scripting-input--command:

Command
~~~~~~~

:ref:`Command <evs-api-input--command>` gives the full declared contract.

+--------------------------------------------------+----------------------------------------------------------------------------+
| Method                                           | Role                                                                       |
+==================================================+============================================================================+
| ``public bool IsAnalog(InputChannels channel)``  | Checks whether the specified command channel is marked as an analog input. |
+--------------------------------------------------+----------------------------------------------------------------------------+
| ``public bool IsDigital(InputChannels channel)`` | Checks whether the specified command channel is marked as a digital input. |
+--------------------------------------------------+----------------------------------------------------------------------------+

.. _evs-scripting-input--iinput:

IInput
~~~~~~

:ref:`IInput <evs-api-input--iinput>` gives the full declared contract.

+---------------------------+-----------------------------------------------------------------------------------------------------------+
| Method                    | Role                                                                                                      |
+===========================+===========================================================================================================+
| ``Command ReadCommand()`` | Returns a sanitized sampled command and consumes this provider's pending one-shot actions where buffered. |
+---------------------------+-----------------------------------------------------------------------------------------------------------+

.. _evs-scripting-input--imodule:

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

.. _evs-scripting-input--inputbuffer:

InputBuffer
~~~~~~~~~~~

:ref:`InputBuffer <evs-api-input--inputbuffer>` gives the full declared contract.

+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Method                                                                                                         | Role                                                                                                      |
+================================================================================================================+===========================================================================================================+
| ``public virtual void SubmitCommand(Command command)``                                                         | Replaces the pending buffered command, including its channel metadata and action flags.                   |
+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public virtual void ClearControls()``                                                                        | Clears retained axes, channel metadata and pending one-shot input actions.                                |
+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public virtual void SetAxes(float throttle, float steering, float brake = 0, bool handbrake = false)``       | Updates buffered drive-axis values and their input metadata without replacing all pending actions.        |
+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public virtual void SetAnalogAxes(float throttle, float steering, float brake = 0, bool handbrake = false)`` | Sets proportional driving axes and marks the corresponding channels analog.                               |
+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public virtual void SetFlightAxes(float pitch, float roll, float yaw, float lift)``                          | Updates buffered lift/pitch/roll/yaw-related axes using the declared channel metadata.                    |
+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public virtual void SetStrafe(float strafe)``                                                                | Updates the buffered lateral movement axis.                                                               |
+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public virtual void ToggleIgnition()``                                                                       | Queues an ignition toggle for the next sampled command.                                                   |
+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public virtual void ToggleProfile()``                                                                        | Queues a movement-profile toggle for the next sampled command.                                            |
+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public virtual void SetClutch(float pedal)``                                                                 | Sets normalized clutch pedal travel: zero released/connected, one pressed/disconnected.                   |
+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public virtual void SelectGear(int gear)``                                                                   | Queues an explicit gear-selection action in the input buffer.                                             |
+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public virtual void ShiftGear(int direction)``                                                               | Queues a relative up/down gear action in the input buffer.                                                |
+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public virtual void ToggleGearbox()``                                                                        | Queues a transmission-mode toggle in the input buffer.                                                    |
+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public virtual void ToggleHeadlights()``                                                                     | Queues a headlight toggle in the input buffer.                                                            |
+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public virtual void ToggleHighBeams()``                                                                      | Queues a high-beam toggle in the input buffer.                                                            |
+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public virtual void ToggleLeftIndicator()``                                                                  | Queues a left-indicator toggle for the next sampled command.                                              |
+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public virtual void ToggleRightIndicator()``                                                                 | Queues a right-indicator toggle for the next sampled command.                                             |
+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public virtual void ToggleHazards()``                                                                        | Queues a hazard-indicator toggle in the input buffer.                                                     |
+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public virtual void SetIndicators(IndicatorState state)``                                                    | Requests the selected direction/hazard indicator state.                                                   |
+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public virtual Command ReadCommand()``                                                                       | Returns a sanitized sampled command and consumes this provider's pending one-shot actions where buffered. |
+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+

.. _evs-scripting-input--inputgate:

InputGate
~~~~~~~~~

:ref:`InputGate <evs-api-input--inputgate>` gives the full declared contract.

+---------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Method                                                        | Role                                                                                                                 |
+===============================================================+======================================================================================================================+
| ``public override void Configure(VehicleController vehicle)`` | Rebinds ``ConfigurationChanged`` on the current owner, resolves ``ProfileSwitcher`` and refreshes input permissions. |
+---------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Refresh()``                             | Re-evaluates the input gate's configured permission and target input availability.                                   |
+---------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+

.. _evs-scripting-input--inputgateroute:

InputGate.Route
~~~~~~~~~~~~~~~

:ref:`InputGate.Route <evs-api-input--inputgateroute>` gives the full declared contract.

+--------------------------------+------------------------------------------------------------------------+
| Event / callback               | Role                                                                   |
+================================+========================================================================+
| ``public UnityEvent selected`` | Inspector callback when this controller route is selected; no payload. |
+--------------------------------+------------------------------------------------------------------------+

.. _evs-scripting-input--keyboardboatinput:

KeyboardBoatInput
~~~~~~~~~~~~~~~~~

:ref:`KeyboardBoatInput <evs-api-input--keyboardboatinput>` gives the full declared contract.

+------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Method                                   | Role                                                                                                      |
+==========================================+===========================================================================================================+
| ``public virtual Command ReadCommand()`` | Returns a sanitized sampled command and consumes this provider's pending one-shot actions where buffered. |
+------------------------------------------+-----------------------------------------------------------------------------------------------------------+

.. _evs-scripting-input--keyboarddriveinput:

KeyboardDriveInput
~~~~~~~~~~~~~~~~~~

:ref:`KeyboardDriveInput <evs-api-input--keyboarddriveinput>` gives the full declared contract.

+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| Method                                                                  | Role                                                                                                          |
+=========================================================================+===============================================================================================================+
| ``public virtual float AdvanceSteering(float target, float deltaTime)`` | Advances keyboard steering shaping for elapsed time rather than reading a separate mechanical steering state. |
+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| ``public virtual Command ReadCommand()``                                | Returns a sanitized sampled command and consumes this provider's pending one-shot actions where buffered.     |
+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+

.. _evs-scripting-input--keyboardflightinput:

KeyboardFlightInput
~~~~~~~~~~~~~~~~~~~

:ref:`KeyboardFlightInput <evs-api-input--keyboardflightinput>` gives the full declared contract.

+------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Method                                   | Role                                                                                                      |
+==========================================+===========================================================================================================+
| ``public virtual void ResetControls()``  | Clears the flight keyboard adapter's retained control state.                                              |
+------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public virtual Command ReadCommand()`` | Returns a sanitized sampled command and consumes this provider's pending one-shot actions where buffered. |
+------------------------------------------+-----------------------------------------------------------------------------------------------------------+

.. _evs-scripting-input--keyboardsubmarineinput:

KeyboardSubmarineInput
~~~~~~~~~~~~~~~~~~~~~~

:ref:`KeyboardSubmarineInput <evs-api-input--keyboardsubmarineinput>` gives the full declared contract.

+------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Method                                   | Role                                                                                                      |
+==========================================+===========================================================================================================+
| ``public virtual Command ReadCommand()`` | Returns a sanitized sampled command and consumes this provider's pending one-shot actions where buffered. |
+------------------------------------------+-----------------------------------------------------------------------------------------------------------+

.. _evs-scripting-input--module:

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
