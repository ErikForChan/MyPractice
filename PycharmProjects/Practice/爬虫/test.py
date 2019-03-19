import urllib.parse
import json
dict = {'k1':'v1','k2':'v2'}
# data = json.dumps(dict)
data = urllib.parse.urlencode(dict)
print(data)


