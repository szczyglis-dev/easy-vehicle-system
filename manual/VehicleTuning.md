# Tune a vehicle

For km/h, mph or m/s authoring and readouts, see [Speed units](SpeedUnits.md).

Change one group at a time and compare the same maneuver. Use the controller's Live values to distinguish an input problem, a mechanical limit and a presentation problem.

## 1. Establish the physical scale

Verify wheel radius/width, wheelbase, track width, chassis clearance and center of mass. Use the intended loaded mass, including physical characters and hinged parts. Configuration currently applies a minimum chassis mass of 100 kg.

A scaled visual model alone does not make a correct contact setup. Complete [wheel setup](GettingStarted.md#create-your-first-wheel-vehicle) before increasing grip or torque.

## 2. Make suspension support the load

Tune spring, damping, travel and target position until the vehicle settles within useful travel. Then check braking, cornering and a small bump. Add anti-roll support afterward. See [Suspension](Suspension.md).

## 3. Match engine and gearing

For gearbox drive, tune Peak Torque, torque curve, idle/redline and ratios together. Maximum Power and Maximum Drive Acceleration can cap the result; raising torque alone may not increase acceleration when a cap is active.

Direct mode uses Vehicle Settings' wheel-torque budget. Top Speed supplies a soft drive-torque fade, not a forced velocity. With gears, ratios, redline, drag and available power also determine attainable speed.

Set shift timing and automatic RPM thresholds after the gear range works. Configure a clutch if the player needs a pedal or a controllable launch. See [Gearbox](Gearbox.md), [Clutch](Clutch.md) and [drivetrain reference](Scripting/DriveDynamics.md).

## 4. Tune steering and grip

Set the road-wheel steering limit for the geometry. Configure visible steering-wheel travel separately. Adjust digital steering speed, optional speed/radius limits and Ackermann behavior, then check with the intended analog or digital input.

Set base grip and [ground Surface multipliers](Surfaces.md). Add traction/stability assistance after native contact behavior is acceptable. If DrivingAssists is installed, edit its shared settings there.

## 5. Validate before adding effects

Check start/stop, reverse, a tight turn, a fast turn, a slope and a landing. Verify passenger load and a reset/re-enable cycle. Save persistent changes outside Play Mode and repeat with a fresh instance.

Only then balance engine sound, exhaust, tire particles and marks. Those outputs should explain the mechanical behavior, not hide missing contact or an unsuitable drivetrain. Use [Troubleshooting](Troubleshooting.md) when a symptom cannot be isolated.
