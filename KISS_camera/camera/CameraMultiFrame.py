import PySpin
from .Camera import Camera

class CameraMultiFrame(Camera):
    def __init__(
        self,
        serial_number = None
    ):
        Camera.__init__(
            self,
            acquisition_mode = PySpin.AcquisitionMode_MultiFrame
        )

    def __del__(self):
        Camera.__del__(self)

    def get_image(self, N=5):
        raise NotImplementedError

        """
        image_list = [None] * N
        Camera.begin_acquisition(self)
        for n in range(N):
            print('n: %i' % n)
            image_list[n] = Camera.get_image(self)
        Camera.end_acquisition(self)
        return image_list
        """