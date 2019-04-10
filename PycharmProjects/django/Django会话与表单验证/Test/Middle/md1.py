#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/4/10 16:51
# software: PyCharm
from django.utils.deprecation import MiddlewareMixin

# 一个中间件
class Row1(MiddlewareMixin):  # 继承MiddlewareMixin
    def process_request(self,request):
        print("0")
    def process_view(self,request,view_func,view_func_agrs,view_func_kwargs):
        pass
    def process_response(self,request,response):
        print("1")

    def process_exception(self,request,exception):
        pass
        # 处理异常


class Row2(MiddlewareMixin):  # 继承MiddlewareMixin
    def process_request(self,request):
        print("4")
    def process_response(self,request,response):
        print("3")


# views: 2
