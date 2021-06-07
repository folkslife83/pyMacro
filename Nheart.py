import pyautogui
import time
import random


def heart(num):
    
    cnt = 0
    heartTotal = 0
    cntMax = num

    while cnt< cntMax:
        pyautogui.click((1200,500))
  
        h1 = pyautogui.locateAllOnScreen('images/nH.png', grayscale=True)
        h2 = pyautogui.locateAllOnScreen('images/nHH.png', grayscale=True)   

        hrt = list(h1) + list(h2)
        hrt.sort(key=lambda x:x[1])
        for h in hrt:
            pyautogui.moveTo(h)
            #pyautogui.click(h)
            time.sleep(random.random()) #0과 1사이값
            heartTotal += 1
            cnt += 1
        
    
        pyautogui.click((3,500))
        time.sleep(0.2)
        pyautogui.typewrite(['pagedown'])
        
        cnt += 1
    return heartTotal
