# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView
from .models import Volcanes
from django.core.urlresolvers import reverse_lazy

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.views.generic.edit import FormView
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
#Importamos el formulario de autenticación de django
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import JsonResponse
from django.core import serializers
import json
import jsonpickle
from json import JSONEncoder


class Attributes(object):
    def __init__(self, objectid, nombrevolc, alturasobr, latitud, longitud, url, actividad, imagen, detalle, imagenesgaleria):
        self.objectid = objectid
        self.nombrevolc = nombrevolc
        self.alturasobr = alturasobr
        self.latitud = latitud
        self.longitud = longitud
        self.url = url
        self.actividad = actividad
        self.imagen = imagen
        self.detalle = detalle
        self.imagenesgaleria = imagenesgaleria


class Geometry(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Feature(object):
    def __init__(self, attributes, geometry):
        self.attributes = attributes
        self.geometry = geometry


class FieldAliases(object):
    def __init__(self, objectid, nombrevolc, alturasobr, latitud, longitud, url, actividad, imagen, imagenesgaleria):
        self.objectid = objectid
        self.nombrevolc = nombrevolc
        self.alturasobr = alturasobr
        self.latitud = latitud
        self.longitud = longitud
        self.url = url
        self.actividad = actividad
        self.imagen = imagen
        self.imagenesgaleria = imagenesgaleria



class Field(object):
    def __init__(self, name, type, alias, length):
        self.name = name
        self.type = type
        self.alias = alias
        self.length = length


class SpatialReference(object):
    def __init__(self, wkid, latest_wkid):
        self.wkid = wkid
        self.latest_wkid = latest_wkid


class FeatureService(object):
    def __init__(self, display_field_name, field_aliases, geometry_type, spatial_reference, fields, features):
        self.display_field_name = display_field_name
        self.field_aliases = field_aliases
        self.geometry_type = geometry_type
        self.spatial_reference = spatial_reference
        self.fields = fields
        self.features = features

field_aliases=FieldAliases("OBJECTID","NOMBREVOLC","ALTURASOBR", "LATITUD","LONGITUD","URL","ACTIVIDAD","IMAGEN","IMAGENESGALERIA")
spatialreference = SpatialReference(4686,4686)
fields=[
    Field("OBJECTID","esriFieldTypeOID","OBJECTID",""),
    Field("NOMBREVOLC","esriFieldTypeString","NOMBREVOLC",50),
    Field("ALTURASOBR","esriFieldTypeString","ALTURASOBR",""),
    Field("LATITUD","esriFieldTypeString","LATITUD",25),
    Field("LONGITUD","esriFieldTypeString","LONGITUD",25),
    Field("URL","esriFieldTypeString","URL",254),
    Field("ACTIVIDAD","esriFieldTypeString","ACTIVIDAD",254),
    Field("IMAGEN","esriFieldTypeString","IMAGEN",255),
    Field("DETALLE","esriFieldTypeString","DETALLE",255),
    Field("IMAGENESGALERIA","esriFieldTypeString","IMAGENESGALERIA",255),

]

all_volcanes = Volcanes.objects.all()

features=[]

for vol in all_volcanes:
    featAtributes=Attributes(vol.OBJECTID,vol.NOMBREVOLC,vol.ALTURASOBR,vol.LATITUD,vol.LONGITUD,vol.URL,vol.ACTIVIDAD,vol.IMAGEN,vol.DETALLE,vol.IMAGENESGALERIA)
    featGeometry=Geometry(float(vol.LONGITUD_DECIMALES),float(vol.LATITUD_DECIMALES))
    featVolcan= Feature(featAtributes,featGeometry)
    features.append(featVolcan)

featureServices=FeatureService("",field_aliases,"esriGeometryPoint",spatialreference,fields,features)

featureServicesJSON = jsonpickle.encode(featureServices,unpicklable=False)




####Vistas
class VolcanesList(ListView):
    model = Volcanes

class VolcanesDetail(DetailView):
    model = Volcanes

class VolcanesCreation(CreateView):
    model = Volcanes
    success_url = reverse_lazy('volcanes:list')
    fields = ['NOMBREVOLC', 'ALTURASOBR', 'LATITUD', 'LONGITUD', 'URL', 'ACTIVIDAD', 'IMAGEN', 'DETALLE', 'IMAGENESGALERIA', 'LONGITUD_DECIMALES', 'LATITUD_DECIMALES']


class VolcanesUpdate(UpdateView):
    model = Volcanes
    success_url = reverse_lazy('volcanes:list')
    fields = ['NOMBREVOLC', 'ALTURASOBR', 'LATITUD', 'LONGITUD', 'URL', 'ACTIVIDAD', 'IMAGEN', 'DETALLE', 'IMAGENESGALERIA', 'LONGITUD_DECIMALES', 'LATITUD_DECIMALES']


class VolcanesDelete(DeleteView):
    model = Volcanes
    success_url = reverse_lazy('volcanes:list')

# Create your views here.

# Create your views here.
class Login(FormView):
    # Establecemos la plantilla a utilizar
    template_name = 'login.html'
    # Le indicamos que el formulario a utilizar es el formulario de autenticación de Django
    form_class = AuthenticationForm
    # Le decimos que cuando se haya completado exitosamente la operación nos redireccione a la url bienvenida de la aplicación personas
    success_url = reverse_lazy('volcanes:list')

    def dispatch(self, request, *args, **kwargs):
        # Si el usuario está autenticado entonces nos direcciona a la url establecida en success_url
        if request.user.is_authenticated():
            return HttpResponseRedirect(self.get_success_url())
        # Sino lo está entonces nos muestra la plantilla del login simplemente
        else:
            return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(Login, self).form_valid(form)

def send_json(request):
    d =json.loads(featureServicesJSON)
    return JsonResponse(d, safe=False,)