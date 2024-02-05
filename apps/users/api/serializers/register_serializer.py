from rest_framework import serializers
from apps.users.models import User
from django.core.exceptions import ValidationError
import io
from django.core.files.base import ContentFile


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name','last_name','email','username','movil','password','ci','user_type')
        
    def validate_password(self,data):
        if len(data) < 8:
            raise ValidationError("La contraseña debe poseer más de 8 caracteres")
        if data.lower() == data:
            raise ValidationError("La contraseña debe poseer al menos una mayúscula")
        return data
    
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    