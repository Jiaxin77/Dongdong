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


def enter_auth_file(instance, filename, license_name):
    return "enterAuth/{enterprise}/{authType}/{file}".format(instance.id, enterprise=instance.enterName,
                                                             authType=license_name, file=filename)
# 企业库
class Enterprise(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="企业ID")
    name = models.CharField(max_length=100, verbose_name="企业用户名")
    password = models.CharField(max_length=5000, verbose_name="企业密码")
    authState = models.CharField(max_length=200, default= "未提交",verbose_name="审核状态")
    #authState = models.IntegerField(choices=enterState,default=-1,verbose_name="审核状态")
    authAdvice = models.CharField(max_length=2000,null=True,verbose_name="审核意见")
    enterName = models.CharField(max_length=500, null=True, verbose_name="企业名称")
    enterDes = models.CharField(max_length=1000, null=True, verbose_name="企业简介")
    scope = models.CharField(max_length=1000, null=True, verbose_name="经营范围")
    nowProject = models.CharField(max_length=1000,null=True,verbose_name="当前工程")
    #icon = models.ImageField(upload_to='head',null=True)

    #资质信息


    # 头像
    # 营业执照
    businessLicense = models.FileField(upload_to=enter_auth_file(license_name='businessLicense'), null=True, verbose_name="营业执照")
    constructionQUAL = models.FileField(upload_to=enter_auth_file(license_name='constructionQUAL'), null=True, verbose_name="建筑资质")
    securityLicense = models.FileField(upload_to=enter_auth_file(license_name='securityLicense'), null=True,verbose_name="安全许可证")
    socialSecurityCert = models.FileField(upload_to=enter_auth_file(license_name='socialSecurityCert'), null=True, verbose_name="社保缴费证明")
    noticeOfBid = models.FileField(upload_to=enter_auth_file(license_name='noticeOfBid'), null=True, verbose_name="拟用工项目中标通知书或其他文件")
    businessItemInsurance = models.FileField(upload_to=enter_auth_file(license_name='businessItemInsurance'), null=True, verbose_name="商业项目保险")
    noTaxExpStatement = models.FileField(upload_to=enter_auth_file(license_name='noTaxExpStatement'), null=True, verbose_name="无纳税异常声明")
    planningPermit = models.FileField(upload_to=enter_auth_file(license_name='planningPermit'), null=True, verbose_name='规划许可证')
    constructionPermit = models.FileField(upload_to=enter_auth_file(license_name='constructionPermit'), null=True, verbose_name="施工许可证")
    landUseCert = models.FileField(upload_to=enter_auth_file(license_name='landUseCert'), null=True, verbose_name="土地使用证")
    startReport = models.FileField(upload_to=enter_auth_file(license_name='startReport'), null=True, verbose_name="开工报告")




#包工头
class Foreman(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="包工头ID")
    name = models.CharField(max_length=100, verbose_name="包工头用户名")
    password = models.CharField(max_length=5000, verbose_name="包工头密码")
    openid = models.CharField(max_length=5000, default="null", verbose_name="小程序openid")
    IDCard = models.CharField(max_length=100, null=True, verbose_name="包工头身份证号")
    phonenumber = models.CharField(max_length=100,null=True, verbose_name="手机号")
    Bank = models.CharField(max_length=100,null=True,verbose_name="银行")
    BankNumber = models.CharField(max_length=1000,null=True,verbose_name="银行卡号")

# 工种+班级号
class Farmers(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="组ID")
    classNumber = models.IntegerField(default=-1, verbose_name="组号")
    #type = models.IntegerField(choices=farmerType, default=-1, verbose_name="工种")  # 民工种类
    type = models.CharField(max_length=2000, default="未设置", verbose_name="工种")
    memberNumber = models.IntegerField(default=0, verbose_name="小组人数")
    leader = models.ForeignKey("Foreman",on_delete=models.SET_NULL, verbose_name="所属包工头",null=True)
    ingNeed = models.ForeignKey("needs.Needs", on_delete=models.SET_NULL, verbose_name="进行中需求",null=True)  # 正在做的需求
    authState = models.CharField(max_length=2000,default="审核中",verbose_name="审核状态") #审核未通过、审核中、审核已通过
    #completedNeed = models.CharField(max_length=500, null=True, verbose_name="已完成需求")

    #completedNeed = models.ManyToManyField("needs.Needs") # 已完成的需求(多对多) --按组的话不需要，但是存在组内有人未完成吗
    #ingNeed = models.CharField(max_length=500, null=True, verbose_name="进行中需求")  # 正在做的需求 --按组的话不需要，但是存在组内有人未完成吗

# 民工个人
class FarmersMember(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="农民工ID")
    name = models.CharField(max_length=100,verbose_name="农民工姓名")
    IDCard = models.CharField(max_length=100,verbose_name="农民工身份证号")
    phoneNumber = models.CharField(max_length=100,verbose_name="手机号",null=True)
    #age = models.IntegerField(null=True,verbose_name="年龄")
    group = models.ForeignKey("user.Farmers", null=True,on_delete=models.SET_NULL)  # 所在组
    authInfo = models.ImageField(upload_to='farmerAuth',null=True)#资质照片




# 管理员库
class Administrator(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="管理员ID")
    name = models.CharField(max_length=100, verbose_name="管理员用户名")
    password = models.CharField(max_length=100, verbose_name="管理员密码")


