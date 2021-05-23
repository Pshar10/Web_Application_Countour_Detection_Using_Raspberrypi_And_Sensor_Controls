import cv2
import numpy as np

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        hsvFrame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)  
        blue_lower = np.array([44, 90, 130], np.uint8)
        blue_upper = np.array([124, 246, 236], np.uint8)
        blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)
        red_lower = np.array([148, 89, 130], np.uint8)
        red_upper = np.array([172, 188, 165], np.uint8)
        red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)


    
        kernal = np.ones((10, 10), "uint8")

        # For blue color
        blue_mask = cv2.dilate(blue_mask, kernal)
        res_blue = cv2.bitwise_and(image, image,
                               mask = blue_mask)
        # For red color
        red_mask = cv2.dilate(red_mask, kernal)
        res_red = cv2.bitwise_and(image, image, 
                              mask = red_mask)                           

        contours, hierarchy = cv2.findContours(blue_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if(area > 10000):
                    x, y, w, h = cv2.boundingRect(contour)
                    image = cv2.rectangle(image, (x, y),(x +w, y + h),(255, 0, 0), 2)
                    cv2.putText(image, "Zone", (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                    (255, 0, 0))
            break
    
        contours, hierarchy = cv2.findContours(red_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if(area > 500):
                    x1, y1, w1, h1 = cv2.boundingRect(contour)
                    img = cv2.rectangle(image, (x1, y1),(x1 +w1, y1+ h1),(0, 0, 255), 2)
            
                    cv2.putText(image, "Mark", (x1, y1),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                    (0, 0, 255))
    
            break

        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
