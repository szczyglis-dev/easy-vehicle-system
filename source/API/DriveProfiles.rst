.. _evs-api-driveprofiles--movement-strategies-and-transitions-api:

Movement strategies and transitions API
=======================================

Read :doc:`the system explanation </Scripting/DriveProfiles>` for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from ``MonoBehaviour``, ``Object`` or ``ScriptableObject`` are documented by Unity.

.. _evs-api-driveprofiles--types:

Types
-----

-  :ref:`AirProfile <evs-api-driveprofiles--airprofile>`
-  :ref:`Drive <evs-api-driveprofiles--drive>`
-  :ref:`DriveCore <evs-api-driveprofiles--drivecore>`
-  :ref:`DriveProfileSlot <evs-api-driveprofiles--driveprofileslot>`
-  :ref:`DriveDefaults <evs-api-driveprofiles--drivedefaults>`
-  :ref:`DriveModule <evs-api-driveprofiles--drivemodule>`
-  :ref:`DriveProfile <evs-api-driveprofiles--driveprofile>`
-  :ref:`FreeProfile <evs-api-driveprofiles--freeprofile>`
-  :ref:`HoverDriveTransition <evs-api-driveprofiles--hoverdrivetransition>`
-  :ref:`HoverProfile <evs-api-driveprofiles--hoverprofile>`
-  :ref:`MotorcycleProfile <evs-api-driveprofiles--motorcycleprofile>`
-  :ref:`ProfileSwitcher <evs-api-driveprofiles--profileswitcher>`
-  :ref:`ProfileTransition <evs-api-driveprofiles--profiletransition>`
-  :ref:`WheeledProfile <evs-api-driveprofiles--wheeledprofile>`

.. _evs-api-driveprofiles--airprofile:

AirProfile
----------

**Runtime/Drive/Profiles/AirProfile.cs**

Configuration/implementation type for air profile within movement strategies and transitions.

**Inherits / implements:** :ref:`FreeProfile <evs-api-driveprofiles--freeprofile>`.

.. _evs-api-driveprofiles--state-and-configuration:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------+-----------------------------------------------------+
| Member                                     | Meaning                                             |
+============================================+=====================================================+
| ``public override string Medium { get; }`` | Movement-family label used by the profile contract. |
+--------------------------------------------+-----------------------------------------------------+

.. _evs-api-driveprofiles--drive:

Drive
-----

**Runtime/Drive/Drive.cs**

Retains the vehicle's boat motion and sampling history.

**Inherits / implements:** :ref:`DriveModule <evs-api-driveprofiles--drivemodule>`.

.. _evs-api-driveprofiles--methods:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                  | Role and behavior                                                                               | Arguments and result                                                                                                                                                                                                     |
+============================================================================================+=================================================================================================+==========================================================================================================================================================================================================================+
| ``public override void Configure(VehicleController vehicle)``                              | Rebinds teleport reset, clears hold/boat/hover history and configures the current profile.      | ``vehicle`` — Vehicle context/owner receiving the operation.                                                                                                                                                             |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Clears inapplicable hold state, then invokes the active ``DriveProfile.Step`` for this vehicle. | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-driveprofiles--state-and-configuration-1:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------------+---------------------------------------------------------------+
| Member                                            | Meaning                                                       |
+===================================================+===============================================================+
| ``public override int ExecutionOrder { get; }``   | Default local priority within phase/category.                 |
+---------------------------------------------------+---------------------------------------------------------------+
| ``public override ExecutionPhase Phase { get; }`` | Cross-category execution barrier used by the module pipeline. |
+---------------------------------------------------+---------------------------------------------------------------+

.. _evs-api-driveprofiles--drivecore:

DriveCore
---------

**Runtime/Drive/Core/DriveCore.cs**

Configuration/implementation type for drive core within movement strategies and transitions.

**Inherits / implements:** :ref:`CategoryCore <evs-api-modules--categorycore>`.

.. _evs-api-driveprofiles--methods-1:

Methods
~~~~~~~

+------------------------+-----------------------------------------------------------+--------------------------------------------------------------------+
| Signature              | Role and behavior                                         | Arguments and result                                               |
+========================+===========================================================+====================================================================+
| ``public DriveCore()`` | Constructs ``DriveCore`` with the supplied initial state. | **Returns:** New instance initialized from the supplied arguments. |
+------------------------+-----------------------------------------------------------+--------------------------------------------------------------------+

