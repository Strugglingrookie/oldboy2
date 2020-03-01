import flask
from flask_cors import CORS

server = flask.Flask(__name__)
CORS(server, supports_credentials=True)


@server.route("/api/project", methods=["get", "put", "post", "delete"])
def project():
    print(flask.request.args)
    if flask.request.method == "GET":
        data = {"code": 0,
                "count": 4,
                "data": [{"id": 1,
                          "name": "nhy测试项目1",
                          "desc": "项目描述",
                          "user": "一个很帅的人",
                          "create_time": "2019-07-25 23:55:01",
                          "host": "http://api.nnzhp.cn"},
                         {"id": 2,
                          "name": "nhy测试项目2",
                          "desc": "项目描述",
                          "user": "一个很帅的人",
                          "create_time": "2019-07-25 23:55:01",
                          "host": "http://api.nnzhp.cn"},
                         {"id": 3,
                          "name": "nhy测试项目3",
                          "desc": "项目描述",
                          "user": "一个很帅的人",
                          "create_time": "2019-07-25 23:55:01",
                          "host": "http://api.nnzhp.cn"},
                         {"id": 4,
                          "name": "nhy测试项目4",
                          "desc": "项目描述",
                          "user": "一个很帅的人",
                          "create_time": "2018-07-25 23:55:01",
                          "host": "http://api.nnzhp.cn"},
                         ],
                "msg": "成功"}
    else:
        data = {
            "code": 0,
            "msg": "成功"
        }
    return flask.jsonify(data)


@server.route("/api/parameter", methods=["get", "put", "post", "delete"])
def parameter():
    print(flask.request.args)
    if flask.request.method == "GET":
        data = {
            "code": 0,
            "count": 100,
            "data": [
                {"id": 1, "name": "sessionid", "desc": "登录sessionid", "value": "sdfsddf23", },
                {"id": 2, "name": "token", "desc": "登录token", "value": "sdfsddf23", },
                {"id": 3, "name": "shop_id", "desc": "商户id", "value": "1", },
            ],
            "msg": "成功"
        }
    else:
        data = {
            "code": 0,
            "msg": "成功"
        }
    return flask.jsonify(data)


@server.route("/api/interface", methods=["get", "put", "post", "delete"])
def interface():
    print(flask.request.values)
    if flask.request.method == "GET":
        data = {"code": 0,
                "count": 100,
                "data": [{"id": 1,
                          "name": "登录",
                          "create_time": "2019-07-21 18:01:02",
                          "update_time": "2019-07-21 18:01:02",
                          "project_name": "牛牛测试项目1",
                          "project_id": 1,
                          "uri": "/api/user/login",
                          "params": '{"token": "123456", "userid": "1"}',
                          "headers": '{"cookie": "cookie1"}',
                          "user": "牛牛"},
                         {"id": 2,
                          "name": "注册",
                          "create_time": "2019-07-21 18:01:02",
                          "update_time": "2019-07-21 18:01:02",
                          "project_name": "牛牛测试项目2",
                          "project_id": 2,
                          "uri": "/api/user/login",
                          "params": '{"token": "223456", "userid": "2"}',
                          "headers": '{"cookie": "cookie2"}',
                          "user": "牛牛"},
                         {"id": 3,
                          "name": "充值",
                          "create_time": "2019-07-21 18:01:02",
                          "update_time": "2019-07-21 18:01:02",
                          "project_name": "牛牛测试项目3",
                          "project_id": 3,
                          "uri": "/api/user/login",
                          "params": '{"token": "323456", "userid": "3"}',
                          "headers": '{"cookie": "cookie2"}',
                          "user": "牛牛"},
                         ],
                "msg": "成功"}
    else:
        data = {
            "code": 0,
            "msg": "成功"
        }
    return flask.jsonify(data)


@server.route("/api/case_collection", methods=["get", "put", "post", "delete"])
def case_collection():
    print(flask.request.values)
    if flask.request.method == "GET":
        data = {"code": 0,
                "count": 100,
                "data": [{"id": 1,
                          "name": "回归case",
                          "create_time": "2019-07-21 18:01:02",
                          "update_time": "2019-07-21 18:01:02",
                          "project_name": "牛牛测试项目1",
                          "project_id": 1,
                          "desc": "回归流程使用",
                          "case_count": 5,
                          "report_id": 1,
                          "report_name": "2019-08-06测试报告",
                          "user": "牛牛",
                          "run_user": "牛牛"},
                         {"id": 2,
                          "name": "冒烟case",
                          "create_time": "2019-07-21 18:01:02",
                          "update_time": "2019-07-21 18:01:02",
                          "project_name": "牛牛测试项目2",
                          "project_id": 2,
                          "desc": "冒烟测试使用",
                          "case_count": 4,
                          "report_id": 2,
                          "report_name": "2019-08-06测试报告",
                          "user": "牛牛",
                          "run_user": "牛牛"},
                         {"id": 3,
                          "name": "支付流程",
                          "create_time": "2019-07-21 18:01:02",
                          "update_time": "2019-07-21 18:01:02",
                          "project_name": "牛牛测试项目3",
                          "project_id": 3,
                          "desc": "支付流程",
                          "case_count": 3,
                          "report_id": 3,
                          "report_name": "2019-08-06测试报告",
                          "user": "牛牛",
                          "run_user": "牛牛"},
                         ],
                "msg": "成功"}
    else:
        data = {
            "code": 0,
            "msg": "成功"
        }
    return flask.jsonify(data)


@server.route("/api/case_run", methods=["post"])
def collection_run():
    print(flask.request.headers)
    print("json", flask.request.json)

    data = {
        "code": 0,
        "msg": "成功"
    }
    return flask.jsonify(data)


