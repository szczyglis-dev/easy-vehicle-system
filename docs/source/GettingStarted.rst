.. _evs-gettingstarted--getting-started:

Getting started
===============

For km/h, mph or m/s authoring and readouts, see :doc:`Speed units </SpeedUnits>`.

.. _evs-gettingstarted--install-the-package:

Install the package
-------------------

Use one distribution format in a project. Start with a compatible Unity 6 project:

-  **UPM:** install through Unity Package Manager. Read the manual in the package's Documentation~ directory and import **Demo** from its Samples section if you want the demo.
-  **Asset Store / Unity asset package:** use Unity's standard import window. Keep **Documentation** selected beside **Demo** in the file list; content is imported under ``Assets/Szczyglis/EasyVehicleSystem``.

The package declares Unity **6000.0** or newer and its Input System/module dependencies in ``package.json``. The supplied demo uses URP materials. Use a compatible URP project for its intended appearance; when using another render pipeline, supply suitable materials for the sample models and effects. The vehicle mechanics do not require URP.

Do not install both formats together: they contain the same assemblies and asset identities. See :doc:`installation layouts </Distribution>`.

.. _evs-gettingstarted--run-the-supplied-scene:

Run the supplied scene
----------------------

1. Keep Demo selected in the Asset Store import window, or import it from Package Manager's Samples section when using UPM.
2. Open ``Demo.unity`` in the imported sample's folder, or ``Demo/Demo.unity`` in the asset-package layout.
3. Enter Play Mode. Use the on-screen vehicle list to identify selection keys and the selected vehicle's control hints.
4. Use Page Up / Page Down to cycle vehicles, Tab to change camera mode and R to reset the selected vehicle's pose.

See :doc:`Demo </Demo>` for the controls.

.. _evs-gettingstarted--create-your-first-wheel-vehicle:

Create your first wheel vehicle
-------------------------------

This walkthrough builds a four-wheel car from your own model.

.. _evs-gettingstarted--1-prepare-the-root-and-model:

1. Prepare the root and model
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Create a root GameObject named **Car**. Use scale **(1, 1, 1)**, local **+Z forward** and **+Y up**.
2. Place the body model beneath it. Keep imported mesh scale/orientation corrections on model children.
3. Add a **Rigidbody** to the root and a suitable chassis collider. Keep the chassis collider clear of the wheel volumes. Wheels share the root Rigidbody; do not add a Rigidbody to each tire.
4. Select the root and choose **Tools → EasyVehicleSystem → Add Vehicle → Wheeled**. This adds VehicleController and the supporting modules.

.. _evs-gettingstarted--2-add-a-wheel-component-for-each-tire:

2. Add a Wheel component for each tire
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Create a **Wheels** child beneath the root.
2. Under Wheels, create an empty object for the first wheel, for example **WheelFL**. Place its pivot at the visible tire center. Keep its scale at **(1, 1, 1)** and its axes aligned with the vehicle.
3. On that object choose **Add Component → EasyVehicleSystem → Physics → Wheels → Wheel**. Adding **Wheel** also adds the required Unity **WheelCollider** on the same object.
4. Assign the visible tire's transform to **Wheel → Visual**. Use a centered visual pivot with the imported mesh beneath it if the source mesh has an offset origin. The visual pivot must be separate from the WheelCollider object: Wheel moves the visual to match suspension, steering and tire spin.
5. Set **Radius**, **Width** and **Mass** to match this tire. Radius is half the outside tire diameter, in metres. Review the WheelCollider gizmo against the model.
6. Set the wheel roles: enable **Steering** on front wheels, **Driven** on the driven axle, **Brake** for service braking and **Handbrake** on the intended parking-brake wheels.
7. Repeat for the remaining tires, for example **WheelFR**, **WheelRL** and **WheelRR**. Check each Visual assignment and pivot position individually.

For a first rear-wheel-drive car, use this role setup:

========== ======== ====== ===== =========
Wheels     Steering Driven Brake Handbrake
========== ======== ====== ===== =========
Front pair On       Off    On    Off
Rear pair  Off      On     On    On
========== ======== ====== ===== =========

Enable Driven on both pairs for all-wheel drive. Wheel count and roles can be changed for other axle layouts.

.. _evs-gettingstarted--3-register-and-configure-the-wheels:

3. Register and configure the wheels
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Select the vehicle root and open **VehicleController → Wheels**.
2. Click **Discover child Wheel Colliders** to populate **Wheel Setup** from the child wheels.
3. Expand every entry. Check its WheelCollider, wheel visual, radius and Steer/Drive/Brake/Handbrake roles. Add an optional caliper visual if needed.
4. Use **Advanced wheel configuration** for width, mass, steering multiplier, drive weight and visual rotation offsets. After discovery, **Wheel Setup** is the authoring source used when the controller configures the Wheel components; make further tuning changes here.
5. Click **Apply vehicle configuration**. Resolve validation messages before checking.

.. _evs-gettingstarted--4-connect-input-and-check:

4. Connect input and check
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. In **Setup**, check the input source installed by the preset. Use the keyboard sample, ``ActionInput`` or your own ``IInput`` provider.
2. Set the vehicle mass, center of mass and drivetrain values for your model. Adjust suspension travel, spring and damping for its weight.
3. Place the vehicle above a ground collider and enter Play Mode. Check tire contact, steering direction, acceleration and braking.
4. If a mesh rotates incorrectly, adjust its child orientation or Wheel Setup rotation offset. Check steering multipliers if an axle steers the wrong way.
5. Exit Play Mode, save tuning and references, then save the vehicle as a prefab.

The configured vehicle should have supported wheels, correct steering, forward acceleration and a stop under braking. If it does not, use :doc:`Troubleshooting </Troubleshooting>` before adding more systems.

Choose the next feature in :doc:`Choose systems </ChoosingSystems>`. Assign its model geometry and assets explicitly. Non-wheel modes can use an empty wheel list; aircraft can use authored landing gear. Setup cannot infer model-specific hinges, seats or effect outlets.

Continue with :doc:`Configuration </Configuration>`, :doc:`Drive profiles </DriveProfiles>` and :doc:`Vehicle tuning </VehicleTuning>`. For custom mechanics and replacements, see :doc:`Scripting </Scripting>`.
