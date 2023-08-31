import pyautogui
import time
import cv2
import numpy as np

screenshotImage = pyautogui.screenshot()
screenshotImage = np.array(screenshotImage)
opencvImage = cv2.cvtColor(screenshotImage, cv2.COLOR_RGB2BGR)
savedMapImage = "./images/map.png"

duration = 0

topLeft = (310, 267)
topRight = (810, 267)
bottomRight = (810, 765)
bottomLeft = (310, 765)
print('Top left:          {0}'.format(topLeft))
print('Top right:         {0}'.format(topRight))
print('Bottom right:      {0}'.format(bottomRight))
print('Bottom left:       {0}'.format(bottomLeft))

gridTopLeft = (371, 271)
gridBottomRight = (419, 319)
print('Grid top left:     {0}'.format(gridTopLeft))
print('Grid bottom right: {0}'.format(gridBottomRight))

gridWidth = gridBottomRight[0] - gridTopLeft[0]
gridHeight = gridBottomRight[1] - gridTopLeft[1]
print('Grid width:        {0}'.format(gridWidth))
print('Grid height:       {0}'.format(gridHeight))

pyautogui.moveTo(topLeft, duration=duration)
pyautogui.moveTo(topRight, duration=duration)
pyautogui.moveTo(bottomRight, duration=duration)
pyautogui.moveTo(bottomLeft, duration=duration)


# Create a circle around each corner
offset = ((topRight[0]-topLeft[0])/2, (bottomLeft[1]-topLeft[1])/2)
print('Offset:            {0}'.format(offset))
newTopLeft = tuple(np.add(topLeft, offset).astype(int))
newTopRight = tuple(np.add(topRight, offset).astype(int))
newBottomRight = tuple(np.add(bottomRight, offset).astype(int))
newBottomLeft = tuple(np.add(bottomLeft, offset).astype(int))
print('* Top left         {0}'.format(newTopLeft))
print('* Top right        {0}'.format(newTopRight))
print('* Bottom right     {0}'.format(newBottomRight))
print('* Bottom left      {0}'.format(newBottomLeft))

image = opencvImage.copy()
height, width = image.shape[:2]
print('Image width:       {0}'.format(width))
print('Image height:      {0}'.format(height))

# image[topLeft] = np.array([0, 255, 0])
# print('Pixel at location: {0}'.format(image[topLeft]))

radius = 10
# cv2.circle(image, newTopLeft, radius, (0, 0, 255), 10)
# cv2.circle(image, newTopRight, radius, (0, 0, 255), 10)
# cv2.circle(image, newBottomRight, radius, (0, 0, 255), 10)
# cv2.circle(image, newBottomLeft, radius, (0, 0, 255), 10)
cv2.circle(image, topLeft, radius, (0, 0, 255), 10)
cv2.circle(image, topRight, radius, (0, 0, 255), 10)
cv2.circle(image, bottomRight, radius, (0, 0, 255), 10)
cv2.circle(image, bottomLeft, radius, (0, 0, 255), 10)
cv2.imwrite(savedMapImage, image)

# cv2.imshow("Processes", image)