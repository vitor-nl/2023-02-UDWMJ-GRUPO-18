from .models import Atendente
from rest_framework import serializers

class AtendenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atendente
        fields = '__all__'