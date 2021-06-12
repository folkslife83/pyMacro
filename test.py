import pyautogui
from tkinter import Tk
from _tkinter import TclError
import time, ctypes
pyautogui.FAILSAFE = False

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

    lst = []
    id = get_clipboard().split('\n')  #클립보드 텍스트    
    id =  [v for v in id if v] #빈문자열 제거
    for i in id[6:]:
        if i.find('blogId='):
            lst.append(i)

    for one in lst:
        print(one.split('=')[-1])


icon()