from ..System import System, PySpin
from ..Image import Image

class IMAGE_DATATYPE:
    NUMPY = 0
    IMAGE = 1

class Camera:
    # settings
    #acquisition_mode = ACQUISITION_MODE.CONTINUOUS
    color_processing_algorithm = PySpin.HQ_LINEAR
    pixel_format = PySpin.PixelFormat_RGB8
    image_datatype = IMAGE_DATATYPE.NUMPY

    # status variable
    status_acquisition = False

    def __init__(
        self,
        acquisition_mode,
        index = 0,
        serial_number = None,
        system = None,
        image_datatype = IMAGE_DATATYPE.NUMPY
    ):
        # create system instance if not provided
        self.system = None
        if( system is None ):
            self.system = System()
        
        # get camera handle
        self.camera = self.system.get_camera_by_index( index )
        if( self.camera is None ):
            raise ValueError( 'index: not found' )

        # retrieve TL device nodemap
        self.nodemap_GetTLDevice = self.camera.GetTLDeviceNodeMap()

        # initialize camera
        self.camera.Init()

        # retrieve GenICam nodemap
        self.nodemap_GenICam = self.camera.GetNodeMap()

        # set aquisition mode
        self.set_acquisition_mode(acquisition_mode)

        # set pixel format
        self.set_pixel_format()

        # set image_datatype
        self.image_datatype = image_datatype
            
    def __del__( self ):
        # end acquisition if still runing
        if( self.status_acquisition == True ):
            self.end_acquisition()
        
        # deinitialize camera
        if( self.camera is not None ):
            self.camera.DeInit()

        # release camera
        if( self.camera is not None ):
            del self.camera

        # release system if initiated by instance
        if( self.system is not None ):
            del self.system
    
    def begin_acquisition( self ):
        self.camera.BeginAcquisition()
        self.status_acquisition = True

    def end_acquisition( self ):
        self.camera.EndAcquisition()
        self.status_acquisition = False
    
    def is_acquiring(self):
        pass
        
    def get_image( self ):
        try:
            # retrieve next received image
            image_next = self.camera.GetNextImage()

            # ensure image completion
            if( image_next.IsIncomplete() ):
                print( "Image incomplete with image status %d ..." % image_next.GetImageStatus() )
                return False
            
            # converted image does not affect the camera buffer (no release required)
            image = image_next.Convert(
                self.pixel_format,
                self.color_processing_algorithm
            )

            # release image
            image_next.Release()
        except Exception as e:
            print( e )
            return False 
        
        return Image(image)

    """
    def __image_datatype_conversion( self, image ):
        # image data type conversion
        lambda_numpy = lambda image : image.GetNDArray()

        datatype_conversion = {
            IMAGE_DATATYPE.NUMPY: lambda_numpy,
            IMAGE_DATATYPE.IMAGE: lambda image : image,
        }.get( self.image_datatype, lambda_numpy )

        img = datatype_conversion( image )

        # release image if datatype has been converted
        if( self.image_datatype != IMAGE_DATATYPE.IMAGE ):
            del image
        
        return img
    """

    def set_acquisition_mode( self, acquisition_mode ):
        # In order to access the node entries, they have to be casted to a pointer type (CEnumerationPtr here)
        node_acquisition_mode = PySpin.CEnumerationPtr( self.nodemap_GenICam.GetNode( "AcquisitionMode" ) )
        if not PySpin.IsAvailable( node_acquisition_mode ) or not PySpin.IsWritable( node_acquisition_mode ):
            print( "Unable to set acquisition mode to continuous (enum retrieval). Aborting..." )
            return False

        """
        # Retrieve entry node from enumeration node
        node_acquisition_mode_continuous = node_acquisition_mode.GetEntryByName( "Continuous" )
        if not PySpin.IsAvailable( node_acquisition_mode_continuous ) or not PySpin.IsReadable( node_acquisition_mode_continuous ):
            print( "Unable to set acquisition mode to continuous (entry retrieval). Aborting..." )
            return False

        # Retrieve integer value from entry node
        acquisition_mode_continuous = node_acquisition_mode_continuous.GetValue()
        #acquisition_mode_continuous = PySpin.AcquisitionMode_MultiFrame
        #print( 'acquisition_mode_continuous: ', acquisition_mode_continuous )
        """
        

        # Set integer value from entry node as new value of enumeration node
        node_acquisition_mode.SetIntValue(acquisition_mode)

        return True
    
    def set_pixel_format(self):
        # image format setup
        node_pixel_format = PySpin.CEnumerationPtr( self.nodemap_GenICam.GetNode("PixelFormat"))

        # Retrieve entry node from enumeration node
        node_pixel_format_rgb8 = PySpin.CEnumEntryPtr(node_pixel_format.GetEntryByName("RGB8"))
        if not PySpin.IsAvailable(node_pixel_format_rgb8) or not PySpin.IsReadable(node_pixel_format_rgb8):
            print("Unable to set Pixel Format to RGB8. Aborting...")
            return False

        # Retrieve integer value from entry node
        pixel_format_rgb8 = node_pixel_format_rgb8.GetValue()

        # Set integer value from entry node as new value of enumeration node
        node_pixel_format.SetIntValue(pixel_format_rgb8)

        return True

    def get_device_serial_number( self ):
        node_device_serial_number = PySpin.CStringPtr( self.nodemap_GetTLDevice.GetNode( "DeviceSerialNumber" ) )
        if( PySpin.IsAvailable( node_device_serial_number ) and PySpin.IsReadable( node_device_serial_number ) ):
            device_serial_number = node_device_serial_number.GetValue()
            return device_serial_number
        
        return None

    def get_acquisition_frame_rate( self ):
        node_acquisition_framerate = PySpin.CFloatPtr( self.nodemap_GenICam.GetNode( 'AcquisitionFrameRate' ) )
        if( not PySpin.IsAvailable( node_acquisition_framerate ) and not PySpin.IsReadable( node_acquisition_framerate ) ):
            print( 'Unable to retrieve frame rate. Aborting...' )
            return None
        acquisition_framerate = node_acquisition_framerate.GetValue()

        return acquisition_framerate
    
    def __error( self, exception ):
        #except PySpin.SpinnakerException as exception:
        print( "Error: %s" % exception )
        return False


