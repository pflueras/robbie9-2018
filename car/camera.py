from picamera import PiCamera
from time import sleep

class Camera:
    def __init__(self):
        self.camera = PiCamera(resolution = (1920, 1080))
        self.camera.rotation = 270


    def take_picture(self, image_filename):
        """ Take a new picture and save it to image_filename location.
        """
        self.camera.start_preview()
        sleep(2)
        self.camera.capture(image_filename)
        self.camera.stop_preview()
