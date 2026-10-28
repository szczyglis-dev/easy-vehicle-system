.. _evs-controlinteractions--timed-control-interactions:

Timed control interactions
==========================

Use ControlInteraction when an action should commit at contact or during a gesture. It separates the gameplay action from the chosen presentation.

.. _evs-controlinteractions--choose-presentation:

Choose presentation
-------------------

+-----------+--------------------------------------------------------------------------+
| Mode      | Prepare                                                                  |
+===========+==========================================================================+
| Immediate | The action only; no character required                                   |
+-----------+--------------------------------------------------------------------------+
| IK        | Occupied seat, chosen hand, target handle and HandTransferHandle         |
+-----------+--------------------------------------------------------------------------+
| Animator  | Occupied seat or explicit supported Animator, trigger and gesture timing |
+-----------+--------------------------------------------------------------------------+
| Custom    | Occupied seat and your IControlInteractionDriver component               |
+-----------+--------------------------------------------------------------------------+

Animator mode still requires an occupied seat for admission, even with an explicit Animator override. Use Immediate for a character-independent action or provide an application integration.

.. _evs-controlinteractions--configure-the-action:

Configure the action
--------------------

1. Add ControlInteraction and choose the mode.
2. Assign the mode's seat/hand/target/driver references.
3. Connect On Commit to the gameplay action.
4. Start with a simple switch action and verify one commit per interaction.
5. Check interruption, a busy hand and seat exit before using it for game-critical controls.

When supplying a commit callback from code, leave On Commit empty unless both operations are intentional. Cancellation does not undo an action that already committed.

.. _evs-controlinteractions--animator-gesture:

Animator gesture
----------------

Create the configured trigger and transitions in your Animator Controller. Use an arm/hand Avatar Mask for a localized gesture. Set Commit Time to contact and Duration to the end of return; these times do not automatically follow clip speed.

For variable timing, use Animation Events for CommitAnimation/CompleteAnimation. Put the event relay on the actual Animator GameObject, including a generated seated animation source where applicable. Keep a timeout for missing events.

Call Cancel when abandoning an interaction. See :doc:`interaction contracts and examples </Scripting/Interactions>` for custom drivers, completion and late callbacks.
