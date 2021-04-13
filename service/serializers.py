from rest_framework import serializers
from service.models import UsuarioPoblacion, PuestoVacunacion, ResponsableVacuna, CompuestoVacuna
from django.contrib.auth.models import User

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class UsuarioPoblacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioPoblacion
        fields = ['nombres', 'apellidos', 'direccion', 'telefono', 'ciudad', 'departamento', 'edad', 'fecha_de_nacimiento', 'codigo_de_vacunacion', 'regimen', 'estado']

class PuestoVacunacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PuestoVacunacion
        fields = ['nombre', 'direccion', 'nombre_ips', 'telefono_1', 'telefono_2', 'horario_de_atencion']

class ResponsableVacunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponsableVacuna
        fields = ['nombre', 'numero_identificacion', 'titulo_profesional', 'codigo_profesional']

class CompuestoVacunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompuestoVacuna
        fields = ['fabricante', 'codigo_fabricante', 'fecha_fabricacion', 'fecha_expiracion', 'dosis', 'paciente', 'responsable', 'consentimiento_informado']
