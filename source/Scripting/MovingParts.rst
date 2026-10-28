.. _evs-scripting-movingparts--anchored-moving-parts:

Anchored moving parts
=====================

``MovingPart`` is a reusable motion actuator for a visible vehicle part. It can rotate, slide, follow a target or move under rate input around an authored neutral pose. Gameplay provides requests; the component owns constrained motion and pose application.

Use it for an independently controlled mechanism such as a turret base, sliding platform or adjustable exterior part. Keep the higher-level rule — who may operate it, what it aims at and whether an action is allowed — in the application or a dedicated mechanic.

.. _evs-scripting-movingparts--implementation-map:

Implementation map
------------------

+--------------------+--------------------------------------------------------------------------+
| Class              | Responsibility                                                           |
+====================+==========================================================================+
| ``MovingPart``     | Owns rotation/translation requests, constraints and scheduled motion.    |
+--------------------+--------------------------------------------------------------------------+
| ``ExteriorModule`` | Base integration with the vehicle module lifecycle.                      |
+--------------------+--------------------------------------------------------------------------+
| ``DamagePart``     | Defines released-part ownership that can stop vehicle-controlled motion. |
+--------------------+--------------------------------------------------------------------------+

``MovingPart`` is an Exterior module configured on an owned child or with an explicit part transform. It captures a neutral pose once; ``CaptureNeutralPose`` deliberately replaces that baseline and clears requests.

.. _evs-scripting-movingparts--rotation-and-translation:

Rotation and translation
------------------------

The neutral pose is the coordinate origin for a mechanism, not necessarily its closed or minimum position. A target is measured relative to that baseline. ``CaptureNeutralPose`` intentionally replaces the baseline, so call it while the model is at its authored neutral pose rather than at an arbitrary animated point.

A rotational mechanism can run from rate input, a target angle or world-target tracking. A translation uses a bounded metre offset and an explicit frame. Changing control mode changes the active request; use ``Stop()`` to clear retained rate/target/tracking ownership before another application system takes over the same part.

A custom actuator can reuse ``GetRotationFrame``, ``GetTranslationFrame``, ``ClampAngle`` and ``ClampPosition`` to remain consistent with configured limits. Do not implement a separate axis convention for a UI slider: map that slider to the existing normalized/target operation so the component remains the authority for geometry.

Choose the frame before tuning the limits. A translation in world space behaves differently from one along the vehicle's local axis when the vehicle turns. An anchor frame is useful when the mechanism belongs to a separate stable mounting point. Keep that anchor independent of the moving part to avoid measuring motion from a frame the actuator itself changes.

Rate and target requests also have different meanings. Rate input says “keep moving in this direction”; a target says “move to this bounded offset.” A hold button should release its rate request when input ownership ends. A workshop preset should request a target instead of simulating a held button until a guessed time elapses.

Rotation uses the local axis/forward, optional hinge anchor, signed angle limits and angular speed. Rate input supports full turns; target angles can use shortest-arc policy. ``AimAt`` follows a world point or transform around the allowed axis.

Translation uses metres from neutral in Part, Parent, World or Anchor space. Direction angles rotate the axis inside that frame. Parent motion is followed, and scale compensation preserves configured world travel. Invalid self/descendant anchors fall back to the neutral part frame.

.. _evs-scripting-movingparts--hold-button-slider:

Hold-button slider
------------------

The adapter stores both button states so releasing one button does not erase the other. It calculates a single signed rate request and stops on disable. This cleanup is important for touch controls and possession handovers, where the normal release event may never reach an object being disabled.

The example does not know the slider's axis, distance or speed. Those remain on ``MovingPart``, so the same input adapter can operate a differently authored mechanism without changing its code.

``Configure`` translation geometry in the Inspector, then connect press/release callbacks to this component. Both buttons held result in zero. No keyboard convention is built into the moving part.

**Example: ``SliderButtons.cs``**

.. raw:: html

   <!-- example: SliderButtons.cs -->

.. code-block:: csharp

   using UnityEngine;
   using EasyVehicleSystem;

   namespace VehicleDocumentationExamples
   {
       public class SliderButtons : MonoBehaviour
       {
           public MovingPart slider;
           private bool forward, backward;

           public void SetForward(bool pressed) { forward = pressed; Apply(); }
           public void SetBackward(bool pressed) { backward = pressed; Apply(); }
           private void Apply()
           {
               if (slider) slider.SetInput((forward ? 1 : 0) - (backward ? 1 : 0));
           }
           private void OnDisable()
           {
               forward = backward = false;
               if (slider) slider.Stop();
           }
       }
   }

