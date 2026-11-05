.. _evs-inspectorreference-interior--interior-controls-and-instruments:

Interior controls and instruments
=================================

:doc:`Back to the complete Inspector reference </InspectorReference>`.

In the controller’s Interior group, **Animators** animate cockpit controls/instruments and connect data sources; **Handles** connect controls to passenger hand/foot grips and IK targets. Both groups include short descriptions and header tooltips.

+---------------------------------------------------------------------------------------------------------------+------------------------+
| Component or data block                                                                                       | Settings declared here |
+===============================================================================================================+========================+
| :ref:`AircraftHud <evs-inspectorreference-interior--aircrafthud>`                                             | 5                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`AnchoredControlAnimator <evs-inspectorreference-interior--anchoredcontrolanimator>`                     | 7                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`AnchoredRotation <evs-inspectorreference-interior--anchoredrotation>`                                   | 3                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`CarHud <evs-inspectorreference-interior--carhud>`                                                       | 6                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`ClutchSource <evs-inspectorreference-interior--clutchsource>`                                           | 0                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`CommandValueSource <evs-inspectorreference-interior--commandvaluesource>`                               | 1                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`ControlAnimator <evs-inspectorreference-interior--controlanimator>`                                     | 4                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`ControlInteraction <evs-inspectorreference-interior--controlinteraction>`                               | 15                     |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`ControlInteractionAnimationEvents <evs-inspectorreference-interior--controlinteractionanimationevents>` | 1                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`EngineRpmSource <evs-inspectorreference-interior--enginerpmsource>`                                     | 1                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`GasSource <evs-inspectorreference-interior--gassource>`                                                 | 2                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`GearLeverAnimator <evs-inspectorreference-interior--gearleveranimator>`                                 | 8                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`GearLeverPosition <evs-inspectorreference-interior--gearleverposition>`                                 | 3                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`GearPaddleAnimator <evs-inspectorreference-interior--gearpaddleanimator>`                               | 7                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`GearShiftAnimator <evs-inspectorreference-interior--gearshiftanimator>`                                 | 3                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`GearShiftDirection <evs-inspectorreference-interior--gearshiftdirection>`                               | 0                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`HandbrakeSource <evs-inspectorreference-interior--handbrakesource>`                                     | 0                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`HandleMotion <evs-inspectorreference-interior--handlemotion>`                                           | 6                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`IGearShiftAnimator <evs-inspectorreference-interior--igearshiftanimator>`                               | 0                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`IndicatorSwitchBinding <evs-inspectorreference-interior--indicatorswitchbinding>`                       | 3                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`InstrumentNeedle <evs-inspectorreference-interior--instrumentneedle>`                                   | 0                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`InteriorDataSourceAttribute <evs-inspectorreference-interior--interiordatasourceattribute>`             | 0                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`InteriorModule <evs-inspectorreference-interior--interiormodule>`                                       | 0                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`InteriorValueSource <evs-inspectorreference-interior--interiorvaluesource>`                             | 0                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`PedalAnimator <evs-inspectorreference-interior--pedalanimator>`                                         | 8                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`PitchSource <evs-inspectorreference-interior--pitchsource>`                                             | 0                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`ProfileSwitchBinding <evs-inspectorreference-interior--profileswitchbinding>`                           | 5                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`RearMirror <evs-inspectorreference-interior--rearmirror>`                                               | 14                     |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`RearMirrors <evs-inspectorreference-interior--rearmirrors>`                                             | 4                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`RollSource <evs-inspectorreference-interior--rollsource>`                                               | 1                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`RotaryAnimator <evs-inspectorreference-interior--rotaryanimator>`                                       | 9                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`ServiceBrakeSource <evs-inspectorreference-interior--servicebrakesource>`                               | 1                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`SpeedValueSource <evs-inspectorreference-interior--speedvaluesource>`                                   | 3                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`SteeringSource <evs-inspectorreference-interior--steeringsource>`                                       | 1                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`SteeringStickAnimator <evs-inspectorreference-interior--steeringstickanimator>`                         | 14                     |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`SteeringWheelAnimator <evs-inspectorreference-interior--steeringwheelanimator>`                         | 8                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`SwitchAnimator <evs-inspectorreference-interior--switchanimator>`                                       | 8                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`SwitchPosition <evs-inspectorreference-interior--switchposition>`                                       | 0                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`ThrottleAnimator <evs-inspectorreference-interior--throttleanimator>`                                   | 8                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`TwistThrottleAnimator <evs-inspectorreference-interior--twistthrottleanimator>`                         | 0                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`VehicleHandleAnimator <evs-inspectorreference-interior--vehiclehandleanimator>`                         | 1                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`VehicleValueSource <evs-inspectorreference-interior--vehiclevaluesource>`                               | 1                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+
| :ref:`YokeAnimator <evs-inspectorreference-interior--yokeanimator>`                                           | 5                      |
+---------------------------------------------------------------------------------------------------------------+------------------------+

.. _evs-inspectorreference-interior--aircrafthud:

AircraftHud
-----------

Configuration/implementation type for aircraft hud within cockpit instruments and bindings.

**Source:** ``Runtime/Interior/Render/AircraftHud.cs``. Component / asset.

**Inherited settings:** :ref:`InteriorModule <evs-inspectorreference-interior--interiormodule>`. These settings also appear on this type.

+---------------------+----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting             | Type                                                                                         | Description                                                                                                                                                         | Declared default and constraints |
+=====================+==============================================================================================+=====================================================================================================================================================================+==================================+
| ``cockpitSurface``  | ``Renderer``                                                                                 | Screen mesh receiving the flight-display texture through its material property block. Assign the display face rather than the whole cockpit renderer when possible. | ``None / unassigned``            |
+---------------------+----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``customTexture``   | ``Texture``                                                                                  | Fixed texture displayed instead of drawing the generated flight HUD. Leave empty to show live vehicle readouts.                                                     | ``None / unassigned``            |
+---------------------+----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``refreshRate``     | ``float``                                                                                    | Maximum times per second the generated flight display redraws. Lower values save work but make readout changes less smooth.                                         | ``15``; Range: 1 to 30           |
+---------------------+----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``textureProperty`` | ``string``                                                                                   | Shader texture slot on the cockpit screen that receives the HUD image. Use the exact property name exposed by the screen material's shader.                         | ``"_BaseMap"``                   |
+---------------------+----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``vehicle``         | ``VehicleController`` (:ref:`fields <evs-inspectorreference-controller--vehiclecontroller>`) | Aircraft supplying speed, attitude and other flight readouts. If empty, the display initially binds to a VehicleController in its parent hierarchy.                 | ``None / unassigned``            |
+---------------------+----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _evs-inspectorreference-interior--anchoredcontrolanimator:

AnchoredControlAnimator
-----------------------

**Source:** ``Runtime/Interior/Animators/AnchoredControlAnimator.cs``. Component configuration.

**Inherited settings:** ``ControlAnimator``.

