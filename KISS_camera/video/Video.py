# import
import PySpin

class AVI_option:
    def __init__(
        self,
        frame_rate
    ):
        # option
        self.option = PySpin.AVIOption()
        self.option.frameRate = frame_rate

class MJPG_option:
    def __init__(
        self,
        frame_rate,
        quality = 75
    ):
        self.option = PySpin.MJPGOption()
        self.option.frameRate = frame_rate
        self.option.quality = quality

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

class Video:
    def __init__(
        self,
        option,
        filename = ''
    ):
        # option
        self.option = option

        # create recorder
        self.avi_recorder = PySpin.SpinVideo()

        # open file
        self.open_file(
            filename = filename,
            option = option
        )

    def open_file( self, filename, option ):
        self.avi_recorder.Open( filename, option.option )
    
    def add_image( self, image ):
        try:
            self.avi_recorder.Append( image )
        except PySpin.SpinnakerException as e:
            print( 'error: %s' % e )
            return False
        return True
    
    def close_file( self ):
        self.avi_recorder.Close()

    def __del__( self ):
        try:
            self.close_file()
        except:
            pass