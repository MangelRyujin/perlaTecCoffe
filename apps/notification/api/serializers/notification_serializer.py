from django.core.exceptions import ValidationError
from rest_framework import serializers
from apps.notification.models import Notification



        

    
    
class NotificationsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Notification
        fields = ('id','item','user','date','time')
        
    def to_representation(self, instance):
        return {
            'id':instance.id,
            'item':instance.item.product.product_name,
            'user':instance.user.username,
            'table':instance.item.order.table.number,
            'date':instance.date,
            'time':instance.time,
        }
        

