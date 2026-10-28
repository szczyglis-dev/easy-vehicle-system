.. _evs-api-audio--audio-cores-and-channels-api:

Audio cores and channels API
============================

Read :doc:`the system explanation </Scripting/Audio>` for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from ``MonoBehaviour``, ``Object`` or ``ScriptableObject`` are documented by Unity.

.. _evs-api-audio--types:

Types
-----

-  :ref:`Audio <evs-api-audio--audio>`
-  :ref:`AudioEvent <evs-api-audio--audioevent>`
-  :ref:`AudioModule <evs-api-audio--audiomodule>`
-  :ref:`BoatWaterAudio <evs-api-audio--boatwateraudio>`
-  :ref:`BrakeAudio <evs-api-audio--brakeaudio>`
-  :ref:`CommercialAudio <evs-api-audio--commercialaudio>`
-  :ref:`DamageAudio <evs-api-audio--damageaudio>`
-  :ref:`EngineAudio <evs-api-audio--engineaudio>`
-  :ref:`EnginePitchMode <evs-api-audio--enginepitchmode>`
-  :ref:`EngineSoundProfile <evs-api-audio--enginesoundprofile>`
-  :ref:`EventAudio <evs-api-audio--eventaudio>`
-  :ref:`IAudioModule <evs-api-audio--iaudiomodule>`
-  :ref:`IndicatorAudio <evs-api-audio--indicatoraudio>`
-  :ref:`SwitchAudio <evs-api-audio--switchaudio>`
-  :ref:`TireAudio <evs-api-audio--tireaudio>`

.. _evs-api-audio--audio:

Audio
-----

**Runtime/Effects/Audio/Audio.cs**

Owns channel discovery, common audio settings and render-frame dispatch.

**Inherits / implements:** :ref:`EffectsModule <evs-api-presentation--effectsmodule>`.

.. _evs-api-audio--methods:

Methods
~~~~~~~

