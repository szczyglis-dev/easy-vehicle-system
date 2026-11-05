.. _evs-scripting-eventsreference--events-reference:

Events reference
================

Public notifications grouped by the class that declares them. Each class has its own table with the event/callback, argument types and the point at which it fires. Events follow declaration order within each class; the class sections are ordered by name.

``C#`` means subscribe with ``+=`` / ``-=``. ``Inspector`` means a UnityEvent field, connected in the Inspector or with ``AddListener`` / ``RemoveListener``. Arguments are shown in delegate order; ``—`` means no arguments. Read current state when first subscribing rather than expecting an initial notification.

Inherited events are listed once on their declaring base class: Module lifecycle events also apply to derived modules. Profiles and helper classes are included where they expose events. Inspector callbacks nested in settings identify their invoking component below.

.. _evs-scripting-eventsreference--runtime-classes:

Runtime classes
---------------

.. _evs-scripting-eventsreference--aircraftcontrolsurfaces:

AircraftControlSurfaces
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------+------+-------------+----------------------------------------------------------------------------------------------------+
| Event / callback           | Kind | Arguments   | When it fires / meaning                                                                            |
+============================+======+=============+====================================================================================================+
| ``ControlsChanged``        | C#   | ``Vector3`` | When displayed pitch/roll/yaw controls change; Vector3 components carry those presentation values. |
+----------------------------+------+-------------+----------------------------------------------------------------------------------------------------+
| ``FlapsChanged``           | C#   | ``float``   | When the normalized flap presentation request changes.                                             |
+----------------------------+------+-------------+----------------------------------------------------------------------------------------------------+
| ``AirbrakeChanged``        | C#   | ``float``   | When the normalized airbrake presentation request changes.                                         |
+----------------------------+------+-------------+----------------------------------------------------------------------------------------------------+
| ``ExternalControlChanged`` | C#   | ``bool``    | When aircraft surface presentation changes external/follow-vehicle ownership.                      |
+----------------------------+------+-------------+----------------------------------------------------------------------------------------------------+

Details: :ref:`AircraftControlSurfaces API <evs-api-aircraft--aircraftcontrolsurfaces>`.

.. _evs-scripting-eventsreference--aircrafthud:

AircraftHud
~~~~~~~~~~~

+------------------+------+---------------+--------------------------------------------+
| Event / callback | Kind | Arguments     | When it fires / meaning                    |
+==================+======+===============+============================================+
| ``Changed``      | C#   | ``Telemetry`` | After the HUD receives an updated reading. |
+------------------+------+---------------+--------------------------------------------+

Details: :ref:`AircraftHud API <evs-api-interior--aircrafthud>`.

.. _evs-scripting-eventsreference--anchoredcontrolanimator:

AnchoredControlAnimator
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------+-----------+-----------+----------------------------------------------------------------------------------------+
| Event / callback   | Kind      | Arguments | When it fires / meaning                                                                |
+====================+===========+===========+========================================================================================+
| ``onValueChanged`` | Inspector | ``float`` | After the animated control value changes (0–1), including reset to the released value. |
+--------------------+-----------+-----------+----------------------------------------------------------------------------------------+

Details: :ref:`AnchoredControlAnimator API <evs-api-interior--anchoredcontrolanimator>`.

.. _evs-scripting-eventsreference--boatprofile:

BoatProfile
~~~~~~~~~~~

+--------------------+------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
| Event / callback   | Kind | Arguments | When it fires / meaning                                                                                                                                 |
+====================+======+===========+=========================================================================================================================================================+
| ``SinkingChanged`` | C#   | ``bool``  | Raised once when sinking is started or stopped. The argument is the new sinking state; repeated requests for the same state do not raise another event. |
+--------------------+------+-----------+---------------------------------------------------------------------------------------------------------------------------------------------------------+

Details: :ref:`BoatProfile API <evs-api-boat--boatprofile>`.

.. _evs-scripting-eventsreference--brakes:

Brakes
~~~~~~

+-------------------------+------+-----------+------------------------------------------------------------------------------------------------------------------+
| Event / callback        | Kind | Arguments | When it fires / meaning                                                                                          |
+=========================+======+===========+==================================================================================================================+
| ``ServiceBrakeChanged`` | C#   | ``float`` | When resolved service-brake demand changes (0–1).                                                                |
+-------------------------+------+-----------+------------------------------------------------------------------------------------------------------------------+
| ``HandbrakeChanged``    | C#   | ``bool``  | When the resolved handbrake state changes; bool reports the new state.                                           |
+-------------------------+------+-----------+------------------------------------------------------------------------------------------------------------------+
| ``BrakingChanged``      | C#   | ``bool``  | Moving service-brake activity changes; payload is active/inactive. Owned by Brakes, independent of TireFeedback. |
+-------------------------+------+-----------+------------------------------------------------------------------------------------------------------------------+

Details: :ref:`Brakes API <evs-api-drivedynamics--brakes>`.

.. _evs-scripting-eventsreference--burnout:

Burnout
~~~~~~~

+--------------------+------+-----------+--------------------------------------------------------+
| Event / callback   | Kind | Arguments | When it fires / meaning                                |
+====================+======+===========+========================================================+
| ``BurnoutStarted`` | C#   | —         | Assistance begins.                                     |
+--------------------+------+-----------+--------------------------------------------------------+
| ``BurnoutStopped`` | C#   | —         | Assistance ends, including reset/disable.              |
+--------------------+------+-----------+--------------------------------------------------------+
| ``StateChanged``   | C#   | ``bool``  | Reports transitions into and out of active assistance. |
+--------------------+------+-----------+--------------------------------------------------------+

Details: :ref:`Burnout API <evs-api-drivedynamics--burnout>`.

.. _evs-scripting-eventsreference--cameras:

Cameras
~~~~~~~

+-------------------+------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| Event / callback  | Kind | Arguments    | When it fires / meaning                                                                                                                               |
+===================+======+==============+=======================================================================================================================================================+
| ``CameraChanged`` | C#   | ``Camera``   | After Attach changes the assigned camera or Detach releases it; payload is the new camera or null. Inspector field edits do not raise this API event. |
+-------------------+------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``ModeChanged``   | C#   | ``ViewMode`` | After SetView or Attach changes the view; payload is the new mode.                                                                                    |
+-------------------+------+--------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+

Details: :ref:`Cameras API <evs-api-camera--cameras>`.

.. _evs-scripting-eventsreference--carhud:

CarHud
~~~~~~

+------------------+------+---------------+--------------------------------------------+
| Event / callback | Kind | Arguments     | When it fires / meaning                    |
+==================+======+===============+============================================+
| ``Changed``      | C#   | ``Telemetry`` | After the HUD receives an updated reading. |
+------------------+------+---------------+--------------------------------------------+

Details: :ref:`CarHud API <evs-api-interior--carhud>`.

.. _evs-scripting-eventsreference--clutch:

Clutch
~~~~~~

+-----------------------+------+-----------+----------------------------------------------------------------------------+
| Event / callback      | Kind | Arguments | When it fires / meaning                                                    |
+=======================+======+===========+============================================================================+
| ``EngagementChanged`` | C#   | ``float`` | When resolved clutch engagement changes (0–1); distinct from pedal travel. |
+-----------------------+------+-----------+----------------------------------------------------------------------------+
| ``AutomaticChanged``  | C#   | ``bool``  | When automatic clutch assistance selection changes.                        |
+-----------------------+------+-----------+----------------------------------------------------------------------------+

Details: :ref:`Clutch API <evs-api-drivedynamics--clutch>`.

.. _evs-scripting-eventsreference--controlinteraction:

ControlInteraction
~~~~~~~~~~~~~~~~~~

+------------------+-----------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------+
| Event / callback | Kind      | Arguments | When it fires / meaning                                                                                                                 |
+==================+===========+===========+=========================================================================================================================================+
| ``onStarted``    | Inspector | —         | After an interaction is admitted and its request is established. No payload; a handler can cancel immediately.                          |
+------------------+-----------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------+
| ``onCommit``     | Inspector | —         | After the request's gameplay callback commits, at most once. No payload; do not duplicate the same mechanical action in both callbacks. |
+------------------+-----------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------+
| ``onCompleted``  | Inspector | —         | After the interaction completes. No payload; completion commits first if still needed.                                                  |
+------------------+-----------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------+
| ``onCancelled``  | Inspector | —         | After an active interaction is cancelled. No payload; committed gameplay is not rolled back.                                            |
+------------------+-----------+-----------+-----------------------------------------------------------------------------------------------------------------------------------------+

Details: :ref:`ControlInteraction API <evs-api-interactions--controlinteraction>`.

.. _evs-scripting-eventsreference--coupler:

Coupler
~~~~~~~

+------------------+------+-------------+---------------------------------------------------------------+
| Event / callback | Kind | Arguments   | When it fires / meaning                                       |
+==================+======+=============+===============================================================+
| ``Attached``     | C#   | ``Trailer`` | After coupler admission creates the relationship.             |
+------------------+------+-------------+---------------------------------------------------------------+
| ``Detached``     | C#   | ``Trailer`` | After explicit detachment/cleanup of this hitch relationship. |
+------------------+------+-------------+---------------------------------------------------------------+

