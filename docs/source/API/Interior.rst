.. _evs-api-interior--cockpit-instruments-and-bindings-api:

Cockpit instruments and bindings API
====================================

Read :doc:`the system explanation </Scripting/Interior>` for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from ``MonoBehaviour``, ``Object`` or ``ScriptableObject`` are documented by Unity.

.. _evs-api-interior--types:

Types
-----

-  :ref:`AircraftControlMotion <evs-api-interior--aircraftcontrolmotion>`
-  :ref:`AircraftControlMotionMode <evs-api-interior--aircraftcontrolmotionmode>`
-  :ref:`AircraftHud <evs-api-interior--aircrafthud>`
-  :ref:`AnchoredRotation <evs-api-interior--anchoredrotation>`
-  :ref:`CarHud <evs-api-interior--carhud>`
-  :ref:`EngineRpmSource <evs-api-interior--enginerpmsource>`
-  :ref:`FuelTank <evs-api-interior--fueltank>`
-  :ref:`GearPaddleHandle <evs-api-interior--gearpaddlehandle>`
-  :ref:`GearShiftBinding <evs-api-interior--gearshiftbinding>`
-  :ref:`GearShiftDirection <evs-api-interior--gearshiftdirection>`
-  :ref:`HandleCommandInput <evs-api-interior--handlecommandinput>`
-  :ref:`IGearShiftHandle <evs-api-interior--igearshifthandle>`
-  :ref:`IInteriorValueSource <evs-api-interior--iinteriorvaluesource>`
-  :ref:`IndicatorSwitchBinding <evs-api-interior--indicatorswitchbinding>`
-  :ref:`InstrumentNeedle <evs-api-interior--instrumentneedle>`
-  :ref:`InteriorCore <evs-api-interior--interiorcore>`
-  :ref:`InteriorModule <evs-api-interior--interiormodule>`
-  :ref:`InteriorValueSource <evs-api-interior--interiorvaluesource>`
-  :ref:`ProfileSwitchBinding <evs-api-interior--profileswitchbinding>`
-  :ref:`RearMirror <evs-api-interior--rearmirror>`
-  :ref:`RearMirrors <evs-api-interior--rearmirrors>`
-  :ref:`RotaryHandle <evs-api-interior--rotaryhandle>`
-  :ref:`SpeedValueSource <evs-api-interior--speedvaluesource>`
-  :ref:`SteeringStickAnimator <evs-api-interior--steeringstickanimator>`
-  :ref:`SteeringWheelAnimator <evs-api-interior--steeringwheelanimator>`
-  :ref:`StickSetup <evs-api-interior--sticksetup>`
-  :ref:`ThrottleAnimator <evs-api-interior--throttleanimator>`
-  :ref:`ThrottleSetup <evs-api-interior--throttlesetup>`
-  :ref:`Wiper <evs-api-interior--wiper>`
-  :ref:`WiperBlade <evs-api-interior--wiperblade>`
-  :ref:`WiperSwitchBinding <evs-api-interior--wiperswitchbinding>`
-  :ref:`WiperType <evs-api-interior--wipertype>`
-  :ref:`Wipers <evs-api-interior--wipers>`
-  :ref:`YokeAnimator <evs-api-interior--yokeanimator>`

.. _evs-api-interior--aircraftcontrolmotion:

AircraftControlMotion
---------------------

**Runtime/Interior/Controls/AircraftControlMotion.cs**

Configuration/implementation type for aircraft control motion within cockpit instruments and bindings.

**Inherits / implements:** ``MonoBehaviour``.

.. _evs-api-interior--methods:

Methods
~~~~~~~

+----------------------------------------------------+------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| Signature                                          | Role and behavior                                                                        | Arguments and result                                                          |
+====================================================+==========================================================================================+===============================================================================+
| ``public virtual void SetValue(float normalized)`` | Applies normalized aircraft-control travel to its authored rotation/translation mapping. | ``normalized`` — Normalized value; the owner maps it to its configured range. |
+----------------------------------------------------+------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

.. _evs-api-interior--state-and-configuration:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------+----------------------------------------------------------------------------------------------+
| Member                                                 | Meaning                                                                                      |
+========================================================+==============================================================================================+
| ``public Transform movingPart``                        | Authored moving part used by ``AircraftControlMotion``.                                      |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``public Transform anchor``                            | Authored anchor used by ``AircraftControlMotion``.                                           |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``public AircraftControlMotionMode mode``              | Authored mode used by ``AircraftControlMotion``.                                             |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``public Vector3 localAxis``                           | Authored local axis used by ``AircraftControlMotion``. Initial value: ``Vector3.right``.     |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``public float minimum``                               | Authored minimum used by ``AircraftControlMotion``. Initial value: ``-20``.                  |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``public float maximum``                               | Authored maximum used by ``AircraftControlMotion``. Initial value: ``20``.                   |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``public virtual float Value { get; protected set; }`` | Current value in this control's domain; use the declaring control's detailed value contract. |
+--------------------------------------------------------+----------------------------------------------------------------------------------------------+

.. _evs-api-interior--aircraftcontrolmotionmode:

AircraftControlMotionMode
-------------------------

**Runtime/Interior/Controls/AircraftControlMotion.cs**

Defines the allowed aircraft control motion mode choices used by this topic.

.. _evs-api-interior--values:

Values
~~~~~~

-  ``Rotation``
-  ``Translation``

.. _evs-api-interior--aircrafthud:

AircraftHud
-----------

**Runtime/Interior/Render/AircraftHud.cs**

Configuration/implementation type for aircraft hud within cockpit instruments and bindings.

**Inherits / implements:** :ref:`InteriorModule <evs-api-interior--interiormodule>`.

.. _evs-api-interior--methods-1:

Methods
~~~~~~~

+-------------------------------------------------------------+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| Signature                                                   | Role and behavior                                                                         | Arguments and result                                                                       |
+=============================================================+===========================================================================================+============================================================================================+
| ``public override void Configure(VehicleController owner)`` | Binds the HUD to this vehicle's telemetry source.                                         | ``owner`` — Unity/application owner whose identity controls this relationship or resource. |
+-------------------------------------------------------------+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+
| ``public virtual void Bind(VehicleController owner)``       | Binds the HUD to a vehicle/telemetry source and releases its previous owned subscription. | ``owner`` — Unity/application owner whose identity controls this relationship or resource. |
+-------------------------------------------------------------+-------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+

.. _evs-api-interior--events-and-inspector-callbacks:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------+-------------------------------------------------------------------------+
| Declaration                                | Trigger, payload and meaning                                            |
+============================================+=========================================================================+
| ``public event Action<Telemetry> Changed`` | After the HUD receives an updated reading. Payload: Telemetry snapshot. |
+--------------------------------------------+-------------------------------------------------------------------------+

.. _evs-api-interior--state-and-configuration-1:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| Member                                                             | Meaning                                                                           |
+====================================================================+===================================================================================+
| ``public VehicleController vehicle``                               | Authored vehicle used by ``AircraftHud``.                                         |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| ``public Renderer cockpitSurface``                                 | Authored cockpit surface used by ``AircraftHud``.                                 |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| ``public Texture customTexture``                                   | Authored custom texture used by ``AircraftHud``.                                  |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| ``public string textureProperty``                                  | Authored texture property used by ``AircraftHud``. Initial value: ``"_BaseMap"``. |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| ``public float refreshRate``                                       | Authored refresh rate used by ``AircraftHud``. Initial value: ``15``.             |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| ``public virtual Telemetry Telemetry { get; protected set; }``     | Latest cached vehicle snapshot published after the module pipeline.               |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| ``public virtual LandingGear LandingGear { get; protected set; }`` | Read-only/resolved landing gear for ``AircraftHud``.                              |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------+
| ``public virtual Texture DisplayTexture { get; }``                 | Read-only/resolved display texture for ``AircraftHud``.                           |
+--------------------------------------------------------------------+-----------------------------------------------------------------------------------+

.. _evs-api-interior--anchoredrotation:

AnchoredRotation
----------------

**Runtime/Interior/Controls/AnchoredRotation.cs**

Preserves a neutral pose relative to an independent pivot frame.

.. _evs-api-interior--methods-2:

Methods
~~~~~~~

