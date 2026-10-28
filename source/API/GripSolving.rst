.. _evs-api-gripsolving--grip-fitting-and-steering-ownership-api:

Grip fitting and steering ownership API
=======================================

Read :doc:`the system explanation </Scripting/GripSolving>` for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from ``MonoBehaviour``, ``Object`` or ``ScriptableObject`` are documented by Unity.

.. _evs-api-gripsolving--types:

Types
-----

-  :ref:`AdaptiveHandGrip <evs-api-gripsolving--adaptivehandgrip>`
-  :ref:`AdaptiveHandGrip.Finger <evs-api-gripsolving--adaptivehandgripfinger>`
-  :ref:`HandGrip <evs-api-gripsolving--handgrip>`
-  :ref:`HandGrip.FingerPose <evs-api-gripsolving--handgripfingerpose>`
-  :ref:`IPassengerHandPose <evs-api-gripsolving--ipassengerhandpose>`
-  :ref:`SteeringHandPhase <evs-api-gripsolving--steeringhandphase>`
-  :ref:`SteeringHandRegrip <evs-api-gripsolving--steeringhandregrip>`
-  :ref:`SteeringHandRegripSettings <evs-api-gripsolving--steeringhandregripsettings>`

.. _evs-api-gripsolving--adaptivehandgrip:

AdaptiveHandGrip
----------------

**Runtime/World/Passengers/IK/AdaptiveHandGrip.cs**

Binds a character to a surface and applies fitted finger poses.

**Inherits / implements:** ``MonoBehaviour``, :ref:`IPassengerHandPose <evs-api-gripsolving--ipassengerhandpose>`.

.. _evs-api-gripsolving--methods:

Methods
~~~~~~~

+-----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                         | Role and behavior                                                                                                             | Arguments and result                                                                                                                                                                                                           |
+===================================================================================+===============================================================================================================================+================================================================================================================================================================================================================================+
| ``public virtual void Bind(VehicleHandle surface, Animator animator, bool left)`` | Binds this character hand to a ``VehicleHandle`` surface, calibrates the selected side and prepares adaptive surface fitting. | ``surface`` — Surface, interpreted by this operation in the declared type. ``animator`` — Character Animator providing mapped bones/animation context. ``left`` — ``true`` selects the left hand; ``false`` selects the right. |
+-----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Unbind()``                                                  | Releases the current source/hand association and its owned state.                                                             | No arguments; no returned value.                                                                                                                                                                                               |
+-----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool ApplyGrip()``                                               | Applies the currently prepared adaptive grip to the mapped hand.                                                              | **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated.                                                                                                  |
+-----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool Calibrate(Animator animator)``                              | Builds hand measurements/reference frames from the supplied character Animator.                                               | ``animator`` — Character Animator providing mapped bones/animation context. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated.                      |
+-----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryApplyPose(bool gripping)``                               | Applies the prepared gripping/released hand pose when this hand-pose provider can supply it.                                  | ``gripping`` — ``true`` requests a gripping pose; ``false`` requests released/relaxed presentation. **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values.                   |
+-----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Release()``                                                 | Releases this part or hand pose through its declaring type's ownership boundary.                                              | No arguments; no returned value.                                                                                                                                                                                               |
+-----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetPalmPressure(float pressure)``                           | Sets normalized palm pressure and updates a bound adaptive hand when applicable.                                              | ``pressure`` — Normalized palm pressure.                                                                                                                                                                                       |
+-----------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-gripsolving--state-and-configuration:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| Member                                                              | Meaning                                                                                                                          |
+=====================================================================+==================================================================================================================================+
| ``public SteeringWheelHandle wheel``                                | Authored wheel used by ``AdaptiveHandGrip``.                                                                                     |
+---------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``public bool leftHand``                                            | Authored left hand used by ``AdaptiveHandGrip``.                                                                                 |
+---------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``public Finger[] digits``                                          | Generated from Mecanim mapping or assigned explicitly for a custom skeleton.                                                     |
+---------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``public float palmThickness``                                      | Authored palm thickness used by ``AdaptiveHandGrip``. Initial value: ``.009f``.                                                  |
+---------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``public float palmPressureHeelOffset``                             | Palm-pressure contact offset from the knuckles towards the wrist, in metres. Smaller values let the hand sit lower over the rim. |
+---------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``public int iterations``                                           | Authored iterations used by ``AdaptiveHandGrip``. Initial value: ``6``.                                                          |
+---------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``public float closure``                                            | Authored closure used by ``AdaptiveHandGrip``. Initial value: ``1``.                                                             |
+---------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``public float poseRefitDistance``                                  | Ignore small physical wrist compliance instead of repeatedly re-optimizing finger curls.                                         |
+---------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``public float poseRefitAngle``                                     | Authored pose refit angle used by ``AdaptiveHandGrip``. Initial value: ``2``.                                                    |
+---------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``public int refitFingersPerFrame``                                 | Authored refit fingers per frame used by ``AdaptiveHandGrip``. Initial value: ``2``.                                             |
+---------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``public float thumbBaseCone``                                      | Authored thumb base cone used by ``AdaptiveHandGrip``. Initial value: ``50``.                                                    |
+---------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``public float thumbOppositionLimit``                               | Small base opposition keeps steering thumbs pointing forwards rather than folding across the palm.                               |
+---------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``public float thumbSpreadLimit``                                   | Authored thumb spread limit used by ``AdaptiveHandGrip``. Initial value: ``5``.                                                  |
+---------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumFingerSpeed``                                 | Authored maximum finger speed used by ``AdaptiveHandGrip``. Initial value: ``300``.                                              |
+---------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector2 relaxedCurlRange``                                 | Random relaxed finger bend as a fraction of anatomical flexion limits, sampled once per open-hand gesture.                       |
+---------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float RenderedClosure { get; }``                   | Read-only/resolved rendered closure for ``AdaptiveHandGrip``.                                                                    |
+---------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool IsCalibrated { get; }``                       | Current is calibrated predicate; read it instead of maintaining a second application flag.                                       |
+---------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float MaximumPenetration { get; protected set; }`` | Largest measured finger intrusion into the grip surface, in metres.                                                              |
+---------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float MeanContactGap { get; protected set; }``     | Mean positive distance between fitted fingers and the grip, in metres.                                                           |
+---------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-gripsolving--adaptivehandgripfinger:

