from django.core.exceptions import ValidationError
from rest_framework import serializers
from apps.bar.api.serializers.aggregateItem_serializer import AggregateItemsBarSerializer
from apps.orders.models import AggregateItems, Items




        

    
    
class ItemsBarSerializer(serializers.ModelSerializer):
    aggregateitemItems = AggregateItemsBarSerializer(many = True)
    class Meta:
        model = Items
        fields = ('id','cant','amount','state','order','product','aggregateitemItems')
    
        

