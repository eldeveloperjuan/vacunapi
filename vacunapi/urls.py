"""vacunapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from service.views import UsuarioPoblacionLista, UsuarioPoblacionDetalle, PuestoVacunacionLista, PuestoVacunacionDetalle, ResponsableVacunaLista, ResponsableVacunaDetalle,  CompuestoVacunaLista, CompuestoVacunaDetalle, UsuarioLista, UsuarioDetalle

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', UsuarioLista.as_view()),
    path('usuario/<int:pk>/', UsuarioDetalle.as_view()),
    path('usuarios_poblacion/', UsuarioPoblacionLista.as_view()),
    path('usuario_poblacion/', UsuarioPoblacionDetalle.as_view()),
    path('puestos_vacunacion/', PuestoVacunacionLista.as_view()),
    path('puesto_vacunacion/', PuestoVacunacionDetalle.as_view()),
    path('responsables_vacuna/', ResponsableVacunaLista.as_view()),
    path('responsable_vacuna/', ResponsableVacunaDetalle.as_view()),
    path('responsables_vacuna/', CompuestoVacunaLista.as_view()),
    path('responsable_vacuna/', CompuestoVacunaDetalle.as_view())
]
