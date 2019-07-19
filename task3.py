import os.path, openpyxl
def folder_creation():
    os.chdir('/myproject/task')
    workbook = openpyxl.load_workbook('roughwork.xlsx')
    sheet = workbook.get_sheet_by_name('Sheet')
    col_values = [cell.value for col in sheet.iter_cols() for cell in col]
    for value in col_values:       
        folderName = value
        baseDir = '/myproject/task/task3'
        os.makedirs(os.path.join(baseDir, folderName))
        print("\nFolder created in: ", os.path.join(baseDir, folderName))
    
folder_creation()