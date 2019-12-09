from rest_framework import  serializers
from needs.serializer import NeedsSerializer
from order.models import Order


class OrderSerializer(serializers.ModelSerializer):
    needId = NeedsSerializer(read_only=True)

    class Meta:
        model = Order
        fields = "__all__"