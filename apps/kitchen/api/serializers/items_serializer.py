from django.core.exceptions import ValidationError
from rest_framework import serializers
from apps.kitchen.api.serializers.aggregateItem_serializer import AggregateItemsKitchenSerializer
from apps.orders.models import AggregateItems, Items




        

    
    
class ItemsKitchenSerializer(serializers.ModelSerializer):
    aggregateitemItems = AggregateItemsKitchenSerializer(many = True)
    class Meta:
        model = Items
        fields = ('id','cant','amount','state','order','product','aggregateitemItems')
    
        

