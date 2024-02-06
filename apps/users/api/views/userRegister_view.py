from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from apps.users.api.serializers.userRegister_serializer import RegisterSerializer
from rest_framework.permissions import IsAuthenticated
from apps.users.permission.super_user_permission import IsSuperUserOrAdmin

  
class RegisterViewSet(viewsets.GenericViewSet):
    serializer_class= RegisterSerializer
    permission_classes = (IsAuthenticated,IsSuperUserOrAdmin)
    
    def create(self, request):
        serializers = self.serializer_class(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'message':'Usuario creado correctamente!'}, status = status.HTTP_201_CREATED)
        return Response(serializers.errors,status = status.HTTP_400_BAD_REQUEST)
    