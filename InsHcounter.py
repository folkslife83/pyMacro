import pyautogui
import time
import datetime
import InsiconClicker
import os
import shutil
import sys
from tkinter import *
import tkinter.ttk as ttk
from _tkinter import TclError
import ctypes
import webbrowser
pyautogui.FAILSAFE = False

#Chrome창 전체화면 왼쪽, 다운로드바 없게

def get_clipboard():
    root = Tk()
    root.withdraw()
    result = None
    try:
        result = root.clipboard_get()
    except TclError as e:
        print('empty clipboard')
    return result

clipTxt = get_clipboard().split(' ')  #클립보드 텍스트    
clipTxt = [v for v in clipTxt if v]

nUrls = {} # 글번호 - url 쌍
n = len(clipTxt)
for i in range(0,n,2):
    nUrls[clipTxt[i]] = clipTxt[i+1]

output=""
for num in nUrls:
    url = nUrls[num]
    webbrowser.open(url)
    #browser 열기 url = nUrls[num]
    time.sleep(3)
    

    #리턴값으로 txt받기
    
    idLst = str(InsiconClicker.icon(num))
    output += idLst + ' '


#파일로 기록

now = datetime.datetime.today()
fname = now.strftime('%Y-%m-%d-%H%M%S')
fname = fname + ".txt"
f=open("instaTxt/"+fname, 'w',encoding="UTF8")
datas = output.split(' ')
for data in datas:
    lines = data.split('-')
    for line in lines:
        f.write(line+ "\n")
    f.write("\n")
f.close()




    