+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                                      | Role and behavior                                                                                             | Arguments and result                                                                                                                                                                                                                                                                                                           |
+================================================================================================================+===============================================================================================================+================================================================================================================================================================================================================================================================================================================================+
| ``public override void Configure(VehicleController owner)``                                                    | Stores the owner, ensures standard channels, refreshes channel order and resolves missing channel references. | ``owner`` — Unity/application owner whose identity controls this relationship or resource.                                                                                                                                                                                                                                     |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void RefreshAudioModules()``                                                                  | Rebuilds the audio core's channel snapshot in effective execution order.                                      | No arguments; no returned value.                                                                                                                                                                                                                                                                                               |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void EnsureModules(System.Func<System.Type, AudioModule> addChannel = null)``                 | Ensures the audio core has its required standard channel components.                                          | ``addChannel`` — Optional audio-channel creation callback. Default: ``null``.                                                                                                                                                                                                                                                  |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float FilterCornerSqueal(float skid, bool corner, float deltaTime)``                          | Filters or evaluates corner squeal using the tire-audio policy without changing tire physics.                 | ``skid`` — Resolved skid activity. ``corner`` — Corner, interpreted by this operation in the declared type. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. **Returns:** Computed float in the operation's documented unit/domain.                                                                        |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void PlayEvent(EffectEvent effect)``                                                          | Plays the configured presentation sound for a vehicle effect event.                                           | ``effect`` — Resolved vehicle ``EffectEvent`` to present.                                                                                                                                                                                                                                                                      |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual AudioSource CreateSource(string name, bool loop)``                                            | Creates an audio source with the audio core's routing/spatial policy.                                         | ``name`` — Diagnostic name for the generated source/object. ``loop`` — Whether the created voice should loop. **Returns:** Returned ``AudioSource``; ownership remains as specified by the creating/lookup operation.                                                                                                          |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void UpdateLoop(AudioSource source, AudioClip clip, float volume, float pitch, float blend)`` | Updates an existing voice's clip, gain and pitch with the supplied response factor.                           | ``source`` — Explicit provider being selected or bound. ``clip`` — Assigned ``AudioClip``; ``null`` follows the declaring channel's silence/fallback policy. ``volume`` — Target audio gain. ``pitch`` — Normalized pitch input, or audio pitch multiplier in an audio operation. ``blend`` — Response/interpolation fraction. |
+----------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-audio--state-and-configuration:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+----------------------------------------------------------------------------+
| Member                                                          | Meaning                                                                    |
+=================================================================+============================================================================+
| ``public VehicleController vehicle``                            | Authored vehicle used by Audio.                                            |
+-----------------------------------------------------------------+----------------------------------------------------------------------------+
| ``public Engine engine``                                        | Authored engine used by Audio.                                             |
+-----------------------------------------------------------------+----------------------------------------------------------------------------+
| ``public Feedback feedback``                                    | Authored feedback used by Audio.                                           |
+-----------------------------------------------------------------+----------------------------------------------------------------------------+
| ``public Events events``                                        | Authored events used by Audio.                                             |
+-----------------------------------------------------------------+----------------------------------------------------------------------------+
| ``public AudioMixerGroup output``                               | Authored output used by Audio.                                             |
+-----------------------------------------------------------------+----------------------------------------------------------------------------+
| ``public float spatialBlend``                                   | Blend from nonspatial audio at zero to fully positional audio at one.      |
+-----------------------------------------------------------------+----------------------------------------------------------------------------+
| ``public float minDistance``                                    | Distance within which positional audio retains full volume, in metres.     |
+-----------------------------------------------------------------+----------------------------------------------------------------------------+
| ``public float maxDistance``                                    | Authored max distance used by Audio. Initial value: ``70``.                |
+-----------------------------------------------------------------+----------------------------------------------------------------------------+
| ``public float response``                                       | Authored response used by Audio. Initial value: ``8``.                     |
+-----------------------------------------------------------------+----------------------------------------------------------------------------+
| ``public virtual bool RequiresMigration { get; }``              | Read-only/resolved requires migration for Audio.                           |
+-----------------------------------------------------------------+----------------------------------------------------------------------------+
| ``public virtual AudioModule[] AudioModules { get; }``          | Read-only/resolved audio modules for Audio.                                |
+-----------------------------------------------------------------+----------------------------------------------------------------------------+
| ``public virtual AudioClip engineLoop { get; set; }``           | Configurable engine loop for Audio.                                        |
+-----------------------------------------------------------------+----------------------------------------------------------------------------+
| ``public virtual float engineVolume { get; set; }``             | Configurable engine volume for Audio.                                      |
+-----------------------------------------------------------------+----------------------------------------------------------------------------+
| ``public virtual float engineMixGain { get; set; }``            | Configurable engine mix gain for Audio.                                    |
+-----------------------------------------------------------------+----------------------------------------------------------------------------+
| ``public virtual float engineLoopReferenceRpm { get; set; }``   | Configurable engine loop reference rpm for Audio.                          |
+-----------------------------------------------------------------+----------------------------------------------------------------------------+
| ``public virtual float engineRpmPitchExponent { get; set; }``   | Configurable engine rpm pitch exponent for Audio.                          |
+-----------------------------------------------------------------+----------------------------------------------------------------------------+
| ``public virtual bool loadSensitiveTone { get; set; }``         | Configurable load sensitive tone for Audio.                                |
+-----------------------------------------------------------------+----------------------------------------------------------------------------+
| ``public virtual Vector2 engineToneCutoff { get; set; }``       | Idle-to-loaded low-pass cutoff range, in Hz.                               |
+-----------------------------------------------------------------+----------------------------------------------------------------------------+
| ``public virtual Vector2 enginePitchRange { get; set; }``       | Configurable engine pitch range for Audio.                                 |
+-----------------------------------------------------------------+----------------------------------------------------------------------------+
| ``public virtual AudioClip brakingLoop { get; set; }``          | Configurable braking loop for Audio.                                       |
+-----------------------------------------------------------------+----------------------------------------------------------------------------+
| ``public virtual AudioClip tireSquealLoop { get; set; }``       | Configurable tire squeal loop for Audio.                                   |
+-----------------------------------------------------------------+----------------------------------------------------------------------------+
| ``public virtual float brakingVolume { get; set; }``            | Configurable braking volume for Audio.                                     |
+-----------------------------------------------------------------+----------------------------------------------------------------------------+
| ``public virtual float tireVolume { get; set; }``               | Configurable tire volume for Audio.                                        |
+-----------------------------------------------------------------+----------------------------------------------------------------------------+
| ``public virtual Vector2 cornerSquealDelay { get; set; }``      | Minimum and maximum sustained-turn delay before squeal starts, in seconds. |
+-----------------------------------------------------------------+----------------------------------------------------------------------------+
| ``public virtual float cornerSquealMinimumSpeed { get; set; }`` | Configurable corner squeal minimum speed for Audio.                        |
+-----------------------------------------------------------------+----------------------------------------------------------------------------+
| ``public virtual AudioEvent[] eventSounds { get; set; }``       | Configurable event sounds for Audio.                                       |
+-----------------------------------------------------------------+----------------------------------------------------------------------------+
| ``public virtual float EngineLoopVolume { get; }``              | Read-only/resolved engine loop volume for Audio.                           |
+-----------------------------------------------------------------+----------------------------------------------------------------------------+
| ``public virtual bool EngineLoopPlaying { get; }``              | Read-only/resolved engine loop playing for Audio.                          |
+-----------------------------------------------------------------+----------------------------------------------------------------------------+
| ``public virtual float EnginePitch { get; }``                   | Read-only/resolved engine pitch for Audio.                                 |
+-----------------------------------------------------------------+----------------------------------------------------------------------------+
| ``public virtual float EngineToneCutoff { get; }``              | Current engine low-pass filter cutoff, in Hz.                              |
+-----------------------------------------------------------------+----------------------------------------------------------------------------+
| ``public virtual float CornerSquealWait { get; }``              | Remaining wait before a sustained corner becomes audible, in seconds.      |
+-----------------------------------------------------------------+----------------------------------------------------------------------------+
| ``public virtual int PlayedEventCount { get; }``                | Read-only/resolved played event count for Audio.                           |
+-----------------------------------------------------------------+----------------------------------------------------------------------------+

