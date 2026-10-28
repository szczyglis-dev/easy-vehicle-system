.. _evs-suspension--suspension-setup:

Suspension setup
================

Start with native wheel suspension. Add visual linkage only after the chassis is supported and settles correctly.

.. _evs-suspension--support-the-vehicle:

Support the vehicle
-------------------

1. Check wheel radius, chassis clearance and vehicle mass.
2. Set suspension travel in Vehicle Settings.
3. On Suspension, set Spring, Damper and Target Position. Tune the loaded vehicle, including intended occupants.
4. Apply vehicle configuration and check a flat-ground rest, braking, cornering and a small bump.
5. Adjust AntiRoll independently if axle roll support is needed.

+--------------------------------------+--------------------------------------------------------------------+
| Observed behavior                    | First adjustment                                                   |
+======================================+====================================================================+
| Suspension sits at an end stop       | Check travel, mass, spring strength and target position.           |
+--------------------------------------+--------------------------------------------------------------------+
| Repeated bouncing                    | Increase damping gradually after the spring supports the load.     |
+--------------------------------------+--------------------------------------------------------------------+
| Very harsh sharp bumps               | Check travel and degressive damping before adding body assistance. |
+--------------------------------------+--------------------------------------------------------------------+
| Wheel contacts intersect the chassis | Fix collider geometry and wheel placement.                         |
+--------------------------------------+--------------------------------------------------------------------+

Native wheel springs remain configured when the setup script is disabled. Suspension writes the native wheel spring/damper/travel settings. Edit its settings rather than tuning the same WheelCollider values separately.

.. _evs-suspension--add-visible-linkage:

Add visible linkage
-------------------

Use ShockAbsorber for a shock assembly, ControlArm for arms, SuspensionHub and SteeringTieRod for hub/steering geometry, SuspensionAxle for an axle presentation, and HalfShaft for a shaft. Assign their wheel and attachment references at the model's actual joints. Keep mesh scale/orientation corrections on child meshes.

Preview compression/rebound and both steering locks. Axis permissions and length/angular limits must allow the geometry to reach those poses. Visual linkage cannot make incompatible anchors meet.

A ShockAbsorber can override one wheel's physical spring/damper using its motion ratio. Use one physical override per wheel. Set up visual-only shocks without that override.

See the :doc:`suspension reference </Scripting/Suspension>` for linkage solving, units, motion-ratio conversion and a code tuning example. Aircraft's hinged gear has a separate :ref:`setup <evs-aircraft--hinged-gear-suspension>`.
