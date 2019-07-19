from datetime import datetime
import os.path,xlsxwriter
now = datetime.now()
folder = now.strftime("%d-%m-%Y")
source = os.listdir("/myproject/task")
def task2(excel):
    if os.path.exists('/myproject/task/' + folder):
workbook = xlsxwriter.Workbook('hello.xlsx') 
worksheet = workbook.add_worksheet()
row = 0
column = 0
content = [source]
for item in content : 
    worksheet.write(row, column, item) 
    row += 1
      
workbook.close() 

 