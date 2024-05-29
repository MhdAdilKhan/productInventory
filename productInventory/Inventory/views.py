from django.shortcuts import render
from rest_framework import viewsets
from .serializers import (ProductInventorySerializer)
from .models import (ProductInventory)
# Create your views here.

class ProductInventoryViewSet(viewsets.ModelViewSet):
	queryset = ProductInventory.objects.all()
	serializer_class = ProductInventorySerializer
	http_method_names = ['get','post','patch','delete']