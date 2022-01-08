"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from AppCoder.views import crea_curso
from core.views import despedirse, saluda_con_nombre, saluda_con_template, saludo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludar', saludo),
    path('chau', despedirse),
    path('saluda_nombre/<nombre>', saluda_con_nombre), #/<nombre> es una variable que se completa: /y escribis tu nombre en el buscador.
    path('saluda-template', saluda_con_template),
    path('crea-curso/<nombre>/<camada>', crea_curso)
]
