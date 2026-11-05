.. _evs-inspectorreference--complete-inspector-settings-reference:

Complete Inspector settings reference
=====================================

This final reference covers every editable Inspector field declared by the package runtime components, their base classes, referenced configuration blocks, profile types and the shipped demo components. The tables include serialized private fields as well as public settings. Internal caches hidden from the Inspector, runtime-only properties, methods and development verification tools are outside this reference.

.. _evs-inspectorreference--how-to-use-this-reference:

How to use this reference
-------------------------

-  Find a component in the alphabetical index below, or open a system chapter.
-  The Setting column gives the serialized field name. Unity normally displays a spaced label; custom inspectors may group or rename it.
-  Follow Inherited settings to see fields from base classes. Follow linked types to expand a nested configuration block or inspect a referenced package component.
-  Declared defaults are source initializers for a new component/data block, not the tuned values in a saved prefab. Constructors, selected drive profiles, setup commands and runtime binding can replace them. Range/Min entries describe Inspector constraints, not every validation rule.
-  Reference fields start unassigned unless initialized in source. Assign required model, body, animation, input and effect references before using the feature.
-  Speed fields use the selected Inspector display unit; each row states the stored unit. Other vector/angle frames depend on the component description.
-  The component enabled checkbox controls component availability. Additional per-feature switches only change that feature. Active, enabled and camera assignment can be separate states.

.. _evs-inspectorreference--configuration-ownership:

Configuration ownership
-----------------------

Vehicle Controller → Wheels → Wheel Setup owns registered Wheel geometry, roles and visual references. Those copied fields are read-only in Wheel; its local visual smoothing remains editable. Apply Vehicle Configuration copies the authored wheel setup and module tuning to native components.

Suspension owns native WheelCollider spring, damper, travel and force application settings. Configure these in Vehicle Settings/Suspension; an overriding ShockAbsorber can supply per-wheel physical settings. A native WheelCollider edit can be replaced on the next configuration.

Use the :doc:`Inspector overview </InspectorConfiguration>` for grouped tabs, module visibility and subclass configuration, and the :doc:`configuration guide </Configuration>` for the setup workflow.

.. _evs-inspectorreference--chapters:

Chapters
--------

