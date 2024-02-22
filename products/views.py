from rest_framework.viewsets import ModelViewSet
from .models import Category, Product
from .serializers import ProductListSerializer, ProductSerializer, CategorySerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser


class PermissionMixin:
    def get_permissions(self):
        if self.action in ('retrieve', 'list'):
            permissions = [AllowAny]
        else:
            permissions = [IsAdminUser]
        return [permission() for permission in permissions]

    
class CategoryViewSet(PermissionMixin, ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class ProductViewSet(PermissionMixin, ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        return self.serializer_class
        