+-----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                           | Role and behavior                                                                         | Arguments and result                                                                                                                                                                                                                                                                                                               |
+=====================================================================================================+===========================================================================================+====================================================================================================================================================================================================================================================================================================================================+
| ``public virtual void CaptureRestPose()``                                                           | Captures the currently authored rest pose for this geometry mapper or blade.              | No arguments; no returned value.                                                                                                                                                                                                                                                                                                   |
+-----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TryGetPose(float degrees, out Vector3 position, out Quaternion orientation)`` | Computes a pose from the captured anchored rest frame when geometry references are valid. | ``degrees`` — Requested angle in degrees. ``position`` — Requested point or switch detent; see its declared type and owning operation. ``orientation`` — Orientation, interpreted by this operation in the declared type. **Returns:** ``true`` if admitted/applied; inspect the described completion boundary and any out values. |
+-----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual Vector3 GetPointAtAngle(Vector3 meshLocalPoint, float degrees)``                   | Returns the neutral-frame point after applying a specified rotation angle.                | ``meshLocalPoint`` — Impact point in the deformed mesh's local coordinates. ``degrees`` — Requested angle in degrees. **Returns:** Returned Vector3; ownership remains as specified by the creating/lookup operation.                                                                                                              |
+-----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetAngle(float degrees)``                                                     | Immediately applies a moving-part/geometry rotation in degrees.                           | ``degrees`` — Requested angle in degrees.                                                                                                                                                                                                                                                                                          |
+-----------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-interior--state-and-configuration-2:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------+---------------------------------------------------------------------------------------+
| Member                                   | Meaning                                                                               |
+==========================================+=======================================================================================+
| ``public Transform movingPart``          | Authored moving part used by ``AnchoredRotation``.                                    |
+------------------------------------------+---------------------------------------------------------------------------------------+
| ``public Transform anchor``              | Authored anchor used by ``AnchoredRotation``.                                         |
+------------------------------------------+---------------------------------------------------------------------------------------+
| ``public Vector3 localAxis``             | Authored local axis used by ``AnchoredRotation``. Initial value: ``Vector3.right``.   |
+------------------------------------------+---------------------------------------------------------------------------------------+
| ``public Vector3 Axis { get; }``         | Read-only/resolved axis for ``AnchoredRotation``.                                     |
+------------------------------------------+---------------------------------------------------------------------------------------+
| ``public virtual bool IsValid { get; }`` | Current is valid predicate; read it instead of maintaining a second application flag. |
+------------------------------------------+---------------------------------------------------------------------------------------+

.. _evs-api-interior--carhud:

CarHud
------

**Runtime/Interior/Render/CarHud.cs**

Configuration/implementation type for car hud within cockpit instruments and bindings.

**Inherits / implements:** :ref:`InteriorModule <evs-api-interior--interiormodule>`.

.. _evs-api-interior--methods-3:

Methods
~~~~~~~

+----------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+
| Signature                                                | Role and behavior                                                                         | Arguments and result                                                         |
+==========================================================+===========================================================================================+==============================================================================+
| ``public virtual void Bind(VehicleController selected)`` | Binds the HUD to a vehicle/telemetry source and releases its previous owned subscription. | ``selected`` — Selected, interpreted by this operation in the declared type. |
+----------------------------------------------------------+-------------------------------------------------------------------------------------------+------------------------------------------------------------------------------+

.. _evs-api-interior--events-and-inspector-callbacks-1:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------+-------------------------------------------------------------------------+
| Declaration                                | Trigger, payload and meaning                                            |
+============================================+=========================================================================+
| ``public event Action<Telemetry> Changed`` | After the HUD receives an updated reading. Payload: Telemetry snapshot. |
+--------------------------------------------+-------------------------------------------------------------------------+

.. _evs-api-interior--state-and-configuration-3:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------+------------------------------------------------------------------------------+
| Member                                                         | Meaning                                                                      |
+================================================================+==============================================================================+
| ``public VehicleController vehicle``                           | Authored vehicle used by ``CarHud``.                                         |
+----------------------------------------------------------------+------------------------------------------------------------------------------+
| ``public Renderer cockpitSurface``                             | Authored cockpit surface used by ``CarHud``.                                 |
+----------------------------------------------------------------+------------------------------------------------------------------------------+
| ``public Texture customTexture``                               | Authored custom texture used by ``CarHud``.                                  |
+----------------------------------------------------------------+------------------------------------------------------------------------------+
| ``public string textureProperty``                              | Authored texture property used by ``CarHud``. Initial value: ``"_BaseMap"``. |
+----------------------------------------------------------------+------------------------------------------------------------------------------+
| ``public float refreshRate``                                   | Authored refresh rate used by ``CarHud``. Initial value: ``10``.             |
+----------------------------------------------------------------+------------------------------------------------------------------------------+
| ``public virtual Telemetry Telemetry { get; protected set; }`` | Latest cached vehicle snapshot published after the module pipeline.          |
+----------------------------------------------------------------+------------------------------------------------------------------------------+
| ``public virtual Lights Lights { get; }``                      | Read-only/resolved lights for ``CarHud``.                                    |
+----------------------------------------------------------------+------------------------------------------------------------------------------+
| ``public virtual FuelTank FuelTank { get; }``                  | Read-only/resolved fuel tank for ``CarHud``.                                 |
+----------------------------------------------------------------+------------------------------------------------------------------------------+
| ``public virtual DrivingAssists Assists { get; }``             | Read-only/resolved assists for ``CarHud``.                                   |
+----------------------------------------------------------------+------------------------------------------------------------------------------+
| ``public virtual Texture DisplayTexture { get; }``             | Read-only/resolved display texture for ``CarHud``.                           |
+----------------------------------------------------------------+------------------------------------------------------------------------------+

+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| Member                         | Meaning                                                                                                                                     |
+================================+=============================================================================================================================================+
| ``public SpeedUnit speedUnit`` | Output unit; defaults to Kph. Changing this does not alter vehicle physics. For a signed SpeedValueSource, reverse motion remains negative. |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-interior--enginerpmsource:

EngineRpmSource
---------------

**Runtime/Interior/Controls/EngineRpmSource.cs**

Configuration/implementation type for engine rpm source within cockpit instruments and bindings.

**Inherits / implements:** :ref:`InteriorValueSource <evs-api-interior--interiorvaluesource>`.

.. _evs-api-interior--methods-4:

Methods
~~~~~~~

+---------------------------------------+----------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| Signature                             | Role and behavior                                                                      | Arguments and result                                                   |
+=======================================+========================================================================================+========================================================================+
| ``public override float ReadValue()`` | Reads a numeric instrument source in the source's documented physical/normalized unit. | **Returns:** Computed float in the operation's documented unit/domain. |
+---------------------------------------+----------------------------------------------------------------------------------------+------------------------------------------------------------------------+

.. _evs-api-interior--state-and-configuration-4:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

======================== ============================================
Member                   Meaning
======================== ============================================
``public Engine engine`` Authored engine used by ``EngineRpmSource``.
======================== ============================================

.. _evs-api-interior--fueltank:

FuelTank
--------

**Runtime/Engine/FuelTank.cs**

Quantity change, empty transition and actual fuel increase

**Inherits / implements:** :ref:`EngineModule <evs-api-drivedynamics--enginemodule>`.

.. _evs-api-interior--methods-5:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                  | Role and behavior                                                                                                          | Arguments and result                                                                                                                                                                                                     |
+============================================================================================+============================================================================================================================+==========================================================================================================================================================================================================================+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Stops an empty constrained engine, otherwise consumes running idle/load fuel and publishes actual quantity transitions.    | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float Drain(float litres)``                                               | Removes a finite nonnegative requested number of litres, bounded by available fuel, and returns the actual litres removed. | ``litres`` — Requested fuel transfer in litres; actual transfer can be smaller. **Returns:** Actual transferred litres.                                                                                                  |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Fill()``                                                             | Sets quantity to capacity through ``SetFuel``, with normal actual-change notifications.                                    | No arguments; no returned value.                                                                                                                                                                                         |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float Refuel(float litres)``                                              | Adds up to the requested litres, limited by capacity, and returns actual transfer.                                         | ``litres`` — Requested fuel transfer in litres; actual transfer can be smaller. **Returns:** Actual transferred litres.                                                                                                  |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetFuel(float litres)``                                              | Sets fuel quantity within capacity and publishes actual quantity/empty/refuel transitions.                                 | ``litres`` — Requested fuel transfer in litres; actual transfer can be smaller.                                                                                                                                          |
+--------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-interior--events-and-inspector-callbacks-2:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------+-------------------------------------------------------------------------------------------------+
| Declaration                                | Trigger, payload and meaning                                                                    |
+============================================+=================================================================================================+
| ``public event Action<float> FuelChanged`` | After actual fuel quantity changes. Payload: current litres, not the requested transfer amount. |
+--------------------------------------------+-------------------------------------------------------------------------------------------------+
| ``public event Action Emptied``            | On the transition to empty fuel. No payload.                                                    |
+--------------------------------------------+-------------------------------------------------------------------------------------------------+
| ``public event Action Refuelled``          | After an actual increase in fuel, including ``SetFuel``. No payload; query quantity if needed.  |
+--------------------------------------------+-------------------------------------------------------------------------------------------------+