Details: :ref:`Coupler API <evs-api-towing--coupler>`.

.. _evs-scripting-eventsreference--damage:

Damage
~~~~~~

+--------------------------+------+----------------------+----------------------------------------------------------------------------------------------------------+
| Event / callback         | Kind | Arguments            | When it fires / meaning                                                                                  |
+==========================+======+======================+==========================================================================================================+
| ``Hit``                  | C#   | ``DamageHit``        | When a damage hit is accepted.                                                                           |
+--------------------------+------+----------------------+----------------------------------------------------------------------------------------------------------+
| ``DeformationRequested`` | C#   | ``DamageHit, float`` | Accepted hit and radius before part detachment; optional deformation receivers process it synchronously. |
+--------------------------+------+----------------------+----------------------------------------------------------------------------------------------------------+
| ``EffectsCleared``       | C#   | —                    | Requests clearing optional impact presentation.                                                          |
+--------------------------+------+----------------------+----------------------------------------------------------------------------------------------------------+
| ``FullyRepaired``        | C#   | —                    | After a full repair pass and effect cleanup; it does not guarantee destroyed objects were recreated.     |
+--------------------------+------+----------------------+----------------------------------------------------------------------------------------------------------+
| ``PartsChanged``         | C#   | —                    | Reports that the damage boundary list has been refreshed.                                                |
+--------------------------+------+----------------------+----------------------------------------------------------------------------------------------------------+

Details: :ref:`Damage API <evs-api-damage--damage>`.

.. _evs-scripting-eventsreference--damageaudio:

DamageAudio
~~~~~~~~~~~

+---------------------+------+-----------------------------------------------+------------------------------------------------------------------------------------------+
| Event / callback    | Kind | Arguments                                     | When it fires / meaning                                                                  |
+=====================+======+===============================================+==========================================================================================+
| ``Played``          | C#   | ``DamageHit, DamageImpactProfile, AudioClip`` | After a damage sound starts, carrying the hit, selected profile and chosen clip.         |
+---------------------+------+-----------------------------------------------+------------------------------------------------------------------------------------------+
| ``CollisionPlayed`` | C#   | ``Impact, AudioClip``                         | Raised after a collision sound starts; carries the copied Impact and selected clip.      |
+---------------------+------+-----------------------------------------------+------------------------------------------------------------------------------------------+
| ``LandingPlayed``   | C#   | ``LandingEvent, AudioClip``                   | Raised after a wheel touchdown sound starts; carries LandingEvent and the selected clip. |
+---------------------+------+-----------------------------------------------+------------------------------------------------------------------------------------------+

Details: :ref:`DamageAudio API <evs-api-audio--damageaudio>`.

.. _evs-scripting-eventsreference--damageimpacteffects:

DamageImpactEffects
~~~~~~~~~~~~~~~~~~~

+------------------+------+------------------------------------+-------------------------------------+
| Event / callback | Kind | Arguments                          | When it fires / meaning             |
+==================+======+====================================+=====================================+
| ``EffectPlayed`` | C#   | ``DamageHit, DamageImpactProfile`` | Raised after a visual lease starts. |
+------------------+------+------------------------------------+-------------------------------------+

Details: :ref:`DamageImpactEffects API <evs-api-damage--damageimpacteffects>`.

.. _evs-scripting-eventsreference--damagepart:

DamagePart
~~~~~~~~~~

+------------------+------+-----------------------+--------------------------------------------------------------------------------------------+
| Event / callback | Kind | Arguments             | When it fires / meaning                                                                    |
+==================+======+=======================+============================================================================================+
| ``Restored``     | C#   | ``DamagePart``        | After full remount/state/mesh repair; incremental Repair(amount) does not emit this event. |
+------------------+------+-----------------------+--------------------------------------------------------------------------------------------+
| ``Detached``     | C#   | ``DamagePart``        | After a damage part detaches.                                                              |
+------------------+------+-----------------------+--------------------------------------------------------------------------------------------+
| ``Damaged``      | C#   | ``DamagePart, float`` | After the part accepts damage.                                                             |
+------------------+------+-----------------------+--------------------------------------------------------------------------------------------+
| ``Repaired``     | C#   | ``DamagePart, float`` | After damage is actually removed.                                                          |
+------------------+------+-----------------------+--------------------------------------------------------------------------------------------+

Details: :ref:`DamagePart API <evs-api-damage--damagepart>`.

.. _evs-scripting-eventsreference--drivingassists:

DrivingAssists
~~~~~~~~~~~~~~

+-----------------------------+------+-----------+--------------------------------------------------------------------------+
| Event / callback            | Kind | Arguments | When it fires / meaning                                                  |
+=============================+======+===========+==========================================================================+
| ``TractionControlChanged``  | C#   | ``bool``  | When ``DrivingAssists`` changes its coordinated traction-control choice. |
+-----------------------------+------+-----------+--------------------------------------------------------------------------+
| ``StabilityControlChanged`` | C#   | ``bool``  | When ``DrivingAssists`` changes its stability-assistance choice.         |
+-----------------------------+------+-----------+--------------------------------------------------------------------------+

Details: :ref:`DrivingAssists API <evs-api-drivedynamics--drivingassists>`.

.. _evs-scripting-eventsreference--droppableobject:

DroppableObject
~~~~~~~~~~~~~~~

+------------------+------+---------------------+--------------------------------------------------+
| Event / callback | Kind | Arguments           | When it fires / meaning                          |
+==================+======+=====================+==================================================+
| ``Dropped``      | C#   | ``DroppableObject`` | After this payload detaches and inherits motion. |
+------------------+------+---------------------+--------------------------------------------------+

Details: :ref:`DroppableObject API <evs-api-weapons--droppableobject>`.

.. _evs-scripting-eventsreference--engine:

Engine
~~~~~~

+--------------------------+------+-------------+--------------------------------------------------------------------------------------------------------------------------+
| Event / callback         | Kind | Arguments   | When it fires / meaning                                                                                                  |
+==========================+======+=============+==========================================================================================================================+
| ``EngineStateChanged``   | C#   | ``bool``    | After engine running state changes.                                                                                      |
+--------------------------+------+-------------+--------------------------------------------------------------------------------------------------------------------------+
| ``GearChanged``          | C#   | ``int``     | When Engine observes a changed gearbox gear during Step; the initial gear sample is silent.                              |
+--------------------------+------+-------------+--------------------------------------------------------------------------------------------------------------------------+
| ``ActiveGearboxChanged`` | C#   | ``Gearbox`` | Reports a change of effective gearbox identity, including removal or disable. Read ActiveGearbox when first subscribing. |
+--------------------------+------+-------------+--------------------------------------------------------------------------------------------------------------------------+

Details: :ref:`Engine API <evs-api-drivedynamics--engine>`.

.. _evs-scripting-eventsreference--eventaudio:

EventAudio
~~~~~~~~~~

+------------------+------+----------------------------+--------------------------------------------------+
| Event / callback | Kind | Arguments                  | When it fires / meaning                          |
+==================+======+============================+==================================================+
| ``Played``       | C#   | ``EffectEvent, AudioClip`` | When ``EventAudio`` plays a resolved event clip. |
+------------------+------+----------------------------+--------------------------------------------------+

Details: :ref:`EventAudio API <evs-api-audio--eventaudio>`.

.. _evs-scripting-eventsreference--events:

Events
~~~~~~

+------------------+------+-----------------+------------------------------------------------------------------------------------------------------+
| Event / callback | Kind | Arguments       | When it fires / meaning                                                                              |
+==================+======+=================+======================================================================================================+
| ``Raised``       | C#   | ``EffectEvent`` | When the adapter translates a typed source notification or an integration publishes a custom effect. |
+------------------+------+-----------------+------------------------------------------------------------------------------------------------------+

Details: :ref:`Events API <evs-api-events--events>`.

.. _evs-scripting-eventsreference--fueltank:

FuelTank
~~~~~~~~

+------------------+------+-----------+------------------------------------------------------------------------------------------------+
| Event / callback | Kind | Arguments | When it fires / meaning                                                                        |
+==================+======+===========+================================================================================================+
| ``FuelChanged``  | C#   | ``float`` | After fuel quantity changes; the value is current litres, not the transfer amount.             |
+------------------+------+-----------+------------------------------------------------------------------------------------------------+
| ``Emptied``      | C#   | —         | On the transition to empty fuel.                                                               |
+------------------+------+-----------+------------------------------------------------------------------------------------------------+
| ``Refuelled``    | C#   | —         | After an actual increase in fuel, including ``SetFuel``. No payload; query quantity if needed. |
+------------------+------+-----------+------------------------------------------------------------------------------------------------+

Details: :ref:`FuelTank API <evs-api-interior--fueltank>`.

.. _evs-scripting-eventsreference--gearbox:

Gearbox
~~~~~~~

