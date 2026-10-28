.. _evs-api-passengeraccess--animated-access-api:

Animated access API
===================

Read :doc:`the system explanation </Scripting/PassengerAccess>` for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from ``MonoBehaviour``, ``Object`` or ``ScriptableObject`` are documented by Unity.

.. _evs-api-passengeraccess--types:

Types
-----

-  :ref:`AccessAnimationEvents <evs-api-passengeraccess--accessanimationevents>`
-  :ref:`AccessAnimationProfile <evs-api-passengeraccess--accessanimationprofile>`
-  :ref:`AccessMotion <evs-api-passengeraccess--accessmotion>`
-  :ref:`AccessSide <evs-api-passengeraccess--accessside>`
-  :ref:`AccessState <evs-api-passengeraccess--accessstate>`
-  :ref:`HumanoidAccessMotion <evs-api-passengeraccess--humanoidaccessmotion>`
-  :ref:`PassengerAccess <evs-api-passengeraccess--passengeraccess>`
-  :ref:`SeatAccess <evs-api-passengeraccess--seataccess>`

.. _evs-api-passengeraccess--accessanimationevents:

AccessAnimationEvents
---------------------

**Runtime/World/Passengers/Access/AccessAnimationEvents.cs**

Relays animation access markers into the sequence.

**Inherits / implements:** ``MonoBehaviour``.

.. _evs-api-passengeraccess--methods:

Methods
~~~~~~~

+-------------------------------------------+-----------------------------------------------------------------------------+----------------------------------+
| Signature                                 | Role and behavior                                                           | Arguments and result             |
+===========================================+=============================================================================+==================================+
| ``public virtual void AccessOpenDoor()``  | Delivers an animation marker requesting opening of the current access door. | No arguments; no returned value. |
+-------------------------------------------+-----------------------------------------------------------------------------+----------------------------------+
| ``public virtual void AccessCloseDoor()`` | Delivers an animation marker requesting closure of the current access door. | No arguments; no returned value. |
+-------------------------------------------+-----------------------------------------------------------------------------+----------------------------------+

.. _evs-api-passengeraccess--accessanimationprofile:

AccessAnimationProfile
----------------------

**Runtime/World/Passengers/Access/AccessAnimationProfile.cs**

Stores animation states, references and timing configuration.

**Inherits / implements:** ``ScriptableObject``.

