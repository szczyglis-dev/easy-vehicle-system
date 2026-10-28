.. _evs-seatsandhandles--seats-and-handles:

Seats and handles
=================

Configure occupants in **VehicleController → Seats**. Each seat has independent hand and foot settings. For character setup and controller selection, see :doc:`Passengers </Passengers>`.

.. _evs-seatsandhandles--bind-a-limb-to-a-control:

Bind a limb to a control
------------------------

1. Add the appropriate handle to the control object: ``SteeringWheelHandle``, ``YokeHandle``, ``JoystickHandle``, ``ThrottleHandle``, ``SwitchHandle``, ``PedalHandle`` or a fixed ``AnchorHandle``.
2. Place its contact anchor within the character's reach. For moving controls, put the neutral motion anchor outside the moving part's hierarchy.
3. Assign the handle to the seat limb's **VehicleHandle** field and select **IK Handle** mode.
4. Configure **Hold** and palm contact for hands, or **Pin To Anchor** and rotation alignment for feet.
5. Preview the seated pose and check the control's full travel.

For a fixed rest without a handle, assign the limb's **Anchor** directly. Keep all targets under the same vehicle.

.. _evs-seatsandhandles--choose-limb-ownership:

Choose limb ownership
---------------------

+-----------+---------------------------------------------------------------------------------------------------+
| Mode      | Use                                                                                               |
+===========+===================================================================================================+
| IK Handle | Follow the assigned handle or direct anchor. Physical hold settings apply to a physical occupant. |
+-----------+---------------------------------------------------------------------------------------------------+
| Animator  | Let animation control that limb.                                                                  |
+-----------+---------------------------------------------------------------------------------------------------+
| Free      | Release IK and vehicle support for that limb.                                                     |
+-----------+---------------------------------------------------------------------------------------------------+

The modes apply independently to both hands and feet. Change a limb's ``mode``, ``handle`` or ``anchor`` at runtime to hand it to another controller. See the :ref:`runtime handover contract <evs-scripting-handles--runtime-handover>` for update timing.

.. _evs-seatsandhandles--fit-a-hand-grip:

Fit a hand grip
---------------

Enable **Adaptive Grip** on a compatible handle and set **Grip Diameter** to the full thickness in metres. Orient the palm anchor to match the control, then run **Preview seated hand grip**. Configure finger mapping and palm calibration on the character; see :doc:`Steering grips </SteeringHandGrip>`.

For steering wheels, choose **Both Hands**, **Left Hand**, **Right Hand** or **Released** in ``gripMode``. Regrip settings control hand repositioning during large rotations.

.. _evs-seatsandhandles--configure-switches-and-pedals:

Configure switches and pedals
-----------------------------

For ``SwitchHandle``, assign the moving pivot, neutral anchor, axis, endpoints and transition duration. Connect its change event to the desired gameplay action. Use ``SwitchAudio`` for a settled-position click.

For ``PedalHandle``, select the input channel, released/pressed angles and travel times. ``useResolvedPedals`` follows the vehicle's resolved accelerator/brake demand. Assign ``contactAnchor`` when a foot should follow the pedal.

To move one foot between accelerator and brake, add ``PedalFootHandle``, assign both pedal handles and a stable transfer target, then bind the seat's foot to it. Set brake thresholds, transfer duration and lift height. Keep the transfer target separate from the moving pedals.

.. _evs-seatsandhandles--temporary-interactions-and-custom-controls:

Temporary interactions and custom controls
------------------------------------------

Use ``HandTransferHandle`` for an out-and-back IK transfer. Use :doc:`ControlInteraction </ControlInteractions>` for a timed action with IK, Animator, Custom or Immediate presentation.

Derive from ``VehicleHandle`` for another control type. The :doc:`handle reference </Scripting/Handles>` describes contact frames, API operations, callbacks and runtime ownership. The :doc:`passenger reference </Scripting/PassengerPhysics>` covers physical restraints and collision settings.
