.. _evs-scripting-audio--audio-ownership-and-extension:

Audio ownership and extension
=============================

Vehicle audio is organized as a core plus replaceable channels. The core owns common routing and spatial policy; a channel reads vehicle state or events and manages its particular voices. ``Engine``, tire, indicator and switch audio can therefore be configured or replaced independently.

An audio channel is a presentation consumer. It should use mechanical RPM, contact or accepted actions as inputs, rather than changing the engine or replaying input requests to infer what happened. This makes the same mechanic usable with a different sound implementation.

.. _evs-scripting-audio--implementation-map:

Implementation map
------------------

+------------------------+--------------------------------------------------------------------------+
| Class                  | Responsibility                                                           |
+========================+==========================================================================+
| ``Audio``              | Owns channel discovery, common audio settings and render-frame dispatch. |
+------------------------+--------------------------------------------------------------------------+
| ``AudioModule``        | Base channel with source creation, loop update and cleanup helpers.      |
+------------------------+--------------------------------------------------------------------------+
| ``EngineAudio``        | Selects and modulates the engine loop and ignition transitions.          |
+------------------------+--------------------------------------------------------------------------+
| ``EngineSoundProfile`` | Stores engine sound behavior and asset configuration.                    |
+------------------------+--------------------------------------------------------------------------+
| ``TireAudio``          | Consumes per-wheel contact/effect-surface state.                         |
+------------------------+--------------------------------------------------------------------------+
| ``IndicatorAudio``     | Follows actual indicator output phase.                                   |
+------------------------+--------------------------------------------------------------------------+
| ``DamageAudio``        | Separate Effects module for damage sound presentation.                   |
+------------------------+--------------------------------------------------------------------------+

.. _evs-scripting-audio--core-and-channels:

Core and channels
-----------------

Use ``AudioModule`` for a channel that belongs to the audio core's lifecycle. Its ``RenderAudio`` callback runs in the render-frame flow, which is appropriate for smooth volume and pitch changes. Do not schedule the same channel from ``Update`` as well, or its smoothing and playback logic will advance twice.

Use an event subscription when the signal is a discrete transition such as a settled switch click. Use a continuously read state for a loop such as engine RPM. In either case, release subscriptions and owned sources when the channel stops participating; an invisible or disabled vehicle should not leave orphaned voices behind.

``Audio`` owns routing/spatial configuration and advances its local ``AudioModule`` channels once per render frame. A channel creates sources through its core and owns cleanup. Core/channel disable suspends playback. ``DamageAudio`` is a separate Effects module; not every sound-producing component is an ``AudioModule`` channel.

.. _evs-scripting-audio--engine-sound-selection:

Engine sound selection
----------------------

``EngineAudio`` combines a sound choice with a response model. The selected clip/profile determines the character of the sound; engine running state, RPM and activity determine how it plays. This permits an engine recording to change without altering torque, shifting or fuel consumption.

``EngineSoundProfile.EvaluatePitch`` and ``EvaluateActivity`` provide reusable evaluation for the configured sound behavior. A custom channel can use those calculations or replace modulation while still obtaining mechanical state from the engine. Keep pitch and volume changes in the audio domain; they should not write back into the RPM used by the drivetrain.

``TireAudio`` instead consumes wheel feedback and surface profiles. ``IndicatorAudio`` listens to output phase, and ``SwitchAudio`` listens to settled switches. These channels intentionally use different evidence. A custom all-in-one audio system should preserve those distinctions rather than interpreting every sound from throttle/brake input alone.

Separate asset selection from modulation. First resolve which loop should play from override/profile/fallback policy. Then determine its pitch and activity from the selected sound behavior and mechanical state. This allows one engine implementation to support different recordings without encoding asset names into the drivetrain.

A startup one-shot represents a running-state transition, not simply “this component has enabled.” This distinction prevents pooled or already-running vehicles from replaying ignition when their presentation is restored. Assign transition clips explicitly and check both fresh ignition and re-enabling an already-running engine.

