import xlwings as xw
#  调用表格宏命令


wb = xw.Book(r'E:\\hong-v1.0\\主算表.xlsm')
sheet = wb.sheets('Sheet1')
sheet.range('F24').value = '细粒土'
macro_var_1 = '模板确认'
macro_var_2 = '数据生成'
macro_var_3 = '数据成果导出'
macro_1 = wb.macro(macro_var_1)
macro_2 = wb.macro(macro_var_2)
macro_3 = wb.macro(macro_var_3)
macro_1()
macro_2()
macro_3()




