AdaptiveHandGrip.Finger
-----------------------

**Runtime/World/Passengers/IK/AdaptiveHandGrip.cs**

:doc:`Grip solving </API/GripSolving>`

.. _evs-api-gripsolving--state-and-configuration-1:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------+-----------------------------------------------------------------------------------------------------+
| Member                                | Meaning                                                                                             |
+=======================================+=====================================================================================================+
| ``public string name``                | Authored name used by Finger.                                                                       |
+---------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``public bool thumb``                 | Uses thumb-specific opposition/spread fitting instead of ordinary finger bending.                   |
+---------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``public Vector3 oppositionAxis``     | Authored opposition axis used by Finger.                                                            |
+---------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``public Vector3 spreadAxis``         | Authored spread axis used by Finger.                                                                |
+---------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``public float opposition``           | Authored opposition used by Finger.                                                                 |
+---------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``public float spread``               | Authored spread used by Finger.                                                                     |
+---------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``public Transform[] bones``          | Authored bones used by Finger. Initial value: ``new Transform[3]``.                                 |
+---------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``public Quaternion[] openRotations`` | Authored open rotations used by Finger. Initial value: ``new Quaternion[3]``.                       |
+---------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``public Vector3[] flexionAxes``      | Authored flexion axes used by Finger. Initial value: ``new Vector3[3]``.                            |
+---------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``public Vector3 tipOffset``          | Authored tip offset used by Finger.                                                                 |
+---------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``public float padRadius``            | Authored pad radius used by Finger. Initial value: ``.006f``.                                       |
+---------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``public Vector3 maximumFlexion``     | Authored maximum flexion used by Finger. Initial value: ``new Vector3(85, 110, 80)``.               |
+---------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``public Vector3 angles``             | Authored angles used by Finger.                                                                     |
+---------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``public Vector3 referenceAngles``    | Runtime reference angles data retained by Finger; it is not serialized authoring configuration.     |
+---------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``public float referenceOpposition``  | Runtime reference opposition data retained by Finger; it is not serialized authoring configuration. |
+---------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``public float referenceSpread``      | Runtime reference spread data retained by Finger; it is not serialized authoring configuration.     |
+---------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``public Quaternion[] rendered``      | Runtime rendered data retained by Finger; it is not serialized authoring configuration.             |
+---------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``public bool renderedReady``         | Runtime rendered ready data retained by Finger; it is not serialized authoring configuration.       |
+---------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``public Quaternion[] fixedGrip``     | Runtime fixed grip data retained by Finger; it is not serialized authoring configuration.           |
+---------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``public float relaxedCurl``          | Runtime relaxed curl data retained by Finger; it is not serialized authoring configuration.         |
+---------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``public float minimumWrapDepth``     | Runtime minimum wrap depth data retained by Finger; it is not serialized authoring configuration.   |
+---------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``public float arcRatio``             | Runtime arc ratio data retained by Finger; it is not serialized authoring configuration.            |
+---------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``public Vector3 boundAngles``        | Runtime bound angles data retained by Finger; it is not serialized authoring configuration.         |
+---------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``public float boundOpposition``      | Runtime bound opposition data retained by Finger; it is not serialized authoring configuration.     |
+---------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``public float boundSpread``          | Runtime bound spread data retained by Finger; it is not serialized authoring configuration.         |
+---------------------------------------+-----------------------------------------------------------------------------------------------------+

