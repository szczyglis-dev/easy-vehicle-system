.. _evs-interior--plan-the-cockpit:

Plan the cockpit
================

Choose presentation, physical contact and gameplay bindings separately:

+--------------------------------------+------------------------------------------------+
| Need                                 | Configure                                      |
+======================================+================================================+
| A moving steering wheel/yoke/stick   | The corresponding animator and motion pivots   |
+--------------------------------------+------------------------------------------------+
| A hand or foot following the control | A handle and seat limb binding                 |
+--------------------------------------+------------------------------------------------+
| A gauge or needle                    | InstrumentNeedle/RotaryHandle and value source |
+--------------------------------------+------------------------------------------------+
| A control requesting an action       | A mechanic binding or ControlInteraction       |
+--------------------------------------+------------------------------------------------+
| Mirrors/wipers/display               | The relevant Interior module                   |
+--------------------------------------+------------------------------------------------+

First verify that the mechanic works from input/API. Then add model animation, and finally fit the character's contacts through the complete range of motion.

Use independent neutral anchors at real hinges. Keep imported mesh corrections below motion pivots and avoid driving the same transform from several components.

Continue with :doc:`Interior controls </InteriorControls>`, :doc:`Seats and handles </SeatsAndHandles>`, :doc:`Timed interactions </ControlInteractions>` or :doc:`Mirrors and wipers </InteriorSystems>`.
