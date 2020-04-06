from django.conf.urls import url

from .views import   (
    VolcanesList,
    VolcanesDetail,
    VolcanesCreation,
    VolcanesUpdate,
    VolcanesDelete
)



urlpatterns = [


    url(r'^$', VolcanesList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', VolcanesDetail.as_view(), name='detail'),
    url(r'^nuevo$', VolcanesCreation.as_view(), name='new'),
    url(r'^editar/(?P<pk>\d+)$', VolcanesUpdate.as_view(), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', VolcanesDelete.as_view(), name='delete'),
]