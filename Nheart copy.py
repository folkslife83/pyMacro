import pyautogui
import time
import random


def heart(numHeart, numPages):
    
    cnt_p = 0
    heartTotal = 0
    confidenceVal = 0.8
    cntH = numHeart
    cntP = numPages

    while heartTotal < cntH and cnt_p < cntP :
        pyautogui.click((0,0))
  
  

        h1 = pyautogui.locateAllOnScreen('images/nH.png', confidence = confidenceVal)
        h2 = pyautogui.locateAllOnScreen('images/nHH.png', confidence = confidenceVal)   

        hrt = list(h1) + list(h2)
        hrt.sort(key=lambda x:x[1])
        for h in hrt:
            if heartTotal >= cntH:
                break
            #pyautogui.moveTo(h)
            pyautogui.click(h)
            time.sleep(random.random()) #0과 1사이값
            time.sleep(random.random()) #0과 1사이값
            heartTotal += 1   

        pyautogui.click((2,50))
        time.sleep(0.2)
        pyautogui.typewrite(['pagedown'])
        
        cnt_p += 1

    return heartTotal


def heartSimul(numHeart, numPages):
    

    cnt_p = 0
    heartTotal = 0
    confidenceVal = 0.8
    cntH = numHeart
    cntP = numPages

    while heartTotal < cntH and cnt_p < cntP :
        pyautogui.click((0,0))
  
  

        h1 = pyautogui.locateAllOnScreen('images/nH.png', confidence = confidenceVal)
        h2 = pyautogui.locateAllOnScreen('images/nHH.png', confidence = confidenceVal)   

        hrt = list(h1) + list(h2)
        hrt.sort(key=lambda x:x[1])
        for h in hrt:
            if heartTotal >= cntH:
                break
            pyautogui.moveTo(h)
            #pyautogui.click(h)
            time.sleep(random.random()) #0과 1사이값
            time.sleep(random.random()) #0과 1사이값
            heartTotal += 1   

        pyautogui.click((2,50))
        time.sleep(0.2)
        pyautogui.typewrite(['pagedown'])
        
        cnt_p += 1

    return heartTotal
heart(1000, 200)