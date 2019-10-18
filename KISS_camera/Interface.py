import PySpin

class Interface:
    def __init__(self, interface):
        self.interface = interface

        # nodemap from interface
        self.nodemap_interface = interface.GetTLNodeMap()
    
    def __del__( self ):
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
    
    def get_camera_by_index(self, index):
        camera_list = self.get_cameras()
        camera = camera_list.GetByIndex(index)
        del camera_list
        return camera
    
    def get_camera_by_serial_number(self, serial_number):
        camera_list = self.get_cameras()
        camera = camera_list.GetBySerial(serial_number)
        del camera_list
        return camera

    ## spinnaker
    def get_cameras(self, update_cameras=True):
        camera_list = self.interface.GetCameras(update_cameras)
        return camera_list
    
    def unpdate_cameras(self):
        return self.interface.UpdateCameras()
    
    def get_TL_node_map(self):
        return self.interface.GetTLNodeMap()
    
    def register_event(self):
        raise NotImplementedError

    def unregister_event(self):
        raise NotImplementedError

    def is_in_use(self):
        return self.interface.IsInUse()
    
    def SendActionCommand(self):
        raise NotImplementedError

    def is_valid(self):
        return self.interface.IsValid()