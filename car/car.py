import RPi.GPIO as GPIO
from enum import Enum
from car.camera import Camera
from car.motor import Motor

from enum import Enum

class CarStatus(Enum):
    MOVING_FORWARD = 'MOVING_FORWARD'
    MOVING_BACKWARD = 'MOVING_BACKWARD'
    STOPPED = 'STOPPED'


class Car:
    def __init__(self, m1_forward, m1_backward, m2_forward, m2_backward, m3_forward, m3_backward, m4_forward, m4_backward):
        GPIO.setmode(GPIO.BCM)

        self._camera = Camera()
        self._motor1 = Motor(m1_forward, m1_backward)
        self._motor2 = Motor(m2_forward, m2_backward)
        self._motor3 = Motor(m3_forward, m3_backward)
        self._motor4 = Motor(m4_forward, m4_backward)
        self._status = CarStatus.STOPPED


    def status(self):
        return self._status.name


    def move_forward(self):
        self._motor1.move_forward()
        self._motor2.move_forward()
        self._motor3.move_forward()
        self._motor4.move_forward()
        self._status = CarStatus.MOVING_FORWARD


    def move_backward(self):
        self._motor1.move_backward()
        self._motor2.move_backward()
        self._motor3.move_backward()
        self._motor4.move_backward()
        self._status = CarStatus.MOVING_BACKWARD


    def stop(self):
        self._motor1.stop()
        self._motor2.stop()
        self._motor3.stop()
        self._motor4.stop()
        self._status = CarStatus.STOPPED


    def take_picture(self, image_filename):
        self._camera.take_picture(image_filename)
