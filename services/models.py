from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    subtitle = models.CharField(max_length=100, verbose_name='Subtítulo')
    image = models.ImageField(verbose_name='Imagen', upload_to='servicess')
    content = models.TextField(verbose_name='Contenido')
    
    # Auditoría
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')
    
    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['-created']
    
    # Función para que devuelva el título en el gestor de servicios
    def __str__(self):
        return self.title
