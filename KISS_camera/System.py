import PySpin
from .Interface import Interface

def get_instance():
    return PySpin.System.GetInstance()

class System:
    def __init__( self ):
        self.system = get_instance() # singleton!

    def __del__( self ):
        self.release_instance()
    
    def num_interfaces( self ):
        interface_list = self.get_interfaces()
        num_interfaces = len(interface_list)
        del interface_list
        return num_interfaces

    def num_cameras( self ):
        camera_list = self.get_cameras()
        num_cameras = len(camera_list)
        del camera_list
        return num_cameras

    def get_camera_by_index(self, index):
        camera_list = self.get_cameras()
        if(len(camera_list) <= index):
            camera = None
        else:
            camera = camera_list[index]
        del camera_list
        return camera

    def get_camera_by_serial_number(self, serial_number):
        camera_list = self.get_cameras()

        camera = camera_list.GetBySerial(serial_number)
        if(camera.IsValid()):
            pass
        else:
            del camera
            camera = None
        del camera_list
        return camera
    
    ## spinnaker
    def release_instance(self):
        self.system.ReleaseInstance()

    def get_interfaces(self, update_interface=True):
        return self.system.GetInterfaces(update_interface) # return spinnaker InterfaceList

    def get_cameras(self, update_interfaces=True, update_cameras=True):
        camera_list = self.system.GetCameras(update_interfaces, update_cameras)
        return camera_list

    def update_cameras(self, update_interfaces=True):
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
        return library_version # return spinnaker structure

    def get_TL_node_map(self):
        return self.system.GetTLNodeMap()
