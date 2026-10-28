.. _evs-media--change-movement-modes:

Change movement modes
=====================

Use separate registered drive configurations when one vehicle can move in several ways, such as drive, hover and boat. Configure each mode's required modules, input and geometry before adding transitions.

.. _evs-media--set-up-a-profile-list:

Set up a profile list
---------------------

1. Add and enable ProfileSwitcher, and keep an enabled Drive module registered on the vehicle.
2. Expand Profiles and add as many entries as needed. Give each a unique ID, for example drive, hover and boat, then choose its strategy and tune its fields.
3. Set Active Profile Id to the entry represented by the controller's current Drive mode. Applying vehicle configuration reconnects that slot to the controller's strategy instance.
4. Use Toggle or the profile input command to advance through the list in order and wrap to the beginning. Use SwitchTo with an ID to select a particular entry.
5. Each entry can use any built-in or custom DriveProfile. Several entries may use the same class with independent tuning.

For runtime management, use RegisterProfile, UnregisterProfile, SetProfiles and ClearProfiles. List changes do not automatically switch the vehicle. Removing the active registration leaves its current movement running; the next Toggle selects the first remaining entry. Registry changes and overlapping switches are rejected while a transition is running.

.. _evs-media--assign-transitions-to-profile-pairs:

Assign transitions to profile pairs
-----------------------------------

Add a ProfileTransition component, or HoverDriveTransition for folding/deploying vehicle wheels. Set From Profile Id and To Profile Id, then add the component to the switcher's Transitions array. Enable Bidirectional to reuse it for the reverse change.

Set Duration on the transition. Forward Clip and Reverse Clip supply optional directional audio, with Volume controlling playback. Different pairs can have different components, durations and sounds. Exactly one enabled component may match a pair; overlapping matches reject the request. Pairs without a matching enabled component switch immediately.

The supplied Car/Porsche maps drive ↔ hover to one bidirectional HoverDriveTransition. It handles wheel folding, landing clearance and restoring road contact. Do not separately enable wheel contacts during its animation. Other registrations can be added without running that road/hover animation for unrelated pairs.

.. _evs-media--route-controls:

Route controls
--------------

Use one compatible input source for all modes, or add InputGate routes keyed by registered Profile Id. A two-position ProfileSwitchBinding maps its On Profile Id and Off Profile Id to any two entries. The gate selects inputs; your application owns possession.

.. _evs-media--hover-and-helicopter-presentation:

Hover and helicopter presentation
---------------------------------

HoverVisuals animates configured wheel/rotor mounts. Set tilt amounts and response for the model independently of hull forces. Propulsion handles supported rotor/propeller meshes; PropulsionJets supplies visual outlets.

Helicopter altitude hold captures height after lift release while powered. Configure it separately from visible controls and rotor response.

See :ref:`profile scripting <evs-scripting-driveprofiles--immediate-change-versus-animated-transition>` for lifecycle, registration APIs and a five-profile example. :doc:`Input </Input>` and :doc:`Particles </Particles>` cover the independent adapters and effects.
