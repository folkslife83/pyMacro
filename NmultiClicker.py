import pyautogui
import time
import NiconClicker
import Nheart

from tkinter import *
import tkinter.ttk as ttk


def mult(num1, num2, num3):   
 
    pyautogui.click((3,500))
    time.sleep(0.2)
    pyautogui.typewrite(['home'])
    heartMax = num2
    pgMax = num3 #맥스 활동량, 클릭, pgdn 합계

    for i in range(num1):
        NiconClicker.icon()
        time.sleep(0.5)
        Nheart.heart(pgMax, heartMax)

        pyautogui.click((3,500))
        pyautogui.hotkey('ctrl','w')


def multSimul(num1, num2, num3):   
 
    pyautogui.click((3,500))
    time.sleep(0.2)
    pyautogui.typewrite(['home'])
    heartMax = num2
    pgMax = num3 #맥스 활동량, 클릭, pgdn 합계

    for i in range(num1):
        NiconClicker.icon()
        time.sleep(0.5)
        Nheart.heartSimul(pgMax, heartMax)

        pyautogui.click((3,500))
        pyautogui.hotkey('ctrl','w')



def okClick():
    num1 = int(combx.get())
    num2 = int(combxH.get())
    num3 = int(combxP.get())
    mult(num1, num2, num3)

def okClickSimul():
    num1 = int(combx.get())
    num2 = int(combxH.get())
    num3 = int(combxP.get())
    multSimul(num1, num2, num3)

win = Tk()
win.geometry("300x250+1300+100")
win.resizable(False,False)
win.title("execute")

label=Label(win, text="작업대상 웹페이지 수 선택")
label.pack()

val = [str(i) for i in (1,5,10,30, 50, 100)]
combx = ttk.Combobox(win, height=5, values=val)
combx.set(10)
combx.pack()



label=Label(win, text="좋아요 최대 클릭수")
label.pack()

valH = [str(i) for i in (1,3,5, 10)]
combxH = ttk.Combobox(win, height=5, values=val)
combxH.set(5)
combxH.pack()

label=Label(win, text="탐색 페이지 수")
label.pack()

valP = [str(i) for i in (1,3,5, 10)]
combxP = ttk.Combobox(win, height=5, values=val)
combxP.set(5)
combxP.pack()

btn = Button(win, text = "실행", overrelief="solid", width=15, command=okClick)
btn.pack()

btn2 = Button(win, text = "모의탐색", overrelief="solid", width=15, command=okClickSimul)
btn2.pack()

win.mainloop()