.. _evs-api-interior--state-and-configuration-5:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| Member                                                         | Meaning                                                                                                                        |
+================================================================+================================================================================================================================+
| ``public bool consumeFuel``                                    | Consume fuel while the engine is running. Disable for an unlimited driving range while retaining the gauge and refuelling API. |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public bool stopEngineWhenEmpty``                            | Stop the engine and block ignition when the tank is empty.                                                                     |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool BlocksIgnition { get; }``                | Whether an active/enabled tank with ``stopEngineWhenEmpty`` currently blocks engine start.                                     |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public float capacityLitres``                                | Authored capacity litres used by ``FuelTank``. Initial value: ``60``.                                                          |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public float idleLitresPerHour``                             | Authored idle litres per hour used by ``FuelTank``. Initial value: ``.8f``.                                                    |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public float fullLoadLitresPerHour``                         | Authored full load litres per hour used by ``FuelTank``. Initial value: ``35``.                                                |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float FuelLitres { get; }``                   | Read-only/resolved fuel litres for ``FuelTank``.                                                                               |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float Fraction { get; }``                     | Fuel quantity divided by capacity, suitable for a 0–1 instrument source.                                                       |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool HasFuel { get; }``                       | Whether the tank currently contains usable fuel.                                                                               |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float LitresPerHour { get; protected set; }`` | Read-only/resolved litres per hour for ``FuelTank``.                                                                           |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }``              | Cross-category execution barrier used by the module pipeline.                                                                  |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public override int ExecutionOrder { get; }``                | Default local priority within phase/category.                                                                                  |
+----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-interior--gearpaddlehandle:

GearPaddleHandle
----------------

**Runtime/Interior/Controls/GearPaddleHandle.cs**

Configuration/implementation type for gear paddle handle within cockpit instruments and bindings.

**Inherits / implements:** ``MonoBehaviour``, :ref:`IGearShiftHandle <evs-api-interior--igearshifthandle>`.

.. _evs-api-interior--methods-6:

Methods
~~~~~~~

+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| Signature                                                            | Role and behavior                                                                                                                   | Arguments and result                                                                                       |
+======================================================================+=====================================================================================================================================+============================================================================================================+
| ``public virtual void ResetMotion()``                                | Clears presentation requests and restores the released/default motion state.                                                        | No arguments; no returned value.                                                                           |
+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public virtual void Tick(float deltaTime)``                        | Advances the declaring presentation/state machine by elapsed seconds; avoid a second call when its built-in owner already ticks it. | ``deltaTime`` — Elapsed time in seconds supplied by the owning loop.                                       |
+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public virtual void AnimateShift(int previousGear, int nextGear)`` | Requests a presentation gesture for an accepted change from the previous gear to the next gear.                                     | ``previousGear`` — Previously selected signed gear index. ``nextGear`` — Newly selected signed gear index. |
+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| ``public virtual void Press()``                                      | Requests a paddle presentation press in the selected shift direction.                                                               | No arguments; no returned value.                                                                           |
+----------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+

.. _evs-api-interior--events-and-inspector-callbacks-3:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------+------------------------------------------------------------------------------------------------------+
| Declaration                     | Trigger, payload and meaning                                                                         |
+=================================+======================================================================================================+
| ``public UnityEvent onPressed`` | Inspector callback for a paddle press; no payload. The configured paddle determines shift direction. |
+---------------------------------+------------------------------------------------------------------------------------------------------+

.. _evs-api-interior--state-and-configuration-6:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------+----------------------------------------------------------------------------------------------+
| Member                                                   | Meaning                                                                                      |
+==========================================================+==============================================================================================+
| ``public AnchoredRotation motion``                       | Authored motion used by ``GearPaddleHandle``. Initial value: ``new AnchoredRotation()``.     |
+----------------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``public GearShiftDirection direction``                  | Authored direction used by ``GearPaddleHandle``.                                             |
+----------------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``public float pressedAngle``                            | Signed inward travel from the neutral pose, in degrees.                                      |
+----------------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``public float pressDuration``                           | Authored press duration used by ``GearPaddleHandle``. Initial value: ``.08f``.               |
+----------------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``public float returnDuration``                          | Authored return duration used by ``GearPaddleHandle``. Initial value: ``.16f``.              |
+----------------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``public virtual float Value { get; protected set; }``   | Current value in this control's domain; use the declaring control's detailed value contract. |
+----------------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``public virtual bool IsMoving { get; protected set; }`` | Whether displayed switch travel differs from its requested detent target.                    |
+----------------------------------------------------------+----------------------------------------------------------------------------------------------+

.. _evs-api-interior--gearshiftbinding:

GearShiftBinding
----------------

**Runtime/Interior/Controls/GearShiftBinding.cs**

Synchronizes shift presentation with accepted mechanical gear changes.

**Inherits / implements:** :ref:`InteriorModule <evs-api-interior--interiormodule>`.

.. _evs-api-interior--methods-7:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                  | Role and behavior                                                                                           | Arguments and result                                                                                                                                                                                                     |
+============================================================================================+=============================================================================================================+==========================================================================================================================================================================================================================+
| ``public virtual void Bind(Engine source)``                                                | Connects a gearbox to an ``IGearShiftHandle`` and refreshes the accepted-shift subscription.                | ``source`` — Explicit provider being selected or bound.                                                                                                                                                                  |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void RefreshBinding()``                                                   | Re-resolves the current gearbox/shift-handle binding and its subscription.                                  | No arguments; no returned value.                                                                                                                                                                                         |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Configure(VehicleController vehicle)``                              | Refreshes the connected gearbox/shift-handle binding and subscriptions.                                     | ``vehicle`` — Vehicle context/owner receiving the operation.                                                                                                                                                             |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Refreshes its gearbox/handle association so changed explicit references use the correct event subscription. | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-interior--state-and-configuration-7:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------+-------------------------------------------------------------------------------------+
| Member                                            | Meaning                                                                             |
+===================================================+=====================================================================================+
| ``public Engine engine``                          | When assigned, follows the engine's active gearbox, including transmission changes. |
+---------------------------------------------------+-------------------------------------------------------------------------------------+
| ``public Gearbox gearbox``                        | Authored gearbox used by ``GearShiftBinding``.                                      |
+---------------------------------------------------+-------------------------------------------------------------------------------------+
| ``public MonoBehaviour[] handles``                | Any components implementing ``IGearShiftHandle``.                                   |
+---------------------------------------------------+-------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }`` | Cross-category execution barrier used by the module pipeline.                       |
+---------------------------------------------------+-------------------------------------------------------------------------------------+

.. _evs-api-interior--gearshiftdirection:

GearShiftDirection
------------------

**Runtime/Interior/Controls/GearPaddleHandle.cs**

Defines the allowed gear shift direction choices used by this topic.

.. _evs-api-interior--values-1:

Values
~~~~~~

-  ``Both``
-  ``Up``
-  ``Down``

.. _evs-api-interior--handlecommandinput:

HandleCommandInput
------------------

**Runtime/Interior/Controls/HandleCommandInput.cs**

Configuration/implementation type for handle command input within cockpit instruments and bindings.

.. _evs-api-interior--methods-8:

Methods
~~~~~~~

+------------------------------------------------------------------+---------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                        | Role and behavior                                                                           | Arguments and result                                                                                                                                                                                                                             |
+==================================================================+=============================================================================================+==================================================================================================================================================================================================================================================+
| ``public static float Read(Command command, HandleInput input)`` | Maps one ``HandleInput`` choice to the corresponding Command axis for cockpit presentation. | ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``input`` — Command handle channel or normalized rate, according to the signature. **Returns:** Computed float in the operation's documented unit/domain. |
+------------------------------------------------------------------+---------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-interior--igearshifthandle:

IGearShiftHandle
----------------

**Runtime/Interior/Controls/IGearShiftHandle.cs**