``EngineAudio`` resolves ``soundOverride`` first, otherwise the current profile sound when ``useProfileSound`` is enabled, otherwise its ``engineLoop`` fallback. ``profileLoopOverride`` replaces a profile loop. RPM profiles can opt into engine-response tuning; Constant fixes pitch, Motion uses speed-based activity.

Ignition one-shots require assigned clips and an explicit running-state transition. Empty clips are silent at runtime. The editor's authoring defaults may populate clip references; runtime does not search for them. Loop-start delay applies to transitions; already-running scene engines do not synthesize a start.

``Propulsion`` spool gates/scales supported rotor/aircraft presentation separately from mechanical ignition. Sound pitch/volume does not set torque or RPM.

.. _evs-scripting-audio--add-a-custom-loop-channel:

Add a custom loop channel
-------------------------

The example lazily creates one voice through ``CreateSource``, then reuses it. ``UpdateLoop`` receives the desired clip, volume, pitch and response factor. The exponential response factor uses ``dt`` so smoothing tracks elapsed time instead of depending on a fixed number of render frames.

The voice is channel-owned; the clip is an assigned asset. Deriving from ``AudioModule`` keeps the base cleanup behavior. If a subclass overrides lifecycle cleanup, retain the base work or provide equivalent release of every source it created.

Attach this beside ``Audio``, assign a loop clip, and refresh the core's audio modules. It creates one owned source and lets the core apply routing. Base lifecycle cleanup remains intact.

**Example: ``AuxiliaryAudioLoop.cs``**

.. raw:: html

   <!-- example: AuxiliaryAudioLoop.cs -->

.. code-block:: csharp

   using UnityEngine;
   using EasyVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class AuxiliaryAudioLoop : AudioModule
       {
           public AudioClip loop;
           [Range(0, 1)] public float volume = .2f;
           private AudioSource voice;

           public override void RenderAudio(EasyVehicleSystem.Audio core, float dt)
           {
               if (!voice) voice = CreateSource(core, "Auxiliary loop", true);
               UpdateLoop(core, voice, loop, loop ? volume : 0, 1,
                   1 - Mathf.Exp(-core.response * dt));
           }
       }
   }

Do not destroy externally assigned clips/mixers. See :doc:`event subscriptions </Scripting/Events>` for custom event-driven audio and :doc:`presentation </Scripting/Presentation>` for generated visual resources.

.. _evs-scripting-audio--complete-public-method-and-event-index:

Complete public method and event index
--------------------------------------

The lists below cover public methods and events for this topic and their package base contracts. Signatures include overloads. See :doc:`the detailed audio cores and channels API </API/Audio>` for arguments, return semantics, state and configuration. An override replaces the matching inherited implementation; it is not an additional call to make.

.. _evs-scripting-audio--audio:

Audio
~~~~~

:ref:`Audio <evs-api-audio--audio>` gives the full declared contract.

+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| Method                                                                                                         | Role                                                                                                          |
+================================================================================================================+===============================================================================================================+
| ``public override void Configure(VehicleController owner)``                                                    | Stores the owner, ensures standard channels, refreshes channel order and resolves missing channel references. |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| ``public virtual void RefreshAudioModules()``                                                                  | Rebuilds the audio core's channel snapshot in effective execution order.                                      |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| ``public virtual void EnsureModules(System.Func<System.Type, AudioModule> addChannel = null)``                 | Ensures the audio core has its required standard channel components.                                          |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| ``public virtual float FilterCornerSqueal(float skid, bool corner, float deltaTime)``                          | Filters or evaluates corner squeal using the tire-audio policy without changing tire physics.                 |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| ``public virtual void PlayEvent(EffectEvent effect)``                                                          | Plays the configured presentation sound for a vehicle effect event.                                           |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| ``public virtual AudioSource CreateSource(string name, bool loop)``                                            | Creates an audio source with the audio core's routing/spatial policy.                                         |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| ``public virtual void UpdateLoop(AudioSource source, AudioClip clip, float volume, float pitch, float blend)`` | Updates an existing voice's clip, gain and pitch with the supplied response factor.                           |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+

.. _evs-scripting-audio--audiomodule:

AudioModule
~~~~~~~~~~~

:ref:`AudioModule <evs-api-audio--audiomodule>` gives the full declared contract.

