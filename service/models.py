from django.utils.translation import gettext_lazy as _
from django.db import models

REGIMEN = (
    ('contributivo', _('Contributivo')),
    ('subsidiado', _('Subsidiado'))
)

ESTADO = (
    ('no_vacunado', _('No Vacunado')),
    ('proceso_iniciado', _('Proceso de vacunación iniciado')),
    ('vacunado', _('Vacunado'))
)

DOSIS = (
    ('primera', _('Primera dosis')),
    ('segunda', _('Segunda dosis'))
)


class PuestoVacunacion(models.Model):
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    nombre_ips = models.CharField(max_length=50)
    telefono_1 = models.CharField(max_length=30)
    telefono_2 = models.CharField(max_length=30)
    horario_de_atencion = models.CharField(max_length=30)


class ResponsableVacuna(models.Model):
    nombre = models.CharField(max_length=30)
    numero_identificacion = models.CharField(max_length=30)
    titulo_profesional = models.CharField(max_length=40)
    codigo_profesional = models.CharField(max_length=30)

class UsuarioPoblacion(models.Model):
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    edad = models.IntegerField()
    fecha_de_nacimiento = models.DateField()
    codigo_de_vacunacion = models.CharField(max_length=15)
    puesto_vacunacion = models.ForeignKey(
        PuestoVacunacion, on_delete=models.CASCADE, related_name='puesto_vacunacion'
    )

    regimen = models.CharField(
        max_length=32,
        choices=REGIMEN,
        default='contributivo',
    )

    estado = models.CharField(
        max_length=32,
        choices=ESTADO,
        default='no_vacunado',
    )


class CompuestoVacuna(models.Model):
    fabricante = models.CharField(max_length=30)
    codigo_fabricante = models.CharField(max_length=20)
    fecha_fabricacion = models.DateField()
    fecha_expiracion = models.DateField()
    dosis = models.CharField(
        max_length=32,
        choices=DOSIS,
        default='primera'
    )
    paciente = models.ForeignKey(
        UsuarioPoblacion, on_delete=models.CASCADE, related_name='paciente')
    responsable = models.ForeignKey(
        ResponsableVacuna, on_delete=models.CASCADE, related_name='responsable')
    consentimiento_informado = models.FileField()