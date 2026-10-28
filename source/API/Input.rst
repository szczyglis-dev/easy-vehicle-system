.. _evs-api-input--input-and-commands-api:

Input and commands API
======================

Read :doc:`the system explanation </Scripting/Input>` for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from ``MonoBehaviour``, ``Object`` or ``ScriptableObject`` are documented by Unity.

.. _evs-api-input--types:

Types
-----

-  :ref:`ActionInput <evs-api-input--actioninput>`
-  :ref:`Command <evs-api-input--command>`
-  :ref:`ControllerCore <evs-api-input--controllercore>`
-  :ref:`ControllerModule <evs-api-input--controllermodule>`
-  :ref:`ExternalController <evs-api-input--externalcontroller>`
-  :ref:`IInput <evs-api-input--iinput>`
-  :ref:`InputBuffer <evs-api-input--inputbuffer>`
-  :ref:`InputChannels <evs-api-input--inputchannels>`
-  :ref:`InputGate <evs-api-input--inputgate>`
-  :ref:`InputGate.Route <evs-api-input--inputgateroute>`
-  :ref:`InputMode <evs-api-input--inputmode>`
-  :ref:`KeyboardBoatInput <evs-api-input--keyboardboatinput>`
-  :ref:`KeyboardDriveInput <evs-api-input--keyboarddriveinput>`
-  :ref:`KeyboardFlightInput <evs-api-input--keyboardflightinput>`
-  :ref:`KeyboardSubmarineInput <evs-api-input--keyboardsubmarineinput>`

.. _evs-api-input--actioninput:

ActionInput
-----------

**Runtime/Controller/Input/ActionInput.cs**

Reads configured Unity Input System actions.

**Inherits / implements:** :ref:`ControllerModule <evs-api-input--controllermodule>`, :ref:`IInput <evs-api-input--iinput>`.

.. _evs-api-input--methods:

Methods
~~~~~~~

+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                          | Role and behavior                                                                                         | Arguments and result                                                                                                                                                                                                                       |
+====================================================================================+===========================================================================================================+============================================================================================================================================================================================================================================+
| ``[ContextMenu("Refresh action bindings")] public virtual void RefreshBindings()`` | Re-resolves Input System action references, including the selected ``PlayerInput`` action asset.          | No arguments; no returned value.                                                                                                                                                                                                           |
+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``[ContextMenu("Use as vehicle input")] public virtual void UseAsVehicleInput()``  | Selects this action adapter as the vehicle's current input source.                                        | No arguments; no returned value.                                                                                                                                                                                                           |
+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public static Command MergeHover(Command keyboard, Command analog)``             | Combines hover-related adapter input into the current command.                                            | ``keyboard`` — Keyboard, interpreted by this operation in the declared type. ``analog`` — Channel metadata choosing proportional behavior. **Returns:** Returned Command; ownership remains as specified by the creating/lookup operation. |
+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual Command ReadCommand()``                                           | Returns a sanitized sampled command and consumes this provider's pending one-shot actions where buffered. | **Returns:** Returned Command; ownership remains as specified by the creating/lookup operation.                                                                                                                                            |
+------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-input--state-and-configuration:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| Member                                         | Meaning                                                                                                    |
+================================================+============================================================================================================+
| ``public InputActionReference throttle``       | Authored throttle used by ``ActionInput``.                                                                 |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public InputActionReference steering``       | Authored steering used by ``ActionInput``.                                                                 |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public InputActionReference brake``          | Authored brake used by ``ActionInput``.                                                                    |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public InputActionReference pitch``          | Authored pitch used by ``ActionInput``.                                                                    |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public InputActionReference roll``           | Authored roll used by ``ActionInput``.                                                                     |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public InputActionReference yaw``            | Authored yaw used by ``ActionInput``.                                                                      |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public InputActionReference lift``           | Authored lift used by ``ActionInput``.                                                                     |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public InputActionReference strafe``         | Authored strafe used by ``ActionInput``.                                                                   |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public InputActionReference handbrake``      | Authored handbrake used by ``ActionInput``.                                                                |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public InputActionReference ignition``       | Authored ignition used by ``ActionInput``.                                                                 |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public InputActionReference profile``        | Authored profile used by ``ActionInput``.                                                                  |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public InputActionReference clutch``         | Authored clutch used by ``ActionInput``.                                                                   |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public InputActionReference shiftUp``        | Authored shift up used by ``ActionInput``.                                                                 |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public InputActionReference shiftDown``      | Authored shift down used by ``ActionInput``.                                                               |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public InputActionReference reverseGear``    | Authored reverse gear used by ``ActionInput``.                                                             |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public InputActionReference forwardGear``    | Authored forward gear used by ``ActionInput``.                                                             |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public InputActionReference headlights``     | Authored headlights used by ``ActionInput``.                                                               |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public InputActionReference highBeams``      | Authored high beams used by ``ActionInput``.                                                               |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public InputActionReference leftIndicator``  | Authored left indicator used by ``ActionInput``.                                                           |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public InputActionReference rightIndicator`` | Authored right indicator used by ``ActionInput``.                                                          |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public InputActionReference hazards``        | Authored hazards used by ``ActionInput``.                                                                  |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public InputMode throttleMode``              | Authored throttle mode used by ``ActionInput``.                                                            |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public InputMode steeringMode``              | Authored steering mode used by ``ActionInput``.                                                            |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public InputMode brakeMode``                 | Authored brake mode used by ``ActionInput``.                                                               |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public bool useDefaultGamepadBindings``      | Authored use default gamepad bindings used by ``ActionInput``. Initial value: ``true``.                    |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public PlayerInput playerInput``             | Authored player input used by ``ActionInput``.                                                             |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public bool enableReferencedActions``        | Enable referenced actions while this adapter is active. Disable when ``PlayerInput`` owns their lifecycle. |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------+

