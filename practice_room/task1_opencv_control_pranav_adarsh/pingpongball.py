from cv2 import cv2
import numpy as np

# Capturing video through webcam
webcam = cv2.VideoCapture(0)

# Start a while loop
while(1):
    global centre_x
    global centre_y
    centre_x=0
    centre_y=0 
    # Reading the video from the
    # webcam in image frames
    ret, imageFrame = webcam.read()
    # Convert the imageFrame in 
    # BGR(RGB color space) to 
    # HSV(hue-saturation-value)
    # color space
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)
        # Set range for red color and 
    # define mask
    red_lower = np.array([14, 107, 166], np.uint8)
    red_upper = np.array([62, 221, 255], np.uint8)
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)
    mask_2=cv2.inRange(hsvFrame, np.array((0.34,-0.2,0.18)), np.array((0.7,-0.32,0.17)))
    red_mask = red_mask | mask_2



    kernal = np.ones((1, 1), "uint8")

    red_mask = cv2.dilate(red_mask, kernal)
    res_red = cv2.bitwise_and(imageFrame, imageFrame, 
    mask = red_mask)

    contours, hierarchy = cv2.findContours(red_mask,
    cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 60):
                    x, y, w, h = cv2.boundingRect(contour)
                    res_red = cv2.rectangle(res_red, (x, y),(x +w, y + h),(20, 200, 168), 2)
                    centre_x= round(x+((w)/2))
                    centre_y= round(y+((h)/2))
                    centre=(centre_x,centre_y)
                    cv2.circle(res_red,centre,3,(0,0,255),2)
                    centre_x-=80
                    centre_y-=6--centre_y

                    print(centre_x,centre_y)

            
                    #cv2.putText(res_red, "green Colour", (x, y),
                    #cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                    #(0, 0, 255))

    res_re = cv2.flip(res_red,1)
    cv2.imshow("Pingpong ball", res_re) 




    if cv2.waitKey(10) & 0xFF == ord('q'):
        webcam.release()
        cv2.destroyAllWindows()
        break 