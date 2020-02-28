import os
import random,string
import time
import traceback
import jsonpath
import xlrd
import yagmail
from xlutils import copy
from config.setting import REPORT_PATH,log,EMAIL_INFO,TO,CC



def get_value(d,k):
    '这个函数是用来从返回结果里面获取key的'
    result = jsonpath.jsonpath(d,'$..%s'%k)
    if result:
        return result[0]
    return ''



def write_excel(file_name,result_list):
    #[ ['请求参数','实际记过','原因','状态']  ]
    log.debug('现在开始写报告了：文件名是 %s  内容：%s'%(file_name,result_list))
    book = xlrd.open_workbook(file_name)
    new_book = copy.copy(book)
    sheet = new_book.get_sheet(0)
    for row,result in enumerate(result_list,1):
        for col,value in enumerate(result[1:],7):#写7 8 9 这3列
            sheet.write(row,col,value)
        sheet.write(row,3,result[0])#写请求参数的第4列

    file_name = os.path.split(file_name)[-1].replace('xlsx','xls')
    new_file_name = time.strftime('%Y%m%d%H%M%S')+'_'+file_name
    abs_path = os.path.join(REPORT_PATH,new_file_name)
    new_book.save(abs_path)
    log.debug('报告生成完成，文件名是%s'%abs_path)
    return abs_path


def send_mail(all_count,pass_count,file_name):
    log.debug('开始发送邮件')
    content = '''
各位好！
    本次接口测试结果如下：总共运行%s条用例，通过%s条，失败【%s】条。
    详细信息请查看附件。
    ''' % (all_count,pass_count,all_count-pass_count)
    subject = '%s-接口测试报告' % time.strftime('%Y-%m-%d %H:%M:%S')

    EMAIL_INFO = {
        'user': 'uitestp4p@163.com',
        'host': 'smtp.163.com',
        'password': 'houyafan123'
    }
    try:
        mail = yagmail.SMTP(**EMAIL_INFO)
        mail.send(to=TO,cc=CC,subject=subject,
                  contents=content,attachments=file_name)
    except Exception as e:
        log.error("发送邮件出错了，错误信息是:\n%s"%traceback.format_exc())
    else:
        log.info("发送邮件成功")








