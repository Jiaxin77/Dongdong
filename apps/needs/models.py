from django.db import models

# Create your models here.

# 需求枚举
needType = (
    (-1, '未设置'),
    (1, '编辑中'),
    (2, '审核中'),
    (3, '已通过'),
    (4, '未通过')
)


class Needs(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="需求ID")
    enterId = models.ForeignKey('Enterprise', on_delete=models.CASCADE, verbose_name="企业ID")
    needsDes = models.CharField(max_length=500, null=True, verbose_name="需求描述")
    needsFarmerType = models.CharField(max_length=1000, null=True, verbose_name="所需工种")
    needsNum = models.CharField(max_length=500, null=True, verbose_name="所需工种人员")  # 几个工种用这个，一个工种用integer
    matchResult = models.CharField(max_length=1000, null=True, verbose_name="匹配结果")
    price = models.IntegerField(default=-1, verbose_name="价格")
    needsTime = models.CharField(max_length=500, null=True, verbose_name="时间")  # 时间
    needsLocation = models.CharField(max_length=1000, null=True, verbose_name="地点")  # 地点
    needsType = models.IntegerField(choices=needType, default=-1, verbose_name="需求状态")

