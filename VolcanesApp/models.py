# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Volcanes(models.Model):
    OBJECTID = models.AutoField(primary_key=True)
    NOMBREVOLC = models.CharField(max_length=200)
    ALTURASOBR = models.CharField(max_length=1024)
    LATITUD = models.CharField(max_length=50)
    LONGITUD = models.CharField(max_length=50)
    URL = models.CharField(max_length=1024)
    ACTIVIDAD = models.CharField(max_length=50)
    IMAGEN = models.CharField(max_length=500)
    DETALLE = models.CharField(max_length=500)
    IMAGENESGALERIA = models.CharField(max_length=500)

# Create your models here.
