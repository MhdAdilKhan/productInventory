from django.urls import path, include
from .views import (ProductInventoryViewSet)
from rest_framework.routers import DefaultRouter
# import django_eventstream
router = DefaultRouter()

router.register(r'inventory', ProductInventoryViewSet, basename='doc-images')

urlpatterns = [
	path('', include(router.urls)),
]