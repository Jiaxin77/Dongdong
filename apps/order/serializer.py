from rest_framework import  serializers
from needs.serializer import NeedsSerializer
from order.models import Order
from user.serializer import FarmersSerializer


class OrderSerializer(serializers.ModelSerializer):
    needId = NeedsSerializer(read_only=True)
    #farmers = FarmersSerializer(read_only=True)
    money = serializers.DecimalField(max_digits=20, decimal_places=2)
    moneyToFarmers = serializers.DecimalField(max_digits=20,decimal_places=2)
    moneyToApp = serializers.DecimalField(max_digits=20,decimal_places=2)
    class Meta:
        model = Order
        fields = "__all__"