from django.shortcuts import render
from rest_framework import generics, serializers
from .models import Product
from .serializers import ProductSerializer, ProductWritableSerializer


class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'product_id'

class ProductDestroy(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer        
    lookup_url_kwarg = 'product_id'

class ProductCreate(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductWritableSerializer        
    lookup_url_kwarg = 'product_id'