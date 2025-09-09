from rest_framework import serializers
from .models import Product, ProductCategory



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
    # fields = ["name", "category", "unit_price","sku", "quantity"]
        fields = "__all__"

class ProductInventoryList(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields ="__all__"