+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Method                                                            | Role                                                                                                 |
+===================================================================+======================================================================================================+
| ``public abstract void RenderAudio(Audio core, float deltaTime)`` | Advances one channel's audio presentation for elapsed render time; the Audio core normally calls it. |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public virtual void SuspendAudio()``                            | Suspends the channel's playback and active subscriptions/resources as implemented by that channel.   |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+

.. _evs-scripting-audio--boatwateraudio:

BoatWaterAudio
~~~~~~~~~~~~~~

:ref:`BoatWaterAudio <evs-api-audio--boatwateraudio>` gives the full declared contract.

+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Method                                                            | Role                                                                                                 |
+===================================================================+======================================================================================================+
| ``public override void RenderAudio(Audio core, float deltaTime)`` | Advances one channel's audio presentation for elapsed render time; the Audio core normally calls it. |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public override void SuspendAudio()``                           | Suspends the channel's playback and active subscriptions/resources as implemented by that channel.   |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+

.. _evs-scripting-audio--brakeaudio:

BrakeAudio
~~~~~~~~~~

:ref:`BrakeAudio <evs-api-audio--brakeaudio>` gives the full declared contract.

+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Method                                                            | Role                                                                                                 |
+===================================================================+======================================================================================================+
| ``public override void RenderAudio(Audio core, float deltaTime)`` | Advances one channel's audio presentation for elapsed render time; the Audio core normally calls it. |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+

.. _evs-scripting-audio--engineaudio:

EngineAudio
~~~~~~~~~~~

:ref:`EngineAudio <evs-api-audio--engineaudio>` gives the full declared contract.

+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Method                                                            | Role                                                                                                 |
+===================================================================+======================================================================================================+
| ``public override void RenderAudio(Audio core, float deltaTime)`` | Advances one channel's audio presentation for elapsed render time; the Audio core normally calls it. |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public override void SuspendAudio()``                           | Suspends the channel's playback and active subscriptions/resources as implemented by that channel.   |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+

.. _evs-scripting-audio--enginesoundprofile:

EngineSoundProfile
~~~~~~~~~~~~~~~~~~

:ref:`EngineSoundProfile <evs-api-audio--enginesoundprofile>` gives the full declared contract.

+-------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| Method                                                                              | Role                                                                             |
+=====================================================================================+==================================================================================+
| ``public virtual float EvaluateActivity(VehicleController vehicle, Engine engine)`` | Evaluates sound activity from the configured sound profile and mechanical input. |
+-------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ``public virtual float EvaluatePitch(float activity)``                              | Evaluates audio pitch from the configured engine sound response.                 |
+-------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+

.. _evs-scripting-audio--eventaudio:

EventAudio
~~~~~~~~~~

:ref:`EventAudio <evs-api-audio--eventaudio>` gives the full declared contract.

+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Method                                                             | Role                                                                                                 |
+====================================================================+======================================================================================================+
| ``public override void RenderAudio(Audio owner, float deltaTime)`` | Advances one channel's audio presentation for elapsed render time; the Audio core normally calls it. |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public override void SuspendAudio()``                            | Suspends the channel's playback and active subscriptions/resources as implemented by that channel.   |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public virtual void PlayEvent(EffectEvent effect)``              | Plays the configured presentation sound for a vehicle effect event.                                  |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+

+---------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| Event / callback                                              | Role                                                                                         |
+===============================================================+==============================================================================================+
| ``public event System.Action<EffectEvent, AudioClip> Played`` | When ``EventAudio`` plays a resolved event clip. Payload: ``EffectEvent`` and ``AudioClip``. |
+---------------------------------------------------------------+----------------------------------------------------------------------------------------------+

.. _evs-scripting-audio--iaudiomodule:

IAudioModule
~~~~~~~~~~~~

:ref:`IAudioModule <evs-api-audio--iaudiomodule>` gives the full declared contract.

+---------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Method                                            | Role                                                                                                 |
+===================================================+======================================================================================================+
| ``void RenderAudio(Audio core, float deltaTime)`` | Advances one channel's audio presentation for elapsed render time; the Audio core normally calls it. |
+---------------------------------------------------+------------------------------------------------------------------------------------------------------+

