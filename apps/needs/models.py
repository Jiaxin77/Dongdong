from django.db import models


# Create your models here.

# 需求枚举
needType = (
    (-1, '未设置'),
    (1, '编辑中'),
    (2, '匹配中'),
    (3, '匹配完成待支付'),  # 匹配完成未支付（未到开工时间或是在工作中）
    (4, '匹配失败'),
    (5, '已完成')
)


class Needs(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="需求ID")
    enterId = models.ForeignKey('user.Enterprise', on_delete=models.CASCADE, verbose_name="企业ID",null=True)
    needsDes = models.CharField(max_length=500, null=True, verbose_name="需求描述")
    #needsFarmerType = models.IntegerField(choices=user.models.farmerType,null=True,verbose_name="所需工种")
    needsFarmerType = models.CharField(max_length=2000,null=True,verbose_name="所需工种")
    needsNum = models.IntegerField(default=0,verbose_name="所需工种人员数")
    nowNum = models.IntegerField(default=0, verbose_name="目前人数")
    #matchResult = models.CharField(max_length=1000, null=True, verbose_name="匹配结果")
    matchResult = models.ManyToManyField("user.Farmers",verbose_name="匹配结果人员",null=True)  # 组
    price = models.IntegerField(default=-1, verbose_name="工资")
    needsTime = models.DateField(auto_now_add=True, verbose_name="需求创建时间")
    #needsTime = models.CharField(max_length=500, null=True, verbose_name="开工时间")  # 时间
    needsBeginTime = models.DateField(null=True, verbose_name="开工时间") #开工时间 --时间的匹配？
    needsLocation = models.CharField(max_length=1000, null=True, verbose_name="工地")  # 地点
    #needsDayNum = models.IntegerField(default=0,verbose_name="工期")
    needsEndTime = models.DateField(null=True, verbose_name="截止时间")
    remarks = models.CharField(max_length=2000, null=True,verbose_name="备注")
    needsType = models.CharField(max_length=200,default="未设置", verbose_name="需求状态")
    contractTime = models.DateField(null=True,verbose_name="合同生成时间")
    contractType = models.IntegerField(default=0,null=True,verbose_name="合同是否确认") #

