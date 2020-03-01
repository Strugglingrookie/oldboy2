# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/2/29 15:44
# @File   : tools.py


import yagmail, time, traceback, jsonpath, copy, random, string
from config.settings import log, EMAIL_INFO, CS, TO


def get_value(d, k):
    '这个函数是用来从返回结果里面获取key的'
    result = jsonpath.jsonpath(d, '$..%s' % k)
    if result:
        return result[0]
    return ''


def send_mail(pass_count, fail_count, file_name):
    log.debug('开始发送邮件')
    content = '''
各位好！
    本次接口测试结果如下：总共运行%s条用例，通过%s条，失败【%s】条。
    详细信息请查看附件。
    ''' % (pass_count + fail_count, pass_count, fail_count)
    subject = '%s-接口测试报告' % time.strftime('%Y-%m-%d %H:%M:%S')
    try:
        mail = yagmail.SMTP(**EMAIL_INFO)
        mail.send(to=TO, cc=CS, subject=subject,
                  contents=content, attachments=file_name)
    except Exception as e:
        log.error("发送邮件出错了，错误信息是:\n%s" % traceback.format_exc())
    else:
        log.info("发送邮件成功")


def get_params(data_path):
    data_list = []
    with open(data_path, encoding="utf8") as f:
        for line in f:
            data_line = line.strip().split(',')
            if data_line:
                data_list.append(data_line)
    return data_list


def json_assert(expected_json, actual_json, tmp_json=None):
    '''
    判断预期json是否是实际json的子集,实际json可能存在嵌套
    :param expected_json: 预期的json
    :param actual_json: 实际json
    :return: True or False
    '''
    tmp_json = copy.deepcopy(expected_json) if tmp_json == None else tmp_json
    if type(actual_json) == dict:
        for key, value in actual_json.items():
            if type(value) == dict or type(value) == list:
                json_assert(tmp_json, value, tmp_json)
            elif tmp_json.get(key) == value:
                tmp_json.pop(key)
    elif type(actual_json) == list:
        for element in actual_json:
            if type(element) == dict or type(element) == list:
                json_assert(tmp_json, element, tmp_json)
    if tmp_json == {}:
        return True
    else:
        return False


def str_to_dic(s):
    '''字符串转换成字典'''
    dic = {}
    log.debug("请求参数转换字典：%s" % s)
    if s.strip():
        for var in s.split("&"):
            k, v = var.split("=")
            dic[k] = v
    log.debug('%s 转换字典为 %s' % (s, dic))
    return dic


def create_token():
    letters = string.digits + string.ascii_letters
    token = random.sample(letters, 6)
    token = ''.join(token)
    return token


if __name__ == '__main__':
    dic0 = {"a": "b", "x": "y"}
    dic1 = {"a": "b", "x": "z"}
    dic2 = {"a": {"a": "c"}, 1: [2, 3, 6, 7, {"c": {"a": "b"}}], "x": {"x": "y"}, "c": "d"}
    print(json_assert(dic0, dic2))
    print(json_assert(dic1, dic2))
    print(create_token())
