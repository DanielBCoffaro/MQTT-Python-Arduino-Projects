
import RPi.GPIO as GPIO
from time import sleep
import paho.mqtt.publish as publish

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

GPIO.output(22, 0) # Lock
on_off=False
for x in range(6):
    GPIO.output(23,on_off) # Yellow Led
    on_off=not on_off
    GPIO.output(24,on_off) # Green Led
    sleep(.5)
#publish.single("LockBox", "It was locked", hostname="192.168.0.107")
#thebox="locked"
try:
    while True:
        if GPIO.input(14):
            #try:
            #    if thebox=="locked":
            #           publish.single("LockBox", "It was unlocked", hostname="192.168.0.107")
                #       thebox="unlocked"
            #except:
            #    print("error with MQQT")
            GPIO.output(24, 1)
            GPIO.output(22, 0)
            GPIO.output(23, 0)
        if not GPIO.input(14):
            #try:
                #if thebox=="unlocked":
                 #       publish.single("LockBox", "It was locked", hostname="192.168.0.107")
                #       thebox="locked"
            #except:
             #   print("error with MQQT")
            GPIO.output(24, 0)
            GPIO.output(22, 1)
            GPIO.output(23, 1)

finally:          # trap a CTRL+C keyboard interrupt
    GPIO.cleanup()
