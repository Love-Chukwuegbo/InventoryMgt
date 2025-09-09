from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import Product,ProductInventory
from .serializers import ProductSerializer, ProductInventorySerializer;
from .permissions import IsAuthorOrReadOnly
# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthorOrReadOnly,)

class ProductInventoryList(generics.ListAPIView):
    queryset=ProductInventory.objects.all()
    serializer_class = ProductInventorySerializer
