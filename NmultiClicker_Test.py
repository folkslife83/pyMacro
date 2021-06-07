import pyautogui
import time
import NiconClicker
import Nheart

def mult(num):
    
    ranT = 0
    pyautogui.click((3,500))
    time.sleep(0.2)
    pyautogui.typewrite(['home'])

    for i in range(num):
        NiconClicker.icon()        
        pyautogui.click((3,500))
        pyautogui.hotkey('ctrl','w')


mult(10)