+---------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Setting             | Type                  | Meaning                                                                                                                                                             |
+=====================+=======================+=====================================================================================================================================================================+
| ``motion``          | ``AnchoredRotation``  | Animator-owned moving geometry, independent pivot/reference, axis and travel mapping. Parent the IK contact under the moving geometry.                              |
+---------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``onValueChanged``  | ``UnityEvent<float>`` | After this control's value changes. Payload: the event's value type; ``PedalAnimator`` reports displayed travel, ``SwitchAnimator`` reports a changed bool request. |
+---------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``pressDuration``   | ``float``             | Seconds for full released-to-pressed travel; smaller demands stop proportionally earlier.                                                                           |
+---------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``pressedAngle``    | ``float``             | Pedal angle in degrees at displayed value one.                                                                                                                      |
+---------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``releasedAngle``   | ``float``             | Pedal angle in degrees at displayed value zero.                                                                                                                     |
+---------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``releaseDuration`` | ``float``             | Seconds to fade after releasing the request; zero stops immediately.                                                                                                |
+---------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**AnchoredControlAnimator data source:** ``dataSource`` — Optional component implementing IInteriorValueSource. Overrides built-in sampling; any application MonoBehaviour can implement the interface. An assigned disabled, invalid or non-finite source produces zero. Empty uses the documented built-in default (Rotary remains API-driven).

.. _evs-inspectorreference-interior--anchoredrotation:

AnchoredRotation
----------------

Preserves a neutral pose relative to an independent pivot frame.

**Source:** ``Runtime/Interior/Controls/AnchoredRotation.cs``. Nested configuration data; expand its owning field in the Inspector.

+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting        | Type          | Description                                                                                                                                            | Declared default and constraints |
+================+===============+========================================================================================================================================================+==================================+
| ``anchor``     | ``Transform`` | Fixed transform defining the rotation centre and axes. It cannot be the moving mesh or its child, otherwise the hinge would move with the part.        | ``None / unassigned``            |
+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``localAxis``  | ``Vector3``   | Hinge direction in Anchor's local coordinates. The mesh rotates around this axis through the anchor position, even if its imported pivot is elsewhere. | ``Vector3.right``                |
+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``movingPart`` | ``Transform`` | Mesh rotated around the independent anchor, retaining its captured offset from the hinge. Its own imported pivot does not have to lie on the hinge.    | ``None / unassigned``            |
+----------------+---------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _evs-inspectorreference-interior--carhud:

CarHud
------

Configuration/implementation type for car hud within cockpit instruments and bindings.

**Source:** ``Runtime/Interior/Render/CarHud.cs``. Component / asset.

**Inherited settings:** :ref:`InteriorModule <evs-inspectorreference-interior--interiormodule>`. These settings also appear on this type.

+---------------------+----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting             | Type                                                                                         | Description                                                                                                                                                                             | Declared default and constraints |
+=====================+==============================================================================================+=========================================================================================================================================================================================+==================================+
| ``cockpitSurface``  | ``Renderer``                                                                                 | Dashboard screen renderer receiving the display texture. The configured Texture Property must exist in its material's shader.                                                           | ``None / unassigned``            |
+---------------------+----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``customTexture``   | ``Texture``                                                                                  | Texture replacing the generated dashboard readout. Leave empty for live speed, fuel and warning indicators.                                                                             | ``None / unassigned``            |
+---------------------+----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``refreshRate``     | ``float``                                                                                    | Maximum dashboard image redraws per second. Reduce for cheaper small screens; increase for smoother live needles/readouts.                                                              | ``10``; Range: 1 to 30           |
+---------------------+----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``speedUnit``       | ``SpeedUnit``                                                                                | Unit used for the dashboard's speed readout. Switching between km/h, mph and m/s changes the numbers, not the vehicle's physical speed. Options: ``Kph``, ``Mph``, ``MetresPerSecond``. | ``SpeedUnit.Kph``                |
+---------------------+----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``textureProperty`` | ``string``                                                                                   | Shader texture slot receiving the generated dashboard image or Custom Texture. A wrong property name leaves the screen material unchanged.                                              | ``"_BaseMap"``                   |
+---------------------+----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``vehicle``         | ``VehicleController`` (:ref:`fields <evs-inspectorreference-controller--vehiclecontroller>`) | Vehicle supplying speed, fuel, lights and assist indicators to the dashboard screen. If empty, the display initially finds a parent VehicleController.                                  | ``None / unassigned``            |
+---------------------+----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _evs-inspectorreference-interior--clutchsource:

ClutchSource
------------

**Source:** ``Runtime/Interior/Controls/Source/ClutchSource.cs``. Samples Command.Clutch (0..1).

+-------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Field       | Type                  | Meaning                                                                                                                                       |
+=============+=======================+===============================================================================================================================================+
| ``vehicle`` | ``VehicleController`` | Vehicle supplying presentation values. When unassigned, resolves the nearest parent VehicleController, allowing a source beside its animator. |
+-------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-inspectorreference-interior--commandvaluesource:

CommandValueSource
------------------

**Source:** ``Runtime/Interior/Controls/Source/CommandValueSource.cs``. Samples a selected Command channel, without resolved actuator mapping.

+-------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Field       | Type                  | Meaning                                                                                                                                       |
+=============+=======================+===============================================================================================================================================+
| ``input``   | ``HandleInput``       | Command channel to sample through HandleCommandInput.                                                                                         |
+-------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``vehicle`` | ``VehicleController`` | Vehicle supplying presentation values. When unassigned, resolves the nearest parent VehicleController, allowing a source beside its animator. |
+-------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-inspectorreference-interior--controlanimator:

ControlAnimator
---------------

**Source:** ``Runtime/Interior/Animators/ControlAnimator.cs``. Shared control presentation base. It references an optional IK handle, coordinates real limb arrival and owns Wait For Handle / Fake Sync Handle Motion. It does not act as an IK target.

**Inherited settings:** ``VehicleHandleAnimator``.

+--------------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Setting                  | Type              | Meaning                                                                                                                                                                                 |
+==========================+===================+=========================================================================================================================================================================================+
| ``fakeSyncHandleMotion`` | ``bool``          | Default false. Outbound reach uses the contact pose captured before visual motion; after arrival it follows the live anchor.                                                            |
+--------------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``handle``               | ``VehicleHandle`` | Optional IK contact for this animated control. Set its anchor on the moving grip and author limb/pose settings on that component. An unassigned handle permits immediate visual motion. |
+--------------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``showGizmos``           | ``bool``          | Shows this component’s scene guides and editing handles. Enabled by default; Inspector: **Gizmos > Show gizmos**. Does not change gameplay or physics.                                  |
+--------------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``waitForHandle``        | ``bool``          | Default true. Wait for the real palm/foot within 2.5 cm after transit, plus finger blending for hands. Mechanics remain immediate; steering is excluded.                                |
+--------------------------+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-inspectorreference-interior--controlinteraction:

ControlInteraction
------------------

``Started``, ``Commit``, ``Completed`` and ``Cancelled``

**Source:** ``Runtime/Interior/Controls/ControlInteraction.cs``. Component / asset.

