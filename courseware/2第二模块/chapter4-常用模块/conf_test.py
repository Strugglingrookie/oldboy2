# _*_coding:utf-8_*_
# created by Alex Li on 10/17/17

import configparser

conf = configparser.ConfigParser()


conf.read("conf_test.ini")


#conf.remove_option("group1","k2")
conf.remove_section("group1")

# conf.add_section("group3")
# conf['group3']['name'] = "Alex Li"
# conf['group3']['age'] = "22"
#
conf.write(open('conf_test2.ini', "w"))

# print(dir(conf))
#
# print(conf.options("group1"))
# print(conf['group1']["k2"])