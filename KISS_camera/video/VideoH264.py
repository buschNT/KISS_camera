# import
import PySpin

class H264_option:
    def __init__(
        self,
        frame_rate,
        height,
        width,
        bitrate = 1000000
    ):
        option = PySpin.H264Option()
        option.frameRate = frame_rate
        option.bitrate = bitrate
        option.height = height
        option.width = width