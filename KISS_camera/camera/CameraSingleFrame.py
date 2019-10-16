import PySpin
from .Camera import Camera

class CameraSingleFrame(Camera):
    def __init__(
        self,
        serial_number=''
    ):
        Camera.__init__(
            self,
            acquisition_mode=PySpin.AcquisitionMode_SingleFrame
        )

    def __del__(self):
        Camera.__del__(self)

    def get_image(self):
        Camera.begin_acquisition(self)
        image = Camera.get_image(self)
        Camera.end_acquisition(self)
        return image