from django.shortcuts import render

# Create your views here.
from app01 import models

from django import forms
from django.forms import fields as Ffields
from django.forms import widgets as Fwidgets

class UserInfoModelForm(forms.Form):
    class Meta:
        model = models.UserInfo
        # fields = '__all__ '
        fields = ['username','email']
        exclude = []
        labels = {
            "username":"用户名",
            "pwd":"密码",
        }
        help_text = {
            "username": "提示信息",
        }
        widgets = {
            "username": Fwidgets.Textarea(attrs={}),
        }

        error_messages = {
            "email":{
                "required":""
            }
        }

        # field_classes = None  # 自定义字段类 （也可以自定义字段）
        # localized_fields = ('birth_date',)  # 本地化，如：根据不同时区显示数据


def index(request):
    if request.method == 'GET':
        obj = UserInfoModelForm()
        return render(request,"index.html",{"obj",obj})
    if request.method == 'POST':
        obj = UserInfoModelForm(request.POST)
        print(obj.is_valid())
        if obj.is_valid():
            obj.save() # 添加保存数据，支持多对多
            # 与obj.save()功能相同
            # instance = obj.save(False)
            # instance.save()
            # obj.save_m2m()
        print(obj.errors)
        print(obj.changed_data)
        return render(request, "index.html", {"obj", obj})


def user_list(request):
    users = models.UserInfo.objects.all().select_related('user_type')
    return render(request,"user_list.html",{"users":users})

def user_edit(request,nid):
    if request.method == 'GET':
        user_obj = models.UserInfo.objects.filter(id = nid).first()
        mf = UserInfoModelForm(instance = user_obj)
        return render(request,"user_edit.html",{"mf",mf})

    if request.method == 'POST':
        user_obj = models.UserInfo.objects.filter(id=nid).first()
        mf = UserInfoModelForm(request.POST, instance=user_obj)
        if mf.is_valid():
            mf.save()
        else:
            print(mf.errors.as_json())
        return render(request,"user_edit.html",{"mf",mf})


def ajax(request):

    return render(request,"ajax.gtml")


# 上传文件
def upload(request):

    return render(request,"upload.gtml")
