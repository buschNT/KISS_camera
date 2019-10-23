# import
import os
from KISS_camera import CameraContinuous
from KISS_camera import VideoAVI, VideoMJPG, VideoH264

# settings
SERIAL_NUMBER = None
VIDEO_DURATION = 5
VIDEO_FOLDER = 'video'

def main():
    # get camera
    camera = CameraContinuous(
        serial_number = SERIAL_NUMBER
    )

    # create video
    video = VideoAVI(
        filename = os.path.join(VIDEO_FOLDER, 'test'),
        frame_rate = camera.get_node('AcquisitionFrameRate')
    )

    # video loop
    for _ in range(VIDEO_DURATION * int(camera.get_node('AcquisitionFrameRate'))):
        image = camera.get_image()
        video.add_image(image)

    del video
    del camera

    return True

if __name__ == '__main__':
    main()
    print( 'Done.' )