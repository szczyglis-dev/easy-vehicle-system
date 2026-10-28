.. _evs-lights--vehicle-lighting:

Vehicle lighting
================

Lights manages independent headlight, high-beam, tail, brake, reverse and indicator channels.

.. _evs-lights--configure-channels:

Configure channels
------------------

1. Add Lights to the vehicle.
2. Assign Light sources and emissive renderers to each required channel.
3. Set channel availability, color, intensity and emission strength.
4. Use materials with emission support and separate renderers for independently controlled lenses.
5. Configure automatic brake/reverse response and indicator blink interval, then check the channels.

Tail lamps follow the requested beam mode. Brake and reverse lamps can follow mechanics or use API overrides. Configure **Handbrake Activates Brake Lights** if needed.

.. _evs-lights--control-lighting:

Control lighting
----------------

Use ``SetBeamMode``, ``SetIndicators``, ``SetHazards`` and ``SetChannelEnabled``. Brake, reverse and tail overrides accept ``null`` to restore automatic behavior. The controller's Live tab uses the same actions. See :doc:`Demo </Demo>` for sample bindings.

.. _evs-lights--indicator-sound:

Indicator sound
---------------

Add IndicatorAudio with Audio and Lights. Use the generated relay clicks or assign ``tickOn`` / ``tickOff``. Set volume, spatial blend and mixer routing; disable ``useDefaultClicks`` when unassigned clips should stay silent.

For phase events, output state, material handling and relay lifetime, see the :doc:`lighting reference </Scripting/Lights>`.
