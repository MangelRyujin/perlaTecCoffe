from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from apps.orders.api.serializers.orders_serializer import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from apps.products.models import Product
from apps.restaurant.models import Table
from apps.orders.models import Items, Order
from apps.orders.api.serializers.items_serializer import ItemsSerializer
from decimal import Decimal
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


transfer = openapi.Parameter('transfer', openapi.IN_QUERY, description="enter transfer", type=openapi.TYPE_NUMBER)
cash = openapi.Parameter('cash', openapi.IN_QUERY, description="enter cash", type=openapi.TYPE_NUMBER)
order = openapi.Parameter('order', openapi.IN_QUERY, description="enter order", type=openapi.TYPE_NUMBER)
table = openapi.Parameter('table', openapi.IN_QUERY, description="enter table", type=openapi.TYPE_NUMBER)
item = openapi.Parameter('item', openapi.IN_QUERY, description="enter item", type=openapi.TYPE_NUMBER)



class OrderViewSet(viewsets.GenericViewSet):
    serializer_class= OrderSerializer
    permission_classes = (IsAuthenticated,)
    
    def get_queryset(self,pk = None,user = None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(user=user).filter(state = 'Unpaid')
        else: return self.get_serializer().Meta.model.objects.filter(table = pk).filter(user=user).filter(state = 'Unpaid').first()

    
    #method list all orders with state Unpaid
    def list(self, request, pk = None):

        product = self.get_queryset(None,request.user.id)
        if product:
            product_serializers = self.serializer_class(product, many=True)
            return Response(product_serializers.data, status= status.HTTP_200_OK)
        return Response({'message':'No existen ordenes'}, status= status.HTTP_404_NOT_FOUND)
    
    #method list detail order id with state Unpaid
    def retrieve(self, request, pk = None):

        product = self.get_queryset(pk,request.user.id)
        if product:
            product_serializers = self.serializer_class(product)
            return Response(product_serializers.data, status= status.HTTP_200_OK)
        return Response({'message':'No existe la orden'}, status= status.HTTP_404_NOT_FOUND)
    
    #method for create order in table id
    @swagger_auto_schema(manual_parameters=[table])
    @action(detail = False, methods = ['post'])
    def createOrder(self,request):
        table = get_object_or_404(Table, pk = request.data['table'])
        data = {'table':table.id , 'user': request.user.id, 'amount':0}
        serializer = self.serializer_class(data = data)
        if serializer.is_valid():
            serializer.save()
            table.state='busy'
            table.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    #method for create item order in order id 
    @swagger_auto_schema(manual_parameters=[order])
    @action(detail = False, methods = ['post'])
    def createItemOrder(self,request):
        order = get_object_or_404(Order, pk = request.data['order'])
        if order.state =='Unpaid':
            product = get_object_or_404(Product, pk = request.data['product'])
            if product.discount > 0:
                amount=Decimal(((product.cost*product.discount)/100)*int(request.data['cant']))   
            else: 
                amount=Decimal(product.cost*int(request.data['cant']))
            data = {'order':order.id , 'product': product.id, 'state':'Delivered','cant':request.data['cant'], 'amount': amount,'aggregateitemItems':request.data['aggregateitemItems']}
            serializer = ItemsSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'la orden ya esta pagada'},status=status.HTTP_400_BAD_REQUEST)
    
    #method for paid transfer order id
    @swagger_auto_schema(manual_parameters=[order],responses={status.HTTP_200_OK: 'Cuenta pagada',})
    @action(detail = False, methods = ['post'])
    def paidOrderTransfer(self,request):
        order = get_object_or_404(Order, pk = request.data['order'])
        if order.state == 'Unpaid':
            items = Items.objects.filter(order=request.data['order'])
            if items.exists():
                amount = 0
                for item in items:
                    amount+=item.amount
                order.amount = amount
                order.paid = 'Transfer'
                order.paidOrder()
                order.save()
                order.table.state='available'
                order.table.save()
                return Response({'message':'Cuenta pagada'},status=status.HTTP_200_OK)
            return Response({'error':'Esta cuenta no contiene pedidos'},status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'Esta cuenta ya ha sido pagada'},status=status.HTTP_400_BAD_REQUEST)
    
    
    #method for paid cash order id
    @swagger_auto_schema(manual_parameters=[order],responses={status.HTTP_200_OK: 'Cuenta pagada',})
    @action(detail = False, methods = ['post'])
    def paidOrderCash(self,request):
        order = get_object_or_404(Order, pk = request.data['order'])
        if order.state == 'Unpaid':
            items = Items.objects.filter(order=request.data['order'])
            if items.exists():
                amount = 0
                for item in items:
                    amount+=item.amount
                order.amount = amount
                order.paid = 'Cash'
                order.paidOrder()
                order.save()
                order.table.state='available'
                order.table.save()
                return Response({'message':'Cuenta pagada'},status=status.HTTP_200_OK)
            return Response({'error':'Esta cuenta no contiene pedidos'},status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'Esta cuenta ya ha sido pagada'},status=status.HTTP_400_BAD_REQUEST)
    
    
    #method for paid both order id
    @swagger_auto_schema(manual_parameters=[order,transfer,cash],responses={status.HTTP_200_OK: 'Cuenta pagada',})
    @action(detail = False, methods = ['post'])
    def paidOrderBoth(self,request):                    
        order = get_object_or_404(Order, pk = request.data['order'])
        if order.state == 'Unpaid':
            items = Items.objects.filter(order=request.data['order'])
            if items.exists():
                amount = 0
                for item in items:
                    amount+=item.amount
                both = 0 
                if int(request.data['transfer']) > 0 and int(request.data['cash']) > 0:
                    both = Decimal(request.data['transfer']) + Decimal(request.data['cash'])
                    if both == amount:
                        order.amount = amount
                        order.paid = 'Both'
                        order.transfer = Decimal(request.data['transfer'])
                        order.cash = Decimal(request.data['cash'])
                        order.paidOrder()
                        order.save()
                        order.table.state='available'
                        order.table.save()
                        return Response({'message':f'Cuenta pagada'},status=status.HTTP_200_OK)
                    return Response({'error':'El total a pagar no coincide con la suma de la transferencia y el efectivo'},status=status.HTTP_400_BAD_REQUEST)
                return Response({'error':'Introduzca un cantidad en transferencia y efectivo'},status=status.HTTP_400_BAD_REQUEST)
            return Response({'error':'Esta cuenta no contiene pedidos'},status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'Esta cuenta ya ha sido pagada'},status=status.HTTP_400_BAD_REQUEST)
    
    
    #method for delete order
    @swagger_auto_schema(manual_parameters=[order])
    @action(detail = False, methods = ['delete'])
    def deleteOrder(self,request):
        order = get_object_or_404(Order, pk = request.data['order'])
        if order.state =='Unpaid':
            order.delete()
            return Response({'message':'Orden cancelada'},status=status.HTTP_200_OK)
        return Response({'error':'La orden ya esta pagada'},status=status.HTTP_400_BAD_REQUEST)
    
    
    #method for delete item of order
    @swagger_auto_schema(manual_parameters=[item])
    @action(detail = False, methods = ['delete'])
    def deleteItemOrder(self,request):
        item = get_object_or_404(Items, pk = request.data['item'])
        if item.state=='Delivered':
            item.delete()
            return Response({'message':'Pedido cancelado'},status=status.HTTP_200_OK)
        return Response({'message':f'Ya se está {item.state}'},status=status.HTTP_400_BAD_REQUEST)