.. _evs-input--input-setup:

Input setup
===========

Assign a component implementing ``IInput`` to VehicleController's input source. Built-in adapters support keyboard, Input Actions and externally supplied commands. For the supplied scene's keyboard bindings, see :doc:`Demo </Demo>`.

.. _evs-input--input-actions-and-gamepads:

Input Actions and gamepads
--------------------------

1. Add ``ActionInput`` and choose **Use as vehicle input**, or assign it as the controller's input source.
2. Use the built-in gamepad bindings or assign your own ``InputActionReference`` fields.
3. Use **Value / Axis** actions for pedals and steering. Pedals use 0..1; steering uses -1..1. A Vector2 source reads X for steering and Y for throttle.
4. Choose Auto, Analog or Digital per axis. Auto detects standard keyboard/buttons and analog controls.
5. If using ``PlayerInput``, assign it so references resolve against that player's action asset.

======================= =========================
Action                  Built-in gamepad binding
======================= =========================
Throttle / brake        Right / left trigger
Steering                Left stick X
Handbrake               West face button
Reverse / forward       North / south face button
Shift up / down         Right / left shoulder
Ignition / profile      Start / Select
Clutch                  Left-stick press
Headlights / high beams D-pad up / down
Indicators              D-pad left / right
Hazards                 Right-stick press
======================= =========================

Use **Refresh action bindings** after changing references during play. Configure action enabling and shared ownership as described in the :doc:`input reference </Scripting/Input>`.

.. _evs-input--digital-and-analog-response:

Digital and analog response
---------------------------

Use ``Brakes.progressiveDigitalBraking`` and ``brakeRiseTime`` for a gradual digital brake response. Analog channels preserve continuous pedal/steering values. Configure deadzones and processors in the Input Action asset.

For custom providers, mark continuous axes in ``Command.AnalogControls`` and buttons in ``DigitalControls``. Use ``InputBuffer.SetAnalogAxes`` for analog commands. See the :ref:`channel policy <evs-scripting-input--progressive-keyboard-braking-and-analog-controllers>` for the corresponding mechanical response.

.. _evs-input--ai-replay-and-external-control:

AI, replay and external control
-------------------------------

Use ``InputBuffer`` or ``ExternalController`` to submit axes and one-shot actions. Select it with ``vehicle.SetInputSource(source)`` and call ``ClearControls()`` when the producer disconnects or relinquishes control. ``SetInputSource(null)`` releases the source.

The :ref:`input reference <evs-scripting-input--external-controller-and-runtime-ownership>` includes a source handover example and describes retained commands, focus behavior and sampling. :doc:`Scripting </Scripting>` lists command and event APIs.
