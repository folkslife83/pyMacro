import pyautogui
from tkinter import Tk
from _tkinter import TclError
import time, ctypes
pyautogui.FAILSAFE = False

coordU = (1135, 420)
coordD = (1135, 740)


def get_clipboard():
    root = Tk()
    root.withdraw()
    result = None
    try:
        result = root.clipboard_get()
    except TclError as e:
        print('empty clipboard')
    return result


def icon(num):
    
    confidenceVal = 0.5 #0.7은 인식불가
    # 좋아하는 첫id가 길면 글자가 밀리는 현상
    nLikeThis = pyautogui.locateCenterOnScreen('images/USE/iH.png', confidence = confidenceVal)

    print(nLikeThis)
    if(nLikeThis):
        pyautogui.click(nLikeThis)
        time.sleep(2)
    else:
        return

    
    clipTxt = ""
    idList=[]

    while True:
        if clipTxt != get_clipboard():
            clipTxt = get_clipboard()
            time.sleep(1)
            pyautogui.moveTo(coordU)
            pyautogui.drag(0,330,1,button='left')
            time.sleep(1)
            pyautogui.hotkey('ctrl','c')
            time.sleep(1)
            idList += clipTxt.split('\n')
            pyautogui.typewrite(['pagedown'])
            time.sleep(1)
            pyautogui.click(coordU)

        else:
            break

    txtSet = set(idList) #세트로 바꾸면 중복이 사라짐
    # 님의 프로필 사진  - 포함하는 원소만 추리기
    output = str(num)

    for name in txtSet:
        if '님의 프로필 사진' in name:
            output += '-'+ name[:-9]
        else:
            continue
    time.sleep(1)   
    pyautogui.hotkey('ctrl','w')

    return output
