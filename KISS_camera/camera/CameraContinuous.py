import PySpin
from .Camera import Camera

class CameraContinuous(Camera):
    def __init__(
        self,
        serial_number = None
    ):
        Camera.__init__(
            self,
            acquisition_mode = PySpin.AcquisitionMode_Continuous,
            serial_number = serial_number
        )

        Camera.begin_acquisition(self)
    
    def __del__(self):
        Camera.end_acquisition(self)
        Camera.__del__(self)

    def get_image(self):
        image = Camera.get_image(self)
        return image