+------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting                            | Type                                                                            | Description                                                                                                                                                                                                                                                                           | Declared default and constraints |
+====================================+=================================================================================+=======================================================================================================================================================================================================================================================================================+==================================+
| ``animationEvents``                | ``bool``                                                                        | Use Animation Events to call Commit and Complete instead of elapsed time.                                                                                                                                                                                                             | ``false``                        |
+------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``animationLayer``                 | ``string``                                                                      | Optional layer name temporarily enabled for the gesture. Empty preserves controller weights. Put the gesture trigger transition on that layer.                                                                                                                                        | ``""``                           |
+------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``animationLayerWeight``           | ``float``                                                                       | Temporary weight of Animation Layer. Completion/cancellation restores its previous weight unless another system changed it.                                                                                                                                                           | ``1``; Range: 0–1                |
+------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``animator``                       | ``Animator``                                                                    | Optional override. Otherwise use the current occupant's SeatedAnimator.                                                                                                                                                                                                               | ``None / unassigned``            |
+------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``commitTime``                     | ``float``                                                                       | Seconds from animation start until the control action is committed when timed commit is used. Set it to the moment the hand visibly presses or moves the control.                                                                                                                     | ``.25``; Minimum: 0              |
+------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``customDriver``                   | ``MonoBehaviour``                                                               | A MonoBehaviour implementing IControlInteractionDriver.                                                                                                                                                                                                                               | ``None / unassigned``            |
+------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``duration``                       | ``float``                                                                       | Total timed animation interaction length in seconds. After both this duration and Commit Time have elapsed, the sequence can complete and restore hand control.                                                                                                                       | ``.7``; Minimum: 0               |
+------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``hand``                           | ``PassengerBodyPart``                                                           | Hand used for the interaction. Choose LeftHand or RightHand; foot selections are not accepted by this hand-interaction sequence. Options: ``LeftHand``, ``RightHand``, ``LeftFoot``, ``RightFoot``.                                                                                   | ``PassengerBodyPart.LeftHand``   |
+------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``keepHandOnTargetWhileAnimating`` | ``bool``                                                                        | IK then Animator: retain the hand target and existing IK/physical arm support while a layer masked to fingers performs the press. Ignored by other interaction modes. Captured when the request begins.                                                                               | ``false``                        |
+------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``mode``                           | ``ControlInteractionMode``                                                      | Immediate commits the control action at once. IK first transfers a hand to Target. Animator uses an animation and its timing/events. Custom delegates the sequence to the assigned interaction handler. Options: ``Immediate``, ``IK``, ``Animator``, ``Custom``, ``IKThenAnimator``. | ``ControlInteractionMode.IK``    |
+------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``onCancelled``                    | ``UnityEvent``                                                                  | After an active interaction is cancelled. No payload; committed gameplay is not rolled back.                                                                                                                                                                                          | ``No listeners``                 |
+------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``onCommit``                       | ``UnityEvent``                                                                  | After the request's gameplay callback commits, at most once. No payload; do not duplicate the same mechanical action in both callbacks.                                                                                                                                               | ``No listeners``                 |
+------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``onCompleted``                    | ``UnityEvent``                                                                  | After the interaction completes. No payload; completion commits first if still needed.                                                                                                                                                                                                | ``No listeners``                 |
+------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``onStarted``                      | ``UnityEvent``                                                                  | After an interaction is admitted and its request is established. No payload; a handler can cancel immediately.                                                                                                                                                                        | ``No listeners``                 |
+------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``seat``                           | ``PassengerSeat`` (:ref:`fields <evs-inspectorreference-world--passengerseat>`) | Seat containing the character who operates this control. IK, Animator and Custom modes require an eligible occupant; Immediate can work without one.                                                                                                                                  | ``None / unassigned``            |
+------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``target``                         | ``VehicleHandle`` (:ref:`fields <evs-inspectorreference-world--vehiclehandle>`) | Handle the character reaches for before the control action is committed in IK mode. Its contact pose determines where the hand goes.                                                                                                                                                  | ``None / unassigned``            |
+------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``timeout``                        | ``float``                                                                       | Cancels an unfinished Animator or Custom action, including missing animation events. Zero disables timeout.                                                                                                                                                                           | ``5``; Minimum: 0                |
+------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``trigger``                        | ``string``                                                                      | Exact Animator trigger parameter name used to start an Animator-mode interaction. It must exist as a trigger in the assigned animation controller.                                                                                                                                    | ``"Interact"``                   |
+------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _evs-inspectorreference-interior--controlinteractionanimationevents:

ControlInteractionAnimationEvents
---------------------------------

Relays Animator events to the active interaction.

**Source:** ``Runtime/Interior/Controls/ControlInteractionAnimationEvents.cs``. Component / asset.

+-----------------+----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting         | Type                                                                                         | Description                                                                                                                                                   | Declared default and constraints |
+=================+==============================================================================================+===============================================================================================================================================================+==================================+
| ``interaction`` | ``ControlInteraction`` (:ref:`fields <evs-inspectorreference-interior--controlinteraction>`) | Active interaction receiving commit, complete and cancel events from this animation clip. Put this relay on the object receiving the clip's Animation Events. | ``None / unassigned``            |
+-----------------+----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _evs-inspectorreference-interior--enginerpmsource:

EngineRpmSource
---------------

Configuration/implementation type for engine rpm source within cockpit instruments and bindings.

**Source:** ``Runtime/Interior/Controls/Source/EngineRpmSource.cs``. Component / asset.

**Inherited settings:** :ref:`InteriorValueSource <evs-inspectorreference-interior--interiorvaluesource>`. These settings also appear on this type.

+------------+--------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting    | Type                                                               | Description                                                                                                    | Declared default and constraints |
+============+====================================================================+================================================================================================================+==================================+
| ``engine`` | ``Engine`` (:ref:`fields <evs-inspectorreference-engine--engine>`) | Engine whose current RPM is returned to the bound gauge or control. A missing or disabled engine returns zero. | ``None / unassigned``            |
+------------+--------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _evs-inspectorreference-interior--gassource:

GasSource
---------

**Source:** ``Runtime/Interior/Controls/Source/GasSource.cs``. Samples DriveDemand or raw throttle demand. Optional magnitude supports reverse propulsion and motorcycle twist grips.

+-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Field                 | Type                  | Meaning                                                                                                                                       |
+=======================+=======================+===============================================================================================================================================+
| ``absoluteValue``     | ``bool``              | Return the magnitude, including reverse propulsion; disable to retain the signed source value.                                                |
+-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``useResolvedDemand`` | ``bool``              | Read resolved signed DriveDemand when true; otherwise Command.Throttle.                                                                       |
+-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``vehicle``           | ``VehicleController`` | Vehicle supplying presentation values. When unassigned, resolves the nearest parent VehicleController, allowing a source beside its animator. |
+-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-inspectorreference-interior--gearleveranimator:

GearLeverAnimator
-----------------

**Source:** ``Runtime/Interior/Animators/GearLeverAnimator.cs``. Component configuration.

**Inherited settings:** ``ControlAnimator``.