.. _evs-api-audio--audioevent:

AudioEvent
----------

**Runtime/Effects/Audio/AudioEvent.cs**

Configuration/implementation type for audio event within audio cores and channels.

.. _evs-api-audio--state-and-configuration-1:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------+-----------------------------------------------------------------------------------------+
| Member                            | Meaning                                                                                 |
+===================================+=========================================================================================+
| ``public string eventId``         | Authored event id used by ``AudioEvent``. Initial value: ``EventIds.Collision``.        |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| ``public AudioClip[] clips``      | Authored clips used by ``AudioEvent``.                                                  |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| ``public float volume``           | Authored volume used by ``AudioEvent``. Initial value: ``.8f``.                         |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| ``public Vector2 pitchRange``     | Authored pitch range used by ``AudioEvent``. Initial value: ``new Vector2(.9f, 1.1f)``. |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| ``public float cooldown``         | Authored cooldown used by ``AudioEvent``. Initial value: ``.15f``.                      |
+-----------------------------------+-----------------------------------------------------------------------------------------+
| ``public float minimumIntensity`` | Authored minimum intensity used by ``AudioEvent``. Initial value: ``.05f``.             |
+-----------------------------------+-----------------------------------------------------------------------------------------+

.. _evs-api-audio--audiomodule:

AudioModule
-----------

**Runtime/Effects/Audio/Core/AudioModule.cs**

Base channel with source creation, loop update and cleanup helpers.

**Inherits / implements:** :ref:`EffectsModule <evs-api-presentation--effectsmodule>`, :ref:`IAudioModule <evs-api-audio--iaudiomodule>`.

.. _evs-api-audio--methods-1:

Methods
~~~~~~~

+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                         | Role and behavior                                                                                    | Arguments and result                                                                                                                     |
+===================================================================+======================================================================================================+==========================================================================================================================================+
| ``public abstract void RenderAudio(Audio core, float deltaTime)`` | Advances one channel's audio presentation for elapsed render time; the Audio core normally calls it. | ``core`` — Owning audio or passenger core supplying shared context. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SuspendAudio()``                            | Suspends the channel's playback and active subscriptions/resources as implemented by that channel.   | No arguments; no returned value.                                                                                                         |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-audio--boatwateraudio:

BoatWaterAudio
--------------

**Runtime/Effects/Audio/Modules/BoatWaterAudio.cs**

Configuration/implementation type for boat water audio within audio cores and channels.

**Inherits / implements:** :ref:`AudioModule <evs-api-audio--audiomodule>`.

.. _evs-api-audio--methods-2:

Methods
~~~~~~~

+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                         | Role and behavior                                                                                    | Arguments and result                                                                                                                     |
+===================================================================+======================================================================================================+==========================================================================================================================================+
| ``public override void RenderAudio(Audio core, float deltaTime)`` | Advances one channel's audio presentation for elapsed render time; the Audio core normally calls it. | ``core`` — Owning audio or passenger core supplying shared context. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void SuspendAudio()``                           | Suspends the channel's playback and active subscriptions/resources as implemented by that channel.   | No arguments; no returned value.                                                                                                         |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-audio--state-and-configuration-2:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| Member                                                              | Meaning                                                                                          |
+=====================================================================+==================================================================================================+
| ``public bool waterSoundsEnabled``                                  | Authored water sounds enabled used by ``BoatWaterAudio``. Initial value: ``true``.               |
+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public AudioClip lappingLoop``                                    | Authored lapping loop used by ``BoatWaterAudio``.                                                |
+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public AudioClip wakeLoop``                                       | Authored wake loop used by ``BoatWaterAudio``.                                                   |
+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public AudioClip[] splashClips``                                  | Authored splash clips used by ``BoatWaterAudio``.                                                |
+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public float lappingVolume``                                      | Authored lapping volume used by ``BoatWaterAudio``. Initial value: ``.22f``.                     |
+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public float wakeVolume``                                         | Authored wake volume used by ``BoatWaterAudio``. Initial value: ``.45f``.                        |
+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public float splashVolume``                                       | Authored splash volume used by ``BoatWaterAudio``. Initial value: ``.5f``.                       |
+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public float fullWakeSpeed``                                      | Authored full wake speed used by ``BoatWaterAudio``. Initial value: ``20``.                      |
+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public Vector2 hullHalfSize``                                     | Hull half-width and half-length, metres; converts real roll/pitch rates to water-contact motion. |
+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public float fullLappingMotion``                                  | Authored full lapping motion used by ``BoatWaterAudio``. Initial value: ``.12f``.                |
+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public float splashThreshold``                                    | Authored splash threshold used by ``BoatWaterAudio``. Initial value: ``.2f``.                    |
+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public float splashCooldown``                                     | Authored splash cooldown used by ``BoatWaterAudio``. Initial value: ``.8f``.                     |
+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public virtual bool WaterContact { get; protected set; }``        | Read-only/resolved water contact for ``BoatWaterAudio``.                                         |
+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public virtual float HullMotion { get; protected set; }``         | Read-only/resolved hull motion for ``BoatWaterAudio``.                                           |
+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public virtual float LappingVolume { get; }``                     | Read-only/resolved lapping volume for ``BoatWaterAudio``.                                        |
+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public virtual float WakeVolume { get; }``                        | Read-only/resolved wake volume for ``BoatWaterAudio``.                                           |
+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public virtual int PlayedSplashCount { get; protected set; }``    | Read-only/resolved played splash count for ``BoatWaterAudio``.                                   |
+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+
| ``public virtual AudioClip LastSplashClip { get; protected set; }`` | Read-only/resolved last splash clip for ``BoatWaterAudio``.                                      |
+---------------------------------------------------------------------+--------------------------------------------------------------------------------------------------+

