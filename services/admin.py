from django.contrib import admin
from .models import Service

# Configuracion extendida para los datos de auditoría
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

# Register your models here.
admin.site.register(Service, ServiceAdmin)