# Action Camera Quality Control Test Plan (Organized by Test Type)

**Product:** Action Camera (Model: [Insert Model Number/Name])

**Ratings:** 100m Water Resistance, 15m Drop Resistance, 10 Hours Standby, 4 Hours Filming

**Buttons:** Power, Shutter, Mode Switch

**Test Plan Version:** 1.0

**Date:** February 14, 2024

## Risks

1. Test list is not full because some requirements are currently missed: 

 * Unspecified Ports and Connectivity
 * Memory Support Not Defined
 * Temperature Regimes Not Fully Covered
 * Maximum water temperature is also not specified

2. Some spare cameras are required for testing becase some of them could be damaged during Durability tests.


## Tests:

### I. Buttons Tests:


| Test ID | Test Description | Test Procedure Steps | Expected Results (Pass/Fail) |
|---|---|---|---|
| 1 | Power Button: General On/Off | 1. Press the power button to turn on the camera.<br>2. Press the power button briefly.<br>| 1. Camera powers on. <br>2. Camera powers off.  |
| 2 | Switch Button: Multiple Presses | 1. Power on the camera.<br>2. Press the mode switch button several times in quick succession.<br>3. Press Switch button 5 more times. | 1. Camera powers on successfully. <br>2. Modes change with each press. <br>3. Image and Vidoe mode are cycled properly  |
| 3 | Switch Button: Power Off in Each Mode | 1. Power on the camera.<br>2. Switch to each available mode using the mode switch button.<br>3. In each mode, attempt to power off the camera using the power button. | 1. Camera powers on successfully. <br>2. All modes accessible. <br>3. Camera powers off successfully in each mode.  | |
| 4 | Shutter Button (Image Mode) | 1. Power on the camera.<br>2. Press the mode switch button to change to image mode. <br>3. Press the shutter button.<br>4. Press the shutter button 5 more times. | 1. Camera powers on successfully. <br>2. Image mode engaged. <br>3. Image captured successfully.<br>4. 5 more Images captured successfully.  |
| 5 | Shutter Button (Video Mode)| 1. Power on the camera.<br>2. Press Switch button.<br>3. Press the Shutter button.<br>4. Press the shutter button again. | 1. Camera powers on successfully. <br>2. Video mode is set. <br>3. Video recording starts successfully.   <br>4. Video recording is stopped. |


### II. Record Quality Tests:

| Test ID | Test Description | Test Procedure Steps | Expected Results (Pass/Fail) |
|---|---|---|---|
| 6 | Video Quality Test (Day mode)| 1. Record video in various lighting conditions (bright, low light, indoors, outdoors).<br>2. Review recorded video on a large screen. | 1. Video records in all lighting conditions. <br>2. Video quality meets specifications (sharpness, color accuracy, stabilization, frame rate, resolution).  |
| 7 | Still Image Quality Test (Day mode) | 1. Capture still images in various lighting conditions.<br>2. Review captured images on a large screen. | 1. Images captured in all lighting conditions. <br>2. Image quality meets specifications (resolution, clarity, color accuracy, resolution).  | |
| 8 | Video Quality Test (Night mode) | 1. Record video in various night conditions.<br>2. Review recorded video on a large screen. | 1. Video records in all lighting conditions. <br>2. Video quality meets specifications (sharpness, color accuracy, stabilization, frame rate, resolution).  |
| 9 | Still Image Quality Test(Night mode) | 1. Capture still images in night conditions.<br>2. Review captured images on a large screen. | 1. Images captured in all lighting conditions. <br>2. Image quality meets specifications (resolution, clarity, color accuracy, xresolution).  | |

### III. Batttery Tests:
| Test ID | Test Description | Test Procedure Steps | Expected Results (Pass/Fail) |
|---|---|---|---|
| 10 | Battery Life Test (Standby) | 1. Fully charge battery.<br>2. Leave camera in standby mode.<br>3. Monitor battery life. | 1. Battery lasts for at least 10 hours in standby mode.  |
| 11 | Battery Life Test (Filming) | 1. Fully charge battery.<br>2. Record continuous video.<br>3. Monitor battery life. | 1. Battery lasts for at least 4 hours while filming.  |
| 12 | Battery Life Test (Image and Video) | 1. Fully charge battery.<br>2. Start to record video, stop it, make few images, then return in video mode. Repet it until battery is discharged<br>3. Monitor battery life. | 1. Battery lasts for at least 4 hours while filming and making photos.  |
### IV. Durability Tests:

| Test ID | Test Description | Test Procedure Steps | Expected Results (Pass/Fail) |
|---|---|---|---|
| 13 | Water Resistance Test (short time) |Repeat the following steps for 1m, 50 and 100m, water temperature should be 22°C: <br>1. Place camera in a pressurized chamber simulating required depth for 10sec.<br>2.Check image and video recording under the water. <br>3. Remove camera and inspect for water damage. | 1. No water damafe observed. <br>2. Image and video can be recorded sussfully under the water <br>3. Camera functions normally after test after remoing from water.  |
| 14 | Water Resistance Test (long time) |Repeat the following steps for 1m, 50 and 100m, water temperature should be 22°C: <br>1. Place camera in a pressurized chamber simulating required depth for 1 hour.<br>2.Check video recording under the water during 1 hour. <br>3. Inspect camera body for water damage. | 1. Buttons function correctly underwater.  <br>2. Image and video can be recorded sussfully under the water <br>3. Camera functions normally after test after remoing from water.  |
| 15 | Drop Test (power off) | Repeat the following steps for 1m, 8m and 15m: <br>1. Drop camera from a height of 15m onto a hard surface (concrete).<br>2. Turn on camera and inspect for physical damage and functionality. | 1. Camera withstands drop without significant damage. <br>2. Camera functions normally after drop.  |
| 16 | Drop Test (power on with video) | Repeat the following steps for 1m, 8m and 15m: <br>1. Turn on the camera and start filming.<br>2. Drop camera from a height of 15m onto a hard surface (concrete).<br>2. Take camera and inspect for physical damage and functionality. | <br>2. Filming is started successfully.<br>1. Camera withstands drop without significant damage. <br>2. Camera functions normally after drop and video can be stopped and saved.  |
 |