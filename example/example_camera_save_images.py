# import
import os
from KISS_camera import CameraContinuous

# settings
SERIAL_NUMBER = None
IMAGE_COUNT = 10
IMAGE_FOLDER = 'image'

def main():
    # get camera
    camera = CameraContinuous(
        serial_number = SERIAL_NUMBER
    )

    # save images
    for index in range(IMAGE_COUNT):
        image = camera.get_image()
        image.save_as_jpeg(os.path.join(IMAGE_FOLDER, str(index)))
        del image

    del camera

    return True

if __name__ == '__main__':
    main()
    print( 'Done.' )