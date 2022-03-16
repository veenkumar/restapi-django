from rest_framework import serializers
from .models import CartItem, SendYourQueries


class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(max_length=200)
    product_price = serializers.FloatField()
    product_quantity = serializers.IntegerField(required=False, default=1)

    class Meta:
        model = CartItem
        fields = ('__all__')

class SendYourQueriesSerializer(serializers.ModelSerializer):
    service_type = serializers.CharField(max_length=30)
    name = serializers.CharField(max_length=100)
    company = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=200)
    contact_no = serializers.CharField(max_length=20)
    email = serializers.CharField(max_length=100)
    your_queries = serializers.CharField(max_length=200)

    class Meta:
        model = SendYourQueries
        fields = ('__all__')
