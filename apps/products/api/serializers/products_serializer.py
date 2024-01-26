from django.core.exceptions import ValidationError
from rest_framework import serializers
from apps.products.models import *



        
class AggregateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aggregate
        fields = ('id','agregate_name','measurement_unit','measurement_unit_quantity','cost')
        
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id','ingredient_name')
        

    
    
class ProductSerializer(serializers.ModelSerializer):
    agregateProduct = AggregateSerializer(many = True, read_only=True)
    ingredientProduct = IngredientSerializer(many = True, read_only=True)
    class Meta:
        model = Product
        fields = ('id','product_name','cost','discount','image','ingredientProduct','agregateProduct')
        

        
class CategorySerializer(serializers.ModelSerializer):
    productCategory = ProductSerializer(many = True, read_only=True)
    class Meta:
        model = Category
        fields = ('id','category_name','productCategory')
        