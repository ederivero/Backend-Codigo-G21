from django.db import models
from datetime import datetime


class Producto(models.Model):
    # https://docs.djangoproject.com/en/5.1/ref/models/fields/
    id = models.AutoField(primary_key=True, null=False)
    nombre = models.TextField(null=False)
    descripcion = models.TextField(null=True)

    # Para configurar opciones del modelo
    class Meta:
        # https://docs.djangoproject.com/en/5.1/ref/models/options/
        db_table = 'productos'


class Lista(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    nombrePropietario = models.TextField(
        db_column='nombre_propietario', null=False)
    fechaCreacion = models.DateTimeField(
        default=datetime.now, db_column='fecha_creacion')

    class Meta:
        db_table = 'listas'