Configuration/implementation type for igear shift handle within cockpit instruments and bindings.

.. _evs-api-interior--methods-9:

Methods
~~~~~~~

+-------------------------------------------------------+-------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+
| Signature                                             | Role and behavior                                                                               | Arguments and result                                                                                       |
+=======================================================+=================================================================================================+============================================================================================================+
| ``void AnimateShift(int previousGear, int nextGear)`` | Requests a presentation gesture for an accepted change from the previous gear to the next gear. | ``previousGear`` — Previously selected signed gear index. ``nextGear`` — Newly selected signed gear index. |
+-------------------------------------------------------+-------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+

.. _evs-api-interior--iinteriorvaluesource:

IInteriorValueSource
--------------------

**Runtime/Interior/Controls/InteriorValueSource.cs**

Configuration/implementation type for iinterior value source within cockpit instruments and bindings.

.. _evs-api-interior--methods-10:

Methods
~~~~~~~

+-----------------------+----------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| Signature             | Role and behavior                                                                      | Arguments and result                                                   |
+=======================+========================================================================================+========================================================================+
| ``float ReadValue()`` | Reads a numeric instrument source in the source's documented physical/normalized unit. | **Returns:** Computed float in the operation's documented unit/domain. |
+-----------------------+----------------------------------------------------------------------------------------+------------------------------------------------------------------------+

.. _evs-api-interior--indicatorswitchbinding:

IndicatorSwitchBinding
----------------------

**Runtime/Interior/Controls/IndicatorSwitchBinding.cs**

Configuration/implementation type for indicator switch binding within cockpit instruments and bindings.

**Inherits / implements:** ``MonoBehaviour``.

.. _evs-api-interior--methods-11:

Methods
~~~~~~~

+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+
| Signature                                           | Role and behavior                                                                                                                   | Arguments and result                                                 |
+=====================================================+=====================================================================================================================================+======================================================================+
| ``public virtual void Tick(float deltaTime)``       | Advances the declaring presentation/state machine by elapsed seconds; avoid a second call when its built-in owner already ticks it. | ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+
| ``public virtual void Synchronize(bool immediate)`` | Synchronizes presentation/selector state with its source; gearbox synchronization is not a validated driving shift request.         | ``immediate`` — Whether to bypass normal presentation travel.        |
+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+

.. _evs-api-interior--state-and-configuration-8:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------+--------------------------------------------------------------------------------------------------------+
| Member                                 | Meaning                                                                                                |
+========================================+========================================================================================================+
| ``public Lights lights``               | Authored lights used by ``IndicatorSwitchBinding``.                                                    |
+----------------------------------------+--------------------------------------------------------------------------------------------------------+
| ``public SwitchHandle switchHandle``   | Authored switch handle used by ``IndicatorSwitchBinding``.                                             |
+----------------------------------------+--------------------------------------------------------------------------------------------------------+
| ``public SwitchPosition leftPosition`` | Authored left position used by ``IndicatorSwitchBinding``. Initial value: ``SwitchPosition.Negative``. |
+----------------------------------------+--------------------------------------------------------------------------------------------------------+
| ``public bool animateHandle``          | Authored animate handle used by ``IndicatorSwitchBinding``.                                            |
+----------------------------------------+--------------------------------------------------------------------------------------------------------+

.. _evs-api-interior--instrumentneedle:

InstrumentNeedle
----------------

**Runtime/Interior/Controls/InstrumentNeedle.cs**

Specializes value-driven rotation for instruments.

**Inherits / implements:** :ref:`RotaryHandle <evs-api-interior--rotaryhandle>`.

.. _evs-api-interior--interiorcore:

InteriorCore
------------

**Runtime/Interior/Core/InteriorCore.cs**

Configuration/implementation type for interior core within cockpit instruments and bindings.

**Inherits / implements:** :ref:`CategoryCore <evs-api-modules--categorycore>`.

.. _evs-api-interior--methods-12:

Methods
~~~~~~~

+---------------------------+--------------------------------------------------------------+--------------------------------------------------------------------+
| Signature                 | Role and behavior                                            | Arguments and result                                               |
+===========================+==============================================================+====================================================================+
| ``public InteriorCore()`` | Constructs ``InteriorCore`` with the supplied initial state. | **Returns:** New instance initialized from the supplied arguments. |
+---------------------------+--------------------------------------------------------------+--------------------------------------------------------------------+

.. _evs-api-interior--state-and-configuration-9:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------+--------------------------------------------------------------------------------------+
| Member                                               | Meaning                                                                              |
+======================================================+======================================================================================+
| ``public override ModuleCategory Category { get; }`` | Module responsibility category; it does not independently determine execution phase. |
+------------------------------------------------------+--------------------------------------------------------------------------------------+

.. _evs-api-interior--interiormodule:

InteriorModule
--------------

**Runtime/Interior/Core/InteriorModule.cs**

Configuration/implementation type for interior module within cockpit instruments and bindings.

**Inherits / implements:** :ref:`Module <evs-api-modules--module>`, :ref:`IInteriorModule <evs-api-modules--iinteriormodule>`.

.. _evs-api-interior--state-and-configuration-10:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------+--------------------------------------------------------------------------------------+
| Member                                                      | Meaning                                                                              |
+=============================================================+======================================================================================+
| ``public sealed override ModuleCategory Category { get; }`` | Module responsibility category; it does not independently determine execution phase. |
+-------------------------------------------------------------+--------------------------------------------------------------------------------------+

.. _evs-api-interior--interiorvaluesource:

InteriorValueSource
-------------------

**Runtime/Interior/Controls/InteriorValueSource.cs**

Base adapter for an ``IInteriorValueSource`` value producer.

**Inherits / implements:** ``MonoBehaviour``, :ref:`IInteriorValueSource <evs-api-interior--iinteriorvaluesource>`.

.. _evs-api-interior--methods-13:

Methods
~~~~~~~

+---------------------------------------+----------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| Signature                             | Role and behavior                                                                      | Arguments and result                                                   |
+=======================================+========================================================================================+========================================================================+
| ``public abstract float ReadValue()`` | Reads a numeric instrument source in the source's documented physical/normalized unit. | **Returns:** Computed float in the operation's documented unit/domain. |
+---------------------------------------+----------------------------------------------------------------------------------------+------------------------------------------------------------------------+

.. _evs-api-interior--profileswitchbinding:

ProfileSwitchBinding
--------------------

**Runtime/Interior/Controls/ProfileSwitchBinding.cs**

Configuration/implementation type for profile switch binding within cockpit instruments and bindings.

**Inherits / implements:** ``MonoBehaviour``.

.. _evs-api-interior--methods-14:

Methods
~~~~~~~

+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                           | Role and behavior                                                                                                                   | Arguments and result                                                                                                                                                                    |
+=====================================================+=====================================================================================================================================+=========================================================================================================================================================================================+
| ``public virtual void Tick(float deltaTime)``       | Advances the declaring presentation/state machine by elapsed seconds; avoid a second call when its built-in owner already ticks it. | ``deltaTime`` — Elapsed time in seconds supplied by the owning loop.                                                                                                                    |
+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SetOn(bool on)``              | Requests onProfileId when on is true, otherwise offProfileId.                                                                       | ``on`` — Select the configured on or off registration ID. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Synchronize(bool immediate)`` | Synchronizes presentation/selector state with its source; gearbox synchronization is not a validated driving shift request.         | ``immediate`` — Whether to bypass normal presentation travel.                                                                                                                           |
+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-interior--state-and-configuration-11:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------+-------------------------------------------------------------------------------------------------+
| Member                                     | Meaning                                                                                         |
+============================================+=================================================================================================+
| ``public VehicleController vehicle``       | Authored vehicle used by ``ProfileSwitchBinding``.                                              |
+--------------------------------------------+-------------------------------------------------------------------------------------------------+
| ``public ProfileSwitcher profileSwitcher`` | Authored profile switcher used by ``ProfileSwitchBinding``.                                     |
+--------------------------------------------+-------------------------------------------------------------------------------------------------+
| ``public SwitchHandle switchHandle``       | Authored switch handle used by ``ProfileSwitchBinding``.                                        |
+--------------------------------------------+-------------------------------------------------------------------------------------------------+
| ``public string onProfileId``              | Registration ID requested by the on position; defaults to hover.                                |
+--------------------------------------------+-------------------------------------------------------------------------------------------------+
| ``public string offProfileId``             | Registration ID requested by the off position; defaults to drive.                               |
+--------------------------------------------+-------------------------------------------------------------------------------------------------+
| ``public bool animateHandle``              | Enable when this binding owns visual stepping. Disable if Passengers already steps this handle. |
+--------------------------------------------+-------------------------------------------------------------------------------------------------+

