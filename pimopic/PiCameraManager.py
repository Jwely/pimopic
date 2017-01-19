import picamera
from datetime import datetime
import os


class PiCameraManager(object):
    """ This is a small camera manager object """

    def __init__(self):
        # configure the picamera
        self.camera = picamera.PiCamera()
        self.camera.brightness = 80

        # make sure it isn't already recording.
        try:
            self.camera.stop_recording()
        except: pass


        self.datetime_fmt = "%Y-%m-%d_%H-%M-%S"
        self.img_path = 'img'
        self.video_path = 'vid'
        self.video_res = (1920, 1080)
        self.image_res = (1920, 1080)

        # filepath where video is actively being stored
        self._video_path = None
        
    def _name_video(self):
        fname = os.path.join(
            self.video_path,
            "video_{}.h264".format(
                datetime.now().strftime(self.datetime_fmt)))
        return fname

    def _name_image(self):
        fname = os.path.join(
            self.img_path,
            "image_{}.jpg".format(
                datetime.now().strftime(self.datetime_fmt)))
        return fname

    def start_recording(self):
        video_path = self._name_video()
        self._video_path = video_path
        self.camera.resolution = self.video_res
        self.camera.start_recording(video_path)

    def stop_recording(self):
        self.camera.stop_recording()
        # return video path string and remove it from temp variable
        video_path = self._video_path
        self._video_path = None
        return video_path

    def capture(self):
        image_path = self._name_image()
        self.camera.resolution = self.image_res
        self.camera.capture(image_path)
        return image_path


if __name__ == "__main__":
    pc = PiCameraManager()
    pc.capture()
