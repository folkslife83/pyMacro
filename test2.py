import pyautogui
import time

def icon():

    cnt = 0
    cntMax = 3
    confidenceVal = 0.8

    pyautogui.click((3,500))
    time.sleep(0.2)
    pyautogui.typewrite(['home'])

    while cnt< cntMax:
        pyautogui.click((1200,500))

        lstIcon = pyautogui.locateOnScreen('images/nListIcon.png', confidence = confidenceVal)
        lstIconB = pyautogui.locateOnScreen('images/nListIconB.png', confidence = confidenceVal)
        
   
        if(lstIcon):
            pyautogui.click(lstIcon)                    
            break        

        if(lstIconB):        
            break
        
        pyautogui.click((3,500))
        time.sleep(0.2)
        pyautogui.typewrite(['pagedown'])
        cnt += 1