+--------------------+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Setting            | Type                    | Meaning                                                                                                                                                                  |
+====================+=========================+==========================================================================================================================================================================+
| ``anchor``         | ``Transform``           | Contact transform used for IK. Parent it to the moving grip; it is separate from the animator hinge/pivot anchor.                                                        |
+--------------------+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``downshiftDelay`` | ``float``               | Quiet period after the latest downshift (.25 seconds by default). Further reductions restart it; upshifts, first gear, N and R cancel/bypass it. Zero disables the wait. |
+--------------------+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``engine``         | ``Engine``              | Assign the engine Engine component/asset used by Propulsion.                                                                                                             |
+--------------------+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``gearbox``        | ``Gearbox``             | Assign the gearbox Gearbox component/asset used by CommercialAudio.                                                                                                      |
+--------------------+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``mode``           | ``GearLeverMotionMode`` | Rotation or Translation.                                                                                                                                                 |
+--------------------+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``movingPart``     | ``Transform``           | ``Transform`` whose pose this mapper owns; keep imported-mesh offsets on its child.                                                                                      |
+--------------------+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``positions``      | ``GearLeverPosition[]`` | Unique signed gear numbers and their absolute poses. Defaults include R, N and gears 1–6.                                                                                |
+--------------------+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``shiftDuration``  | ``float``               | Visual lever travel duration in seconds; independent of gearbox torque transfer. Initial value: ``.18f``.                                                                |
+--------------------+-------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-inspectorreference-interior--gearleverposition:

GearLeverPosition
-----------------

**Source:** ``Runtime/Interior/Animators/GearLeverAnimator.cs``. Serializable position entry.

+--------------+-------------+--------------------------------------------------------------------------------------+
| Setting      | Type        | Meaning                                                                              |
+==============+=============+======================================================================================+
| ``gear``     | ``int``     | -1 = R, 0 = N, positive = forward gear. Duplicates and numbers below -1 are invalid. |
+--------------+-------------+--------------------------------------------------------------------------------------+
| ``position`` | ``Vector3`` | Absolute local offset relative to Anchor, used in Translation mode.                  |
+--------------+-------------+--------------------------------------------------------------------------------------+
| ``rotation`` | ``Vector3`` | Absolute Euler degrees relative to Anchor, used in Rotation mode.                    |
+--------------+-------------+--------------------------------------------------------------------------------------+

.. _evs-inspectorreference-interior--gearpaddleanimator:

GearPaddleAnimator
------------------

**Source:** ``Runtime/Interior/Animators/GearPaddleAnimator.cs``. Receives accepted gear changes through IGearShiftAnimator, coalesces downshifts, then reaches, presses and releases the paddle. Link a GearPaddleHandle for the intended hand.

**Inherited settings:** ``ControlAnimator``, ``IGearShiftAnimator``.

+--------------------+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Setting            | Type                   | Meaning                                                                                                                                                                  |
+====================+========================+==========================================================================================================================================================================+
| ``direction``      | ``GearShiftDirection`` | Selects the direction policy for this configuration. Options: ``Both``, ``Up``, ``Down``.                                                                                |
+--------------------+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``downshiftDelay`` | ``float``              | Quiet period after the latest downshift (.25 seconds by default). Further reductions restart it; upshifts, first gear, N and R cancel/bypass it. Zero disables the wait. |
+--------------------+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``motion``         | ``AnchoredRotation``   | Animator-owned moving geometry, independent pivot/reference, axis and travel mapping. Parent the IK contact under the moving geometry.                                   |
+--------------------+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``onPressed``      | ``UnityEvent``         | Inspector callback when visual pressing actually starts, after the optional limb wait; no payload. The configured paddle determines shift direction.                     |
+--------------------+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``pressDuration``  | ``float``              | Seconds for full released-to-pressed travel; smaller demands stop proportionally earlier.                                                                                |
+--------------------+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``pressedAngle``   | ``float``              | Pedal angle in degrees at displayed value one.                                                                                                                           |
+--------------------+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``returnDuration`` | ``float``              | Return travel duration in seconds, independent of outbound travel.                                                                                                       |
+--------------------+------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-inspectorreference-interior--gearshiftanimator:

GearShiftAnimator
-----------------

**Source:** ``Runtime/Interior/Animators/GearShiftAnimator.cs``. Component configuration.

**Inherited settings:** ``VehicleHandleAnimator``.

+---------------+---------------------+--------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting       | Type                | Description                                                                                                        | Declared default and constraints |
+===============+=====================+====================================================================================================================+==================================+
| ``animators`` | ``MonoBehaviour[]`` | Visual gear controls implementing IGearShiftAnimator. Assign the paddle animators; do not assign their IK handles. |                                  |
+---------------+---------------------+--------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``engine``    | ``Engine``          | Assign the engine Engine component/asset used by Propulsion.                                                       |                                  |
+---------------+---------------------+--------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``gearbox``   | ``Gearbox``         | Assign the gearbox Gearbox component/asset used by CommercialAudio.                                                |                                  |
+---------------+---------------------+--------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _evs-inspectorreference-interior--gearshiftdirection:

GearShiftDirection
------------------

**Source:** ``Runtime/Interior/Animators/GearPaddleAnimator.cs``. Component configuration.

Configure inherited contact/pose settings on this component; visual motion belongs to its animator.

.. _evs-inspectorreference-interior--handbrakesource:

HandbrakeSource
---------------

**Source:** ``Runtime/Interior/Controls/Source/HandbrakeSource.cs``. Samples Command.Handbrake as 0 or 1.

+-------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Field       | Type                  | Meaning                                                                                                                                       |
+=============+=======================+===============================================================================================================================================+
| ``vehicle`` | ``VehicleController`` | Vehicle supplying presentation values. When unassigned, resolves the nearest parent VehicleController, allowing a source beside its animator. |
+-------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-inspectorreference-interior--handlemotion:

HandleMotion
------------

**Source:** ``Runtime/Interior/Animators/HandleMotion.cs``. Reusable geometry mapping for animator-owned rotation or translation in an independent anchor frame. It is not an IK contact.

+----------------+-------------------------------+-------------------------------------------------------------------------------------------------------------------+
| Setting        | Type                          | Meaning                                                                                                           |
+================+===============================+===================================================================================================================+
| ``anchor``     | ``Transform``                 | Contact transform used for IK. Parent it to the moving grip; it is separate from the animator hinge/pivot anchor. |
+----------------+-------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``localAxis``  | ``Vector3``                   | Local axis around which the configured motion or operation takes place. Initial value: ``Vector3.forward``.       |
+----------------+-------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``maximum``    | ``float``                     | Offset at normalized value one; values may be signed/reversed to match model direction.                           |
+----------------+-------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``minimum``    | ``float``                     | Offset at normalized value zero: degrees in rotation mode, local distance in translation mode.                    |
+----------------+-------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``mode``       | ``AircraftControlMotionMode`` | Chooses rotation (degrees) or translation (local distance) for minimum/maximum/offset.                            |
+----------------+-------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``movingPart`` | ``Transform``                 | ``Transform`` whose pose this mapper owns; keep imported-mesh offsets on its child.                               |
+----------------+-------------------------------+-------------------------------------------------------------------------------------------------------------------+

.. _evs-inspectorreference-interior--igearshiftanimator:

IGearShiftAnimator
------------------

**Source:** ``Runtime/Interior/Animators/IGearShiftAnimator.cs``. Presentation contract for accepted gear changes. Implement it on visual gear controls; IK handles do not consume gearbox events.

Configure inherited contact/pose settings on this component; visual motion belongs to its animator.

.. _evs-inspectorreference-interior--indicatorswitchbinding:

IndicatorSwitchBinding
----------------------

**Source:** ``Runtime/Interior/Controls/IndicatorSwitchBinding.cs``. Component configuration.

**Inherited settings:** ``MonoBehaviour``.

+--------------------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| Setting            | Type               | Meaning                                                                                                                                                |
+====================+====================+========================================================================================================================================================+
| ``leftPosition``   | ``SwitchPosition`` | Selects the left position policy for this configuration. Options: ``Negative``, ``Neutral``, ``Positive``. Initial value: ``SwitchPosition.Negative``. |
+--------------------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``lights``         | ``Lights``         | Assign the lights Lights component/asset used by IndicatorAudio.                                                                                       |
+--------------------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``switchAnimator`` | ``SwitchAnimator`` | Switch animator for this control.                                                                                                                      |
+--------------------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-inspectorreference-interior--instrumentneedle:

InstrumentNeedle
----------------

Specializes value-driven rotation for instruments.

**Source:** ``Runtime/Interior/Controls/InstrumentNeedle.cs``. Component / asset.

**Inherited settings:** :ref:`RotaryAnimator <evs-inspectorreference-interior--rotaryanimator>`. These settings also appear on this type.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

.. _evs-inspectorreference-interior--interiordatasourceattribute:

InteriorDataSourceAttribute
---------------------------

**Source:** ``Runtime/Interior/Controls/Source/InteriorDataSourceAttribute.cs``. Marks an Inspector component field as an IInteriorValueSource consumer. The editor picker accepts application MonoBehaviours implementing the interface.

.. _evs-inspectorreference-interior--interiormodule:

InteriorModule
--------------

Configuration/implementation type for interior module within cockpit instruments and bindings.

**Source:** ``Runtime/Interior/Core/InteriorModule.cs``. Abstract base; settings are inherited by derived components.

**Inherited settings:** :ref:`VehicleModule <evs-inspectorreference-common--vehiclemodule>`. These settings also appear on this type.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

.. _evs-inspectorreference-interior--interiorvaluesource:

InteriorValueSource
-------------------

Base adapter for an ``IInteriorValueSource`` value producer.

**Source:** ``Runtime/Interior/Controls/Source/InteriorValueSource.cs``. Abstract base; settings are inherited by derived components.

No additional Inspector settings are declared on this type. Use the inherited settings above and the component enabled checkbox where available.

.. _evs-inspectorreference-interior--pedalanimator:

PedalAnimator
-------------

**Source:** ``Runtime/Interior/Animators/PedalAnimator.cs``. Samples resolved propulsion/service braking or an explicit command axis, and animates pedal travel. Its paired PedalHandle owns foot/ankle contact geometry.

**Inherited settings:** ``ControlAnimator``.

+---------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Setting             | Type                  | Meaning                                                                                                                                                             |
+=====================+=======================+=====================================================================================================================================================================+
| ``absoluteInput``   | ``bool``              | Use absolute input for signed propulsion/reverse commands.                                                                                                          |
+---------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``motion``          | ``AnchoredRotation``  | Animator-owned moving geometry, independent pivot/reference, axis and travel mapping. Parent the IK contact under the moving geometry.                              |
+---------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``onValueChanged``  | ``UnityEvent<float>`` | After this control's value changes. Payload: the event's value type; ``PedalAnimator`` reports displayed travel, ``SwitchAnimator`` reports a changed bool request. |
+---------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``pressDuration``   | ``float``             | Seconds for full released-to-pressed travel; smaller demands stop proportionally earlier.                                                                           |
+---------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``pressedAngle``    | ``float``             | Pedal angle in degrees at displayed value one.                                                                                                                      |
+---------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``releasedAngle``   | ``float``             | Pedal angle in degrees at displayed value zero.                                                                                                                     |
+---------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``releaseDuration`` | ``float``             | Seconds to fade after releasing the request; zero stops immediately.                                                                                                |
+---------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**PedalAnimator data source:** ``dataSource`` — Optional component implementing IInteriorValueSource. Overrides built-in sampling; any application MonoBehaviour can implement the interface. An assigned disabled, invalid or non-finite source produces zero. Empty uses the documented built-in default (Rotary remains API-driven).

.. _evs-inspectorreference-interior--pitchsource:

PitchSource
-----------

**Source:** ``Runtime/Interior/Controls/Source/PitchSource.cs``. Samples normalized Command.Pitch (-1..1).

+-------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Field       | Type                  | Meaning                                                                                                                                       |
+=============+=======================+===============================================================================================================================================+
| ``vehicle`` | ``VehicleController`` | Vehicle supplying presentation values. When unassigned, resolves the nearest parent VehicleController, allowing a source beside its animator. |
+-------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-inspectorreference-interior--profileswitchbinding:

ProfileSwitchBinding
--------------------

**Source:** ``Runtime/Interior/Controls/ProfileSwitchBinding.cs``. Component configuration.

**Inherited settings:** ``MonoBehaviour``.

+---------------------+-----------------------+-------------------------------------------------------------------------------------------+
| Setting             | Type                  | Meaning                                                                                   |
+=====================+=======================+===========================================================================================+
| ``offProfileId``    | ``string``            | Registration ID requested by the off position; defaults to drive.                         |
+---------------------+-----------------------+-------------------------------------------------------------------------------------------+
| ``onProfileId``     | ``string``            | Registration ID requested by the on position; defaults to hover.                          |
+---------------------+-----------------------+-------------------------------------------------------------------------------------------+
| ``profileSwitcher`` | ``ProfileSwitcher``   | Assign the profile switcher ProfileSwitcher component/asset used by ProfileSwitchBinding. |
+---------------------+-----------------------+-------------------------------------------------------------------------------------------+
| ``switchAnimator``  | ``SwitchAnimator``    | Switch animator for this control.                                                         |
+---------------------+-----------------------+-------------------------------------------------------------------------------------------+
| ``vehicle``         | ``VehicleController`` | Assign the vehicle VehicleController component/asset used by Audio.                       |
+---------------------+-----------------------+-------------------------------------------------------------------------------------------+

.. _evs-inspectorreference-interior--rearmirror:

RearMirror
----------

Configuration/implementation type for rear mirror within cockpit instruments and bindings.

**Source:** ``Runtime/Interior/Render/RearMirrors.cs``. Nested configuration data; expand its owning field in the Inspector.