+--------------------+------+-----------+--------------------------------------------------------------------------------------------------------+
| Event / callback   | Kind | Arguments | When it fires / meaning                                                                                |
+====================+======+===========+========================================================================================================+
| ``GearChanged``    | C#   | ``int``   | After gear selection/synchronization changes the signed gear: reverse -1, neutral 0, forward positive. |
+--------------------+------+-----------+--------------------------------------------------------------------------------------------------------+
| ``ShiftStarted``   | C#   | ``int``   | When an accepted selection starts its shift interval.                                                  |
+--------------------+------+-----------+--------------------------------------------------------------------------------------------------------+
| ``ShiftCompleted`` | C#   | ``int``   | When that shift interval completes; a zero-duration shift can complete immediately.                    |
+--------------------+------+-----------+--------------------------------------------------------------------------------------------------------+

Details: :ref:`Gearbox API <evs-api-drivedynamics--gearbox>`.

.. _evs-scripting-eventsreference--gearpaddleanimator:

GearPaddleAnimator
~~~~~~~~~~~~~~~~~~

+------------------+-----------+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| Event / callback | Kind      | Arguments | When it fires / meaning                                                                                                                              |
+==================+===========+===========+======================================================================================================================================================+
| ``onPressed``    | Inspector | —         | Inspector callback when visual pressing actually starts, after the optional limb wait; no payload. The configured paddle determines shift direction. |
+------------------+-----------+-----------+------------------------------------------------------------------------------------------------------------------------------------------------------+

Details: :ref:`GearPaddleAnimator API <evs-api-interior--gearpaddleanimator>`.

.. _evs-scripting-eventsreference--handlecontroller:

HandleController
~~~~~~~~~~~~~~~~

+------------------+------+---------------+---------------------------------------------------------------------------------------------------------------------+
| Event / callback | Kind | Arguments     | When it fires / meaning                                                                                             |
+==================+======+===============+=====================================================================================================================+
| ``Started``      | C#   | ``HandleUse`` | After a token owns its limb. Payload is the new token.                                                              |
+------------------+------+---------------+---------------------------------------------------------------------------------------------------------------------+
| ``Finished``     | C#   | ``HandleUse`` | After completion or cancellation has released ownership and restored any owned binding. Payload is the ended token. |
+------------------+------+---------------+---------------------------------------------------------------------------------------------------------------------+

Details: :ref:`HandleController API <evs-api-handles--handlecontroller>`.

.. _evs-scripting-eventsreference--handleuse:

HandleUse
~~~~~~~~~

+------------------+------+-----------+-----------------------------------------------------------------------------------------------------------------+
| Event / callback | Kind | Arguments | When it fires / meaning                                                                                         |
+==================+======+===========+=================================================================================================================+
| ``Arrived``      | C#   | —         | After binding the destination and running the arrival callback. Persistent acquisitions do not emit this event. |
+------------------+------+-----------+-----------------------------------------------------------------------------------------------------------------+
| ``Completed``    | C#   | —         | After the return completes and the home binding is restored.                                                    |
+------------------+------+-----------+-----------------------------------------------------------------------------------------------------------------+
| ``Cancelled``    | C#   | —         | After cancellation has released ownership. An already committed action is not undone.                           |
+------------------+------+-----------+-----------------------------------------------------------------------------------------------------------------+

Details: :ref:`HandleUse API <evs-api-handles--handleuse>`.

.. _evs-scripting-eventsreference--humanoidpassenger:

HumanoidPassenger
~~~~~~~~~~~~~~~~~

+--------------------+------+-----------------------+------------------------------------+
| Event / callback   | Kind | Arguments             | When it fires / meaning            |
+====================+======+=======================+====================================+
| ``BeforeSeatedIK`` | C#   | ``HumanoidPassenger`` | Immediately before seated IK work. |
+--------------------+------+-----------------------+------------------------------------+
| ``AfterSeatedIK``  | C#   | ``HumanoidPassenger`` | Immediately after seated IK work.  |
+--------------------+------+-----------------------+------------------------------------+

Details: :ref:`HumanoidPassenger API <evs-api-passengercontrollers--humanoidpassenger>`.

.. _evs-scripting-eventsreference--inputgateroute:

InputGate.Route
~~~~~~~~~~~~~~~

+------------------+-----------+-----------+--------------------------------------------------------------------------------------------+
| Event / callback | Kind      | Arguments | When it fires / meaning                                                                    |
+==================+===========+===========+============================================================================================+
| ``selected``     | Inspector | —         | InputGate selects the route matching the active profile, after assigning its input source. |
+------------------+-----------+-----------+--------------------------------------------------------------------------------------------+

Details: :ref:`InputGate.Route API <evs-api-input--inputgateroute>`.

.. _evs-scripting-eventsreference--ipartmotionsource:

IPartMotionSource
~~~~~~~~~~~~~~~~~

+------------------------+------+---------------------+------------------------------------------------+
| Event / callback       | Kind | Arguments           | When it fires / meaning                        |
+========================+======+=====================+================================================+
| ``MotionOccurred``     | C#   | ``PartMotionEvent`` | Reports the corresponding source state change. |
+------------------------+------+---------------------+------------------------------------------------+
| ``MotionAudioStopped`` | C#   | —                   | Reports the corresponding source state change. |
+------------------------+------+---------------------+------------------------------------------------+

Details: :ref:`IPartMotionSource API <evs-api-movingparts--ipartmotionsource>`.

.. _evs-scripting-eventsreference--landinggear:

LandingGear
~~~~~~~~~~~

+------------------+------+----------------------+----------------------------------------------------------+
| Event / callback | Kind | Arguments            | When it fires / meaning                                  |
+==================+======+======================+==========================================================+
| ``StateChanged`` | C#   | ``LandingGearState`` | When deployment sequencing changes ``LandingGearState``. |
+------------------+------+----------------------+----------------------------------------------------------+

Details: :ref:`LandingGear API <evs-api-aircraft--landinggear>`.

.. _evs-scripting-eventsreference--lightchannel:

LightChannel
~~~~~~~~~~~~

+------------------+------+-----------+------------------------------------------------------+
| Event / callback | Kind | Arguments | When it fires / meaning                              |
+==================+======+===========+======================================================+
| ``LitChanged``   | C#   | ``bool``  | When a ``LightChannel``'s actual lit output changes. |
+------------------+------+-----------+------------------------------------------------------+

Details: :ref:`LightChannel API <evs-api-lights--lightchannel>`.

.. _evs-scripting-eventsreference--lights:

Lights
~~~~~~

+---------------------------+------+--------------------+------------------------------------------------+
| Event / callback          | Kind | Arguments          | When it fires / meaning                        |
+===========================+======+====================+================================================+
| ``IndicatorPhaseChanged`` | C#   | ``bool``           | When the shared flashing output phase changes. |
+---------------------------+------+--------------------+------------------------------------------------+
| ``BeamModeChanged``       | C#   | ``BeamMode``       | When requested beam mode changes.              |
+---------------------------+------+--------------------+------------------------------------------------+
| ``IndicatorsChanged``     | C#   | ``IndicatorState`` | When requested direction/hazard state changes. |
+---------------------------+------+--------------------+------------------------------------------------+

Details: :ref:`Lights API <evs-api-lights--lights>`.

.. _evs-scripting-eventsreference--movingpart:

MovingPart
~~~~~~~~~~

+--------------------------+------+---------------------+------------------------------------------------------------------------------------------------------------------------+
| Event / callback         | Kind | Arguments           | When it fires / meaning                                                                                                |
+==========================+======+=====================+========================================================================================================================+
| ``OpeningStarted``       | C#   | —                   | Once before an opening operation moves the pose. No payload; interruptions never imply completion.                     |
+--------------------------+------+---------------------+------------------------------------------------------------------------------------------------------------------------+
| ``OpeningCompleted``     | C#   | —                   | Once after the actual pose reaches the requested opening target. No payload; physical hinges use Completion Tolerance. |
+--------------------------+------+---------------------+------------------------------------------------------------------------------------------------------------------------+
| ``ClosingStarted``       | C#   | —                   | Once before a closing operation moves the pose.                                                                        |
+--------------------------+------+---------------------+------------------------------------------------------------------------------------------------------------------------+
| ``ClosingCompleted``     | C#   | —                   | Once after the actual pose reaches the requested closing target.                                                       |
+--------------------------+------+---------------------+------------------------------------------------------------------------------------------------------------------------+
| ``Moved``                | C#   | ``MovingPart``      | After moving-part pose changes.                                                                                        |
+--------------------------+------+---------------------+------------------------------------------------------------------------------------------------------------------------+
| ``MotionEnabledChanged`` | C#   | ``bool``            | When moving-part motion availability changes.                                                                          |
+--------------------------+------+---------------------+------------------------------------------------------------------------------------------------------------------------+
| ``MotionOccurred``       | C#   | ``PartMotionEvent`` | Reports an admitted movement phase to optional presentation receivers.                                                 |
+--------------------------+------+---------------------+------------------------------------------------------------------------------------------------------------------------+
| ``MotionAudioStopped``   | C#   | —                   | Requests stopping movement audio after interruption or disable.                                                        |
+--------------------------+------+---------------------+------------------------------------------------------------------------------------------------------------------------+

