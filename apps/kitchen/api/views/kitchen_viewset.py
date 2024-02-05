from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from apps.kitchen.api.serializers.items_serializer import ItemsKitchenSerializer
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.shortcuts import get_object_or_404
from apps.orders.models import Items


item = openapi.Parameter('item', openapi.IN_QUERY, description="enter item", type=openapi.TYPE_NUMBER)


class ItemsKitchenViewSet(viewsets.GenericViewSet):
    serializer_class= ItemsKitchenSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self,pk = None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.exclude(state='Finished')
        return self.get_serializer().Meta.model.objects.exclude(state='Finished').first()

    
    #method list all orders with state Unpaid
    def list(self, request):
        items = self.get_queryset(None)
        if items:
            items_serializers = self.serializer_class(items, many=True)
            return Response(items_serializers.data, status= status.HTTP_200_OK)
        return Response({'message':'No existen pedidos'}, status= status.HTTP_404_NOT_FOUND)
    
    @swagger_auto_schema(manual_parameters=[item])
    @action(detail = False, methods = ['put'])
    def elaboratingStateItem(self,request):
        item = get_object_or_404(Items, pk = request.data['item'])
        item.elaborating_state()
        item_serializer = self.serializer_class(item)
        return Response(item_serializer.data,status=status.HTTP_201_CREATED)
    
    @swagger_auto_schema(manual_parameters=[item])
    @action(detail = False, methods = ['put'])
    def finishedStateItem(self,request):
        item = get_object_or_404(Items, pk = request.data['item'])
        item.finished_state()
        item_serializer = self.serializer_class(item)
        return Response(item_serializer.data,status=status.HTTP_201_CREATED)
        