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


class VolcanesList(ListView):
    model = Volcanes


class VolcanesDetail(DetailView):
    model = Volcanes

class VolcanesCreation(CreateView):
    model = Volcanes
    success_url = reverse_lazy('volcanes:list')
    fields = ['NOMBREVOLC', 'ALTURASOBR', 'LATITUD', 'LONGITUD', 'URL', 'ACTIVIDAD', 'IMAGEN', 'DETALLE', 'IMAGENESGALERIA']


class VolcanesUpdate(UpdateView):
    model = Volcanes
    success_url = reverse_lazy('volcanes:list')
    fields = ['NOMBREVOLC', 'ALTURASOBR', 'LATITUD', 'LONGITUD', 'URL', 'ACTIVIDAD', 'IMAGEN', 'DETALLE', 'IMAGENESGALERIA']


class VolcanesDelete(DeleteView):
    model = Volcanes
    success_url = reverse_lazy('volcanes:list')

# Create your views here.
