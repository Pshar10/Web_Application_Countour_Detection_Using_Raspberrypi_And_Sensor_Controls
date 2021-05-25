# Importing the important libraries

from opencv_controller import OpenCVController
from camera import Camera
import time
import cv2
import numpy as np
import base64
import warnings
warnings.filterwarnings("ignore",category=DeprecationWarning) #Suppressed the warning

print("\n")

opencv_controller = OpenCVController()

print("\n")

for i in range(5):
  frame = opencv_controller.get_frame(Camera())
  
#   Display in window
#   jpg_as_np = np.fromstring(frame, np.uint8)
#   img = cv2.imdecode(jpg_as_np, cv2.COLOR_BGR2RGB) #(have used them inside the calling function.)

  cv2.imshow('image', frame)
  print("Is in zone: ", opencv_controller.is_in_zone())
  print("---------------------------------")

  cv2.waitKey(0)
  cv2.destroyAllWindows()


  

