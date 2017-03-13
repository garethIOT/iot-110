[LAB8 INDEX](https://gitlab.com/iot110/iot110-student/blob/master/Labs/Lab9/setup.md)

## Part A - Install MQTT on Azure Ubuntu VM
**Synopsis:** In this part, we will install and test MQTT on an Azure Ubuntu Virtual Machine (VM).

## Objectives
* Provision an Azure Ubuntu VM as aan MQTT Broker
* Test the MQTT Pub/Sub Capability
* Setup basic Password Authentication to the MQTT Broker and Test
* Set up SSL Certificates and Test

### Step A1: Provision an Azure VM to act as an MQTT Broker
From Azure Portal Choose an Ubuntu 16 Compute VM.
![Ubuntu 16.04 LTS VM](https://gitlab.com/iot110/iot110-student/raw/master/Resources/Images/AzureCreateVM.png)

Get SSH public key from development host machine (from the ~/.ssh/id_rsa.pub file created with the ssh-keygen comamnd).

Note: if you have not created a public key please log into a linux shell or Git Bash CLI and perform the following:
```sh
host$ cd ~/.ssh
host$ ssh-keygen        # <= just hit enter for all questions
host$ cat id_rsa.pub    # <= copy the SSH public key to your clipboard
```  

![Ubuntu SSH Keys](https://gitlab.com/iot110/iot110-student/raw/master/Resources/Images/AzureVM-SSHKeys.png)

### Step A2: Log In & Install Libraries and Mosquitto MQTT Broker
There is a great tutorial found at Digital Ocean concerning installing and testing both
password only and encrypted (SSL) communications between a MQTT client and
MQTT broker (server).  [Digital Ocean MQTT Tutorial](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-the-mosquitto-mqtt-messaging-broker-on-ubuntu-16-04)

We will adapt that tutorial for our Azure VM example.
```sh
AzureVM$ sudo apt-get update
AzureVM$ sudo apt-get install -y mosquitto mosquitto-clients
AzureVM$ $ ps aux | grep mos
mosquit+  3103  0.0  0.1  35828  4540 ?        S    21:42   0:00 /usr/sbin/mosquitto -c /etc/mosquitto/mosquitto.conf
sdame     3165  0.0  0.0  12944  1084 pts/0    S+   21:43   0:00 grep --color=auto mos
```
Open a subscriber terminal for testing
```sh
AzureVM$ $ mosquitto_sub -h localhost -t test
=> hello MQTT world!
```

Open a publisher terminal for publishing a test message
```sh
AzureVM$ $ mosquitto_pub -h localhost -t test -m "hello MQTT world!"
```

### Step A3: Establish MQTT Password Access on Port 1883
In this step we need to both edit the MQTT configuration file to require a
username and password as well as open a port in the network security resource.

Add a new configuration file in /etc/mosquitto/conf.d (then edit)
```shsudo touch /etc/mosquitto/conf.d/mosquitto.conf
AzureVM$ sudo vim /etc/mosquitto/conf.d/mosquitto.conf
=>...
user mo
listener 1883
allow_anonymous false
password_file /etc/mosquitto/passwd
```

Setup a username ("mo" and password "squitto")

```sh
AzureVM$ sudo mosquitto_passwd -c /etc/mosquitto/passwd mo
Password: ******* (<= "squitto")
Reenter password: ******** (<= "squitto")

```


[PART B](https://gitlab.com/iot110/iot110-student/blob/master/Labs/Lab9/PartB.md)  Install MQTT Client Tool MQTT.fx

[LAB8 INDEX](https://gitlab.com/iot110/iot110-student/blob/master/Labs/Lab9/setup.md)
