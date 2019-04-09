from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from django.utils.safestring import mark_safe
from utils import pagination
# set_cookie("","",max_age = 10) max_age为cookie保持时间
#date = datetime.datetime.utcnow() +datetime.timedelta(seconds=5)
# set_cookie("","",expired = date) expired为指定的时间
# response.COOKIES.get("")
# path 受影响的路径
# domain 生效的域名
# secure http传输
# httponly 是否只支持http传输
# set_signed_cookie(salt="123") # 带签名的cookie
# get_signed_cookie("",salt="")
# python操作md5

user_info = {
    'dachengzi': {'pwd': "123123"},
    'kanbazi': {'pwd': "kkkkkkk"},
}
def login(request):
    if request.method == "GET":
        return render(request,'.html')
    if request.method == "POST":
        u = request.POST.get("name")
        p = request.POST.get('pwd')
        dic = user_info.get(u)
        if not dict:
            return render(request,'')
        if dict['pwd'] == p:
            res = redirect('/index/')
            res.set_cookie('name',u)
            res.set_cookie('pwd',p)
        else:
            return render(request,'.html')

def cookie(request):
    #
    # request.COOKIES
    # request.COOKIES['username111']
    request.COOKIES.get('username111')

    response = render(request, 'index.html')
    response = redirect('/index/')
    # 设置cookie，关闭浏览器失效
    response.set_cookie('key', "value")
    # 设置cookie, N秒只有失效
    response.set_cookie('username111', "value", max_age=10)
    # 设置cookie, 截止时间失效
    import datetime
    current_date = datetime.datetime.utcnow()
    current_date = current_date + datetime.timedelta(seconds=5)
    response.set_cookie('username111', "value", expires=current_date)
    response.set_cookie('username111', "value", max_age=10)

    # request.COOKIES.get('...')
    # response.set_cookie(...)
    obj = HttpResponse('s')

    obj.set_signed_cookie('username', "kangbazi", salt="asdfasdf")
    request.get_signed_cookie('username', salt="asdfasdf")

    return response


# CBV和FBV用户认证装饰器
def auth(func):
    def inner(request,*args,**kwargs):
        v = request.COOKIES.get("email")
        if not v:
            return redirect('')
        return func(request,*args,**kwargs)
    return inner


class Order():

    def get(self,request):
        v = request.COOKIES.get("email")
        if not v:
            return redirect('')
        return render(request,"",{'':''})
    def post(self,request):
        v = request.COOKIES.get("email")
        if not v:
            return redirect('')
        return render(request, "", {'': ''})


LIST = []
for i in range(209):
    LIST.append(i)


def user_list(request):
    current_page = request.GET.get('p', 1)
    current_page = int(current_page)

    per_page_count = request.COOKIES.get('per_page_count',10)
    page_obj = pagination.Page(current_page, len(LIST), int(per_page_count))

    data = LIST[page_obj.start:page_obj.end]

    page_str = page_obj.page_str("/user_list/")

    # cur_page = request.GET.get("p",1)  # 默认第一页
    # cur_page = int(cur_page)
    # LIST = []
    # for i in range(209):
    #     LIST.append(i)
    # start = (cur_page-1) * 10
    # end = cur_page * 10
    # # if cur_page > 5:
    # #     start = cur_page - 5
    # #     end = cur_page + 5
    # # else:
    # #     start = 1
    # #     end = 10
    # data = LIST[start:end]
    #
    # page_count,left = divmod(len(LIST),10)
    # if left > 0:
    #     page_count += 1
    # print(cur_page)
    # print(page_count)
    # page_list = []
    # if page_count < 11:
    #     start_index = 1
    #     end_index = page_count
    # else:
    #     if cur_page > 5 and cur_page + 5 <= page_count:
    #         start_index = cur_page - 5
    #         end_index = cur_page + 6
    #     elif cur_page + 5 > page_count:
    #         start_index = page_count - 10
    #         end_index = page_count + 1
    #     else:
    #         start_index = 1
    #         end_index = 12
    # if cur_page > 1:
    #     prev = '<a calss="page active" href="/user_list/?p=%s">上一页</a>'%(cur_page-1)
    # else:
    #     prev = '<a calss="page" href="javascript::void(0)">上一页</a>'
    # page_list.append(prev)
    # for i in range(start_index,end_index):
    #     if i==cur_page:
    #         temp = '<a calss="page active" href="/user_list/?p=%s">%s</a>' %(i,i)
    #     else:
    #         temp = '<a calss="page" href="/user_list/?p=%s">%s</a>' % (i, i)
    #     page_list.append(temp)
    # if cur_page == page_count:
    #     next = '<a calss="page" href="javascript::void(0)">下一页</a>'
    # else:
    #     next = '<a calss="page active" href="/user_list/?p=%s">下一页</a>' % (cur_page + 1)
    #
    # page_list.append(next)
    # page_str = "".join(page_list)
    # page_str = mark_safe(page_str)

    return render(request,"分页.html",{'li': data,"page_str":page_str})


