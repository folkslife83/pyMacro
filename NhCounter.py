import pyautogui
import time
import random
import webbrowser
from openpyxl import load_workbook
import webbrowser
from tkinter import *
import tkinter.ttk as ttk
from _tkinter import TclError
import time, ctypes
pyautogui.FAILSAFE = False

def brR():
    pyautogui.click((10,200))
    time.sleep(0.2)
    pyautogui.hotkey('win','up')
    time.sleep(0.2)
    pyautogui.hotkey('win','left')
    time.sleep(1)
    pyautogui.hotkey('ctrl','-')
    time.sleep(0.2)
    pyautogui.hotkey('ctrl','-')
    time.sleep(0.2)
    pyautogui.hotkey('ctrl','-')
    time.sleep(1)
   

def nCount():
    url = "https://blog.naver.com/folkslife/222369468311"
    webbrowser.open(url)
    time.sleep(1)
    brR()
    
def get_clipboard():
    root = Tk()
    root.withdraw()
    result = None
    try:
        result = root.clipboard_get()
    except TclError as e:
        print('empty clipboard')
    return result

def getUrl():
    pyautogui.click(button='right')
    time.sleep(0.5)
    pyautogui.typewrite(['e'])
    return get_clipboard()

def count():
    pyautogui.moveTo((240,230))
    url = ""
    urlList=[]
    dup = 0
    while True:        
        if url != getUrl():
            url = get_clipboard()
            dup = 0
            time.sleep(0.2)
            urlList.append(url)
            time.sleep(0.2)
            pyautogui.typewrite(['down'])
            time.sleep(0.5)

        elif dup < 2:
            pyautogui.typewrite(['down'])            
            dup += 1
        
        else:
            break

    

    pyautogui.click(button='right')
    time.sleep(0.5)
    pyautogui.typewrite(['e'])










