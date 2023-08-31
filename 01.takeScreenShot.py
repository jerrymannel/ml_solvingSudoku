import pyautogui
import mss

# import time
# time.sleep(2)

screenshot = pyautogui.screenshot('screenshot.png')
screenshot.save(r'./images/screen.png')


with mss.mss() as sct:
  filename = sct.shot(output="./images/screen2.png", mon=2)
  # sct.save()
  print(filename)