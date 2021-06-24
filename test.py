from  tkinter import *
from  tkinter import filedialog

root = Tk()
root.filename =  filedialog.askopenfilenames(initialdir = "C:\\Git\\pyMacro\\nHgiven",title = "choose your file",filetypes = (("txt files","*.txt"),("all files","*.*")))
print (len(root.filename))
