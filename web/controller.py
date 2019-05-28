from flask import Flask
from flask_socketio import SocketIO, emit
from flask import Flask, Response, render_template
from time import sleep
import datetime
import json
from cloud.s3_service import S3Service

class Controller:
    def __init__(self, car):
        self._car = car
        self._flaskApp = Flask('robbie9')
        self._s3_service = S3Service('aclabs2019-blue')

    def index(self):
        return render_template('index.html')


    def car_status(self):
        payload = {'car-status': self._car.status()}
        response = Response(json.dumps(payload), status = 200, mimetype = 'application/json')

        return response


    def move_car_forward(self, message):
        print('Moving the car forward. Got message: ' + str(message))
        self._car.move_forward()
        emit('car_status', {'status': self._car.status()})


    def move_car_backward(self, message):
        print('Moving the car backward. Got message: ' + str(message))
        self._car.move_backward()
        emit('car_status', {'status': self._car.status()})


    def stop_car(self, message):
        print('Stopping the car. Got message: ' + str(message))
        self._car.stop()
        emit('car_status', {'status': self._car.status()})


    def take_picture(self, message):
        today = datetime.date.today()
        now = datetime.datetime.now()
        image_filename = str(today) + '_' + str(now.time()) + '.png'
        print('Taking picture: ' + image_filename)
        self._car.take_picture('static/' + image_filename)
        self._s3_service.upload('static/' + image_filename, image_filename)


    def run(self):
        self._flaskApp.config['SECRET_KEY'] = 'secret!'
        self._flaskApp.route('/')(self.index)
        self._flaskApp.route('/car-status')(self.car_status)

        socket_io = SocketIO(self._flaskApp)
        socket_io.on('car_forward', namespace = '/test')(self.move_car_forward)
        socket_io.on('car_backward', namespace = '/test')(self.move_car_backward)
        socket_io.on('car_stop', namespace = '/test')(self.stop_car)
        socket_io.on('take_picture', namespace = '/test')(self.take_picture)
        socket_io.run(self._flaskApp, host = '0.0.0.0')
