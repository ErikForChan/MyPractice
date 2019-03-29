from django.shortcuts import render
import time
# Create your views here.
def index(request):
    ctime = time.time()
    return render(request,"index.html",{"ctime":ctime})