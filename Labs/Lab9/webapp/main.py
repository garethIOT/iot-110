#!/usr/bin/python
import time
import paho.mqtt.client as paho
from sense import PiSenseHat
from flask import *

# create Pi SenseHat Object
pi_sense_hat = PiSenseHat()


# ============================= MQTT Callbacks ================================
# The callback for when a CONNACK message is received from the broker.
def on_connect(client, userdata, flags, rc):
    print("CONNACK received with code %d." % (rc))

# The callback for when a PUBLISH message is received from the broker.
def on_message(client, userdata, msg):
    print (string.split(msg.payload))
# ============================= MQTT Callbacks ================================

# ============================== Functions ====================================
def get_sensor_values():
    return pi_sense_hat.getAllSensors()

# ============================== API Routes ===================================
app = Flask(__name__)

# MQTT Configuration for local network
localBroker = "iot24ff"     # Local MQTT broker
localPort   = 1883          # Local MQTT port
localUser   = "pi"          # Local MQTT user
localPass = "raspberry"     # Local MQTT password
localTopic = "iot/sensor"   # Local MQTT topic to monitor
localTimeOut = 120          # Local MQTT session timeout

# Setup to Publish Sensor Data
mqttc = paho.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.username_pw_set(localUser, localPass)
mqttc.connect(localBroker, localPort, localTimeOut)

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
            data_obj['host'] = 'iot24ff.iot'
            yield('data: {0}\n\n'.format(data_obj))
#           print("MQTT Topic:"+localTopic, str(data_obj))
            print("MQTT Topic:"+localTopic, str(data_obj))
            mqttc.publish(localTopic,str(data_obj))
            time.sleep(1.0)
    return Response(get_values(), mimetype='text/event-stream')
# ============================== API Routes ===================================

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, threaded=True)
