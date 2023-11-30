from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'attendant'

router = routers.DefaultRouter()
router.register('atendente', views.CategoryViewSet, basename='atendente')

urlpatterns = [
    path('', include(router.urls) )
]
