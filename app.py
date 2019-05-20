import RPi.GPIO as GPIO
from time import sleep
from car.car import Car
from web.controller import Controller

if __name__ == '__main__':
    # print('Running Robbie9 application ...')
    car = Car(17, 18, 22, 23, 5, 6, 12, 13)
    controller = Controller(car)

    try:
        controller.run()
    finally:
        print('Cleaning up GPIO...')
        GPIO.cleanup()
