import mss, pyautogui
from pynput.mouse import Listener, Controller

# Globals
duration = 0.1 # Duration of the mouse movement
# topLeft = (0, 0)
topLeft = (1926, 225)
topRight = (0, 0)
bottomRight = (0, 0)
bottomLeft = (0, 0)
heightOfGrid = 500
widthOfGrid = 500
# newGameButton = (0, 0)
newGameButton = (2617, 687)

counter = 0
cellStartOffset = 25;
startingPosition = (topLeft[0] + cellStartOffset, topLeft[1] + cellStartOffset)
offset = 50
offsetMatrix = {
	"x": [],
	"y": []
}


def generateOffsetMatrix():
	for i in range(0, 9):
		calculatedOffset = (offset * i) + (i*5)
		offsetMatrix["x"].append(startingPosition[0] + calculatedOffset)
		offsetMatrix["y"].append(startingPosition[1] + calculatedOffset)

def takeScreenShot():
	with mss.mss() as sct:
		filename = sct.shot(output="./images/screen.png", mon=2)
		print(filename)


def on_click(x, y, button, pressed):
	global counter, topLeft, newGameButton
	if pressed:
		if counter == 0:
			topLeft = tuple(int(i) for i in (x, y))
			print('Click on the "New Game" button.')
		if counter == 1:
			newGameButton = tuple(int(i) for i in (x, y))
			return False
		counter += 1


def mapCoordinates():
	print('Click on the top left corner of the grid.')
	# with Listener(on_click=on_click) as listener:
	# 	listener.join()


def takeScreenshotOfASpecificArea(topLeft, bottomRight):
	with mss.mss() as sct:
		monitor = {"top": topLeft[1], "left": topLeft[0], "width": bottomRight[0] - topLeft[0], "height": bottomRight[1] - topLeft[1]}
		return sct.grab(monitor)

def getCellCoordinates(x, y):
	calcOffSet = offsetMatrix[x][y]
	print('Position offset from starting: {0}'.format(calcOffSet))
	position = (startingPosition[0] + calcOffSet[0], startingPosition[1] + calcOffSet[1])
	print('Position:                      {0}'.format(position))
	return position

def understandTheGrid():
	x, y = 0, 0
	pyautogui.moveTo(offsetMatrix["x"][x], offsetMatrix["y"][y], duration=duration)
	# takeScreenshotOfASpecificArea()


if __name__ == '__main__':
	# takeScreenShot()
	mapCoordinates()
	
	topRight = (topLeft[0] + widthOfGrid, topLeft[1])
	bottomRight = (topLeft[0] + widthOfGrid, topLeft[1] + heightOfGrid)
	bottomLeft = (topLeft[0], topLeft[1] + heightOfGrid)
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
	# takeScreenshotOfASpecificArea(topLeft, bottomRight)
	
	# pyautogui.moveTo(topLeft, duration=duration)
	# pyautogui.moveTo(topRight, duration=duration)
	# pyautogui.moveTo(bottomRight, duration=duration)
	# pyautogui.moveTo(bottomLeft, duration=duration)
	# pyautogui.moveTo(newGameButton, duration=duration)
	understandTheGrid()

	# position = getCellCoordinates(0, 0)
			