.. _evs-api-driveprofiles--state-and-configuration-2:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------------------+--------------------------------------------------------------------------------------+
| Member                                               | Meaning                                                                              |
+======================================================+======================================================================================+
| ``public override ModuleCategory Category { get; }`` | Module responsibility category; it does not independently determine execution phase. |
+------------------------------------------------------+--------------------------------------------------------------------------------------+

.. _evs-api-driveprofiles--drivedefaults:

DriveDefaults
-------------

**Runtime/Drive/DriveDefaults.cs**

Builds initial settings for supported movement families.

.. _evs-api-driveprofiles--methods-2:

Methods
~~~~~~~

+-----------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                       | Role and behavior                                                                                     | Arguments and result                                                                                                                                                           |
+=================================================================+=======================================================================================================+================================================================================================================================================================================+
| ``public static DriveProfile Create(System.Type type)``         | Creates a concrete built-in or custom DriveProfile type through its public parameterless constructor. | ``type`` — Type, interpreted by this operation in the declared type. **Returns:** Returned ``DriveProfile``; ownership remains as specified by the creating/lookup operation.  |
+-----------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public static Settings CreateSettings(DriveProfile profile)`` | Returns a fresh initial shared settings object for explicit creation/profile selection.               | ``profile`` — Movement/surface configuration, according to its declared type. **Returns:** Returned Settings; ownership remains as specified by the creating/lookup operation. |
+-----------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-driveprofiles--drivemodule:

DriveModule
-----------

**Runtime/Drive/Core/DriveModule.cs**

Configuration/implementation type for drive module within movement strategies and transitions.

**Inherits / implements:** :ref:`Module <evs-api-modules--module>`, :ref:`IDriveModule <evs-api-modules--idrivemodule>`.

.. _evs-api-driveprofiles--state-and-configuration-3:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------------------+--------------------------------------------------------------------------------------+
| Member                                                      | Meaning                                                                              |
+=============================================================+======================================================================================+
| ``public sealed override ModuleCategory Category { get; }`` | Module responsibility category; it does not independently determine execution phase. |
+-------------------------------------------------------------+--------------------------------------------------------------------------------------+

.. _evs-api-driveprofiles--driveprofile:

DriveProfile
------------

**Runtime/Drive/DriveProfile.cs**

Defines settings creation, configuration, stepping and drive-demand resolution.

.. _evs-api-driveprofiles--methods-3:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                  | Role and behavior                                                                                                 | Arguments and result                                                                                                                                                                                                       |
+============================================================================================+===================================================================================================================+============================================================================================================================================================================================================================+
| ``public virtual Settings CreateSettings()``                                               | Returns a fresh initial shared settings object for explicit creation/profile selection.                           | **Returns:** Returned Settings; ownership remains as specified by the creating/lookup operation.                                                                                                                           |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Configure(VehicleController vehicle)``                               | Empty base strategy setup hook; family implementations may ensure helpers and apply profile-owned settings.       | ``vehicle`` — Vehicle context/owner receiving the operation.                                                                                                                                                               |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public abstract void Step(VehicleController vehicle, Command command, float deltaTime)`` | Abstract movement-strategy step called by Drive; apply the selected family's movement using this vehicle context. | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop.   |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual DriveProfile Clone()``                                                    | Creates an independent serialized profile-configuration copy; configure it on its destination vehicle before use. | **Returns:** Returned ``DriveProfile``; ownership remains as specified by the creating/lookup operation.                                                                                                                   |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float ResolveDriveDemand(VehicleController vehicle, Command command)``    | Maps the command and strategy state to propulsion demand for surrounding mechanics.                               | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. **Returns:** Computed float in the operation's documented unit/domain. |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float ResolveExternalDriveIntent(VehicleController vehicle)``             | Returns signed non-wheel propulsion intent used by shared coasting/contact policy.                                | ``vehicle`` — Vehicle context/owner receiving the operation. **Returns:** Computed float in the operation's documented unit/domain.                                                                                        |
+--------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-driveprofiles--state-and-configuration-4:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+-------------------------------------------------+-----------------------------------------------------------------------------+
| Member                                          | Meaning                                                                     |
+=================================================+=============================================================================+
| ``public EngineSoundProfile engineSound``       | Authored engine sound used by ``DriveProfile``.                             |
+-------------------------------------------------+-----------------------------------------------------------------------------+
| ``public virtual string Medium { get; }``       | Movement-family label used by the profile contract.                         |
+-------------------------------------------------+-----------------------------------------------------------------------------+
| ``public virtual bool RequiresWheels { get; }`` | Whether this profile requires valid wheel definitions during configuration. |
+-------------------------------------------------+-----------------------------------------------------------------------------+

