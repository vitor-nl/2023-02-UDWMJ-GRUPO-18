from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'consult'

router = routers.DefaultRouter()
router.register('consulta', views.CategoryViewSet, basename='consulta')

urlpatterns = [
    path('', include(router.urls) )
]
