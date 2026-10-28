.. _evs-distribution--installation-layouts-and-included-content:

Installation layouts and included content
=========================================

.. _evs-distribution--upm-installation:

UPM installation
----------------

Package identity: ``dev.szczyglis.easy-vehicle-system``. Runtime and editor sources remain in the installed package. Read the manual in its ``Documentation~`` directory.

Import **Demo** from Package Manager's **Samples** section if you want the example scene and its prefabs, scripts, art and licenses. Unity places it under ``Assets/Samples/Easy Vehicle System/<version>/Demo``.

.. _evs-distribution--asset-store-installation:

Asset Store installation
------------------------

1. In Package Manager, open **My Assets**, select Easy Vehicle System and choose **Import** after downloading it.
2. In Unity's standard **Import Unity Package** window, expand ``Assets/Szczyglis/EasyVehicleSystem``.
3. **Documentation** and **Demo** are separate sibling folders in that file list, alongside Runtime and Editor. Keep Documentation selected to import the manual; select Demo if you want the scene and examples. New package files are selected by default on the first import.
4. Choose **Import**. The manual is placed in ``Assets/Szczyglis/EasyVehicleSystem/Documentation``. Open ``Demo/Demo.unity`` for the supplied scene.

Importing a ``.unitypackage`` file directly uses the same standard Unity file-selection window and destination layout.

Choose one distribution format per project. Installing both introduces duplicate assemblies/assets. Keep the ``.meta`` files with imported assets when moving them in a Unity project.

.. _evs-distribution--requirements-and-rendering:

Requirements and rendering
--------------------------

The package manifest declares Unity 6000.0 or newer, Input System 1.19.0 and the required Unity physics, vehicles, animation, audio and particle modules. The supplied scene uses URP materials. For another render pipeline, provide suitable vehicle, water and effect materials; runtime mechanics do not depend on URP.

Installation does not replace your project's render pipeline or input settings. Configure input handling for the Input System and review your own project layers/collision matrix.

.. _evs-distribution--license-and-credits:

License and credits
-------------------

Read the package LICENSE and the supplied art/audio credits before redistribution. Original package code and third-party content have separate license terms. Third-party attribution and license files accompany the distributed assets; see :doc:`Third-party credits </ThirdParty>`.
