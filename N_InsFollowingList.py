import pyautogui
import time, ctypes
import datetime
import os
import shutil
import sys
from tkinter import *
import tkinter.ttk as ttk
from tkinter import Tk
from _tkinter import TclError
import webbrowser
import random
from openpyxl import load_workbook, Workbook
from checkBR import brOK, browser
import tkinter.messagebox

pyautogui.FAILSAFE = False
coordU = (700,370)  #드래그 시작할 위치

#Chrome창 전체화면 왼쪽모니터, 다운로드바 없게

def get_clipboard():
    root = Tk()
    root.withdraw()
    result = None
    try:
        result = root.clipboard_get()
    except TclError as e:
        print('empty clipboard')
    return result

def okClick():
   
        time.sleep(1)
        confidenceVal = 0.8 #0.7은 인식불가 
        # 좋아하는 첫id가 길면 글자가 밀리는 현상
        
        clipTxt = "first"
        idList=[]
        
        while True:                        
            if clipTxt != str(get_clipboard()):
                clipTxt = str(get_clipboard())
                idList += clipTxt.split('\n')
                time.sleep(1)
                pyautogui.moveTo(coordU)
                pyautogui.drag(0,580,1,button='left')
                time.sleep(2)
                pyautogui.hotkey('ctrl','c')
                time.sleep(1)
                pyautogui.typewrite(['pagedown'])
                time.sleep(1)               
                pyautogui.click(coordU)

            else:
                break
            if len(idList) == 0:
                continue


        output = []
        for name in idList:   # 님의 프로필 사진  - 포함하는 원소만 추리기
            if '님의 프로필 사진' in name:  
                output.append(name[:-9])
            else:
                continue
        ids = set(output)
        time.sleep(1)   

        now = datetime.datetime.today()   
        fname = now.strftime('%Y-%m-%d-%H%M%S_'+"FollowingList.txt" )            
        f=open("iFollowList/"+fname, 'w',encoding="UTF8")
                
        for id in ids:
            f.write(id + "\n")
        f.close()

        time.sleep(1)
        exit()
okClick()