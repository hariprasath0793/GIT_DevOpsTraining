from datetime import datetime
import os.path,xlsxwriter
now = datetime.now()
folder = now.strftime("%d-%m-%Y")
source = os.walk('/myproject/task/task2')
def excel():
    if os.path.exists('/myproject/task/' + folder):
        workbook = xlsxwriter.Workbook('roughwork.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.write(0,0, "Folder name")
        worksheet.write(0,1, "Files")
        row = 1
        column = 0
    for root, dirs, files in source:
        worksheet.write_column(row , column , dirs)
        column += 1
        worksheet.write_column(row, column, files)
        row += 1
    workbook.close()
    if not os.path.exists('/myproject/task/' + folder):
        print ("Folder for today does not exist")
excel()