+-------------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting                 | Type              | Description                                                                                                                                                                         | Declared default and constraints |
+=========================+===================+=====================================================================================================================================================================================+==================================+
| ``active``              | ``bool``          | Allows this individual mirror to render while the mirror system is enabled and the surface is visible. Turn off to stop updates for this mirror only.                               | ``true``                         |
+-------------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``aspectRatio``         | ``float``         | Width divided by height for an automatically created mirror texture. At 2, the texture is twice as wide as high. Match this to the mirror screen shape.                             | ``1.8``; Range: .5f to 3         |
+-------------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``camera``              | ``Camera``        | Dedicated camera looking behind the vehicle for this mirror. RearMirrors renders it manually to a texture, so do not use the main driving camera here.                              | ``None / unassigned``            |
+-------------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``cullingMask``         | ``LayerMask``     | Layers visible in this mirror's reflection. Exclude UI, helpers or costly geometry that should not appear behind the vehicle.                                                       | ``~0``                           |
+-------------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``farClip``             | ``float``         | Mirror camera's far clipping distance, in metres.                                                                                                                                   | ``120``; Minimum: 1              |
+-------------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``fieldOfView``         | ``float``         | Vertical view angle in degrees of this mirror camera. Increase to show a wider rear area, at the cost of making objects look smaller.                                               | ``55``; Range: 10 to 150         |
+-------------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``flipHorizontally``    | ``bool``          | Flips the displayed camera image left-to-right. Enable when the mirror should present a mirrored view instead of a rear-facing camera feed.                                         | ``true``                         |
+-------------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``maximumViewDistance`` | ``float``         | Observer-to-mirror distance in metres beyond which this mirror stops updating. Lower values save rendering work when the camera is far from the vehicle.                            | ``25``; Minimum: 1               |
+-------------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``nearClip``            | ``float``         | Mirror camera's near clipping distance, in metres.                                                                                                                                  | ``.1``; Minimum: .01f            |
+-------------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``refreshRate``         | ``float``         | Maximum mirror updates per second. Reduce to save rendering work; frame budget, visibility and distance can further lower the actual rate.                                          | ``20``; Range: 1 to 60           |
+-------------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``resolution``          | ``int``           | Width in pixels of an automatically created mirror texture. Higher values sharpen the reflection but increase rendering and texture memory; an assigned Texture keeps its own size. | ``256``; Range: 64 to 2048       |
+-------------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``surface``             | ``Renderer``      | Mirror-face renderer that displays this entry's camera image. Its visibility, layer and distance from the observer decide whether a render is needed.                               | ``None / unassigned``            |
+-------------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``texture``             | ``RenderTexture`` | Optional existing render texture receiving the mirror image. If empty, the system creates one using Resolution and Aspect Ratio.                                                    | ``None / unassigned``            |
+-------------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``textureProperty``     | ``string``        | Exact shader property name receiving this mirror's render texture, such as the material's main texture slot. It must match the shader used by Surface.                              | ``"_BaseMap"``                   |
+-------------------------+-------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _evs-inspectorreference-interior--rearmirrors:

RearMirrors
-----------

Owns mirror eligibility, camera rendering and generated textures.

**Source:** ``Runtime/Interior/Render/RearMirrors.cs``. Component / asset.

**Inherited settings:** :ref:`InteriorModule <evs-inspectorreference-interior--interiormodule>`. These settings also appear on this type.

+----------------------------+------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting                    | Type                                                                               | Description                                                                                                                                                 | Declared default and constraints |
+============================+====================================================================================+=============================================================================================================================================================+==================================+
| ``maximumRendersPerFrame`` | ``int``                                                                            | Maximum mirror-camera renders in one frame. Lower this to spread updates across frames and reduce frame spikes; higher values update more mirrors together. | ``2``; Range: 1 to 8             |
+----------------------------+------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``mirrors``                | ``List<RearMirror>`` (:ref:`fields <evs-inspectorreference-interior--rearmirror>`) | Mirror screens and their dedicated cameras. Add one entry per independently rendered mirror; each can have its own resolution and refresh limits.           | ``Empty list``                   |
+----------------------------+------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``mirrorsEnabled``         | ``bool``                                                                           | Master switch for updating all mirror cameras. Individual entries still need Active enabled and must pass visibility/distance checks.                       | ``true``                         |
+----------------------------+------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``observer``               | ``Camera``                                                                         | Camera used to decide whether mirror surfaces are visible and close enough to update. If empty, Camera.main is used.                                        | ``None / unassigned``            |
+----------------------------+------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _evs-inspectorreference-interior--rollsource:

RollSource
----------

**Source:** ``Runtime/Interior/Controls/Source/RollSource.cs``. Samples normalized roll (-1..1), optionally displaying resolved wheel steering while taxiing.

+-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Field                 | Type                  | Meaning                                                                                                                                       |
+=======================+=======================+===============================================================================================================================================+
| ``useGroundSteering`` | ``bool``              | Use resolved SteeringNormalized while an airplane is on the ground; otherwise return Command.Roll.                                            |
+-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``vehicle``           | ``VehicleController`` | Vehicle supplying presentation values. When unassigned, resolves the nearest parent VehicleController, allowing a source beside its animator. |
+-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-inspectorreference-interior--rotaryanimator:

RotaryAnimator
--------------

**Source:** ``Runtime/Interior/Animators/RotaryAnimator.cs``. Displays a bounded value as rotation, optionally following an IInteriorValueSource. Link a RotaryHandle when an occupant needs to touch the knob.

**Inherited settings:** ``ControlAnimator``.

+--------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Setting            | Type                  | Meaning                                                                                                                                                             |
+====================+=======================+=====================================================================================================================================================================+
| ``dataSource``     | ``MonoBehaviour``     | Optional component implementing ``IInteriorValueSource``; leave empty for API or ``UnityEvents`` control.                                                           |
+--------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``maximumAngle``   | ``float``             | Upper rotation angle in degrees for the configured motion. Initial value: ``135``.                                                                                  |
+--------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``maximumValue``   | ``float``             | Upper input/value endpoint mapped to the motion or instrument range. Initial value: ``1``.                                                                          |
+--------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``minimumAngle``   | ``float``             | Lower rotation angle in degrees for the configured motion. Initial value: ``-135``.                                                                                 |
+--------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``minimumValue``   | ``float``             | Lower input/value endpoint mapped to the motion or instrument range.                                                                                                |
+--------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``motion``         | ``AnchoredRotation``  | Animator-owned moving geometry, independent pivot/reference, axis and travel mapping. Parent the IK contact under the moving geometry.                              |
+--------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``onValueChanged`` | ``UnityEvent<float>`` | After this control's value changes. Payload: the event's value type; ``PedalAnimator`` reports displayed travel, ``SwitchAnimator`` reports a changed bool request. |
+--------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``response``       | ``float``             | Response rate toward the requested state. Higher values generally follow changes faster; consult the component for zero behavior. Initial value: ``18``.            |
+--------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

\| ``value`` \| ``float`` \| ``0`` \| Requested value in configured units. An assigned Data Source replaces it each frame. \|

.. _evs-inspectorreference-interior--servicebrakesource:

ServiceBrakeSource
------------------

**Source:** ``Runtime/Interior/Controls/Source/ServiceBrakeSource.cs``. Samples resolved service braking or raw Command.ServiceBrake (0..1).

+----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Field                | Type                  | Meaning                                                                                                                                       |
+======================+=======================+===============================================================================================================================================+
| ``useResolvedBrake`` | ``bool``              | Read resolved ServiceBrake when true; otherwise Command.ServiceBrake.                                                                         |
+----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``vehicle``          | ``VehicleController`` | Vehicle supplying presentation values. When unassigned, resolves the nearest parent VehicleController, allowing a source beside its animator. |
+----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-inspectorreference-interior--speedvaluesource:

SpeedValueSource
----------------

Configuration/implementation type for speed value source within cockpit instruments and bindings.

**Source:** ``Runtime/Interior/Controls/Source/SpeedValueSource.cs``. Component / asset.