.. _evs-api-passengeraccess--state-and-configuration:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Member                                          | Meaning                                                                                                                   |
+=================================================+===========================================================================================================================+
| ``public RuntimeAnimatorController controller`` | Authored controller used by ``AccessAnimationProfile``.                                                                   |
+-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public int layer``                            | Authored layer used by ``AccessAnimationProfile``.                                                                        |
+-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public string standingState``                 | Authored standing state used by ``AccessAnimationProfile``. Initial value: ``"Base Layer.Idle"``.                         |
+-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public string seatedState``                   | Authored seated state used by ``AccessAnimationProfile``. Initial value: ``"Base Layer.Seated"``.                         |
+-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public string enterState``                    | Authored enter state used by ``AccessAnimationProfile``. Initial value: ``"Base Layer.Enter In"``.                        |
+-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public string exitState``                     | Authored exit state used by ``AccessAnimationProfile``. Initial value: ``"Base Layer.Enter Out"``.                        |
+-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public string enterTrigger``                  | Authored enter trigger used by ``AccessAnimationProfile``. Initial value: ``"EnterIn"``.                                  |
+-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public string exitTrigger``                   | Authored exit trigger used by ``AccessAnimationProfile``. Initial value: ``"EnterOut"``.                                  |
+-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public AnimationClip standingClip``           | Authored standing clip used by ``AccessAnimationProfile``.                                                                |
+-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public AnimationClip seatedClip``             | Authored seated clip used by ``AccessAnimationProfile``.                                                                  |
+-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public AnimationClip enterClip``              | Authored enter clip used by ``AccessAnimationProfile``.                                                                   |
+-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public AnimationClip exitClip``               | Authored exit clip used by ``AccessAnimationProfile``.                                                                    |
+-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public Vector2 enterRange``                   | Authored enter range used by ``AccessAnimationProfile``. Initial value: ``new Vector2(0, 1)``.                            |
+-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public Vector2 exitRange``                    | Authored exit range used by ``AccessAnimationProfile``. Initial value: ``new Vector2(0, 1)``.                             |
+-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public float playbackSpeed``                  | Authored playback speed used by ``AccessAnimationProfile``. Initial value: ``1``.                                         |
+-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public float transitionAllowance``            | Authored transition allowance used by ``AccessAnimationProfile``. Initial value: ``.2f``.                                 |
+-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public float completionTimeout``              | Additional time allowed before an unfinished access operation is cancelled, in seconds.                                   |
+-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public float horizontalScale``                | Authored horizontal scale used by ``AccessAnimationProfile``. Initial value: ``1``.                                       |
+-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public AnimationCurve enterPlacement``        | Weight of the outside alignment during entry; fades before the character sits.                                            |
+-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public AnimationCurve exitPlacement``         | Authored exit placement used by ``AccessAnimationProfile``. Initial value: ``AnimationCurve.EaseInOut(.2f, 0, .85f, 1)``. |
+-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public AnimationCurve seatPose``              | Blend to the physical seat pose. Reach 1 before handing over to seat physics.                                             |
+-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public float footBlendSeconds``               | Authored foot blend seconds used by ``AccessAnimationProfile``. Initial value: ``.16f``.                                  |
+-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public float plantHeight``                    | Authored plant height used by ``AccessAnimationProfile``. Initial value: ``.06f``.                                        |
+-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public float plantSpeed``                     | Authored plant speed used by ``AccessAnimationProfile``. Initial value: ``.3f``.                                          |
+-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public float releaseEntryFeet``               | Normalized boarding progress after which standing foot plants are released.                                               |
+-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public bool holdFeetWhileIdle``               | Disable when an application locomotion / ground IK system owns standing feet.                                             |
+-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool HasBindings { get; }``    | Current has bindings predicate; read it instead of maintaining a second application flag.                                 |
+-------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-passengeraccess--accessmotion:

AccessMotion
------------

**Runtime/World/Passengers/Access/AccessMotion.cs**

Replaceable character-motion adapter called by ``PassengerAccess`` during entry/exit.

**Inherits / implements:** ``MonoBehaviour``.

.. _evs-api-passengeraccess--methods-1:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                  | Role and behavior                                                                                                                                    | Arguments and result                                                                                                                                                                                                                                                              |
+============================================================================================+======================================================================================================================================================+===================================================================================================================================================================================================================================================================================+
| ``public abstract bool Begin(SeatAccess access, PassengerBody passenger, bool entering)``  | Attempts to begin character motion for the selected endpoint/body/direction. False rejects the adapter operation before successful motion ownership. | ``access`` — Access, interpreted by this operation in the declared type. ``passenger`` — Character body receiving motion/attachment. ``entering`` — ``true`` for entry motion; ``false`` for exit. **Returns:** ``true`` if the operation starts; ``false`` if admission fails.   |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public abstract void End(bool completed)``                                               | Ends the motion adapter, using the completion flag to restore or hand over its owned state.                                                          | ``completed`` — ``true`` for successful motion completion; ``false`` for interruption/cleanup.                                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool CanPlay(SeatAccess access, PassengerBody passenger, bool entering)`` | Checks whether the motion adapter can play this access operation for the supplied body and direction.                                                | ``access`` — Access, interpreted by this operation in the declared type. ``passenger`` — Character body receiving motion/attachment. ``entering`` — ``true`` for entry motion; ``false`` for exit. **Returns:** ``true`` when the described condition holds; ``false`` otherwise. |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float GetDuration(SeatAccess access, bool entering)``                     | Returns nominal access-motion duration for this endpoint and direction.                                                                              | ``access`` — Access, interpreted by this operation in the declared type. ``entering`` — ``true`` for entry motion; ``false`` for exit. **Returns:** Computed float in the operation's documented unit/domain.                                                                     |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public abstract void Sample(float normalizedTime)``                                      | Receives normalized access progress from ``PassengerAccess``; implement pose/motion sampling without choosing a new seat.                            | ``normalizedTime`` — Normalized access progress supplied by the owner.                                                                                                                                                                                                            |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-passengeraccess--state-and-configuration-1:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------+-------------------------------------------------------------------------------------------+
| Member                                                   | Meaning                                                                                   |
+==========================================================+===========================================================================================+
| ``public virtual bool IsComplete { get; }``              | Current is complete predicate; read it instead of maintaining a second application flag.  |
+----------------------------------------------------------+-------------------------------------------------------------------------------------------+
| ``public virtual float CompletionTimeout { get; }``      | Additional seconds permitted after nominal motion duration before cancellation.           |
+----------------------------------------------------------+-------------------------------------------------------------------------------------------+
| ``public virtual bool UsesAnimationDoorEvents { get; }`` | Whether door requests must come from animation markers instead of timed fallback control. |
+----------------------------------------------------------+-------------------------------------------------------------------------------------------+

