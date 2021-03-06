import pyautogui
from tkinter import Tk
from _tkinter import TclError
import time, ctypes
pyautogui.FAILSAFE = False

def get_clipboard():
    root = Tk()
    root.withdraw()
    result = None
    try:
        result = root.clipboard_get()
    except TclError as e:
        print('empty clipboard')
    return result


def icon():

    cnt = 0
    cntMax = 3
    confidenceVal = 0.98

    pyautogui.click((200,60)) #크롬 웹브라우저 주소창 높이 
    time.sleep(1)
    pyautogui.hotkey('ctrl','c')
    time.sleep(0.2)
    id = get_clipboard().split('/')  #클립보드 텍스트    

    pyautogui.click((10,200))
    time.sleep(0.2)
    pyautogui.typewrite(['home'])

    while cnt< cntMax:
        pyautogui.click((10,0))

        lstIcon = pyautogui.locateCenterOnScreen('images/USE/nListIcon.png', confidence = confidenceVal)
        lstIconB = pyautogui.locateCenterOnScreen('images/USE/nListIconB.png', confidence = confidenceVal)
        
   
        if(lstIcon):
            pyautogui.click(lstIcon)
            time.sleep(0.2)                    
            break        

        if(lstIconB):
            time.sleep(0.2)        
            break
        
        pyautogui.click((10,200))
        time.sleep(0.5)
        pyautogui.typewrite(['pagedown'])
        cnt += 1
    return id[-1]