import pyautogui
import time
import NiconClicker
import Nheart

from tkinter import *
import tkinter.ttk as ttk


def mult(num1, num2, num3, simul):   
    #전체화면에서 시작 또는 2,10에 브라우저 클릭되게
    pyautogui.click((1,5))
    time.sleep(0.2)
    pyautogui.hotkey('win','up')
    time.sleep(0.2)
    pyautogui.hotkey('win','left')
    time.sleep(0.2)
 
    pyautogui.hotkey('alt','space')
    time.sleep(1)
    pyautogui.typewrite(['s'])
    time.sleep(0.2)
    for i in range(10):
        pyautogui.typewrite(['right'])

    time.sleep(0.2)
    pyautogui.typewrite(['enter'])

    pyautogui.hotkey('alt','space')
    time.sleep(1)
    pyautogui.typewrite(['m'])
    time.sleep(0.2)
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

        pyautogui.click((1,5))
        pyautogui.hotkey('ctrl','w')
        print(history)


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

win = Tk()
win.geometry("300x250+1300+100")
win.resizable(False,False)
win.title("execute")

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



