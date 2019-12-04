
# Black Glasses - Assistente para deficientes visuais via geolocalização

William Lopes da Silva\
Orientador - Dalton Solano dos Reis\
Curso de Bacharel em Ciência da Computação\
Departamento de Sistemas e Computação
Universidade Regional de Blumenau (FURB) – Blumenau, SC – Brasil

Installation guide for the tools used in this project.

File for printing the 3D case in [arquivos_case](arquivos_case/)
![Image of Yaktocat](arquivos_case/Case_3d.png)

## Install CMUSphinx/Pocketsphinx 


The following steps show you how to test Google/Sphinx Speech Recognition using PyAudio and SpeechRecognition module on Raspberry Pi using a C-Media USB Microphone.

1 - Test USB Microphone

1.1: Use "cat /proc/asound/cards" to check if C-Media USB Microphone is listed.\
1.2 Use "alsamixer" to addjust USB Microphone gain\
1.3 Use "arecord -D sysdefault:CARD=1 -duration=10 -f cd -vv ~/mic.wav" to record something into mic.wav\
1.4 Use "aplay ./mic.wav -D sysdefault:CARD=0" to play mic.wave to verify USB Microphone works fine.

2 - Install python3-pip and SpeechRecognition module
```
sudo apt-get update
sudo apt-get install python3-pip
sudo pip3 install SpeechRecognition
```

3 - Install PyAudio
```
sudo apt-get install git
sudo git clone http://people.csail.mit.edu/hubert/git/pyaudio.git
sudo apt-get install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev
sudo apt-get install python3-dev
cd pyaudio
sudo python3 setup.py install
```

4 - Install flac which would be used by Google Speech Recognition.
```
sudo apt-get install flac
```

5 - Test PyAudio and SpeechRecognition module using Googole: Using the following python code saved in google.py and run "python3 google.py"
```
#!/usr/bin/env python3

import speech_recognition as sr

# obtain audio from the microphone

r = sr.Recognizer()
r.energy_threshold = 4000

while True:
  with sr.Microphone() as source:
	print("Say something!")
	audio = r.listen(source)
	
   try:
	print("The audio file contains: " + r.recognize_google(audio))
   except sr.UnknownValueError:
	print("Google Speech Recognition could not understand audio")
   except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
```
6 - Setup pocketsphinx

```
sudo apt-get install swig
sudo apt-get install libpulse-dev
sudo pip3 install pocketsphinx
```
7 - Test PyAudio and SpeechRecognition module using pocketsphinx: Using the following python code saved in sphinx.py and run "python3 sphinx.py"
```
#!/usr/bin/env python3

import speech_recognition as sr

# obtain audio from the microphone

r = sr.Recognizer()
r.energy_threshold = 4000

while True:
	with sr.Microphone() as source:
		print("Say something!")
		audio = r.listen(source)
	
	try: 
		print("Sphinx thinks you said " + r.recognize_sphinx(audio))
	except sr.UnknownValueError:
		print("Sphinx could not understand audio")
	except sr.RequestError as e:
		print("Sphinx error; {0}".format(e))
```

# Install  NEO-6M-GPS-Raspberry-Pi

Adapted tutorial from 
[FranzTscharf](https://github.com/FranzTscharf/Python-NEO-6M-GPS-Raspberry-Pi)\
Python script for the NEO-6M GPS module on the Raspberry Pi
## 1. Connecting Schema
![Image of Yaktocat](https://raspberrytips.nl/wp-content/uploads/2016/12/UBOLX-NEO-6M-RPI-600x274.png)
![Image of Yaktoc2at](https://www.raspberrypi-spy.co.uk/wp-content/uploads/2012/06/Raspberry-Pi-GPIO-Layout-Model-B-Plus-rotated-2700x900.png)
![Image of Yaktoc2at2](
http://www.gtkdb.de/images/00532_Raspberry_Pi_NEO-6M_GPS-Modul_-_Schaltplan.png)
## 2. Install the Dependencies
* pip installed.
```
sudo apt-get install python-pip
```
* you will need pynmea2.
```
sudo pip install pynmea2
```
* You need the GPS software
```
sudo apt-get install gpsd gpsd-clients python-gps minicom
```
## 3.1 Configurate the services - USING UART
* Serial port modify cmdline.txt:
```
sudo nano /boot/cmdline.txt
```
and replace all with the following lines:
```
dwc_otg.lpm_enable=0 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline fsck.repair=yes rootwait quiet splash plymouth.ignore-serial-consoles
```
* Change startup settings:
```
sudo nano /boot/config.txt
```
and at the end of the file add the following lines:
```
dtparam=spi=on
dtoverlay=pi3-disable-bt
core_freq=250
enable_uart=1
force_turbo=1
init_uart_baud=9600
```
* reboot the system:
```
sudo reboot now
```
* Configure the module for the 9600 rate:
```
stty -F /dev/ttyAMA0 9600
```
* Connect AMA0 to the GPS Software 
First kill the process and add the device to gpsd tool
```
sudo killall gpsd
sudo nano /etc/default/gpsd
```
Edit the file /etc/default/gpsd and add your serial port in DEVICES, like
```
DEVICES="/dev/ttyAMA0"
```
* Restart the Software
```
sudo systemctl enable gpsd.socket
sudo systemctl start gpsd.socket 
sudo cgps -s
```
## 3.2 Configurate the services - USING USB to UART CP2102
Connect CP2102 to USB

* Restart the Software

```
sudo systemctl enable gpsd.socket
sudo systemctl start gpsd.socket 
sudo cgps -s
```

Use python code:
```
serialPort = serial.Serial("/dev/ttyUSB0", 9600, timeout=0.5)

```
## 4. Run the Example
These instructions will get you a quick start with the script and please check before if you have the dependencies installed. Also connect the raspberry like the obove schemata.
* Look if the terminal output of the sensor works
```
cat /dev/ttyAMA0
```
or use:
```
cgps -s
```
* Run the script
```
cd Python-NEO-6M-GPS-Raspberry-Pi
sudo python Neo6mGPS.py
```

## 5. Example source code
```
import serial
import pynmea2
def parseGPS(str):
    if str.find('GGA') > 0:
        msg = pynmea2.parse(str)
        print "Timestamp: %s -- Lat: %s %s -- Lon: %s %s -- Altitude:
%s %s" %
(msg.timestamp,msg.lat,msg.lat_dir,msg.lon,msg.lon_dir,msg.altitude,m
sg.altitude_units)
#serialPort = serial.Serial("/dev/ttyAMA0", 9600, timeout=0.5)
#serialPort = serial.Serial("/dev/ttyUSB0", 9600, timeout=0.5)
while True:
    str = serialPort.readline()
    parseGPS(str)

```

# Install QMC5883l

tutorial from 
[RigacciOrg](https://github.com/RigacciOrg/py-qmc5883l)