from django.core.exceptions import ValidationError
from rest_framework import serializers
from apps.orders.api.serializers.items_serializer import ItemsSerializer
from apps.orders.models import Order
from apps.restaurant.api.serializers.restaurant_serializer import TableSerializer



        
class OrderSerializer(serializers.ModelSerializer):
    itemsOrder = ItemsSerializer(many = True, read_only=True)
    class Meta:
        model = Order
        fields = ('id','amount','state','user','table','itemsOrder','date','time')
        

        
