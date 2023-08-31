import mss, pyautogui
from pynput.mouse import Listener, Controller

# Globals
monitor = 1
duration = 0.1 # Duration of the mouse movement
# topLeft = (0, 0)
topLeft = (40, 267)
topRight = (0, 0)
bottomRight = (0, 0)
bottomLeft = (0, 0)
heightOfGrid = 500
widthOfGrid = 500
# newGameButton = (0, 0)
newGameButton = (2617, 687)

counter = 0
cellStartOffset = 25;
startingPosition = (0, 0)
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
		filename = sct.shot(output="./images/screen.png", mon=monitor)
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
	with Listener(on_click=on_click) as listener:
		listener.join()


def takeScreenshotOfASpecificArea(topLeft, bottomRight):
	with mss.mss() as sct:
		monitor = {"top": topLeft[1], "left": topLeft[0], "width": bottomRight[0] - topLeft[0], "height": bottomRight[1] - topLeft[1]}
		return sct.grab(monitor)


def understandTheGrid():
	x, y = 0, 0
	for y in range(0, 9):
		for x in range(0, 9):
			pyautogui.moveTo(offsetMatrix["x"][x], offsetMatrix["y"][y], duration=duration)
	pyautogui.moveTo(offsetMatrix["x"][x], offsetMatrix["y"][y], duration=duration)
	# takeScreenshotOfASpecificArea()


if __name__ == '__main__':
	takeScreenShot()
	# mapCoordinates()
	
	topRight = (topLeft[0] + widthOfGrid, topLeft[1])
	bottomRight = (topLeft[0] + widthOfGrid, topLeft[1] + heightOfGrid)
	bottomLeft = (topLeft[0], topLeft[1] + heightOfGrid)
	startingPosition = (topLeft[0] + cellStartOffset, topLeft[1] + cellStartOffset)
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
			