import cv2
import numpy as np
import pyautogui

# Set up the camera
cap = cv2.VideoCapture(0)

# Define the lower and upper bounds for skin color in HSV
lower_skin = np.array([0, 20, 70], dtype=np.uint8)
upper_skin = np.array([20, 255, 255], dtype=np.uint8)

# Set up the starting position of the cursor
x, y = pyautogui.position()

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Flip the frame horizontally for a mirror effect
    frame = cv2.flip(frame, 1)

    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Threshold the image to get skin color
    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    # Apply morphological operations to the mask
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
    mask = cv2.erode(mask, kernel, iterations=1)
    mask = cv2.dilate(mask, kernel, iterations=2)
    mask = cv2.medianBlur(mask, 7)

    # Find contours in the mask
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Find the largest contour and its centroid
    if len(contours) > 0:
        max_contour = max(contours, key=cv2.contourArea)
        M = cv2.moments(max_contour)
        if M['m00'] > 0:
            cx = int(M['m10'] / M['m00'])
            cy = int(M['m01'] / M['m00'])
            # Move the cursor based on the hand position
            x = x + (cx - x) / 10
            y = y + (cy - y) / 10
    # Display the original frame and the mask
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)

    # Exit if the user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
