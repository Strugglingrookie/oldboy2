#coding=utf-8

from handlers import IndexHandler
from tornado.web import url

urls = [
    url(r'.*', IndexHandler,name="index"),

]