.. _evs-api-audio--brakeaudio:

BrakeAudio
----------

**Runtime/Effects/Audio/Modules/BrakeAudio.cs**

Configuration/implementation type for brake audio within audio cores and channels.

**Inherits / implements:** :ref:`AudioModule <evs-api-audio--audiomodule>`.

.. _evs-api-audio--methods-3:

Methods
~~~~~~~

+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                         | Role and behavior                                                                                    | Arguments and result                                                                                                                     |
+===================================================================+======================================================================================================+==========================================================================================================================================+
| ``public override void RenderAudio(Audio core, float deltaTime)`` | Advances one channel's audio presentation for elapsed render time; the Audio core normally calls it. | ``core`` — Owning audio or passenger core supplying shared context. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-audio--state-and-configuration-3:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------+-------------------------------------------------------------------------------------------------+
| Member                                | Meaning                                                                                         |
+=======================================+=================================================================================================+
| ``public AudioClip brakingLoop``      | Authored braking loop used by ``BrakeAudio``.                                                   |
+---------------------------------------+-------------------------------------------------------------------------------------------------+
| ``public float brakingVolume``        | Authored braking volume used by ``BrakeAudio``. Initial value: ``.15f``.                        |
+---------------------------------------+-------------------------------------------------------------------------------------------------+
| ``public Vector2 brakeSpeedRangeKph`` | Speed range in km/h from silent to full brake-loop volume.                                      |
+---------------------------------------+-------------------------------------------------------------------------------------------------+
| ``public Vector2 brakePitchRange``    | Authored brake pitch range used by ``BrakeAudio``. Initial value: ``new Vector2(.85f, 1.05f)``. |
+---------------------------------------+-------------------------------------------------------------------------------------------------+

.. _evs-api-audio--commercialaudio:

CommercialAudio
---------------

**Runtime/Effects/Audio/CommercialAudio.cs**

Configuration/implementation type for commercial audio within audio cores and channels.

**Inherits / implements:** :ref:`EffectsModule <evs-api-presentation--effectsmodule>`.

.. _evs-api-audio--state-and-configuration-4:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+----------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| Member                                                               | Meaning                                                                              |
+======================================================================+======================================================================================+
| ``public VehicleController vehicle``                                 | Authored vehicle used by ``CommercialAudio``.                                        |
+----------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public Gearbox gearbox``                                           | Authored gearbox used by ``CommercialAudio``.                                        |
+----------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public bool airBrakesEnabled``                                     | Authored air brakes enabled used by ``CommercialAudio``. Initial value: ``true``.    |
+----------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public bool reverseAlarmEnabled``                                  | Authored reverse alarm enabled used by ``CommercialAudio``. Initial value: ``true``. |
+----------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public bool stopStartOnly``                                        | Service-brake hiss only on stopping and setting off; disable for pedal-edge sounds.  |
+----------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public float stoppedSpeedKph``                                     | Authored stopped speed kph used by ``CommercialAudio``. Initial value: ``.5f``.      |
+----------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public float movingSpeedKph``                                      | Authored moving speed kph used by ``CommercialAudio``. Initial value: ``1.5f``.      |
+----------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public bool parkingApplySound``                                    | Authored parking apply sound used by ``CommercialAudio``. Initial value: ``true``.   |
+----------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public bool parkingReleaseSound``                                  | Off for the demo Space handbrake. Enable for pneumatic parking-brake release audio.  |
+----------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public AudioClip brakeApplyClip``                                  | Authored brake apply clip used by ``CommercialAudio``.                               |
+----------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public AudioClip brakeReleaseClip``                                | Authored brake release clip used by ``CommercialAudio``.                             |
+----------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public AudioClip parkingApplyClip``                                | Authored parking apply clip used by ``CommercialAudio``.                             |
+----------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public AudioClip parkingReleaseClip``                              | Authored parking release clip used by ``CommercialAudio``.                           |
+----------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public AudioClip reverseBeepClip``                                 | One beep; cadence is controlled separately below.                                    |
+----------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public float brakeApplyVolume``                                    | Authored brake apply volume used by ``CommercialAudio``. Initial value: ``.24f``.    |
+----------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public float brakeReleaseVolume``                                  | Authored brake release volume used by ``CommercialAudio``. Initial value: ``.55f``.  |
+----------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public float parkingVolume``                                       | Authored parking volume used by ``CommercialAudio``. Initial value: ``.65f``.        |
+----------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public float reverseVolume``                                       | Authored reverse volume used by ``CommercialAudio``. Initial value: ``.45f``.        |
+----------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public float reverseInterval``                                     | Authored reverse interval used by ``CommercialAudio``. Initial value: ``.85f``.      |
+----------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public float airCooldown``                                         | Authored air cooldown used by ``CommercialAudio``. Initial value: ``.15f``.          |
+----------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public float brakeThreshold``                                      | Authored brake threshold used by ``CommercialAudio``. Initial value: ``.12f``.       |
+----------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public AudioMixerGroup output``                                    | Authored output used by ``CommercialAudio``.                                         |
+----------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public float spatialBlend``                                        | Blend from nonspatial audio at zero to fully positional audio at one.                |
+----------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public float minDistance``                                         | Distance within which positional audio retains full volume, in metres.               |
+----------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public float maxDistance``                                         | Authored max distance used by ``CommercialAudio``. Initial value: ``65``.            |
+----------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public virtual AudioClip LastAirClip { get; protected set; }``     | Read-only/resolved last air clip for ``CommercialAudio``.                            |
+----------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public virtual AudioClip LastReverseClip { get; protected set; }`` | Read-only/resolved last reverse clip for ``CommercialAudio``.                        |
+----------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public virtual int AirSoundCount { get; protected set; }``         | Read-only/resolved air sound count for ``CommercialAudio``.                          |
+----------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public virtual int ReverseBeepCount { get; protected set; }``      | Read-only/resolved reverse beep count for ``CommercialAudio``.                       |
+----------------------------------------------------------------------+--------------------------------------------------------------------------------------+
| ``public virtual bool ReverseAlarmActive { get; protected set; }``   | Read-only/resolved reverse alarm active for ``CommercialAudio``.                     |
+----------------------------------------------------------------------+--------------------------------------------------------------------------------------+

