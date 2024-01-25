from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from apps.restaurant.api.serializers.restaurant_serializer import LocalSerializer
from rest_framework.permissions import IsAuthenticated


class RestaurantViewSet(viewsets.GenericViewSet):
    serializer_class= LocalSerializer
    # permission_classes = (IsAuthenticated,)
    
    def get_queryset(self,pk = None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(pk = pk).first()

    def list(self,request):
        local = self.get_queryset(None)
        if local.exists():
            local_serializers = self.serializer_class(local,many = True)
            return Response(local_serializers.data, status = status.HTTP_200_OK)
        return Response({'message':'No existen locales!'},status = status.HTTP_404_NOT_FOUND)
    
    def retrieve(self, request, pk = None):
        local = self.get_queryset(pk)
        if local:
            local_serializers = self.serializer_class(local)
            return Response(local_serializers.data, status= status.HTTP_200_OK)
        return Response({'message':'No existe el local'}, status= status.HTTP_404_NOT_FOUND)
    
    