.. _evs-api-interior--rearmirror:

RearMirror
----------

**Runtime/Interior/Render/RearMirrors.cs**

Configuration/implementation type for rear mirror within cockpit instruments and bindings.

.. _evs-api-interior--state-and-configuration-12:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------+----------------------------------------------------------------------------------+
| Member                               | Meaning                                                                          |
+======================================+==================================================================================+
| ``public bool active``               | Authored active used by ``RearMirror``. Initial value: ``true``.                 |
+--------------------------------------+----------------------------------------------------------------------------------+
| ``public Renderer surface``          | Authored surface used by ``RearMirror``.                                         |
+--------------------------------------+----------------------------------------------------------------------------------+
| ``public Camera camera``             | Authored camera used by ``RearMirror``.                                          |
+--------------------------------------+----------------------------------------------------------------------------------+
| ``public RenderTexture texture``     | Authored texture used by ``RearMirror``.                                         |
+--------------------------------------+----------------------------------------------------------------------------------+
| ``public string textureProperty``    | Authored texture property used by ``RearMirror``. Initial value: ``"_BaseMap"``. |
+--------------------------------------+----------------------------------------------------------------------------------+
| ``public float fieldOfView``         | Authored field of view used by ``RearMirror``. Initial value: ``55``.            |
+--------------------------------------+----------------------------------------------------------------------------------+
| ``public float nearClip``            | Mirror camera's near clipping distance, in metres.                               |
+--------------------------------------+----------------------------------------------------------------------------------+
| ``public float farClip``             | Mirror camera's far clipping distance, in metres.                                |
+--------------------------------------+----------------------------------------------------------------------------------+
| ``public int resolution``            | Authored resolution used by ``RearMirror``. Initial value: ``256``.              |
+--------------------------------------+----------------------------------------------------------------------------------+
| ``public float aspectRatio``         | Authored aspect ratio used by ``RearMirror``. Initial value: ``1.8f``.           |
+--------------------------------------+----------------------------------------------------------------------------------+
| ``public float refreshRate``         | Authored refresh rate used by ``RearMirror``. Initial value: ``20``.             |
+--------------------------------------+----------------------------------------------------------------------------------+
| ``public float maximumViewDistance`` | Authored maximum view distance used by ``RearMirror``. Initial value: ``25``.    |
+--------------------------------------+----------------------------------------------------------------------------------+
| ``public LayerMask cullingMask``     | Authored culling mask used by ``RearMirror``. Initial value: ``~0``.             |
+--------------------------------------+----------------------------------------------------------------------------------+
| ``public bool flipHorizontally``     | Authored flip horizontally used by ``RearMirror``. Initial value: ``true``.      |
+--------------------------------------+----------------------------------------------------------------------------------+

.. _evs-api-interior--rearmirrors:

RearMirrors
-----------

**Runtime/Interior/Render/RearMirrors.cs**

Owns mirror eligibility, camera rendering and generated textures.

**Inherits / implements:** :ref:`InteriorModule <evs-api-interior--interiormodule>`.

.. _evs-api-interior--methods-15:

Methods
~~~~~~~

+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                         | Role and behavior                                                                                                 | Arguments and result                                                                                                                                                                                                       |
+===================================================================================================+===================================================================================================================+============================================================================================================================================================================================================================+
| ``public virtual void SetMirrorsEnabled(bool value)``                                             | Changes the whole mirror system's rendering availability.                                                         | ``value`` — Requested bool state for this operation.                                                                                                                                                                       |
+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetMirrorEnabled(int index, bool value)``                                   | Changes eligibility of one mirror entry.                                                                          | ``index`` — Zero-based configured-entry index; use the owner's current list ordering. ``value`` — Requested bool state for this operation.                                                                                 |
+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetCameraPose(int index, Vector3 localPosition, Quaternion localRotation)`` | Sets local camera position/rotation for the indexed mirror. The index must be valid; a missing camera is ignored. | ``index`` — Zero-based configured-entry index; use the owner's current list ordering. ``localPosition`` — Position in the selected parent/local frame. ``localRotation`` — Orientation in the selected parent/local frame. |
+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-interior--events-and-inspector-callbacks-4:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------+------------------------------------------------------------------------+
| Declaration                                             | Trigger, payload and meaning                                           |
+=========================================================+========================================================================+
| ``public event Action<bool> MirrorsEnabledChanged``     | When whole-system mirror eligibility changes. Payload: bool.           |
+---------------------------------------------------------+------------------------------------------------------------------------+
| ``public event Action<int, bool> MirrorEnabledChanged`` | When one mirror's eligibility changes. Payload: mirror index and bool. |
+---------------------------------------------------------+------------------------------------------------------------------------+

.. _evs-api-interior--state-and-configuration-13:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------+--------------------------------------------------------------------------------------+
| Member                                | Meaning                                                                              |
+=======================================+======================================================================================+
| ``public Camera observer``            | Authored observer used by ``RearMirrors``.                                           |
+---------------------------------------+--------------------------------------------------------------------------------------+
| ``public List<RearMirror> mirrors``   | Authored mirrors used by ``RearMirrors``. Initial value: ``new List<RearMirror>()``. |
+---------------------------------------+--------------------------------------------------------------------------------------+
| ``public bool mirrorsEnabled``        | Authored mirrors enabled used by ``RearMirrors``. Initial value: ``true``.           |
+---------------------------------------+--------------------------------------------------------------------------------------+
| ``public int maximumRendersPerFrame`` | Authored maximum renders per frame used by ``RearMirrors``. Initial value: ``2``.    |
+---------------------------------------+--------------------------------------------------------------------------------------+

.. _evs-api-interior--rotaryhandle:

RotaryHandle
------------

**Runtime/Interior/Controls/RotaryHandle.cs**

Maps requested/source values to rotary presentation.

**Inherits / implements:** ``MonoBehaviour``.

.. _evs-api-interior--methods-16:

Methods
~~~~~~~

+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| Signature                                                    | Role and behavior                                                                                                                                             | Arguments and result                                                                                  |
+==============================================================+===============================================================================================================================================================+=======================================================================================================+
| ``public virtual void Bind(MonoBehaviour valueSource)``      | Sets the ongoing instrument value source; ``null`` releases source ownership for explicit value API control.                                                  | ``valueSource`` — Instrument source taking ongoing value ownership; ``null`` releases source binding. |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| ``public virtual void Tick(float deltaTime)``                | Advances the declaring presentation/state machine by elapsed seconds; avoid a second call when its built-in owner already ticks it.                           | ``deltaTime`` — Elapsed time in seconds supplied by the owning loop.                                  |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| ``public virtual void SetNormalizedValue(float normalized)`` | Maps a normalized fraction across an instrument's configured physical value range.                                                                            | ``normalized`` — Normalized value; the owner maps it to its configured range.                         |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| ``public virtual void SetValue(float value)``                | Requests an instrument value in the configured physical/source range and emits ``ValueChanged`` for an actual request change; presentation smooths toward it. | ``value`` — Requested value in the instrument's configured source units.                              |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
| ``public virtual void SetImmediate(float value)``            | Applies the requested instrument value without smoothing, using the component's value-range and notification policy.                                          | ``value`` — Requested value in the instrument's configured source units.                              |
+--------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+

.. _evs-api-interior--events-and-inspector-callbacks-5:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Declaration                                        | Trigger, payload and meaning                                                                                                                                    |
+====================================================+=================================================================================================================================================================+
| ``public event System.Action<float> ValueChanged`` | When the requested instrument value changes. Payload: value in configured source units; this is not a motion-arrival notification.                              |
+----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent<float> onValueChanged``        | After this control's value changes. Payload: the event's value type; ``PedalHandle`` reports displayed travel, ``SwitchHandle`` reports a changed bool request. |
+----------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-interior--state-and-configuration-14:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| Member                                                 | Meaning                                                                                                   |
+========================================================+===========================================================================================================+
| ``public AnchoredRotation motion``                     | Authored motion used by ``RotaryHandle``. Initial value: ``new AnchoredRotation()``.                      |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public MonoBehaviour source``                        | Optional component implementing ``IInteriorValueSource``; leave empty for API or ``UnityEvents`` control. |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public float minimumValue``                          | Authored minimum value used by ``RotaryHandle``.                                                          |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public float maximumValue``                          | Authored maximum value used by ``RotaryHandle``. Initial value: ``1``.                                    |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public float minimumAngle``                          | Authored minimum angle used by ``RotaryHandle``. Initial value: ``-135``.                                 |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public float maximumAngle``                          | Authored maximum angle used by ``RotaryHandle``. Initial value: ``135``.                                  |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public float response``                              | Exponential visual response per second. Zero applies the requested angle immediately.                     |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public virtual float Value { get; }``                | Requested/current instrument-domain value exposed by this control, not a universal 0–1 axis.              |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public virtual float NormalizedValue { get; }``      | Read-only/resolved normalized value for ``RotaryHandle``.                                                 |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+
| ``public virtual float Angle { get; protected set; }`` | Read-only/resolved angle for ``RotaryHandle``.                                                            |
+--------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+