.. _evs-scripting-audio--imodule:

IModule
~~~~~~~

:ref:`IModule <evs-api-modules--imodule>` gives the full declared contract.

+----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| Method                                                                     | Role                                                                                                                        |
+============================================================================+=============================================================================================================================+
| ``void Configure(VehicleController vehicle)``                              | Repeatable setup contract supplied with the owning ``VehicleController``.                                                   |
+----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+
| ``void Step(VehicleController vehicle, Command command, float deltaTime)`` | Contract for one owner-supplied fixed tick; implement only the module responsibility and use the supplied Command/timestep. |
+----------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+

.. _evs-scripting-audio--indicatoraudio:

IndicatorAudio
~~~~~~~~~~~~~~

:ref:`IndicatorAudio <evs-api-audio--indicatoraudio>` gives the full declared contract.

+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Method                                                            | Role                                                                                                 |
+===================================================================+======================================================================================================+
| ``public override void RenderAudio(Audio core, float deltaTime)`` | Advances one channel's audio presentation for elapsed render time; the Audio core normally calls it. |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public virtual void SetClips(AudioClip on, AudioClip off)``     | Replaces indicator tick clips, retaining generated defaults for independently unassigned clips.      |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public override void SuspendAudio()``                           | Suspends the channel's playback and active subscriptions/resources as implemented by that channel.   |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+

.. _evs-scripting-audio--module:

Module
~~~~~~

:ref:`Module <evs-api-modules--module>` gives the full declared contract.

+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Method                                                                                    | Role                                                                                                                                   |
+===========================================================================================+========================================================================================================================================+
| ``public virtual void Configure(VehicleController vehicle)``                              | Empty base setup hook. Derived components may cache references/apply persistent settings; the controller owns lifecycle notifications. |
+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Step(VehicleController vehicle, Command command, float deltaTime)`` | Empty base extension point. The controller schedules derived work and emits lifecycle notifications around it.                         |
+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetEnabled(bool value)``                                            | Changes module enabled state and publishes an actual requested-flag change.                                                            |
+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SupportsProfile(DriveProfile profile)``                             | Checks movement-family compatibility; this is independent of the Unity enabled flag.                                                   |
+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+

+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| Event / callback                                                          | Role                                                                                                              |
+===========================================================================+===================================================================================================================+
| ``public event System.Action<bool> EnabledChanged``                       | After ``SetEnabled`` changes the module flag. Payload: requested enabled bool; no event for an unchanged request. |
+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public event System.Action<VehicleController> Configured``              | After controller-driven module configuration. Payload: the owning ``VehicleController``.                          |
+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+
| ``public event System.Action<VehicleController, Command, float> Stepped`` | After this registered module has stepped. Payload: vehicle, sampled Command, timestep in seconds.                 |
+---------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+

.. _evs-scripting-audio--switchaudio:

SwitchAudio
~~~~~~~~~~~

:ref:`SwitchAudio <evs-api-audio--switchaudio>` gives the full declared contract.

+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Method                                                            | Role                                                                                                 |
+===================================================================+======================================================================================================+
| ``public override void RenderAudio(Audio core, float deltaTime)`` | Advances one channel's audio presentation for elapsed render time; the Audio core normally calls it. |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+

.. _evs-scripting-audio--tireaudio:

TireAudio
~~~~~~~~~

:ref:`TireAudio <evs-api-audio--tireaudio>` gives the full declared contract.

+------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| Method                                                                                         | Role                                                                                                 |
+================================================================================================+======================================================================================================+
| ``public override void RenderAudio(Audio core, float deltaTime)``                              | Advances one channel's audio presentation for elapsed render time; the Audio core normally calls it. |
+------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public virtual float FilterCornerSqueal(float skid, bool highSpeedCorner, float deltaTime)`` | Filters or evaluates corner squeal using the tire-audio policy without changing tire physics.        |
+------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
| ``public override void SuspendAudio()``                                                        | Suspends the channel's playback and active subscriptions/resources as implemented by that channel.   |
+------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+
