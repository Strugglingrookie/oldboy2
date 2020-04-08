#!/usr/bin/env Python
#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


import os,base64,uuid
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from plugin.base import getCfgValue

INSTALLED_APPS=[
    "apps.main"
]

DATABASE = {
    'DBDRIVER':'mysqldb',
    'NAME':getCfgValue('mysql','dbname'),
    'USER':getCfgValue('mysql','user'),
    'PASSWORD':getCfgValue('mysql','password'),
    'HOST':getCfgValue('mysql','host'),
    'PORT':getCfgValue('mysql','port')
}

Base = declarative_base()
engine = create_engine('mysql+{DBDRIVER}://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}?charset=utf8'.format(**DATABASE))

settings=dict(
    template_path = os.path.join(os.path.dirname(__file__),"templates"),
    static_path = os.path.join(os.path.dirname(__file__),"statics"),
    debug = False,
    cookie_secret = base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes),
    xsrf_cookies = False,
    login_url = '/mockServer/login',
)



