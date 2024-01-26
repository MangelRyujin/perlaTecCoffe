from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from apps.products.api.serializers.products_serializer import CategorySerializer
from rest_framework.permissions import IsAuthenticated


class ProductsViewSet(viewsets.GenericViewSet):
    serializer_class= CategorySerializer
    # permission_classes = (IsAuthenticated,)
    
    def get_queryset(self,pk = None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(pk = pk).first()

    def list(self,request):
        products = self.get_queryset(None)
        if products.exists():
            products_serializers = self.serializer_class(products,many = True)
            return Response(products_serializers.data, status = status.HTTP_200_OK)
        return Response({'message':'No existen productos!'},status = status.HTTP_404_NOT_FOUND)
    
    def retrieve(self, request, pk = None):
        product = self.get_queryset(pk)
        if product:
            product_serializers = self.serializer_class(product)
            return Response(product_serializers.data, status= status.HTTP_200_OK)
        return Response({'message':'No existe el producto'}, status= status.HTTP_404_NOT_FOUND)
    
    