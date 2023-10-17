from django.contrib import admin
from.models import Empleado, Habilidades

# Register your models here.
admin.site.register(Habilidades)

#List_display: para ordenar por columnas los datos ingresados
class EmpleadoAdmin(admin.ModelAdmin):
    list_display=(
        "nombre", 
        "apellido",
        "trabajo",
        "departamento", 
    )

admin.site.register(Empleado, EmpleadoAdmin)