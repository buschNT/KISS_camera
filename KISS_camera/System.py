# import
import PySpin
from .Interface import Interface

class System:
    def __init__( self ):
        # get system instance (singleton)
        self.system = PySpin.System.GetInstance()

    def __del__( self ):
        # release system
        self.system.ReleaseInstance()
    
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