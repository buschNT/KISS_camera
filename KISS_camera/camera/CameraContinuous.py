import PySpin
from .Camera import Camera

class CameraContinuous(Camera):
    def __init__(
        self,
        serial_number=''
    ):
        Camera.__init__(
            self,
            acquisition_mode=PySpin.AcquisitionMode_Continuous
        )

        Camera.begin_acquisition(self)
    
    def __del__(self):
        Camera.end_acquisition(self)
        Camera.__del__(self)

    def get_image(self):
        image = Camera.get_image(self)
        return image