Details: :ref:`MovingPart API <evs-api-movingparts--movingpart>`.

.. _evs-scripting-eventsreference--nitro:

Nitro
~~~~~

+------------------------+------+-----------+-----------------------------------------------------------------------------------------------------+
| Event / callback       | Kind | Arguments | When it fires / meaning                                                                             |
+========================+======+===========+=====================================================================================================+
| ``NitroStarted``       | C#   | —         | Effective boost begins.                                                                             |
+------------------------+------+-----------+-----------------------------------------------------------------------------------------------------+
| ``NitroStopped``       | C#   | —         | Effective boost ends, including reset/disable.                                                      |
+------------------------+------+-----------+-----------------------------------------------------------------------------------------------------+
| ``AmountChanged``      | C#   | ``float`` | Reports actual remaining charge after a change; payload is charge units.                            |
+------------------------+------+-----------+-----------------------------------------------------------------------------------------------------+
| ``BoostStateChanged``  | C#   | ``bool``  | Reports transitions into/out of resolved boost; payload is the active flag.                         |
+------------------------+------+-----------+-----------------------------------------------------------------------------------------------------+
| ``Depleted``           | C#   | —         | Raised once when positive charge reaches zero.                                                      |
+------------------------+------+-----------+-----------------------------------------------------------------------------------------------------+
| ``OutputStateChanged`` | C#   | ``bool``  | Reports a change of the propulsion-output session. Receivers can be absent without affecting boost. |
+------------------------+------+-----------+-----------------------------------------------------------------------------------------------------+

Details: :ref:`Nitro API <evs-api-drivedynamics--nitro>`.

.. _evs-scripting-eventsreference--objectdropper:

ObjectDropper
~~~~~~~~~~~~~

+----------------------------+------+------------------------------------+---------------------------------------------------------------------------------+
| Event / callback           | Kind | Arguments                          | When it fires / meaning                                                         |
+============================+======+====================================+=================================================================================+
| ``Dropped``                | C#   | ``ObjectDropper, DroppableObject`` | After the dropper releases a payload; includes the dropper and released object. |
+----------------------------+------+------------------------------------+---------------------------------------------------------------------------------+
| ``DroppingEnabledChanged`` | C#   | ``bool``                           | When dropper availability changes.                                              |
+----------------------------+------+------------------------------------+---------------------------------------------------------------------------------+

Details: :ref:`ObjectDropper API <evs-api-weapons--objectdropper>`.

.. _evs-scripting-eventsreference--partmotionevents:

PartMotionEvents
~~~~~~~~~~~~~~~~

+----------------------+-----------+-----------+----------------------------------------------------------------------------------------------------------------+
| Event / callback     | Kind      | Arguments | When it fires / meaning                                                                                        |
+======================+===========+===========+================================================================================================================+
| ``openingStarted``   | Inspector | —         | VehicleBodyPart or MovingPart starts opening; follows its OpeningStarted C# event.                             |
+----------------------+-----------+-----------+----------------------------------------------------------------------------------------------------------------+
| ``openingCompleted`` | Inspector | —         | VehicleBodyPart or MovingPart reaches its open target; follows OpeningCompleted, not an interrupted operation. |
+----------------------+-----------+-----------+----------------------------------------------------------------------------------------------------------------+
| ``closingStarted``   | Inspector | —         | VehicleBodyPart or MovingPart starts closing; follows its ClosingStarted C# event.                             |
+----------------------+-----------+-----------+----------------------------------------------------------------------------------------------------------------+
| ``closingCompleted`` | Inspector | —         | VehicleBodyPart or MovingPart reaches its closed target; follows ClosingCompleted.                             |
+----------------------+-----------+-----------+----------------------------------------------------------------------------------------------------------------+

Details: :ref:`PartMotionEvents API <evs-api-movingparts--partmotionevents>`.

.. _evs-scripting-eventsreference--passengeraccess:

PassengerAccess
~~~~~~~~~~~~~~~

+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| Event / callback      | Kind      | Arguments                        | When it fires / meaning                                                                                             |
+=======================+===========+==================================+=====================================================================================================================+
| ``StateChanged``      | C#        | ``PassengerAccess, AccessState`` | When access sequencing changes.                                                                                     |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``Finished``          | C#        | ``PassengerAccess, bool``        | When an access attempt ends; the bool reports success. Check occupancy after cancellation/handover.                 |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``BeforeEnter``       | C#        | ``PassengerSeatContext``         | After reservation succeeds, before collision preparation, door requests and entry motion.                           |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``AfterEnter``        | C#        | ``PassengerSeatContext``         | After the entire entry sequence succeeds and its reservation/Target are cleared.                                    |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``BeforeExit``        | C#        | ``PassengerSeatContext``         | Before collision preparation, door requests and exit motion; occupancy is still retained.                           |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``AfterExit``         | C#        | ``PassengerSeatContext``         | After the entire exit sequence succeeds and its reservation/Target are cleared.                                     |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``Cancelled``         | C#        | ``PassengerSeatContext``         | After a prepared/started sequence is cancelled and reservation/Target cleared; context retains original identities. |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``EnterBegin``        | C#        | ``PassengerSeatContext``         | Once an admitted entry starts in Opening, after Before checks; seat reservation is held.                            |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``EnterInProgress``   | C#        | ``PassengerAccessProgress``      | After each entry motion sample in Moving, starting at zero; progress one is not whole-sequence completion.          |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``EnterFinished``     | C#        | ``PassengerSeatContext``         | Only after the entire entry succeeds, including the required door state and reservation/Target cleanup.             |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``EnterCancelled``    | C#        | ``PassengerSeatContext``         | After a reserved entry is cancelled or fails and cleanup finishes; an immediately rejected request emits nothing.   |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``ExitBegin``         | C#        | ``PassengerSeatContext``         | Once an admitted exit starts in Opening, after Before checks; seat reservation is held.                             |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``ExitInProgress``    | C#        | ``PassengerAccessProgress``      | After each exit motion sample in Moving, starting at zero; progress one is not whole-sequence completion.           |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``ExitFinished``      | C#        | ``PassengerSeatContext``         | Only after the entire exit succeeds, including the required door state and reservation/Target cleanup.              |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``ExitCancelled``     | C#        | ``PassengerSeatContext``         | After a reserved exit is cancelled or fails and cleanup finishes; an immediately rejected request emits nothing.    |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``started``           | Inspector | —                                | Inspector callback when access sequencing starts; no payload.                                                       |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``completed``         | Inspector | —                                | Inspector callback when access succeeds; no payload.                                                                |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``cancelled``         | Inspector | —                                | Inspector callback when access is cancelled; no payload.                                                            |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``onEnterBegin``      | Inspector | —                                | Counterpart of ``EnterBegin``; no arguments.                                                                        |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``onEnterInProgress`` | Inspector | ``float``                        | Counterpart of ``EnterInProgress``; normalized motion time 0..1.                                                    |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``onEnterFinish``     | Inspector | —                                | Counterpart of ``EnterFinished``; no arguments.                                                                     |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``onEnterCancelled``  | Inspector | —                                | Counterpart of ``EnterCancelled``; no arguments.                                                                    |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``onExitBegin``       | Inspector | —                                | Counterpart of ``ExitBegin``; no arguments.                                                                         |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``onExitInProgress``  | Inspector | ``float``                        | Counterpart of ``ExitInProgress``; normalized motion time 0..1.                                                     |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``onExitFinish``      | Inspector | —                                | Counterpart of ``ExitFinished``; no arguments.                                                                      |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``onExitCancelled``   | Inspector | —                                | Counterpart of ``ExitCancelled``; no arguments.                                                                     |
+-----------------------+-----------+----------------------------------+---------------------------------------------------------------------------------------------------------------------+

Details: :ref:`PassengerAccess API <evs-api-passengeraccess--passengeraccess>`.

.. _evs-scripting-eventsreference--passengers:

Passengers
~~~~~~~~~~

+------------------+------+-------------------------------------------------------+-------------------------------------------------------------------------------------------+
| Event / callback | Kind | Arguments                                             | When it fires / meaning                                                                   |
+==================+======+=======================================================+===========================================================================================+
| ``Entered``      | C#   | ``PassengerSeat, PassengerBody``                      | After a body acquires a seat; includes both the seat and occupant.                        |
+------------------+------+-------------------------------------------------------+-------------------------------------------------------------------------------------------+
| ``Exited``       | C#   | ``PassengerSeat, PassengerBody, PassengerExitReason`` | After occupancy is released; includes seat, former occupant and exit reason.              |
+------------------+------+-------------------------------------------------------+-------------------------------------------------------------------------------------------+
| ``BeforeEnter``  | C#   | ``PassengerSeatContext``                              | Forwards the validated seat entry boundary before occupancy/controller assignment.        |
+------------------+------+-------------------------------------------------------+-------------------------------------------------------------------------------------------+
| ``AfterEnter``   | C#   | ``PassengerSeatContext``                              | After successful attachment and entry notifications; carries the seat/passenger context.  |
+------------------+------+-------------------------------------------------------+-------------------------------------------------------------------------------------------+
| ``BeforeExit``   | C#   | ``PassengerSeatContext``                              | Before an occupied seat detaches its passenger, including ejection and lifecycle cleanup. |
+------------------+------+-------------------------------------------------------+-------------------------------------------------------------------------------------------+
| ``AfterExit``    | C#   | ``PassengerSeatContext``                              | After detachment and exit notifications; before an ejection adds its velocity change.     |
+------------------+------+-------------------------------------------------------+-------------------------------------------------------------------------------------------+
| ``BeforeEject``  | C#   | ``PassengerSeatContext``                              | Before a seat starts ejection detachment; occupancy is still retained.                    |
+------------------+------+-------------------------------------------------------+-------------------------------------------------------------------------------------------+
| ``AfterEject``   | C#   | ``PassengerSeatContext``                              | After seat ejection and its built-in velocity change.                                     |
+------------------+------+-------------------------------------------------------+-------------------------------------------------------------------------------------------+

