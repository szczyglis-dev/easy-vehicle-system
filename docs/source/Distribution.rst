.. _evs-distribution--installation-and-included-content:

Installation and included content
=================================

.. _evs-distribution--install-from-the-asset-store:

Install from the Asset Store
----------------------------

1. Open a Unity **6000.0.84f1** or newer project and sign in with the Unity account used to acquire Easy Vehicle System from the Asset Store.
2. Open **Window → Package Management → Package Manager** and select **My Assets**.
3. Select **Easy Vehicle System**, click **Download** if needed, then **Import**.
4. In the **Import Unity Package** window, keep the package files selected. Keep **Documentation** for the manual and **Demo** for the example scene and vehicles, then click **Import**.
5. Find the imported content under ``Assets/Szczyglis/EasyVehicleSystem``. The manual is in ``Documentation``; the example scene is ``Demo/Demo.unity``.

.. _evs-distribution--requirements-and-rendering:

Requirements and rendering
--------------------------

Use Unity 6000.0.84f1 or newer with Input System 1.19.0 installed. The supplied scene uses URP materials. For another render pipeline, provide suitable vehicle, water and effect materials; runtime mechanics do not depend on URP.

Installation does not replace your project's render pipeline or input settings. Configure input handling for the Input System and review your own project layers/collision matrix.

.. _evs-distribution--license-and-credits:

License and credits
-------------------

Read the package LICENSE and the supplied art/audio credits before redistribution. Original package code and third-party content have separate license terms. Third-party attribution and license files accompany the distributed assets; see :doc:`Third-party credits </ThirdParty>`.

.. _evs-distribution--release-version:

Release version
---------------

``EasyVehicleSystem.PackageVersion.Current`` is the shared version label for runtime UI and the vehicle Inspector, including Asset Store imports and player builds. When releasing, update ``Runtime/Core/PackageVersion.cs`` and the UPM ``package.json`` version together. ``Tools/build_distribution.py`` validates that these values match before writing distribution files. The demo footer uses the shared value rather than its own version string.
