#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import random,string


class CommonMethod():

    @classmethod
    def randomString(cls,prefix,appd_len,appd_is_alpha=False):
        if appd_is_alpha:
            appd = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(appd_len))
        else:
            appd = ''.join(random.choice(string.digits) for _ in range(appd_len))
        ret = prefix+appd
        return ret


if __name__ == '__main__':
    x = CommonMethod.__dict__
    for i in x:
        print i