**Inherited settings:** :ref:`InteriorValueSource <evs-inspectorreference-interior--interiorvaluesource>`. These settings also appear on this type.

+---------------+----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting       | Type                                                                                         | Description                                                                                                                                                                                 | Declared default and constraints |
+===============+==============================================================================================+=============================================================================================================================================================================================+==================================+
| ``signed``    | ``bool``                                                                                     | Preserves forward/reverse sign in the speed readout instead of returning speed magnitude.                                                                                                   | ``false``                        |
+---------------+----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``speedUnit`` | ``SpeedUnit``                                                                                | Output unit; defaults to Kph. Changing this does not alter vehicle physics. For a signed SpeedValueSource, reverse motion remains negative. Options: ``Kph``, ``Mph``, ``MetresPerSecond``. | ``SpeedUnit.Kph``                |
+---------------+----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``vehicle``   | ``VehicleController`` (:ref:`fields <evs-inspectorreference-controller--vehiclecontroller>`) | Vehicle whose speed is read for a gauge or display. Signed chooses forward/reverse speed; Speed Unit determines the returned units.                                                         | ``None / unassigned``            |
+---------------+----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

.. _evs-inspectorreference-interior--steeringsource:

SteeringSource
--------------

**Source:** ``Runtime/Interior/Controls/Source/SteeringSource.cs``. Samples normalized resolved steering (-1..1), with Hover command steering support.

+-------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Field                   | Type                  | Meaning                                                                                                                                       |
+=========================+=======================+===============================================================================================================================================+
| ``useResolvedSteering`` | ``bool``              | Read SteeringNormalized when true, except Hover which uses Command.Steering. False always reads Command.Steering.                             |
+-------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``vehicle``             | ``VehicleController`` | Vehicle supplying presentation values. When unassigned, resolves the nearest parent VehicleController, allowing a source beside its animator. |
+-------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-inspectorreference-interior--steeringstickanimator:

SteeringStickAnimator
---------------------

**Source:** ``Runtime/Interior/Animators/SteeringStickAnimator.cs``. Owns joystick pitch/roll model motion and taxi steering presentation. JoystickHandle supplies only the hand contacts.

**Inherited settings:** ``SteeringWheelAnimator``.

+-----------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Setting               | Type                 | Meaning                                                                                                                                                                                 |
+=======================+======================+=========================================================================================================================================================================================+
| ``controlResponse``   | ``float``            | Visual pitch and airborne roll response per second. Taxi roll follows wheel steering directly.                                                                                          |
+-----------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``driverSeat``        | ``PassengerSeat``    | Assign the driver seat PassengerSeat component/asset used by SteeringStickAnimator.                                                                                                     |
+-----------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``handle``            | ``JoystickHandle``   | Optional IK contact for this animated control. Set its anchor on the moving grip and author limb/pose settings on that component. An unassigned handle permits immediate visual motion. |
+-----------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``leftHandRest``      | ``Transform``        | Independent left-hand palm target, in cabin space. Reserved through the steering hand API.                                                                                              |
+-----------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``localPitchAxis``    | ``Vector3``          | Direction vector defining local pitch axis in the local frame used by this mechanism; it is not an absolute world position. Initial value: ``Vector3.right``.                           |
+-----------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``localRollAxis``     | ``Vector3``          | Local axis used to apply roll input to the handle or stick. Initial value: ``Vector3.forward``.                                                                                         |
+-----------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``maximumPitch``      | ``float``            | Pitch attitude limit in the assisted profile. Aerobatic profiles use angular rates instead.                                                                                             |
+-----------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``maximumRoll``       | ``float``            | Upper local roll angle in degrees. Initial value: ``6``.                                                                                                                                |
+-----------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``maximumRollOffset`` | ``float``            | Maximum roll offset for this control.                                                                                                                                                   |
+-----------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``minimumRoll``       | ``float``            | Lower local roll angle in degrees. Initial value: ``-6``.                                                                                                                               |
+-----------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``motion``            | ``HandleMotion``     | Animator-owned moving geometry, independent pivot/reference, axis and travel mapping. Parent the IK contact under the moving geometry.                                                  |
+-----------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``rotationPivot``     | ``Transform``        | Floor/base pivot. Place the stick mesh and its grip targets below this transform.                                                                                                       |
+-----------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``throttle``          | ``ThrottleAnimator`` | Assign the throttle ThrottleAnimator component/asset used by SteeringStickAnimator.                                                                                                     |
+-----------------------+----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**SteeringStickAnimator data source:** ``pitchSource`` — Independent IInteriorValueSource for normalized pitch (-1..1); empty uses Command.Pitch. Uses the same disabled/non-finite handling as Data Source.

.. _evs-inspectorreference-interior--steeringwheelanimator:

SteeringWheelAnimator
---------------------

**Source:** ``Runtime/Interior/Animators/SteeringWheelAnimator.cs``. Component configuration.

**Inherited settings:** ``VehicleHandleAnimator``.

+-----------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Setting                     | Type                  | Meaning                                                                                                                                                               |
+=============================+=======================+=======================================================================================================================================================================+
| ``boatSteeringResponse``    | ``float``             | Boat helm rendering response per second. Zero follows the resolved rudder immediately.                                                                                |
+-----------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``invert``                  | ``bool``              | Reverses the sign of the assigned control input before applying control-surface motion.                                                                               |
+-----------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``localRotationAxis``       | ``Vector3``           | Direction vector defining local rotation axis in the local frame used by this mechanism; it is not an absolute world position. Initial value: ``Vector3.forward``.    |
+-----------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``overrideSteeringAngle``   | ``bool``              | Use this animator’s visual full-lock angle instead of the vehicle’s shared steering-wheel angle. Default false; does not change physical wheel steering.              |
+-----------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``steeringAngleAtFullLock`` | ``float``             | Degrees from neutral to full lock on either side when override is enabled. Default 35; nonnegative.                                                                   |
+-----------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``steeringWheel``           | ``Transform``         | Assign the steering wheel reference used by SteeringWheelAnimator. Leave unassigned only when this feature is optional or the component can resolve it automatically. |
+-----------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``vehicle``                 | ``VehicleController`` | Assign the vehicle VehicleController component/asset used by Audio.                                                                                                   |
+-----------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**SteeringWheelAnimator data source:** ``dataSource`` — Optional component implementing IInteriorValueSource. Overrides built-in sampling; any application MonoBehaviour can implement the interface. An assigned disabled, invalid or non-finite source produces zero. Empty uses the documented built-in default (Rotary remains API-driven).

.. _evs-inspectorreference-interior--switchanimator:

SwitchAnimator
--------------

**Source:** ``Runtime/Interior/Animators/SwitchAnimator.cs``. Owns binary or three-position detents, requested/actual state, visual travel and switch events. It references a SwitchHandle for optional limb reach synchronization.

**Inherited settings:** ``ControlAnimator``.