.. _evs-api-driveprofiles--freeprofile:

FreeProfile
-----------

**Runtime/Drive/Profiles/FreeProfile.cs**

Configuration/implementation type for free profile within movement strategies and transitions.

**Inherits / implements:** :ref:`DriveProfile <evs-api-driveprofiles--driveprofile>`.

.. _evs-api-driveprofiles--methods-4:

Methods
~~~~~~~

+------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                | Role and behavior                                                                   | Arguments and result                                                                                                                                                                                                       |
+==========================================================================================+=====================================================================================+============================================================================================================================================================================================================================+
| ``public override float ResolveDriveDemand(VehicleController vehicle, Command command)`` | Maps the command and strategy state to propulsion demand for surrounding mechanics. | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. **Returns:** Computed float in the operation's documented unit/domain. |
+------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-driveprofiles--state-and-configuration-5:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+--------------------------------------------------+-----------------------------------------------------------------------------+
| Member                                           | Meaning                                                                     |
+==================================================+=============================================================================+
| ``public override bool RequiresWheels { get; }`` | Whether this profile requires valid wheel definitions during configuration. |
+--------------------------------------------------+-----------------------------------------------------------------------------+
| ``public float acceleration``                    | Authored acceleration used by ``FreeProfile``. Initial value: ``12``.       |
+--------------------------------------------------+-----------------------------------------------------------------------------+
| ``public float drag``                            | Authored drag used by ``FreeProfile``. Initial value: ``.4f``.              |
+--------------------------------------------------+-----------------------------------------------------------------------------+
| ``public float angularDamping``                  | Authored angular damping used by ``FreeProfile``. Initial value: ``3``.     |
+--------------------------------------------------+-----------------------------------------------------------------------------+

.. _evs-api-driveprofiles--hoverdrivetransition:

HoverDriveTransition
--------------------

**Runtime/Drive/Profiles/HoverDriveTransition.cs**

Configuration/implementation type for hover drive transition within movement strategies and transitions.

**Inherits / implements:** :ref:`ProfileTransition <evs-api-driveprofiles--profiletransition>`.

.. _evs-api-driveprofiles--methods-5:

Methods
~~~~~~~

+----------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                                      | Role and behavior                                                                                            | Arguments and result                                                                                                                                                                                                                                        |
+================================================================================================================+==============================================================================================================+=============================================================================================================================================================================================================================================================+
| ``public override void Begin(VehicleController vehicle, DriveProfile previous, DriveProfile target)``          | Starts the owning operation or adapter; its parameters identify the request, seat or transition being owned. | ``vehicle`` — Vehicle context/owner receiving the operation. ``previous`` — Prior buffer segment/state. ``target`` — Configured target object/point; see declared type and owner.                                                                           |
+----------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, float progress, float remainingTime, float deltaTime)`` | Applies configured landing-clearance support while returning from hover to wheel drive.                      | ``vehicle`` — Vehicle context/owner receiving the operation. ``progress`` — Normalized transition progress in 0–1. ``remainingTime`` — Estimated transition time remaining in seconds. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+----------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Complete(VehicleController vehicle)``                                                   | Completes hover/wheel transition geometry and its inherited transition cleanup.                              | ``vehicle`` — Vehicle context/owner receiving the operation.                                                                                                                                                                                                |
+----------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Progress(VehicleController vehicle, float progress)``                                   | Returns normalized progress for the active profile transition.                                               | ``vehicle`` — Vehicle context/owner receiving the operation. ``progress`` — Normalized transition progress in 0–1.                                                                                                                                          |
+----------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-driveprofiles--state-and-configuration-6:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| Member                                   | Meaning                                                                                                       |
+==========================================+===============================================================================================================+
| ``public float landingClearance``        | Extra clearance above fully extended tires while unfolding near the ground. Zero disables landing assistance. |
+------------------------------------------+---------------------------------------------------------------------------------------------------------------+
| ``public float landingLiftAcceleration`` | Maximum upward correction acceleration during low hover-to-drive deployment, in m/s².                         |
+------------------------------------------+---------------------------------------------------------------------------------------------------------------+

