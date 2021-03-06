from django.db import models

# Create your models here.

#分类
class Category(models.Model):
    caption = models.CharField(max_length=32)

class ArticleType(models.Model):
    caption = models.CharField(max_length=32)

# 文章
class Article(models.Model):
    title = models.CharField(max_length=32)
    content = models.CharField(max_length=32)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    article_type = models.ForeignKey(ArticleType,on_delete=models.CASCADE)

