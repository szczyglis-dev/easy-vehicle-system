.. _evs-audio--add-vehicle-sound:

Add vehicle sound
=================

``Audio`` supplies shared mixer and spatial settings. Its channels add engine, tire, brake, indicator, switch and event sounds; water and damage systems have their own sound components. An **Engine Sound Profile** is a reusable asset describing an engine/propulsion loop, its pitch behavior and volume.

.. _evs-audio--1-prepare-the-vehicles-audio-components:

1. Prepare the vehicle's audio components
-----------------------------------------

1. Select the vehicle and add **Audio** plus **Engine Audio** through the controller's module controls or **Tools → EasyVehicleSystem → Add Component → Effects → Audio**.
2. Keep the core and its channels on the same GameObject. Assign the core's **Vehicle**, **Engine** and the intended Audio Mixer **Output** references; discover/register the core with the vehicle controller if you added it manually.
3. Configure **Spatial Blend**, **Min Distance** and **Max Distance** for the game camera/listener. Make sure the scene has an active AudioListener.
4. Add only the other channels you need, such as Tire Audio, Brake Audio or Boat Water Audio. Configure their clips separately from the engine loop.

Add Vehicle can populate bundled sound defaults. Your saved references control playback at runtime; you can replace them with your own assets.

.. _evs-audio--2-create-an-engine-sound-profile:

2. Create an Engine Sound Profile
---------------------------------

1. Import the desired loop recording into your project's Assets folder. Choose a recording with a clean loop boundary and suitable import/load settings for your game.
2. Create a folder such as **Assets/Audio/VehicleProfiles**. In the Project window, right-click and choose **Create → EasyVehicleSystem → Audio → Engine Sound Profile**.
3. Give the asset a descriptive name, such as **My Car Engine** or **Drone Rotor**.
4. Assign the imported AudioClip to **Loop**. This is the repeating engine/propulsion sound; start and stop recordings are assigned separately on Engine Audio.
5. Choose **Pitch Mode** from the table below. Set **Volume** and **Pitch Range** to suit the recording.
6. For an RPM profile, decide whether **Use Engine Response** should retain the vehicle's Engine Audio RPM/reference, load-tone and shifting response. Leave it off for the profile's simple activity-to-pitch mapping.
7. For a Motion profile, configure **Forward Speed Reference** and **Vertical Speed Reference**. They set the speeds at which motion activity reaches its upper range; use the unit selector beside the fields to enter your preferred speed units.
8. Save the asset, then assign it to a vehicle as described below.

+------------+---------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+
| Pitch Mode | Behavior                                                                                                                                    | Useful starting point                                      |
+============+=============================================================================================================================================+============================================================+
| Rpm        | Uses the engine's normalized RPM. With Use Engine Response enabled, Engine Audio supplies its more detailed RPM/load/shift response.        | Cars, trucks, motorcycles and tracked engines.             |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+
| Constant   | Uses the first Pitch Range value for its base pitch. Propulsion spool can still change the audible pitch/level during startup and shutdown. | A steady rotor or engine recording.                        |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+
| Motion     | Uses the larger normalized forward or vertical speed activity.                                                                              | Speed-responsive hover, rotor or other motion-based loops. |
+------------+---------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------+

To customize a bundled profile, duplicate it into your own Assets folder and edit the copy. Editing one shared profile changes every vehicle that references that asset; use separate assets when vehicles need independent sound tuning.

.. _evs-audio--3-assign-a-profile-to-a-drive-mode:

3. Assign a profile to a drive mode
-----------------------------------

1. Select the vehicle root and expand **VehicleController → Setup → Drive mode**.
2. Drag the Engine Sound Profile asset into that drive profile's **Engine Sound** field.
3. On **Engine Audio**, enable **Use Profile Sound**. Clear **Sound Override** to allow the selected drive profile's sound to be used.
4. For a vehicle with ProfileSwitcher, expand its registered Profiles and assign an Engine Sound to each mode that needs a different loop. The active registration represents the controller's current profile; when editing its sound, use the controller's Drive mode as the current configuration.
5. Save the vehicle prefab. In Play Mode, start the engine and check idle, acceleration, deceleration and mode changes from the intended listener position.

Profile changes select the active mode's assigned sound automatically when Use Profile Sound is enabled and no Sound Override is assigned. Mechanical engine settings and flight response are independent of the audio profile.

.. _evs-audio--4-replace-or-override-an-existing-sound:

4. Replace or override an existing sound
----------------------------------------

-  **Replace the sound for one drive mode:** create or duplicate a profile and replace that mode's Engine Sound reference. Other modes can keep their own assets.
-  **Use one sound across all modes on one vehicle:** assign **Engine Audio → Sound Override**. This takes priority over the active drive profile, even when Use Profile Sound is off. Clear the override to return to mode-specific sounds.
-  **Replace only the clip while retaining profile tuning:** assign **Profile Loop Override** on Engine Audio. Pitch and profile volume still come from the selected profile. Clear it to use that profile's Loop again.
-  **Use the fallback Engine Loop instead of profiles:** clear Sound Override and disable Use Profile Sound, or leave the active mode without an Engine Sound asset. Assign **Engine Loop**, **Engine Volume** and **Engine Pitch Range** on Engine Audio.

The selection order is **Sound Override → active drive profile when enabled → fallback Engine Loop**. An assigned profile with an empty Loop is silent unless Profile Loop Override supplies its clip; an empty clip does not automatically select the fallback. Profile Loop Override applies to a selected profile, not to the fallback Engine Loop.

Keep permanent reference changes outside Play Mode and save the prefab. Editing a shared asset changes every user of that asset; replacing the reference or duplicating the asset is the way to isolate one vehicle's sound.

.. _evs-audio--5-configure-ignition-levels-and-rotor-spool:

5. Configure ignition, levels and rotor spool
---------------------------------------------

Assign **Engine Start Clip** and **Engine Stop Clip** on Engine Audio and enable **Play Ignition Sounds** if you want those one-shot recordings. Set their individual volumes and **Engine Loop Start Delay** for the desired startup presentation. This delay controls the ordinary engine-loop path; supported propeller/rotor profiles follow the Propulsion spool state.

Use **Profile Volume Multiplier** to scale profile-driven loops on that vehicle and **Engine Mix Gain** to balance its engine channel. Mixer output and spatial distances are controlled by the shared Audio core. For rotorcraft, Propulsion's spin-up/spin-down state also affects playback, so a newly started rotor is not immediately at its full audible level.

If the replacement is silent, check that the core/channel and engine are enabled, ignition is running, the selected profile has a clip, overrides are set as intended, and the listener is within the configured audio range. An assigned Sound Override can hide a sound change made on the drive profile.

.. _evs-audio--tire-and-contact-sound-profiles:

Tire and contact sound profiles
-------------------------------

Engine Sound Profiles do not configure tire noise. For road, gravel or other ground sounds, create a **Tire Surface Profile**, assign its tire loop and rolling activity settings, then assign it through a **Tire Surface** on the ground collider or a parent. Set Feedback's Default Surface for ground without an explicit mapping. See :doc:`Surface setup </Surfaces>` for the complete assignment process.

TireAudio uses grounded rolling/slip feedback. Brake, indicator, event, water and damage clips belong to their own channels; balance them separately rather than replacing the engine profile. See :doc:`Audio scripting </Scripting/Audio>` for custom channels and runtime sound selection.
