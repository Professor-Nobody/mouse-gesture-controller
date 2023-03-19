# Gesture Mouse Control with Python <br>
This is a Python program that allows you to control your computer mouse using hand gestures.<br> The program uses OpenCV to detect hand gestures and PyAutoGUI to move the mouse cursor.
<br>

# Dependencies
To run this program, you'll need to install the following Python packages:
<br>
numpy <br>
opencv-python <br>
pyautogui <br>
You can install these packages using pip by running the following command:

```
pip install numpy opencv-python pyautogui
```

# Running the Program
To run the program, open a terminal window and navigate to the directory where you've saved the program files. <br> Then, run the following command:

```
python mouse-gesture-controller.py
```

This will start the program and launch the video feed from your computer's camera.

# Controlling the Mouse
To control the mouse, hold your hand up in front of the camera with your palm facing the camera. <br> Make sure your hand is well-lit and there's not too much background clutter.

The program will detect your hand and draw a bounding box around it. To move the mouse, <br> move your hand left, right, up, or down within the bounding box. The mouse cursor <br> will move in the same direction as your hand.

To click the mouse, make a fist with your hand while it's within the bounding box. <br> To right-click, hold down the "shift" key while making a fist.<br>

To exit the program, press the "q" key.

# Limitations
This program is designed to work with a single hand only, and may not work well in low-light conditions or with complex backgrounds. <br> It's also intended for use with a standard mouse, and may not be suitable for tasks that require more precise or nuanced mouse control. <br>

# Contributions

<a href="https://github.com/ItsRahilAnwar">RahilAnwar </a>
