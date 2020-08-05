from django.contrib import admin

# Register your models here.

from django.contrib import admin
from Maternidad.models import paciente,profesional,medicamentos,tipo_reposo, cirugias, regimen, hoja_indicaciones
from Maternidad.models import cadacuanto, controles, prevision,recien_nacido,  examene
# Register your models here.


class Paciente_Admin (admin.ModelAdmin):
    list_display=("rut","nombre","apellido","edad","prevision","embarazada")
    search_fields=("nombre","apellido")
    
class Profesional_Admin(admin.ModelAdmin):
    list_display=("rut","nombre_completo","profesion")

class Medicamento_Admin(admin.ModelAdmin):
    list_display=("nombre","dosis")


class Reposo_Admin(admin.ModelAdmin):
    list_display=("nombre",)


class Cirugias_Admin(admin.ModelAdmin):
    list_display=("nombre_cirugia",)

class Regimen_Admin(admin.ModelAdmin):
    list_display=("tipo_regimen",)

class Hoja_Admin(admin.ModelAdmin):
    list_display=("fecha","nombre_profesional","nombre_paciente","tipo_regimen","Nombre_cirugias",
                 "reposo","control")
    search_fields=("nombre_paciente","nombre_profesional")
    list_filter=("fecha","tipo_regimen")
    date_hierarchy="fecha"
class  Examenes_Admin(admin.ModelAdmin):
    list_display=("nombre_examen",)

admin.site.register(paciente,Paciente_Admin)
admin.site.register(profesional,Profesional_Admin)
admin.site.register(medicamentos,Medicamento_Admin)
admin.site.register(tipo_reposo,Reposo_Admin)
admin.site.register(cirugias,Cirugias_Admin)
admin.site.register(regimen,Regimen_Admin)
admin.site.register(hoja_indicaciones,Hoja_Admin)
admin.site.register(cadacuanto)
admin.site.register(controles)
admin.site.register(recien_nacido)
admin.site.register(prevision)
admin.site.register(examene,Examenes_Admin)
