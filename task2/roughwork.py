import xlsxwriter 
  
workbook = xlsxwriter.Workbook('hello.xlsx') 
worksheet = workbook.add_worksheet()
row = 0
column = 0
  
content = ["ankit", "rahul", "priya", "harshita", 
                    "sumit", "neeraj", "shivam"] 
for item in content : 
    worksheet.write(row, column, item) 
    row += 1
      
workbook.close() 