from tkinter import Tk

clip = Tk()                        # 창 생성
clip.withdraw()                  # 창이 보이지 않도록 너비 조정

def a():                           # 편한 사용을 위한 함수1(상용구 느낌)
    clip.clipboard_clear() 
    clip.clipboard_append("Copy data 1")
   

def b():                           # 편한 사용을 위한 함수2(상용구 느낌)
    clip.clipboard_clear() 
    clip.clipboard_append("Copy data 2")
a()