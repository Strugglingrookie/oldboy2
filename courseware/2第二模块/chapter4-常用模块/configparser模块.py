# _*_coding:utf-8_*_
# created by Alex Li on 10/17/17

import configparser

conf = configparser.ConfigParser()
#
# print(conf.sections())

conf.read("conf.ini")

# print(conf.sections())
# print(conf.default_section)

#print(list(conf["bitbucket.org"].keys()))
# print(conf["bitbucket.org"]['User'])

# for k,v in conf["bitbucket.org"].items():
#     print(k,v)

# if 'user' in conf["bitbucket.org"]:
#     print('in ')