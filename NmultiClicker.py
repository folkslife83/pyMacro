import pyautogui
import time
import NiconClicker
import Nheart
import os

from tkinter import *
import tkinter.ttk as ttk
pyautogui.FAILSAFE = False

def mult(num1, num2, num3, simul):   
    #전체화면에서 시작 또는 2,10에 브라우저 클릭되게
    pyautogui.click((10,200))
    time.sleep(0.2)
    pyautogui.hotkey('win','up')
    time.sleep(0.2)
    pyautogui.hotkey('win','left')
    time.sleep(0.2)
 
    pyautogui.hotkey('alt','space')
    time.sleep(1.5)
    pyautogui.typewrite(['s'])
    time.sleep(1.5)
    for i in range(10):
        pyautogui.typewrite(['right'])

    time.sleep(0.2)
    pyautogui.typewrite(['enter'])

    pyautogui.hotkey('alt','space')
    time.sleep(3)
    pyautogui.typewrite(['m'])
    time.sleep(1)
    pyautogui.hotkey('ctrl','down')
    pyautogui.hotkey('ctrl','down')
    pyautogui.hotkey('ctrl','down')
    time.sleep(0.2)
    pyautogui.typewrite(['enter'])

    time.sleep(0.2)

    pyautogui.typewrite(['home'])
    time.sleep(0.2)
    heartMax = num2
    pgMax = num3 #맥스 활동량, 클릭, pgdn 합계
    history = {}

    for i in range(num1):       #  i는 key, 나주에 id 값으로 바꿀것
        NiconClicker.icon()
        time.sleep(1)
        if simul:
            history[i] = Nheart.heartSimul(heartMax,pgMax)
        else:
            history[i] = Nheart.heart(heartMax,pgMax)

        pyautogui.click((10,200))
        pyautogui.hotkey('ctrl','w')



def okClick():
    num1 = int(combx.get())
    num2 = int(combxH.get())
    num3 = int(combxP.get())
    mult(num1, num2, num3,False)

def okClickSimul():
    num1 = int(combx.get())
    num2 = int(combxH.get())
    num3 = int(combxP.get())
    mult(num1, num2, num3,True)

def okClickImage1(): #집컴 home
    pathHome = os.path.realpath('images/home') 
    path = os.path.realpath('images')

    os.startfile(pathHome)
def okClickImage2(): #원장실 one
    pathOne = os.path.realpath('images/one') 
    path = os.path.realpath('images')
    os.startfile(path)
def okClickImage3(): #원장실sub
    pathOneSub = os.path.realpath('images/oneSub') 
    path = os.path.realpath('images')
    os.startfile(path)

win = Tk()
win.geometry("300x300+1300+100")
win.resizable(False,False)
win.title("execute")

btn3 = Button(win, text = "***이미지수정***집pc", overrelief="solid", width=30, command=okClickImage1)
btn3.pack()
btn4 = Button(win, text = "***이미지수정***원장실", overrelief="solid", width=30, command=okClickImage2)
btn4.pack()
btn5 = Button(win, text = "***이미지수정***원장실sub", overrelief="solid", width=30, command=okClickImage3)
btn5.pack()

label=Label(win, text="작업대상 웹페이지 수 선택")
label.pack()

val = [str(i) for i in (1,5,10,30, 50, 100, 200, 500)]
combx = ttk.Combobox(win, height=5, values=val)
combx.set(2)
combx.pack()



label=Label(win, text="좋아요 최대 클릭수")
label.pack()

valH = [str(i) for i in (1,3,5, 10)]
combxH = ttk.Combobox(win, height=5, values=valH)
combxH.set(5)
combxH.pack()

label=Label(win, text="탐색 페이지 수")
label.pack()

valP = [str(i) for i in (1,3,5, 10,30)]
combxP = ttk.Combobox(win, height=5, values=valP)
combxP.set(10)
combxP.pack()

btn = Button(win, text = "실행", overrelief="solid", width=15, command=okClick)
btn.pack()

btn2 = Button(win, text = "모의탐색", overrelief="solid", width=15, command=okClickSimul)
btn2.pack()

win.mainloop()



