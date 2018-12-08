# -*- coding: utf-8 -*-
# @Time    : 2018/12/5 11:23
# @Author  : Xiao



import xlrd,xlwt,xlutils,os
from xlutils.copy import copy
book=xlrd.open_workbook('stu.xls')#打开一个excel文件对象
sheet=book.sheet_by_name('Sheet1')#通过sheet 名称指定工作sheet
# sheet=book.sheet_by_index(0)#通过sheet 索引指定工作sheet
all_sheets=book.sheet_names()#获取所有sheet名称，返回一个list
print(all_sheets)
print(sheet.cell(0,0).value)#通过cell获取指定坐标的数据
print(sheet.nrows)#获取sheet页的行数
print(sheet.ncols)#获取sheet页的列数
print(sheet.row_values(0))#获取指定行数的数据
print(sheet.col_values(0))#获取指定列数的数据

workbook=xlwt.Workbook()#打开一个excel文件对象
wsheet=workbook.add_sheet('sheet1')#添加一个sheet
wsheet.write(0,0,'test')#写入数据
workbook.save('test.xls')#保存excel，后缀必须是.xls，否则报错

ubook=xlrd.open_workbook('stu.xls')#打开一个excel文件对象
mbook=copy(ubook)#复制读到的文件对象
msheet=mbook.get_sheet(0)#获取sheet页，注意这里只能用get_sheet(0)方法，指定下标
msheet.write(0,0,'new_data')#写入数据
mbook.save('new.xls')#保存数据
os.remove('stu.xls')
os.rename('new.xls','stu.xls')