.. _evs-api-audio--damageaudio:

DamageAudio
-----------

**Runtime/Effects/Audio/Damage/DamageAudio.cs**

Separate Effects module for damage sound presentation.

**Inherits / implements:** :ref:`EffectsModule <evs-api-presentation--effectsmodule>`.

.. _evs-api-audio--state-and-configuration-5:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------+---------------------------------------------------------------------+
| Member                                              | Meaning                                                             |
+=====================================================+=====================================================================+
| ``public Damage damage``                            | Authored damage used by ``DamageAudio``.                            |
+-----------------------------------------------------+---------------------------------------------------------------------+
| ``public AudioClip[] metalClips``                   | Authored metal clips used by ``DamageAudio``.                       |
+-----------------------------------------------------+---------------------------------------------------------------------+
| ``public AudioClip[] glassClips``                   | Authored glass clips used by ``DamageAudio``.                       |
+-----------------------------------------------------+---------------------------------------------------------------------+
| ``public float volume``                             | Authored volume used by ``DamageAudio``. Initial value: ``.7f``.    |
+-----------------------------------------------------+---------------------------------------------------------------------+
| ``public float cooldown``                           | Authored cooldown used by ``DamageAudio``. Initial value: ``.12f``. |
+-----------------------------------------------------+---------------------------------------------------------------------+
| ``public UnityEngine.Audio.AudioMixerGroup output`` | Authored output used by ``DamageAudio``.                            |
+-----------------------------------------------------+---------------------------------------------------------------------+

.. _evs-api-audio--engineaudio:

EngineAudio
-----------

**Runtime/Effects/Audio/Modules/EngineAudio.cs**

Selects and modulates the engine loop and ignition transitions.

**Inherits / implements:** :ref:`AudioModule <evs-api-audio--audiomodule>`.

.. _evs-api-audio--methods-4:

Methods
~~~~~~~

