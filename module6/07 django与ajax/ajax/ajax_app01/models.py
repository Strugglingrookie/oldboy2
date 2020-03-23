from django.db import models


# Create your models here.


class UserDetail(models.Model):
    id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=32)
    phone = models.BigIntegerField(null=True)
    age = models.BigIntegerField(null=True)
    address = models.CharField(max_length=32, null=True)
    dep = models.CharField(max_length=32, null=True)


class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16)
    password = models.CharField(max_length=16)
    user_detail = models.OneToOneField(to=UserDetail, on_delete=models.CASCADE)
