import RPi.GPIO as GPIO
from time import sleep

M1_FORWARD = 17
M1_BACKWARD = 18

M2_FORWARD = 22
M2_BACKWARD = 23

M3_FORWARD = 5
M3_BACKWARD = 6

M4_FORWARD = 12
M4_BACKWARD = 13

try:
    # for GPIO numbering, choose BCM
    GPIO.setmode(GPIO.BCM)
    GPIO.setup([M1_FORWARD, M1_BACKWARD, M2_FORWARD, M2_BACKWARD, M3_FORWARD, M3_BACKWARD, M4_FORWARD, M4_BACKWARD, ], GPIO.OUT)

    GPIO.output(M1_FORWARD, GPIO.LOW)
    GPIO.output(M1_BACKWARD, GPIO.LOW)

    GPIO.output(M2_FORWARD, GPIO.LOW)
    GPIO.output(M2_BACKWARD, GPIO.LOW)

    GPIO.output(M3_FORWARD, GPIO.LOW)
    GPIO.output(M3_BACKWARD, GPIO.LOW)

    GPIO.output(M4_FORWARD, GPIO.LOW)
    GPIO.output(M4_BACKWARD, GPIO.LOW)

    print('Setup complete. Preparing to run the engine...')
    sleep(1)

    GPIO.output(M1_FORWARD, GPIO.HIGH)
    GPIO.output(M1_BACKWARD, GPIO.LOW)

    GPIO.output(M2_FORWARD, GPIO.HIGH)
    GPIO.output(M2_BACKWARD, GPIO.LOW)

    GPIO.output(M3_FORWARD, GPIO.HIGH)
    GPIO.output(M3_BACKWARD, GPIO.LOW)

    GPIO.output(M4_FORWARD, GPIO.HIGH)
    GPIO.output(M4_BACKWARD, GPIO.LOW)
    print('Engine is running...')
    sleep(2)

    # Reset the engine
    GPIO.output(M1_FORWARD, GPIO.LOW)
    GPIO.output(M1_BACKWARD, GPIO.LOW)

    GPIO.output(M2_FORWARD, GPIO.LOW)
    GPIO.output(M2_BACKWARD, GPIO.LOW)

    GPIO.output(M3_FORWARD, GPIO.LOW)
    GPIO.output(M3_BACKWARD, GPIO.LOW)

    GPIO.output(M4_FORWARD, GPIO.LOW)
    GPIO.output(M4_BACKWARD, GPIO.LOW)
finally:
    GPIO.cleanup()
