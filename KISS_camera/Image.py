import os
import PySpin

# static
def create(*args):
    return PySpin.Image_Create(*args)

def get_default_color_processing():
    return PySpin.Image_GetDefaultColorProcessing()

def get_image_status_description(status):
    return PySpin.Image_GetImageStatusDescription(status)

def set_default_color_processing(default_method):
    PySpin.Image_SetDefaultColorProcessing(default_method)


class Image:
    def __init__(self, image):
        self.image = image
    
    def __del__(self):
        try:
            self.release()
        except:
            pass

    def convert_to_numpy(self):
        image_numpy = self.image.GetNDArray()
        return image_numpy

    def __save_check_filename(self, filename, extension):
        # check extension
        if(not filename.endswith(extension)):
            filename += extension[0]
        
        # check & create path
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError:
            pass

        return filename

    def save_as_pgm(self, filename):
        self.save(
            self.__save_check_filename(filename, ('.pgm', )),
            format=PySpin.PGM
        )

    def save_as_ppm(self, filename):
        self.save(
            self.__save_check_filename(filename, ('.ppm', )),
            format=PySpin.PPM
        )

    def save_as_bmp(self, filename):
        self.save(
            self.__save_check_filename(filename, ('.bmp', '.dib')),
            format=PySpin.BMP
        )

    def save_as_jpeg(self, filename):
        self.save(
            self.__save_check_filename(filename, ('.jpeg', 'jpg')),
            format=PySpin.JPEG
        )

    def save_as_jpeg2000(self, filename):
        self.save(
            self.__save_check_filename(filename, ('.jp2', '.j2k', '.jpf', '.jpg2', '.jpx', '.jpm', '.mj2', '.mjp2')),
            format=PySpin.JPEG2000
        )

    def save_as_tiff(self, filename):
        self.save(
            self.__save_check_filename(filename, ('.tiff', '.tif')),
            format=PySpin.TIFF
        )

    def save_as_png(self, filename):
        self.save(
            self.__save_check_filename(filename, ('.png', )),
            format=PySpin.PNG
        )

    def save_as_raw(self, filename):
        self.save(
            self.__save_check_filename(filename, ('.raw', )),
            format=PySpin.RAW
        )

    def save_as_jpeg12_c(self, filename):
        self.save(
            self.__save_check_filename(filename, ('.jpeg12_c', )),
            format=PySpin.JPEG12_C
        )

    ## spinnaker functions
    def calculate_channel_statistics(self):
        raise NotImplementedError

    def check_CRC(self):
        return self.image.CheckCRC()

    def convert(
        self,
        format=PySpin.PixelFormat_Mono8,
        algorithm=PySpin.HQ_LINEAR
    ):
        image_converted = self.image.Convert(format, algorithm)
        return Image(image_converted)

    def deep_copy(self):
        image_p = create(self.image)
        self.image.DeepCopy(image_p)
        return Image(image_p)

    def get_bits_per_pixel(self):
        return self.image.GetBitsPerPixel()

    def get_buffer_size(self):
        return self.image.GetBufferSize()

    def get_chunk_data(self):
        raise NotImplementedError

    def get_chunk_layout_id(self):
        raise NotImplementedError

    def get_color_processing(self):
        return self.image.GetColorProcessing()

    def get_frame_ID(self):
        return self.image.GetFrameID()

    def get_height(self):
        return self.image.GetHeight()

    def get_ID(self):
        return self.image.GetID()

    def get_image_size(self):
        return self.image.GetImageSize()

    def get_image_status(self):
        return self.image.GetImageStatus()

    def get_num_channels(self):
        return self.image.GetNumChannels()

    def get_get_payload_type(self):
        return self.image.GetPayloadType()

    def get_pixel_format(self):
        return self.image.GetPixelFormat()

    def get_pixel_format_int_type(self):
        return self.image.GetPixelFormatIntType()

    def get_pixel_format_name(self):
        return self.image.GetPixelFormatName()

    # spinnaker: no way to set private data for image yet.
    #def get_private_data(self):
    #    raise NotImplementedError

    def get_stride(self):
        return self.image.GetStride()

    def get_TL_payload_type(self):
        raise NotImplementedError

    def get_TL_pixel_format(self):
        return self.image.GetTLPixelFormat()

    def get_TL_pixel_format_namespace(self):
        raise NotImplementedError

    def get_time_stamp(self):
        return self.image.GetTimeStamp()

    def get_valid_payload_size(self):
        return self.image.GetValidPayloadSize()

    def get_width(self):
        return self.image.GetWidth()

    def get_X_offset(self):
        return self.image.GetXOffset()

    def get_X_padding(self):
        return self.image.GetXPadding()

    def get_Y_offset(self):
        return self.image.GetYOffset()

    def get_Y_padding(self):
        return self.image.GetYPadding()

    def has_CRC(self):
        return self.image.hasCRC()

    def is_in_use(self):
        return self.image.IsInUse()

    def is_incomplete(self):
        return self.image.IsIncomplete()

    def release(self):
        self.image.Release()

    def reset_image(
        self,
        width,
        height,
        offset_X,
        offset_Y,
        pixel_format
    ):
        raise NotImplementedError

    def save(self, filename, format=PySpin.FROM_FILE_EXT):
        # check & create path
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError:
            pass

        self.image.Save(filename, format)
