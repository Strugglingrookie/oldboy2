#!/usr/bin/env Python
#coding = utf-8
import tornado.ioloop
import tornado.httpserver
import tornado.options
import tornado.web
from urls import urls
from setting import settings
from tornado.options import define,options

application = tornado.web.Application(
    handlers=urls,
    **settings
)

define("port",default=8000,help="run on the given prot",type = int)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(application,xheaders=True)
    http_server.listen(options.port)
    print "Development server is running at http://127.0.0.1:%s"%options.port
    print "Quit the server with Control-C"
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()