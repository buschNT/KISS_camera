import PySpin
from .Interface import Interface

def get_instance():
    return PySpin.System.GetInstance()

class System:
    def __init__( self ):
        self.system = get_instance()    # singleton!

    def __del__( self ):
        self.release_instance()
    
    def num_interfaces( self ):
        # get interface list
        interface_list = self.system.GetInterfaces()

        # get number of interfaces
        num_interfaces = interface_list.GetSize()

        # clear interface list
        interface_list.Clear()

        return num_interfaces
    
    def get_interface( self, index ):
        # get interface list
        interface_list = self.system.GetInterfaces()

        # get interface
        try:
            interface = Interface( interface_list[ index ] )
        except:
            interface = None

        # clear interface list
        interface_list.Clear()

        return interface

    def num_cameras( self ):
        # get camera list
        cam_list = self.system.GetCameras()

        # get number of cameras
        num_cameras = cam_list.GetSize()

        # clear camera list
        cam_list.Clear()

        return num_cameras

    def get_camera_by_index( self, camera_index ):
        # camera
        camera = None

        # loop through interfaces
        for index in range( self.num_interfaces() ):
            # get interface
            interface = self.get_interface( index )

            # check for camera
            camera = interface.get_camera( camera_index )
            if( camera is None ):
                continue
            
            break

        # release interface
        del interface

        return camera

    def get_camera_by_serial_number( self, serial_number ):
        # camera
        camera = None

        # loop through interfaces
        for index in range( self.num_interfaces() ):
            # get interface
            interface = self.get_interface( index )

            # check for camera
            camera = interface.get_camera_by_serial_number( serial_number )
            if( camera is None ):
                continue
            
            break

        # release interface
        del interface

        return camera
    
    ## spinnaker
    def release_instance(self):
        self.system.ReleaseInstance()

    def get_interfaces(self, update_interface=True):
        interface_list = self.system.GetInterfaces(update_interface)     # TODO: InterfaceList
        return interface_list

    def get_cameras(self, update_interfaces=True, update_cameras=True)
        camera_list = self.system.GetCameras(update_interfaces, update_cameras) # TODO: CameraList
        return camera_list

    def update_cameras(self, update_interfaces=True)
        return self.system.UpdateCameras(update_interfaces)

    def update_interface_list(self):
        self.system.UpdateInterfaceList()

    def register_event(self):
        raise NotImplementedError

    def unregister_event(self):
        raise NotImplementedError

    def register_interface_event(self):
        raise NotImplementedError

    def unregister_interface_event(self):
        raise NotImplementedError

    def register_logging_event(self):
        raise NotImplementedError

    def unregister_all_logging_event(self):
        raise NotImplementedError

    def unregister_logging_event(self):
        raise NotImplementedError

    def set_logging_event_priority_level(self):
        raise NotImplementedError

    def get_logging_event_priority_level(self):
        raise NotImplementedError

    def is_in_use(self):
        self.system.IsInUse()

    def send_action_command(self):
        raise NotImplementedError

    def get_library_version(self):
        library_version = self.system.GetLibraryVersion()
        return library_version  # return spinnaker structure

    def get_TL_node_map(self):
        return self.system.GetTLNodeMap()
