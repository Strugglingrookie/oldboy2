import nnlog
from config.setting import HOST, LOG_PATH,log
from lib.util import get_value


class ParseResponse:
    fuhao = ['!=', '>=', '<=', '=', '>', '<']

    def __init__(self, check_str, response):
        self.check_str = check_str
        self.response = response
        self.status = '通过'
        self.reason = '都通过啦'
        self.check_response()

    def check_response(self):
        if self.check_str.strip():
            for s in self.check_str.split(','):  #
                for f in self.fuhao:
                    if f in s:
                        key, yuqijieguo = s.split(f)
                        shijijieguo = get_value(self.response, key)
                        f = '==' if f == '=' else f
                        code = "%s %s %s" % (shijijieguo, f, yuqijieguo)
                        tag = eval(code)
                        if tag != True:
                            self.reason = 'key是%s，运算的代码是%s' % (key, code)
                            log.debug(self.reason)
                            self.status = '失败'
                            return False
                        break
        return True

