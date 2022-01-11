import pyautogui, time
from datetime import datetime

timeCheck = datetime.now().strftime("%H:%M:%S")

try:
    while timeCheck < '16:00:00' or timeCheck > '9:00:00':
        pyautogui.moveTo(1, 2, duration=.25)
        pyautogui.press('shift')
        time.sleep(300)
        pyautogui.moveTo(2, 1, duration=.25)
        pyautogui.press('shift')
        time.sleep(300)
except KeyboardInterrupt:
    print("user interrupted")
    pass
