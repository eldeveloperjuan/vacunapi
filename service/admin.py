from django.contrib import admin
from service.models import PuestoVacunacion

# Register your models here.
class PuestoVacunacionAdmin(admin.ModelAdmin):
    pass

# Register the admin class with the associated model
admin.site.register(PuestoVacunacion, PuestoVacunacionAdmin)