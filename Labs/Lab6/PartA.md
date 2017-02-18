[LAB6 INDEX](https://gitlab.com/iot110/iot110-student/blob/master/Labs/Lab6/setup.md)

## Part A - Test SenseHat Hardware
**Synopsis:** We need to initially test and ensure that the SenseHat hardware is
functional and driver is loaded.

## Objectives
* Fasten [SenseHat](https://www.raspberrypi.org/products/sense-hat/) to RPi3 Platform
* Browse to the [SenseHat API](http://pythonhosted.org/sense-hat/api/)
* Startup and manually send a message and read some temperature data

### Step A1: Install SenseHat Library
```sh
pi$ sudo apt-get update
pi$ sudo apt-get install sense-hat
pi$ sudo reboot
```

### Step A2: Hello SenseHat
```sh
pi$ python
>>> from sense_hat import SenseHat
>>> sense = SenseHat()
>>> sense.show_message("Hello SenseHat World!")
```
This should scroll a message across the SenseHat LED Matrix Display.


### Step A3: Verify some Sensor Data
```sh
pi$ python
>>> from sense_hat import SenseHat
>>> sense = SenseHat()
>>> temp = sense.get_temperature()
>>> print("Temperature: %s C" % temp)
Temperature: 31.2470054626 C
>>> <ctrl-D>
```

### Step A4: Check the I2C Bus Address Map
```sh
pi$ sudo i2cdetect -y 1
0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- 1c -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- UU -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- 5c -- -- 5f
60: -- -- -- -- -- -- -- -- -- -- 6a -- -- -- -- --
70: -- -- -- -- -- -- -- --
```
You are now ready to use SenseHat!

[PART B](https://gitlab.com/iot110/iot110-student/blob/master/Labs/Lab6/PartB.md) Import jQuery UI Framework for Lab6

[LAB6 INDEX](https://gitlab.com/iot110/iot110-student/blob/master/Labs/Lab6/setup.md)
