from fake_gpio import GPIO # For testing in PC
# import RPi.GPIO as GPIO # For testing in Raspberry Pi
# import ...

class MotorController(object):

  def __init__(self):
    self.working = False

  def start_motor(self):
    self.PIN_STEP = 25 # do not change
    self.PIN_DIR = 8 # do not change
    self.working = True
    # ...
    print('Motor started')

  def is_working(self):
    return self.working