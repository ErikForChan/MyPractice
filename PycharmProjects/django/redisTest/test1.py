import redis

#操作模式
r = redis.Redis(host="192.168.100.9",port=6379)
r.set('foo','Bar')

#连接池
# pool = redis.ConnectionPool(host='10.211.55.4', port=6379)
# r = redis.Redis(connection_pool=pool)
# r.set('foo','Bar')

set('', "", ex=None, px=None, nx=False, xx=False)
# ex，过期时间（秒）
# px，过期时间（毫秒）
# nx，如果设置为True，则只有name不存在时，当前set操作才执行
# xx，如果设置为True，则只有name存在时，岗前set操作才执行
# print(r.get('foo'))

# 批量设置值
r.mset({'k1': 'v1', 'k2': 'v2'})
r.append('key','value')

r.hset('name','key','value')
r.hmset('name','dict') # Hash操作,字典
r.lpush('name',1,2,3) # List操作,1,2,3一次放在列表中
r.lpush('name',12) # 在name对应的list中添加元素，只有name已经存在时，值添加到列表的最左边
r.sadd('name','set') # 集合
r.zadd('name','n1', 1, 'n2', 2) # 有序集合
