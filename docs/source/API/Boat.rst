.. _evs-api-boat--boat-movement-api:

Boat movement API
=================

Read :doc:`the system explanation </Scripting/Boat>` for composition, setup and worked examples. This reference lists public members declared by each package type. Base-type links identify inherited contracts; the topic's method index also includes the relevant package base methods. Unity framework methods inherited from ``MonoBehaviour``, ``Object`` or ``ScriptableObject`` are documented by Unity.

.. _evs-api-boat--types:

Types
-----

-  :ref:`BoatProfile <evs-api-boat--boatprofile>`

.. _evs-api-boat--boatprofile:

BoatProfile
-----------

**Runtime/Drive/Profiles/BoatProfile.cs**

Owns authored boat movement parameters and the profile behavior.

**Inherits / implements:** :ref:`FreeProfile <evs-api-driveprofiles--freeprofile>`.

.. _evs-api-boat--methods:

Methods
~~~~~~~

+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Signature                                                                                  | Role and behavior                                                                                          | Arguments and result                                                                                                                                                                                                       |
+============================================================================================+============================================================================================================+============================================================================================================================================================================================================================+
| ``public BoatProfile()``                                                                   | Constructs ``BoatProfile`` with the supplied initial state.                                                | **Returns:** New instance initialized from the supplied arguments.                                                                                                                                                         |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public override void Step(VehicleController vehicle, Command command, float deltaTime)`` | Resolves steering, samples water and applies buoyancy, water-relative resistance, thrust and trim/rocking. | ``vehicle`` — Vehicle context/owner receiving the operation. ``command`` — Command sampled for this tick; use its channel metadata as well as axes. ``deltaTime`` — Elapsed time in seconds supplied by the owning loop.   |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| ``public virtual bool ContainsWater(Vector3 position)``                                    | Checks whether a position lies inside this profile's fallback water region.                                | ``position`` — Requested point or switch detent; see its declared type and owning operation. **Returns:** Predicate/result flag described by this operation; it is not a completion notification unless explicitly stated. |
+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _evs-api-boat--state-and-configuration:

State and configuration
~~~~~~~~~~~~~~~~~~~~~~~

+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| Member                                      | Meaning                                                                                                                                |
+=============================================+========================================================================================================================================+
| ``public override string Medium { get; }``  | Movement-family label used by the profile contract.                                                                                    |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public float waterLevel``                 | Flat fallback water-surface height in world metres.                                                                                    |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector2 waterCenter``              | Authored water center used by ``BoatProfile``. Initial value: ``new Vector2(-280f, 80f)``.                                             |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector2 waterSize``                | Zero size means an infinite flat water plane. Otherwise bounds are world-space X/Z.                                                    |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public float buoyancyDepth``              | Authored buoyancy depth used by ``BoatProfile``. Initial value: ``0.85f``.                                                             |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public float verticalDamping``            | Authored vertical damping used by ``BoatProfile``. Initial value: ``1.8f``.                                                            |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public float forwardDragScale``           | Scales the inherited Drag setting along the hull; lower values retain momentum longer.                                                 |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public float lateralResistance``          | Sideways resistance: lower values preserve sideways drift longer.                                                                      |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public float speedLateralResistance``     | Extra sideways grip per m/s of forward speed; keeps the hull tracking its heading under power.                                         |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public float speedResistance``            | Authored speed resistance used by ``BoatProfile``. Initial value: ``0.006f``.                                                          |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public float yawDampingScale``            | Scales inherited Angular Damping for yaw; pitch/roll use Rocking Damping.                                                              |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumYawRate``             | Upper requested yaw rate used by turning assistance, in rad/s.                                                                         |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public float steeringYawResponse``        | Rudder response to desired turn rate. Countersteering first arrests the current turn instead of building unchecked opposing torque.    |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public float stationaryTurnAcceleration`` | Authored stationary turn acceleration used by ``BoatProfile``. Initial value: ``0.12f``.                                               |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public float stationaryYawRate``          | Maximum requested low-speed boat yaw rate, in rad/s.                                                                                   |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public float steeringRiseTime``           | Authored steering rise time used by ``BoatProfile``. Initial value: ``0.35f``.                                                         |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public float steeringReturnTime``         | Authored steering return time used by ``BoatProfile``. Initial value: ``0.22f``.                                                       |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public float rockingStrength``            | Strength of maneuver, continuous water sway and wave rocking. Zero disables excitation while retaining upright stability and momentum. |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public float rockingSpring``              | Authored rocking spring used by ``BoatProfile``. Initial value: ``3.5f``.                                                              |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public float rockingDamping``             | Authored rocking damping used by ``BoatProfile``. Initial value: ``0.65f``.                                                            |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector2 accelerationTilt``         | Pitch/roll degrees per m/s² of measured acceleration.                                                                                  |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public float maximumManeuverTilt``        | Authored maximum maneuver tilt used by ``BoatProfile``. Initial value: ``6f``.                                                         |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public float poweredPitchDegrees``        | Sustained bow/stern lift at full propeller load, degrees; builds gradually with squared throttle demand and forward motion.            |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public float poweredPitchRiseTime``       | Seconds for sustained throttle lift to approach its target; longer values make the bow rise more gradually.                            |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public float poweredPitchReleaseTime``    | Seconds for sustained lift to settle after releasing/reversing throttle.                                                               |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public float powerPitchBoost``            | Authored power pitch boost used by ``BoatProfile``. Initial value: ``0.2f``.                                                           |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public float rockingMemorySeconds``       | Authored rocking memory seconds used by ``BoatProfile``. Initial value: ``2.5f``.                                                      |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public float loadedRockingDampingRatio``  | Authored loaded rocking damping ratio used by ``BoatProfile``. Initial value: ``0.85f``.                                               |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public float ambientWaveDegrees``         | Continuous rhythmic pitch/roll amplitude, degrees; active while idle and moving. Zero disables background sway.                        |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public float ambientWavePeriod``          | Seconds for a complete side-to-side water rocking cycle.                                                                               |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector2 ambientWaveInterval``      | Seconds between subtle random changes in wave amplitude and pitch phase; the side-to-side rhythm remains continuous.                   |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public Vector2 idleWaveInterval``         | Random interval between occasional stronger wave impulses, seconds; also active while moving.                                          |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
| ``public float idleWaveDegrees``            | Occasional wave impulse strength. Zero disables these impulses independently of background sway.                                       |
+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------+
