from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet,ProductInventoryList


router = DefaultRouter()
router.register(r"product", ProductViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("inventory", ProductInventoryList),
    
]