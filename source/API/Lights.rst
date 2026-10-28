.. _evs-api-lights--vehicle-lighting-api:

Vehicle lighting API
====================

Read :doc:`the system explanation </Scripting/Lights>` for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from ``MonoBehaviour``, ``Object`` or ``ScriptableObject`` are documented by Unity.

.. _evs-api-lights--types:

Types
-----

-  :ref:`BeamMode <evs-api-lights--beammode>`
-  :ref:`IndicatorState <evs-api-lights--indicatorstate>`
-  :ref:`LightChannel <evs-api-lights--lightchannel>`
-  :ref:`LightType <evs-api-lights--lighttype>`
-  :ref:`Lights <evs-api-lights--lights>`

.. _evs-api-lights--beammode:

BeamMode
--------

**Runtime/Exterior/Lights/Lights.cs**

Defines the allowed beam mode choices used by this topic.

.. _evs-api-lights--values:

Values
~~~~~~

-  ``Off``
-  ``Low``
-  ``High``

.. _evs-api-lights--indicatorstate:

IndicatorState
--------------

**Runtime/Exterior/Lights/Lights.cs**

Defines the allowed indicator state choices used by this topic.

.. _evs-api-lights--values-1:

Values
~~~~~~

-  ``Off``
-  ``Left``
-  ``Right``
-  ``Hazard``

.. _evs-api-lights--lightchannel:

LightChannel
------------

**Runtime/Exterior/Lights/LightChannel.cs**

One lamp/emission output channel, including lit output state and its output notification.

.. _evs-api-lights--methods:

Methods
~~~~~~~

+-----------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------+
| Signature                                     | Role and behavior                                                                                                                    | Arguments and result                                                           |
+===============================================+======================================================================================================================================+================================================================================+
| ``public virtual void Apply(bool requested)`` | Applies requested lit state/intensity to configured native lights and emission outputs, publishing ``LitChanged`` on output changes. | ``requested`` — Requested, interpreted by this operation in the declared type. |
+-----------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------+

.. _evs-api-lights--events-and-inspector-callbacks:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------+---------------------------------------------------------------------+
| Declaration                              | Trigger, payload and meaning                                        |
+==========================================+=====================================================================+
| ``public event Action<bool> LitChanged`` | When a ``LightChannel``'s actual lit output changes. Payload: bool. |
+------------------------------------------+---------------------------------------------------------------------+

.. _evs-api-lights--state-and-configuration:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------+---------------------------------------------------------------------------------------+
| Member                                                | Meaning                                                                               |
+=======================================================+=======================================================================================+
| ``public bool enabled``                               | Authored enabled used by ``LightChannel``. Initial value: ``true``.                   |
+-------------------------------------------------------+---------------------------------------------------------------------------------------+
| ``public Light[] lights``                             | Authored lights used by ``LightChannel``. Initial value: ``Array.Empty<Light>()``.    |
+-------------------------------------------------------+---------------------------------------------------------------------------------------+
| ``public Renderer[] lenses``                          | Authored lenses used by ``LightChannel``. Initial value: ``Array.Empty<Renderer>()``. |
+-------------------------------------------------------+---------------------------------------------------------------------------------------+
| ``public Color color``                                | Authored color used by ``LightChannel``. Initial value: ``Color.white``.              |
+-------------------------------------------------------+---------------------------------------------------------------------------------------+
| ``public float intensity``                            | Authored intensity used by ``LightChannel``. Initial value: ``4``.                    |
+-------------------------------------------------------+---------------------------------------------------------------------------------------+
| ``public float emission``                             | Authored emission used by ``LightChannel``. Initial value: ``2``.                     |
+-------------------------------------------------------+---------------------------------------------------------------------------------------+
| ``public virtual bool IsLit { get; protected set; }`` | Current is lit predicate; read it instead of maintaining a second application flag.   |
+-------------------------------------------------------+---------------------------------------------------------------------------------------+

.. _evs-api-lights--lighttype:

LightType
---------

**Runtime/Exterior/Lights/Lights.cs**

