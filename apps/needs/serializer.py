from rest_framework import  serializers

from needs.models import Needs
from user.serializer import FarmersSerializer,EnterpriseSerializer


class NeedsSerializer(serializers.ModelSerializer):
    matchResult = FarmersSerializer(many=True,read_only=True)
    enterId = EnterpriseSerializer(read_only=True)

    class Meta:
        model = Needs
        fields = "__all__"


# class Needs(models.Model):
#     id = models.AutoField(primary_key=True, verbose_name="需求ID")
#     enterId = models.ForeignKey('user.Enterprise', on_delete=models.CASCADE, verbose_name="企业ID",null=True)
#     needsDes = models.CharField(max_length=500, null=True, verbose_name="需求描述")
#     needsFarmerType = models.IntegerField(choices=user.models.farmerType,null=True,verbose_name="所需工种")
#     needsNum = models.IntegerField(default=0,verbose_name="所需工种人员数")
#     # matchResult = models.CharField(max_length=1000, null=True, verbose_name="匹配结果")
#     matchResult = models.ManyToManyField("user.Farmers",verbose_name="匹配结果人员")  # 包工头
#     price = models.IntegerField(default=-1, verbose_name="工资")
#     #needsTime = models.CharField(max_length=500, null=True, verbose_name="开工时间")  # 时间
#     needsTime = models.DateTimeField(null=True,verbose_name="开工时间") #开工时间 --时间的匹配？
#     needsLocation = models.CharField(max_length=1000, null=True, verbose_name="工地")  # 地点
#     needsDayNum = models.IntegerField(default=0,verbose_name="工期")
#     remarks = models.CharField(max_length=2000,null=True,verbose_name="备注")
#     needsType = models.IntegerField(choices=needType, default=-1, verbose_name="需求状态")