.. _evs-api-driveprofiles--hoverprofile:

HoverProfile
------------

**Runtime/Drive/Profiles/HoverProfile.cs**

Configuration/implementation type for hover profile within movement strategies and transitions.

**Inherits / implements:** :ref:`AirProfile <evs-api-driveprofiles--airprofile>`.

.. _evs-api-driveprofiles--methods-6:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                  | Role and behavior                                                                     | Arguments and result                                                                                                                                                                                                     |
+============================================================================================+=======================================================================================+==========================================================================================================================================================================================================================+
| ``public HoverProfile()``                                                                  | Constructs ``HoverProfile`` with the supplied initial state.                          | **Returns:** New instance initialized from the supplied arguments.                                                                                                                                                       |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Configure(VehicleController vehicle)``                              | Ensures a ``HoverVisuals`` helper exists for the hover family.                        | ``vehicle`` — Vehicle context/owner receiving the operation.                                                                                                                                                             |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Applies powered vertical support, horizontal drive, attitude response and resistance. | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-driveprofiles--state-and-configuration-7:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| Member                                      | Meaning                                                                                                              |
+=============================================+======================================================================================================================+
| ``public float bodyTiltDegrees``            | Maximum combined hull lean toward forward/sideways thrust and steering, in degrees.                                  |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| ``public float bodyTiltResponse``           | Hull lean response per second, including return to level.                                                            |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| ``public float height``                     | Authored height used by ``HoverProfile``. Initial value: ``2.5f``.                                                   |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| ``public float spring``                     | Authored spring used by ``HoverProfile``. Initial value: ``12f``.                                                    |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| ``public float damping``                    | Authored damping used by ``HoverProfile``. Initial value: ``6f``.                                                    |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| ``public float verticalDamping``            | Authored vertical damping used by ``HoverProfile``. Initial value: ``2f``.                                           |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| ``public LayerMask groundMask``             | Authored ground mask used by ``HoverProfile``. Initial value: ``-1``.                                                |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| ``public float wheelSteeringTilt``          | Authored wheel steering tilt used by ``HoverProfile``. Initial value: ``12f``.                                       |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| ``public float wheelThrustTilt``            | Authored wheel thrust tilt used by ``HoverProfile``. Initial value: ``10f``.                                         |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| ``public float wheelTiltResponse``          | Visual wheel tilt response per second. Lower values make acceleration, braking and steering tilt settle more slowly. |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| ``public bool compensateGravity``           | Authored compensate gravity used by ``HoverProfile``. Initial value: ``true``.                                       |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| ``public bool automaticLeveling``           | Authored automatic leveling used by ``HoverProfile``. Initial value: ``true``.                                       |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| ``public bool surfaceSupport``              | Authored surface support used by ``HoverProfile``. Initial value: ``true``.                                          |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| ``public float attitudeStrength``           | Authored attitude strength used by ``HoverProfile``. Initial value: ``12``.                                          |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| ``public float yawAcceleration``            | Authored yaw acceleration used by ``HoverProfile``. Initial value: ``4``.                                            |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| ``public float yawDamping``                 | Authored yaw damping used by ``HoverProfile``. Initial value: ``2``.                                                 |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| ``public float maximumDescentAcceleration`` | Authored maximum descent acceleration used by ``HoverProfile``. Initial value: ``15``.                               |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
| ``public float maximumAscentAcceleration``  | Authored maximum ascent acceleration used by ``HoverProfile``. Initial value: ``25``.                                |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------+

.. _evs-api-driveprofiles--motorcycleprofile:

MotorcycleProfile
-----------------

**Runtime/Drive/Profiles/MotorcycleProfile.cs**

Configuration/implementation type for motorcycle profile within movement strategies and transitions.

**Inherits / implements:** :ref:`DriveProfile <evs-api-driveprofiles--driveprofile>`.

