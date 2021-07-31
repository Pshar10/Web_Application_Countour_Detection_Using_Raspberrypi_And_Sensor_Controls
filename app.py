from flask import Flask, render_template, Response, request, jsonify

from opencv_controller import OpenCVController
#from camera import Camera
from motor_controller import MotorController
from sensor_controller import SensorController
import time

app = Flask(__name__)
global a
motor_controller = MotorController()
opencv_controller = OpenCVController()
sensor_controller = SensorController()
should_stop_in_zone = False

@app.route('/')
def index():
    return render_template('index.html') 

def get_frame(camera):
    while True:
        frame = opencv_controller.get_frame() #remove the camera when using raspi
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')            

@app.route('/video_feed')
def video_feed():
    return Response(get_frame(opencv_controller), # replace Camera() by  opencv_controller
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/start_motor',methods=["POST"])
def start_motor():
    # ...     
    request.method== "POST"
    # clk = True
    a = opencv_controller.is_in_zone()
    motor_controller.start_motor(a)
    return jsonify({
        'success': True
        })
#dis = sensor_controller.get_distance()

@app.route('/monitor')
def monitor():

    sensor_controller.track_rod()
    #print(sensor_controller.get_distance()) 
    # t = 2
    # start_time = time.time()
    # while(int(time.time() - start_time) < t):
    a = opencv_controller.is_in_zone()
    b = sensor_controller.get_distance() #change bels
    # if a : 
    #     clk = False
    return jsonify({
        "distance": b,
        "inZone": a
    
        })
    


@app.route('/stop_system',methods=["POST"])
def stop_system():
    # ...
    request.method== "POST"
    motor_controller.stop_motor()
    # sensor_controller.track_rod() #Changed
    return { 'success': True }
    # return jsonify({
    #     'success': True,
    #    "inZone": opencv_controller.is_in_zone(),
    #    "distance": sensor_controller.get_distance()
    #     })

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

