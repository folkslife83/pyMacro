import pyautogui
import time, ctypes
import datetime
import os
import shutil
import sys
from tkinter import *
import tkinter.ttk as ttk
from tkinter import Tk
from _tkinter import TclError
import webbrowser
import random
from openpyxl import load_workbook, Workbook
from checkBR import brOK, browser
import tkinter.messagebox
import os
pyautogui.FAILSAFE = False
confidenceVal = 0.8

#m = pyautogui.locateCenterOnScreen('images/USE/iHm.png', confidence = confidenceVal)

#print (m)

m1 = (760,273)
m = (760, 960)

pyautogui.moveTo(m)
