import random
import string


def random_password():
    '''产生随机密码的函数'''
    a  = random.sample(string.digits,2)
    b  = random.sample(string.ascii_letters,2)
    c  = random.sample(string.ascii_uppercase,2)
    d  = random.sample(string.punctuation,2)
    result = a + b + c + d
    random.shuffle(result)
    return ''.join(result)