+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                         | Role and behavior                                                                                    | Arguments and result                                                                                                                     |
+===================================================================+======================================================================================================+==========================================================================================================================================+
| ``public override void RenderAudio(Audio core, float deltaTime)`` | Advances one channel's audio presentation for elapsed render time; the Audio core normally calls it. | ``core`` — Owning audio or passenger core supplying shared context. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void SuspendAudio()``                           | Suspends the channel's playback and active subscriptions/resources as implemented by that channel.   | No arguments; no returned value.                                                                                                         |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-audio--state-and-configuration-6:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                                | Meaning                                                                                                                                       |
+=======================================================================+===============================================================================================================================================+
| ``public AudioClip engineStartClip``                                  | Authored engine start clip used by ``EngineAudio``.                                                                                           |
+-----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public AudioClip engineStopClip``                                   | Authored engine stop clip used by ``EngineAudio``.                                                                                            |
+-----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool playIgnitionSounds``                                    | Authored play ignition sounds used by ``EngineAudio``. Initial value: ``true``.                                                               |
+-----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float engineStartVolume``                                    | Authored engine start volume used by ``EngineAudio``. Initial value: ``.65f``.                                                                |
+-----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float engineStopVolume``                                     | Authored engine stop volume used by ``EngineAudio``. Initial value: ``.6f``.                                                                  |
+-----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual int StartSoundCount { get; protected set; }``        | Read-only/resolved start sound count for ``EngineAudio``.                                                                                     |
+-----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual int StopSoundCount { get; protected set; }``         | Read-only/resolved stop sound count for ``EngineAudio``.                                                                                      |
+-----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual AudioClip LastIgnitionClip { get; protected set; }`` | Read-only/resolved last ignition clip for ``EngineAudio``.                                                                                    |
+-----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public EngineSoundProfile soundOverride``                           | Authored sound override used by ``EngineAudio``.                                                                                              |
+-----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public AudioClip profileLoopOverride``                              | Authored profile loop override used by ``EngineAudio``.                                                                                       |
+-----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float profileVolumeMultiplier``                              | Authored profile volume multiplier used by ``EngineAudio``. Initial value: ``1``.                                                             |
+-----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool useProfileSound``                                       | Authored use profile sound used by ``EngineAudio``. Initial value: ``true``.                                                                  |
+-----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public AudioClip engineLoop``                                       | Authored engine loop used by ``EngineAudio``.                                                                                                 |
+-----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float engineLoopStartDelay``                                 | Seconds from starting ignition until the engine loop can play. Zero starts immediately. Already-running engines on scene load are unaffected. |
+-----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float engineVolume``                                         | Authored engine volume used by ``EngineAudio``. Initial value: ``.45f``.                                                                      |
+-----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float engineMixGain``                                        | Authored engine mix gain used by ``EngineAudio``. Initial value: ``1``.                                                                       |
+-----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float engineLoopReferenceRpm``                               | Authored engine loop reference rpm used by ``EngineAudio``.                                                                                   |
+-----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public float engineRpmPitchExponent``                               | Authored engine rpm pitch exponent used by ``EngineAudio``. Initial value: ``1``.                                                             |
+-----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public bool loadSensitiveTone``                                     | Authored load sensitive tone used by ``EngineAudio``.                                                                                         |
+-----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector2 engineToneCutoff``                                   | Idle-to-loaded low-pass cutoff range, in Hz.                                                                                                  |
+-----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector2 enginePitchRange``                                   | Authored engine pitch range used by ``EngineAudio``. Initial value: ``new Vector2(.65f, 1.8f)``.                                              |
+-----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float EngineLoopVolume { get; }``                    | Read-only/resolved engine loop volume for ``EngineAudio``.                                                                                    |
+-----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool EngineLoopPlaying { get; }``                    | Read-only/resolved engine loop playing for ``EngineAudio``.                                                                                   |
+-----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float EngineLoopDelayRemaining { get; }``            | Seconds remaining before the running engine loop may become audible.                                                                          |
+-----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float EnginePitch { get; }``                         | Read-only/resolved engine pitch for ``EngineAudio``.                                                                                          |
+-----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float EngineToneCutoff { get; }``                    | Current engine low-pass filter cutoff, in Hz.                                                                                                 |
+-----------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-audio--enginepitchmode:

EnginePitchMode
---------------

**Runtime/Effects/Audio/EngineSoundProfile.cs**

Defines the allowed engine pitch mode choices used by this topic.

.. _evs-api-audio--values:

Values
~~~~~~

-  ``Rpm``
-  ``Constant``
-  ``Motion``

.. _evs-api-audio--enginesoundprofile:

EngineSoundProfile
------------------

**Runtime/Effects/Audio/EngineSoundProfile.cs**

Stores engine sound behavior and asset configuration.

**Inherits / implements:** ``ScriptableObject``.

.. _evs-api-audio--methods-5:

Methods
~~~~~~~

+-------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                           | Role and behavior                                                                | Arguments and result                                                                                                                                                                                            |
+=====================================================================================+==================================================================================+=================================================================================================================================================================================================================+
| ``public virtual float EvaluateActivity(VehicleController vehicle, Engine engine)`` | Evaluates sound activity from the configured sound profile and mechanical input. | ``vehicle`` — Vehicle context/owner receiving the operation. ``engine`` — Engine whose running/RPM/gearbox state supplies the operation. **Returns:** Computed float in the operation's documented unit/domain. |
+-------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float EvaluatePitch(float activity)``                              | Evaluates audio pitch from the configured engine sound response.                 | ``activity`` — Normalized presentation activity. **Returns:** Computed float in the operation's documented unit/domain.                                                                                         |
+-------------------------------------------------------------------------------------+----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-audio--state-and-configuration-7:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| Member                                  | Meaning                                                                                                            |
+=========================================+====================================================================================================================+
| ``public AudioClip loop``               | Authored loop used by ``EngineSoundProfile``.                                                                      |
+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| ``public EnginePitchMode pitchMode``    | Authored pitch mode used by ``EngineSoundProfile``.                                                                |
+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| ``public bool useEngineResponse``       | For RPM profiles, retain ``EngineAudio``'s RPM exponent/reference, throttle level, tone filter and shift response. |
+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| ``public float volume``                 | Authored volume used by ``EngineSoundProfile``. Initial value: ``.5f``.                                            |
+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| ``public Vector2 pitchRange``           | Authored pitch range used by ``EngineSoundProfile``. Initial value: ``new Vector2(.9f, 1.1f)``.                    |
+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| ``public float forwardSpeedReference``  | Authored forward speed reference used by ``EngineSoundProfile``. Initial value: ``25``.                            |
+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------+
| ``public float verticalSpeedReference`` | Authored vertical speed reference used by ``EngineSoundProfile``. Initial value: ``6``.                            |
+-----------------------------------------+--------------------------------------------------------------------------------------------------------------------+

