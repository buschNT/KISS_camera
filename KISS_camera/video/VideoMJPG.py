# import
import PySpin

class MJPG_option:
    def __init__(
        self,
        frame_rate,
        quality = 75
    ):
        self.option = PySpin.MJPGOption()
        self.option.frameRate = frame_rate
        self.option.quality = quality
