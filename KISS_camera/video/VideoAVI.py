import PySpin
from.Video import Video

class VideoAVI(Video):
    def __init__(
        self,
        filename,
        frame_rate,
        maximum_file_size = None
    ):
        option = PySpin.AVIOption()
        option.frameRate = frame_rate

        Video.__init__(
            self,
            filename = filename,
            option = option,
            maximum_file_size = maximum_file_size
        )