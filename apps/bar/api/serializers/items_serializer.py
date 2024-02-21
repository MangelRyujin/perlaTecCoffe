from django.core.exceptions import ValidationError
from rest_framework import serializers
from apps.bar.api.serializers.aggregateItem_serializer import AggregateItemsBarSerializer
from apps.orders.models import AggregateItems, Items




        

    
    
class ItemsBarSerializer(serializers.ModelSerializer):
    aggregateitemItems = AggregateItemsBarSerializer(many = True)
    class Meta:
        model = Items
        fields = ('id','cant','amount','state','order','product','aggregateitemItems')
    
    def to_representation(self, instance):
        # Primero llamamos al método original para obtener la representación básica
        representation = super().to_representation(instance)
        
        # Reemplazamos el valor del campo 'product' por su 'product_name'
        representation['product'] = instance.product.product_name
        return representation
    

