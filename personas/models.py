from django.db import models

# Create your models here.
class Persona(models.Model):
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    email = models.TextField()
    telefono = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

class Medico(models.Model):
    tipo_documento = models.CharField(max_length=10)
    numero_documento = models.CharField(max_length=20, unique=True)
    primer_nombre = models.CharField(max_length=50)
    segundo_nombre = models.CharField(max_length=50, blank=True, null=True)
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.primer_nombre} {self.primer_apellido}"