# KISS_camera
I use this module to capture images/videos from my Point Grey Camera (Chameleon3 CM3-U3-13S2C). It is more compact than the examples in the skinnaker SDK and requires only a few lines of code to get started. Please take a look inside the `example` folder to get an idea how to use this module.

# tested software/hardware
software:
- python 3.6
- spinnaker 1.15.0.52

hardware:
- Chameleon3 CM3-U3-13S2C (other cameras are not tested)

# install
Download the module and navigate to `setup.py`.  
Now you can install the package locally (for use on our system), with:  
`$ pip install .`

You can also install the package with a symlink, so that changes to the source files will be immediately available to other users of the package on our system:  
`$ pip install -e .`

You might need to choose your python version:  
`$ C:\...\python.exe -m pip install -e .`

I recommend a virtual environment.