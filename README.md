# Computer Vision - Lab 01

## Overview
This repository demonstrates basic image loading and display operations using Python and OpenCV.

## Directory Structure
- **Files/**: Contains the Python source code (`images.py`).
- **Images/**: Contains the sample image datasets (`baboon1.png`, `baboon2.png`).

## Script Functionality
The `images.py` script:
1. Dynamically constructs the relative path to the `Images/` folder.
2. Loads two baboon images into memory using `cv2.imread()`.
3. Displays both images in separate GUI windows using `cv2.imshow()`.
4. Waits for any keyboard input before terminating cleanly.

## Prerequisites
- Python 3.x
- OpenCV (`pip install opencv-python`)
