.. _evs-api-interactions--committed-control-interactions-api:

Committed control interactions API
==================================

Read :doc:`the system explanation </Scripting/Interactions>` for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from ``MonoBehaviour``, ``Object`` or ``ScriptableObject`` are documented by Unity.

.. _evs-api-interactions--types:

Types
-----

-  :ref:`ControlInteraction <evs-api-interactions--controlinteraction>`
-  :ref:`ControlInteractionAnimationEvents <evs-api-interactions--controlinteractionanimationevents>`
-  :ref:`ControlInteractionMode <evs-api-interactions--controlinteractionmode>`
-  :ref:`ControlInteractionRequest <evs-api-interactions--controlinteractionrequest>`
-  :ref:`IControlInteractionDriver <evs-api-interactions--icontrolinteractiondriver>`

.. _evs-api-interactions--controlinteraction:

ControlInteraction
------------------

**Runtime/Interior/Controls/ControlInteraction.cs**

``Started``, ``Commit``, ``Completed`` and ``Cancelled``

**Inherits / implements:** ``MonoBehaviour``.

.. _evs-api-interactions--methods:

Methods
~~~~~~~

+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                | Role and behavior                                                                                                                                | Arguments and result                                                                                                                                                                                                                             |
+==========================================================+==================================================================================================================================================+==================================================================================================================================================================================================================================================+
| ``public virtual bool TryBegin(Action onCommit = null)`` | Requests a control interaction; ``true`` means admitted, not necessarily committed or completed.                                                 | ``onCommit`` — Optional gameplay callback invoked at most once before the interaction's ``onCommit`` ``UnityEvent``. Default: ``null``. **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values. |
+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Begin()``                          | ``UnityEvent``-friendly wrapper around ``TryBegin``; it discards the bool result. Use ``TryBegin`` when the caller must handle refusal.          | No arguments; no returned value.                                                                                                                                                                                                                 |
+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void CommitAnimation()``                | Commits the current interaction from an Animation Event entry point.                                                                             | No arguments; no returned value.                                                                                                                                                                                                                 |
+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void CompleteAnimation()``              | Completes the current interaction from an Animation Event entry point.                                                                           | No arguments; no returned value.                                                                                                                                                                                                                 |
+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool Commit()``                         | Commits gameplay at most once for the addressed interaction request.                                                                             | **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values.                                                                                                                                         |
+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool Complete()``                       | Completes an active request, committing first if necessary; after commit rechecks request identity before cleanup/completion notification.       | **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values.                                                                                                                                         |
+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Cancel()``                         | Cancels the active interaction, stops owned driver/transfer/animation state and invokes ``onCancelled``. Already committed gameplay is retained. | No arguments; no returned value.                                                                                                                                                                                                                 |
+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Tick(float deltaTime)``            | Advances the declaring presentation/state machine by elapsed seconds; avoid a second call when its built-in owner already ticks it.              | ``deltaTime`` — Elapsed time in seconds supplied by the owning loop.                                                                                                                                                                             |
+----------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-interactions--events-and-inspector-callbacks:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| Declaration                       | Trigger, payload and meaning                                                                                                            |
+===================================+=========================================================================================================================================+
| ``public UnityEvent onStarted``   | After an interaction is admitted and its request is established. No payload; a handler can cancel immediately.                          |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent onCommit``    | After the request's gameplay callback commits, at most once. No payload; do not duplicate the same mechanical action in both callbacks. |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent onCompleted`` | After the interaction completes. No payload; completion commits first if still needed.                                                  |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent onCancelled`` | After an active interaction is cancelled. No payload; committed gameplay is not rolled back.                                            |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-interactions--state-and-configuration:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| Member                                                                             | Meaning                                                                                                     |
+====================================================================================+=============================================================================================================+
| ``public ControlInteractionMode mode``                                             | Authored mode used by ``ControlInteraction``. Initial value: ``ControlInteractionMode.IK``.                 |
+------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| ``public PassengerSeat seat``                                                      | Authored seat used by ``ControlInteraction``.                                                               |
+------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| ``public PassengerBodyPart hand``                                                  | Authored hand used by ``ControlInteraction``. Initial value: ``PassengerBodyPart.LeftHand``.                |
+------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| ``public VehicleHandle target``                                                    | Authored target used by ``ControlInteraction``.                                                             |
+------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| ``public HandTransferHandle transfer``                                             | Authored transfer used by ``ControlInteraction``.                                                           |
+------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| ``public Animator animator``                                                       | Optional override. Otherwise use the current occupant's ``SeatedAnimator``.                                 |
+------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| ``public string trigger``                                                          | Authored trigger used by ``ControlInteraction``. Initial value: ``"Interact"``.                             |
+------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| ``public bool animationEvents``                                                    | Use Animation Events to call ``Commit`` and ``Complete`` instead of elapsed time.                           |
+------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| ``public float commitTime``                                                        | Authored commit time used by ``ControlInteraction``. Initial value: ``.25f``.                               |
+------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| ``public float duration``                                                          | Authored duration used by ``ControlInteraction``. Initial value: ``.7f``.                                   |
+------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| ``public float timeout``                                                           | Cancels an unfinished Animator or Custom action, including missing animation events. Zero disables timeout. |
+------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| ``public MonoBehaviour customDriver``                                              | A ``MonoBehaviour`` implementing ``IControlInteractionDriver``.                                             |
+------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| ``public virtual bool IsBusy { get; }``                                            | True while an ``ActiveRequest`` exists, including presentation after gameplay commit.                       |
+------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+
| ``public virtual ControlInteractionRequest ActiveRequest { get; protected set; }`` | Exact active interaction request, or ``null`` when idle; retain this identity for delayed callbacks.        |
+------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+

