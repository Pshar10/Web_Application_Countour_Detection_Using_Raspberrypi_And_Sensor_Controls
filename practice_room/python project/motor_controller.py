from fake_gpio import GPIO
import time # For testing in PC
from opencv_controller import OpenCVController
from flask import Flask, render_template, Response, request, jsonify
# import RPi.GPIO as GPIO # For testing in Raspberry Pi
# import ...

class MotorController(object):

  def __init__(self):
    self.working = False

    
  def is_working(self):   #was at last of the code changed the postitn
    return self.working

  def start_motor(self):

    #pin definition
    self.PIN_STEP = 25 # do not change
    self.PIN_DIR = 8 # do not change
    self.working = True
    SPR = 200 # 1 step = 0.225 degree  and we have to rotate for 45 degrees
    # CW=1 # clockwise
    # CCW=0 #anti clockwise
    # ...
    #print('Motor working status: Started') # showing status of motor to started

    # PIN SETUP MODE
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.PIN_DIR, GPIO.OUT)
    GPIO.setup(self.PIN_STEP, GPIO.OUT)
    cnt = 0
    while(True):
      cnt = cnt+1
      print("Starting to rotate in clockwise direction for 45 degrees")

    # Motor direction setup Clockwise
      GPIO.output(self.PIN_DIR,GPIO.LOW)
      step_count = SPR
      delay = 0.005
      print(self.working)
      for x in range(step_count):
        GPIO.output(self.PIN_STEP,GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(self.PIN_STEP,GPIO.LOW)
      print("Motor has rotated clockwise for 45 degrees")
      time.sleep(0.5)

   
   
      print("Aiming for 75 degrees")

      step_count = 333 # for 30 degree more rotation

      for x in range(step_count):
        GPIO.output(self.PIN_STEP,GPIO.HIGH)
        time.sleep(0.003)
        GPIO.output(self.PIN_STEP,GPIO.LOW)

      print("Motor has rotated clockwise for 75 degrees now changing the direction ")
      time.sleep(0.5)


    # Motor direction setup AntiClockwise
      print("Motor Started rotating 45 degree anticlockwise")
      GPIO.output(self.PIN_DIR,GPIO.HIGH)
      step_count = SPR
      delay = 0.005
      for x in range(step_count):
        GPIO.output(self.PIN_STEP,GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(self.PIN_STEP,GPIO.LOW)
      print("Motor has rotated anti-clockwise for 45 degrees")
      print(".....................................................")
      print(cnt," cycle complete")

      time.sleep(0.5)

      if (cnt == 2):
        break
      
      if (self.working == False):
        break

    #print("Motor Working Status: Stopped") ## showing status of motor to started
    # print(self.working)

  def stop_motor(self):

    #pin definition
    self.PIN_STEP = 25 # do not change
    self.PIN_DIR = 8 # do not change
    self.working = False
    
    # PIN SETUP MODE
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.PIN_DIR, GPIO.OUT)
    GPIO.setup(self.PIN_STEP, GPIO.OUT)
    
    # Setting stepper pin low
    GPIO.output(self.PIN_STEP,GPIO.LOW)


