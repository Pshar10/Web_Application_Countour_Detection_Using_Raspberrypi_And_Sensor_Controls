# Importing the important libraries

from opencv_controller import OpenCVController
from camera import Camera
import time
import cv2
import numpy as np
import base64

#Setting the global variables

global p
global q
global r
global s

opencv_controller = OpenCVController()

for i in range(5):
  frame = opencv_controller.get_frame(Camera())
  
  # Display in window
  jpg_as_np = np.fromstring(frame, np.uint8)  
  img = cv2.imdecode(jpg_as_np, cv2.COLOR_BGR2RGB)

  #Converting RGB frame to HSV
  hsvFrame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

  # Setting Range for Blue Zone
  blue_lower = np.array([97, 209, 145], np.uint8)
  blue_upper = np.array([102, 250, 211], np.uint8)
  blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)

  #Setting Range ofr Red zone
  red_lower = np.array([0, 183, 107], np.uint8)
  red_upper = np.array([0, 220, 161], np.uint8)
  red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)
 
  #Setting up kernal(here 10*10) can also be (5*5)
  kernal = np.ones((10, 10), "uint8")

  # For red color dialting and bitwise operation to get res_red to show just red color in the frame
  red_mask = cv2.dilate(red_mask, kernal)
  res_red = cv2.bitwise_and(img, img, 
                              mask = red_mask)
      

  # For blue color dialting and bitwise operation to get res_blue to show just blue color in the frame
  blue_mask = cv2.dilate(blue_mask, kernal)
  res_blue = cv2.bitwise_and(img, img,
                               mask = blue_mask)



  # Process to find the Contours -Each individual contour is a Numpy array of (x,y) coordinates of boundary points of the object.
  
  contours, hierarchy = cv2.findContours(blue_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

  for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 10000):
                    x, y, w, h = cv2.boundingRect(contour) #given the coorddinates draw rectangle
                    img = cv2.rectangle(img, (x, y),(x +w, y + h),(255, 0, 0), 2)
                    cv2.putText(img, "Zone", (x, y),       # To put the text for the rectangle
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                    (255, 0, 0))

                    p=x
                    q=y
                    r=w
                    s=h 

   

  contours, hierarchy = cv2.findContours(red_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
  for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 5000):
                    x1, y1, w1, h1 = cv2.boundingRect(contour) #given the coorddinates draw rectangle
                    img = cv2.rectangle(img, (x1, y1),(x1 +w1, y1+ h1),(0, 0, 255), 2)
            
                    cv2.putText(img, "Mark", (x1, y1),     # To put the text for the rectangle
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                    (0, 0, 255))


                    #Applying the conditions for mark to be in zone and setting the value of variable
                    if ((p+r>x1>p) or (p<x1+w1<p+r)):
                        opencv_controller.in_zone = True
                        print("Is in zone: ", opencv_controller.is_in_zone())
                        print("---------------------------------")
                    else:
                        opencv_controller.in_zone = False
                        print("Is in zone: ", opencv_controller.is_in_zone())
                        print("---------------------------------")

  #Showing the resulting image
  cv2.imshow('image', img) 
  cv2.waitKey(0)
  cv2.destroyAllWindows()
