import re
import requests
from pprint import pprint
import urllib3
urllib3.disable_warnings()

url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8971'
response = requests.get(url, verify=False)
stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)
pprint(dict(stations), indent=4)
# stations = re.findall('([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)
# stations = dict(stations)
# pprint(stations, indent=4)
# names = re.findall('[\u4e00-\u9fa5]+', response.text)
# telecodes = re.findall('[([A-Z]+', response.text)


# def get_name(code):
#     return names[telecodes.index(code)]
#
#
# def get_telecode(name):
#     return telecodes[names.index(name)]
# # print(names)
# # print(telecodes)



