import pyautogui
import pytesseract
import cv2
import numpy as np
import mss

# import time
# time.sleep(2)

offset = 50
offsetMatrix = {
	"x": [70, 125, 180, 235, 290, 345, 400, 455, 510],
	"y": [297, 352, 407, 462, 517, 572, 627, 682, 737]
}

filename ="./images/screen.png"

# screenshot = pyautogui.screenshot('screenshot.png')
# screenshot.save(r'./images/screen.png')

# with mss.mss() as sct:
#   filename = sct.shot(output="./images/screen.png")
#   print(filename)

# image = cv2.imread(filename)

# x, y = 120 * 2, 292 * 2

# offset = 50
# x1, y1 = x - offset, y - offset
# x2, y2 = x + offset, y + offset

# cv2.circle(image, (x,y), 10, (0, 0, 255), 10)

# cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)

# cv2.imwrite("./images/cell.png", image)

def convertToBW(image, greyLimit):
	for y in range(0, len(image)):
		for x in range(0, len(image[y])):
			if image[y][x] < greyLimit:
				image[y][x] = 0
			else:
				image[y][x] = 255
	return image

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

def takeScreenshotOfCell(x, y, filename):
	trimValue = 5
	x = x - offset/2 + trimValue
	y = y - offset/2 + trimValue
	length = offset - (trimValue * 3)
	return takeScreenShotOfRegionInOpenCVFormat(x, y, length, length)

# difficulty image 
x, y = 38.04296875, 227.140625
region = takeScreenShotOfRegionInOpenCVFormat(x, y, 70, 20)
region = convertToBW(region, 170)
cv2.imwrite("./images/difficulty.png", region)

# generate the numbers
# x, y = 2,4
# takeScreenshotOfCell(offsetMatrix["x"][x], offsetMatrix["y"][y], "./images/n-1")
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

# numbers = []
# for i in range(0, 9):
# 	numbers.append(cv2.imread("./images/n-" + str(i+1) + ".png", cv2.IMREAD_GRAYSCALE))

# x, y = 7,8 # 1
# x, y = 2,1 # 2
# x, y = 5,3 # 3
# x, y = 4,7 # 4
# x, y = 8,6 # 5
# x, y = 6,4 # 6
# x, y = 5,2 # 7
# x, y = 8,4 # 8
# x, y = 4,8 # 9
# cell = takeScreenshotOfCell(offsetMatrix["x"][x], offsetMatrix["y"][y], "./images/cell")

# maxValue = 0
# number = 0
# for i in range(0, len(numbers)):
# 	result = cv2.matchTemplate(cell, numbers[i], cv2.TM_CCOEFF_NORMED)
# 	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
# 	print("{0} {1}".format(i+1, max_val))
# 	if max_val > maxValue:
# 		maxValue = max_val
# 		number = i+1

# print(number)

# def toBW(image):
# 	for y in range(0, len(image)):
# 		for x in range(0, len(image[y])):
# 			if image[y][x] < 180:
# 				image[y][x] = 0
# 			else:
# 				image[y][x] = 255
# 	return image

imageOfDifficulty = cv2.imread("./images/difficulty.png", cv2.IMREAD_GRAYSCALE)

imageOfSreen = cv2.imread("./images/screen.png", cv2.IMREAD_GRAYSCALE)
imageOfSreen = convertToBW(imageOfSreen, 180)
cv2.imwrite("./images/screenBW.png", imageOfSreen)

result = cv2.matchTemplate(imageOfSreen, imageOfDifficulty, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
# print(min_val, max_val, min_loc, max_loc)
print(max_loc)

locMax = tuple(int(i/2) for i in max_loc)
print(locMax)

topLeft = (40, 267)
print(topLeft)

topLeft = (locMax[0], locMax[1] + 40)
print(topLeft)
pyautogui.moveTo(topLeft, duration=1)