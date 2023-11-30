from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'consult'

router = routers.DefaultRouter()
router.register('consulta', views.ConsultaViewSet, basename='consulta')

urlpatterns = [
    #path('', include((router.urls), namespace='consult')),
    path('', include(router.urls)), #adicionei o namespace, mas dps pediu para eu alterar novamente
]
