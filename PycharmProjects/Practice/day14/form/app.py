
#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/1/18 12:45
# software: PyCharm
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        print("get")
        self.write("is Get")
        u = self.get_argument("user")
        p = self.get_argument("password")
        print(u)
        if u == 'CJM':
            print("Good")

    def post(self, *args, **kwargs):
        print("post")
        self.write("is Post")
        u = self.get_argument("user")
        p = self.get_argument("password")
        print(u)
        print(p)


application = tornado.web.Application([(r"/index",MainHandler)])
if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()