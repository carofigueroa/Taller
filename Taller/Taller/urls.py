"""Taller URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from Maternidad import views



admin.site.site_header="Hospital San Juan de Dios."
admin.site.site_title = "Hospital San Juan de Dios."
admin.site.index_title = "Administración: Unidad Gineco-Obstetra."

urlpatterns = [
    path('admin/', admin.site.urls, name="Admi"),
    path('',views.main, name='Inicio'),
    path('cir/', views.cirugia, name="cirugia"),
    path('med/',views.medicamento, name="Medicamentos"),
    path('emb/',views.embarazos, name="Embarazos"),
    path('camas/',views.camas, name="Camas")
]

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)