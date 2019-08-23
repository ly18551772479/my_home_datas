from django.db import models


# Create your models here.

class Info(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    gender = models.CharField(max_length=20, verbose_name='性别')
