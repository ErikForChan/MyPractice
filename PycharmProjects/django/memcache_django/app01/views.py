from django.shortcuts import render,HttpResponse
import time
# Create your views here.
def index(request):
    ctime = time.time()
    return render(request,"index.html",{"ctime":ctime})


def new(request):
    ctime = time.time()
    return HttpResponse(ctime)