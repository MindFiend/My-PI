import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.output(18,GPIO.LOW)
GPIO.output(15,GPIO.LOW)
GPIO.output(14,GPIO.LOW)
GPIO.output(23,GPIO.LOW)
GPIO.output(18,GPIO.HIGH)
time.sleep(.3)
GPIO.output(18,GPIO.LOW)
time.sleep(.3)
GPIO.output(15,GPIO.HIGH)
time.sleep(.3)
GPIO.output(15,GPIO.LOW)
time.sleep(.3)
GPIO.output(14,GPIO.HIGH)
time.sleep(.3)
GPIO.output(14,GPIO.LOW)
time.sleep(.3)
GPIO.output(23,GPIO.HIGH)
time.sleep(.3)
GPIO.output(23,GPIO.LOW)
time.sleep(.3)
GPIO.output(18,GPIO.HIGH)
time.sleep(.3)
GPIO.output(18,GPIO.LOW)
time.sleep(.3)
GPIO.output(15,GPIO.HIGH)
time.sleep(.3)
GPIO.output(15,GPIO.LOW)
time.sleep(.3)
GPIO.output(14,GPIO.HIGH)
time.sleep(.3)
GPIO.output(14,GPIO.LOW)
time.sleep(.3)
GPIO.output(23,GPIO.HIGH)
time.sleep(.3)
GPIO.output(23,GPIO.LOW)
time.sleep(.3)
GPIO.output(18,GPIO.HIGH)
GPIO.output(15,GPIO.HIGH)
GPIO.output(14,GPIO.HIGH)
GPIO.output(23,GPIO.HIGH)
time.sleep(.3)
GPIO.output(18,GPIO.LOW)
GPIO.output(15,GPIO.LOW)
GPIO.output(14,GPIO.LOW)
GPIO.output(23,GPIO.LOW)
time.sleep(.3)
GPIO.output(18,GPIO.HIGH)
GPIO.output(15,GPIO.HIGH)
GPIO.output(14,GPIO.HIGH)
GPIO.output(23,GPIO.HIGH)
time.sleep(.3)
GPIO.output(18,GPIO.LOW)
GPIO.output(15,GPIO.LOW)
GPIO.output(14,GPIO.LOW)
GPIO.output(23,GPIO.LOW)
time.sleep(.3)
GPIO.output(18,GPIO.HIGH)
GPIO.output(15,GPIO.HIGH)
GPIO.output(14,GPIO.HIGH)
GPIO.output(23,GPIO.HIGH)
time.sleep(.3)
GPIO.output(18,GPIO.LOW)
GPIO.output(15,GPIO.LOW)
GPIO.output(14,GPIO.LOW)
GPIO.output(23,GPIO.LOW)
time.sleep(.3)
GPIO.output(18,GPIO.HIGH)
GPIO.output(15,GPIO.HIGH)
GPIO.output(14,GPIO.HIGH)
GPIO.output(23,GPIO.HIGH)
time.sleep(.3)
GPIO.output(18,GPIO.LOW)
GPIO.output(15,GPIO.LOW)
GPIO.output(14,GPIO.LOW)
GPIO.output(23,GPIO.LOW)
time.sleep(.3)
GPIO.output(14,GPIO.HIGH)
GPIO.output(23,GPIO.HIGH)
time.sleep(.3)
GPIO.output(14,GPIO.LOW)
GPIO.output(23,GPIO.LOW)
time.sleep(.3)
GPIO.output(15,GPIO.HIGH)
GPIO.output(18,GPIO.HIGH)
time.sleep(.3)
GPIO.output(15,GPIO.LOW)
GPIO.output(18,GPIO.LOW)
time.sleep(.3)
GPIO.output(15,GPIO.HIGH)
GPIO.output(18,GPIO.HIGH)
time.sleep(.3)
GPIO.output(15,GPIO.LOW)
GPIO.output(18,GPIO.LOW)
time.sleep(.3)
GPIO.output(14,GPIO.HIGH)
GPIO.output(18,GPIO.HIGH)
time.sleep(.3)
GPIO.output(14,GPIO.LOW)
GPIO.output(18,GPIO.LOW)
time.sleep(.3)
GPIO.output(23,GPIO.HIGH)
GPIO.output(18,GPIO.HIGH)
time.sleep(.3)
GPIO.output(23,GPIO.LOW)
GPIO.output(18,GPIO.LOW)
time.sleep(.3)
GPIO.output(15,GPIO.HIGH)
GPIO.output(14,GPIO.HIGH)
time.sleep(.3)
GPIO.output(15,GPIO.LOW)
GPIO.output(14,GPIO.LOW)
time.sleep(.3)
GPIO.output(15,GPIO.HIGH)
GPIO.output(14,GPIO.HIGH)
time.sleep(.3)
GPIO.output(15,GPIO.LOW)
GPIO.output(14,GPIO.LOW)
time.sleep(.3)
GPIO.output(23,GPIO.HIGH)
GPIO.output(18,GPIO.HIGH)
time.sleep(.3)
GPIO.output(23,GPIO.LOW)
GPIO.output(18,GPIO.LOW)