+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| System                                                                                                        | Reference                                      |
+===============================================================================================================+================================================+
| :ref:`AccessAnimationEvents <evs-inspectorreference-world--accessanimationevents>`                            | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AccessAnimationProfile <evs-inspectorreference-world--accessanimationprofile>`                          | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AccessMotion <evs-inspectorreference-world--accessmotion>`                                              | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ActionInput <evs-inspectorreference-controller--actioninput>`                                           | Vehicle controller and input                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AdaptiveHandGrip <evs-inspectorreference-world--adaptivehandgrip>`                                      | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AdaptiveHandGrip.Finger <evs-inspectorreference-world--adaptivehandgripfinger>`                         | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AerobaticAirplaneProfile <evs-inspectorreference-drive--aerobaticairplaneprofile>`                      | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AimingHandExample <evs-inspectorreference-demo--aiminghandexample>`                                     | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AircraftControlMotion <evs-inspectorreference-exterior--aircraftcontrolmotion>`                         | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AircraftControlSurface <evs-inspectorreference-exterior--aircraftcontrolsurface>`                       | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AircraftControlSurfaces <evs-inspectorreference-exterior--aircraftcontrolsurfaces>`                     | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AircraftHud <evs-inspectorreference-interior--aircrafthud>`                                             | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AirplaneGroundContact <evs-inspectorreference-drive--airplanegroundcontact>`                            | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AirplaneProfile <evs-inspectorreference-drive--airplaneprofile>`                                        | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AirProfile <evs-inspectorreference-drive--airprofile>`                                                  | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AnchoredControlAnimator <evs-inspectorreference-interior--anchoredcontrolanimator>`                     | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AnchoredRotation <evs-inspectorreference-interior--anchoredrotation>`                                   | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AnchorHandle <evs-inspectorreference-world--anchorhandle>`                                              | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AntiRoll <evs-inspectorreference-drive--antiroll>`                                                      | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AntiRoll.Axle <evs-inspectorreference-drive--antirollaxle>`                                             | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Audio <evs-inspectorreference-effects--audio>`                                                          | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AudioEvent <evs-inspectorreference-effects--audioevent>`                                                | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AudioModule <evs-inspectorreference-effects--audiomodule>`                                              | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AudioSettingsOverride <evs-inspectorreference-effects--audiosettingsoverride>`                          | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`AutomaticGearbox <evs-inspectorreference-engine--automaticgearbox>`                                     | Engine, fuel and transmission                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`BalanceRider <evs-inspectorreference-world--balancerider>`                                              | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`BoatProfile <evs-inspectorreference-drive--boatprofile>`                                                | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`BoatWaterAudio <evs-inspectorreference-effects--boatwateraudio>`                                        | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`BoatWaterParticles <evs-inspectorreference-effects--boatwaterparticles>`                                | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Body <evs-inspectorreference-exterior--body>`                                                           | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`BrakeAudio <evs-inspectorreference-effects--brakeaudio>`                                                | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Brakes <evs-inspectorreference-drive--brakes>`                                                          | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Burnout <evs-inspectorreference-drive--burnout>`                                                        | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`CameraModule <evs-inspectorreference-world--cameramodule>`                                              | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Cameras <evs-inspectorreference-world--cameras>`                                                        | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`CarHud <evs-inspectorreference-interior--carhud>`                                                       | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Clutch <evs-inspectorreference-engine--clutch>`                                                         | Engine, fuel and transmission                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ClutchSource <evs-inspectorreference-interior--clutchsource>`                                           | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Coasting <evs-inspectorreference-physics--coasting>`                                                    | Wheels, contact and damage                     |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Collisions <evs-inspectorreference-physics--collisions>`                                                | Wheels, contact and damage                     |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`CommandValueSource <evs-inspectorreference-interior--commandvaluesource>`                               | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`CommercialAudio <evs-inspectorreference-effects--commercialaudio>`                                      | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ContactEnvelope <evs-inspectorreference-drive--contactenvelope>`                                        | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ControlAnimator <evs-inspectorreference-interior--controlanimator>`                                     | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ControlArm <evs-inspectorreference-drive--controlarm>`                                                  | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ControlHandle <evs-inspectorreference-world--controlhandle>`                                            | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ControlInteraction <evs-inspectorreference-interior--controlinteraction>`                               | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ControlInteractionAnimationEvents <evs-inspectorreference-interior--controlinteractionanimationevents>` | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ControllerModule <evs-inspectorreference-controller--controllermodule>`                                 | Vehicle controller and input                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Coupler <evs-inspectorreference-world--coupler>`                                                        | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`CustomLightGroup <evs-inspectorreference-exterior--customlightgroup>`                                   | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`CustomPassengerBody <evs-inspectorreference-world--custompassengerbody>`                                | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Damage <evs-inspectorreference-physics--damage>`                                                        | Wheels, contact and damage                     |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DamageAudio <evs-inspectorreference-effects--damageaudio>`                                              | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DamageAudio.ContactSound <evs-inspectorreference-effects--damageaudiocontactsound>`                     | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DamageCollisionRelay <evs-inspectorreference-physics--damagecollisionrelay>`                            | Wheels, contact and damage                     |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DamageImpactProfile <evs-inspectorreference-effects--damageimpactprofile>`                              | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DamagePart <evs-inspectorreference-exterior--damagepart>`                                               | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DefaultParticlePreset <evs-inspectorreference-effects--defaultparticlepreset>`                          | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DemoAircraftSystems <evs-inspectorreference-demo--demoaircraftsystems>`                                 | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DemoAnimatorCar <evs-inspectorreference-demo--demoanimatorcar>`                                         | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DemoCameraRig <evs-inspectorreference-demo--democamerarig>`                                             | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DemoCinematicCamera <evs-inspectorreference-demo--democinematiccamera>`                                 | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DemoControlsHud <evs-inspectorreference-demo--democontrolshud>`                                         | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DemoDamageControls <evs-inspectorreference-demo--demodamagecontrols>`                                   | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DemoDayNight <evs-inspectorreference-demo--demodaynight>`                                               | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DemoDirectWaypointAI <evs-inspectorreference-demo--demodirectwaypointai>`                               | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DemoDownforceModule <evs-inspectorreference-demo--demodownforcemodule>`                                 | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DemoEngineAudioMode <evs-inspectorreference-demo--demoengineaudiomode>`                                 | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DemoExternalControl <evs-inspectorreference-demo--demoexternalcontrol>`                                 | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DemoExternalControl.GizmoSettings <evs-inspectorreference-demo--demoexternalcontrolgizmosettings>`      | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DemoFreeCamera <evs-inspectorreference-demo--demofreecamera>`                                           | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DemoFreeCameraMotion <evs-inspectorreference-demo--demofreecameramotion>`                               | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DemoFreeParentCamera <evs-inspectorreference-demo--demofreeparentcamera>`                               | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DemoHud <evs-inspectorreference-demo--demohud>`                                                         | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DemoPassengerAccess <evs-inspectorreference-demo--demopassengeraccess>`                                 | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DemoPowerWindows <evs-inspectorreference-demo--demopowerwindows>`                                       | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DemoProbeModule <evs-inspectorreference-demo--demoprobemodule>`                                         | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DemoTowingControls <evs-inspectorreference-demo--demotowingcontrols>`                                   | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DemoUnderwater <evs-inspectorreference-demo--demounderwater>`                                           | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DemoVehicleSelector <evs-inspectorreference-demo--demovehicleselector>`                                 | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DemoVehicleWeapon <evs-inspectorreference-demo--demovehicleweapon>`                                     | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DemoWaterEntryAudio <evs-inspectorreference-demo--demowaterentryaudio>`                                 | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DemoWaypointAI <evs-inspectorreference-demo--demowaypointai>`                                           | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Differential <evs-inspectorreference-engine--differential>`                                             | Engine, fuel and transmission                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Differential.Axle <evs-inspectorreference-engine--differentialaxle>`                                    | Engine, fuel and transmission                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DirectController <evs-inspectorreference-controller--directcontroller>`                                 | Vehicle controller and input                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Drive <evs-inspectorreference-drive--drive>`                                                            | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DriveModule <evs-inspectorreference-drive--drivemodule>`                                                | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DriveProfile <evs-inspectorreference-drive--driveprofile>`                                              | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DriveProfileSlot <evs-inspectorreference-drive--driveprofileslot>`                                      | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DrivingAssists <evs-inspectorreference-drive--drivingassists>`                                          | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DroppableObject <evs-inspectorreference-world--droppableobject>`                                        | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`DynamicObstacle <evs-inspectorreference-physics--dynamicobstacle>`                                      | Wheels, contact and damage                     |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`EffectsModule <evs-inspectorreference-effects--effectsmodule>`                                          | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Engine <evs-inspectorreference-engine--engine>`                                                         | Engine, fuel and transmission                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`EngineAudio <evs-inspectorreference-effects--engineaudio>`                                              | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`EngineAudioItem <evs-inspectorreference-effects--engineaudioitem>`                                      | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`EngineModule <evs-inspectorreference-engine--enginemodule>`                                             | Engine, fuel and transmission                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`EngineRpmSource <evs-inspectorreference-interior--enginerpmsource>`                                     | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`EngineSoundProfile <evs-inspectorreference-effects--enginesoundprofile>`                                | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`EventAudio <evs-inspectorreference-effects--eventaudio>`                                                | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Events <evs-inspectorreference-effects--events>`                                                        | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ExhaustSmoke <evs-inspectorreference-effects--exhaustsmoke>`                                            | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ExteriorModule <evs-inspectorreference-exterior--exteriormodule>`                                       | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ExternalController <evs-inspectorreference-controller--externalcontroller>`                             | Vehicle controller and input                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`FreeProfile <evs-inspectorreference-drive--freeprofile>`                                                | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Friction <evs-inspectorreference-physics--friction>`                                                    | Wheels, contact and damage                     |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`FuelTank <evs-inspectorreference-engine--fueltank>`                                                     | Engine, fuel and transmission                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`GasSource <evs-inspectorreference-interior--gassource>`                                                 | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Gearbox <evs-inspectorreference-engine--gearbox>`                                                       | Engine, fuel and transmission                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`GearLeverAnimator <evs-inspectorreference-interior--gearleveranimator>`                                 | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`GearLeverHandle <evs-inspectorreference-world--gearleverhandle>`                                        | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`GearLeverPosition <evs-inspectorreference-interior--gearleverposition>`                                 | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`GearPaddleAnimator <evs-inspectorreference-interior--gearpaddleanimator>`                               | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`GearPaddleHandle <evs-inspectorreference-world--gearpaddlehandle>`                                      | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`GearShiftAnimator <evs-inspectorreference-interior--gearshiftanimator>`                                 | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`GearShiftDirection <evs-inspectorreference-interior--gearshiftdirection>`                               | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HalfShaft <evs-inspectorreference-drive--halfshaft>`                                                    | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HandbrakeSource <evs-inspectorreference-interior--handbrakesource>`                                     | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HandGrip <evs-inspectorreference-world--handgrip>`                                                      | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HandGrip.FingerPose <evs-inspectorreference-world--handgripfingerpose>`                                 | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HandleAnimatorBinding <evs-inspectorreference-world--handleanimatorbinding>`                            | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HandleFingerPosition <evs-inspectorreference-world--handlefingerposition>`                              | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HandleHandPose <evs-inspectorreference-world--handlehandpose>`                                          | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HandleHandPosition <evs-inspectorreference-world--handlehandposition>`                                  | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HandleHandPositionPreset <evs-inspectorreference-world--handlehandpositionpreset>`                      | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HandleMotion <evs-inspectorreference-interior--handlemotion>`                                           | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HandlePoseSettings <evs-inspectorreference-world--handleposesettings>`                                  | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HandleUseSettings <evs-inspectorreference-world--handleusesettings>`                                    | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HelicopterProfile <evs-inspectorreference-drive--helicopterprofile>`                                    | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HornAudio <evs-inspectorreference-effects--hornaudio>`                                                  | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HoverDriveTransition <evs-inspectorreference-drive--hoverdrivetransition>`                              | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HoverProfile <evs-inspectorreference-drive--hoverprofile>`                                              | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HoverVisuals <evs-inspectorreference-exterior--hovervisuals>`                                           | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HoverVisuals.TiltMount <evs-inspectorreference-exterior--hovervisualstiltmount>`                        | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HumanoidAccessMotion <evs-inspectorreference-world--humanoidaccessmotion>`                              | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HumanoidIK <evs-inspectorreference-world--humanoidik>`                                                  | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HumanoidJointDefinition <evs-inspectorreference-world--humanoidjointdefinition>`                        | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`HumanoidPassenger <evs-inspectorreference-world--humanoidpassenger>`                                    | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`IGearShiftAnimator <evs-inspectorreference-interior--igearshiftanimator>`                               | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`IndicatorAudio <evs-inspectorreference-effects--indicatoraudio>`                                        | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`IndicatorSwitchBinding <evs-inspectorreference-interior--indicatorswitchbinding>`                       | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`InputBuffer <evs-inspectorreference-controller--inputbuffer>`                                           | Vehicle controller and input                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`InputGate <evs-inspectorreference-controller--inputgate>`                                               | Vehicle controller and input                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`InputGate.Route <evs-inspectorreference-controller--inputgateroute>`                                    | Vehicle controller and input                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`InstrumentNeedle <evs-inspectorreference-interior--instrumentneedle>`                                   | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`InteriorCamera <evs-inspectorreference-world--interiorcamera>`                                          | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`InteriorDataSourceAttribute <evs-inspectorreference-interior--interiordatasourceattribute>`             | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`InteriorModule <evs-inspectorreference-interior--interiormodule>`                                       | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`InteriorValueSource <evs-inspectorreference-interior--interiorvaluesource>`                             | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`JetProfile <evs-inspectorreference-drive--jetprofile>`                                                  | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`JoystickHandle <evs-inspectorreference-world--joystickhandle>`                                          | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`KeyboardBoatInput <evs-inspectorreference-controller--keyboardboatinput>`                               | Vehicle controller and input                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`KeyboardDriveInput <evs-inspectorreference-controller--keyboarddriveinput>`                             | Vehicle controller and input                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`KeyboardFlightInput <evs-inspectorreference-controller--keyboardflightinput>`                           | Vehicle controller and input                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`KeyboardInput <evs-inspectorreference-controller--keyboardinput>`                                       | Vehicle controller and input                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`KeyboardSubmarineInput <evs-inspectorreference-controller--keyboardsubmarineinput>`                     | Vehicle controller and input                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`LandingGear <evs-inspectorreference-exterior--landinggear>`                                             | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`LandingGearPart <evs-inspectorreference-exterior--landinggearpart>`                                     | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`LandingGearSuspension <evs-inspectorreference-exterior--landinggearsuspension>`                         | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`LandingGearSuspensionPart <evs-inspectorreference-exterior--landinggearsuspensionpart>`                 | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`LandingGearSwitch <evs-inspectorreference-demo--landinggearswitch>`                                     | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`LightChannel <evs-inspectorreference-exterior--lightchannel>`                                           | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Lights <evs-inspectorreference-exterior--lights>`                                                       | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ManualGearbox <evs-inspectorreference-engine--manualgearbox>`                                           | Engine, fuel and transmission                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`MotorcycleBalance <evs-inspectorreference-drive--motorcyclebalance>`                                    | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`MotorcycleHandle <evs-inspectorreference-world--motorcyclehandle>`                                      | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`MotorcycleProfile <evs-inspectorreference-drive--motorcycleprofile>`                                    | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`MovingPart <evs-inspectorreference-exterior--movingpart>`                                               | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Nitro <evs-inspectorreference-engine--nitro>`                                                           | Engine, fuel and transmission                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ObjectDropper <evs-inspectorreference-world--objectdropper>`                                            | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`OrbitCamera <evs-inspectorreference-world--orbitcamera>`                                                | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ParkingHold <evs-inspectorreference-drive--parkinghold>`                                                | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PartMotionAudio <evs-inspectorreference-exterior--partmotionaudio>`                                     | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PartMotionEvents <evs-inspectorreference-exterior--partmotionevents>`                                   | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PassengerAccess <evs-inspectorreference-world--passengeraccess>`                                        | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PassengerBehaviour <evs-inspectorreference-world--passengerbehaviour>`                                  | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PassengerBody <evs-inspectorreference-world--passengerbody>`                                            | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PassengerBodyPartConfig <evs-inspectorreference-world--passengerbodypartconfig>`                        | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PassengerFootConfig <evs-inspectorreference-world--passengerfootconfig>`                                | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PassengerGForceLimits <evs-inspectorreference-world--passengergforcelimits>`                            | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PassengerHandConfig <evs-inspectorreference-world--passengerhandconfig>`                                | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PassengerJointSupport <evs-inspectorreference-world--passengerjointsupport>`                            | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PassengerModule <evs-inspectorreference-world--passengermodule>`                                        | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PassengerRestraints <evs-inspectorreference-world--passengerrestraints>`                                | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Passengers <evs-inspectorreference-world--passengers>`                                                  | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PassengerSeat <evs-inspectorreference-world--passengerseat>`                                            | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PassengerTransformSupport <evs-inspectorreference-world--passengertransformsupport>`                    | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PedalAnimator <evs-inspectorreference-interior--pedalanimator>`                                         | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PedalFootMode <evs-inspectorreference-world--pedalfootmode>`                                            | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PedalHandle <evs-inspectorreference-world--pedalhandle>`                                                | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PhysicsModule <evs-inspectorreference-physics--physicsmodule>`                                          | Wheels, contact and damage                     |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PitchSource <evs-inspectorreference-interior--pitchsource>`                                             | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ProfileSwitchBinding <evs-inspectorreference-interior--profileswitchbinding>`                           | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ProfileSwitcher <evs-inspectorreference-drive--profileswitcher>`                                        | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ProfileTransition <evs-inspectorreference-drive--profiletransition>`                                    | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Projectile <evs-inspectorreference-demo--projectile>`                                                   | Demo components and examples                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Propulsion <evs-inspectorreference-exterior--propulsion>`                                               | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Propulsion.Propeller <evs-inspectorreference-exterior--propulsionpropeller>`                            | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`PropulsionJets <evs-inspectorreference-effects--propulsionjets>`                                        | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`RagdollCollisionHelper <evs-inspectorreference-world--ragdollcollisionhelper>`                          | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`RagdollCollisionRelay <evs-inspectorreference-world--ragdollcollisionrelay>`                            | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`RearMirror <evs-inspectorreference-interior--rearmirror>`                                               | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`RearMirrors <evs-inspectorreference-interior--rearmirrors>`                                             | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Rocket <evs-inspectorreference-world--rocket>`                                                          | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`RocketLauncher <evs-inspectorreference-world--rocketlauncher>`                                          | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`RollSource <evs-inspectorreference-interior--rollsource>`                                               | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`RotaryAnimator <evs-inspectorreference-interior--rotaryanimator>`                                       | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`RotaryHandle <evs-inspectorreference-world--rotaryhandle>`                                              | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`SceneGizmoOptions <evs-inspectorreference-common--scenegizmooptions>`                                   | Common settings and base components            |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`SeatAccess <evs-inspectorreference-world--seataccess>`                                                  | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ServiceBrakeSource <evs-inspectorreference-interior--servicebrakesource>`                               | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Settings <evs-inspectorreference-common--settings>`                                                     | Common settings and base components            |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ShockAbsorber <evs-inspectorreference-drive--shockabsorber>`                                            | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Skidmarks <evs-inspectorreference-effects--skidmarks>`                                                  | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`SpeedValueSource <evs-inspectorreference-interior--speedvaluesource>`                                   | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Stabilization <evs-inspectorreference-physics--stabilization>`                                          | Wheels, contact and damage                     |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Steering <evs-inspectorreference-drive--steering>`                                                      | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`SteeringHandRegrip <evs-inspectorreference-world--steeringhandregrip>`                                  | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`SteeringHandRegripSettings <evs-inspectorreference-world--steeringhandregripsettings>`                  | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`SteeringPart <evs-inspectorreference-exterior--steeringpart>`                                           | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`SteeringSource <evs-inspectorreference-interior--steeringsource>`                                       | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`SteeringStickAnimator <evs-inspectorreference-interior--steeringstickanimator>`                         | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`SteeringTieRod <evs-inspectorreference-drive--steeringtierod>`                                          | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`SteeringWheelAnimator <evs-inspectorreference-interior--steeringwheelanimator>`                         | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`SteeringWheelHandle <evs-inspectorreference-world--steeringwheelhandle>`                                | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`SteeringWheelHandle.RimSample <evs-inspectorreference-world--steeringwheelhandlerimsample>`             | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`SubmarineProfile <evs-inspectorreference-drive--submarineprofile>`                                      | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Surface <evs-inspectorreference-physics--surface>`                                                      | Wheels, contact and damage                     |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Suspension <evs-inspectorreference-drive--suspension>`                                                  | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`SuspensionAxle <evs-inspectorreference-drive--suspensionaxle>`                                          | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`SuspensionHub <evs-inspectorreference-drive--suspensionhub>`                                            | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`SuspensionRotationLimits <evs-inspectorreference-drive--suspensionrotationlimits>`                      | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`SwitchAnimator <evs-inspectorreference-interior--switchanimator>`                                       | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`SwitchAudio <evs-inspectorreference-effects--switchaudio>`                                              | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`SwitchHandle <evs-inspectorreference-world--switchhandle>`                                              | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`SwitchPosition <evs-inspectorreference-interior--switchposition>`                                       | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ThrottleAnimator <evs-inspectorreference-interior--throttleanimator>`                                   | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`ThrottleHandle <evs-inspectorreference-world--throttlehandle>`                                          | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`TireAudio <evs-inspectorreference-effects--tireaudio>`                                                  | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`TireCollision <evs-inspectorreference-physics--tirecollision>`                                          | Wheels, contact and damage                     |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`TireFeedback <evs-inspectorreference-effects--tirefeedback>`                                            | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`TireSmoke <evs-inspectorreference-effects--tiresmoke>`                                                  | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`TireSurface <evs-inspectorreference-effects--tiresurface>`                                              | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`TireSurface.LayerMapping <evs-inspectorreference-effects--tiresurfacelayermapping>`                     | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`TireSurfaceProfile <evs-inspectorreference-effects--tiresurfaceprofile>`                                | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`TrackedProfile <evs-inspectorreference-drive--trackedprofile>`                                          | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`TrackPathBuilder <evs-inspectorreference-exterior--trackpathbuilder>`                                   | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Tracks <evs-inspectorreference-drive--tracks>`                                                          | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`TrackVisuals <evs-inspectorreference-exterior--trackvisuals>`                                           | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`TrackVisuals.Belt <evs-inspectorreference-exterior--trackvisualsbelt>`                                  | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`TrackVisuals.Roller <evs-inspectorreference-exterior--trackvisualsroller>`                              | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`TractionControl <evs-inspectorreference-engine--tractioncontrol>`                                       | Engine, fuel and transmission                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Trailer <evs-inspectorreference-world--trailer>`                                                        | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Transmission <evs-inspectorreference-engine--transmission>`                                             | Engine, fuel and transmission                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`TwistThrottleAnimator <evs-inspectorreference-interior--twistthrottleanimator>`                         | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`VehicleAudioSettings <evs-inspectorreference-effects--vehicleaudiosettings>`                            | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`VehicleBodyPart <evs-inspectorreference-exterior--vehiclebodypart>`                                     | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`VehicleController <evs-inspectorreference-controller--vehiclecontroller>`                               | Vehicle controller and input                   |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`VehicleHandle <evs-inspectorreference-world--vehiclehandle>`                                            | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`VehicleHandleAnimator <evs-inspectorreference-interior--vehiclehandleanimator>`                         | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`VehicleMeshDeformation <evs-inspectorreference-physics--vehiclemeshdeformation>`                        | Wheels, contact and damage                     |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`VehicleModule <evs-inspectorreference-common--vehiclemodule>`                                           | Common settings and base components            |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`VehicleValueSource <evs-inspectorreference-interior--vehiclevaluesource>`                               | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`WaterInteraction <evs-inspectorreference-world--waterinteraction>`                                      | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`WaterProvider <evs-inspectorreference-world--waterprovider>`                                            | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`WaterStyle <evs-inspectorreference-world--waterstyle>`                                                  | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`WaterSurface <evs-inspectorreference-world--watersurface>`                                              | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`WeaponBarrel <evs-inspectorreference-world--weaponbarrel>`                                              | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`WeaponEffects <evs-inspectorreference-effects--weaponeffects>`                                          | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`WeaponRecoil <evs-inspectorreference-effects--weaponrecoil>`                                            | Audio, particles and feedback                  |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Wheel <evs-inspectorreference-physics--wheel>`                                                          | Wheels, contact and damage                     |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`WheelDynamics <evs-inspectorreference-physics--wheeldynamics>`                                          | Wheels, contact and damage                     |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`WheeledProfile <evs-inspectorreference-drive--wheeledprofile>`                                          | Drive profiles, steering and suspension        |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`WheelLift <evs-inspectorreference-physics--wheellift>`                                                  | Wheels, contact and damage                     |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`WheelPart <evs-inspectorreference-exterior--wheelpart>`                                                 | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`WheelSetup <evs-inspectorreference-physics--wheelsetup>`                                                | Wheels, contact and damage                     |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Wiper <evs-inspectorreference-exterior--wiper>`                                                         | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`WiperBlade <evs-inspectorreference-exterior--wiperblade>`                                               | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`Wipers <evs-inspectorreference-exterior--wipers>`                                                       | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`WiperSwitchBinding <evs-inspectorreference-exterior--wiperswitchbinding>`                               | Body, lights, wipers and aircraft equipment    |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`WorldModule <evs-inspectorreference-world--worldmodule>`                                                | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`YokeAnimator <evs-inspectorreference-interior--yokeanimator>`                                           | Interior controls and instruments              |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+
| :ref:`YokeHandle <evs-inspectorreference-world--yokehandle>`                                                  | Cameras, passengers, water, towing and weapons |
+---------------------------------------------------------------------------------------------------------------+------------------------------------------------+

