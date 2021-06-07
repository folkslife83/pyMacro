import pyautogui
import time
import random


def heart(numHeart, numPages):
    
    cnt_h = 0
    cnt_p = 0
    heartTotal = 0
    cntH = numHeart
    cntP = numPages

    while cnt_h < cntH and cnt_p < cntP :
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
            cnt_h += 1
        
    
        pyautogui.click((3,500))
        time.sleep(0.2)
        pyautogui.typewrite(['pagedown'])
        
        cnt_p += 1

    return heartTotal
heart(5,5)