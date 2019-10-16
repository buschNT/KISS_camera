# import
import PySpin

class Video:
    def __init__(
        self,
        filename,
        option,
        maximum_file_size = None
    ):
        # create recorder
        self.avi_recorder = PySpin.SpinVideo()

        # set maximum_file_size
        if(maximum_file_size is not None):
            self.avi_recorder.SetMaximumFileSize(maximum_file_size)

        # open file
        self.avi_recorder.Open( filename, option.option )

    def __del__( self ):
        try:
            self.avi_recorder.Close()
        except:
            pass

    def __check_filename(self, filename, extension):
        # check extension
        if(not filename.endswith(extension)):
            filename += extension[0]
        
        # check & create path
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError:
            pass

        return filename

    def add_image(self, image):
        try:
            self.avi_recorder.Append(image.image)
        except PySpin.SpinnakerException as e:
            print(e)
            return False
        return True
