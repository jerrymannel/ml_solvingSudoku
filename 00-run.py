import mss, pyautogui, cv2
import numpy as np
from subprocess import Popen, PIPE
import time

# Globals
monitor = 1
duration = 0.5 # Duration of the mouse movement
scale = 1.0 # Scale of the screenshot

topLeft = (0, 0)
topRight = (0, 0)
bottomRight = (0, 0)
bottomLeft = (0, 0)
heightOfGrid = 500
widthOfGrid = 500

newGameButton = (0, 0)
easyGameButton = (0, 0)
mediumGameButton = (0, 0)
hardGameButton = (0, 0)
expertGameButton = (0, 0)

counter = 0
cellStartOffset = 30;
startingPosition = (0, 0)
offset = 50
offsetMatrix = {
	"x": [],
	"y": []
}

imageOfDifficulty = cv2.imread("./images/difficulty.png", cv2.IMREAD_GRAYSCALE)
numbers = []
for i in range(0, 9):
	numbers.append(cv2.imread("./images/n-" + str(i+1) + ".png", cv2.IMREAD_GRAYSCALE))

emptyCells = [];

def generateOffsetMatrix():
	for i in range(0, 9):
		calculatedOffset = (offset * i) + (i*5)
		offsetMatrix["x"].append(startingPosition[0] + calculatedOffset)
		offsetMatrix["y"].append(startingPosition[1] + calculatedOffset)

def takeScreenShot():
	with mss.mss() as sct:
		monitor = sct.monitors[1]
		screenshot = np.array(sct.grab(monitor))
		return cv2.cvtColor(screenshot, cv2.COLOR_BGRA2GRAY)

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

def takeScreenshotOfCell(x, y):
	trimValue = 0
	x = x - offset/2 + trimValue
	y = y - offset/2 + trimValue
	length = offset - (trimValue * 3)
	cell = takeScreenShotOfRegionInOpenCVFormat(x, y, length, length)
	cell = convertToBW(cell, 170)
	return cell

def findTopLeftCorner():
	imageOfScreen = takeScreenShot()
	imageOfScreen = convertToBW(imageOfScreen, 180)
	result = cv2.matchTemplate(imageOfScreen, imageOfDifficulty, cv2.TM_CCOEFF_NORMED)
	max_loc = cv2.minMaxLoc(result)[3]
	print(max_loc)
	locMax = tuple(int(i/2) for i in max_loc)
	return (locMax[0] + 2, locMax[1] + 40)

def identifyNumber(cell):
	maxValue = 0
	number = 0
	for i in range(0, len(numbers)):
		result = cv2.matchTemplate(cell, numbers[i], cv2.TM_CCOEFF_NORMED)
		max_val = cv2.minMaxLoc(result)[1]
		if max_val > maxValue:
			maxValue = max_val
			number = i+1
	# print("{0} / {1}".format(number, maxValue)) if number > 0 else None
	return number

def scanTheGrid():
	gridValues = ""
	x, y = 0, 0
	for y in range(0, 9):
		for x in range(0, 9):
			pyautogui.click(offsetMatrix["x"][x], offsetMatrix["y"][y])
			cell = takeScreenshotOfCell(offsetMatrix["x"][x], offsetMatrix["y"][y])
			number = identifyNumber(cell)
			if number == 0:
				emptyCells.append((offsetMatrix["x"][x], offsetMatrix["y"][y]))
			gridValues += str(number)
	return gridValues

def solveTheGrid(values):
	process = Popen(["./goSudoku", "-i", values], stdout=PIPE)
	return process.communicate()[0].decode("utf-8").strip()

def sudokuSolver():
	pyautogui.click(topLeft, clicks=2)
	
	gridValues = scanTheGrid()
	print(gridValues)
	solvedGrid = solveTheGrid(gridValues)
	print(solvedGrid)

	for cell in range(0, len(gridValues)):
		if gridValues[cell] == "0":
			pos = emptyCells.pop(0)
			pyautogui.click(pos)
			pyautogui.write(solvedGrid[cell])
	
	pyautogui.click(newGameButton)
	# pyautogui.click(easyGameButton)
	# pyautogui.click(mediumGameButton)
	# pyautogui.click(hardGameButton)
	pyautogui.click(expertGameButton)


if __name__ == '__main__':
	# topLeft = findTopLeftCorner()
	topLeft = (55, 267)
	topRight = (topLeft[0] + widthOfGrid, topLeft[1])
	bottomRight = (topLeft[0] + widthOfGrid, topLeft[1] + heightOfGrid)
	bottomLeft = (topLeft[0], topLeft[1] + heightOfGrid)
	startingPosition = (topLeft[0] + cellStartOffset, topLeft[1] + cellStartOffset)
	
	newGameButton = (bottomRight[0] + 100, bottomRight[1] - 30)
	easyGameButton = (newGameButton[0], newGameButton[1] - 320)
	mediumGameButton = (newGameButton[0], newGameButton[1] - 275)
	hardGameButton = (newGameButton[0], newGameButton[1] - 225)
	expertGameButton = (newGameButton[0], newGameButton[1] - 175)
	
	print('Top left:          {0}'.format(topLeft))
	print('Top right:         {0}'.format(topRight))
	print('Bottom right:      {0}'.format(bottomRight))
	print('Bottom left:       {0}'.format(bottomLeft))
	print('Height:            {0}'.format(heightOfGrid))
	print('Width:             {0}'.format(widthOfGrid))
	print('New Game:          {0}'.format(newGameButton))
	print('Starting position: {0}'.format(startingPosition))
	
	generateOffsetMatrix()
	print(offsetMatrix["x"])
	print(offsetMatrix["y"])

	counter = 5
	while counter > 0:
		sudokuSolver()
		time.sleep(1)
		counter -= 1