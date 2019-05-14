from django.shortcuts import render

# Create your views here.
from app01 import models


def article(request,*args,**kwargs):
    result = models.Article.objects.all()
    article_type_list = models.ArticleType.objects.all()

    dict = {}
    for k, v in kwargs.items():
        if v == '0':
            pass
        else:
            dict[k] = v
    category_list = models.Category.objects.filter(**dict)
    for i in result:
        print(i.title)
    return render(request,"article.html",{"result":result,"article_type_list":article_type_list,"category_list":category_list})
