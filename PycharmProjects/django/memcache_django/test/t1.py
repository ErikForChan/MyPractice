#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Erik Chan
# datetime:2019/3/30 16:51
# software: PyCharm
import memcache
mc = memcache.Client([('192.168.0.196:11211'),],debug=True) #mc[0]为第一台机器
# mc.set('k','value',10) #超时时间为10
# mc.set('kt',1000)
rc = mc.get('kt')
print(rc)