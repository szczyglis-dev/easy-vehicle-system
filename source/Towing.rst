.. _evs-towing--tow-a-trailer:

Tow a trailer
=============

A trailer is an independent vehicle root with its own Rigidbody, wheels and wheel-support modules. It receives braking through Trailer rather than a player input source.

.. _evs-towing--configure-the-connection:

Configure the connection
------------------------

1. Prepare the trailer's wheel setup, suspension, friction and chassis collider.
2. Add Trailer and place its front Hitch at the connection point.
3. Add Coupler to the towing vehicle and place its rear Hitch.
4. Set Attach Distance, articulation limits and breaking policy. Place the two hitches close together.
5. Assign Initial Trailer and enable Attach On Start for startup attachment, or attach through gameplay.
6. Check forward/reverse towing, braking, a tight turn, detachment and detached parking.

Coupler refuses occupied hitches, self-attachment, cycles and distant trailers. Attachment aligns accepted nearby hitches over time; it does not teleport a distant vehicle.

.. _evs-towing--braking-and-detachment:

Braking and detachment
----------------------

Trailer forwards the towing vehicle's resolved service brake and handbrake. Park When Detached controls its parking policy. Set wheel brake roles and brake strength on the trailer itself.

Use Allow Joint Break for a breakable hitch; Explicit Detach remains available independently. Add a rear Coupler to a trailer for a road train, and validate the complete train's stability.

.. _evs-towing--tire-presentation:

Tire presentation
-----------------

Add Feedback and the desired tire audio, marks and particles to the trailer to use its own contacts. It does not need an engine loop.

The :doc:`towing reference </Scripting/Towing>` describes joint compliance, collision exclusions and a complete attach/detach example.
