[IOT STUDENT HOME](https://gitlab.com/iot110/iot110-student/blob/master/README.md)

## Setting up Lab6

**Synopsis:** For this lab we will continue building on our IoT suite by creating a web app
for the SenseHat device.  We will build on the jQuery  dashboard user interface
we started in Lab5, but focus on the major functional sensor and actuator classes
of the SenseHat platform.  Using the same Server Sent Events and JavaScript
charting capability we established in Lab5, we will extend to the *Environmental*,
*Inertial* sensors and provision for a future UI around the *JoyStick* and *LED
Matrix* Display capability.

### Objectives
* Test to ensure SenseHat hardware is functional and Python Library is Loaded
* Import jQuery UI HTML/CSS *Tabbed Panel* Framework
* Build a ```sense.py``` Python Driver to Provide an API for the SenseHat
* Interface the main Flask webapp ```main.py``` to the SenseHat Driver
* Add JavaScript code to parse the SenseHat sensor data and render on Tab panels

The various steps of this lab are summarized as:
* [PART A](https://gitlab.com/iot110/iot110-student/blob/master/Labs/Lab6/PartA.md) Test SenseHat Hardware
* [PART B](https://gitlab.com/iot110/iot110-student/blob/master/Labs/Lab6/PartB.md) Import jQuery UI Framework for Lab6
* [PART C](https://gitlab.com/iot110/iot110-student/blob/master/Labs/Lab6/PartC.md) SenseHat Driver and Main WebApp Python code
* [PART D](https://gitlab.com/iot110/iot110-student/blob/master/Labs/Lab6/PartD.md) Build Sensor UI Components

[IOT STUDENT HOME](https://gitlab.com/iot110/iot110-student/blob/master/README.md)

## Additional Supplemental Information for Debug ##
If your SenseHat is experiencing specific errors, your RPi may be in need of an
update ... see below:
[Errors running SenseHat](https://www.reddit.com/r/raspberry_pi/comments/3yg0rz/sense_hat_and_jessie/)

May need to run
```
pi$ sudo rpi-update
 *** Downloading specific firmware revision (this will take a few minutes)
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
                                 ...
 *** Updating firmware
 *** Updating kernel modules
 *** depmod 4.4.48+
 *** depmod 4.4.48-v7+
 *** Updating VideoCore libraries
 *** Using HardFP libraries
 *** Updating SDK
 *** Running ldconfig
 *** Storing current firmware revision
 *** Deleting downloaded files
 *** Syncing changes to disk
 *** If no errors appeared, your firmware was successfully updated to 71c475563fd5aa4ade62c9a31dd25865ab7d4a7b
 *** A reboot is needed to activate the new firmware
```
