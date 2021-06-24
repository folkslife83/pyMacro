import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
from  tkinter import *
from  tkinter import filedialog

scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)
client = gspread.authorize(creds)
sheet = client.open("blog_list").sheet1

def hGiven():
    root = Tk()
    root.filename =  filedialog.askopenfilenames(initialdir = "C:\\Git\\pyMacro\\nHgiven",title = "choose your file",filetypes = (("txt files","*.txt"),("all files","*.*")))

    for file in root.filename:
        f=open(file, 'r')
        lines = f.readlines()
        lines = list(map(lambda s: s.strip(), lines))        
        for line in lines:
            id = line.split("=")[0]
            idClick = line.split("=")[1]
            idrow = sheet.find(id).row
            if int(idClick) >0:                
                try:
                    val = sheet.cell(idrow,5).value
                    val += int(idClick)
                except:
                    val = int(idClick)      
                sheet.update_cell(idrow,5, val)

        f.close()

def hReceive():
    root = Tk()
    root.filename =  filedialog.askopenfilenames(initialdir = "C:\\Git\\pyMacro\\nHreceive",title = "choose your file",filetypes = (("txt files","*.txt"),("all files","*.*")))
    
    for file in root.filename:
        f=open(file, 'r')
        lines = f.readlines()
        lines = list(map(lambda s: s.strip(), lines))                
        for line in lines:
            idrow = sheet.find(line).row       
            '''
            try:
                val = sheet.cell(idrow,4).value
                val += 1
            except:
                val = 1           
                
            sheet.update_cell(idrow,4, int(val))
            '''
            print(idrow)
        f.close()

hGiven()





