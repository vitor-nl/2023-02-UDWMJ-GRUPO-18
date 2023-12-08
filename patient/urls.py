from django.urls import path, include
from . import views
from rest_framework import routers
from .views import cadastrar_paciente
from .views import LoginPageView

app_name = 'patient'

router = routers.DefaultRouter()
router.register('paciente', views.PacienteViewSet, basename='paciente')

urlpatterns = [
    #path('', include((router.urls), namespace='patient'))
    path('', include(router.urls)),
    path('login/', LoginPageView.as_view(), name='login'),
]