.. _evs-api-input--command:

Command
-------

**Runtime/Core/Command.cs**

Value type carrying normalized driving axes, pending actions and analog/digital channel metadata.

.. _evs-api-input--methods-1:

Methods
~~~~~~~

+----------------------------------------------------------------------------+----------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                  | Role and behavior                                                          | Arguments and result                                                                                                                                                                                                                                                          |
+============================================================================+============================================================================+===============================================================================================================================================================================================================================================================================+
| ``public Command(float throttle, float steering, bool handbrake = false)`` | Constructs Command with the supplied initial state.                        | ``throttle`` — Normalized propulsion/throttle request. ``steering`` — Normalized steering input, or bool steering participation when declared bool. ``handbrake`` — Handbrake request. Default: ``false``. **Returns:** New instance initialized from the supplied arguments. |
+----------------------------------------------------------------------------+----------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool IsAnalog(InputChannels channel)``                            | Checks whether the specified command channel is marked as an analog input. | ``channel`` — Input/light channel selected by its enum. **Returns:** ``true`` when the described condition holds; ``false`` otherwise.                                                                                                                                        |
+----------------------------------------------------------------------------+----------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool IsDigital(InputChannels channel)``                           | Checks whether the specified command channel is marked as a digital input. | ``channel`` — Input/light channel selected by its enum. **Returns:** ``true`` when the described condition holds; ``false`` otherwise.                                                                                                                                        |
+----------------------------------------------------------------------------+----------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-input--state-and-configuration-1:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| Member                                         | Meaning                                                                                                                            |
+================================================+====================================================================================================================================+
| ``public InputChannels AnalogControls``        | Authored analog controls used by Command.                                                                                          |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public InputChannels DigitalControls``       | Authored digital controls used by Command.                                                                                         |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public float Throttle``                      | Authored throttle used by Command.                                                                                                 |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public float Steering``                      | Signed steering input from minus one to one.                                                                                       |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public float Brake``                         | Normalized service-brake input from zero to one.                                                                                   |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public float Pitch``                         | Signed flight rotation, vertical lift and lateral thrust demands, each from minus one to one.                                      |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public float Roll``                          | Signed flight rotation, vertical lift and lateral thrust demands, each from minus one to one.                                      |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public float Yaw``                           | Signed flight rotation, vertical lift and lateral thrust demands, each from minus one to one.                                      |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public float Lift``                          | Signed flight rotation, vertical lift and lateral thrust demands, each from minus one to one.                                      |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public float Strafe``                        | Signed flight rotation, vertical lift and lateral thrust demands, each from minus one to one.                                      |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool ToggleIgnition``                 | Authored toggle ignition used by Command.                                                                                          |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool ToggleProfile``                  | Authored toggle profile used by Command.                                                                                           |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public float Clutch``                        | Pedal amount: 0 couples the engine, 1 releases the optional clutch. Clutch pedal amount: zero couples and one releases the engine. |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool Handbrake``                      | Authored handbrake used by Command.                                                                                                |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public int? RequestedGear``                  | One-shot gear selection; ``null`` leaves selection unchanged, zero is neutral and minus one is reverse.                            |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public int Shift``                           | One-shot shift direction: minus one down, zero unchanged, plus one up.                                                             |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool ToggleTransmission``             | Authored toggle transmission used by Command.                                                                                      |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool ToggleHeadlights``               | Authored toggle headlights used by Command.                                                                                        |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool ToggleHighBeams``                | Authored toggle high beams used by Command.                                                                                        |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool ToggleHazards``                  | Authored toggle hazards used by Command.                                                                                           |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool ToggleLeftIndicator``            | Authored toggle left indicator used by Command.                                                                                    |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool ToggleRightIndicator``           | Authored toggle right indicator used by Command.                                                                                   |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| ``public IndicatorState? RequestedIndicators`` | Authored requested indicators used by Command.                                                                                     |
+------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-input--controllercore:

