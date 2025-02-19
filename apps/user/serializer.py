from rest_framework import  serializers

from user.models import Enterprise, Farmers, FarmersMember, Administrator, Foreman


class EnterpriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enterprise
        exclude = ('password',)


class FarmersMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmersMember
        fields = "__all__"




class ForemanSerializer(serializers.ModelSerializer):
    #groups = FarmersSerializer(read_only=True, many=True)
    class Meta:
        model = Foreman
        exclude = ('password','openid',)

class FarmersSerializer(serializers.ModelSerializer):
    #members  = FarmersMemberSerializer(read_only=True, many=True)
    leader = ForemanSerializer(read_only=True)
    class Meta:
        model = Farmers
        fields = "__all__"




class AdministratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrator
        exclude = ('password',)
# class EnterpriseSerializer(serializers.Serializer):
#     name = serializers.CharField()
#     enterName = serializers.CharField(default="000")
#     authState = serializers.IntegerField(default=-1)
#
#
#
#     def create(self, validated_data):  # 增
#         enterprise = Enterprise.objects.create(name = validated_data['username'],password = validated_data['password'])
#         return enterprise
#
#     def update(self, instance, validated_data):  # 更新密码
#         instance.password = validated_data['password']
#         instance.save()
#         return instance
#
#
# class FarmersSerializer(serializers.Serializer):
#     name = serializers.CharField()
#     type = serializers.IntegerField(default=-1)
#     ingNeed = serializers.CharField(default="-1")
#
#     def create(self, validated_data):  # 增
#         farmer = Farmers.objects.create(name = validated_data['username'],password = validated_data['password'])
#         return farmer
#
#     def update(self, instance, validated_data):  # 更新密码
#         instance.password = validated_data['password']
#         instance.save()
#         return instance