.. _evs-api-audio--eventaudio:

EventAudio
----------

**Runtime/Effects/Audio/Modules/EventAudio.cs**

Configuration/implementation type for event audio within audio cores and channels.

**Inherits / implements:** :ref:`AudioModule <evs-api-audio--audiomodule>`.

.. _evs-api-audio--methods-6:

Methods
~~~~~~~

+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                          | Role and behavior                                                                                    | Arguments and result                                                                                                                                            |
+====================================================================+======================================================================================================+=================================================================================================================================================================+
| ``public override void RenderAudio(Audio owner, float deltaTime)`` | Advances one channel's audio presentation for elapsed render time; the Audio core normally calls it. | ``owner`` — Unity/application owner whose identity controls this relationship or resource. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void SuspendAudio()``                            | Suspends the channel's playback and active subscriptions/resources as implemented by that channel.   | No arguments; no returned value.                                                                                                                                |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void PlayEvent(EffectEvent effect)``              | Plays the configured presentation sound for a vehicle effect event.                                  | ``effect`` — Resolved vehicle ``EffectEvent`` to present.                                                                                                       |
+--------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-audio--events-and-inspector-callbacks:

Events and Inspector callbacks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| Declaration                                                   | Trigger, payload and meaning                                                                 |
+===============================================================+==============================================================================================+
| ``public event System.Action<EffectEvent, AudioClip> Played`` | When ``EventAudio`` plays a resolved event clip. Payload: ``EffectEvent`` and ``AudioClip``. |
+---------------------------------------------------------------+----------------------------------------------------------------------------------------------+

.. _evs-api-audio--state-and-configuration-8:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------+
| Member                                                          | Meaning                                                   |
+=================================================================+===========================================================+
| ``public AudioEvent[] eventSounds``                             | Authored event sounds used by ``EventAudio``.             |
+-----------------------------------------------------------------+-----------------------------------------------------------+
| ``public virtual int PlayedEventCount { get; protected set; }`` | Read-only/resolved played event count for ``EventAudio``. |
+-----------------------------------------------------------------+-----------------------------------------------------------+

.. _evs-api-audio--iaudiomodule:

IAudioModule
------------

**Runtime/Effects/Audio/Core/AudioModule.cs**

Configuration/implementation type for iaudio module within audio cores and channels.

**Inherits / implements:** :ref:`IEffectsModule <evs-api-modules--ieffectsmodule>`.

.. _evs-api-audio--methods-7:

Methods
~~~~~~~

+---------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                         | Role and behavior                                                                                    | Arguments and result                                                                                                                     |
+===================================================+======================================================================================================+==========================================================================================================================================+
| ``void RenderAudio(Audio core, float deltaTime)`` | Advances one channel's audio presentation for elapsed render time; the Audio core normally calls it. | ``core`` — Owning audio or passenger core supplying shared context. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+---------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-audio--indicatoraudio:

IndicatorAudio
--------------

**Runtime/Effects/Audio/Modules/IndicatorAudio.cs**

Follows actual indicator output phase.

**Inherits / implements:** :ref:`AudioModule <evs-api-audio--audiomodule>`.

.. _evs-api-audio--methods-8:

Methods
~~~~~~~

+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                         | Role and behavior                                                                                    | Arguments and result                                                                                                                     |
+===================================================================+======================================================================================================+==========================================================================================================================================+
| ``public override void RenderAudio(Audio core, float deltaTime)`` | Advances one channel's audio presentation for elapsed render time; the Audio core normally calls it. | ``core`` — Owning audio or passenger core supplying shared context. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetClips(AudioClip on, AudioClip off)``     | Replaces indicator tick clips, retaining generated defaults for independently unassigned clips.      | ``on`` — On, interpreted by this operation in the declared type. ``off`` — Off, interpreted by this operation in the declared type.      |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void SuspendAudio()``                           | Suspends the channel's playback and active subscriptions/resources as implemented by that channel.   | No arguments; no returned value.                                                                                                         |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-audio--state-and-configuration-9:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------------------------+----------------------------------------------------------------------------------+
| Member                                                              | Meaning                                                                          |
+=====================================================================+==================================================================================+
| ``public Lights lights``                                            | Authored lights used by ``IndicatorAudio``.                                      |
+---------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ``public AudioClip tickOn``                                         | Optional replacement for the relay click when the lamps turn on.                 |
+---------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ``public AudioClip tickOff``                                        | Optional replacement for the relay click when the lamps turn off.                |
+---------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ``public bool useDefaultClicks``                                    | Authored use default clicks used by ``IndicatorAudio``. Initial value: ``true``. |
+---------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ``public float volume``                                             | Authored volume used by ``IndicatorAudio``. Initial value: ``.45f``.             |
+---------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ``public float spatialBlend``                                       | Blend from nonspatial audio at zero to fully positional audio at one.            |
+---------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ``public virtual int PlayedClickCount { get; protected set; }``     | Read-only/resolved played click count for ``IndicatorAudio``.                    |
+---------------------------------------------------------------------+----------------------------------------------------------------------------------+
| ``public virtual AudioClip LastPlayedClip { get; protected set; }`` | Read-only/resolved last played clip for ``IndicatorAudio``.                      |
+---------------------------------------------------------------------+----------------------------------------------------------------------------------+

