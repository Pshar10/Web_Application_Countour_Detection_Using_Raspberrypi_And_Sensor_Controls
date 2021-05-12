import time
from sensor_controller import SensorController

sensor_controller = SensorController()

for x in range(5):
  sensor_controller.track_rod()
  print("Distance: ", sensor_controller.get_distance())
  time.sleep(2)