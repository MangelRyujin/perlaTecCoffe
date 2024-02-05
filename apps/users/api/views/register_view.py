from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from apps.users.api.serializers.register_serializer import RegisterSerializer

@api_view(["POST"])
def user_register(request):
    serializers = RegisterSerializer(data = request.data)
    if serializers.is_valid():
        serializers.save()
        return Response({'message':'Usuario creado correctamente!'}, status = status.HTTP_201_CREATED)
    return Response(serializers.errors,status = status.HTTP_400_BAD_REQUEST)
    
