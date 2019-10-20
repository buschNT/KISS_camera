# KISS_camera
I use this module to capture images/videos from my Point Grey Camera (Chameleon3 CM3-U3-13S2C). This module keeps image acquisition simple.  
The implemenation of camera functions is limited to my needs, so not everything is available.

# requirements / tested with
software:
- python 3.6
- spinnaker 1.15.0.52

hardware:
- Chameleon3 CM3-U3-13S2C (other cameras should work, too)

# install
Navigate to `setup.py`.  
Now you can install the package locally (for use on our system), with:  
`$ pip install .`

You can also install the package with a symlink, so that changes to the source files will be immediately available to other users of the package on our system:  
`$ pip install -e .`

You might need to choose your python version:  
`$ C:\...\python.exe -m pip install -e .`

# example
Please take a look inside the example folder to get an idea how to use this module.