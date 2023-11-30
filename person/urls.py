from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'person'

router = routers.DefaultRouter()
router.register('pessoa', views.PessoaViewSet, basename='pessoa')

urlpatterns = [
    #path('', include((router.urls), namespace='consult'))
    path('', include(router.urls))
]
