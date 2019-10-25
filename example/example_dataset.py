# import
import os
from KISS_camera import CameraSingleFrame

# settings
SERIAL_NUMBER = None
IMAGE_COUNT = 10
IMAGE_FOLDER = 'dataset/test'

def main():
    # get camera
    camera = CameraSingleFrame(
        serial_number = SERIAL_NUMBER
    )

    # acquire images
    for index in range(IMAGE_COUNT):
        input('Press Enter to acquire image. [%i/%i]' % (index + 1, IMAGE_COUNT))
        image = camera.get_image()
        image.save_as_jpeg(os.path.join(IMAGE_FOLDER, str(index)))
        del image

    del camera

    return True

if __name__ == '__main__':
    main()
    print( 'Done.' )