.. _evs-api-gripsolving--handgrip:

HandGrip
--------

**Runtime/World/Passengers/IK/HandGrip.cs**

Stores character hand frames and fallback finger poses.

**Inherits / implements:** ``MonoBehaviour``.

.. _evs-api-gripsolving--methods-1:

Methods
~~~~~~~

+---------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                                                                               | Role and behavior                                                                 | Arguments and result                                                                                                                                                                                                                                                                                                                                                                                                                    |
+=========================================================================================================================================================+===================================================================================+=========================================================================================================================================================================================================================================================================================================================================================================================================================================+
| ``public virtual void ApplyPose(bool gripping)``                                                                                                        | Applies the configured character hand pose without creating a new seat occupancy. | ``gripping`` — ``true`` requests a gripping pose; ``false`` requests released/relaxed presentation.                                                                                                                                                                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ConfigureJoint(ConfigurableJoint joint, Rigidbody vehicle, VehicleHandle handle)``                                                | Configures a physical hand joint using the prepared grip frame and drive policy.  | ``joint`` — Joint, interpreted by this operation in the declared type. ``vehicle`` — Vehicle context/owner receiving the operation. ``handle`` — Handle, interpreted by this operation in the declared type.                                                                                                                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual Quaternion WristRotation(Transform target)``                                                                                           | Returns wrist orientation from the prepared hand/contact frame.                   | ``target`` — Configured target object/point; see declared type and owner. **Returns:** Returned Quaternion; ownership remains as specified by the creating/lookup operation.                                                                                                                                                                                                                                                            |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual Vector3 WristPosition(Transform target)``                                                                                              | Returns the wrist position corresponding to a prepared palm/contact frame.        | ``target`` — Configured target object/point; see declared type and owner. **Returns:** Returned Vector3; ownership remains as specified by the creating/lookup operation.                                                                                                                                                                                                                                                               |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void DriveRotation(ConfigurableJoint joint, Rigidbody vehicle, Transform target, VehicleHandle handle, bool left, float contact = 1)`` | Applies the physical wrist rotational drive in the prepared hand/contact frame.   | ``joint`` — Joint, interpreted by this operation in the declared type. ``vehicle`` — Vehicle context/owner receiving the operation. ``target`` — Configured target object/point; see declared type and owner. ``handle`` — Handle, interpreted by this operation in the declared type. ``left`` — ``true`` selects the left hand; ``false`` selects the right. ``contact`` — Normalized physical contact participation. Default: ``1``. |
+---------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-gripsolving--state-and-configuration-2:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------+--------------------------------------------------------------------------------------+
| Member                            | Meaning                                                                              |
+===================================+======================================================================================+
| ``public Transform contactPoint`` | Authored contact point used by ``HandGrip``.                                         |
+-----------------------------------+--------------------------------------------------------------------------------------+
| ``public FingerPose[] fingers``   | Authored fingers used by ``HandGrip``. Initial value: ``Array.Empty<FingerPose>()``. |
+-----------------------------------+--------------------------------------------------------------------------------------+
| ``public float angularSpring``    | Authored angular spring used by ``HandGrip``. Initial value: ``1200``.               |
+-----------------------------------+--------------------------------------------------------------------------------------+
| ``public float angularDamper``    | Authored angular damper used by ``HandGrip``. Initial value: ``35``.                 |
+-----------------------------------+--------------------------------------------------------------------------------------+
| ``public float maximumTorque``    | Authored maximum torque used by ``HandGrip``. Initial value: ``250``.                |
+-----------------------------------+--------------------------------------------------------------------------------------+