.. _evs-api-passengeraccess--accessside:

AccessSide
----------

**Runtime/World/Passengers/Access/SeatAccess.cs**

Defines the allowed access side choices used by this topic.

.. _evs-api-passengeraccess--values:

Values
~~~~~~

-  ``Left``
-  ``Right``
-  ``Custom``

.. _evs-api-passengeraccess--accessstate:

AccessState
-----------

**Runtime/World/Passengers/Access/PassengerAccess.cs**

Defines the allowed access state choices used by this topic.

.. _evs-api-passengeraccess--values-1:

Values
~~~~~~

-  ``Idle``
-  ``Opening``
-  ``Moving``
-  ``Closing``

.. _evs-api-passengeraccess--humanoidaccessmotion:

HumanoidAccessMotion
--------------------

**Runtime/World/Passengers/Access/HumanoidAccessMotion.cs**

Built-in Animator-based humanoid access implementation.

**Inherits / implements:** :ref:`AccessMotion <evs-api-passengeraccess--accessmotion>`.

.. _evs-api-passengeraccess--methods-2:

Methods
~~~~~~~

+-----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                     | Role and behavior                                                                                                                       | Arguments and result                                                                                                                                                                                                                                                                 |
+===============================================================================================+=========================================================================================================================================+======================================================================================================================================================================================================================================================================================+
| ``public virtual void Configure(AccessAnimationProfile profile)``                             | Selects the ``AccessAnimationProfile`` used by subsequent access motion.                                                                | ``profile`` — Movement/surface configuration, according to its declared type.                                                                                                                                                                                                        |
+-----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool Begin(SeatAccess target, PassengerBody passenger, bool isEntering)``   | Validates humanoid Animator, clips, mapped feet/pelvis and non-ragdoll state, then captures character/Animator state for access motion. | ``target`` — Configured target object/point; see declared type and owner. ``passenger`` — Character body receiving motion/attachment. ``isEntering`` — ``true`` for entry motion; ``false`` for exit. **Returns:** ``true`` if the operation starts; ``false`` if admission fails.   |
+-----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void End(bool completed)``                                                  | Ends the motion adapter, using the completion flag to restore or hand over its owned state.                                             | ``completed`` — ``true`` for successful motion completion; ``false`` for interruption/cleanup.                                                                                                                                                                                       |
+-----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float Duration(bool entering)``                                              | Returns the built-in humanoid motion duration for the selected access direction/configuration.                                          | ``entering`` — ``true`` for entry motion; ``false`` for exit. **Returns:** Computed float in the operation's documented unit/domain.                                                                                                                                                 |
+-----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override bool CanPlay(SeatAccess target, PassengerBody passenger, bool isEntering)`` | Checks whether the motion adapter can play this access operation for the supplied body and direction.                                   | ``target`` — Configured target object/point; see declared type and owner. ``passenger`` — Character body receiving motion/attachment. ``isEntering`` — ``true`` for entry motion; ``false`` for exit. **Returns:** ``true`` when the described condition holds; ``false`` otherwise. |
+-----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override float GetDuration(SeatAccess target, bool isEntering)``                     | Returns nominal access-motion duration for this endpoint and direction.                                                                 | ``target`` — Configured target object/point; see declared type and owner. ``isEntering`` — ``true`` for entry motion; ``false`` for exit. **Returns:** Computed float in the operation's documented unit/domain.                                                                     |
+-----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Sample(float normalizedTime)``                                         | Evaluates the access motion or water style at the supplied normalized/world sample coordinates.                                         | ``normalizedTime`` — Normalized access progress supplied by the owner.                                                                                                                                                                                                               |
+-----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ReleaseIdleFeet()``                                                     | Releases temporary idle-foot ownership held during humanoid access motion.                                                              | No arguments; no returned value.                                                                                                                                                                                                                                                     |
+-----------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-passengeraccess--state-and-configuration-2:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------+-------------------------------------------------------------------------------------------+
| Member                                                    | Meaning                                                                                   |
+===========================================================+===========================================================================================+
| ``public AccessAnimationProfile defaultProfile``          | Fallback profile; a ``SeatAccess`` profile takes precedence for each request.             |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------+
| ``public virtual AnimationClip enterClip { get; }``       | Read-only/resolved enter clip for ``HumanoidAccessMotion``.                               |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------+
| ``public virtual AnimationClip exitClip { get; }``        | Read-only/resolved exit clip for ``HumanoidAccessMotion``.                                |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------+
| ``public virtual AnimationClip idleClip { get; }``        | Read-only/resolved idle clip for ``HumanoidAccessMotion``.                                |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------+
| ``public virtual bool LeftFootPlanted { get; }``          | Read-only/resolved left foot planted for ``HumanoidAccessMotion``.                        |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------+
| ``public virtual bool RightFootPlanted { get; }``         | Read-only/resolved right foot planted for ``HumanoidAccessMotion``.                       |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------+
| ``public virtual Vector3 LeftFootLock { get; }``          | Current left planted-foot support point in world space.                                   |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------+
| ``public virtual Vector3 RightFootLock { get; }``         | Current right planted-foot support point in world space.                                  |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------+
| ``public override bool UsesAnimationDoorEvents { get; }`` | Whether door requests must come from animation markers instead of timed fallback control. |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------+
| ``public override bool IsComplete { get; }``              | Current is complete predicate; read it instead of maintaining a second application flag.  |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------+
| ``public override float CompletionTimeout { get; }``      | Additional seconds permitted after nominal motion duration before cancellation.           |
+-----------------------------------------------------------+-------------------------------------------------------------------------------------------+

