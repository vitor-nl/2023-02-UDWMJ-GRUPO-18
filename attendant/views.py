from django.shortcuts import render
from .models import Atendente
from rest_framework import viewsets
from .serializer import AtendenteSerializer

# Create your views here.

class AtendenteViewSet(viewsets.ModelViewSet):
    queryset = Atendente.objects.all()
    serializer_class = AtendenteSerializer  