.. _evs-api-interior--speedvaluesource:

SpeedValueSource
----------------

**Runtime/Interior/Controls/SpeedValueSource.cs**

Configuration/implementation type for speed value source within cockpit instruments and bindings.

**Inherits / implements:** :ref:`InteriorValueSource <evs-api-interior--interiorvaluesource>`.

.. _evs-api-interior--methods-17:

Methods
~~~~~~~

+---------------------------------------+----------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| Signature                             | Role and behavior                                                                      | Arguments and result                                                   |
+=======================================+========================================================================================+========================================================================+
| ``public override float ReadValue()`` | Reads a numeric instrument source in the source's documented physical/normalized unit. | **Returns:** Computed float in the operation's documented unit/domain. |
+---------------------------------------+----------------------------------------------------------------------------------------+------------------------------------------------------------------------+

.. _evs-api-interior--state-and-configuration-15:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------+------------------------------------------------+
| Member                               | Meaning                                        |
+======================================+================================================+
| ``public VehicleController vehicle`` | Authored vehicle used by ``SpeedValueSource``. |
+--------------------------------------+------------------------------------------------+
| ``public bool signed``               | Authored signed used by ``SpeedValueSource``.  |
+--------------------------------------+------------------------------------------------+

+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| Member                         | Meaning                                                                                                                                     |
+================================+=============================================================================================================================================+
| ``public SpeedUnit speedUnit`` | Output unit; defaults to Kph. Changing this does not alter vehicle physics. For a signed SpeedValueSource, reverse motion remains negative. |
+--------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-interior--steeringstickanimator:

SteeringStickAnimator
---------------------

**Runtime/Interior/Animators/SteeringStickAnimator.cs**

Configuration/implementation type for steering stick animator within cockpit instruments and bindings.

**Inherits / implements:** :ref:`SteeringWheelAnimator <evs-api-interior--steeringwheelanimator>`.

.. _evs-api-interior--methods-18:

Methods
~~~~~~~

+----------------------------------------------+--------------------------------------------------------------------------------------+----------------------------------+
| Signature                                    | Role and behavior                                                                    | Arguments and result             |
+==============================================+======================================================================================+==================================+
| ``public override void PrepareHandPose()``   | Prepares the hand pose associated with this cockpit animator.                        | No arguments; no returned value. |
+----------------------------------------------+--------------------------------------------------------------------------------------+----------------------------------+
| ``public override void CalibrateRestPose()`` | Captures the model's current neutral presentation frame for later control animation. | No arguments; no returned value. |
+----------------------------------------------+--------------------------------------------------------------------------------------+----------------------------------+

.. _evs-api-interior--state-and-configuration-16:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------+-------------------------------------------------------------------------------------------------+
| Member                                               | Meaning                                                                                         |
+======================================================+=================================================================================================+
| ``public Transform rotationPivot``                   | Floor/base pivot. Place the stick mesh and its grip targets below this transform.               |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------+
| ``public JoystickHandle stickHandle``                | Authored stick handle used by ``SteeringStickAnimator``.                                        |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------+
| ``public StickSetup stickSetup``                     | Authored stick setup used by ``SteeringStickAnimator``.                                         |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------+
| ``public Vector3 localPitchAxis``                    | Authored local pitch axis used by ``SteeringStickAnimator``. Initial value: ``Vector3.right``.  |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------+
| ``public Vector3 localRollAxis``                     | Authored local roll axis used by ``SteeringStickAnimator``. Initial value: ``Vector3.forward``. |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------+
| ``public float maximumPitch``                        | Authored maximum pitch used by ``SteeringStickAnimator``. Initial value: ``6``.                 |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------+
| ``public float maximumRoll``                         | Authored maximum roll used by ``SteeringStickAnimator``. Initial value: ``6``.                  |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------+
| ``public float controlResponse``                     | Visual stick response per second.                                                               |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------+
| ``public PassengerSeat driverSeat``                  | Authored driver seat used by ``SteeringStickAnimator``.                                         |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------+
| ``public Transform leftHandRest``                    | Independent left-hand palm target, in cabin space. Reserved through the steering hand API.      |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------+
| ``public ThrottleAnimator throttle``                 | Authored throttle used by ``SteeringStickAnimator``.                                            |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------+
| ``public override bool SupportsHandRegrip { get; }`` | Read-only/resolved supports hand regrip for ``SteeringStickAnimator``.                          |
+------------------------------------------------------+-------------------------------------------------------------------------------------------------+

.. _evs-api-interior--steeringwheelanimator:

SteeringWheelAnimator
---------------------

**Runtime/Interior/Animators/SteeringWheelAnimator.cs**

Configuration/implementation type for steering wheel animator within cockpit instruments and bindings.

**Inherits / implements:** :ref:`InteriorModule <evs-api-interior--interiormodule>`.

.. _evs-api-interior--methods-19:

Methods
~~~~~~~

+-----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                     | Role and behavior                                                                                 | Arguments and result                                                                                                                                                                                                     |
+===============================================================================================+===================================================================================================+==========================================================================================================================================================================================================================+
| ``public virtual void PrepareHandPose()``                                                     | Prepares the hand pose associated with this cockpit animator.                                     | No arguments; no returned value.                                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)``    | Advances steering presentation/hand targets once in the fixed pipeline before passenger feedback. | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+-----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``[ContextMenu("Capture steering wheel rest pose")] public virtual void CalibrateRestPose()`` | Captures the model's current neutral presentation frame for later control animation.              | No arguments; no returned value.                                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-interior--state-and-configuration-17:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| Member                                                          | Meaning                                                                                             |
+=================================================================+=====================================================================================================+
| ``public VehicleController vehicle``                            | Authored vehicle used by ``SteeringWheelAnimator``.                                                 |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``public Transform steeringWheel``                              | Authored steering wheel used by ``SteeringWheelAnimator``.                                          |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``public Vector3 localRotationAxis``                            | Authored local rotation axis used by ``SteeringWheelAnimator``. Initial value: ``Vector3.forward``. |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``public bool invert``                                          | Authored invert used by ``SteeringWheelAnimator``. Initial value: ``false``.                        |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``public float boatSteeringResponse``                           | Boat helm rendering response per second. Zero follows the resolved rudder immediately.              |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``public virtual float DisplayedAngle { get; protected set; }`` | Read-only/resolved displayed angle for ``SteeringWheelAnimator``.                                   |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``public virtual bool SupportsHandRegrip { get; }``             | Read-only/resolved supports hand regrip for ``SteeringWheelAnimator``.                              |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``public virtual float HandSteeringInput { get; }``             | Read-only/resolved hand steering input for ``SteeringWheelAnimator``.                               |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }``               | Cross-category execution barrier used by the module pipeline.                                       |
+-----------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+

.. _evs-api-interior--sticksetup:

StickSetup
----------

**Runtime/Interior/Controls/StickSetup.cs**

Configuration/implementation type for stick setup within cockpit instruments and bindings.

**Inherits / implements:** :ref:`AircraftControlMotion <evs-api-interior--aircraftcontrolmotion>`.

.. _evs-api-interior--methods-20:

Methods
~~~~~~~

