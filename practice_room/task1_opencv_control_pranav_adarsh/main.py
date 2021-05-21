from opencv_controller import OpenCVController
from camera import Camera
import time
import cv2
import numpy as np
import base64

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
#Adding few lines to detect blue zone
  blue_lower = np.array([97, 209, 145], np.uint8)
  blue_upper = np.array([102, 250, 211], np.uint8)
  blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)
#Adding lines to detect red
  red_lower = np.array([0, 183, 107], np.uint8)
  red_upper = np.array([0, 220, 161], np.uint8)
  red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)
 
 #setting up kernal

  kernal = np.ones((10, 10), "uint8")

    # For red color
  red_mask = cv2.dilate(red_mask, kernal)
  res_red = cv2.bitwise_and(img, img, 
                              mask = red_mask)
      

    # For blue color
  blue_mask = cv2.dilate(blue_mask, kernal)
  res_blue = cv2.bitwise_and(img, img,
                               mask = blue_mask)

#find the contours
  # contours, hierarchy = cv2.findContours(blue_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
  # for contour in contours:
  #     area = cv2.contourArea(contour)
  #     if(area > 1000):
  #                   cv2.drawContours(img, contour, -1, (255, 0, 0), 3) 
  #                   peri = cv2.arcLength(contour,True)
  #                   approx = cv2.approxPolyDP(contour,0.02*peri,True)

  #                   x, y, w, h = cv2.boundingRect(approx)
  #                   img = cv2.rectangle(img, (x, y),(x +w, y + h),(255, 0, 0), 3)
  #                   cv2.putText(img, "Blue Colour", (x, y),
  #                   cv2.FONT_HERSHEY_SIMPLEX, 1.0,
  #                   (255, 0, 0))

  # contours, hierarchy = cv2.findContours(red_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
  # for contour in contours:
  #     area = cv2.contourArea(contour)
  #     if(area > 1000):
  #                   cv2.drawContours(img, contour, -1, (0, 0, 255), 3) 
  #                   peri = cv2.arcLength(contour,True)
  #                   approx = cv2.approxPolyDP(contour,0.02*peri,True)

  #                   x, y, w, h = cv2.boundingRect(contour)
  #                   img = cv2.rectangle(img, (x, y),(x +w, y + h),(0, 0, 255), 3)
            
  #                   cv2.putText(img, "Red Colour", (x, y),
  #                   cv2.FONT_HERSHEY_SIMPLEX, 1.0,
  #                   (0, 0, 255))


    
  contours, hierarchy = cv2.findContours(blue_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
  for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 10000):
                    x, y, w, h = cv2.boundingRect(contour)
                    img = cv2.rectangle(img, (x, y),(x +w, y + h),(255, 0, 0), 2)
                    cv2.putText(img, "Zone", (x, y),
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
                    x1, y1, w1, h1 = cv2.boundingRect(contour)
                    img = cv2.rectangle(img, (x1, y1),(x1 +w1, y1+ h1),(0, 0, 255), 2)
            
                    cv2.putText(img, "Mark", (x1, y1),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                    (0, 0, 255))
                    if ((p+r>x1>p) or (p<x1+w1<p+r)):
                        opencv_controller.in_zone = True
                        print("Is in zone: ", opencv_controller.is_in_zone())
                        print("---------------------------------")
                    else:
                        opencv_controller.in_zone = False
                        print("Is in zone: ", opencv_controller.is_in_zone())
                        print("---------------------------------")


  cv2.imshow('image', img) 


  # print("Is in zone: ", opencv_controller.is_in_zone())
  # print("---------------------------------")
  
  cv2.waitKey(0)
  cv2.destroyAllWindows()
