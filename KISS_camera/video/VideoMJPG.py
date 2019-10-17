import PySpin
from.Video import Video

class VideoMJPG(Video):
    def __init__(
        self,
        filename,
        frame_rate,
        quality = 75,
        maximum_file_size = None
    ):
        option = PySpin.MJPGOption()
        option.frameRate = frame_rate
        option.quality = quality

        Video.__init__(
            self,
            filename = filename,
            option = option,
            maximum_file_size = maximum_file_size
        )