from django.db import models

# Create your models here.

# 企业审核状态
enterState = (
    (-1, '未审核'),
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
    password = models.CharField(max_length=5000, verbose_name="企业密码")
    authState = models.IntegerField(choices=enterState,default=-1,verbose_name="审核状态")
    authAdvice = models.CharField(max_length=2000,null=True,verbose_name="审核意见")
    enterName = models.CharField(max_length=500, null=True, verbose_name="企业名称")
    enterDes = models.CharField(max_length=1000, null=True,verbose_name="企业简介")

    icon = models.ImageField(upload_to='head',null=True)


    # 这部分必须的 default=1？否则default=0？  【必须和非必须怎么表示？】
    # 头像
    # 营业执照
    # 建筑资质
    # 安全生产许可证
    # 社保缴费证明（6个月）
    # 拟用工项目中标通知书或其他文件
    # 项目商业保险
    # 无纳税异常声明
    # 土地使用证
    # 规划许可证
    # 施工许可证
    # 开工报告





# 包工头库
class Farmers(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="包工头ID")
    name = models.CharField(max_length=100, verbose_name="包工头用户名")
    password = models.CharField(max_length=5000, verbose_name="农民工密码")
    IDCard = models.CharField(max_length=100, null=True, verbose_name="包工头身份证号")
    type = models.IntegerField(choices=farmerType, default=-1, verbose_name="工种")  # 民工种类
    memberNumber = models.IntegerField(default=1, verbose_name="小组人数")
    ingNeed = models.ForeignKey("needs.Needs", on_delete=models.SET_NULL, verbose_name="进行中需求",null=True)  # 正在做的需求

    #completedNeed = models.CharField(max_length=500, null=True, verbose_name="已完成需求")

    #completedNeed = models.ManyToManyField("needs.Needs") # 已完成的需求(多对多) --按组的话不需要，但是存在组内有人未完成吗
    #ingNeed = models.CharField(max_length=500, null=True, verbose_name="进行中需求")  # 正在做的需求 --按组的话不需要，但是存在组内有人未完成吗


# 民工个人
class FarmersMember(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="农民工ID")
    name = models.CharField(max_length=100,verbose_name="农民工姓名")
    IDCard = models.CharField(max_length=100,verbose_name="农民工身份证号",unique=True)
    age = models.IntegerField(null=True,verbose_name="年龄")
    group = models.ForeignKey("user.Farmers", on_delete=models.CASCADE,null=True)  # 所在组





# 管理员库
class Administrator(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="管理员ID")
    name = models.CharField(max_length=100, verbose_name="管理员用户名")
    password = models.CharField(max_length=100, verbose_name="管理员密码")


