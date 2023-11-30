from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'attendant'

router = routers.DefaultRouter()
router.register('atendente', views.AtendenteViewSet, basename='atendente')

urlpatterns = [
    #path('', include((router.urls), namespace='attendant'))
    path('', include(router.urls))
]