.. _evs-api-driveprofiles--methods-7:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                  | Role and behavior                                                                                                   | Arguments and result                                                                                                                                                                                                     |
+============================================================================================+=====================================================================================================================+==========================================================================================================================================================================================================================+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Provides fallback family balance only when enabled and no dedicated ``MotorcycleBalance`` owns that responsibility. | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-driveprofiles--state-and-configuration-8:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------+-----------------------------------------------------------------------------------------------+
| Member                                      | Meaning                                                                                       |
+=============================================+===============================================================================================+
| ``public bool automaticBalance``            | Enable fallback balance when no Motorcycle Balance module is installed.                       |
+---------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``public float wheelbase``                  | Authored wheelbase used by ``MotorcycleProfile``. Initial value: ``1.45f``.                   |
+---------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``public float maximumLean``                | Authored maximum lean used by ``MotorcycleProfile``. Initial value: ``28f``.                  |
+---------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``public float balanceStrength``            | Authored balance strength used by ``MotorcycleProfile``. Initial value: ``80f``.              |
+---------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``public float balanceDamping``             | Authored balance damping used by ``MotorcycleProfile``. Initial value: ``14f``.               |
+---------------------------------------------+-----------------------------------------------------------------------------------------------+
| ``public float maximumAngularAcceleration`` | Authored maximum angular acceleration used by ``MotorcycleProfile``. Initial value: ``100f``. |
+---------------------------------------------+-----------------------------------------------------------------------------------------------+

.. _evs-api-driveprofiles--profileswitcher:

ProfileSwitcher
---------------

**Runtime/Drive/ProfileSwitcher.cs**

Owns an ordered list of registered drive strategies and selects optional pair-specific transitions. Inherits ControllerModule.

+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Member                                                                                     | Meaning                                                                                                                                                                                                                   |
+============================================================================================+===========================================================================================================================================================================================================================+
| ``public override void Configure(VehicleController vehicle)``                              | Binds the owner and reconnects its current profile to the saved active ID. Does not recreate removed registrations.                                                                                                       |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Consumes ToggleProfile, advances the selected route and restores target contacts at completion.                                                                                                                           |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual DriveProfile GetProfile(string id)``                                      | Finds a registered profile by case-sensitive ID, or returns null.                                                                                                                                                         |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool RegisterProfile(string id, DriveProfile profile)``                   | Appends a non-null profile with a unique nonblank ID and unique instance. Rejects changes during switching or transition.                                                                                                 |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool UnregisterProfile(string id)``                                       | Removes a slot. Removing the active registration leaves the vehicle strategy running and clears ActiveProfileId; no automatic switch occurs.                                                                              |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SetProfiles(IEnumerable<DriveProfileSlot> slots)``                   | Atomically replaces/reorders the list after validation. Duplicate IDs, shared instances, null entries and blank IDs reject the entire replacement. Preserves the active ID only when its current instance is included.    |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool ClearProfiles()``                                                    | Clears all registrations without replacing the current vehicle strategy. Rejected during switching/transition.                                                                                                            |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SwitchTo(string id)``                                                | Requests a registered profile by ID. Rejects disabled/unconfigured switchers, overlapping changes, invalid wheel requirements and ambiguous/rejected routes. A pair without a matching enabled route changes immediately. |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SwitchTo(DriveProfile target)``                                      | Selects an already registered instance; does not implicitly register it.                                                                                                                                                  |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Toggle()``                                                           | Requests the next profile in list order. Suitable for UnityEvent bindings.                                                                                                                                                |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool SwitchToNext()``                                                     | Requests the next list entry and wraps at the end. With no registered active ID, requests the first entry. Empty lists and requests for the same current instance return false.                                           |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<DriveProfile> ProfileChanged``                                       | After an accepted change has configured the target. Payload: target strategy. For animated routes, this precedes transition completion.                                                                                   |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action ProfilesChanged``                                                    | After successful registration, removal or list replacement. Does not imply a strategy change.                                                                                                                             |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action TransitionStarted``                                                  | After target configuration and matching route initialization. Not emitted for immediate changes.                                                                                                                          |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action<float> TransitionProgressed``                                        | During animation, with normalized progress.                                                                                                                                                                               |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action TransitionCompleted``                                                | After animation, target contacts and final presentation are restored.                                                                                                                                                     |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public event Action TransitionInterrupted``                                              | On disable during a transition, after finalizing the selected target and presentation.                                                                                                                                    |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public ProfileTransition[] transitions``                                                 | Enabled route components to consider. Exactly one matching route is allowed per pair; no matching route means immediate switching.                                                                                        |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public IReadOnlyList<DriveProfileSlot> Profiles { get; }``                               | Registrations in Toggle order. Use registration methods to mutate the list at runtime.                                                                                                                                    |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public string ActiveProfileId { get; }``                                                 | Registered ID represented by VehicleController.driveProfile, or an empty string if unregistered. Serialized for correct reload even with several profiles of the same class.                                              |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool IsTransitioning { get; protected set; }``                            | Whether a coordinated change is in progress.                                                                                                                                                                              |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual ProfileTransition ActiveTransition { get; protected set; }``              | Selected route during animation; null when idle.                                                                                                                                                                          |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float Progress { get; }``                                                 | Animation progress in 0–1; 1 when idle. Duration is captured from the route when the change starts.                                                                                                                       |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent started``                                                              | Inspector callback when an animated route starts.                                                                                                                                                                         |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent<float> progressed``                                                    | Inspector callback with normalized animation progress.                                                                                                                                                                    |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public UnityEvent completed``                                                            | Inspector callback after animated route completion.                                                                                                                                                                       |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-driveprofiles--profiletransition:

