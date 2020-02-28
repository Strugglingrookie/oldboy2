import os

import jsonpath
import yagmail
import time
import traceback
from config.setting import log,TO,CC,EMAIL_INFO,DATA_PATH

def get_value(d,k):
    '这个函数是用来从返回结果里面获取key的'
    result = jsonpath.jsonpath(d,'$..%s'%k)
    if result:
        return result[0]
    return ''

def send_mail(pass_count,fail_count,file_name):
    log.debug('开始发送邮件')
    content = '''
各位好！
    本次接口测试结果如下：总共运行%s条用例，通过%s条，失败【%s】条。
    详细信息请查看附件。
    ''' % (pass_count+fail_count,pass_count,fail_count)
    subject = '%s-接口测试报告' % time.strftime('%Y-%m-%d %H:%M:%S')

    try:
        mail = yagmail.SMTP(**EMAIL_INFO)
        mail.send(to=TO,cc=CC,subject=subject,
                  contents=content,attachments=file_name)
    except Exception as e:
        log.error("发送邮件出错了，错误信息是:\n%s"%traceback.format_exc())
    else:
        log.info("发送邮件成功")

def get_data_form_text(file_name):
    '''获取参数化文件的内容'''
    data = [ ]
    file_name = os.path.join(DATA_PATH,file_name)
    with open(file_name,encoding='utf-8') as fr:
        for line in fr:
            line = line.strip()
            if line:
                data.append(line.split(','))
    return data

def get_data_form_excel(file_name):
    '''从excel里面获取数据'''
    data = [ ]
    'xxxxxx'
    return data
def get_data_form_db():
    pass

def get_data_form_redis():
    pass