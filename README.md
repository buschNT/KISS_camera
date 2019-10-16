# KISS_camera
Simple access to my FLIR camera.  
I use this module to capture images/videos from a Point Grey Camera (Chameleon3 CM3-U3-13S2C)

# requirements / tested with
- python 3.6
- spinnaker 1.15.0.52
- camera

# install
Navigate to `setup.py`.  
Now we can install the package locally (for use on our system), with:  
`$ pip install .`

We can also install the package with a symlink, so that changes to the source files will be immediately available to other users of the package on our system:  
`$ pip install -e .`

You might need to choose your python version:  
`$ C:\...\python.exe -m pip install -e .`