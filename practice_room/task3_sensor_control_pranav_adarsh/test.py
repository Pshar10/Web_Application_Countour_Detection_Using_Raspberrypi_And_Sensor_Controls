import time

from numpy.lib.function_base import append
from test_sensor_controller import SensorController
import numpy as np

sensor_controller = SensorController()


sensor_controller.track_rod()
print("Distance: ", sensor_controller.get_distance())
  # count= np.append(med,(sensor_controller.get_distance()))
  # arr = np.append(arr,(sensor_controller.get_distance()))
  #time.sleep(2)  
  # arr=sensor_controller.reading(arr,med)
  # print(arr)
  
