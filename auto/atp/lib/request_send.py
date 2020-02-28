# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/2/27 22:47
# @File   : request_send.py


import requests, traceback, jsonpath, threading, re
from config.settings import HOST, RELEVANCE_DATA, log
from urllib.parse import urljoin


class MyRequest():
    def __init__(self, url, method, data=None, headers=None, is_json="否", rele=None):
        self.tid = threading.get_ident()
        self.url = urljoin(HOST, url)
        self.method = method.lower()
        self.data = self.set_rele(data)  # 关联参数
        self.headers = self.str_to_dic(headers)
        self.is_json = is_json
        self.rele = self.str_to_dic(rele)
        self.req()

    def set_rele(self, data):
        '''
        关联参数，以线程id为key，
        取相应线程的关联参数替换到请求参数
        :param data: 请求参数
        :return: 关联好的请求参数
        '''
        reles = re.findall(r'\{(.*?)\}', data)
        if reles:
            log.debug("开始设置关联参数 %s" % data)
            thread_rels = RELEVANCE_DATA.get(self.tid)
            for rele_k in reles:
                log.debug("获取关联参数 %s" % rele_k)
                rel_data = thread_rels.get(rele_k) if thread_rels else ''
                if rel_data:
                    rele_v = '{' + rele_k + '}'
                    data = data.replace(rele_v, rel_data)
                    log.debug("关联参数设置成功 %s=%s" % (rele_k, rel_data))
                else:
                    log.error("没有找到关联参数 %s" % rele_k)
        return self.str_to_dic(data)

    def str_to_dic(self, s):
        '''字符串转换成字典'''
        dic = {}
        log.debug("请求参数转换字典：%s" % s)
        if s.strip():
            for var in s.split("&"):
                k, v = var.split("=")
                dic[k] = v
        log.debug('%s 转换字典为 %s' % (s, dic))
        return dic

    def req(self):
        log.info("开始发起请求:\nurl:%s\nmethod:%s\nheaders:%s\nreq_data:%s\n待关联的参数:%s"
                 % (self.url, self.method, self.headers, self.data, self.rele))
        try:
            if self.is_json == '是':
                res = requests.request(self.method, self.url, params=self.data, json=self.data,
                                       headers=self.headers).json()
            else:
                res = requests.request(self.method, self.url, params=self.data, data=self.data,
                                       headers=self.headers).json()

            # 如果存在关联参数，从响应数据里取关联参数
            if self.rele:
                # 以线程id为key，同一个线程的关联参数放一起
                RELEVANCE_DATA.setdefault(self.tid, {})
                for k, v in self.rele.items():
                    log.debug("开始获取关联参数 %s" % v)
                    val = jsonpath.jsonpath(res, "$..%s" % v)
                    if val:
                        RELEVANCE_DATA[self.tid][k] = val[0]
                        log.debug("获取关联参数成功 %s=%s,已加载至关联参数池" % (v, val[0]))
                    else:
                        RELEVANCE_DATA[self.tid][k] = ''
                        log.error("获取关联参数失败 %s" % v)
                        log.error("响应数据 %s 里没有关联参数 %s" % (res, v))
        except Exception as e:
            log.error('请求 %s的时候出错了，请求参数是：%s，错误信息是 %s' % (self.url, self.data, traceback.format_exc()))
            self.res = {"msg": "请求接口出错了", "error_msg": traceback.format_exc()}
            self.text = ' {"msg":"请求接口出错了","error_msg":%s} ' % traceback.format_exc()
        else:
            self.res = res
            self.text = str(res)
            log.info('请求 %s 成功，响应参数 %s' % (self.url, self.res))


if __name__ == '__main__':
    from lib.read_case import ParamDeal

    p = ParamDeal()
    cases = p.read_calc(r'D:\oldboy\auto\atp\cases\用例模板.xlsx')
    for case in cases:
        req_obj = MyRequest(*case[:-1])  # 发请求
        req_obj.req()
