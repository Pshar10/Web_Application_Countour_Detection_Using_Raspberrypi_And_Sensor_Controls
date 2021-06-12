from numpy.lib.function_base import _calculate_shapes
from fake_gpio import GPIO # For testing in PC
#import RPi.GPIO as GPIO # For testing in Raspberry Pi
import time
import numpy as np
class SensorController:

  def __init__(self):
    self.PIN_TRIGGER = 18 # do not change
    self.PIN_ECHO = 24 # do not change
    self.distance = None
    #print('Sensor controller initiated')

  def track_rod(self):
    # ...
    count=[]
    arr=[]
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.PIN_TRIGGER, GPIO.OUT)
    GPIO.setup(self.PIN_ECHO, GPIO.IN)
    while True: 
      GPIO.output(self.PIN_TRIGGER, GPIO.LOW)    
      #print( "Waiting for sensor to settle")
      time.sleep(2)
      #print('Monitoring')
      GPIO.output(self.PIN_TRIGGER, GPIO.HIGH)
      time.sleep(0.00001)
      GPIO.output(self.PIN_TRIGGER, GPIO.LOW)
      pulse_start_time = 0
      pulse_end_time = 0
      while GPIO.input(self.PIN_ECHO)==0:
        pulse_start_time = time.time()
      while GPIO.input(self.PIN_ECHO)==1:
        pulse_end_time = time.time()
      pulse_duration = pulse_end_time - pulse_start_time
      d = round(pulse_duration * 17150, 2)
      count= np.append(count,d)
      arr = np.append(arr,d)
      # arr = [1,1,1,1,1,1,1,1,1,1]
      if len(arr)==10:
        # print("...................................")
        if (np.std(arr)<0.5):
        # print("Kudos... you have the result")
          flag=1
        else:  
          # print("Not there yet... appending the first item in the array")
          flag=0

        if flag==0:
          if len(count)==40:
            # print(".....40 measurements done.....")
            self.distance= np.median(arr)
            break
          else: 
            arr = arr[1:10]  
    #print(len(arr))
        if flag ==1:
          # print("i am here")
          self.distance= np.mean(arr)
          break



  def get_distance(self):
    return self.distance