.. _evs-api-gripsolving--handgripfingerpose:

HandGrip.FingerPose
-------------------

**Runtime/World/Passengers/IK/HandGrip.cs**

Value data for finger pose; its fields are listed below.

.. _evs-api-gripsolving--state-and-configuration-3:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------+---------------------------------------------------+
| Member                                | Meaning                                           |
+=======================================+===================================================+
| ``public Transform bone``             | Authored bone used by ``FingerPose``.             |
+---------------------------------------+---------------------------------------------------+
| ``public Quaternion relaxedRotation`` | Authored relaxed rotation used by ``FingerPose``. |
+---------------------------------------+---------------------------------------------------+
| ``public Quaternion gripRotation``    | Authored grip rotation used by ``FingerPose``.    |
+---------------------------------------+---------------------------------------------------+

.. _evs-api-gripsolving--ipassengerhandpose:

IPassengerHandPose
------------------

**Runtime/World/Passengers/IK/IPassengerHandPose.cs**

Configuration/implementation type for ipassenger hand pose within grip fitting and steering ownership.

.. _evs-api-gripsolving--methods-2:

Methods
~~~~~~~

+--------------------------------------+----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                            | Role and behavior                                                                            | Arguments and result                                                                                                                                                                                         |
+======================================+==============================================================================================+==============================================================================================================================================================================================================+
| ``bool TryApplyPose(bool gripping)`` | Applies the prepared gripping/released hand pose when this hand-pose provider can supply it. | ``gripping`` — ``true`` requests a gripping pose; ``false`` requests released/relaxed presentation. **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values. |
+--------------------------------------+----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``void Release()``                   | Releases this part or hand pose through its declaring type's ownership boundary.             | No arguments; no returned value.                                                                                                                                                                             |
+--------------------------------------+----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``void Unbind()``                    | Releases the current source/hand association and its owned state.                            | No arguments; no returned value.                                                                                                                                                                             |
+--------------------------------------+----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-gripsolving--steeringhandphase:

SteeringHandPhase
-----------------

**Runtime/World/Passengers/IK/SteeringHandRegrip.cs**

Defines the allowed steering hand phase choices used by this topic.

.. _evs-api-gripsolving--values:

Values
~~~~~~

-  ``Held``
-  ``Opening``
-  ``Transferring``
-  ``Closing``
-  ``Parked``
-  ``Approaching``
-  ``Released``
-  ``External``

.. _evs-api-gripsolving--steeringhandregrip:

SteeringHandRegrip
------------------

**Runtime/World/Passengers/IK/SteeringHandRegrip.cs**

Coordinates steering contacts, availability and external reservations.

**Inherits / implements:** :ref:`PassengerBehaviour <evs-api-passengercontrollers--passengerbehaviour>`.

.. _evs-api-gripsolving--methods-3:

Methods
~~~~~~~

