import pyautogui
import time
import datetime
import NiconClicker
import Nheart
import os
import shutil
import sys

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
    time.sleep(0.5)
    pyautogui.typewrite(['enter'])

    time.sleep(0.2)

    pyautogui.typewrite(['home'])
    
    

#    keepGoing = Tk()
#    keepGoing.geometry("300x150+1000+100")
#    keepGoing.title("창 위치조정이 완료 되었습니까?")
#    btOK = Button(keepGoing, text = "OK", command=winOK)
#    btFail = Button(keepGoing, text = "FAIL", command=winFail)
#    btOK.pack()
#    btFail.pack()
#    input("Please press the Enter key to proceed") #cmd 창에 엔터 눌러야 이어지는 문제

    nPages = num1
    heartMax = num2
    pgMax = num3 #맥스 활동량, 클릭, pgdn 합계
    history = {}

    for i in range(nPages):       #  i는 key, 나주에 id 값으로 바꿀것
        id=NiconClicker.icon()
        time.sleep(1)
        if simul:
            history[id] = Nheart.heartSimul(heartMax,pgMax)
        else:
            history[id] = Nheart.heart(heartMax,pgMax)

        pyautogui.click((10,200))
        pyautogui.hotkey('ctrl','w')

    
    now = datetime.datetime.today()
    fname = now.strftime('%Y-%m-%d-%H%M%S')
    if simul:
        fname = fname + "SIMULATION.txt"
    else:
        fname = fname + ".txt"
    f=open("click_given/"+fname, 'w',encoding="UTF8")
    lst = list(history.keys())

    for i in reversed(range(len(lst))):
        f.write(str(lst[i]) + "="+str(history[lst[i]])+ "\n")
    f.close()


  

def winOK():
    return True
def winFail():
    sys.exit("기존 프로그램 탐색-종료후 재실행")
    
def okClick():
    num1 = int(combx.get())
    num2 = int(combxH.get())
    num3 = int(combxP.get())
    mult(num1, num2, num3,False)        

def okClickSimul():
    num1 = int(combx.get())
    num2 = int(combxH.get())
    num3 = int(combxP.get())
    mult(num1, num2, num3, True)    

def okClickImage1(): #집컴 home
    pathHome = os.path.realpath('images/home') 
    path = os.path.realpath('images/USE')
    files = os.listdir(pathHome)
    for file in files:
        shutil.copyfile(pathHome+'/'+file, path+'/'+file)

def okClickImage2(): #원장실 one
    pathOne = os.path.realpath('images/one') 
    path = os.path.realpath('images/USE')
    files = os.listdir(pathOne)
    for file in files:
        shutil.copyfile(pathOne+'/'+file, path+'/'+file)


def okClickImage3(): #원장실sub
    pathOneSub = os.path.realpath('images/oneSub') 
    path = os.path.realpath('images/USE')
    files = os.listdir(pathOneSub)
    for file in files:
        shutil.copyfile(pathOneSub+'/'+file, path+'/'+file)


win = Tk()
win.geometry("500x500+1300+100")
win.resizable(True,True)
win.title("execute")

label1=Label(win, text="*Chrome 가장왼쪽모니터 전체화면")
label1.pack()
label1_1=Label(win, text="***창열기전 네이버로그인필수***")
label1_1.pack()

btn3 = Button(win, text = "***이미지수정***집pc", overrelief="solid", width=30, command=okClickImage1)
btn3.pack()
btn4 = Button(win, text = "***이미지수정***원장실", overrelief="solid", width=30, command=okClickImage2)
btn4.pack()
btn5 = Button(win, text = "***이미지수정***원장실sub", overrelief="solid", width=30, command=okClickImage3)
btn5.pack()

label2=Label(win, text="작업대상 웹페이지 수 선택")
label2.pack()

val = [str(i) for i in (1,5,10,30, 50, 100, 200, 500)]
combx = ttk.Combobox(win, height=5, values=val)
combx.set(200)
combx.pack()



label3=Label(win, text="좋아요 최대 클릭수")
label3.pack()

valH = [str(i) for i in (1,3,5, 10)]
combxH = ttk.Combobox(win, height=5, values=valH)
combxH.set(3)
combxH.pack()

label4=Label(win, text="탐색 페이지 수")
label4.pack()

valP = [str(i) for i in (1,3,5, 10,30)]
combxP = ttk.Combobox(win, height=5, values=valP)
combxP.set(5)
combxP.pack()

btn1 = Button(win, text = "실행", overrelief="solid", width=15, command=okClick)
btn1.pack()

btn2 = Button(win, text = "모의탐색", overrelief="solid", width=15, command=okClickSimul)
btn2.pack()

win.mainloop()