Defines the allowed light type choices used by this topic.

.. _evs-api-lights--values-2:

Values
~~~~~~

-  ``Headlights``
-  ``HighBeams``
-  ``Tail``
-  ``Brake``
-  ``Reverse``
-  ``LeftIndicator``
-  ``RightIndicator``

.. _evs-api-lights--lights:

Lights
------

**Runtime/Exterior/Lights/Lights.cs**

Owns beam/indicator requests, automatic outputs and timing.

**Inherits / implements:** :ref:`ExteriorModule <evs-api-modules--exteriormodule>`.

.. _evs-api-lights--methods-1:

Methods
~~~~~~~

+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                           | Role and behavior                                                                                             | Arguments and result                                                                                                                                                                  |
+=====================================================================================+===============================================================================================================+=======================================================================================================================================================================================+
| ``public override void Configure(VehicleController vehicle)``                       | Resolves missing Engine/Events references without replacing explicit assignments.                             | ``vehicle`` — Vehicle context/owner receiving the operation.                                                                                                                          |
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float dt)`` | Consumes light/indicator commands, advances the shared blink clock and applies resolved lamp/emission output. | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``dt`` — Elapsed time in seconds. |
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual LightChannel GetChannel(LightType type)``                          | Returns the configured lighting channel for the selected light role.                                          | ``type`` — Type, interpreted by this operation in the declared type. **Returns:** Returned ``LightChannel``; ownership remains as specified by the creating/lookup operation.         |
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void RestoreAutomaticLights()``                                    | Clears forced lighting overrides so automatic mechanic-following resumes.                                     | No arguments; no returned value.                                                                                                                                                      |
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetBeamMode(BeamMode mode)``                                  | Requests Off, Low or High beam policy through the lighting state machine.                                     | ``mode`` — Mode, interpreted by this operation in the declared type.                                                                                                                  |
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetLowBeams(bool on)``                                        | Requests low-beam availability/state through normal beam policy.                                              | ``on`` — On, interpreted by this operation in the declared type.                                                                                                                      |
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetTailLights(bool on)``                                      | Changes the tail-light request/availability policy.                                                           | ``on`` — On, interpreted by this operation in the declared type.                                                                                                                      |
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetTailOverride(bool? on)``                                   | Forces tail output on/off; ``null`` resumes normal beam-following.                                            | ``on`` — On, interpreted by this operation in the declared type.                                                                                                                      |
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetHazards(bool on)``                                         | Requests synchronized left/right hazard indicators.                                                           | ``on`` — On, interpreted by this operation in the declared type.                                                                                                                      |
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetLeftIndicator(bool on)``                                   | Requests or clears the left turn-indicator state.                                                             | ``on`` — On, interpreted by this operation in the declared type.                                                                                                                      |
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetRightIndicator(bool on)``                                  | Requests or clears the right turn-indicator state.                                                            | ``on`` — On, interpreted by this operation in the declared type.                                                                                                                      |
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetHeadlights(bool on)``                                      | Requests the headlight on/off policy through the lighting state machine.                                      | ``on`` — On, interpreted by this operation in the declared type.                                                                                                                      |
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetHighBeams(bool on)``                                       | Requests or releases high beams using the component's low-beam return policy.                                 | ``on`` — On, interpreted by this operation in the declared type.                                                                                                                      |
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetIndicators(IndicatorState value)``                         | Requests the selected direction/hazard indicator state.                                                       | ``value`` — Requested state/value in this operation's domain; use its configured range/unit.                                                                                          |
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetBrakeOverride(bool? on)``                                  | Forces brake output on/off; ``null`` restores mechanic-following.                                             | ``on`` — On, interpreted by this operation in the declared type.                                                                                                                      |
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetReverseOverride(bool? on)``                                | Forces reverse lamp output on/off; ``null`` resumes mechanic-following.                                       | ``on`` — On, interpreted by this operation in the declared type.                                                                                                                      |
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetChannelEnabled(LightType type, bool available)``           | Changes availability of a selected lighting channel independently of its requested state.                     | ``type`` — Type, interpreted by this operation in the declared type. ``available`` — Requested availability, distinct from mesh detachment.                                           |
+-------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-lights--events-and-inspector-callbacks-1:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| Declaration                                                      | Trigger, payload and meaning                                                                 |
+==================================================================+==============================================================================================+
| ``public event System.Action<bool> IndicatorPhaseChanged``       | When the shared flashing output phase changes. Payload: lit bool; hazards share one phase.   |
+------------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``public event System.Action<BeamMode> BeamModeChanged``         | When requested beam mode changes. Payload: ``BeamMode``.                                     |
+------------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| ``public event System.Action<IndicatorState> IndicatorsChanged`` | When requested direction/hazard state changes. Payload: ``IndicatorState``, not blink phase. |
+------------------------------------------------------------------+----------------------------------------------------------------------------------------------+

