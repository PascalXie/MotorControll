# A motor controll script
# for raspbian pi 3B 
# Motor : Futaba S3003

import RPi.GPIO as GPIO
import time

print("hello")

GPIO.setwarnings(False)

pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

# Initiate PWM
pwm = GPIO.PWM(pin, 50)
pwm.start(0)

# Rotate motor to 0 degree
pwm.ChangeDutyCycle(2.5)
time.sleep(1)

angle = 0
while angle<180:
    duty = 2.5 + 10.*angle/180.
    pwm.ChangeDutyCycle(duty)
    print(duty)
    time.sleep(0.3)
    angle = angle + 10

# Rotate motor to 0 degree
pwm.ChangeDutyCycle(2.5)
time.sleep(1)

GPIO.cleanup()
