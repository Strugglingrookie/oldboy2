# coding=utf-8
import tornado.web
import tornado.concurrent
import tornado.gen
from concurrent.futures import ThreadPoolExecutor
from apps.main.dao.main_curd import checkPasswd, addProject, listAllProjects, addModule, getProjectNameById, \
    listProjectModules, addApi, listProjectApis, getProjectDescById, listApisByMid, getApiData, saveApiData, \
    listAllResponseTypes, saveConsulEnv,listConsulEnvs
from plugin.base import *
import sys, time, json
from plugin import logger

reload(sys)
sys.setdefaultencoding('utf8')

_result = {}
TIMEOUT = 30
MAX_WORKERS = 50


class BaseHandler(tornado.web.RequestHandler):
    executor = ThreadPoolExecutor(max_workers=MAX_WORKERS)

    def prepare(self):
        if self.request.method == "POST":
            self.check_xsrf_cookie()

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")
        self.set_header('Access-Control-Allow-Methods', 'POST,GET,PUT,DELETE,OPTIONS')

    def get_current_user(self):
        return self.get_secure_cookie("user")

class IndexHandler(BaseHandler):
    def prepare(self):
        pass

    def get(self):
        a = self.xsrf_token
        self.write('ok')


class LoginHandler(BaseHandler):
    def post(self):
        account = self.get_argument('account')
        password = self.get_argument('passwd')
        realpasswd = rsa_decrypt(password)
        ispass = checkPasswd(account, md5(hmac_sha256_encrypt(realpasswd, account)))
        if ispass:
            ret = {"status": 0, "msg": "登录成功!"}
            self.set_secure_cookie("user", account)
        else:
            ret = {"status": 1, "msg": "用户名或密码错误！"}
        self.write(ret)

class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie('user')
        ret = {"status": 0, "msg": "退出登录成功!"}
        self.write(ret)

class GetAuthInfoHandler(BaseHandler):
    def get(self):
        user = self.current_user
        if not user:
            ret = {"status": 10001, "msg": "用户未登录！"}
        else:
            ret = {"status": 0, "data": user}
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        ret = json.dumps(ret)
        self.write(ret)

class NewProjectHandler(BaseHandler):
    @tornado.web.authenticated
    def post(self):
        name = self.get_argument('pjname')
        description = self.get_argument('pjdesc')
        owner = 'admin'
        result = addProject(name, description, owner)
        if result:
            ret = {"status": 0, "msg": "创建成功!", "data": result}
        else:
            ret = {"status": 1, "msg": "创建失败！"}
        self.write(ret)


class ListAllProjectsHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        result = listAllProjects()
        if result:
            ret = {"status": 0, "data": result}
        else:
            ret = {"status": 1, "msg": "记录为空！"}
        self.write(ret)


class NewModuleHandler(BaseHandler):
    @tornado.web.authenticated
    def post(self):
        name = self.get_argument('mname')
        pid = self.get_argument('pid')
        result = addModule(name, pid)
        if result:
            ret = {"status": 0, "msg": "创建成功!", "data": result}
        else:
            ret = {"status": 1, "msg": "创建失败！"}
        self.write(ret)


class GetProjectNameHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        pid = self.get_argument('pid')
        result = getProjectNameById(pid)
        if result:
            ret = {"status": 0, "data": result}
        else:
            ret = {"status": 1, "msg": "查询项目名称失败！"}
        self.write(ret)


class GetProjectDescHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        pid = self.get_argument('pid')
        result = getProjectDescById(pid)
        if result:
            ret = {"status": 0, "data": result}
        else:
            ret = {"status": 1, "msg": "查询项目描述失败！"}
        self.write(ret)


class ListProjectModulesHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        pid = self.get_argument('pid')
        result = listProjectModules(pid)
        if result:
            ret = {"status": 0, "data": result}
        else:
            ret = {"status": 1, "msg": "查询项目模块失败！"}
        self.write(ret)


class NewApiHandler(BaseHandler):
    @tornado.web.authenticated
    def post(self):
        mid = self.get_argument('mid')
        aname = self.get_argument('aname')
        result = addApi(int(mid), aname)
        if result:
            ret = {"status": 0, "data": result}
        else:
            ret = {"status": 1, "msg": "新增接口失败！"}
        self.write(ret)


class ListProjectApis(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        pid = self.get_argument('pid')
        try:
            result = listProjectApis(pid)
        except Exception, e:
            ret = {"status": 1, "msg": e.message}
        else:
            ret = {"status": 0, "data": result}
        self.write(ret)


class ListApisByMidHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        mid = self.get_argument('mid')
        try:
            result = listApisByMid(mid)
        except Exception, e:
            ret = {"status": 1, "msg": e.message}
        else:
            ret = {"status": 0, "data": result}
        self.write(ret)


class GetApiDataHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        aid = self.get_argument("aid")
        try:
            result = getApiData(aid)
        except Exception, e:
            ret = {"status": 1, "msg": e.message}
        else:
            ret = {"status": 0, "data": result}
        self.write(ret)


class SaveApiDataHandler(BaseHandler):
    @tornado.web.authenticated
    def post(self):
        aid = self.get_argument("aid")
        serviceName = self.get_argument("serviceName")
        uri = self.get_argument("uri")
        requestType = self.get_argument("requestType")
        method = self.get_argument("method")
        apiName = self.get_argument("apiName")
        apiDesc = self.get_argument("apiDesc", "")
        requestHeaders = self.get_argument("requestHeaders", '[]')
        requestBodys = self.get_argument("requestBodys", '[]')
        responseHeaders = self.get_argument("responseHeaders", '[]')
        responseBodys = self.get_argument("responseBodys", '[]')
        try:
            saveApiData(aid, serviceName, uri, requestType, method, apiName, apiDesc, requestHeaders, requestBodys,
                        responseHeaders, responseBodys)
        except Exception, e:
            ret = {"status": 1, "msg": e.message}
        else:
            ret = {"status": 0, "msg": "保存成功！"}
        self.write(ret)


class ListAllResponseTypesHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        result = listAllResponseTypes()
        if result:
            ret = {"status": 0, "data": result}
        else:
            ret = {"status": 1, "msg": "查询响应类型失败！"}
        self.write(ret)


class GetConsulEnvInfoHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        result = listConsulEnvs()
        if result:
            ret = {"status": 0, "data": result}
        else:
            ret = {"status": 1, "msg": "查询consul环境失败！"}
        self.write(ret)


class SaveConsulEnvInfoHandler(BaseHandler):
    @tornado.web.authenticated
    def post(self):
        consulEnvs = self.get_argument("consulEnvs", [])
        try:
            saveConsulEnv(consulEnvs)
        except Exception, e:
            ret = {"status": 1, "msg": e.message}
        else:
            ret = {"status": 0, "msg": "保存成功！"}
        self.write(ret)


if __name__ == '__main__':
    api_id = 2
