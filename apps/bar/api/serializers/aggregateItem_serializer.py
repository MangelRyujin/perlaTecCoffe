from django.core.exceptions import ValidationError
from rest_framework import serializers
from apps.orders.models import AggregateItems



        

    
    
class AggregateItemsBarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = AggregateItems
        fields = ('id','aggregate')
        
    def to_representation(self, instance):
        return {
            'id':instance.id,
            'aggregate':instance.aggregate.agregate_name,
        }
        

