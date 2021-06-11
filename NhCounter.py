import pyautogui
import time
import random
import webbrowser
from openpyxl import load_workbook, Workbook
import webbrowser
from tkinter import *
import tkinter.ttk as ttk
from _tkinter import TclError
import time, ctypes
from checkBR import brOK
pyautogui.FAILSAFE = False

# 네이버 로그인확인
# 왼쪽 모니터에 100% 배율상태확인
npages = 10 #최대 댓글이 매우 큰 숫자일 경우 높여준다.

def get_clipboard():
    root = Tk()
    root.withdraw()
    result = None
    try:
        result = root.clipboard_get()
    except TclError as e:
        print('empty clipboard')
    return result


def open(docNum):
    url = "https://m.blog.naver.com/SympathyHistoryList.naver?blogId=folkslife&logNo="+ str(docNum) + "&categoryId=POST"
    webbrowser.open(url)
    time.sleep(1)
    

def count():
    time.sleep(1)
    pyautogui.click((450,140))

    for i in range(npages):
        time.sleep(0.5)
        pyautogui.typewrite(['end'])

    time.sleep(0.5)
    pyautogui.hotkey('ctrl','c') 
    time.sleep(0.5)

    pyautogui.click(1100,300)
    time.sleep(1)
    pyautogui.click(button='right')
    time.sleep(1)
    pyautogui.typewrite(['p'])
    time.sleep(1)
    pyautogui.hotkey('ctrl','q') 
    time.sleep(1)
    pyautogui.click((1600,300))
    time.sleep(1)
    pyautogui.typewrite(['space'])
    time.sleep(1)
    pyautogui.hotkey('ctrl','c') 
    time.sleep(0.5)

    id = get_clipboard().split('\n')


    



    url = ""
    urlList=[]
    dup = 0
    while True:        
        if url != getUrl():
            url = get_clipboard()
            dup = 0
            time.sleep(0.5)
            urlList.append(url.split("=")[-1]) 
            # url예시 https://m.blog.naver.com/PostList.naver?blogId=flush6788
            time.sleep(1)
            pyautogui.typewrite(['down'])
            time.sleep(1)

        elif dup < 2:
            time.sleep(1)
            pyautogui.typewrite(['down'])            
            time.sleep(1)
            dup += 1
        
        else:
            break

    for i in range (17):
        pyautogui.move(0,46) #아래로 46px
        time.sleep(0.2)
        url = getUrl()
        time.sleep(0.2)
        urlList.append(url.split("=")[-1])
        time.sleep(0.2)   
    pyautogui.click(50,500)  
    time.sleep(1)
    pyautogui.hotkey('ctrl','w') 
    time.sleep(1)
    return set(urlList)   #중복제거, 순서상관없음

def okClick():
    num1 = int(input_docNum1.get())
    num2 = int(input_docNum2.get())
    mult(num1, num2)

def mult(num1, num2):
    url_test = ("https://m.blog.naver.com/folkslife")
    webbrowser.open(url_test)  
    time.sleep(0.5)
    brOK()

    load_wb = load_workbook("blog_list.xlsm", data_only=True)
    load_ws = load_wb['name'] #시트 이름으로 불러오기
    last_row = load_wb.active.max_row
    lrow = int(last_row)

    if num1 < 1:                    #시작글번호
            docNum1 = 1
    elif num1> lrow-4:
        docNum1 = lrow-4
    else:
        docNum1 = num1  
    
    if  docNum1 > num2: 
        docNum2 = docNum1
    else:
        docNum2 = num2
    print(lrow)
    for i in range (lrow-4):
        docNum = int(load_ws.cell(i+5,1).value) #글번호
        print(docNum)
        
        if docNum > docNum2 :
            continue
        if docNum < docNum1 :
            break

        num = (load_ws.cell(i+5,2).value).split('/')[-1]
        open(num)
        iDic = {}
        iDic[docNum] = count()
        time.sleep(1)
    
    kList = iDic.keys()
    print(kList)

    brB() #브라우저 배율 원복
    time.sleep(1)
    exit()



            

win = Tk()
win.geometry("320x150+1300+100")
win.resizable(True,True)
win.title("H counter")

label1=Label(win, text="*Chrome 가장왼쪽모니터 100%배율* ")
label1.pack()
label2=Label(win, text="***창열기전 네이버로그인//hLink열기!!!***")
label2.pack()

label3=Label(win, text="시작 글번호")
label3.pack()
input_docNum1 = Entry (win, width = 15)
input_docNum1.insert(0, 1)

label4=Label(win, text="마지막 글번호")
label4.pack()
input_docNum2 = Entry (win, width = 15)

btn1 = Button(win, text = "실행", background="cornflowerblue",overrelief="solid", width=15, command=okClick)
btn1.pack()

label3.place(x=30, y=50)
label4.place(x=180, y=50)
input_docNum1.place(x=30, y=70)
input_docNum2.place(x=180, y=70)
btn1.place(x=105,y=100)

win.mainloop()




