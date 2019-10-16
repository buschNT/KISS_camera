# import
import PySpin
from.Video import Video

class AVI_option:
    def __init__(
        self,
        frame_rate
    ):
        self.option = PySpin.AVIOption()
        self.option.frameRate = frame_rate

class VideoAVI(Video):
    def __init__(
        self,
        filename,
        frame_rate
    ):
        option = AVI_option(
            frame_rate = frame_rate
        )

        Video.__init__(
            self,
            filename = filename,
            option = option
        )