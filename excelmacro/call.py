import xlwings as xw
from blog import views
#  调用表格宏命令


wb = xw.Book(r'../outcome/001.xlsx')
sheet = wb.sheets('Sheet1')

v1 = views.search().get()
sheet.range('A1').value = v1






















