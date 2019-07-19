from datetime import datetime
import os.path,shutil
now = datetime.now()
folder = now.strftime("%d-%m-%Y")
source = os.listdir("C:\myproject\\task")
destination = ('C:\myproject\\task\\' + folder)
if os.path.exists('c:\\myproject\\task\\' + folder):
    for files in source:
        if files.endswith(".jpg"):
            shutil.copy(files,destination)
if not os.path.exists('c:\\myproject\\task\\' + folder):
    os.makedirs('C:\\myproject\\task\\'+ folder)
    for files in source:
        if files.endswith(".jpg"):
            shutil.copy(files,destination)