.. _evs-api-passengeraccess--passengeraccess:

PassengerAccess
---------------

**Runtime/World/Passengers/Access/PassengerAccess.cs**

Owns the entry/exit state machine, reservation and cancellation.

**Inherits / implements:** ``MonoBehaviour``.

.. _evs-api-passengeraccess--methods-3:

Methods
~~~~~~~

+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                           | Role and behavior                                                                                                                                    | Arguments and result                                                                                                                                                              |
+=====================================================+======================================================================================================================================================+===================================================================================================================================================================================+
| ``public virtual bool TryEnter(SeatAccess access)`` | Admits an asynchronous entry and reserves the endpoint/seat. True means started, not occupied/completed; observe Finished and actual seat occupancy. | ``access`` — Access, interpreted by this operation in the declared type. **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values. |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryExit()``                   | Admits asynchronous departure. Seat release and motion completion occur at different boundaries; observe Finished for sequence outcome.              | **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values.                                                                          |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void AnimationDoor(bool open)``    | Routes an animation door request into the current passenger access sequence.                                                                         | ``open`` — Requested open state.                                                                                                                                                  |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Cancel()``                    | Unwinds this access attempt's motion/reservation and performs its state-specific occupancy cleanup. Already committed occupancy need not be undone.  | No arguments; no returned value.                                                                                                                                                  |
+-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-passengeraccess--events-and-inspector-callbacks:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| Declaration                                                        | Trigger, payload and meaning                                                                                                         |
+====================================================================+======================================================================================================================================+
| ``public event Action<PassengerAccess, AccessState> StateChanged`` | When access sequencing changes. Payload: ``PassengerAccess`` and ``AccessState``; seat occupancy may commit at a different boundary. |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<PassengerAccess, bool> Finished``            | When an access attempt ends. Payload: ``PassengerAccess`` and success bool; inspect actual occupancy after cancellation/handover.    |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent started``                                      | Inspector callback when access sequencing starts; no payload.                                                                        |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent completed``                                    | Inspector callback when access succeeds; no payload.                                                                                 |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent cancelled``                                    | Inspector callback when access is cancelled; no payload.                                                                             |
+--------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-passengeraccess--state-and-configuration-3:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| Member                                                       | Meaning                                                                              |
+==============================================================+======================================================================================+
| ``public PassengerBody passenger``                           | Authored passenger used by ``PassengerAccess``.                                      |
+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public AccessMotion motion``                               | Authored motion used by ``PassengerAccess``.                                         |
+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public virtual AccessState State { get; protected set; }`` | Read-only/resolved state for ``PassengerAccess``.                                    |
+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public virtual bool IsBusy { get; }``                      | Current is busy predicate; read it instead of maintaining a second application flag. |
+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public virtual SeatAccess Target { get; protected set; }`` | Read-only/resolved target for ``PassengerAccess``.                                   |
+--------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public virtual bool IsEntering { get; protected set; }``   | Whether the current access operation is boarding rather than leaving.                |
+--------------------------------------------------------------+--------------------------------------------------------------------------------------+

