import pyautogui
import time
from tkinter import Tk
from _tkinter import TclError
import time, ctypes

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
    pyautogui.click((1200,500))
    pyautogui.click((200,60)) #크롬 웹브라우저 주소창 높이 
    time.sleep(0.2)
    pyautogui.hotkey('ctrl','c')
    id = get_clipboard().split('/')  #클립보드 텍스트
    #print(id[-1])


    pyautogui.click((3,500))
    time.sleep(0.2)
    pyautogui.typewrite(['home'])

    lib = ctypes.windll.LoadLibrary('user32.dll')
    handle = lib.GetForegroundWindow()    # 활성화된 윈도우의 핸들얻음
    buffer = ctypes.create_unicode_buffer(255)    # 타이틀을 저장할 버퍼
    lib.GetWindowTextW(handle, buffer, ctypes.sizeof(buffer))    # 버퍼에 타이틀 저장
    print(buffer.value)    # 버퍼출력
    

    while cnt< cntMax:
        pyautogui.click((1200,500))
        lstIcon = pyautogui.locateOnScreen('images/nListIcon.png', grayscale=True)
        lstIcon2 = pyautogui.locateOnScreen('images/nListIcon2.png', grayscale=True)
        lstIconB = pyautogui.locateOnScreen('images/nListIconB.png', grayscale=True)
        
        if(lstIcon):
            pyautogui.click(lstIcon)                    
            break
        
        if(lstIcon2):
            pyautogui.click(lstIcon2)                    
            break

        if(lstIconB):        
            break
        
        pyautogui.click((3,500))
        time.sleep(0.2)
        pyautogui.typewrite(['pagedown'])
        cnt += 1
icon()