+------------------------+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Setting                | Type                           | Meaning                                                                                                                                                             |
+========================+================================+=====================================================================================================================================================================+
| ``initiallyOn``        | ``bool``                       | Initial binary request used by first preparation.                                                                                                                   |
+------------------------+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``initialPosition``    | ``SwitchPosition``             | Initial three-position detent used by first preparation.                                                                                                            |
+------------------------+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``motion``             | ``HandleMotion``               | Animator-owned moving geometry, independent pivot/reference, axis and travel mapping. Parent the IK contact under the moving geometry.                              |
+------------------------+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``neutralOffset``      | ``float``                      | Middle-detent geometry offset in degrees or local distance, according to motion.mode.                                                                               |
+------------------------+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``onPositionChanged``  | ``UnityEvent<SwitchPosition>`` | After a changed switch detent request. Payload: ``SwitchPosition``; silent immediate synchronization does not invoke it.                                            |
+------------------------+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``onValueChanged``     | ``UnityEvent<bool>``           | After this control's value changes. Payload: the event's value type; ``PedalAnimator`` reports displayed travel, ``SwitchAnimator`` reports a changed bool request. |
+------------------------+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``threePosition``      | ``bool``                       | Enables Negative/Neutral/Positive detents; without it Negative requests throw.                                                                                      |
+------------------------+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``transitionDuration`` | ``float``                      | Seconds for visible detent travel; settlement events follow that travel.                                                                                            |
+------------------------+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-inspectorreference-interior--switchposition:

SwitchPosition
--------------

**Source:** ``Runtime/Interior/Animators/SwitchAnimator.cs``. Component configuration.

Configure inherited contact/pose settings on this component; visual motion belongs to its animator.

.. _evs-inspectorreference-interior--throttleanimator:

ThrottleAnimator
----------------

**Source:** ``Runtime/Interior/Animators/ThrottleAnimator.cs``. Owns throttle grip geometry and displayed throttle, including optional external presentation. The paired ThrottleHandle contains only IK contact and grip settings.

**Inherited settings:** ``ControlAnimator``.

+----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| Setting              | Type                  | Meaning                                                                                                                                                 |
+======================+=======================+=========================================================================================================================================================+
| ``driverSeat``       | ``PassengerSeat``     | Assign the driver seat PassengerSeat component/asset used by SteeringStickAnimator.                                                                     |
+----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``externalValue``    | ``float``             | Externally supplied throttle/control value used when the selected input mode requests external control.                                                 |
+----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``motion``           | ``HandleMotion``      | Animator-owned moving geometry, independent pivot/reference, axis and travel mapping. Parent the IK contact under the moving geometry.                  |
+----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``response``         | ``float``             | Response rate toward the requested state. Higher values generally follow changes faster; consult the component for zero behavior. Initial value: ``5``. |
+----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``useExternalValue`` | ``bool``              | Uses explicit cockpit presentation instead of following vehicle throttle.                                                                               |
+----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``useLeftHand``      | ``bool``              | Uses the driver's left hand rather than the right for this control.                                                                                     |
+----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``vehicle``          | ``VehicleController`` | Assign the vehicle VehicleController component/asset used by Audio.                                                                                     |
+----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+

**ThrottleAnimator data source:** ``dataSource`` — Optional component implementing IInteriorValueSource. Overrides built-in sampling; any application MonoBehaviour can implement the interface. An assigned disabled, invalid or non-finite source produces zero. Empty uses the documented built-in default (Rotary remains API-driven).

.. _evs-inspectorreference-interior--twistthrottleanimator:

TwistThrottleAnimator
---------------------

**Source:** ``Runtime/Interior/Animators/TwistThrottleAnimator.cs``. Inherits :ref:`AnchoredControlAnimator <evs-inspectorreference-interior--anchoredcontrolanimator>`.

Rotates the grip from resolved DriveDemand. Motion, angle, timing, preview and event settings are inherited.

.. _evs-inspectorreference-interior--limb-motion-synchronization:

Limb motion synchronization
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Control animators, switches, pedals and rotary controls expose ``waitForHandle`` (default true) and ``fakeSyncHandleMotion`` (default false). Assign ``handle`` to the corresponding IK contact on each ControlAnimator. Waiting uses actual limb contact within 2.5 cm after controller arrival, plus finger blending for hands, without a timeout bypass. Fake sync freezes only the outbound contact in the vehicle frame and follows the live contact after arrival. The steering wheel is excluded. See :ref:`the handle synchronization guide <evs-scripting-handles--synchronizing-control-motion-with-limb-arrival>` for mode combinations and lifecycle behavior.

No additional Inspector settings are declared on this type.

.. _evs-inspectorreference-interior--vehiclehandleanimator:

VehicleHandleAnimator
---------------------

**Source:** ``Runtime/Interior/Animators/VehicleHandleAnimator.cs``. Shared base for instrument geometry ownership. Set Automatic Motion off when an external Animator or Timeline owns the model.

**Inherited settings:** ``VehicleModule``.

+---------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------+
| Setting             | Type     | Meaning                                                                                                                           |
+=====================+==========+===================================================================================================================================+
| ``automaticMotion`` | ``bool`` | Default true. Allows this animator to write model transforms; disable when an external animation system owns the visible control. |
+---------------------+----------+-----------------------------------------------------------------------------------------------------------------------------------+

.. _evs-inspectorreference-interior--vehiclevaluesource:

VehicleValueSource
------------------

**Source:** ``Runtime/Interior/Controls/Source/VehicleValueSource.cs``. Base for reusable vehicle presentation sources. It stores an optional vehicle and falls back to the nearest parent vehicle. Sources are read by consumers and never drive the vehicle.

+-------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Field       | Type                  | Meaning                                                                                                                                       |
+=============+=======================+===============================================================================================================================================+
| ``vehicle`` | ``VehicleController`` | Vehicle supplying presentation values. When unassigned, resolves the nearest parent VehicleController, allowing a source beside its animator. |
+-------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-inspectorreference-interior--yokeanimator:

YokeAnimator
------------

Configuration/implementation type for yoke animator within cockpit instruments and bindings.

**Source:** ``Runtime/Interior/Animators/YokeAnimator.cs``. Component / asset.

**Inherited settings:** :ref:`SteeringWheelAnimator <evs-inspectorreference-interior--steeringwheelanimator>`. These settings also appear on this type.

+--------------------------+---------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| Setting                  | Type          | Description                                                                                                                             | Declared default and constraints |
+==========================+===============+=========================================================================================================================================+==================================+
| ``controlResponse``      | ``float``     | Visual control response per second, shared by roll and pitch.                                                                           | ``1.5``; Minimum: .1f            |
+--------------------------+---------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``localPitchTravelAxis`` | ``Vector3``   | Direction the yoke slides for pitch commands, in the slider parent's local coordinates. Usually forward/back along the steering column. | ``Vector3.forward``              |
+--------------------------+---------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``pitchSlide``           | ``Transform`` | Sliding column, with the rotating yoke below it. Leave empty to slide the yoke itself.                                                  | ``None / unassigned``            |
+--------------------------+---------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+
| ``pitchTravel``          | ``float``     | Maximum yoke slide in metres from neutral for full pitch input in either direction. Increase for a longer push/pull stroke.             | ``.035``; Minimum: 0             |
+--------------------------+---------------+-----------------------------------------------------------------------------------------------------------------------------------------+----------------------------------+

**YokeAnimator data source:** ``pitchSource`` — Independent IInteriorValueSource for normalized pitch (-1..1); empty uses Command.Pitch. Uses the same disabled/non-finite handling as Data Source.
