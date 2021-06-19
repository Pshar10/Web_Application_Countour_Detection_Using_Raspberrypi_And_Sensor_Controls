import time

from numpy.lib.function_base import append
from sensor_controller import SensorController
import numpy as np

sensor_controller = SensorController()
arr=[]
count=[]
p=[]
mean=0
f=1
flag = 8
for x in range(100):
  sensor_controller.track_rod()
  print("Distance: ", sensor_controller.get_distance())
  count= np.append(count,(round(sensor_controller.get_distance())))
  arr = np.append(arr,(sensor_controller.get_distance()))
  print(arr)
  print(len(count))
  #time.sleep(2)  
  # flag=sensor_controller.reading(arr,count)
  if len(arr)==5:
    print("...................................")
    if (np.std(arr)<0.5):
      print("Kudos... you have the result")
      flag=1
    else:  
      print("Not there yet... appending the first item in the array")
      flag=0
  # print(flag)
  if flag==0:
    if len(count)==10:
      print(".....10 measurements done.....")
      print("Median of arr : ", np.median(arr))
      break
    else: 
      arr = arr[1:5]
    #print(len(arr))
  if flag ==1:
    print("Mean of arr : ",np.mean(arr))
    break

