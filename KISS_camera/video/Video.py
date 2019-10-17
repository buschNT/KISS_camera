import os
import PySpin

class Video:
    def __init__(
        self,
        filename,
        option,
        maximum_file_size = None
    ):
        # check & create path
        filename = os.path.splitext(filename)[0] # file extensions are added by SpinVideo
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError:
            pass

        # create recorder
        self.spin_video = PySpin.SpinVideo()

        # set maximum_file_size
        if(maximum_file_size is not None):
            self.spin_video.SetMaximumFileSize(maximum_file_size)

        # open file
        self.spin_video.Open(filename, option)

    def __del__( self ):
        try:
            self.spin_video.Close()
        except:
            pass

    def __check_filename(self, filename, extension):
        # TODO: base on option type
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
            self.spin_video.Append(image.image)
        except PySpin.SpinnakerException as e:
            print(e)
            return False
        return True
