import pyautogui
import time

def icon():

    ranT = 0
    cnt = 0
    cntMax = 3

    while cnt< cntMax:
        pyautogui.click((1200,500))
        time.sleep(2)    
        lstIcon = pyautogui.locateOnScreen('images/nListIcon.png', grayscale=True)
        lstIcon2 = pyautogui.locateOnScreen('images/nListIcon2.png', grayscale=True)
        lstIconB = pyautogui.locateOnScreen('images/nListIconB.png', grayscale=True)
        
        if(lstIcon):
            pyautogui.click(lstIcon)        
            time.sleep(ranT)
            break
        
        if(lstIcon2):
            pyautogui.click(lstIcon2)        
            time.sleep(ranT)
            break
        
        if(lstIconB):        
            break
        
        pyautogui.click((3,500))
        time.sleep(0.2)
        pyautogui.typewrite(['pagedown'])
        cnt += 1