.. _evs-api-interactions--controlinteractionanimationevents:

ControlInteractionAnimationEvents
---------------------------------

**Runtime/Interior/Controls/ControlInteractionAnimationEvents.cs**

Relays Animator events to the active interaction.

**Inherits / implements:** ``MonoBehaviour``.

.. _evs-api-interactions--methods-1:

Methods
~~~~~~~

+---------------------------------------------+------------------------------------------------------------------------------+----------------------------------+
| Signature                                   | Role and behavior                                                            | Arguments and result             |
+=============================================+==============================================================================+==================================+
| ``public virtual void CommitAnimation()``   | Commits the current interaction from an Animation Event entry point.         | No arguments; no returned value. |
+---------------------------------------------+------------------------------------------------------------------------------+----------------------------------+
| ``public virtual void CompleteAnimation()`` | Completes the current interaction from an Animation Event entry point.       | No arguments; no returned value. |
+---------------------------------------------+------------------------------------------------------------------------------+----------------------------------+
| ``public virtual void CancelInteraction()`` | Relays an Animator cancellation event to the configured control interaction. | No arguments; no returned value. |
+---------------------------------------------+------------------------------------------------------------------------------+----------------------------------+

.. _evs-api-interactions--state-and-configuration-1:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------+---------------------------------------------------------------------+
| Member                                    | Meaning                                                             |
+===========================================+=====================================================================+
| ``public ControlInteraction interaction`` | Authored interaction used by ``ControlInteractionAnimationEvents``. |
+-------------------------------------------+---------------------------------------------------------------------+

.. _evs-api-interactions--controlinteractionmode:

ControlInteractionMode
----------------------

**Runtime/Interior/Controls/ControlInteraction.cs**

Defines the allowed control interaction mode choices used by this topic.

.. _evs-api-interactions--values:

Values
~~~~~~

-  ``Immediate``
-  ``IK``
-  ``Animator``
-  ``Custom``

.. _evs-api-interactions--controlinteractionrequest:

ControlInteractionRequest
-------------------------

**Runtime/Interior/Controls/ControlInteraction.cs**

Identity of one admitted control interaction; captured callbacks remain tied to this request.

.. _evs-api-interactions--methods-2:

Methods
~~~~~~~

+----------------------------+----------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| Signature                  | Role and behavior                                                                                                          | Arguments and result                                                                                     |
+============================+============================================================================================================================+==========================================================================================================+
| ``public bool Commit()``   | Commits only while this request is still the owner's ``ActiveRequest``. A stale request cannot commit a newer interaction. | **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values. |
+----------------------------+----------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| ``public bool Complete()`` | Completes only this still-active request; stale callbacks return ``false``.                                                | **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values. |
+----------------------------+----------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+
| ``public void Cancel()``   | Cancels only if this exact request remains active; it cannot cancel a newer request.                                       | No arguments; no returned value.                                                                         |
+----------------------------+----------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------+

.. _evs-api-interactions--state-and-configuration-2:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------+------------------------------------------------------------------------------+
| Member                                                   | Meaning                                                                      |
+==========================================================+==============================================================================+
| ``public bool IsActive { get; }``                        | Whether this request still equals its interaction owner's ``ActiveRequest``. |
+----------------------------------------------------------+------------------------------------------------------------------------------+
| ``public PassengerSeat Seat { get; internal set; }``     | Read-only/resolved seat for ``ControlInteractionRequest``.                   |
+----------------------------------------------------------+------------------------------------------------------------------------------+
| ``public PassengerBody Occupant { get; internal set; }`` | Body currently admitted to this seat, or ``null`` when empty.                |
+----------------------------------------------------------+------------------------------------------------------------------------------+
| ``public VehicleHandle Target { get; internal set; }``   | Read-only/resolved target for ``ControlInteractionRequest``.                 |
+----------------------------------------------------------+------------------------------------------------------------------------------+
| ``public PassengerBodyPart Hand { get; internal set; }`` | Read-only/resolved hand for ``ControlInteractionRequest``.                   |
+----------------------------------------------------------+------------------------------------------------------------------------------+

.. _evs-api-interactions--icontrolinteractiondriver:

IControlInteractionDriver
-------------------------

**Runtime/Interior/Controls/ControlInteraction.cs**

Configuration/implementation type for icontrol interaction driver within committed control interactions.

.. _evs-api-interactions--methods-3:

Methods
~~~~~~~

+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| Signature                                          | Role and behavior                                                                                                                         | Arguments and result                                                           |
+====================================================+===========================================================================================================================================+================================================================================+
| ``void Begin(ControlInteractionRequest request)``  | Accepts ownership of one exact interaction request. Start application presentation and retain that request for delayed commit/completion. | ``request`` — Exact interaction attempt; retain it for asynchronous callbacks. |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| ``void Cancel(ControlInteractionRequest request)`` | Stops presentation owned by the supplied request and releases only that request's resources.                                              | ``request`` — Exact interaction attempt; retain it for asynchronous callbacks. |
+----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
