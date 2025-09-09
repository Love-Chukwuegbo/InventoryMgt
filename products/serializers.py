from rest_framework import serializers
from .models import Product, ProductInventory



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
    # fields = ["name", "category", "unit_price","sku", "quantity"]
        fields = "__all__"

class ProductInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInventory
        fields ="__all__"