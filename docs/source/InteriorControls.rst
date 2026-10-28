.. _evs-interiorcontrols--cockpit-controls-and-instruments:

Cockpit controls and instruments
================================

For km/h, mph or m/s authoring and readouts, see :doc:`Speed units </SpeedUnits>`.

Use animators and value sources to present mechanical state on the model. Use a binding or interaction when operating a control should request a gameplay action.

.. _evs-interiorcontrols--prepare-moving-geometry:

Prepare moving geometry
-----------------------

Create an independent neutral anchor at the actual hinge/needle center. Assign the moving part and local axis; keep mesh import offsets on children. The neutral anchor must be outside the moving part's hierarchy. Check the full range before adding hand targets.

.. _evs-interiorcontrols--add-an-rpm-or-speed-needle:

Add an RPM or speed needle
--------------------------

1. Add InstrumentNeedle to the instrument.
2. Set the physical value range and corresponding angle range.
3. Add EngineRpmSource or SpeedValueSource and assign its engine/vehicle.
4. Drag that source into the needle Source field.
5. Set Response for the desired visual smoothing and check idle, acceleration and return.

Use RotaryHandle for another knob/gauge with the same range mapping. For a custom value such as fuel, see the :ref:`value-source example <evs-scripting-interior--add-a-fuel-needle-source>`.

.. _evs-interiorcontrols--animate-a-gear-paddle:

Animate a gear paddle
---------------------

Add GearPaddleHandle to the moving mesh, choose Up/Down/Both and set press/return angles and durations. Add GearShiftBinding to the vehicle and assign the Engine and handles. Accepted gear changes then animate the paddle.

Pressing the visual paddle alone does not select a gear. Connect the input action to a gearbox request, then let the binding show the accepted result.

.. _evs-interiorcontrols--bind-a-switch:

Bind a switch
-------------

Choose a SwitchHandle and configure its endpoints/detents. Add the relevant binding:

+-----------------------------------+------------------------------------------------------------+
| Switch purpose                    | Binding                                                    |
+===================================+============================================================+
| Turn indicators                   | IndicatorSwitchBinding for directional indicators          |
+-----------------------------------+------------------------------------------------------------+
| Wipers                            | WiperSwitchBinding                                         |
+-----------------------------------+------------------------------------------------------------+
| Any two registered drive profiles | ProfileSwitchBinding with On Profile Id and Off Profile Id |
+-----------------------------------+------------------------------------------------------------+
| Application action                | ControlInteraction or your own event binding               |
+-----------------------------------+------------------------------------------------------------+

Configure three-position endpoints for a stalk with Negative/Neutral/Positive positions. Verify external state changes also synchronize the visible control.

See :doc:`Seats and handles </SeatsAndHandles>` for hand/foot contact and :doc:`interior reference </Scripting/Interior>` for value, event and synchronization contracts.