Details: :ref:`Passengers API <evs-api-passengercontrollers--passengers>`.

.. _evs-scripting-eventsreference--passengerseat:

PassengerSeat
~~~~~~~~~~~~~

+-----------------------+------+---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| Event / callback      | Kind | Arguments                                                           | When it fires / meaning                                                                       |
+=======================+======+=====================================================================+===============================================================================================+
| ``ControllerChanged`` | C#   | ``PassengerSeat, PassengerControllerType, PassengerControllerType`` | After a successful controller handover; does not synthesize another entry or exit.            |
+-----------------------+------+---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``Entered``           | C#   | ``PassengerBody``                                                   | After this seat acquires its occupant.                                                        |
+-----------------------+------+---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``ResetRequested``    | C#   | ``PassengerBody``                                                   | When a custom occupant receives a vehicle-reset request; the application performs its reset.  |
+-----------------------+------+---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``Exited``            | C#   | ``PassengerBody, PassengerExitReason``                              | After this seat releases occupancy; includes former occupant and exit reason.                 |
+-----------------------+------+---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``BeforeEnter``       | C#   | ``PassengerSeatContext``                                            | After admission checks, before occupancy/controller assignment; the seat is still empty.      |
+-----------------------+------+---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``AfterEnter``        | C#   | ``PassengerSeatContext``                                            | After successful attachment and Entered notifications.                                        |
+-----------------------+------+---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``BeforeExit``        | C#   | ``PassengerSeatContext``                                            | Before detachment while still occupied; includes exit, ejection, disable and destruction.     |
+-----------------------+------+---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``AfterExit``         | C#   | ``PassengerSeatContext``                                            | After detachment and Exited notifications; an ejection velocity change happens afterward.     |
+-----------------------+------+---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``BeforeEject``       | C#   | ``PassengerSeatContext``                                            | Before ejection detaches the still-seated occupant.                                           |
+-----------------------+------+---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``AfterEject``        | C#   | ``PassengerSeatContext``                                            | After ejection detachment and built-in velocity change; custom controllers own their physics. |
+-----------------------+------+---------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+

Details: :ref:`PassengerSeat API <evs-api-passengercontrollers--passengerseat>`.

.. _evs-scripting-eventsreference--pedalanimator:

PedalAnimator
~~~~~~~~~~~~~

+--------------------+-----------+-----------+----------------------------------------------------------------------------------------+
| Event / callback   | Kind      | Arguments | When it fires / meaning                                                                |
+====================+===========+===========+========================================================================================+
| ``onValueChanged`` | Inspector | ``float`` | After displayed pedal travel changes (0–1), including immediate positioning and reset. |
+--------------------+-----------+-----------+----------------------------------------------------------------------------------------+

Details: :ref:`PedalAnimator API <evs-api-interior--pedalanimator>`.

.. _evs-scripting-eventsreference--profileswitcher:

ProfileSwitcher
~~~~~~~~~~~~~~~

+----------------------------+-----------+---------------------------------------+--------------------------------------------------------------------------------------------------+
| Event / callback           | Kind      | Arguments                             | When it fires / meaning                                                                          |
+============================+===========+=======================================+==================================================================================================+
| ``ProfileChanged``         | C#        | ``DriveProfile``                      | After configuring an accepted target profile; an animated transition may still be in progress.   |
+----------------------------+-----------+---------------------------------------+--------------------------------------------------------------------------------------------------+
| ``ProfilesChanged``        | C#        | —                                     | After successful registration, removal or list replacement. Does not imply a strategy change.    |
+----------------------------+-----------+---------------------------------------+--------------------------------------------------------------------------------------------------+
| ``TransitionStarted``      | C#        | —                                     | After target configuration and animated-route initialization; immediate switches do not emit it. |
+----------------------------+-----------+---------------------------------------+--------------------------------------------------------------------------------------------------+
| ``TransitionBegan``        | C#        | ``ProfileTransition, string, string`` | Admitted transition component, source profile ID and destination profile ID.                     |
+----------------------------+-----------+---------------------------------------+--------------------------------------------------------------------------------------------------+
| ``TransitionAudioStopped`` | C#        | —                                     | Requests stopping transition presentation.                                                       |
+----------------------------+-----------+---------------------------------------+--------------------------------------------------------------------------------------------------+
| ``TransitionProgressed``   | C#        | ``float``                             | During animation, with normalized progress.                                                      |
+----------------------------+-----------+---------------------------------------+--------------------------------------------------------------------------------------------------+
| ``TransitionCompleted``    | C#        | —                                     | After animated transition completion, contact restoration and final presentation.                |
+----------------------------+-----------+---------------------------------------+--------------------------------------------------------------------------------------------------+
| ``TransitionInterrupted``  | C#        | —                                     | On disable during a transition, after finalizing the selected target and presentation.           |
+----------------------------+-----------+---------------------------------------+--------------------------------------------------------------------------------------------------+
| ``started``                | Inspector | —                                     | Inspector callback when an animated route starts.                                                |
+----------------------------+-----------+---------------------------------------+--------------------------------------------------------------------------------------------------+
| ``progressed``             | Inspector | ``float``                             | Inspector callback with normalized animation progress.                                           |
+----------------------------+-----------+---------------------------------------+--------------------------------------------------------------------------------------------------+
| ``completed``              | Inspector | —                                     | Inspector callback after animated route completion.                                              |
+----------------------------+-----------+---------------------------------------+--------------------------------------------------------------------------------------------------+

Details: :ref:`ProfileSwitcher API <evs-api-driveprofiles--profileswitcher>`.

.. _evs-scripting-eventsreference--propulsion:

Propulsion
~~~~~~~~~~

+------------------+------+-----------+-------------------------------------------------------------------------------------------------------------------------+
| Event / callback | Kind | Arguments | When it fires / meaning                                                                                                 |
+==================+======+===========+=========================================================================================================================+
| ``SpeedChanged`` | C#   | ``float`` | When visual propulsion spool changes (0 stopped to 1 full speed); not RPM, mechanical thrust or individual shaft speed. |
+------------------+------+-----------+-------------------------------------------------------------------------------------------------------------------------+

Details: :ref:`Propulsion API <evs-api-aircraft--propulsion>`.

.. _evs-scripting-eventsreference--propulsionjets:

PropulsionJets
~~~~~~~~~~~~~~

+------------------------+------+-----------+---------------------------------------------+
| Event / callback       | Kind | Arguments | When it fires / meaning                     |
+========================+======+===========+=============================================+
| ``JetsEnabledChanged`` | C#   | ``bool``  | When jet presentation availability changes. |
+------------------------+------+-----------+---------------------------------------------+

Details: :ref:`PropulsionJets API <evs-api-presentation--propulsionjets>`.

.. _evs-scripting-eventsreference--rearmirrors:

RearMirrors
~~~~~~~~~~~

+---------------------------+------+---------------+-----------------------------------------------+
| Event / callback          | Kind | Arguments     | When it fires / meaning                       |
+===========================+======+===============+===============================================+
| ``MirrorsEnabledChanged`` | C#   | ``bool``      | When whole-system mirror eligibility changes. |
+---------------------------+------+---------------+-----------------------------------------------+
| ``MirrorEnabledChanged``  | C#   | ``int, bool`` | When one mirror's eligibility changes.        |
+---------------------------+------+---------------+-----------------------------------------------+

Details: :ref:`RearMirrors API <evs-api-interior--rearmirrors>`.

.. _evs-scripting-eventsreference--rocket:

Rocket
~~~~~~

+------------------+------+---------------------+-------------------------------------+
| Event / callback | Kind | Arguments           | When it fires / meaning             |
+==================+======+=====================+=====================================+
| ``Exploded``     | C#   | ``Rocket, Vector3`` | At the rocket's explosion boundary. |
+------------------+------+---------------------+-------------------------------------+

Details: :ref:`Rocket API <evs-api-weapons--rocket>`.

.. _evs-scripting-eventsreference--rocketlauncher:

RocketLauncher
~~~~~~~~~~~~~~

