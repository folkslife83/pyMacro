import pyautogui
import time

#lstIcon = pyautogui.locateOnScreen('images/nListIcon.png')

h1 = pyautogui.locateOnScreen('images/nH.png')
h2 = pyautogui.locateOnScreen('images/nHH.png')

if pyautogui.click(h1) :
    print("heart")
else:
    pyautogui.click((90,601))
    time.sleep(1)
    pyautogui.typewrite(['pagedown'])
    pyautogui.typewrite(['pagedown'])
    pyautogui.typewrite(['pagedown'])