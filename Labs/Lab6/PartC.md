[LAB6 INDEX](https://gitlab.com/iot110/iot110-student/blob/master/Labs/Lab6/setup.md)

## Part C - SenseHat Driver and Main WebApp Python code
**Synopsis:** Now we are developing an interface similar to our other sensor
labs.

## Objectives
* Create ```sense.py``` and add various sensor APIs
* UnitTest ```sense.py``` (via its main function)
* Modify ```main.py```

### Step C1: SenseHat Driver ```sense.py```
```python
#!/usr/bin/python
from sense_hat import SenseHat

class PiSenseHat(object):
    """Raspberry Pi 'IoT Sense Hat API Driver Class'."""

    # Constructor
    def __init__(self):
        self.sense = SenseHat()
        # enable all IMU functions
        self.sense.set_imu_config(True, True, True)

    ... (more to come...)    
```

### Step C2: Add an API for each Sensor
```python
# Pressure
def getPressure(self):
    return self.sense.get_pressure()

# Temperature
def getTemperature(self):
    return self.sense.get_temperature()

# Humidity
def getHumidity(self):
    return self.sense.get_humidity()

def getHumidityTemperature(self):
    return self.sense.get_temperature_from_humidity()

def getPressureTemperature(self):
    return self.sense.get_temperature_from_pressure()

def getOrientationRadians(self):
    return self.sense.get_orientation_radians()

def getOrientationDegrees(self):
    return self.sense.get_orientation_degrees()

# degrees from North
def getCompass(self):
    return self.sense.get_compass()

def getAccelerometer(self):
    return self.sense.get_accelerometer_raw()

def getEnvironmental(self):
    sensors = {'name' : 'sense-hat', 'environmental':{}}
    return sensors

def getJoystick(self):
    sensors = {'name' : 'sense-hat', 'joystick':{}}
    return sensors

def getInertial(self):
    sensors = {'name' : 'sense-hat', 'inertial':{}}
```


### Step C3: Add an API for each Sensor
```python
def getAllSensors(self):
    sensors = {'name' : 'sense-hat', 'environmental':{}, 'inertial':{}, 'joystick':{}}
    sensors['environmental']['pressure'] = { 'value':self.sense.get_pressure(), 'unit':'mbar'}
    sensors['environmental']['temperature'] = { 'value':self.sense.get_temperature(), 'unit':'C'}
    sensors['environmental']['humidity'] = { 'value':self.sense.get_humidity(), 'unit': '%RH'}
    accel = self.sense.get_accelerometer_raw()
    sensors['inertial']['accelerometer'] = { 'x':accel['x'], 'y':accel['y'], 'z': accel['z'], 'unit':'g'}
    orientation = self.sense.get_orientation_degrees()
    sensors['inertial']['orientation'] = { 'compass':self.sense.get_compass(), 'pitch':orientation['pitch'], 'roll':orientation['roll'], 'yaw': orientation['yaw'], 'unit':'degrees'}
    return sensors
```

### Step C3: main to test from CLI
```python
def main():

    # create an instance of my pi sense-hat sensor object
    pi_sense_hat = PiSenseHat()

    # Read Parameters.
    p = pi_sense_hat.getPressure()
    t_c = pi_sense_hat.getTemperature()
    h = pi_sense_hat.getHumidity()
    ht = pi_sense_hat.getHumidityTemperature()
    hp = pi_sense_hat.getPressureTemperature()
    orientation = pi_sense_hat.getOrientationDegrees()
    accel = pi_sense_hat.getAccelerometer()
    d = pi_sense_hat.getCompass()

    print("================ Discrete Sensor Values ==================")
    print "      Pressure :", p
    print "   Temperature :", t_c
    print "      Humidity :", h
    print "  HumidityTemp :", ht
    print "  PressureTemp :", hp
    print "       Compass :", d
    print("  p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))
    print("  x: {x}, y: {y}, z: {z}".format(**accel))
    print("==========================================================\n")

    print("================== Dictionary Object =====================")
    print(pi_sense_hat.getAllSensors())
    print("==========================================================\n")

if __name__=="__main__":
   main()
```

### Step C4: the ```Flask main.py```
```python
#!/usr/bin/python
import time
from sense import PiSenseHat
from flask import *

# create Pi SenseHat Object
pi_sense_hat = PiSenseHat()

# ============================== Functions ====================================
def get_sensor_values():
    return pi_sense_hat.getAllSensors()

# ============================== API Routes ===================================
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

# =========================== Endpoint: /myData ===============================
# read the sensor values by GET method from curl for example
# curl http://iot8e3c:5000/myData
# -----------------------------------------------------------------------------
@app.route('/myData')
def myData():
    def get_values():
        while True:
            # return the yield results on each loop, but never exits while loop
            data_obj = get_sensor_values()
            yield('data: {0}\n\n'.format(data_obj))
            time.sleep(1.0)
    return Response(get_values(), mimetype='text/event-stream')
# ============================== API Routes ===================================

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, threaded=True)
```

OK, onward to our webapp!

[PART D](https://gitlab.com/iot110/iot110-student/blob/master/Labs/Lab6/PartD.md) Build Sensor UI Components

[LAB6 INDEX](https://gitlab.com/iot110/iot110-student/blob/master/Labs/Lab6/setup.md)
