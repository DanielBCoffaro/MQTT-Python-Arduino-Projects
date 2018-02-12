

import RPi.GPIO as GPIO
import paho.mqtt.publish as publish
from time import sleep     # this lets us have a time delay (see line 15)
GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering
GPIO.setup(24, GPIO.IN)    # set GPIO25 as input (button)

i=0
try:
    while True:            # this will carry on until you hit CTRL+C
        if not GPIO.input(24): # if port 25 == 1
            print "There was a SOUND:" + str(i)
           # publish.single("living_room/sound", "There was a SOUND:" + str(i) , hostname="192.168.0.107")
            sleep(0.5)
            i+=1
finally:                   # this block will run no matter how the try block exits
    GPIO.cleanup()         # clean up after yourself
