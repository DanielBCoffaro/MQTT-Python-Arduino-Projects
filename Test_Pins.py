
import RPi.GPIO as GPIO            # import RPi.GPIO module
from time import sleep
GPIO.setwarnings(False)             # lets us have a delay
GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
           # set GPIO24 as an output

try:
    while True:
        print("ran")
        GPIO.output(23, 1)
        GPIO.output(22, 1)
        GPIO.output(24, 0)          # set GPIO24 to 1/GPIO.HIGH/True
        sleep(3)
        GPIO.output(23, 0)
        GPIO.output(22, 0)
        GPIO.output(24, 1)
        sleep(3)
except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt
    GPIO.cleanup()
