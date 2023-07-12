from rest_framework import viewsets
from .models import PessoaProfissional, Consulta
from .serializers import PessoaProfissionalSerializer, ConsultaSerializer

class PessoaProfissionalViewSet(viewsets.ModelViewSet):
    queryset = PessoaProfissional.objects.all()
    serializer_class = PessoaProfissionalSerializer

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