.. _evs-api-audio--switchaudio:

SwitchAudio
-----------

**Runtime/Effects/Audio/Modules/SwitchAudio.cs**

Configuration/implementation type for switch audio within audio cores and channels.

**Inherits / implements:** :ref:`AudioModule <evs-api-audio--audiomodule>`.

.. _evs-api-audio--methods-9:

Methods
~~~~~~~

+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                         | Role and behavior                                                                                    | Arguments and result                                                                                                                     |
+===================================================================+======================================================================================================+==========================================================================================================================================+
| ``public override void RenderAudio(Audio core, float deltaTime)`` | Advances one channel's audio presentation for elapsed render time; the Audio core normally calls it. | ``core`` — Owning audio or passenger core supplying shared context. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+-------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-audio--state-and-configuration-10:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-----------------------------------------------------------------+-----------------------------------------------------------------------+
| Member                                                          | Meaning                                                               |
+=================================================================+=======================================================================+
| ``public SwitchHandle switchHandle``                            | Authored switch handle used by ``SwitchAudio``.                       |
+-----------------------------------------------------------------+-----------------------------------------------------------------------+
| ``public AudioClip click``                                      | Authored click used by ``SwitchAudio``.                               |
+-----------------------------------------------------------------+-----------------------------------------------------------------------+
| ``public float volume``                                         | Authored volume used by ``SwitchAudio``. Initial value: ``.45f``.     |
+-----------------------------------------------------------------+-----------------------------------------------------------------------+
| ``public float spatialBlend``                                   | Blend from nonspatial audio at zero to fully positional audio at one. |
+-----------------------------------------------------------------+-----------------------------------------------------------------------+
| ``public virtual int PlayedClickCount { get; protected set; }`` | Read-only/resolved played click count for ``SwitchAudio``.            |
+-----------------------------------------------------------------+-----------------------------------------------------------------------+

.. _evs-api-audio--tireaudio:

TireAudio
---------

**Runtime/Effects/Audio/Modules/TireAudio.cs**

Consumes per-wheel contact/effect-surface state.

**Inherits / implements:** :ref:`AudioModule <evs-api-audio--audiomodule>`.

.. _evs-api-audio--methods-10:

Methods
~~~~~~~

+------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                      | Role and behavior                                                                                    | Arguments and result                                                                                                                                                                                                                                   |
+================================================================================================+======================================================================================================+========================================================================================================================================================================================================================================================+
| ``public override void RenderAudio(Audio core, float deltaTime)``                              | Advances one channel's audio presentation for elapsed render time; the Audio core normally calls it. | ``core`` — Owning audio or passenger core supplying shared context. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop.                                                                                                               |
+------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float FilterCornerSqueal(float skid, bool highSpeedCorner, float deltaTime)`` | Filters or evaluates corner squeal using the tire-audio policy without changing tire physics.        | ``skid`` — Resolved skid activity. ``highSpeedCorner`` — Corner-squeal input used by tire-audio filtering. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. **Returns:** Computed float in the operation's documented unit/domain. |
+------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void SuspendAudio()``                                                        | Suspends the channel's playback and active subscriptions/resources as implemented by that channel.   | No arguments; no returned value.                                                                                                                                                                                                                       |
+------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-audio--state-and-configuration-11:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| Member                                                            | Meaning                                                                                     |
+===================================================================+=============================================================================================+
| ``public AudioClip tireSquealLoop``                               | Authored tire squeal loop used by ``TireAudio``.                                            |
+-------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| ``public float tireVolume``                                       | Authored tire volume used by ``TireAudio``. Initial value: ``.5f``.                         |
+-------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| ``public bool delayCornerSqueal``                                 | Delay squeal during sustained high-speed corners. Disable for immediate slip feedback.      |
+-------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| ``public float cornerSteeringThreshold``                          | Authored corner steering threshold used by ``TireAudio``. Initial value: ``.75f``.          |
+-------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| ``public Vector2 tirePitchRange``                                 | Authored tire pitch range used by ``TireAudio``. Initial value: ``new Vector2(.9f, 1.1f)``. |
+-------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| ``public Vector2 cornerSquealDelay``                              | Minimum and maximum sustained-turn delay before squeal starts, in seconds.                  |
+-------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| ``public float cornerSquealMinimumSpeed``                         | Authored corner squeal minimum speed used by ``TireAudio``. Initial value: ``50``.          |
+-------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| ``public virtual float CornerSquealWait { get; protected set; }`` | Remaining wait before a sustained corner becomes audible, in seconds.                       |
+-------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
