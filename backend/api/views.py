from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer, ProductSerializer
from .models import Product


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
