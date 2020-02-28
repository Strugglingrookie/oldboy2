# -*- coding: utf-8 -*-
# @Author : XiaoGang
# @Time   : 2020/2/28 13:59
# @File   : parse_response.py


import traceback, jsonpath
from config.settings import log


class ParseResponse():
    symbol = ['!=', '>=', '<=', '=', '>', '<']

    def __init__(self, expected_res, actual_res):
        self.expected_res = expected_res.strip()
        self.actual_res = actual_res
        self.status = '通过'
        self.reason = ''
        self.do_check()

    def do_check(self):
        # 如果预期结果为空 直接返回True通过
        if not self.expected_res:
            return True
        log.debug("开始校验...预期结果 %s，实际结果 %s"
                  % (self.expected_res, self.actual_res))
        expected_lis = self.expected_res.split(",")
        for exp in expected_lis:
            check_flag = False
            for sym in self.symbol:
                if sym in exp:
                    # 预期结果里有对应的运损符，将flag置为True
                    check_flag = True
                    log.debug("开始校验%s" % exp)
                    exp_k, exp_v = exp.split(sym)
                    act_lis = jsonpath.jsonpath(self.actual_res, '$..%s' % exp_k)
                    # 因为预期结果处理得到的数据是字符串
                    # 这里也需要处理为字符串，不然eval会报错
                    act_v = str(act_lis[0]) if act_lis else ''
                    sym = "==" if sym == "=" else sym
                    log.debug("校验表达式%s %s %s" % (act_v, sym, exp_v))
                    res = eval("act_v %s exp_v" % sym)
                    if res != True:
                        self.reason = '预期结果 %s，实际结果 %s' \
                                      % (self.expected_res, self.actual_res)
                        log.error(self.reason)
                        self.status = "失败"
                        return False
            # 预期结果里内有有对应的运损符 用例失败
            if not check_flag:
                self.reason = '预期结果 %s，实际结果 %s' \
                              % (self.expected_res, self.actual_res)
                log.error(self.reason)
                self.status = "失败"
                return False
        log.debug("校验成功...预期结果 %s，实际结果 %s"
                  % (self.expected_res, self.actual_res))


if __name__ == '__main__':
    expect_data = "user=xg,age<28,height=180,money>1000"
    actual_dic = {"user": "xg", "age": 20, 'height': 180, 'money': 101}
    p = ParseResponse(expect_data, actual_dic)
    print(p.status)
