import PySpin

class Interface:
    def __init__( self, interface ):
        # interface
        self.interface = interface

        # nodemap from interface
        self.nodemap_interface = interface.GetTLNodeMap()
    
    def __del__( self ):
        # release interface
        del self.interface
    
    def interface_display_name( self ):
        # get node interface display name
        node_interface_display_name = PySpin.CStringPtr(
            self.nodemap_interface.GetNode( "InterfaceDisplayName" )
        )

        # available / readable
        if( PySpin.IsAvailable( node_interface_display_name ) and PySpin.IsReadable( node_interface_display_name ) == False ):
            return None
        
        # get interface display name
        interface_display_name = node_interface_display_name.GetValue()

        return interface_display_name
    
    def num_cameras( self ):
        # get camera list
        cam_list = self.interface.GetCameras()

        # get number of cameras
        num_cameras = cam_list.GetSize()

        # clear camera list
        cam_list.Clear()

        return num_cameras
    
    def get_camera(self, index):
        # get camera list
        cam_list = self.interface.GetCameras()

        # get camera
        try:
            camera = cam_list[index]
        except:
            camera = None

        # clear camera list
        cam_list.Clear()

        return camera
    
    def get_camera_by_serial_number(self, serial_number):
        # loop through cameras
        for index in range(self.num_cameras()):
            # get camera
            camera = self.get_camera(index)

            # compare serial number
            if(camera.device_serial_number() != serial_number):
                 # release camera
                del camera
                continue
            
            return camera
            
        return None