ControllerCore
--------------

**Runtime/Controller/Core/ControllerCore.cs**

Configuration/implementation type for controller core within input and commands.

**Inherits / implements:** :ref:`CategoryCore <evs-api-modules--categorycore>`.

.. _evs-api-input--methods-2:

Methods
~~~~~~~

+-----------------------------+----------------------------------------------------------------+--------------------------------------------------------------------+
| Signature                   | Role and behavior                                              | Arguments and result                                               |
+=============================+================================================================+====================================================================+
| ``public ControllerCore()`` | Constructs ``ControllerCore`` with the supplied initial state. | **Returns:** New instance initialized from the supplied arguments. |
+-----------------------------+----------------------------------------------------------------+--------------------------------------------------------------------+

.. _evs-api-input--state-and-configuration-2:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------+--------------------------------------------------------------------------------------+
| Member                                               | Meaning                                                                              |
+======================================================+======================================================================================+
| ``public override ModuleCategory Category { get; }`` | Module responsibility category; it does not independently determine execution phase. |
+------------------------------------------------------+--------------------------------------------------------------------------------------+

.. _evs-api-input--controllermodule:

ControllerModule
----------------

**Runtime/Controller/Core/ControllerModule.cs**

Configuration/implementation type for controller module within input and commands.

**Inherits / implements:** :ref:`Module <evs-api-modules--module>`, :ref:`IControllerModule <evs-api-modules--icontrollermodule>`.

.. _evs-api-input--state-and-configuration-3:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------+--------------------------------------------------------------------------------------+
| Member                                                      | Meaning                                                                              |
+=============================================================+======================================================================================+
| ``public sealed override ModuleCategory Category { get; }`` | Module responsibility category; it does not independently determine execution phase. |
+-------------------------------------------------------------+--------------------------------------------------------------------------------------+

.. _evs-api-input--externalcontroller:

ExternalController
------------------

**Runtime/Controller/Input/ExternalController.cs**

Provides the buffered command API for external control.

**Inherits / implements:** :ref:`InputBuffer <evs-api-input--inputbuffer>`.

.. _evs-api-input--iinput:

IInput
------

**Runtime/Core/Command.cs**

Input-provider contract sampled by the controller for one vehicle tick.

.. _evs-api-input--methods-3:

Methods
~~~~~~~

+---------------------------+-----------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+
| Signature                 | Role and behavior                                                                                         | Arguments and result                                                                            |
+===========================+===========================================================================================================+=================================================================================================+
| ``Command ReadCommand()`` | Returns a sanitized sampled command and consumes this provider's pending one-shot actions where buffered. | **Returns:** Returned Command; ownership remains as specified by the creating/lookup operation. |
+---------------------------+-----------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+