+----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                    | Role and behavior                                                                         | Arguments and result                                                                                                                                                                                                                                                                                                                                                       |
+==============================================================================================+===========================================================================================+============================================================================================================================================================================================================================================================================================================================================================================+
| ``public override void PreparePassenger(Passengers core, PassengerSeat passengerSeat)``      | Prepares this passenger behavior for an occupied seat.                                    | ``core`` — Owning audio or passenger core supplying shared context. ``passengerSeat`` — Seat whose occupied hand is temporarily controlled.                                                                                                                                                                                                                                |
+----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void PreparePose()``                                                        | Prepares steering hand pose state for the current passenger/control binding.              | No arguments; no returned value.                                                                                                                                                                                                                                                                                                                                           |
+----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void RenderPassenger(Passengers core)``                                    | Advances render-time passenger presentation owned by this behavior/core.                  | ``core`` — Owning audio or passenger core supplying shared context.                                                                                                                                                                                                                                                                                                        |
+----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void ResetPassenger(Passengers core)``                                     | Resets this passenger behavior's state for the supplied seat.                             | ``core`` — Owning audio or passenger core supplying shared context.                                                                                                                                                                                                                                                                                                        |
+----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool IsHandAvailable(bool left)``                                           | Checks whether the selected steering hand is available under current reservation rules.   | ``left`` — ``true`` selects the left hand; ``false`` selects the right. **Returns:** ``true`` when the described condition holds; ``false`` otherwise.                                                                                                                                                                                                                     |
+----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool IsHandOnWheel(bool left)``                                             | Reports whether the selected hand is currently attached to the steering control.          | ``left`` — ``true`` selects the left hand; ``false`` selects the right. **Returns:** ``true`` when the described condition holds; ``false`` otherwise.                                                                                                                                                                                                                     |
+----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual Object HandOwner(bool left)``                                               | Returns the external Unity object that currently reserves the selected steering hand.     | ``left`` — ``true`` selects the left hand; ``false`` selects the right. **Returns:** Returned Object; ownership remains as specified by the creating/lookup operation.                                                                                                                                                                                                     |
+----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual Transform ColumnSupport(bool left)``                                        | Returns the steering hand's current column-support contribution.                          | ``left`` — ``true`` selects the left hand; ``false`` selects the right. **Returns:** Returned ``Transform``; ownership remains as specified by the creating/lookup operation.                                                                                                                                                                                              |
+----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float MaterialAngle(bool left)``                                            | Returns the selected hand's coordinate on the steering-wheel material.                    | ``left`` — ``true`` selects the left hand; ``false`` selects the right. **Returns:** Computed float in the operation's documented unit/domain.                                                                                                                                                                                                                             |
+----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool IsFirmlySupported(bool left)``                                         | Reports whether the selected steering hand has firm support in the current contact state. | ``left`` — ``true`` selects the left hand; ``false`` selects the right. **Returns:** ``true`` when the described condition holds; ``false`` otherwise.                                                                                                                                                                                                                     |
+----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryReserveHand(bool left, Object owner, Transform palmTarget = null)`` | Reserves a steering hand for a live owner and optional external palm frame.               | ``left`` — ``true`` selects the left hand; ``false`` selects the right. ``owner`` — Unity/application owner whose identity controls this relationship or resource. ``palmTarget`` — Optional stable external palm frame for the reserved hand. Default: ``null``. **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values. |
+----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool ReleaseHand(bool left, Object owner)``                                 | Releases a steering-hand reservation only for the matching owner.                         | ``left`` — ``true`` selects the left hand; ``false`` selects the right. ``owner`` — Unity/application owner whose identity controls this relationship or resource. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated.                                                                           |
+----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool ReleaseSteeringHand(bool left)``                                       | Temporarily releases steering attachment for the selected hand under the regrip policy.   | ``left`` — ``true`` selects the left hand; ``false`` selects the right. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated.                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TakeSteeringHand(bool left)``                                          | Requests steering-hand attachment under the regrip/ownership policy.                      | ``left`` — ``true`` selects the left hand; ``false`` selects the right. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated.                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TrySetLeadingHand(bool left)``                                         | Requests which hand leads steering regrip while respecting the current control state.     | ``left`` — ``true`` selects the left hand; ``false`` selects the right. **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values.                                                                                                                                                                                           |
+----------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-gripsolving--state-and-configuration-4:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------+---------------------------------------------------------------------+
| Member                                                            | Meaning                                                             |
+===================================================================+=====================================================================+
| ``public SteeringWheelHandle surface``                            | Authored surface used by ``SteeringHandRegrip``.                    |
+-------------------------------------------------------------------+---------------------------------------------------------------------+
| ``public SteeringWheelAnimator wheelAnimator``                    | Authored wheel animator used by ``SteeringHandRegrip``.             |
+-------------------------------------------------------------------+---------------------------------------------------------------------+
| ``public virtual bool StopPoseLatched { get; }``                  | Read-only/resolved stop pose latched for ``SteeringHandRegrip``.    |
+-------------------------------------------------------------------+---------------------------------------------------------------------+
| ``public virtual int LeadingHand { get; }``                       | -1: no leader, 0: left, 1: right.                                   |
+-------------------------------------------------------------------+---------------------------------------------------------------------+
| ``public virtual bool LeftHandAvailable { get; }``                | Read-only/resolved left hand available for ``SteeringHandRegrip``.  |
+-------------------------------------------------------------------+---------------------------------------------------------------------+
| ``public virtual bool RightHandAvailable { get; }``               | Read-only/resolved right hand available for ``SteeringHandRegrip``. |
+-------------------------------------------------------------------+---------------------------------------------------------------------+
| ``public virtual SteeringHandPhase LeftPhase { get; }``           | Read-only/resolved left phase for ``SteeringHandRegrip``.           |
+-------------------------------------------------------------------+---------------------------------------------------------------------+
| ``public virtual SteeringHandPhase RightPhase { get; }``          | Read-only/resolved right phase for ``SteeringHandRegrip``.          |
+-------------------------------------------------------------------+---------------------------------------------------------------------+
| ``public virtual int PoseGeneration { get; protected set; }``     | Read-only/resolved pose generation for ``SteeringHandRegrip``.      |
+-------------------------------------------------------------------+---------------------------------------------------------------------+
| ``public virtual int CompletedTransfers { get; protected set; }`` | Read-only/resolved completed transfers for ``SteeringHandRegrip``.  |
+-------------------------------------------------------------------+---------------------------------------------------------------------+