+--------------------------+------+----------------------------+------------------------------------------------------------------------------------+
| Event / callback         | Kind | Arguments                  | When it fires / meaning                                                            |
+==========================+======+============================+====================================================================================+
| ``TriggerChanged``       | C#   | ``bool``                   | When held trigger intent changes.                                                  |
+--------------------------+------+----------------------------+------------------------------------------------------------------------------------+
| ``FiringEnabledChanged`` | C#   | ``bool``                   | When weapon firing availability changes.                                           |
+--------------------------+------+----------------------------+------------------------------------------------------------------------------------+
| ``Fired``                | C#   | ``RocketLauncher, Rocket`` | After an admitted shot launches a rocket; holding the trigger alone is not a shot. |
+--------------------------+------+----------------------------+------------------------------------------------------------------------------------+

Details: :ref:`RocketLauncher API <evs-api-weapons--rocketlauncher>`.

.. _evs-scripting-eventsreference--rotaryanimator:

RotaryAnimator
~~~~~~~~~~~~~~

+--------------------+-----------+-----------+---------------------------------------------------------------------------------------------------------------------+
| Event / callback   | Kind      | Arguments | When it fires / meaning                                                                                             |
+====================+===========+===========+=====================================================================================================================+
| ``ValueChanged``   | C#        | ``float`` | When SetValue changes the requested value in configured units; does not wait for visible rotation to settle.        |
+--------------------+-----------+-----------+---------------------------------------------------------------------------------------------------------------------+
| ``onValueChanged`` | Inspector | ``float`` | After the requested rotary value changes, in configured units; follows ValueChanged and does not wait for settling. |
+--------------------+-----------+-----------+---------------------------------------------------------------------------------------------------------------------+

Details: :ref:`RotaryAnimator API <evs-api-interior--rotaryanimator>`.

.. _evs-scripting-eventsreference--skidmarks:

Skidmarks
~~~~~~~~~

================ ==== ========= ==================================
Event / callback Kind Arguments When it fires / meaning
================ ==== ========= ==================================
``Cleared``      C#   —         After skidmark history is cleared.
================ ==== ========= ==================================

Details: :ref:`Skidmarks API <evs-api-presentation--skidmarks>`.

.. _evs-scripting-eventsreference--stabilization:

Stabilization
~~~~~~~~~~~~~

+------------------+------+---------------+--------------------------------------------------------------------------------------------------------------+
| Event / callback | Kind | Arguments     | When it fires / meaning                                                                                      |
+==================+======+===============+==============================================================================================================+
| ``Overturned``   | C#   | ``Telemetry`` | Raised once when sustained tilt qualifies; carries the telemetry snapshot at that transition.                |
+------------------+------+---------------+--------------------------------------------------------------------------------------------------------------+
| ``Recovered``    | C#   | ``Telemetry`` | Raised once when tilt falls below the recovery threshold; carries the telemetry snapshot at that transition. |
+------------------+------+---------------+--------------------------------------------------------------------------------------------------------------+

Details: :ref:`Stabilization API <evs-api-collisionsandstabilization--stabilization>`.

.. _evs-scripting-eventsreference--steering:

Steering
~~~~~~~~

+------------------+------+-----------+---------------------------------------------------------------------------------------+
| Event / callback | Kind | Arguments | When it fires / meaning                                                               |
+==================+======+===========+=======================================================================================+
| ``AngleChanged`` | C#   | ``float`` | When the resolved road-wheel angle changes, in degrees (not steering-column degrees). |
+------------------+------+-----------+---------------------------------------------------------------------------------------+

Details: :ref:`Steering API <evs-api-drivedynamics--steering>`.

.. _evs-scripting-eventsreference--suspension:

Suspension
~~~~~~~~~~

+----------------------+------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Event / callback     | Kind | Arguments        | When it fires / meaning                                                                                                                                                         |
+======================+======+==================+=================================================================================================================================================================================+
| ``Landed``           | C#   | ``LandingEvent`` | First upright wheel support after qualifying flight. Context includes height, air time, speed and impact data; assisted rebounds are marked. Independent of landing assistance. |
+----------------------+------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``LandingCompleted`` | C#   | ``LandingEvent`` | First support from all operational wheel rays after Landed; may be the same step. This does not mean suspension motion has settled.                                             |
+----------------------+------+------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Details: :ref:`Suspension API <evs-api-suspension--suspension>`.

.. _evs-scripting-eventsreference--switchanimator:

SwitchAnimator
~~~~~~~~~~~~~~

+-----------------------+-----------+--------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| Event / callback      | Kind      | Arguments          | When it fires / meaning                                                                                                                         |
+=======================+===========+====================+=================================================================================================================================================+
| ``ValueChanged``      | C#        | ``bool``           | When requested IsOn changes; negative and positive detents both count as on. Immediate synchronization is silent.                               |
+-----------------------+-----------+--------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| ``Switched``          | C#        | ``bool``           | When motion settles; both negative and positive detents report true.                                                                            |
+-----------------------+-----------+--------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| ``PositionChanged``   | C#        | ``SwitchPosition`` | When the requested detent changes; distinguishes all three positions.                                                                           |
+-----------------------+-----------+--------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| ``PositionReached``   | C#        | ``SwitchPosition`` | When motion settles at the requested detent.                                                                                                    |
+-----------------------+-----------+--------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| ``onValueChanged``    | Inspector | ``bool``           | After the binary IsOn request changes, following ValueChanged. Negative/positive detents both count as on; immediate synchronization is silent. |
+-----------------------+-----------+--------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
| ``onPositionChanged`` | Inspector | ``SwitchPosition`` | After a changed detent request, following PositionChanged; immediate synchronization is silent.                                                 |
+-----------------------+-----------+--------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+

Details: :ref:`SwitchAnimator API <evs-api-interior--switchanimator>`.

.. _evs-scripting-eventsreference--throttleanimator:

ThrottleAnimator
~~~~~~~~~~~~~~~~

+------------------+------+-----------+-----------------------------------------------------------------------------------------------+
| Event / callback | Kind | Arguments | When it fires / meaning                                                                       |
+==================+======+===========+===============================================================================================+
| ``ValueChanged`` | C#   | ``float`` | When the displayed throttle value changes during Step, including smoothing toward its target. |
+------------------+------+-----------+-----------------------------------------------------------------------------------------------+

Details: :ref:`ThrottleAnimator API <evs-api-interior--throttleanimator>`.

.. _evs-scripting-eventsreference--tirefeedback:

TireFeedback
~~~~~~~~~~~~

+--------------------------+------+-----------------------------+------------------------------------------------------------------------------------------------------------------------+
| Event / callback         | Kind | Arguments                   | When it fires / meaning                                                                                                |
+==========================+======+=============================+========================================================================================================================+
| ``Sampled``              | C#   | —                           | After TireFeedback updates its wheel/contact classification. No payload; read the component's current cached feedback. |
+--------------------------+------+-----------------------------+------------------------------------------------------------------------------------------------------------------------+
| ``WheelGroundedChanged`` | C#   | ``int, bool``               | When feedback grounded state changes; arguments are wheel index and the new state.                                     |
+--------------------------+------+-----------------------------+------------------------------------------------------------------------------------------------------------------------+
| ``WheelSurfaceChanged``  | C#   | ``int, TireSurfaceProfile`` | When a wheel selects a different presentation surface; its profile can be null.                                        |
+--------------------------+------+-----------------------------+------------------------------------------------------------------------------------------------------------------------+
| ``SkiddingChanged``      | C#   | ``bool``                    | When aggregate feedback skid state changes.                                                                            |
+--------------------------+------+-----------------------------+------------------------------------------------------------------------------------------------------------------------+

Details: :ref:`TireFeedback API <evs-api-events--tirefeedback>`.

.. _evs-scripting-eventsreference--tractioncontrol:

TractionControl
~~~~~~~~~~~~~~~

+-------------------+------+-----------+------------------------------------------------------------------------------+
| Event / callback  | Kind | Arguments | When it fires / meaning                                                      |
+===================+======+===========+==============================================================================+
| ``ActiveChanged`` | C#   | ``bool``  | When resolved traction-control intervention changes between active/inactive. |
+-------------------+------+-----------+------------------------------------------------------------------------------+

Details: :ref:`TractionControl API <evs-api-drivedynamics--tractioncontrol>`.

.. _evs-scripting-eventsreference--trailer:

Trailer
~~~~~~~

+----------------------+------+-----------+----------------------------------------------------+
| Event / callback     | Kind | Arguments | When it fires / meaning                            |
+======================+======+===========+====================================================+
| ``ConnectionBroken`` | C#   | —         | When a trailer's active hitch relationship breaks. |
+----------------------+------+-----------+----------------------------------------------------+

Details: :ref:`Trailer API <evs-api-towing--trailer>`.

.. _evs-scripting-eventsreference--transmission:

Transmission
~~~~~~~~~~~~

+------------------+------+----------------------+------------------------------------------------------------------------+
| Event / callback | Kind | Arguments            | When it fires / meaning                                                |
+==================+======+======================+========================================================================+
| ``ModeChanged``  | C#   | ``TransmissionMode`` | After transmission mode changes and its gearbox connection is applied. |
+------------------+------+----------------------+------------------------------------------------------------------------+