.. _evs-api-input--inputbuffer:

InputBuffer
-----------

**Runtime/Controller/Input/InputBuffer.cs**

Buffers axes and pending one-shot actions for fixed-step consumption.

**Inherits / implements:** :ref:`ControllerModule <evs-api-input--controllermodule>`, :ref:`IInput <evs-api-input--iinput>`.

.. _evs-api-input--methods-4:

Methods
~~~~~~~

+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                                      | Role and behavior                                                                                         | Arguments and result                                                                                                                                                                                                                                             |
+================================================================================================================+===========================================================================================================+==================================================================================================================================================================================================================================================================+
| ``public virtual void SubmitCommand(Command command)``                                                         | Replaces the pending buffered command, including its channel metadata and action flags.                   | ``command`` — Command sampled for this tick; use its channel metadata as well as axes.                                                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ClearControls()``                                                                        | Clears retained axes, channel metadata and pending one-shot input actions.                                | No arguments; no returned value.                                                                                                                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetAxes(float throttle, float steering, float brake = 0, bool handbrake = false)``       | Updates buffered drive-axis values and their input metadata without replacing all pending actions.        | ``throttle`` — Normalized propulsion/throttle request. ``steering`` — Normalized steering input, or bool steering participation when declared bool. ``brake`` — Normalized brake request. Default: ``0``. ``handbrake`` — Handbrake request. Default: ``false``. |
+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetAnalogAxes(float throttle, float steering, float brake = 0, bool handbrake = false)`` | Sets proportional driving axes and marks the corresponding channels analog.                               | ``throttle`` — Normalized propulsion/throttle request. ``steering`` — Normalized steering input, or bool steering participation when declared bool. ``brake`` — Normalized brake request. Default: ``0``. ``handbrake`` — Handbrake request. Default: ``false``. |
+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetFlightAxes(float pitch, float roll, float yaw, float lift)``                          | Updates buffered lift/pitch/roll/yaw-related axes using the declared channel metadata.                    | ``pitch`` — Normalized pitch input, or audio pitch multiplier in an audio operation. ``roll`` — Normalized roll input. ``yaw`` — Normalized yaw input. ``lift`` — Normalized vertical/lift request.                                                              |
+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetStrafe(float strafe)``                                                                | Updates the buffered lateral movement axis.                                                               | ``strafe`` — Normalized lateral request.                                                                                                                                                                                                                         |
+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ToggleIgnition()``                                                                       | Queues an ignition toggle for the next sampled command.                                                   | No arguments; no returned value.                                                                                                                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ToggleProfile()``                                                                        | Queues a movement-profile toggle for the next sampled command.                                            | No arguments; no returned value.                                                                                                                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetClutch(float pedal)``                                                                 | Sets normalized clutch pedal travel: zero released/connected, one pressed/disconnected.                   | ``pedal`` — Selected pedal handle; ``null`` releases a usable foot destination.                                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SelectGear(int gear)``                                                                   | Queues an explicit gear-selection action in the input buffer.                                             | ``gear`` — Signed gear index: -1 reverse, 0 neutral, positive forward.                                                                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ShiftGear(int direction)``                                                               | Queues a relative up/down gear action in the input buffer.                                                | ``direction`` — Direction, interpreted by this operation in the declared type.                                                                                                                                                                                   |
+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ToggleGearbox()``                                                                        | Queues a transmission-mode toggle in the input buffer.                                                    | No arguments; no returned value.                                                                                                                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ToggleHeadlights()``                                                                     | Queues a headlight toggle in the input buffer.                                                            | No arguments; no returned value.                                                                                                                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ToggleHighBeams()``                                                                      | Queues a high-beam toggle in the input buffer.                                                            | No arguments; no returned value.                                                                                                                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ToggleLeftIndicator()``                                                                  | Queues a left-indicator toggle for the next sampled command.                                              | No arguments; no returned value.                                                                                                                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ToggleRightIndicator()``                                                                 | Queues a right-indicator toggle for the next sampled command.                                             | No arguments; no returned value.                                                                                                                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ToggleHazards()``                                                                        | Queues a hazard-indicator toggle in the input buffer.                                                     | No arguments; no returned value.                                                                                                                                                                                                                                 |
+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetIndicators(IndicatorState state)``                                                    | Requests the selected direction/hazard indicator state.                                                   | ``state`` — State, interpreted by this operation in the declared type.                                                                                                                                                                                           |
+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual Command ReadCommand()``                                                                       | Returns a sanitized sampled command and consumes this provider's pending one-shot actions where buffered. | **Returns:** Returned Command; ownership remains as specified by the creating/lookup operation.                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-input--state-and-configuration-4:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------+------------------------------------------------------------------------------------------------------------+
| Member                                   | Meaning                                                                                                    |
+==========================================+============================================================================================================+
| ``public InputChannels analogControls``  | Mark analog axes to bypass digital shaping. ``SetAnalogAxes`` marks all channels for raw controller input. |
+------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public InputChannels digitalControls`` | Mark button-driven axes here to opt into keyboard assistance such as progressive braking.                  |
+------------------------------------------+------------------------------------------------------------------------------------------------------------+