.. _evs-api-gripsolving--steeringhandregripsettings:

SteeringHandRegripSettings
--------------------------

**Runtime/World/Passengers/IK/SteeringHandRegripSettings.cs**

Configuration/implementation type for steering hand regrip settings within grip fitting and steering ownership.

.. _evs-api-gripsolving--state-and-configuration-5:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------+----------------------------------------------------------------------------------------------------------------+
| Member                                 | Meaning                                                                                                        |
+========================================+================================================================================================================+
| ``public float palmReturnTime``        | Minimum time for a full palm-pressure-to-wrapped-grip blend while the released wheel unwinds.                  |
+----------------------------------------+----------------------------------------------------------------------------------------------------------------+
| ``public float reachAdjustment``       | Search around each preferred angle for a reachable wrist pose.                                                 |
+----------------------------------------+----------------------------------------------------------------------------------------------------------------+
| ``public float reachMargin``           | Safety margin subtracted from the hand's measured arm reach, in metres.                                        |
+----------------------------------------+----------------------------------------------------------------------------------------------------------------+
| ``public float minimumHandSeparation`` | Authored minimum hand separation used by ``SteeringHandRegripSettings``. Initial value: ``75``.                |
+----------------------------------------+----------------------------------------------------------------------------------------------------------------+
| ``public float leftRestAngle``         | Lower rim angles for the relaxed thumb/index support; measured in the unturned wheel plane.                    |
+----------------------------------------+----------------------------------------------------------------------------------------------------------------+
| ``public float guideAdjustmentSpeed``  | Maximum guide grasp adjustment along the rim, in degrees per second. Wheel-following itself is never filtered. |
+----------------------------------------+----------------------------------------------------------------------------------------------------------------+
| ``public float rightRestAngle``        | Authored right rest angle used by ``SteeringHandRegripSettings``. Initial value: ``290``.                      |
+----------------------------------------+----------------------------------------------------------------------------------------------------------------+
