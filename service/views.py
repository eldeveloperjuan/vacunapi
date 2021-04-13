from service.models import UsuarioPoblacion, PuestoVacunacion, ResponsableVacuna, CompuestoVacuna
from service.serializers import UsuarioPoblacionSerializer, PuestoVacunacionSerializer, ResponsableVacunaSerializer, CompuestoVacunaSerializer, UsuarioSerializer
from rest_framework import generics
from django.contrib.auth.models import User

class UsuarioLista(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetalle(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioPoblacionLista(generics.ListCreateAPIView):
    queryset = UsuarioPoblacion.objects.all()
    serializer_class = UsuarioPoblacionSerializer


class UsuarioPoblacionDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = UsuarioPoblacion.objects.all()
    serializer_class = UsuarioPoblacionSerializer

class PuestoVacunacionLista(generics.ListCreateAPIView):
    queryset = PuestoVacunacion.objects.all()
    serializer_class = PuestoVacunacionSerializer

class PuestoVacunacionDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = PuestoVacunacion.objects.all()
    serializer_class = PuestoVacunacionSerializer

class ResponsableVacunaLista(generics.ListCreateAPIView):
    queryset = ResponsableVacuna.objects.all()
    serializer_class = ResponsableVacunaSerializer

class ResponsableVacunaDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = ResponsableVacuna.objects.all()
    serializer_class = ResponsableVacunaSerializer

class CompuestoVacunaLista(generics.ListCreateAPIView):
    queryset = CompuestoVacuna.objects.all()
    serializer_class = CompuestoVacunaSerializer

class CompuestoVacunaDetalle(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompuestoVacuna.objects.all()
    serializer_class = CompuestoVacunaSerializer