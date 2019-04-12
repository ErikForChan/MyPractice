from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponse
# Create your views here.
import sg
from app01 import models
def sig(request):
    obj = models.UserInfo

from django import forms
from django.forms import widgets #自定义样式
from django.forms import fields
class FM(forms.Form):
    user = forms.CharField(
        widget=widgets.Textarea(attrs={"class":"t1"}),
        initial= "初始值",
    )
    pwd = forms.CharField(
        widget=widgets.PasswordInput
    )
    email = forms.EmailField(error_messages={'required':"邮箱不能为空",},max_length= 32)

def fm(request):
    if request.method == "GET":
        obj = FM()
        return render(request,"fm.html",{"obj":obj})
    if request.method == "POST":
        obj = FM(request.POST)
        r1 = obj.is_valid()
        obj.errors #所有错误信息  obj.errors.get["user"]  obj.errors.user.0 第一个错误信息
        obj.cleaned_data #所有正确信息
        return redirect("/fm/")