ProfileTransition
-----------------

**Runtime/Drive/ProfileTransition.cs**

A route component for one source/destination ID pair, optionally bidirectional. Inherits MonoBehaviour.

+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| Member                                                                                                        | Meaning                                                                                                             |
+===============================================================================================================+=====================================================================================================================+
| ``public string fromProfileId``                                                                               | Source registration ID in the owning switcher.                                                                      |
+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public string toProfileId``                                                                                 | Destination registration ID in the owning switcher.                                                                 |
+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public bool bidirectional``                                                                                 | Also match toProfileId → fromProfileId; default false.                                                              |
+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public float duration``                                                                                     | Animation duration in seconds; minimum .01 when starting.                                                           |
+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public AudioClip forwardClip``                                                                              | Optional sound for fromProfileId → toProfileId.                                                                     |
+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public AudioClip reverseClip``                                                                              | Optional sound for the reverse direction of a bidirectional route.                                                  |
+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public float volume``                                                                                       | Transition sound volume, 0–1.                                                                                       |
+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public float takeoffVelocity``                                                                              | Upward velocity change in m/s when leaving a wheel-required strategy; zero disables it.                             |
+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool Matches(string fromId, string toId)``                                                   | Matches the configured pair of registration IDs and optional reverse direction.                                     |
+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public virtual AudioClip GetClip(string fromId, string toId)``                                              | Returns the forward or reverse sound for the selected direction. Called after route matching.                       |
+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool CanBegin(VehicleController vehicle, DriveProfile from, DriveProfile to)``               | Checks admission before any target configuration; receives the actual source and destination strategies.            |
+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Begin(VehicleController vehicle, DriveProfile from, DriveProfile to)``                  | Initializes presentation after the target is configured. Base implementation optionally supplies a takeoff impulse. |
+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Step(VehicleController vehicle, float progress, float remainingTime, float deltaTime)`` | Physics-only assistance per fixed step, using progress and remaining time; base implementation is empty.            |
+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Progress(VehicleController vehicle, float progress)``                                   | Applies presentation for the supplied normalized progress; base implementation is empty.                            |
+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Complete(VehicleController vehicle)``                                                   | Finalizes presentation after target contacts are restored; also called when disabling an active switcher.           |
+---------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------+

.. _evs-api-driveprofiles--wheeledprofile:

WheeledProfile
--------------

**Runtime/Drive/Profiles/WheeledProfile.cs**

Reusable wheeled strategy used by the inheritance example.

**Inherits / implements:** :ref:`DriveProfile <evs-api-driveprofiles--driveprofile>`.

.. _evs-api-driveprofiles--methods-8:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                  | Role and behavior                                                                                                         | Arguments and result                                                                                                                                                                                                     |
+============================================================================================+===========================================================================================================================+==========================================================================================================================================================================================================================+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Empty family step: ordinary wheel propulsion, steering, braking and support are already owned by the surrounding modules. | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop. |
+--------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-driveprofiles--driveprofileslot:

DriveProfileSlot
----------------

**Runtime/Drive/ProfileSwitcher.cs**

Serializable registration descriptor. Each slot stores an independent strategy configuration.

+--------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| Member                                                       | Meaning                                                                                                                        |
+==============================================================+================================================================================================================================+
| ``public string Id { get; }``                                | Stable, case-sensitive registration ID. Edit the serialized ID when authoring the list.                                        |
+--------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public DriveProfile Profile { get; internal set; }``       | Per-slot managed-reference configuration. The switcher rebinds the serialized active slot to the controller's current profile. |
+--------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
| ``public DriveProfileSlot(string id, DriveProfile profile)`` | Creates a descriptor for registering or replacing a list; does not switch the vehicle.                                         |
+--------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
