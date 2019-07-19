from datetime import datetime
import os.path,shutil
now = datetime.now()
folder = now.strftime("%d-%m-%Y")
source = os.listdir("/myproject/task")
destination = ('/myproject/task/' + folder)
if os.path.exists('/myproject/task/' + folder):
    for files in source:
        if files.endswith(".jpg"):
            shutil.copy(files,destination)
if not os.path.exists('/myproject/task/' + folder):
    os.makedirs('/myproject/task/'+ folder)
    for files in source:
        if files.endswith(".jpg"):
            shutil.copy(files,destination)