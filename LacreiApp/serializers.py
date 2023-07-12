from rest_framework import serializers
from .models import PessoaProfissional, Consulta

class PessoaProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PessoaProfissional
        fields = '__all__'

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'
