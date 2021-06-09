import time

from numpy.lib.function_base import append
from sensor_controller import SensorController
import numpy as np

sensor_controller = SensorController()
arr=[]
med=[]
mean=0
f=1
for x in range(100):
  sensor_controller.track_rod()
  print("Distance: ", sensor_controller.get_distance())
  med= np.append(med,(sensor_controller.get_distance()))
  arr = np.append(arr,(sensor_controller.get_distance()))
  print(arr)
  #time.sleep(2)  
  flag=sensor_controller.reading(arr)
  # print(flag)
  if flag==0:
    if len(med)==40:
      print(".....40 measurements done.....")
      break
    else: 
      arr = arr[1:11]
    #print(len(arr))
  if flag ==1:
    print("mean of arr : ", np.mean(arr))
    break

  
print(arr)  
median = np.median(med)
print(median)
