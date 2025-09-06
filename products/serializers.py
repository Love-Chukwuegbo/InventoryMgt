from rest_framework import serializers
from .models import Product



class ProductSerializer(serializers.ModelSerializer):
    model = Product
    fields = ("name", "category", "unit_price","sku", "quantity,")