``SetTargetPosition`` moves toward a bounded metre offset; ``SetPosition`` applies it immediately; ``SetNormalizedPosition`` maps the travel interval. ``ReturnToNeutral`` requests zero within limits. ``SetInput``\ (0) pauses; ``Stop`` clears rate/target/tracking.

Disabling clears commands at the current pose. A detached ``DamagePart`` ancestor cancels motion so physics owns debris. Controller scheduling normally advances the module; only use ``Tick`` for a loop you explicitly own.

.. _evs-scripting-movingparts--complete-public-method-and-event-index:

Complete public method and event index
--------------------------------------

The lists below cover public methods and events for this topic and their package base contracts. Signatures include overloads. See :doc:`the detailed general moving parts API </API/MovingParts>` for arguments, return semantics, state and configuration. An override replaces the matching inherited implementation; it is not an additional call to make.

.. _evs-scripting-movingparts--imodule:

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

.. _evs-scripting-movingparts--module:

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

.. _evs-scripting-movingparts--movingpart:

MovingPart
~~~~~~~~~~

:ref:`MovingPart <evs-api-movingparts--movingpart>` gives the full declared contract.

+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| Method                                                                                                | Role                                                                                                                                |
+=======================================================================================================+=====================================================================================================================================+
| ``public override void Configure(VehicleController vehicle)``                                         | Ensures its neutral pose is captured without recapturing every configuration.                                                       |
+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)``            | Advances ``Tick`` using the controller's timestep; no second caller is needed while registered.                                     |
+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Tick(float deltaTime)``                                                         | Advances the declaring presentation/state machine by elapsed seconds; avoid a second call when its built-in owner already ticks it. |
+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float ClampAngle(float angle)``                                                      | Returns the requested angle restricted by the moving part's configured angular policy.                                              |
+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetMotionEnabled(bool value)``                                                  | Changes moving-part actuation availability and its notification state.                                                              |
+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetInput(float input)``                                                         | Takes signed rate-input ownership for the configured rotation/translation mode; zero pauses rate travel.                            |
+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetTargetAngle(float angle, bool shortestPath = true)``                         | Requests smooth motion toward a bounded angle, optionally using shortest-arc policy.                                                |
+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetAngle(float angle)``                                                         | Immediately applies a moving-part/geometry rotation in degrees.                                                                     |
+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void AimAt(Vector3 worldPoint)``                                                     | Starts or updates world-target tracking around the configured allowed axis; the overload selects a point or a live transform.       |
+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void AimAt(Transform target)``                                                       | Starts or updates world-target tracking around the configured allowed axis; the overload selects a point or a live transform.       |
+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void Stop()``                                                                        | Clears moving-part rate, target and tracking requests at its current pose.                                                          |
+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void ReturnToNeutral()``                                                             | Requests movement toward the configured neutral pose within the part's limits.                                                      |
+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual float ClampPosition(float value)``                                                   | Returns a translation offset restricted to the configured travel limits.                                                            |
+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetTargetPosition(float value)``                                                | Requests smooth motion toward a bounded translation offset.                                                                         |
+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetPosition(float value)``                                                      | Applies an immediate bounded translation offset in metres from the captured neutral pose.                                           |
+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void SetNormalizedPosition(float value)``                                            | Maps a 0–1 fraction across the moving part's translation interval.                                                                  |
+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void CaptureNeutralPose()``                                                          | Replaces a moving part's neutral baseline and clears its previous motion requests.                                                  |
+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void GetRotationFrame(out Vector3 worldPivot, out Quaternion worldNeutralRotation)`` | Returns the moving part's configured rotation pivot/orientation frame.                                                              |
+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual void GetTranslationFrame(out Vector3 origin, out Vector3 direction)``                | Returns the configured frame used to interpret translation travel.                                                                  |
+-------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------+

+----------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| Event / callback                                   | Role                                                                                                             |
+====================================================+==================================================================================================================+
| ``public event Action<MovingPart> Moved``          | After moving-part pose changes. Payload: the ``MovingPart``; inspect current pose/state synchronously if needed. |
+----------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
| ``public event Action<bool> MotionEnabledChanged`` | When moving-part motion availability changes. Payload: bool.                                                     |
+----------------------------------------------------+------------------------------------------------------------------------------------------------------------------+
