#import ...

class OpenCVController(object):

    def __init__(self):
        self.in_zone = False
        print('OpenCV controller initiated')

    def get_frame(self, camera):
        frame = camera.get_frame()
        # ...
        print('Monitoring')
        return frame

    def is_in_zone(self):
        
        return self.in_zone
