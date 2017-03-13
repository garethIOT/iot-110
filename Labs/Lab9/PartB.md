[LAB8 INDEX](https://gitlab.com/iot110/iot110-student/blob/master/Labs/Lab9/setup.md)

## Part B - Create and Configure Devices for Azure IoT Hub
**Synopsis:** In this part, we will configure Azure IoT Hub.

## Objectives
* Provision an Azure IoT Hub

### Step B1: Create Azure IoT Hub
From Azure Portal Choose an Ubuntu 16 Compute VM.
![Azure IoT Hub]()

[npm package iothub explorer](https://www.npmjs.com/package/iothub-explorer)

[iothub-explorer https://github.com/Azure/iothub-explorer/blob/master/readme.md

### Step B2: Setup iothub-explorer
```sh
pi$ apt-get update
pi$ apt-get install -y nodejs
pi$ sudo apt install -y npm
pi$ sudo npm install -g iothub-explorer
pi$ iothub-explorer login "HostName=<<host>>;SharedAccessKeyName=service;SharedAccessKey=<<key>>"
Session started, expires on Sun Mar 05 2017 18:20:05 GMT-0800 (PST)
Session file: /home/pi/.iothub-explorer

https://github.com/Azure/azure-iot-sdk-python
git clone --recursive https://github.com/Azure/azure-iot-sdk-python.git

 => looking down in the service samples directory there is a iothub_messaging_sample.py
 => the standard ConnectionString is not parseable by this current code because it contains

AzureVM$ iothub-explorer list | grep foo
 deviceId:                   foo
 connectionString:           HostName=Iot110-hub.azure-devices.net;DeviceId=foo;SharedAccessKey=PyOxlqIITtqi3K7Jypw9Kg3vWgvMveJCbqSh0O+Q6c0=

 => DeviceId=foo  vs. SharedAccessKeyName=foo ???
AzureVM$ python iothub_messaging_sample.py -c "HostName=Iot110-hub.azure-devices.net;SharedAccessKeyName=foo;SharedAccessKey=PyOxlqIITtqi3K7Jypw9Kg3vWgvMveJCbqSh0O+Q6c0=" -d foo

iothub-explorer send foo 'hello9994' --ack=full

iothub-explorer monitor-feedback foo

iothub-explorer simulate-device --protocol=mqtt foo --receive




python iothub_message_demo.py -c "HostName=Iot110-hub.azure-devices.net;SharedAccessKeyName=device;SharedAccessKey=c6Glzei6IkM42CF9/ZuVknH/7OqbC+LaQVe4k7JaxO0=" -d foo


```

```sh
AzureVM$ sudo ln -s /usr/bin/nodejs /usr/bin/node
```

### Step B3: Login to IoT Hub via iothub-explorer
```sh
iothub-explorer login "HostName=<<host>>;SharedAccessKeyName=service;SharedAccessKey=<<key>>"
```

### Step B4: Create device <foo> via iothub-explorer
```sh
iothub-explorer create foo
```

### Step B5: Create device <foo> via iothub-explorer
```sh
iothub-explorer create foo
```

### Step B6: List all devices on IoT Hub via iothub-explorer
```sh
iothub-explorer list

iothub-explorer list |  grep foo
iothub-explorer list |  grep bar

```

### Step B7: Monitor Events for Device to Cloud (D2C)
```sh
iothub-explorer monitor-events foo --login "HostName=Iot110-hub.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=c6Glzei6IkM42CF9/ZuVknH/7OqbC+LaQVe4k7JaxO0="
```

### Step B8: Send Simulated Message from Device to Cloud (D2C)
```sh
iothub-explorer simulate-device foo --send "{deviceId: 'foo', windSpeed: 10.671534826979041 }"
```

### Step B9:


[PART C](https://gitlab.com/iot110/iot110-student/blob/master/Labs/Lab9/PartB.md)  TBD

[LAB8 INDEX](https://gitlab.com/iot110/iot110-student/blob/master/Labs/Lab9/setup.md)
