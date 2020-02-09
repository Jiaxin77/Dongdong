from django.db import models

# Create your models here.
from datetime import timezone

from django.db import models

# Create your models here.

class Order(models.Model):
    order_status=(
        (1, "交易中"),
        (2, "已完成"),
        (3, "已取消")
    )
    p_id = models.AutoField(default=0,primary_key=True, verbose_name="订单序号")
    id = models.CharField(max_length=1000,default="000",verbose_name="订单流水号")
    #   entid = models.ForeignKey("user.Enterprise",on_delete=models.CASCADE,verbose_name="此订单所属企业") --从所属需求中读取
    farmers = models.ManyToManyField("user.Farmers",verbose_name="组")  # 组
    money = models.FloatField(default=0,verbose_name="总交易金额") #交易金额
    moneyToFarmers = models.FloatField(default=0, verbose_name="给农工金额")
    moneyToApp = models.FloatField(default=0, verbose_name="给软件金额")
    needId = models.ForeignKey("needs.Needs",on_delete=models.CASCADE,verbose_name="此订单所属需求",null=True)
    beginTime = models.DateTimeField(auto_now_add=True) #订单创建时间
    lastModified = models.DateTimeField(auto_now=True) #最后一次更改时间
    status = models.CharField(max_length=200, default="交易中")

