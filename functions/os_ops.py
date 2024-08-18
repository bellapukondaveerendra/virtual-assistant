import os
import subprocess as sp
import platform
import cv2
import numpy as np
import pyautogui

paths = {
    'calculator': "C:\\Windows\\System32\\calc.exe"
}


def open_notepad():
    os.startfile(paths['notepad'])

def open_cmd():
    os.system('start cmd')


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)


def open_calculator():
    sp.Popen(paths['calculator'])

def contol_mouse():
    lower_color = np.array([0, 100, 100])
    upper_color = np.array([10, 255, 255])
    cap = cv2.VideoCapture(0)
    cv2.namedWindow('Color Tracking', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('Color Tracking', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv_frame, lower_color, upper_color)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if contours:
            max_contour = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(max_contour)
            centroid_x = x + w // 2
            centroid_y = y + h // 2
            mouse_x = int(centroid_x * screen_width / frame.shape[1])
            mouse_y = int(centroid_y * screen_height / frame.shape[0])
            pyautogui.moveTo(mouse_x, mouse_y)

        cv2.imshow('Color Tracking', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        cap.release()
        cv2.destroyAllWindows()
    