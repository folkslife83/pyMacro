import pyautogui
import time
import NiconClicker
import Nheart

from tkinter import *
import tkinter.ttk as ttk

def mult(num):   
    ranT = 0
    pyautogui.click((3,500))
    time.sleep(0.2)
    pyautogui.typewrite(['home'])

    for i in range(num):
        NiconClicker.icon()
        time.sleep(0.5)
        Nheart.heart()

        pyautogui.click((3,500))
        pyautogui.hotkey('ctrl','w')

def okClick():
    num = int(combx.get())
    mult(num)

win = Tk()
win.geometry("300x250+1300+100")
win.resizable(False,False)
win.title("execute")
label=Label(win, text="작업량 선택")
label.pack()

val = [str(i) for i in (1,5,10,30, 50, 100)]
combx = ttk.Combobox(win, height=5, values=val)
combx.set(0)
combx.pack()

btn = Button(win, text = "실행", overrelief="solid", width=15, command=okClick)
btn.pack()
win.mainloop()


