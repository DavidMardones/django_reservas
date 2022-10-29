from django.db import models
from django.core import validators

# Create your models here.
class reserva(models.Model) :
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    fecha = models.DateField()
    hora = models.CharField(max_length=20)
    numeroPersonas = models.IntegerField()
    estado = models.CharField(max_length=50)
    observacion = models.CharField(max_length=50)