.. _evs-api-input--inputchannels:

InputChannels
-------------

**Runtime/Core/Command.cs**

Defines the allowed input channels choices used by this topic.

.. _evs-api-input--values:

Values
~~~~~~

-  ``None = 0``
-  ``Throttle = 1``
-  ``Steering = 2``
-  ``Brake = 4``
-  ``Clutch = 8``
-  ``Flight = 16``
-  ``All = Throttle \| Steering \| Brake \| Clutch \| Flight``

.. _evs-api-input--inputgate:

InputGate
---------

**Runtime/Controller/Input/InputGate.cs**

Controls permission to pass input to the vehicle.

**Inherits / implements:** :ref:`ControllerModule <evs-api-input--controllermodule>`.

.. _evs-api-input--methods-5:

Methods
~~~~~~~

+---------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+
| Signature                                                     | Role and behavior                                                                                                    | Arguments and result                                         |
+===============================================================+======================================================================================================================+==============================================================+
| ``public override void Configure(VehicleController vehicle)`` | Rebinds ``ConfigurationChanged`` on the current owner, resolves ``ProfileSwitcher`` and refreshes input permissions. | ``vehicle`` — Vehicle context/owner receiving the operation. |
+---------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+
| ``public virtual void Refresh()``                             | Re-evaluates the input gate's configured permission and target input availability.                                   | No arguments; no returned value.                             |
+---------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------+

.. _evs-api-input--state-and-configuration-5:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------+---------------------------------------------------------------------------------+
| Member                    | Meaning                                                                         |
+===========================+=================================================================================+
| ``public Route[] routes`` | Authored routes used by ``InputGate``. Initial value: ``Array.Empty<Route>()``. |
+---------------------------+---------------------------------------------------------------------------------+

.. _evs-api-input--inputgateroute:

InputGate.Route
---------------

**Runtime/Controller/Input/InputGate.cs**

Controller routing configuration and its selection callback.

.. _evs-api-input--events-and-inspector-callbacks:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------+------------------------------------------------------------------------+
| Declaration                    | Trigger, payload and meaning                                           |
+================================+========================================================================+
| ``public UnityEvent selected`` | Inspector callback when this controller route is selected; no payload. |
+--------------------------------+------------------------------------------------------------------------+

.. _evs-api-input--state-and-configuration-6:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| Member                         | Meaning                                                                                                                      |
+================================+==============================================================================================================================+
| ``public string profileId``    | Case-sensitive registration ID in the vehicle ProfileSwitcher. Select this route when its registered profile becomes active. |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------+
| ``public MonoBehaviour input`` | Authored input used by Route.                                                                                                |
+--------------------------------+------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-input--inputmode:

InputMode
---------

**Runtime/Controller/Input/ActionInput.cs**

Defines the allowed input mode choices used by this topic.

.. _evs-api-input--values-1:

Values
~~~~~~

-  ``Auto``
-  ``Analog``
-  ``Digital``

