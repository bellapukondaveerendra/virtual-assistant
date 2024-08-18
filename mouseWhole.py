import cv2
import numpy as np
import pyautogui
import mss
pyautogui.FAILSAFE = False

screen_list = pyautogui.getAllWindows()
screen_width, screen_height = sum(screen.width for screen in screen_list), max(screen.height for screen in screen_list)

with mss.mss() as sct:
    monitor = {"top": 0, "left": 0, "width": screen_width, "height": screen_height}

    while True:
        frame = np.array(sct.grab(monitor))
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_red = np.array([0, 100, 100])
        upper_red = np.array([10, 255, 255])
        mask = cv2.inRange(hsv_frame, lower_red, upper_red)
        cv2.imshow('Color Mask', mask)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            max_contour = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(max_contour)

            centroid_x = x + w // 2
            centroid_y = y + h // 2
            mouse_x = int(centroid_x * screen_width / frame.shape[1])
            mouse_y = int(centroid_y * screen_height / frame.shape[0])

            print("mouse_x",mouse_x)
            print("mouse_y",mouse_y)
            # Move the mouse cursor
            pyautogui.moveTo(mouse_x, mouse_y)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cv2.destroyAllWindows()