def tp1(request):

    return render(request,"tp1.html")


def index(request):

    # print(request.environ) #封装了所有用户的请求信息
    for k,v in request.environ.items():
        print(k,v)
    return HttpResponse('OK')
    # PATH
    # C:\SoftWare\mysql - 8.0
    # .13 - winx64\bin;
    # D:\DIDE\Toolchains\yagarto - gcc4
    # .9\bin;
    # C:\ProgramData\Oracle\Java\javapath;
    # C:\Program
    # Files(x86)\Intel\Intel(R)
    # Management
    # Engine
    # Components\iCLS\;C:\Program
    # Files\Intel\Intel(R)
    # Management
    # Engine
    # Components\iCLS\;C:\Windows\system32;
    # C:\Windows;
    # C:\Windows\System32\Wbem;
    # C:\Windows\System32\WindowsPowerShell\v1
    # .0\;C:\Windows\System32\OpenSSH\;C:\Program
    # Files(x86)\Intel\Intel(R)
    # Management
    # Engine
    # Components\DAL;
    # C:\Program
    # Files\Intel\Intel(R)
    # Management
    # Engine
    # Components\DAL;
    # C:\Program
    # Files(x86)\Intel\Intel(R)
    # Management
    # Engine
    # Components\IPT;
    # C:\Program
    # Files\Intel\Intel(R)
    # Management
    # Engine
    # Components\IPT;
    # C:\Program
    # Files(x86)\NVIDIA
    # Corporation\PhysX\Common;
    # C:\Program
    # Files\Intel\WiFi\bin\;C:\Program
    # Files\Common
    # Files\Intel\WirelessCommon\;C:\Program
    # Files\Microsoft
    # VS
    # Code\bin;
    # C:\Program
    # Files\Git\cmd;
    # C:\Program
    # Files\Apache
    # Software
    # Foundation\Tomcat
    # 9.0\bin;
    # C:\Program
    # Files\Apache
    # Software
    # Foundation\Tomcat
    # 9.0\lib;
    # C:\SoftWare\apache - maven - 3.6
    # .0\bin;
    # C:\Windows\system32;
    # C:\Windows;
    # C:\Windows\System32\Wbem;
    # C:\Program
    # Files\MySQL\MySQL
    # Utilities
    # 1.6\;D:\Program
    # Files\TortoiseGit\bin;
    # D:\Users\10434\Anaconda3;
    # D:\Users\10434\Anaconda3\Scripts;
    # D:\Users\10434\Anaconda3\Library\bin;
    # D:\Users\10434\Anaconda3\Library\mingw - w64\bin;
    # C:\Users\10434\AppData\Local\Microsoft\WindowsApps;
    # C:\Program
    # Files(x86)\Google\Chrome\Application;
    # C:\SoftWare\IntelliJ
    # IDEA
    # Community
    # Edition
    # 2018.3\bin;
    # PATHEXT.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC
    # PROCESSOR_ARCHITECTURE
    # AMD64
    # PROCESSOR_IDENTIFIER
    # Intel64
    # Family
    # 6
    # Model
    # 142
    # Stepping
    # 10, GenuineIntel
    # PROCESSOR_LEVEL
    # 6
    # PROCESSOR_REVISION
    # 8e0
    # a
    # PROGRAMDATA
    # C:\ProgramData
    # PROGRAMFILES
    # C:\Program
    # Files
    # PROGRAMFILES(X86)
    # C:\Program
    # Files(x86)
    # PROGRAMW6432
    # C:\Program
    # Files
    # PSMODULEPATH
    # C:\Program
    # Files\WindowsPowerShell\Modules;
    # C:\Windows\system32\WindowsPowerShell\v1
    # .0\Modules
    # PUBLIC
    # C:\Users\Public
    # PYCHARM_HOSTED
    # 1
    # PYCHARM_MATPLOTLIB_PORT
    # 53442
    # PYTHONIOENCODING
    # UTF - 8
    # PYTHONPATH
    # D:\WORK\MyGit\PycharmProjects\django\分页与Cookie\Test;
    # D:\Program
    # Files\JetBrains\PyCharm
    # 2018.3
    # .3\helpers\pycharm_matplotlib_backend
    # PYTHONUNBUFFERED
    # 1
    # SESSIONNAME
    # Console
    # SYSTEMDRIVE
    # C:
    # SYSTEMROOT
    # C:\Windows
    # TEMP
    # C:\Users\10434\AppData\Local\Temp
    # TMP
    # C:\Users\10434\AppData\Local\Temp
    # USERDOMAIN
    # LAPTOP - JI9DN5OA
    # USERDOMAIN_ROAMINGPROFILE
    # LAPTOP - JI9DN5OA
    # USERNAME
    # 10434
    # USERPROFILE
    # C:\Users\10434
    # WINDIR
    # C:\Windows
    # RUN_MAIN
    # true
    # SERVER_NAME
    # activate.navicat.com
    # GATEWAY_INTERFACE
    # CGI / 1.1
    # SERVER_PORT
    # 8000
    # REMOTE_HOST
    # CONTENT_LENGTH
    # SCRIPT_NAME
    # SERVER_PROTOCOL
    # HTTP / 1.1
    # SERVER_SOFTWARE
    # WSGIServer / 0.2
    # REQUEST_METHOD
    # GET
    # PATH_INFO / index /
    # QUERY_STRING
    # REMOTE_ADDR
    # 127.0
    # .0
    # .1
    # CONTENT_TYPE
    # text / plain
    # HTTP_HOST
    # 127.0
    # .0
    # .1: 8000
    # HTTP_CONNECTION
    # keep - alive
    # HTTP_UPGRADE_INSECURE_REQUESTS
    # 1
    # HTTP_USER_AGENT
    # Mozilla / 5.0(Windows
    # NT
    # 10.0;
    # Win64;
    # x64) AppleWebKit / 537.36(KHTML, like
    # Gecko) Chrome / 70.0
    # .3538
    # .102
    # Safari / 537.36
    # HTTP_ACCEPT
    # text / html, application / xhtml + xml, application / xml;
    # q = 0.9, image / webp, image / apng, * / *;q = 0.8
    # HTTP_ACCEPT_ENCODING
    # gzip, deflate, br
    # HTTP_ACCEPT_LANGUAGE
    # zh - CN, zh;
    # q = 0.9
    # HTTP_COOKIE
    # csrftoken = G4VzDZASSJIWMGUvKvGgsyP6S4jJTPWo2cOIxaAtZPuaq9HKWvysCNFAqyfZh2Y1

