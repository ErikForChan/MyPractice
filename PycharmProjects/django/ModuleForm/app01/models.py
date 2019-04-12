from django.db import models

# Create your models here.


class UserType():
    caption = models.CharField(max_length=32)


class UserInfo():
    username = models.CharField(max_length=32)
    email = models.EmailField()
    user_type = models.ForeignKey(to='UserType',to_field='id',on_delete=models.CASCADE,)
