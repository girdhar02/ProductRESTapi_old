from django.shortcuts import render
from  rest_framework import generics
from library.models import Product
from library.serializiers import ProductSerializer

# Create your views here.

class ProductList(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= Product
    serializer_class=ProductSerializer