.. _evs-api-input--keyboardboatinput:

KeyboardBoatInput
-----------------

**Runtime/Controller/Input/Samples/KeyboardBoatInput.cs**

Configuration/implementation type for keyboard boat input within input and commands.

**Inherits / implements:** :ref:`ControllerModule <evs-api-input--controllermodule>`, :ref:`IInput <evs-api-input--iinput>`.

.. _evs-api-input--methods-6:

Methods
~~~~~~~

+------------------------------------------+-----------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+
| Signature                                | Role and behavior                                                                                         | Arguments and result                                                                            |
+==========================================+===========================================================================================================+=================================================================================================+
| ``public virtual Command ReadCommand()`` | Returns a sanitized sampled command and consumes this provider's pending one-shot actions where buffered. | **Returns:** Returned Command; ownership remains as specified by the creating/lookup operation. |
+------------------------------------------+-----------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+

.. _evs-api-input--state-and-configuration-7:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------+--------------------------------------------------------------------------------------------------------------+
| Member                             | Meaning                                                                                                      |
+====================================+==============================================================================================================+
| ``public Key ignitionKey``         | Authored ignition key used by ``KeyboardBoatInput``. Initial value: ``Key.I``.                               |
+------------------------------------+--------------------------------------------------------------------------------------------------------------+
| ``public Key profileKey``          | Authored profile key used by ``KeyboardBoatInput``. Initial value: ``Key.B``.                                |
+------------------------------------+--------------------------------------------------------------------------------------------------------------+
| ``public ActionInput analogInput`` | Gamepad/joystick adapter. Created automatically if unassigned; custom Action references remain configurable. |
+------------------------------------+--------------------------------------------------------------------------------------------------------------+

.. _evs-api-input--keyboarddriveinput:

KeyboardDriveInput
------------------

**Runtime/Controller/Input/Samples/KeyboardDriveInput.cs**

Configuration/implementation type for keyboard drive input within input and commands.

**Inherits / implements:** :ref:`ControllerModule <evs-api-input--controllermodule>`, :ref:`IInput <evs-api-input--iinput>`.

.. _evs-api-input--methods-7:

Methods
~~~~~~~

+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                               | Role and behavior                                                                                             | Arguments and result                                                                                                                                                                                                  |
+=========================================================================+===============================================================================================================+=======================================================================================================================================================================================================================+
| ``public virtual float AdvanceSteering(float target, float deltaTime)`` | Advances keyboard steering shaping for elapsed time rather than reading a separate mechanical steering state. | ``target`` — Configured target object/point; see declared type and owner. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. **Returns:** Computed float in the operation's documented unit/domain. |
+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual Command ReadCommand()``                                | Returns a sanitized sampled command and consumes this provider's pending one-shot actions where buffered.     | **Returns:** Returned Command; ownership remains as specified by the creating/lookup operation.                                                                                                                       |
+-------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-input--state-and-configuration-8:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------+----------------------------------------------------------------------------------------+
| Member                                                              | Meaning                                                                                |
+=====================================================================+========================================================================================+
| ``public float steeringRiseTime``                                   | Authored steering rise time used by ``KeyboardDriveInput``. Initial value: ``.25f``.   |
+---------------------------------------------------------------------+----------------------------------------------------------------------------------------+
| ``public float steeringReturnTime``                                 | Authored steering return time used by ``KeyboardDriveInput``. Initial value: ``.12f``. |
+---------------------------------------------------------------------+----------------------------------------------------------------------------------------+
| ``public Key ignitionKey``                                          | Authored ignition key used by ``KeyboardDriveInput``. Initial value: ``Key.I``.        |
+---------------------------------------------------------------------+----------------------------------------------------------------------------------------+
| ``public Key profileKey``                                           | Authored profile key used by ``KeyboardDriveInput``. Initial value: ``Key.B``.         |
+---------------------------------------------------------------------+----------------------------------------------------------------------------------------+
| ``public virtual float SmoothedSteering { get; }``                  | Read-only/resolved smoothed steering for ``KeyboardDriveInput``.                       |
+---------------------------------------------------------------------+----------------------------------------------------------------------------------------+
| ``public virtual bool ReserveVehicleSelectionDigits { get; set; }`` | Configurable reserve vehicle selection digits for ``KeyboardDriveInput``.              |
+---------------------------------------------------------------------+----------------------------------------------------------------------------------------+
| ``public virtual bool NumpadNavigationActive { get; set; }``        | Reserves numeric keypad controls for camera movement rather than vehicle actions.      |
+---------------------------------------------------------------------+----------------------------------------------------------------------------------------+

