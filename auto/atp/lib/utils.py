# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/2/28 16:01
# @File   : lib.py


import xlrd, os, time, traceback, yagmail
from xlutils import copy
from config.settings import log, CASE_PATH, REPORT_PATH, EMAIL_INFO, TO, CS, QQ_EMAIl


def write_excel(file_path, res_list):
    # [ ['请求参数','实际结果','状态','备注(失败原因)']]
    try:
        log.info('现在开始写报告了：文件名是 %s  内容：%s' % (file_path, res_list))
        book = xlrd.open_workbook(file_path)
        new_book = copy.copy(book)
        sheet = new_book.get_sheet(0)
        for row, res in enumerate(res_list, 1):
            # 实际结果 状态 原因 对应 8 9 10 这3列
            for col, val in enumerate(res[1:], 8):
                sheet.write(row, col, val)
            # 请求参数对应第3列
            sheet.write(row, 3, str(res[0]))
        # 写 xlsx格式会报错，替换下
        file_name = os.path.basename(file_path).replace('xlsx', 'xls')
        new_name = time.strftime('%Y%m%d%H%M%S') + '_' + file_name
        report_file = os.path.join(REPORT_PATH, new_name)
        new_book.save(report_file)
        log.info('报告生成完成，文件名是%s' % report_file)
        return report_file
    except:
        log.error("生成 %s 的测试报告失败，报错如下：%s" % (file_path, traceback.format_exc()))


def send_mail(all_count, pass_count, file_name):
    log.debug('开始发送邮件')
    content = '''
各位好！
    本次接口测试结果如下：总共运行%s条用例，通过%s条，失败【%s】条。
    详细信息请查看附件。
    ''' % (all_count, pass_count, all_count - pass_count)
    subject = '%s-接口测试报告' % time.strftime('%Y-%m-%d %H:%M:%S')
    try:
        mail = yagmail.SMTP(**EMAIL_INFO)
        mail.send(to=TO, cc=CS, subject=subject,
                  contents=content, attachments=file_name)
    except Exception as e:
        log.error("发送邮件出错了，错误信息是:\n%s" % traceback.format_exc())
    else:
        log.info("发送邮件成功")


if __name__ == '__main__':
    res = [['请求参数', '实际结果', '状态', '备注(失败原因)']]
    file_path1 = os.path.join(CASE_PATH, "用例模板.xlsx")
    file_path2 = os.path.join(CASE_PATH, "test_copy.xlsx")
    # write_escel(file_path, res)
    print(file_path2, file_path1)
    # send_mail(100,90,file_path1)
    send_mail(100, 90, [file_path1, file_path2])