Details: :ref:`Transmission API <evs-api-drivedynamics--transmission>`.

.. _evs-scripting-eventsreference--vehiclebodypart:

VehicleBodyPart
~~~~~~~~~~~~~~~

+------------------------+------+---------------------+------------------------------------------------------------------------------------------------------------------------+
| Event / callback       | Kind | Arguments           | When it fires / meaning                                                                                                |
+========================+======+=====================+========================================================================================================================+
| ``OpeningStarted``     | C#   | —                   | Once before an opening operation moves the pose. No payload; interruptions never imply completion.                     |
+------------------------+------+---------------------+------------------------------------------------------------------------------------------------------------------------+
| ``OpeningCompleted``   | C#   | —                   | Once after the actual pose reaches the requested opening target. No payload; physical hinges use Completion Tolerance. |
+------------------------+------+---------------------+------------------------------------------------------------------------------------------------------------------------+
| ``ClosingStarted``     | C#   | —                   | Once before a closing operation moves the pose.                                                                        |
+------------------------+------+---------------------+------------------------------------------------------------------------------------------------------------------------+
| ``ClosingCompleted``   | C#   | —                   | Once after the actual pose reaches the requested closing target.                                                       |
+------------------------+------+---------------------+------------------------------------------------------------------------------------------------------------------------+
| ``OpenChanged``        | C#   | ``bool``            | When the part's requested open state changes.                                                                          |
+------------------------+------+---------------------+------------------------------------------------------------------------------------------------------------------------+
| ``PhysicsChanged``     | C#   | ``bool``            | When the part's ``usePhysics`` policy changes.                                                                         |
+------------------------+------+---------------------+------------------------------------------------------------------------------------------------------------------------+
| ``Released``           | C#   | —                   | After the body part is released from vehicle-owned motion.                                                             |
+------------------------+------+---------------------+------------------------------------------------------------------------------------------------------------------------+
| ``MotionOccurred``     | C#   | ``PartMotionEvent`` | Reports an admitted movement phase to optional presentation receivers.                                                 |
+------------------------+------+---------------------+------------------------------------------------------------------------------------------------------------------------+
| ``MotionAudioStopped`` | C#   | —                   | Requests stopping movement audio after interruption or disable.                                                        |
+------------------------+------+---------------------+------------------------------------------------------------------------------------------------------------------------+

Details: :ref:`VehicleBodyPart API <evs-api-damage--vehiclebodypart>`.

.. _evs-scripting-eventsreference--vehiclecontroller:

VehicleController
~~~~~~~~~~~~~~~~~

+------------------------------+------+-------------------+-------------------------------------------------------------------------------------------------------------+
| Event / callback             | Kind | Arguments         | When it fires / meaning                                                                                     |
+==============================+======+===================+=============================================================================================================+
| ``Collided``                 | C#   | ``Collision``     | During Unity collision entry; Collision is live callback data, so copy values before deferring work.        |
+------------------------------+------+-------------------+-------------------------------------------------------------------------------------------------------------+
| ``Impacted``                 | C#   | ``Impact``        | After copying collision contact/velocity/impulse data; the Impact snapshot can be retained.                 |
+------------------------------+------+-------------------+-------------------------------------------------------------------------------------------------------------+
| ``AfterPhysicsStep``         | C#   | ``Telemetry``     | After the module pipeline and telemetry sampling; this is not a callback after native Physics.Simulate.     |
+------------------------------+------+-------------------+-------------------------------------------------------------------------------------------------------------+
| ``Teleported``               | C#   | ``Pose``          | After world pose and occupants have been synchronized.                                                      |
+------------------------------+------+-------------------+-------------------------------------------------------------------------------------------------------------+
| ``CommandSampled``           | C#   | ``Command``       | After the selected provider is sampled.                                                                     |
+------------------------------+------+-------------------+-------------------------------------------------------------------------------------------------------------+
| ``DriveProfileChanged``      | C#   | ``DriveProfile``  | After an immediate profile change is configured successfully.                                               |
+------------------------------+------+-------------------+-------------------------------------------------------------------------------------------------------------+
| ``ConfigurationChanged``     | C#   | —                 | After validated wheel/module configuration is applied.                                                      |
+------------------------------+------+-------------------+-------------------------------------------------------------------------------------------------------------+
| ``WheelAvailabilityChanged`` | C#   | ``int, bool``     | After a wheel availability change; arguments are configured wheel index and new availability.               |
+------------------------------+------+-------------------+-------------------------------------------------------------------------------------------------------------+
| ``InputSourceChanged``       | C#   | ``MonoBehaviour`` | After assigning input ownership.                                                                            |
+------------------------------+------+-------------------+-------------------------------------------------------------------------------------------------------------+
| ``ModuleRegistered``         | C#   | ``VehicleModule`` | After registration/configuration.                                                                           |
+------------------------------+------+-------------------+-------------------------------------------------------------------------------------------------------------+
| ``ModuleUnregistered``       | C#   | ``VehicleModule`` | After removal from future pipeline membership; independent callbacks may still need disabling.              |
+------------------------------+------+-------------------+-------------------------------------------------------------------------------------------------------------+
| ``WheelAttachmentChanged``   | C#   | ``Wheel, bool``   | Forwards an owned Wheel attachment change after its per-wheel notification; bool is the new attached state. |
+------------------------------+------+-------------------+-------------------------------------------------------------------------------------------------------------+
| ``Repaired``                 | C#   | —                 | After RepairAll finishes in-place repair and actuator cleanup; Teleport alone does not emit it.             |
+------------------------------+------+-------------------+-------------------------------------------------------------------------------------------------------------+

Details: :ref:`VehicleController API <evs-api-core--vehiclecontroller>`.

.. _evs-scripting-eventsreference--vehiclehandle:

VehicleHandle
~~~~~~~~~~~~~

+--------------------------+-----------+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| Event / callback         | Kind      | Arguments                | When it fires / meaning                                                                                                         |
+==========================+===========+==========================+=================================================================================================================================+
| ``ContactStarted``       | C#        | ``HandleContactContext`` | Once on a not-touching to touching transition; C# event runs before the matching UnityEvent.                                    |
+--------------------------+-----------+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``ContactUpdated``       | C#        | ``HandleContactContext`` | Once per contact sample while touching, including its start sample. Payload identifies handle, seat, occupant, part and target. |
+--------------------------+-----------+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``ContactEnded``         | C#        | ``HandleContactContext`` | Once when contact is lost or released (including exit/disable/rebinding). Payload retains the original occupant identity.       |
+--------------------------+-----------+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``ValueChangeStarted``   | C#        | ``HandleValueContext``   | Once when a significant value change or explicit BeginValueChange starts activity.                                              |
+--------------------------+-----------+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``ValueChanging``        | C#        | ``HandleValueContext``   | Each active changed/manual sample; does not imply contact or commit a gameplay action.                                          |
+--------------------------+-----------+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``ValueChangeStopped``   | C#        | ``HandleValueContext``   | Once when the value settles for valueStopDelay, explicit EndValueChange runs or the handle is disabled/destroyed.               |
+--------------------------+-----------+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``onContactStarted``     | Inspector | ``HandleContactContext`` | Inspector-configurable counterpart of ContactStarted. Runs after the C# event for the same phase.                               |
+--------------------------+-----------+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``onContactUpdated``     | Inspector | ``HandleContactContext`` | Inspector-configurable counterpart of ContactUpdated. Runs after the C# event for the same phase.                               |
+--------------------------+-----------+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``onContactEnded``       | Inspector | ``HandleContactContext`` | Inspector-configurable counterpart of ContactEnded. Runs after the C# event for the same phase.                                 |
+--------------------------+-----------+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``onValueChangeStarted`` | Inspector | ``HandleValueContext``   | Inspector-configurable counterpart of ValueChangeStarted. Runs after the C# event for the same phase.                           |
+--------------------------+-----------+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``onValueChanging``      | Inspector | ``HandleValueContext``   | Inspector-configurable counterpart of ValueChanging. Runs after the C# event for the same phase.                                |
+--------------------------+-----------+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+
| ``onValueChangeStopped`` | Inspector | ``HandleValueContext``   | Inspector-configurable counterpart of ValueChangeStopped. Runs after the C# event for the same phase.                           |
+--------------------------+-----------+--------------------------+---------------------------------------------------------------------------------------------------------------------------------+

Details: :ref:`VehicleHandle API <evs-api-handles--vehiclehandle>`.

.. _evs-scripting-eventsreference--vehiclemeshdeformation:

VehicleMeshDeformation
~~~~~~~~~~~~~~~~~~~~~~

+------------------------+------+-----------+------------------------------------------------------------------------------------------------------+
| Event / callback       | Kind | Arguments | When it fires / meaning                                                                              |
+========================+======+===========+======================================================================================================+
| ``DeformationChanged`` | C#   | —         | After pending deformation geometry is uploaded. No payload; inspect owned geometry at this boundary. |
+------------------------+------+-----------+------------------------------------------------------------------------------------------------------+
| ``Restored``           | C#   | —         | After deformable shape is restored to rest geometry.                                                 |
+------------------------+------+-----------+------------------------------------------------------------------------------------------------------+

