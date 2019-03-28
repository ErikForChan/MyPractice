import urllib.parse
import json
dict = {'k1':'v1','k2':'v2'}
# data = json.dumps(dict)
data = urllib.parse.urlencode(dict)
print(data)

# 阅读dcrapy-redis源码
# 去重规则：本质利用redis集合元素不重复
# redis:
#  --连接
#  --基本操作
#  --事务 发布 订阅
# -- scrapy-redis:调度器和去重
                # 引擎：获取起始request对象，添加调度器
                # 调度器通知下载器可以开始下载，去调度器中获取request对象
                # 爬虫parse方法,yield
                                    # --Item 交给pipeline处理
                                    # --request 交给调度器管理

