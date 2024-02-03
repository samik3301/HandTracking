# GCVC: Gesture Controlled Volume Changer

### Pre-requisites-

Make a virtual environment and activate it. Everything will be run inside that virtual environment. 

*Then run the following command to clone the repository*

`git clone https://github.com/samik3301/HandTracking.git`

`pip install -r requirements.txt`

The above command installs the required packages needed to run this project.

### How to run the project?

Navigate into the project directory after cloning the project and then run, `python3 volume_control.py`.

### Methodology and Working Explained:

This is an implementation of computer vision technique called hand landmark detection and tracking to track certain landmarks of interest. The MediaPipe Hand Landmarker task lets us detect the landmarks of the hands in an image frame. 

I have made a helper script called `trackingmodule.py` which contains helper functions needed to detect the hands (if detected it will draw them using the parameter `draw=`*{Boolean}* through the `findHands()` function). Another function, `findPosition()` returns the landmark list that is being tracked in the current frame and draws circles around the detected landmarks (can be turned off with `draw=`*{Boolean}* parameter).

Have made another script called `handtracking_min.py` to only track certain hand landmarks of our interest, which can be used to map to a gesture later on, for testing purposes. 

The main script being, `volume_control.py` where the landmarks of hands are being detected and tracked. This script tracks the *landmark 4* and *landmark 8* which are the thumb tip and index tip respectively.

The math function, `hypot` [Multidimensional Euclidean distance from the origin to a point] is used to calculate the distance between the respective x coordinates and y coordinates of the landmarks of interest to find the length between them.

After getting the length, the minimum and the maximum length range can be saved for the next part of the implementation. It is important to know the possible minimum and maximum values of length reached while bring the 2 landmarks together and apart.

The length range is then interpolated with the volume range (0 to 100) using the numpy `interp` function. OSA-Script is used to get access for master volume control for MacOS. PyCaw library can be used to get access to volume control on Windows.

To summarize: This project uses OpenCV with Mediapipe and OSA-Script for MacOS to change the volume by tracking the finger tip landmarks.