.. _evs-api-input--keyboardflightinput:

KeyboardFlightInput
-------------------

**Runtime/Controller/Input/Samples/KeyboardFlightInput.cs**

Configuration/implementation type for keyboard flight input within input and commands.

**Inherits / implements:** :ref:`ControllerModule <evs-api-input--controllermodule>`, :ref:`IInput <evs-api-input--iinput>`.

.. _evs-api-input--methods-8:

Methods
~~~~~~~

+------------------------------------------+-----------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+
| Signature                                | Role and behavior                                                                                         | Arguments and result                                                                            |
+==========================================+===========================================================================================================+=================================================================================================+
| ``public virtual void ResetControls()``  | Clears the flight keyboard adapter's retained control state.                                              | No arguments; no returned value.                                                                |
+------------------------------------------+-----------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+
| ``public virtual Command ReadCommand()`` | Returns a sanitized sampled command and consumes this provider's pending one-shot actions where buffered. | **Returns:** Returned Command; ownership remains as specified by the creating/lookup operation. |
+------------------------------------------+-----------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+

.. _evs-api-input--state-and-configuration-9:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Member                                                       | Meaning                                                                                                                     |
+==============================================================+=============================================================================================================================+
| ``public virtual bool CameraNavigationActive { get; set; }`` | Configurable camera navigation active for ``KeyboardFlightInput``.                                                          |
+--------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``public float throttleChangeRate``                          | Airplane throttle change per second while holding increase/decrease keys.                                                   |
+--------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``public Key airplaneBrakeKey``                              | Authored airplane brake key used by ``KeyboardFlightInput``. Initial value: ``Key.Space``.                                  |
+--------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``public ActionInput analogInput``                           | Hover/airplane gamepad/joystick adapter. Created automatically if unassigned; custom Action references remain configurable. |
+--------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``public float airplaneThrottle``                            | Authored airplane throttle used by ``KeyboardFlightInput``.                                                                 |
+--------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-input--keyboardsubmarineinput:

KeyboardSubmarineInput
----------------------

**Runtime/Controller/Input/Samples/KeyboardSubmarineInput.cs**

Configuration/implementation type for keyboard submarine input within input and commands.

**Inherits / implements:** :ref:`ControllerModule <evs-api-input--controllermodule>`, :ref:`IInput <evs-api-input--iinput>`.

.. _evs-api-input--methods-9:

Methods
~~~~~~~

+------------------------------------------+-----------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+
| Signature                                | Role and behavior                                                                                         | Arguments and result                                                                            |
+==========================================+===========================================================================================================+=================================================================================================+
| ``public virtual Command ReadCommand()`` | Returns a sanitized sampled command and consumes this provider's pending one-shot actions where buffered. | **Returns:** Returned Command; ownership remains as specified by the creating/lookup operation. |
+------------------------------------------+-----------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+

.. _evs-api-input--state-and-configuration-10:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+
| Member                                                       | Meaning                                                                                                      |
+==============================================================+==============================================================================================================+
| ``public virtual bool CameraNavigationActive { get; set; }`` | Configurable camera navigation active for ``KeyboardSubmarineInput``.                                        |
+--------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+
| ``public Key ignitionKey``                                   | Authored ignition key used by ``KeyboardSubmarineInput``. Initial value: ``Key.I``.                          |
+--------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+
| ``public Key profileKey``                                    | Authored profile key used by ``KeyboardSubmarineInput``. Initial value: ``Key.B``.                           |
+--------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+
| ``public ActionInput analogInput``                           | Gamepad/joystick adapter. Created automatically if unassigned; custom Action references remain configurable. |
+--------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+
