from opencv_controller import OpenCVController
from camera import Camera
import time
import cv2
import numpy as np
import base64

opencv_controller = OpenCVController()

for i in range(5):
  frame = opencv_controller.get_frame(Camera())
  
  # Display in window
  jpg_as_np = np.fromstring(frame, np.uint8)

  
  img = cv2.imdecode(jpg_as_np, cv2.COLOR_BGR2RGB)
#Converting RGB frame to HSV
  hsvFrame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#Adding few lines to detect blue zone
  blue_lower = np.array([66, 191, 153], np.uint8)
  blue_upper = np.array([109, 255, 255], np.uint8)
  blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)

  kernal = np.ones((1, 1), "uint8")

  blue_mask = cv2.dilate(blue_mask, kernal)
  res_blue = cv2.bitwise_and(img, img,
    mask = blue_mask)


  cv2.imshow('image', res_blue) #changing img and putting res_blue

  print("Is in zone: ", opencv_controller.is_in_zone())
  print("---------------------------------")
  
  cv2.waitKey(0)
  cv2.destroyAllWindows()
