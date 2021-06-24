import pyautogui
import time
import datetime
import os
import shutil
import sys
import webbrowser
import random
from sys import exit
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
import tkinter.ttk as ttk
pyautogui.FAILSAFE = False
from checkBR import brOK, browser
confidenceVal = 0.9

outClick = (10,0)
inClick = (10,200)
picClick = (10,770)
picCenter = (450,450)
picSearch = (300,170)

def mult(maxP):    


    url = ("https://www.instagram.com/")
    webbrowser.open(url)  
    time.sleep(3)
    browser()
    time.sleep(1)
    for k in range (5):
        time.sleep(0.5)
        pyautogui.hotkey('ctrl','+')
    time.sleep(0.5)
    brOK()

    root = Tk() 
    root.filename = tkinter.filedialog.askopenfilenames(initialdir = "C:\\Git\\pyMacro\\iHreceive\\",title = "choose your file",filetypes = (("txt files","*.txt"),("all files","*.*")))
    idList = []
    for file in root.filename:
        f=open(file, 'r')
        lines = f.readlines()
        lines = list(map(lambda s: s.strip(), lines))        
        for line in lines:
            if line not in idList:
                idList.append(line)
        f.close()
    
    print(idList)
    now = datetime.datetime.today()  
    fname = now.strftime('%Y-%m-%d-%H%M'+ '.txt')
    f=open("C:\\Git\\pyMacro\\iHgiven\\"+fname, 'w',encoding="UTF8") #실행 날짜로 파일 만들기
    for id in idList:
        f.write(id + "\n")
    f.close()


    for id in idList:
        copy_string = "echo " + str(id) + " |clip"
        os.system(copy_string)         #클립보드에 id올리기
        
        time.sleep(1)
        pyautogui.click(picSearch)
        time.sleep(1)
        pyautogui.click(picSearch)        
        time.sleep(1)
        pyautogui.hotkey('ctrl','a')
        time.sleep(0.5)
        pyautogui.typewrite(['del'])


        pyautogui.hotkey('ctrl','v')
        time.sleep(2)
        pyautogui.typewrite(['enter'])
        time.sleep(2)
        pyautogui.typewrite(['enter'])
        time.sleep(2)
        pyautogui.typewrite(['esc'])
        time.sleep(1)
        pyautogui.typewrite(['esc'])
        time.sleep(1)
        pyautogui.typewrite(['pgdn'])
        time.sleep(1)
        pyautogui.click(picClick)        
        time.sleep(2)        
        time.sleep(random.random()) #0과 1사이값
        pyautogui.click(picCenter)        
        time.sleep(2)
        time.sleep(random.random()) #0과 1사이값

        for k in range(9):
            pyautogui.typewrite(['left'])
            time.sleep(0.2)

        cnt =0
        time.sleep(2)
        for k in range(maxP):
            pyautogui.moveTo(picCenter)
            time.sleep(0.5)
            pyautogui.scroll(-10000)
            time.sleep(0.5)
            Hempty = pyautogui.locateCenterOnScreen('images/USE/iHb.png', confidence = confidenceVal)
            #Hfull = pyautogui.locateCenterOnScreen('images/USE/iHr.png', confidence = confidenceVal)
            if Hempty:
                pyautogui.click(Hempty)
                cnt += 1
                time.sleep(random.random()) #0과 1사이값
                pyautogui.typewrite(['right'])
                
            else:
                pyautogui.typewrite(['right'])
        
        
        
        f=open("C:\\Git\\pyMacro\\iHgiven\\"+fname, 'a',encoding="UTF8")
        f.write(id+"="+str(cnt) + "\n")
        f.close()
        time.sleep(random.random()) #0과 1사이값
        cnt = 0
        pyautogui.typewrite(['esc'])
        time.sleep(1) 


    time.sleep(2)
    exit()


   
def okClick():    
    maxP = int(combxP.get())
    
    mult(maxP)        



def okClickImage1(): #집컴 home
    pathHome = os.path.realpath('images/home') 
    path = os.path.realpath('images/USE')
    files = os.listdir(pathHome)
    for file in files:
        shutil.copyfile(pathHome+'/'+file, path+'/'+file)
    Msgbox1()

def okClickImage2(): #원장실 one
    pathOne = os.path.realpath('images/one') 
    path = os.path.realpath('images/USE')
    files = os.listdir(pathOne)
    for file in files:
        shutil.copyfile(pathOne+'/'+file, path+'/'+file)
    Msgbox1()

def okClickImage3(): #원장실sub
    pathOneSub = os.path.realpath('images/oneSub') 
    path = os.path.realpath('images/USE')
    files = os.listdir(pathOneSub)
    for file in files:
        shutil.copyfile(pathOneSub+'/'+file, path+'/'+file)
    Msgbox1()

def Msgbox1():
    tkinter.messagebox.showinfo("Inform","Image files've been copied.")

win = Tk()
win.geometry("500x500+1300+100")
win.resizable(True,True)
win.title("execute")

label1=Label(win, text="*Chrome 가장왼쪽모니터 전체화면")
label1.pack()
label1_1=Label(win, text="***인스타로그인/200%확대확인***")
label1_1.pack()

btn3 = Button(win, text = "***이미지수정***집pc", overrelief="solid", width=30, command=okClickImage1)
btn3.pack()
btn4 = Button(win, text = "***이미지수정***원장실", overrelief="solid", width=30, command=okClickImage2)
btn4.pack()
btn5 = Button(win, text = "***이미지수정***원장실sub", overrelief="solid", width=30, command=okClickImage3)
btn5.pack()

label4=Label(win, text="탐색 페이지 수")
label4.pack()

valP = [str(i) for i in (1,3,5, 10,30)]
combxP = ttk.Combobox(win, height=5, values=valP)
combxP.set(2)
combxP.pack()

btn1 = Button(win, text = "실행", background="cornflowerblue",overrelief="solid", width=15, command=okClick)
btn1.pack()

win.mainloop()



