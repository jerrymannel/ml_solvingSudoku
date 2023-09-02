import pyautogui
import pytesseract
import cv2
import numpy as np
import mss

# import time
# time.sleep(2)

offset = 50
offsetMatrix = {
	"x": [85, 140, 195, 250, 305, 360, 415, 470, 525],
	"y": [297, 352, 407, 462, 517, 572, 627, 682, 737]
}

filename ="./images/screen.png"

def convertToBW(image, greyLimit):
	for y in range(0, len(image)):
		for x in range(0, len(image[y])):
			if image[y][x] < greyLimit:
				image[y][x] = 0
			else:
				image[y][x] = 255
	return image

def takeScreenShot():
	with mss.mss() as sct:
		monitor = sct.monitors[1]
		screenshot = np.array(sct.grab(monitor))
		return cv2.cvtColor(screenshot, cv2.COLOR_BGRA2GRAY)

def takeScreenShotOfRegionInOpenCVFormat(x, y, width, height):
	with mss.mss() as sct:
		monitor = {
			"top": y, 
			"left": x,
			"width": width, 
			"height": height
		}
	region = np.array(sct.grab(monitor))
	region = cv2.cvtColor(region, cv2.COLOR_BGRA2GRAY)
	return region

def takeScreenshotOfCell(x, y):
	pyautogui.click(x, y)
	trimValue = 0
	x = x - offset/2 + trimValue
	y = y - offset/2 + trimValue
	length = offset - (trimValue * 3)
	cell = takeScreenShotOfRegionInOpenCVFormat(x, y, length, length)
	cell = convertToBW(cell, 170)
	return cell

pyautogui.click(offsetMatrix["x"][0], offsetMatrix["y"][0])

# generate the numbers
x, y = 8,0
cell = takeScreenshotOfCell(offsetMatrix["x"][x], offsetMatrix["y"][y])
cv2.imwrite("./images/cell.png", cell)
# x, y = 1,8
# takeScreenshotOfCell(offsetMatrix["x"][x], offsetMatrix["y"][y], "./images/n-2")
# x, y = 2,8
# takeScreenshotOfCell(offsetMatrix["x"][x], offsetMatrix["y"][y], "./images/n-3")
# x, y = 1,6
# takeScreenshotOfCell(offsetMatrix["x"][x], offsetMatrix["y"][y], "./images/n-4")
# x, y = 3,8
# takeScreenshotOfCell(offsetMatrix["x"][x], offsetMatrix["y"][y], "./images/n-5")
# x, y = 3,1
# takeScreenshotOfCell(offsetMatrix["x"][x], offsetMatrix["y"][y], "./images/n-6")
# x, y = 0,8
# takeScreenshotOfCell(offsetMatrix["x"][x], offsetMatrix["y"][y], "./images/n-7")
# x, y = 2,7
# takeScreenshotOfCell(offsetMatrix["x"][x], offsetMatrix["y"][y], "./images/n-8")
# x, y = 4,8
# takeScreenshotOfCell(offsetMatrix["x"][x], offsetMatrix["y"][y], "./images/n-9")

numbers = []
for i in range(0, 9):
	numbers.append(cv2.imread("./images/n-" + str(i+1) + ".png", cv2.IMREAD_GRAYSCALE))

# imageOfScreen = takeScreenShot()
# imageOfScreen = convertToBW(imageOfScreen, 180)
# cv2.imwrite("./images/screenBW.png", imageOfScreen)

# x, y = 0, 0 # 0
# x, y = 7, 8 # 1
# x, y = 2, 1 # 2
# x, y = 8, 8 # 3
# x, y = 4, 7 # 4
# x, y = 4, 5 # 5
# x, y = 6, 4 # 6
# x, y = 5, 2 # 7
# x, y = 8, 4 # 8
# x, y = 4, 8 # 9

x, y = 1,0
cell = takeScreenshotOfCell(offsetMatrix["x"][x], offsetMatrix["y"][y])
cell = convertToBW(cell, 170)
cv2.imwrite("./images/cell.png", cell)

maxValue = 0
number = 0
for i in range(0, len(numbers)):
	result = cv2.matchTemplate(cell, numbers[i], cv2.TM_CCOEFF_NORMED)
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
	print("{0} {1}".format(i+1, max_val))
	if max_val > maxValue:
		maxValue = max_val
		number = i+1

print(number)
