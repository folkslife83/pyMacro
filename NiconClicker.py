import pyautogui
import time
pyautogui.FAILSAFE = False
def icon():

    cnt = 0
    cntMax = 3
    confidenceVal = 0.98

    pyautogui.click((10,200))
    time.sleep(0.2)
    pyautogui.typewrite(['home'])

    while cnt< cntMax:
        pyautogui.click((10,0))

        lstIcon = pyautogui.locateCenterOnScreen('images/USE/nListIcon.png', confidence = confidenceVal)
        lstIconB = pyautogui.locateCenterOnScreen('images/USE/nListIconB.png', confidence = confidenceVal)
        
   
        if(lstIcon):
            pyautogui.click(lstIcon)                    
            break        

        if(lstIconB):        
            break
        
        pyautogui.click((10,200))
        time.sleep(0.2)
        pyautogui.typewrite(['pagedown'])
        cnt += 1