+--------------------------------------------------------------+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+
| Signature                                                    | Role and behavior                                                               | Arguments and result                                                                                                   |
+==============================================================+=================================================================================+========================================================================================================================+
| ``public virtual void SetControls(float pitch, float roll)`` | Applies normalized pitch/roll control presentation to the authored stick setup. | ``pitch`` — Normalized pitch input, or audio pitch multiplier in an audio operation. ``roll`` — Normalized roll input. |
+--------------------------------------------------------------+---------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-interior--state-and-configuration-18:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------+--------------------------------------------------------------------------------------+
| Member                           | Meaning                                                                              |
+==================================+======================================================================================+
| ``public Vector3 localRollAxis`` | Authored local roll axis used by ``StickSetup``. Initial value: ``Vector3.forward``. |
+----------------------------------+--------------------------------------------------------------------------------------+
| ``public float minimumRoll``     | Authored minimum roll used by ``StickSetup``. Initial value: ``-6``.                 |
+----------------------------------+--------------------------------------------------------------------------------------+
| ``public float maximumRoll``     | Authored maximum roll used by ``StickSetup``. Initial value: ``6``.                  |
+----------------------------------+--------------------------------------------------------------------------------------+

.. _evs-api-interior--throttleanimator:

ThrottleAnimator
----------------

**Runtime/Interior/Animators/ThrottleAnimator.cs**

Configuration/implementation type for throttle animator within cockpit instruments and bindings.

**Inherits / implements:** :ref:`InteriorModule <evs-api-interior--interiormodule>`.

.. _evs-api-interior--methods-21:

Methods
~~~~~~~

+------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                | Role and behavior                                                                                                | Arguments and result                                                                                                                                                                                                                                   |
+==========================================================================================+==================================================================================================================+========================================================================================================================================================================================================================================================+
| ``public virtual bool PrepareHandPose()``                                                | Prepares the hand pose associated with this cockpit animator.                                                    | **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated.                                                                                                                          |
+------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Configure(VehicleController owner)``                              | Stores the vehicle supplying throttle presentation.                                                              | ``owner`` — Unity/application owner whose identity controls this relationship or resource.                                                                                                                                                             |
+------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController owner, Command command, float deltaTime)`` | Resolves external or vehicle throttle, smooths lever presentation and updates changed displayed value/hand pose. | ``owner`` — Unity/application owner whose identity controls this relationship or resource. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetThrottle(float value)``                                         | Takes external ownership of normalized throttle-lever presentation; ``FollowVehicle`` releases that override.    | ``value`` — Requested state/value in this operation's domain; use its configured range/unit.                                                                                                                                                           |
+------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void FollowVehicle()``                                                  | Releases external presentation ownership and resumes vehicle-state following.                                    | No arguments; no returned value.                                                                                                                                                                                                                       |
+------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-interior--events-and-inspector-callbacks-6:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------+--------------------------------------------------------------------------------------------+
| Declaration                                        | Trigger, payload and meaning                                                               |
+====================================================+============================================================================================+
| ``public event System.Action<float> ValueChanged`` | When resolved throttle presentation changes. Payload: normalized displayed throttle value. |
+----------------------------------------------------+--------------------------------------------------------------------------------------------+

.. _evs-api-interior--state-and-configuration-19:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+
| Member                                                          | Meaning                                                                                                      |
+=================================================================+==============================================================================================================+
| ``public VehicleController vehicle``                            | Authored vehicle used by ``ThrottleAnimator``.                                                               |
+-----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+
| ``public ThrottleHandle throttleHandle``                        | Authored throttle handle used by ``ThrottleAnimator``.                                                       |
+-----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+
| ``public AircraftControlMotion motion``                         | Authored motion used by ``ThrottleAnimator``.                                                                |
+-----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+
| ``public PassengerSeat driverSeat``                             | Authored driver seat used by ``ThrottleAnimator``.                                                           |
+-----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+
| ``public Transform handAnchor``                                 | Fallback palm pose when the motion helper has no ``ThrottleSetup.handAnchor``. Parent it to the moving grip. |
+-----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+
| ``public virtual Transform HandAnchor { get; }``                | Read-only/resolved hand anchor for ``ThrottleAnimator``.                                                     |
+-----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+
| ``public bool useLeftHand``                                     | Uses the driver's left hand rather than the right for this control.                                          |
+-----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+
| ``public float response``                                       | Authored response used by ``ThrottleAnimator``. Initial value: ``5``.                                        |
+-----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+
| ``public bool useExternalValue``                                | Uses explicit cockpit presentation instead of following vehicle throttle.                                    |
+-----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+
| ``public float externalValue``                                  | Authored external value used by ``ThrottleAnimator``.                                                        |
+-----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+
| ``public virtual float DisplayedValue { get; protected set; }`` | Read-only/resolved displayed value for ``ThrottleAnimator``.                                                 |
+-----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }``               | Cross-category execution barrier used by the module pipeline.                                                |
+-----------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+

.. _evs-api-interior--throttlesetup:

ThrottleSetup
-------------

**Runtime/Interior/Controls/ThrottleSetup.cs**

Configuration/implementation type for throttle setup within cockpit instruments and bindings.

**Inherits / implements:** :ref:`AircraftControlMotion <evs-api-interior--aircraftcontrolmotion>`.

.. _evs-api-interior--state-and-configuration-20:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------+------------------------------------------------------------------------------------+
| Member                          | Meaning                                                                            |
+=================================+====================================================================================+
| ``public Transform handAnchor`` | Palm contact pose. Rotate this anchor to orient the hand around the throttle grip. |
+---------------------------------+------------------------------------------------------------------------------------+

.. _evs-api-interior--wiper:

Wiper
-----

**Runtime/Interior/Wipers/Wipers.cs**

Configuration/implementation type for wiper within cockpit instruments and bindings.

.. _evs-api-interior--state-and-configuration-21:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------+------------------------------------------------------------------------+
| Member                                 | Meaning                                                                |
+========================================+========================================================================+
| ``public WiperBlade helper``           | Authored helper used by Wiper.                                         |
+----------------------------------------+------------------------------------------------------------------------+
| ``public WiperType type``              | Authored type used by Wiper.                                           |
+----------------------------------------+------------------------------------------------------------------------+
| ``public Transform anchor``            | Authored anchor used by Wiper.                                         |
+----------------------------------------+------------------------------------------------------------------------+
| ``public Transform blade``             | Authored blade used by Wiper.                                          |
+----------------------------------------+------------------------------------------------------------------------+
| ``public Vector3 anchorLocalPosition`` | Blade position expressed relative to the optional anchor, in metres.   |
+----------------------------------------+------------------------------------------------------------------------+
| ``public Vector3 localAxis``           | Authored local axis used by Wiper. Initial value: ``Vector3.forward``. |
+----------------------------------------+------------------------------------------------------------------------+
| ``public float parkedAngle``           | Authored parked angle used by Wiper.                                   |
+----------------------------------------+------------------------------------------------------------------------+
| ``public float sweepAngle``            | Authored sweep angle used by Wiper. Initial value: ``75``.             |
+----------------------------------------+------------------------------------------------------------------------+
| ``public bool reverse``                | Authored reverse used by Wiper.                                        |
+----------------------------------------+------------------------------------------------------------------------+

.. _evs-api-interior--wiperblade:

WiperBlade
----------

**Runtime/Interior/Wipers/WiperBlade.cs**

Maps normalized stroke to authored blade geometry.

**Inherits / implements:** ``MonoBehaviour``.

.. _evs-api-interior--methods-22:

Methods
~~~~~~~

+-----------------------------------------------+----------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| Signature                                     | Role and behavior                                                                                        | Arguments and result                                                                         |
+===============================================+==========================================================================================================+==============================================================================================+
| ``public virtual void CaptureRestPose()``     | Captures the currently authored rest pose for this geometry mapper or blade.                             | No arguments; no returned value.                                                             |
+-----------------------------------------------+----------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``public virtual void SetValue(float value)`` | Applies normalized blade stroke using the captured spindle/rest geometry; it does not run a wiper clock. | ``value`` — Requested state/value in this operation's domain; use its configured range/unit. |
+-----------------------------------------------+----------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``public virtual void ParkImmediate()``       | Places the blade at its parked pose without waiting for a wiper cycle.                                   | No arguments; no returned value.                                                             |
+-----------------------------------------------+----------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+

.. _evs-api-interior--state-and-configuration-22:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| Member                                                 | Meaning                                                                                                          |
+========================================================+==================================================================================================================+
| ``public AnchoredRotation motion``                     | Authored motion used by ``WiperBlade``. Initial value: ``new AnchoredRotation { localAxis = Vector3.forward }``. |
+--------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``public WiperType type``                              | Authored type used by ``WiperBlade``.                                                                            |
+--------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``public float minimumAngle``                          | Authored minimum angle used by ``WiperBlade``.                                                                   |
+--------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``public float maximumAngle``                          | Authored maximum angle used by ``WiperBlade``. Initial value: ``65``.                                            |
+--------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``public virtual float Value { get; protected set; }`` | Current value in this control's domain; use the declaring control's detailed value contract.                     |
+--------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``public virtual float Angle { get; }``                | Read-only/resolved angle for ``WiperBlade``.                                                                     |
+--------------------------------------------------------+------------------------------------------------------------------------------------------------------------------+

