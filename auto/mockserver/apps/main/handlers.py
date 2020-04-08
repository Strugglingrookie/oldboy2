# coding=utf-8
import tornado.web
import tornado.concurrent
import tornado.gen
from concurrent.futures import ThreadPoolExecutor
from dao.main_curd import *
from plugin import logger
import sys, time, json
from tornado.httpclient import HTTPRequest
try:
    from tornado.curl_httpclient import CurlAsyncHTTPClient as AsyncHTTPClient
except ImportError:
    from tornado.simple_httpclient import SimpleAsyncHTTPClient as AsyncHTTPClient

reload(sys)
sys.setdefaultencoding('utf8')

_result = {}
TIMEOUT = 30
MAX_WORKERS = 50


class BaseHandler(tornado.web.RequestHandler):
    executor = ThreadPoolExecutor(max_workers=MAX_WORKERS)

    def get_current_user(self):
        return self.get_secure_cookie("user")

class IndexHandler(BaseHandler):
    def on_response(self, respnose):
        if respnose.code!=200:
            self.set_status(respnose.code, respnose.error.message)
        else:
            for k in respnose.headers:
                self.set_header(k,respnose.headers.get(k))
            self.write(respnose.body)
        self.finish()

    @tornado.web.asynchronous
    def post(self):
        try:
            req = self.request
            protocol = req.protocol
            host = req.host
            method = req.method
            uri = req.uri
            urigroups = uri.split('/')
            if urigroups[1]=="errorpage":
                path =self.get_argument("path")
                sc = urigroups[2]
                if sc == "404":
                    reason = "<h1>Not Found</h1><p>The requested URL %s was not found on this server.</p>"%path
                else:
                    reason = "<h1>Internal Server Error</h1>"
                self.set_status(int(sc))
                self.write(reason)
                self.finish()
                return
        except Exception,e:
            self.set_status(500, "Internal Server Error!")
            logger.error(e.message, 'line %d (/apps/api/handlers.py)' % (sys._getframe().f_lineno - 2))
            self.finish()
            return
        try:
            headers_o = req.headers
            body_o = req.body
            remote_ip = req.remote_ip
            path = req.path
            request_headers = req.headers
            request_query = req.arguments
            request_body = req.body
            serviceName = request_headers.get("downstream-service-id", None)
        except Exception,e:
            self.set_status(500, "Internal Server Error!")
            logger.error(e.message, 'line %d (/apps/api/handlers.py)' % (sys._getframe().f_lineno - 2))
            self.finish()
            return
        if not serviceName:
            self.set_status(500, "The request header resolution failed!")
            logger.error("请求头解析失败!", 'line %d (/apps/api/handlers.py)' % (sys._getframe().f_lineno - 2))
            self.finish()
            return
        if not request_body:
            request_body = {}
        else:
            try:
                request_body = json.loads(request_body)
            except:
                request_body = {}
        t = {}
        for i in request_query:
            t.setdefault(i, request_query[i][-1])
        request_query = t
        responseID, headers = checkMockMatch(serviceName, uri, request_headers, request_query,
                                             request_body)
        if responseID:
            response = getResponseById(responseID)
            self.set_status(response.get("statusCode"))
            self.set_header("Content-Type", response.get("type"))
            if headers:
                for hd in headers:
                    self.add_header(hd.get("name"), hd.get("value"))
            self.write(response.get("response"))
            self.finish()
        else:
            try:
                serverIP, serverPort = getServerHost(serviceName)
            except Exception, e:
                self.set_status(500, "Internal Server Error!")
                logger.error(e.message, 'line %d (/apps/api/handlers.py)' % (sys._getframe().f_lineno - 2))
                self.finish()
            else:
                serverhost = "%s://%s:%s" % (protocol, serverIP, serverPort)
                AsyncHTTPClient().fetch(
                    HTTPRequest(
                        url=serverhost + uri,
                        method=method,
                        headers=headers_o,
                        body=body_o,
                        validate_cert=False
                    ),
                    self.on_response)

    @tornado.web.asynchronous
    def get(self):
        try:
            req = self.request
            protocol = req.protocol
            host = req.host
            method = req.method
            uri = req.uri
            urigroups = uri.split('/')
            if urigroups[1]=="errorpage":
                path =self.get_argument("path")
                sc = urigroups[2]
                if sc == "404":
                    reason = "<h1>Not Found</h1><p>The requested URL %s was not found on this server.</p>"%path
                else:
                    reason = "<h1>Internal Server Error</h1>"
                self.set_status(int(sc))
                self.write(reason)
                self.finish()
                return
        except Exception,e:
            self.set_status(500, "Internal Server Error!")
            logger.error(e.message, 'line %d (/apps/api/handlers.py)' % (sys._getframe().f_lineno - 2))
            self.finish()
            return
        try:
            headers_o = req.headers
            body_o = req.body
            remote_ip = req.remote_ip
            path = req.path
            request_headers = req.headers
            request_query = req.arguments
            request_body = req.body
            serviceName = request_headers.get("downstream-service-id", None)
        except Exception,e:
            self.set_status(500, "Internal Server Error!")
            logger.error(e.message, 'line %d (/apps/api/handlers.py)' % (sys._getframe().f_lineno - 2))
            self.finish()
            return
        if not serviceName:
            self.set_status(500, "The request header resolution failed!")
            logger.error("请求头解析失败!", 'line %d (/apps/api/handlers.py)' % (sys._getframe().f_lineno - 2))
            self.finish()
            return
        if not request_body:
            request_body = {}
        else:
            try:
                request_body = json.loads(request_body)
            except:
                request_body = {}
        t = {}
        for i in request_query:
            t.setdefault(i, request_query[i][-1])
        request_query = t
        responseID, headers = checkMockMatch(serviceName, uri, request_headers, request_query,
                                             request_body)
        if responseID:
            response = getResponseById(responseID)
            self.set_status(response.get("statusCode"))
            self.set_header("Content-Type", response.get("type"))
            if headers:
                for hd in headers:
                    self.add_header(hd.get("name"), hd.get("value"))
            self.write(response.get("response"))
            self.finish()
        else:
            try:
                serverIP, serverPort = getServerHost(serviceName)
            except Exception, e:
                self.set_status(500, "Internal Server Error!")
                logger.error(e.message, 'line %d (/apps/api/handlers.py)' % (sys._getframe().f_lineno - 2))
                self.finish()
            else:
                serverhost = "%s://%s:%s" % (protocol, serverIP, serverPort)
                AsyncHTTPClient().fetch(
                    HTTPRequest(
                        url=serverhost + uri,
                        method=method,
                        headers=headers_o,
                        body=body_o,
                        validate_cert=False
                    ),
                    self.on_response)

if __name__ == '__main__':
    skip = False
    ret = ""