@server.route("/api/case", methods=["get", "put", "post", "delete"])
def case():
    print(flask.request.values)
    if flask.request.method == "GET":
        data = {"code": 0,
                "count": 100,
                "data": [{"id": 1,
                          "title": "登陆用例",
                          "create_time": "2019-07-21 18:01:02",
                          "update_time": "2019-07-21 18:01:02",
                          "project_name": "牛牛测试项目1",
                          "project_id": 1,
                          "status": "通过",
                          "pass_count": 5,
                          "fail_count": 1,
                          "report_id": 1,
                          "json": "",
                          "interface_name": "登录",
                          "interface_id": 1,
                          "user": "牛牛",
                          "cache_field": "sign,userId",
                          "method": "post",
                          "params": '{"username": "niuhanyang", "password": "123456"}',
                          "headers": "",
                          "is_json": False,
                          "check": "userid,userId=1"},
                         {"id": 2,
                          "title": "登陆用例2",
                          "create_time": "2019-07-21 18:01:02",
                          "update_time": "2019-07-21 18:01:02",
                          "project_name": "牛牛测试项目2",
                          "project_id": 2,
                          "status": "失败",
                          "pass_count": 5,
                          "fail_count": 1,
                          "report_id": 1,
                          "json": "",
                          "interface_name": "登录",
                          "interface_id": 1,
                          "user": "牛牛",
                          "cache_field": "sign,userId",
                          "method": "get",
                          "params": '{"username": "niuhanyang2", "password": "1234561"}',
                          "headers": '{"Content-Type": "application/json", "cookies": "token=token123"}',
                          "is_json": False,
                          "check": "userid,userId=1"},
                         {"id": 3,
                          "title": "登陆用例3",
                          "create_time": "2019-07-21 18:01:02",
                          "update_time": "2019-07-21 18:01:02",
                          "project_name": "牛牛测试项目3",
                          "project_id": 3,
                          "status": "失败",
                          "pass_count": 5,
                          "fail_count": 1,
                          "report_id": 1,
                          "json": '{"username": "niuhanyang", "password": "123456"}',
                          "interface_name": "登录",
                          "interface_id": 1,
                          "user": "牛牛",
                          "cache_field": "sign,userId",
                          "method": "post",
                          "params": "",
                          "headers": '{"Content-Type": "application/json", "cookies": "token=token123"}',
                          "is_json": True,
                          "check": "userid,userId=1"},
                         ],
                "msg": "成功"}
    else:
        data = {
            "code": 0,
            "msg": "成功"
        }
    return flask.jsonify(data)


@server.route("/api/join_case", methods=["post", "get"])
def join_case():
    print(flask.request.values)
    if flask.request.method == "GET":

        data = {
            "code": 0,
            "msg": "成功",
            "data": {
                "all_case": [{"id": 1, "name": "登陆用例", "create_time": "2019-07-21 18:01:02",
                              "update_time": "2019-07-21 18:01:02",
                              "project_name": "牛牛测试项目1", "project_id": 1, "desc": "回归流程使用", "case_count": 5,
                              "report_id": 1,
                              "report_name": "2019-08-06测试报告", "user": "牛牛"},
                             {"id": 2, "name": "登陆用例1", "create_time": "2019-07-21 18:01:02",
                              "update_time": "2019-07-21 18:01:02",
                              "project_name": "牛牛测试项目2", "project_id": 2, "desc": "冒烟测试使用", "case_count": 4,
                              "report_id": 2,
                              "report_name": "2019-08-06测试报告", "user": "牛牛"},
                             {"id": 3, "name": "登陆用例2", "create_time": "2019-07-21 18:01:02",
                              "update_time": "2019-07-21 18:01:02",
                              "project_name": "牛牛测试项目3", "project_id": 3, "desc": "支付流程", "case_count": 3,
                              "report_id": 3,
                              "report_name": "2019-08-06测试报告", "user": "牛牛"}],
                "join_case": [1]

            }
        }
    else:
        data = {
            "code": 0,
            "msg": "成功"
        }
    return flask.jsonify(data)


@server.route("/api/case_response", methods=["get"])
def case_response():
    print(flask.request.values)
    if flask.request.method == "GET":

        data = {
            "code": 0,
            "msg": "成功",
            "data": {
                "all_case": [{"id": 1, "name": "登陆用例", "create_time": "2019-07-21 18:01:02",
                              "update_time": "2019-07-21 18:01:02",
                              "project_name": "牛牛测试项目1",  "response": "回归流程使用", "case_count": 5,
                              "report_id": 1,
                              "report_name": "2019-08-06测试报告", "user": "牛牛"},
                             {"id": 2, "name": "登陆用例1", "create_time": "2019-07-21 18:01:02",
                              "update_time": "2019-07-21 18:01:02",
                              "project_name": "牛牛测试项目2", "project_id": 2, "desc": "冒烟测试使用", "case_count": 4,
                              "report_id": 2,
                              "report_name": "2019-08-06测试报告", "user": "牛牛"},
                             {"id": 3, "name": "登陆用例2", "create_time": "2019-07-21 18:01:02",
                              "update_time": "2019-07-21 18:01:02",
                              "project_name": "牛牛测试项目3", "project_id": 3, "desc": "支付流程", "case_count": 3,
                              "report_id": 3,
                              "report_name": "2019-08-06测试报告", "user": "牛牛"}],
                "join_case": [1]

            }
        }
    else:
        data = {
            "code": 0,
            "msg": "成功"
        }
    return flask.jsonify(data)

server.run("127.0.0.1", port=8000, debug=True)
