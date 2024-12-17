from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClothesViewSet
from .views import CarViewSet

router = DefaultRouter()
router.register(r'items', ClothesViewSet, basename='item')
router.register(r'items_2', CarViewSet, basename='item_2')

urlpatterns = [
    path('', include(router.urls)),
]