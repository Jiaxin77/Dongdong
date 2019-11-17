from django.db import models

# Create your models here.

# 企业审核状态
enterState = (
    (-1, '未设置'),
    (1, '审核中'),
    (2, '已通过'),
    (3, '未通过')
)

# 工种枚举
farmerType = (
    (-1, '未设置'),
    (1, '木工'),
    (2, '泥瓦工')
)


# 企业库
class Enterprise(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="企业ID")
    name = models.CharField(max_length=100, verbose_name="企业用户名")
    password = models.CharField(max_length=50, verbose_name="企业密码")
    enterName = models.CharField(max_length=500, null=True, verbose_name="企业名称")
    authState = models.IntegerField(choices=enterState, verbose_name="审核状态")


# 民工库
class Farmers(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="农民工ID")
    name = models.CharField(max_length=100, verbose_name="农民工用户名")
    password = models.CharField(max_length=100, verbose_name="农民工密码")
    IDCard = models.CharField(max_length=100, null=True, verbose_name="农民工身份证号")
    type = models.IntegerField(choices=farmerType, default=-1, verbose_name="工种")  # 民工种类
    completedNeed = models.CharField(max_length=500, null=True, verbose_name="已完成需求")  # 已完成的需求
    ingNeed = models.CharField(max_length=500, null=True, verbose_name="进行中需求")  # 正在做的需求


# 管理员库
class Administrator(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="管理员ID")
    name = models.CharField(max_length=100, verbose_name="管理员用户名")
    password = models.CharField(max_length=100, verbose_name="管理员密码")


