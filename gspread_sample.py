import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)
client = gspread.authorize(creds)

sheet = client.open("blog_list").sheet1

#data = sheet.get_all_records()  # 시트의 모든 데이터 담기
#row = sheet.row_values(6) #6행의 데이터 담기
#col = sheet.col_values(2) #2열의 데이터 담기
#cell = sheet.cell(5,2).value
#pprint(cell)

#insertRow = ["hello", 5, "red","blue"]
#sheet.insert_row(insertRow, 5) #5행 만들고 하나씩 밀고 5행에 데이터 넣기
#sheet.delete_row(5) #5행 지우고 하나씩 올리기
#sheet.update_cell(2,1,"changed")

#sheet.getRange('D5:D').clearContent()

sheet.values_clear(sheet.col_values(4))





