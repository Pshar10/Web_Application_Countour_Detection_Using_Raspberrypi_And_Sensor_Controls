# Please note that this is a fake camera, it will just 
# yield the images 1.jpg, 2.jpg, 3.jg and 4.jpg. It is
# just for testing purposes. You should actually use the
# picamera module and implement the get_frame properly  

from time import time
from imutils.video.pivideostream import PiVideoStream
import imutils
import os, sys
import numpy as np


class Camera(object):
    def __init__(self):
        directory = os.path.join(os.path.dirname(__file__), 'test_frames')
        self.test_frames_name = ['1.jpg', '2.jpg', '3.jpg', '4.jpg']
        self.frames = [open(os.path.join(directory, f), 'rb').read() for f in self.test_frames_name]

    def get_frame(self):
        random_index = int(time()) % 4
        print('Frame', self.test_frames_name[random_index])
        return self.frames[random_index]