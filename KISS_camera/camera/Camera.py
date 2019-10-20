from ..System import System, PySpin
from ..Image import Image


class Camera:
    # settings

    # status variable
    status_acquisition = False

    def __init__(
        self,
        acquisition_mode,
        index = 0,
        serial_number = None,
        system = None
    ):
        # create system instance if not provided
        if(system is None):
            self.system = System()
        
        # get camera handle
        self.camera = self.get_camera_handle(serial_number, index)

        # retrieve TL device node map
        self.nodemap_GetTLDevice = self.camera.GetTLDeviceNodeMap()

        # initialize camera
        self.init()

        # retrieve GenICam nodemap
        self.nodemap_GenICam = self.camera.GetNodeMap()

        # set aquisition mode
        self.set_acquisition_mode(acquisition_mode)

        # set pixel format
        self.set_pixel_format()
            
    def __del__( self ):
        # end acquisition if still running
        if( self.is_streaming() == True ):
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
    
    def get_system(self):
        return self.system

    def get_camera_handle(
        self,
        serial_number,
        index
    ):
        # check system
        if(self.system is None):
            return None

        # get handle
        camera = None
        if(serial_number is not None):
            camera = self.system.get_camera_by_serial_number(serial_number)
            if(camera is None):
                raise ValueError('serial_number: not found')
        else:
            camera = self.system.get_camera_by_index(index)
            if(camera is None):
                raise ValueError('index: not found')
        
        return camera

    def get_image(self):
        try:
            # retrieve next received image
            image_next = self.get_next_image()

            # ensure image completion
            if(image_next.is_incomplete()):
                print("Image incomplete with image status %d ..." % image_next.get_image_status())
                return False
            
            # converted image does not affect the camera buffer (no release required)
            pixel_format = PySpin.PixelFormat_RGB8
            color_processing_algorithm = PySpin.HQ_LINEAR
            image = image_next.convert(
                format = pixel_format,
                algorithm = color_processing_algorithm
            )

            # release image
            image_next.release()
        except Exception as e:
            print(e)
            return False 
        
        return image

    def set_acquisition_mode(self, acquisition_mode):
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

    ## spinnaker
    def init(self):
        self.camera.Init()

    def de_init(self):
        self.camera.DeInit()

    def is_initialized(self):
        return self.camera.IsInitialized()

    def is_valid(self):
        return self.camera.IsValid()

    def get_node_map(self):
        return self.camera.GetNodeMap()

    def get_TL_device_node_map(self):
        return self.camera.GetTLDeviceNodeMap()

    def get_TL_stream_node_map(self):
        return self.camera.GetTLStreamNodeMap()

    def get_access_mode(self):
        return self.camera.GetAccessMode()

    def read_port(self, i_address, p_buffer, i_size):
        self.camera.ReadPort(i_address, p_buffer, i_size)

    def write_port(self, i_address, p_buffer, i_size):
        self.camera.WritePort(i_address, p_buffer, i_size)

    def begin_acquisition(self):
        self.camera.BeginAcquisition()

    def end_acquisition(self):
        self.camera.EndAcquisition()

    def get_buffer_ownership(self):
        return self.camera.GetBufferOwnership()

    def set_buffer_ownership(self, mode):
        self.camera.SetBufferOwnership(mode)

    def get_user_buffer_count(self): 
        return self.camera.GetUserBufferCount()

    def get_user_buffer_size(self): 
        return self.camera.GetUserBufferSize()

    def get_user_buffer_total_size(self): 
        return self.camera.GetUserBufferTotalSize()

    def set_user_buffers(self, p_mem_buffers, total_size, buffer_count, buffer_size): 
        #self.camera.SetUserBuffers(p_mem_buffers, total_size)
        #self.camera.SetUserBuffers(pp_mem_buffers, buffer_count, buffer_size)
        raise NotImplementedError

    def get_next_image(
        self,
        grab_timeout = PySpin.EVENT_TIMEOUT_INFINITE,
        stream_ID = 0
    ): 
        image = self.camera.GetNextImage(grab_timeout, stream_ID)
        return Image(image)

    def get_unique_id(self): 
        return self.camera.GetUniqueID()

    def is_streaming(self): 
        return self.camera.IsStreaming()

    def get_gui_xml(self):
        return self.camera.GetGuiXml()

    def register_event(self, evt_to_register, event_name):
        self.camera.RegisterEvent(evt_to_register)

    def unregister_event(self, evt_to_unregister): 
        self.camera.UnregisterEvent(evt_to_unregister)

    def get_num_images_in_use(self): 
        return self.camera.GetNumImagesInUse()

    def get_num_data_streams(self): 
        return self.camera.GetNumDataStreams()

    def discover_max_packet_size(self): 
        return self.camera.DiscoverMaxPacketSize()

    def force_ip(self): 
        self.camera.ForceIP()