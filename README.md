Gesture Mouse Control with Python
This is a Python program that allows you to control your computer mouse using hand gestures. The program uses OpenCV to detect hand gestures and PyAutoGUI to move the mouse cursor.

Dependencies
To run this program, you'll need to install the following Python packages:

numpy
opencv-python
pyautogui
You can install these packages using pip by running the following command:

```
pip install numpy opencv-python pyautogui
```

Running the Program
To run the program, open a terminal window and navigate to the directory where you've saved the program files. Then, run the following command:

Copy code
python gesture_mouse_control.py
This will start the program and launch the video feed from your computer's camera.

Controlling the Mouse
To control the mouse, hold your hand up in front of the camera with your palm facing the camera. Make sure your hand is well-lit and there's not too much background clutter.

The program will detect your hand and draw a bounding box around it. To move the mouse, move your hand left, right, up, or down within the bounding box. The mouse cursor will move in the same direction as your hand.

To click the mouse, make a fist with your hand while it's within the bounding box. To right-click, hold down the "shift" key while making a fist.

To exit the program, press the "q" key.

Limitations
This program is designed to work with a single hand only, and may not work well in low-light conditions or with complex backgrounds. It's also intended for use with a standard mouse, and may not be suitable for tasks that require more precise or nuanced mouse control.

Acknowledgements
This program was inspired by this tutorial on hand gesture recognition with Python and OpenCV.