\| :ref:`NitroAudio <evs-inspectorreference-effects--nitroaudio>` \| Audio, particles and feedback \| \| :ref:`DamageImpactEffects <evs-inspectorreference-effects--damageimpacteffects>` \| Audio, particles and feedback \| \| :ref:`MovingPartAudio <evs-inspectorreference-effects--movingpartaudio>` \| Audio, particles and feedback \| \| :ref:`WipersAudio <evs-inspectorreference-effects--wipersaudio>` \| Audio, particles and feedback \| \| :ref:`WiperAudioEntry <evs-inspectorreference-effects--wiperaudioentry>` \| Audio, particles and feedback \| \| :ref:`ProfileTransitionAudio <evs-inspectorreference-effects--profiletransitionaudio>` \| Audio, particles and feedback \|

\| :ref:`ProfileTransitionAudio.TransitionSound <evs-inspectorreference-effects--profiletransitionaudiotransitionsound>` \| Audio, particles and feedback \|

Coverage: 292 component/base/data sections. Inherited settings are linked to their declaring type; preset constructors and saved prefabs can override initial values.

.. toctree::
   :maxdepth: 1
   :caption: Inspector settings by system

   InspectorReference/Common
   InspectorReference/Controller
   InspectorReference/Demo
   InspectorReference/Drive
   InspectorReference/Effects
   InspectorReference/Engine
   InspectorReference/Exterior
   InspectorReference/Interior
   InspectorReference/Physics
   InspectorReference/World
