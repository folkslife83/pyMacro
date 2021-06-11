import pyautogui
import time
from tkinter import *
from sys import exit

class brOK():
    def __init__(self):
        self.root = Tk()
        self.root.geometry('200x100+1300+0')
        self.root.resizable(True,True)
        self.root.title("CONFIRM WINDOW")
        button = Button(self.root, text = '시작', command=self.OK)
        button.pack()
        button2 = Button(self.root, text = '나가기', command=self.FAIL)
        button2.pack()
       
        self.root.mainloop()

    def OK(self):
        self.root.quit()
        self.root.destroy()
    def FAIL(self):
        #self.root.destroy() #브라우저 확인창만 닫기
        exit()  #전체 프로그램 종료
    

def browser():
    #전체화면에서 시작 또는 2,10에 브라우저 클릭되게
    pyautogui.click((10,200))
    time.sleep(0.2)
    pyautogui.hotkey('win','up')
    time.sleep(0.2)
    pyautogui.hotkey('win','left')
    time.sleep(0.2)
 
    pyautogui.hotkey('alt','space')
    time.sleep(2)
    pyautogui.typewrite(['s'])
    time.sleep(2)
    for i in range(10):
        pyautogui.typewrite(['right'])
        time.sleep(0.2)

    time.sleep(0.2)
    pyautogui.typewrite(['enter'])
    time.sleep(1)

    pyautogui.hotkey('alt','space')
    time.sleep(2)
    pyautogui.typewrite(['m'])
    time.sleep(1)
    pyautogui.hotkey('ctrl','down')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl','down')
    time.sleep(0.5)
    pyautogui.hotkey('ctrl','down')
    time.sleep(1)
    pyautogui.typewrite(['enter'])
    time.sleep(1)

    pyautogui.typewrite(['home'])
    