from django.db import models

# Create your models here.

class UserInfo(models.Model):
    user = models.Field(max_length=32)
