
import numpy as np
import cv2

def detect_rooftop(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
    mask = cv2.medianBlur(thresh, 5)
    color_mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
    return color_mask
