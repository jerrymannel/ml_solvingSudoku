from pynput.mouse import Listener

def on_click(x, y, button, pressed):
	if pressed:
		print('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))



with Listener(on_click=on_click) as listener:
	listener.join()


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
