from django.shortcuts import render

# Create your views here.
import requests
import time
import re
from django.shortcuts import render,HttpResponse,redirect
import json
import webbrowser
from selenium import webdriver

def login(request):
    if request.method == 'GET':
        cur_time = int(time.time() * 1000)
        base_uuid_url = "https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb&redirect_uri=https%3A%2F%2Fwx.qq.com%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&fun=new&lang=en_US&_={0}"
        url = base_uuid_url.format(cur_time)
        r1 = requests.get(url)
        print(r1.text)
        result = re.findall('= "(.*)";',r1.text)
        uuid = result[0]
        # 存储session:cur_time
        request.session['UUID_TIME'] = cur_time
        request.session['UUID'] = uuid
        return render(request,'login.html',{'uuid':uuid})


def check_login(req):
    response = {'code':408,'data':None}
    cur_time = int(time.time() * 1000)
    base_login_url = "https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid={0}&tip=1&r=-1963954647&_={1}"
    login_url = base_login_url.format(req.session['UUID'],cur_time)
    r1 = requests.get(login_url)
    print(r1.text)
    if 'window.code=408' in r1.text:
        response['code'] = 408

    elif 'window.code=201' in r1.text:
        response['code'] = 201
        response['data'] = re.findall("window.userAvatar = '(.*)';",r1.text)[0]

    elif 'window.code=200' in r1.text:
        req.session['LOGIN_COOKIE'] = r1.cookies.get_dict() # &fun=new&version=v2
        base_redirect_url = re.findall('redirect_uri="(.*)";', r1.text)[0]
        redirect_url = base_redirect_url + "&fun=new&version=v2"
        print("base_redirect_url:  "+base_redirect_url)
        # driver = webdriver.Chrome()
        # driver.get(base_redirect_url)
        # webbrowser.open(base_redirect_url)
        r2 = requests.get(redirect_url)
        tick_dict = get_ticket(r2.text)
        req.session['TICKED_DICT'] = tick_dict
        req.session['TICKED_COKKIE'] = r2.cookies.get_dict()

        post_data = {
            "BaseRequest": {
                "DeviceID": "e384757757885382",
                'Sid': tick_dict['wxsid'],
                'Uin': tick_dict['wxuin'],
                'Skey': tick_dict['skey'],
            }
        }

        init_url = "https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxinit?r=-740036701&pass_ticket={0}".format(tick_dict['pass_ticket'])
        r3 = requests.post(
            url=init_url,
            json=post_data
        )
        r3.encoding = 'UTF-8'
        init_dict = json.loads(r3.text)
        req.session['INIT_DICT'] = init_dict
        response['code'] = 200
        # response['data'] = re.findall('window.redirect_uri="(.*)";', r1.text)[0]
    return  HttpResponse(json.dumps(response))


def index(req):
    img_url = "https://wx.qq.com" + req.session['INIT_DICT']['User']['HeadImgUrl']
    res = requests.get(img_url, headers={'Referer': 'https://wx.qq.com/?&lang=zh_CN'})
    return render(req, 'index.html', {'img': res.content})

from bs4 import  BeautifulSoup
def get_ticket(html):
    rect = {}
    soup = BeautifulSoup(html,"html.parser")
    for tag in soup.find(name = 'error').find_all():
        rect[tag.name] = tag.text
    return rect