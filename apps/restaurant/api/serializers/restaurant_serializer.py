from django.core.exceptions import ValidationError
from rest_framework import serializers
from apps.restaurant.models import Local,Lounge,Table



        
class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ('id','state','number','lounge','active','max_people')
        
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'number' : instance.number,
            'state' : instance.state,
            'active' : instance.active,
            'max_people' : instance.max_people,
            
        }
    
    
class LoungeSerializer(serializers.ModelSerializer):
    tableLounge = TableSerializer(many = True, read_only=True)
    class Meta:
        model = Lounge
        fields = ('id','lounge_name','active','tableLounge')
        

        
class LocalSerializer(serializers.ModelSerializer):
    loungeLocal = LoungeSerializer(many = True, read_only=True)
    class Meta:
        model = Local
        fields = ('id','local_name','active','loungeLocal')
        