import cv2
import numpy as np #used here for dealing with different arrays

#uncomment below libraries in case of real use
# import io
# import time
# from picamera.array import PiRGBArray
# from picamera import PiCamera
# time.sleep(0.1)
# camera = PiCamera()
# camera.resolution = (640, 480)
# camera.framerate = 32
# rawCapture = PiRGBArray(camera, size=(640, 480))

class OpenCVController(object):

    def __init__(self):  #used here to define all the instances   
        self.in_zone = False
        print('OpenCV controller initiated') 

    def get_frame(self, camera):
       
  # Starting the code

        frame = camera.get_frame()
        jpg_as_np = np.fromstring(frame, np.uint8)  
        img = cv2.imdecode(jpg_as_np, cv2.COLOR_BGR2RGB)       

  # Converting RGB frame to HSV
        hsvFrame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

  # Setting Range for Blue Zone
        blue_lower = np.array([97, 209, 145], np.uint8)
        blue_upper = np.array([102, 250, 211], np.uint8)
        blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)

  # Setting Range for Red zone
        red_lower = np.array([0, 183, 107], np.uint8)
        red_upper = np.array([0, 220, 161], np.uint8)
        red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)
  




  # Setting up kernal(here 10*10) can also be (5*5)
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
  
        contours, hierarchy = cv2.findContours(blue_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #CHAIN_APPROX_SIMPLE is used to remove all the redundant points, RETR_TREE retrieves all the contours

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

  # Applying the conditions for mark to be in zone and setting the value of variable
                    if ((p+r>x1>p) or (p<x1+w1<p+r)):

                        self.in_zone = True

                    else:
                        self.in_zone = False



        #print('Monitoring')
        
        #return img
        ret, jpeg = cv2.imencode('.jpg', img)
        return jpeg.tobytes()

    def is_in_zone(self):
        
        return self.in_zone


#################################################          Replace in case of real raspi            ###############################################################


# def get_frame(self):
#         for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
#             frame = frame.array
#             img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#             hsvFrame = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#             blue_lower = np.array([97, 209, 145], np.uint8)
#             blue_upper = np.array([102, 250, 211], np.uint8)
#             blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)

#   # Setting Range for Red zone
#             red_lower = np.array([0, 183, 107], np.uint8)
#             red_upper = np.array([0, 220, 161], np.uint8)
#             red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)
  




#   # Setting up kernal(here 10*10) can also be (5*5)
#             kernal = np.ones((10, 10), "uint8")

#   # For red color dialting and bitwise operation to get res_red to show just red color in the frame
#             red_mask = cv2.dilate(red_mask, kernal)
#             res_red = cv2.bitwise_and(img, img, 
#                               mask = red_mask)
      

#   # For blue color dialting and bitwise operation to get res_blue to show just blue color in the frame
#             blue_mask = cv2.dilate(blue_mask, kernal)
#             res_blue = cv2.bitwise_and(img, img,
#                                mask = blue_mask)



#   # Process to find the Contours -Each individual contour is a Numpy array of (x,y) coordinates of boundary points of the object.
  
#             contours, hierarchy = cv2.findContours(blue_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #CHAIN_APPROX_SIMPLE is used to remove all the redundant points, RETR_TREE retrieves all the contours

#             for pic, contour in enumerate(contours):
#                 area = cv2.contourArea(contour)
#                 if(area > 10000):
#                     x, y, w, h = cv2.boundingRect(contour) #given the coorddinates draw rectangle
#                     img = cv2.rectangle(img, (x, y),(x +w, y + h),(255, 0, 0), 2)
#                     cv2.putText(img, "Zone", (x, y),       # To put the text for the rectangle
#                     cv2.FONT_HERSHEY_SIMPLEX, 1.0,
#                     (255, 0, 0))

#                     p=x
#                     q=y
#                     r=w
#                     s=h 

   

#             contours, hierarchy = cv2.findContours(red_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#             for pic, contour in enumerate(contours):
#                 area = cv2.contourArea(contour)
#                 if(area > 5000):
#                     x1, y1, w1, h1 = cv2.boundingRect(contour) #given the coorddinates draw rectangle
#                     img = cv2.rectangle(img, (x1, y1),(x1 +w1, y1+ h1),(0, 0, 255), 2)
            
#                     cv2.putText(img, "Mark", (x1, y1),     # To put the text for the rectangle
#                     cv2.FONT_HERSHEY_SIMPLEX, 1.0,
#                     (0, 0, 255))

#   # Applying the conditions for mark to be in zone and setting the value of variable
#                     if ((p+r>x1>p) or (p<x1+w1<p+r)):
    
#                             self.in_zone = True
    
#                     else:
#                             self.in_zone = False

#             rawCapture.truncate(0)
        
#             ret, jpeg = cv2.imencode('.jpg', img)
#             return jpeg.tobytes()