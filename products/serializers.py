from rest_framework import serializers
from .models import Product



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
    # fields = ["name", "category", "unit_price","sku", "quantity"]
        fields = "__all__"