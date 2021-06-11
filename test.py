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
    for i in id:
        if i.find('blogId='):
            lst.append(i)

    lst = [v for v in lst if v] #빈문자열 제거

    print(lst)


icon()