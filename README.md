# MQTT-Python-Arduino-Projects
Intro Project to using MQTT with Python


Humidty_Temp.py: This project reads temperature and humidity sensors as well as using the Astral module to determine sunset and sunrise. It then publishes this data to and LCD screen.

LockBox.py: This project is a puzzle box. The software portion determines if the puzzle has been solved and if so unlocks the box by activating a transistor hooked to a solonoid. The software also has capablility to send information to a MQTT server when the box is locked or unlocked

Sound_Detector.py: Uses and arduino sound sensor to determine if a sound has occoured and publishes that to an MQTT server.

Test_Pins.py: used to determine it the LockBox was working, and how to setup pins.
