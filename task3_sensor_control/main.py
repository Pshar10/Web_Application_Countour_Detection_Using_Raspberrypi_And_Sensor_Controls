# import time
# from sensor_controller import SensorController

# sensor_controller = SensorController()

# for x in range(5):
#   sensor_controller.track_rod()
#   print("Distance: ", sensor_controller.get_distance())
#   time.sleep(2)


###############################################code for the main RaspberryPi##########################################################


from sensor_controller import SensorController
import numpy as np

sensor_controller = SensorController()


sensor_controller.track_rod()
print("Distance: ", sensor_controller.get_distance())