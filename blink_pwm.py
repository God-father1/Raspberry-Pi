import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
p=GPIO.PWM(12,50)
p.start(0)
try: 
    while True:
        for i in range (0,50,1):
            p.ChangeDutyCycle(i)
            time.sleep(.05)
        for i in range (50,-1,-1):
            p.ChangeDutyCycle(i)
            time.sleep(.05)

except KeyboardInterrupt:
    GPIO.cleanup()
