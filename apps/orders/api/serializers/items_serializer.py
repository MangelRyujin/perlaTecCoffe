from django.core.exceptions import ValidationError
from rest_framework import serializers
from apps.orders.api.serializers.aggregateItem_serializer import AggregateItemsSerializer
from apps.orders.models import AggregateItems, Items




        

    
    
class ItemsSerializer(serializers.ModelSerializer):
    aggregateitemItems = AggregateItemsSerializer(many = True)
    class Meta:
        model = Items
        fields = ('id','cant','amount','state','order','product','aggregateitemItems')
        
    def create(self, validated_data):
        aggregateitems_data = validated_data.pop('aggregateitemItems')
        item = Items.objects.create(**validated_data)
        cant=item.amount
        for aggregateitem_data in aggregateitems_data:
            aggregate = AggregateItems.objects.create(item=item, **aggregateitem_data)
            cant+=aggregate.aggregate.cost
        item.amount=cant
        item.save()
        return item
        

