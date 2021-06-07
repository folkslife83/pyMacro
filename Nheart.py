import pyautogui
import time


def heart():
    
    ranT = 0
    cnt = 0
    heart = 0
    cntMax = 100

    while cnt< cntMax:
        pyautogui.click((1200,500))
        h1 = pyautogui.locateAllOnScreen('images/nH.png', grayscale=True)
        h2 = pyautogui.locateAllOnScreen('images/nHH.png', grayscale=True)
        
        for im1 in h1:
            pyautogui.moveTo(im1)
            pyautogui.click(im1)
            heart += 1
            cnt += 1

        for im2 in h2:
            pyautogui.moveTo(im2)
            pyautogui.click(im2)
            heart += 1
            cnt += 1

        time.sleep(ranT)
        pyautogui.click((3,500))
        time.sleep(0.2)
        pyautogui.typewrite(['pagedown'])
        
        cnt += 1
    return heart