.. _evs-api-passengeraccess--seataccess:

SeatAccess
----------

**Runtime/World/Passengers/Access/SeatAccess.cs**

Describes the seat endpoint, outside marker, door and admission settings.

**Inherits / implements:** ``MonoBehaviour``.

.. _evs-api-passengeraccess--methods-4:

Methods
~~~~~~~

+------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                              | Role and behavior                                                                            | Arguments and result                                                                                                                                                                                     |
+========================================================================+==============================================================================================+==========================================================================================================================================================================================================+
| ``public virtual void RequestDoor(bool open)``                         | Requests the configured access door's required state for the current operation.              | ``open`` — Requested open state.                                                                                                                                                                         |
+------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool DoorReady(bool open)``                           | Checks whether the configured door has reached the required access state.                    | ``open`` — Requested open state. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated.                                           |
+------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool CanContinue(PassengerBody passenger)``           | Checks whether an admitted seat-access sequence can still continue.                          | ``passenger`` — Character body receiving motion/attachment. **Returns:** ``true`` when the described condition holds; ``false`` otherwise.                                                               |
+------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool CanUse(PassengerBody passenger, bool entering)`` | Checks whether a seat-access endpoint is currently usable by the supplied passenger.         | ``passenger`` — Character body receiving motion/attachment. ``entering`` — ``true`` for entry motion; ``false`` for exit. **Returns:** ``true`` when the described condition holds; ``false`` otherwise. |
+------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool IsExitClear(PassengerBody passenger)``           | Checks the configured outside endpoint capsule for exit clearance; it does not plan a route. | ``passenger`` — Character body receiving motion/attachment. **Returns:** ``true`` when the described condition holds; ``false`` otherwise.                                                               |
+------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-passengeraccess--state-and-configuration-4:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------+------------------------------------------------------------------------------------------+
| Member                                              | Meaning                                                                                  |
+=====================================================+==========================================================================================+
| ``public PassengerSeat seat``                       | Authored seat used by ``SeatAccess``.                                                    |
+-----------------------------------------------------+------------------------------------------------------------------------------------------+
| ``public BodyPart door``                            | Authored door used by ``SeatAccess``.                                                    |
+-----------------------------------------------------+------------------------------------------------------------------------------------------+
| ``public AccessSide side``                          | Descriptive side label; the assigned profile selects the actual clips and triggers.      |
+-----------------------------------------------------+------------------------------------------------------------------------------------------+
| ``public AccessAnimationProfile animationProfile``  | Authored animation profile used by ``SeatAccess``.                                       |
+-----------------------------------------------------+------------------------------------------------------------------------------------------+
| ``public Transform outside``                        | Authored feet-level endpoint. Runtime never moves this transform.                        |
+-----------------------------------------------------+------------------------------------------------------------------------------------------+
| ``public bool useOutsideRotation``                  | Authored use outside rotation used by ``SeatAccess``. Initial value: ``true``.           |
+-----------------------------------------------------+------------------------------------------------------------------------------------------+
| ``public Transform doorway``                        | Authored doorway used by ``SeatAccess``.                                                 |
+-----------------------------------------------------+------------------------------------------------------------------------------------------+
| ``public Vector3 standingOffset``                   | Optional offset from Outside in this seat's local axes.                                  |
+-----------------------------------------------------+------------------------------------------------------------------------------------------+
| ``public bool projectOutsideToGround``              | Authored project outside to ground used by ``SeatAccess``. Initial value: ``true``.      |
+-----------------------------------------------------+------------------------------------------------------------------------------------------+
| ``public float outsideGroundClearance``             | Authored outside ground clearance used by ``SeatAccess``. Initial value: ``.02f``.       |
+-----------------------------------------------------+------------------------------------------------------------------------------------------+
| ``public float groundProbeHeight``                  | Authored ground probe height used by ``SeatAccess``. Initial value: ``2``.               |
+-----------------------------------------------------+------------------------------------------------------------------------------------------+
| ``public float groundProbeDistance``                | Authored ground probe distance used by ``SeatAccess``. Initial value: ``5``.             |
+-----------------------------------------------------+------------------------------------------------------------------------------------------+
| ``public float maximumGroundRise``                  | Largest permitted upward projection from the authored outside point, in metres.          |
+-----------------------------------------------------+------------------------------------------------------------------------------------------+
| ``public float maximumGroundDrop``                  | Largest permitted downward projection from the authored outside point, in metres.        |
+-----------------------------------------------------+------------------------------------------------------------------------------------------+
| ``public virtual Vector3 OutsidePosition { get; }`` | Resolved outside position after optional support projection.                             |
+-----------------------------------------------------+------------------------------------------------------------------------------------------+
| ``public float interactionDistance``                | Authored interaction distance used by ``SeatAccess``. Initial value: ``2``.              |
+-----------------------------------------------------+------------------------------------------------------------------------------------------+
| ``public float maximumSpeed``                       | Maximum vehicle point speed in m/s during entry/exit.                                    |
+-----------------------------------------------------+------------------------------------------------------------------------------------------+
| ``public float maximumAngularSpeed``                | Maximum vehicle angular speed in radians per second during entry/exit.                   |
+-----------------------------------------------------+------------------------------------------------------------------------------------------+
| ``public float minimumGroundNormal``                | Minimum upward ground normal for outside placement; 0.5 accepts slopes up to 60 degrees. |
+-----------------------------------------------------+------------------------------------------------------------------------------------------+
| ``public float openDoorTolerance``                  | Authored open door tolerance used by ``SeatAccess``. Initial value: ``8``.               |
+-----------------------------------------------------+------------------------------------------------------------------------------------------+
| ``public float closedDoorTolerance``                | Authored closed door tolerance used by ``SeatAccess``. Initial value: ``3``.             |
+-----------------------------------------------------+------------------------------------------------------------------------------------------+
| ``public float duration``                           | Authored duration used by ``SeatAccess``. Initial value: ``1.6f``.                       |
+-----------------------------------------------------+------------------------------------------------------------------------------------------+
| ``public float doorTimeout``                        | Authored door timeout used by ``SeatAccess``. Initial value: ``2``.                      |
+-----------------------------------------------------+------------------------------------------------------------------------------------------+
| ``public float clearanceRadius``                    | Authored clearance radius used by ``SeatAccess``. Initial value: ``.25f``.               |
+-----------------------------------------------------+------------------------------------------------------------------------------------------+
| ``public float clearanceHeight``                    | Authored clearance height used by ``SeatAccess``. Initial value: ``1.7f``.               |
+-----------------------------------------------------+------------------------------------------------------------------------------------------+
| ``public LayerMask clearanceMask``                  | Authored clearance mask used by ``SeatAccess``. Initial value: ``~0``.                   |
+-----------------------------------------------------+------------------------------------------------------------------------------------------+
| ``public virtual bool DoorIsOpen { get; }``         | Read-only/resolved door is open for ``SeatAccess``.                                      |
+-----------------------------------------------------+------------------------------------------------------------------------------------------+
| ``public virtual bool DoorAvailable { get; }``      | Read-only/resolved door available for ``SeatAccess``.                                    |
+-----------------------------------------------------+------------------------------------------------------------------------------------------+
