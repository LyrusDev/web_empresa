from django.apps import AppConfig


class ServicesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'services'
    # Nombre general en el admin
    verbose_name = 'Gestor de servicios'