.. _evs-api-lights--state-and-configuration-1:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| Member                                                | Meaning                                                                                                         |
+=======================================================+=================================================================================================================+
| ``public Engine engine``                              | Authored engine used by Lights.                                                                                 |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public Events events``                              | Authored events used by Lights.                                                                                 |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public LightChannel headlights``                    | Authored headlights used by Lights. Initial value: ``new LightChannel()``.                                      |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public LightChannel highBeams``                     | Authored high beams used by Lights. Initial value: ``new LightChannel()``.                                      |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public LightChannel tailLights``                    | Rear position-lamp channel following headlights unless overridden.                                              |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public LightChannel brakeLights``                   | Optional Light sources and emissive renderers for the service brake.                                            |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public LightChannel reverseLights``                 | Optional Light sources and emissive renderers for selected reverse gear / direct reverse drive.                 |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public LightChannel leftIndicators``                | Authored left indicators used by Lights. Initial value: ``new LightChannel { color = new Color(1, .4f, 0) }``.  |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public LightChannel rightIndicators``               | Authored right indicators used by Lights. Initial value: ``new LightChannel { color = new Color(1, .4f, 0) }``. |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public float blinkInterval``                        | Authored blink interval used by Lights. Initial value: ``.45f``.                                                |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public bool automaticBrakeLights``                  | Authored automatic brake lights used by Lights. Initial value: ``true``.                                        |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public bool automaticReverseLights``                | Authored automatic reverse lights used by Lights. Initial value: ``true``.                                      |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public float brakeLightThreshold``                  | Minimum applied service brake that turns on stop lamps. Includes progressive and analog braking.                |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public bool handbrakeActivatesBrakeLights``         | Authored handbrake activates brake lights used by Lights. Initial value: ``false``.                             |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public virtual bool BrakeLightsOn { get; }``        | Read-only/resolved brake lights on for Lights.                                                                  |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public virtual bool ReverseLightsOn { get; }``      | Read-only/resolved reverse lights on for Lights.                                                                |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public virtual bool HeadlightsOn { get; }``         | Read-only/resolved headlights on for Lights.                                                                    |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public virtual bool HighBeamsOn { get; }``          | Read-only/resolved high beams on for Lights.                                                                    |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public virtual IndicatorState Indicators { get; }`` | Read-only/resolved indicators for Lights.                                                                       |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public virtual bool IndicatorFlashOn { get; }``     | Read-only/resolved indicator flash on for Lights.                                                               |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public virtual bool TailLightsOn { get; }``         | Read-only/resolved tail lights on for Lights.                                                                   |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public virtual bool LeftIndicatorsOn { get; }``     | Read-only/resolved left indicators on for Lights.                                                               |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public virtual bool RightIndicatorsOn { get; }``    | Read-only/resolved right indicators on for Lights.                                                              |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public virtual BeamMode BeamMode { get; }``         | Read-only/resolved beam mode for Lights.                                                                        |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public override int ExecutionOrder { get; }``       | Default local priority within phase/category.                                                                   |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }``     | Cross-category execution barrier used by the module pipeline.                                                   |
+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
