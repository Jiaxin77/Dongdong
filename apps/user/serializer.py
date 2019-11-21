from rest_framework import  serializers

from user.models import Enterprise, Farmers, FarmersMember


class EnterpriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enterprise
        exclude = ('password',)


class FarmersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmers
        exclude = ('password',)



class FarmersMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmersMember
        field = "__all__"


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
