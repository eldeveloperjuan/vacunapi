from service.models import UsuarioPoblacion, PuestoVacunacion, ResponsableVacuna, CompuestoVacuna
from service.serializers import UsuarioPoblacionSerializer, PuestoVacunacionSerializer, ResponsableVacunaSerializer, CompuestoVacunaSerializer, UsuarioSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated 

class UsuarioLista(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)  
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetalle(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)  
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioPoblacionLista(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)  
    queryset = UsuarioPoblacion.objects.all()
    serializer_class = UsuarioPoblacionSerializer


class UsuarioPoblacionDetalle(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)  
    queryset = UsuarioPoblacion.objects.all()
    serializer_class = UsuarioPoblacionSerializer

class PuestoVacunacionLista(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)  
    queryset = PuestoVacunacion.objects.all()
    serializer_class = PuestoVacunacionSerializer

class PuestoVacunacionDetalle(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)  
    queryset = PuestoVacunacion.objects.all()
    serializer_class = PuestoVacunacionSerializer

class ResponsableVacunaLista(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)  
    queryset = ResponsableVacuna.objects.all()
    serializer_class = ResponsableVacunaSerializer

class ResponsableVacunaDetalle(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)  
    queryset = ResponsableVacuna.objects.all()
    serializer_class = ResponsableVacunaSerializer

class CompuestoVacunaLista(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)  
    queryset = CompuestoVacuna.objects.all()
    serializer_class = CompuestoVacunaSerializer

class CompuestoVacunaDetalle(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)  
    queryset = CompuestoVacuna.objects.all()
    serializer_class = CompuestoVacunaSerializer