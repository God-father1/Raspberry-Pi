import RPi.GPIO as GPIO

import time


GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(12, GPIO.OUT)
GPIO.output(12,0)

try:
    while True:
        if (GPIO.input(11) == 1):
            GPIO.output(12,1)
        else:
            GPIO.output(12,1)
            time.sleep(0.1)
            GPIO.output(12,0)
            time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()