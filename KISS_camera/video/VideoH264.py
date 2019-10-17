# import
import PySpin
from.Video import Video

class VideoH264(Video):
    def __init__(
        self,
        filename,
        frame_rate,
        height,
        width,
        bitrate = 1000000,
        maximum_file_size = None
    ):
        option = PySpin.H264Option()
        option.frameRate = frame_rate
        option.bitrate = bitrate
        option.height = height
        option.width = width

        Video.__init__(
            self,
            filename = filename,
            option = option,
            maximum_file_size = maximum_file_size
        )