import pyautogui
import cv2
import numpy as np
import mss

# import time
# time.sleep(2)

filename ="./images/screen.png"

# screenshot = pyautogui.screenshot('screenshot.png')
# screenshot.save(r'./images/screen.png')

screenshotImage = pyautogui.screenshot()
screenshotImage = np.array(screenshotImage)
opencvImage = cv2.cvtColor(screenshotImage, cv2.COLOR_RGB2BGR)
textLocation = pyautogui.locateAllOnScreen('./images/difficulty.png',grayscale=True, confidence=0.45)

image = opencvImage.copy()
for loc in list(textLocation):
  print(loc)
  cv2.circle(image, (loc.left, loc.top), 10, (0, 0, 255), 10)
  pyautogui.moveTo(loc.left, loc.top, duration=0.1)  

cv2.imwrite("./images/screen2.png", image)

# with mss.mss() as sct:
#   filename = sct.shot(output="./images/screen.png")
#   print(filename)
#   textLocation = pyautogui.locate('./images/difficulty.png', filename, grayscale=True, confidence=0.1)
#   cv2.circle(image, topLeft, radius, (0, 0, 255), 10)
#   print(textLocation)
#   pyautogui.moveTo(textLocation.left, textLocation.top, duration=1)  