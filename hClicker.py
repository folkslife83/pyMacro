import pyautogui
import time

lstIcon = pyautogui.locateOnScreen('images/nListIcon.png')
h1 = pyautogui.locateOnScreen('images/nH.png')
h2 = pyautogui.locateOnScreen('images/nHH.png')

if lstIcon:
    pyautogui.click(lstIcon)
    time.sleep(1)

if h1:
    print(h1)
else:
    pyautogui.click((90,600))
    time.sleep(1)
    pyautogui.typewrite(['pagedown'])
  