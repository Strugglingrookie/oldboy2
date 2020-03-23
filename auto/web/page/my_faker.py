import faker
import random


# 用于参数化
f = faker.Faker(locale="zh-CN")

def get_bankcard():
    head = '622202'
    tail = random.sample('01234567890123456789',13)
    card_id = head+''.join(tail)
    return card_id

PARAMS_MAP = {
    "card": f.ssn,
    "phone": f.phone_number,
    "email": f.email,
    "name": f.name,
    "password": f.password,
    "bankcard": get_bankcard,
    "money": f.random_int,
    "address": f.address
}

