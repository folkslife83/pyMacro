import win32gui
import time

def find_window_movetop():
        hwnd = win32gui.GetDesktopWindow()
        #hwnd = win32gui.FindWindow(0, "제목 없음 - Windows 메모장") 
        #hwnd = win32gui.FindWindow(0, "test.py - pyMacro - Visual Studio Code") 
        #win32gui.ShowWindow(hwnd,5)
        win32gui.SetActiveWindow()
        #win32gui.SetFocus(hwnd)
        
 
        #rect = win32gui.GetWindowRect(hwnd)
        time.sleep(0.2)
        #win32gui.SetForegroundWindow(hwnd)g
        #f = win32gui.GetFocus()
        #print(f)
        #print(win32gui.GetFocus())
        print(hwnd)
        

        #return rect 

find_window_movetop()