Details: :ref:`VehicleMeshDeformation API <evs-api-damage--vehiclemeshdeformation>`.

.. _evs-scripting-eventsreference--vehiclemodule:

VehicleModule
~~~~~~~~~~~~~

+--------------------+------+---------------------------------------+-----------------------------------------------+
| Event / callback   | Kind | Arguments                             | When it fires / meaning                       |
+====================+======+=======================================+===============================================+
| ``EnabledChanged`` | C#   | ``bool``                              | After ``SetEnabled`` changes the module flag. |
+--------------------+------+---------------------------------------+-----------------------------------------------+
| ``Configured``     | C#   | ``VehicleController``                 | After controller-driven module configuration. |
+--------------------+------+---------------------------------------+-----------------------------------------------+
| ``Stepped``        | C#   | ``VehicleController, Command, float`` | After this registered module has stepped.     |
+--------------------+------+---------------------------------------+-----------------------------------------------+

Details: :ref:`VehicleModule API <evs-api-modules--vehiclemodule>`.

.. _evs-scripting-eventsreference--waterinteraction:

WaterInteraction
~~~~~~~~~~~~~~~~

+-------------------------------+------+-------------------+----------------------------------------------------------------------------+
| Event / callback              | Kind | Arguments         | When it fires / meaning                                                    |
+===============================+======+===================+============================================================================+
| ``InteractionEnabledChanged`` | C#   | ``bool``          | When the master water-interaction gate changes.                            |
+-------------------------------+------+-------------------+----------------------------------------------------------------------------+
| ``ProviderChanged``           | C#   | ``WaterProvider`` | When the assigned water provider changes; null means no assigned provider. |
+-------------------------------+------+-------------------+----------------------------------------------------------------------------+
| ``SubmergedChanged``          | C#   | ``bool``          | When sampled body-center submergence changes.                              |
+-------------------------------+------+-------------------+----------------------------------------------------------------------------+

Details: :ref:`WaterInteraction API <evs-api-water--waterinteraction>`.

.. _evs-scripting-eventsreference--weaponbarrel:

WeaponBarrel
~~~~~~~~~~~~

+--------------------------+------+---------------------------------+------------------------------------------------------------------+
| Event / callback         | Kind | Arguments                       | When it fires / meaning                                          |
+==========================+======+=================================+==================================================================+
| ``TriggerChanged``       | C#   | ``bool``                        | When held trigger intent changes.                                |
+--------------------------+------+---------------------------------+------------------------------------------------------------------+
| ``FiringEnabledChanged`` | C#   | ``bool``                        | When weapon firing availability changes.                         |
+--------------------------+------+---------------------------------+------------------------------------------------------------------+
| ``Fired``                | C#   | ``WeaponBarrel, MonoBehaviour`` | After an admitted shot creates/releases its projectile or store. |
+--------------------------+------+---------------------------------+------------------------------------------------------------------+

Details: :ref:`WeaponBarrel API <evs-api-weapons--weaponbarrel>`.

.. _evs-scripting-eventsreference--wheel:

Wheel
~~~~~

+-----------------------+------+-----------------+---------------------------------------------------------------------------------------------------+
| Event / callback      | Kind | Arguments       | When it fires / meaning                                                                           |
+=======================+======+=================+===================================================================================================+
| ``AttachmentChanged`` | C#   | ``Wheel, bool`` | After attachment state and collider/actuator availability update; bool is the new attached state. |
+-----------------------+------+-----------------+---------------------------------------------------------------------------------------------------+

Details: :ref:`Wheel API <evs-api-wheelcontact--wheel>`.

.. _evs-scripting-eventsreference--wheellift:

WheelLift
~~~~~~~~~

+----------------------+------+-----------+--------------------------------------------------------------------------------------------+
| Event / callback     | Kind | Arguments | When it fires / meaning                                                                    |
+======================+======+===========+============================================================================================+
| ``WheelLiftStarted`` | C#   | —         | Assistance begins.                                                                         |
+----------------------+------+-----------+--------------------------------------------------------------------------------------------+
| ``WheelLiftStopped`` | C#   | —         | Assistance ends after controlled lowering, or immediately on reset/disable/excessive tilt. |
+----------------------+------+-----------+--------------------------------------------------------------------------------------------+
| ``StateChanged``     | C#   | ``bool``  | New assistance state.                                                                      |
+----------------------+------+-----------+--------------------------------------------------------------------------------------------+

Details: :ref:`WheelLift API <evs-api-wheellift--wheellift>`.

.. _evs-scripting-eventsreference--wipers:

Wipers
~~~~~~

+--------------------------+------+------------------------+-------------------------------------------------------------------------------------------------------------------+
| Event / callback         | Kind | Arguments              | When it fires / meaning                                                                                           |
+==========================+======+========================+===================================================================================================================+
| ``StrokeStarted``        | C#   | ``bool``               | When a wiper stroke starts.                                                                                       |
+--------------------------+------+------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``RunningChanged``       | C#   | ``bool``               | When the wiper running request changes.                                                                           |
+--------------------------+------+------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``SpeedChanged``         | C#   | ``float``              | After ``SetSpeed`` changes requested wiper speed.                                                                 |
+--------------------------+------+------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``Parked``               | C#   | —                      | When wipers reach their parked state.                                                                             |
+--------------------------+------+------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``WiperStrokeStarted``   | C#   | ``string, bool``       | Reports entry ID and stroke direction: false for outward, true for return. Entries have independent phase clocks. |
+--------------------------+------+------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``WiperRunningChanged``  | C#   | ``string, bool``       | After an API changes an entry's effective running request; payload is its ID and new bool request.                |
+--------------------------+------+------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``WiperSpeedChanged``    | C#   | ``string, float``      | After an API changes an entry's effective speed; payload is its ID and cycles per minute.                         |
+--------------------------+------+------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``WiperParked``          | C#   | ``string``             | When an entry reaches/is immediately placed at its parked pose; payload is its ID.                                |
+--------------------------+------+------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``StrokeAudioRequested`` | C#   | ``Wiper, bool, float`` | Specific wiper, stroke direction and resolved cycles per minute for optional audio.                               |
+--------------------------+------+------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``WiperRemoved``         | C#   | ``Wiper``              | Reports an entry removed from the mechanism so optional receivers can release its resources.                      |
+--------------------------+------+------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``AudioStopped``         | C#   | —                      | Requests stopping wiper audio.                                                                                    |
+--------------------------+------+------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``StrokeBatchStarted``   | C#   | —                      | Begins a mechanism tick; receivers can deduplicate shared voices within this batch.                               |
+--------------------------+------+------------------------+-------------------------------------------------------------------------------------------------------------------+

Details: :ref:`Wipers API <evs-api-wipers--wipers>`.

.. _evs-scripting-eventsreference--demo-and-example-classes:

Demo and example classes
------------------------

These classes belong to the optional Demo sample, outside the runtime assembly.

.. _evs-scripting-eventsreference--democamerarig:

DemoCameraRig
~~~~~~~~~~~~~

+--------------------------+----------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| Event                    | Kind     | Arguments          | When it fires / meaning                                                                                                                             |
+==========================+==========+====================+=====================================================================================================================================================+
| ``ModeChanged``          | C#       | ``ViewMode``       | After a changed camera view mode is applied.                                                                                                        |
+--------------------------+----------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``TargetChanged``        | C#       | ``Transform``      | After retargeting the demo camera; null releases the target.                                                                                        |
+--------------------------+----------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| ``PointerCaptureFilter`` | C# query | ``Vector2 → bool`` | CanCaptureAt checks a screen position. Every invoked filter must allow capture; the first false vetoes it. This is not a state-change notification. |
+--------------------------+----------+--------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-scripting-eventsreference--demovehicleselector:

DemoVehicleSelector
~~~~~~~~~~~~~~~~~~~

+--------------+------+-----------------------+------------------------------------------------------------------------------------------------------------------+
| Event        | Kind | Arguments             | When it fires / meaning                                                                                          |
+==============+======+=======================+==================================================================================================================+
| ``Selected`` | C#   | ``VehicleController`` | After a valid selection updates input routing, camera target and HUD; selecting the same index can notify again. |
+--------------+------+-----------------------+------------------------------------------------------------------------------------------------------------------+

.. _evs-scripting-eventsreference--projectile:

Projectile
~~~~~~~~~~

+--------------+------+----------------------------------+-----------------------------------------------------------------------------------------------------+
| Event        | Kind | Arguments                        | When it fires / meaning                                                                             |
+==============+======+==================================+=====================================================================================================+
| ``Impacted`` | C#   | ``Projectile, ProjectileImpact`` | Once on an accepted collision, after copying impact data and before application-owned hit handling. |
+--------------+------+----------------------------------+-----------------------------------------------------------------------------------------------------+

For sample setup, see :doc:`Demo </Demo>`. For subscription lifetime and complete handler examples, see :ref:`Events and telemetry <evs-scripting-events--subscribe-to-a-components-events>`.
