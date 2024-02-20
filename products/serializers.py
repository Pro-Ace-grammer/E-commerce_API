from rest_framework import serializers
from .models import Product, CartItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    # Using below statement we can get the details of particular product associated to the specific id
    # product_id = ProductSerializer()
    class Meta:
        model = CartItem
        fields = '__all__'