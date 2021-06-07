import pyautogui
import time


def heart():
    
    ranT = 0
    cnt = 0
    heart = 0
    cntMax = 5

    while cnt< cntMax:
        pyautogui.click((1200,500))
        h1 = pyautogui.locateAllOnScreen('images/nH.png', grayscale=True)
        h2 = pyautogui.locateAllOnScreen('images/nHH.png', grayscale=True)   

        hrt = list(h1) + list(h2)
        hrt.sort(key=lambda x:x[1])
        for h in hrt:
            pyautogui.moveTo(h)
            time.sleep(0.5)

        #time.sleep(ranT)
        pyautogui.click((3,500))
        time.sleep(0.2)
        pyautogui.typewrite(['pagedown'])
        
        cnt += 1
    return heart
heart()