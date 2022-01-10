import pyautogui, time
from datetime import datetime

timeCheck = datetime.now().strftime("%H:%M:%S")

try:
    while timeCheck < '16:00:00' or timeCheck > '9:00:00':
        pyautogui.moveTo(1000, 700, duration=.25)
        time.sleep(600)
        pyautogui.moveTo(700, 1000, duration=.25)
        time.sleep(600)
except KeyboardInterrupt:
    pass
