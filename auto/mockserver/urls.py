#!/usr/bin/env Python
# coding=utf-8
from importlib import import_module
from tornado.web import URLSpec
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def include(module):
    res = import_module(module)
    urls = getattr(res, 'urls', res)
    return urls

def url_wrapper(urls):
    wrapper_list = []
    for url in urls:
        if isinstance(url,URLSpec):
            path, handles, name = url.regex.pattern,url.handler_class,url.name
        else:
            path, handles = url[0],url[1]
            name = None if len(url)<3 else url[2]

        if isinstance(handles, (tuple, list)):
            for handle in handles:
                if isinstance(handle, URLSpec):
                    pattern, handle_class, url_name = handle.regex.pattern, handle.handler_class, handle.name
                else:
                    pattern, handle_class = handle[0],handle[1]
                    url_name = None if len(handle)<3 else handle[2]
                if name==None:
                    retname = url_name
                else:
                    retname = name+'_'+url_name if url_name else None
                wrapper_list.append(URLSpec('{0}{1}'.format(path, pattern), handle_class,name=retname))
        else:
            wrapper_list.append(URLSpec(path, handles,name=name))
    return wrapper_list

urls = url_wrapper([

    (r'/mockserverApi/',include('apps.api.urls'),"api"),
    (r'/', include('apps.main.urls'),"main"),

])