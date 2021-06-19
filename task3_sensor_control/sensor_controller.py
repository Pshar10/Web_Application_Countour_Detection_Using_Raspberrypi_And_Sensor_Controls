
# Importing important libraries
from fake_gpio import GPIO  #For testing in PC
#import RPi.GPIO as GPIO    #For testing in Raspberry Pi
import time
import numpy as np




class SensorController:

  def __init__(self):
    self.PIN_TRIGGER = 18 # do not change
    self.PIN_ECHO = 24 # do not change
    self.distance = None
    #print('Sensor controller initiated')

  def track_rod(self):

    count=[]  #Taking the empty arrays for calculations : Count- counts total values
    arr=[]    #Taking the empty arrays for calculations : arr- helps on calculating main operations

    GPIO.setmode(GPIO.BCM)    #Broadcom SOC channel

    GPIO.setup(self.PIN_TRIGGER, GPIO.OUT)    #Setting Pin trigger as Output 
    GPIO.setup(self.PIN_ECHO, GPIO.IN)    #setting Pin echo as Input

# Starting an infinite loop

    while True: 
      GPIO.output(self.PIN_TRIGGER, GPIO.LOW)    #  Settling the Sensor 
      time.sleep(2)
      #print('Monitoring')
      GPIO.output(self.PIN_TRIGGER, GPIO.HIGH)   #  Sending the pulse
      time.sleep(0.00001)
      GPIO.output(self.PIN_TRIGGER, GPIO.LOW)
      pulse_start_time = 0
      pulse_end_time = 0
      while GPIO.input(self.PIN_ECHO)==0:   #  Reading the echo pin
        pulse_start_time = time.time()
      while GPIO.input(self.PIN_ECHO)==1:   #  Reading the echo pin
        pulse_end_time = time.time()
      pulse_duration = pulse_end_time - pulse_start_time #Calculating the time for the pulse
      d = round(pulse_duration * 17150, 2)  # calculating distance
      print("Distance : ",d)

# Calculation part

      count= np.append(count,d)  #  Putting values of distance in the count
      arr = np.append(arr,d)
      print(len(count)) 
      print(arr)   #  Putting values of distance in the arr
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
            self.distance= np.median(arr) #  Calculate the median
            break
          else: 
            arr = arr[1:10]  
    #print(len(arr))
        if flag ==1:
          self.distance= np.mean(arr) # Calculate the mean
          break



  def get_distance(self):
    return self.distance