.. _evs-api-interior--wiperswitchbinding:

WiperSwitchBinding
------------------

**Runtime/Interior/Wipers/WiperSwitchBinding.cs**

Configuration/implementation type for wiper switch binding within cockpit instruments and bindings.

**Inherits / implements:** ``MonoBehaviour``.

.. _evs-api-interior--methods-23:

Methods
~~~~~~~

+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+
| Signature                                           | Role and behavior                                                                                                                   | Arguments and result                                                 |
+=====================================================+=====================================================================================================================================+======================================================================+
| ``public virtual void Tick(float deltaTime)``       | Advances the declaring presentation/state machine by elapsed seconds; avoid a second call when its built-in owner already ticks it. | ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+
| ``public virtual void Synchronize(bool immediate)`` | Synchronizes presentation/selector state with its source; gearbox synchronization is not a validated driving shift request.         | ``immediate`` — Whether to bypass normal presentation travel.        |
+-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------+

.. _evs-api-interior--state-and-configuration-23:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------+------------------------------------------------------------------------------------+
| Member                               | Meaning                                                                            |
+======================================+====================================================================================+
| ``public Wipers wipers``             | Authored wipers used by ``WiperSwitchBinding``.                                    |
+--------------------------------------+------------------------------------------------------------------------------------+
| ``public SwitchHandle switchHandle`` | Authored switch handle used by ``WiperSwitchBinding``.                             |
+--------------------------------------+------------------------------------------------------------------------------------+
| ``public bool onMeansRunning``       | Authored on means running used by ``WiperSwitchBinding``. Initial value: ``true``. |
+--------------------------------------+------------------------------------------------------------------------------------+
| ``public bool animateHandle``        | Authored animate handle used by ``WiperSwitchBinding``.                            |
+--------------------------------------+------------------------------------------------------------------------------------+

.. _evs-api-interior--wipertype:

WiperType
---------

**Runtime/Interior/Wipers/Wipers.cs**

Defines the allowed wiper type choices used by this topic.

.. _evs-api-interior--values-2:

Values
~~~~~~

-  ``Front``
-  ``Rear``
-  ``Custom``

.. _evs-api-interior--wipers:

Wipers
------

**Runtime/Interior/Wipers/Wipers.cs**

Owns wiper cycle timing, running state and blade dispatch.

**Inherits / implements:** :ref:`InteriorModule <evs-api-interior--interiormodule>`.

.. _evs-api-interior--methods-24:

Methods
~~~~~~~

+---------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| Signature                                                     | Role and behavior                                                                                                                   | Arguments and result                                                   |
+===============================================================+=====================================================================================================================================+========================================================================+
| ``public override void Configure(VehicleController vehicle)`` | Applies current blade pose only during Play Mode so Edit Mode configuration does not recapture an animated neutral pose.            | ``vehicle`` — Vehicle context/owner receiving the operation.           |
+---------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| ``public virtual void Tick(float deltaTime)``                 | Advances the declaring presentation/state machine by elapsed seconds; avoid a second call when its built-in owner already ticks it. | ``deltaTime`` — Elapsed time in seconds supplied by the owning loop.   |
+---------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| ``public virtual void SetRunning(bool value)``                | Requests the wiper running state; stopping finishes the current cycle before parking.                                               | ``value`` — Requested bool state for this operation.                   |
+---------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| ``public virtual void Toggle()``                              | Requests the opposite current body/switch/wiper/profile/gear state through the declaring component.                                 | No arguments; no returned value.                                       |
+---------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| ``public virtual void SetSpeed(float speed)``                 | Changes wiper cycle speed; zero pauses cycle motion.                                                                                | ``speed`` — Speed, interpreted by this operation in the declared type. |
+---------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+
| ``public virtual void CaptureRestPoses()``                    | Captures rest poses for the wiper geometry owned by the module.                                                                     | No arguments; no returned value.                                       |
+---------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------+

.. _evs-api-interior--events-and-inspector-callbacks-7:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| Declaration                                  | Trigger, payload and meaning                                                                                              |
+==============================================+===========================================================================================================================+
| ``public event Action<bool> StrokeStarted``  | When a wiper stroke starts. Payload: returning bool, ``true`` for the return stroke and ``false`` for the outward stroke. |
+----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<bool> RunningChanged`` | When the wiper running request changes. Payload: bool; a stop can still finish the current cycle.                         |
+----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<float> SpeedChanged``  | After ``SetSpeed`` changes requested wiper speed. Payload: configured cycle-speed value; zero pauses motion.              |
+----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+
| ``public event Action Parked``               | When wipers reach their parked state. No payload.                                                                         |
+----------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-interior--state-and-configuration-24:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| Member                                                              | Meaning                                                                                 |
+=====================================================================+=========================================================================================+
| ``public List<Wiper> wipers``                                       | Authored wipers used by Wipers. Initial value: ``new List<Wiper>()``.                   |
+---------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| ``public float cyclesPerMinute``                                    | Authored cycles per minute used by Wipers. Initial value: ``45``.                       |
+---------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| ``public AudioSource audioSource``                                  | Authored audio source used by Wipers.                                                   |
+---------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| ``public AudioClip outwardClip``                                    | Authored outward clip used by Wipers.                                                   |
+---------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| ``public AudioClip returnClip``                                     | Authored return clip used by Wipers.                                                    |
+---------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| ``public float volume``                                             | Authored volume used by Wipers. Initial value: ``.4f``.                                 |
+---------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| ``public bool synchronizeAudioSpeed``                               | Match the recorded stroke duration to the mechanical sweep speed.                       |
+---------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| ``public virtual AudioClip LastStrokeClip { get; protected set; }`` | Read-only/resolved last stroke clip for Wipers.                                         |
+---------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| ``public virtual bool IsRunning { get; }``                          | Current is running predicate; read it instead of maintaining a second application flag. |
+---------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
| ``public virtual bool IsParked { get; }``                           | Current is parked predicate; read it instead of maintaining a second application flag.  |
+---------------------------------------------------------------------+-----------------------------------------------------------------------------------------+

.. _evs-api-interior--yokeanimator:

YokeAnimator
------------

**Runtime/Interior/Animators/YokeAnimator.cs**

Configuration/implementation type for yoke animator within cockpit instruments and bindings.

**Inherits / implements:** :ref:`SteeringWheelAnimator <evs-api-interior--steeringwheelanimator>`.

.. _evs-api-interior--methods-25:

Methods
~~~~~~~

+----------------------------------------------+--------------------------------------------------------------------------------------+----------------------------------+
| Signature                                    | Role and behavior                                                                    | Arguments and result             |
+==============================================+======================================================================================+==================================+
| ``public override void CalibrateRestPose()`` | Captures the model's current neutral presentation frame for later control animation. | No arguments; no returned value. |
+----------------------------------------------+--------------------------------------------------------------------------------------+----------------------------------+

.. _evs-api-interior--state-and-configuration-25:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------+------------------------------------------------------------------------------------------------+
| Member                                               | Meaning                                                                                        |
+======================================================+================================================================================================+
| ``public Transform pitchSlide``                      | Sliding column, with the rotating yoke below it. Leave empty to slide the yoke itself.         |
+------------------------------------------------------+------------------------------------------------------------------------------------------------+
| ``public Vector3 localPitchTravelAxis``              | Authored local pitch travel axis used by ``YokeAnimator``. Initial value: ``Vector3.forward``. |
+------------------------------------------------------+------------------------------------------------------------------------------------------------+
| ``public float pitchTravel``                         | Authored pitch travel used by ``YokeAnimator``. Initial value: ``.035f``.                      |
+------------------------------------------------------+------------------------------------------------------------------------------------------------+
| ``public float controlResponse``                     | Visual control response per second, shared by roll and pitch.                                  |
+------------------------------------------------------+------------------------------------------------------------------------------------------------+
| ``public override float HandSteeringInput { get; }`` | Read-only/resolved hand steering input for ``YokeAnimator``.                                   |
+------------------------------------------------------+------------------------------------------------------------------------------------------------+
