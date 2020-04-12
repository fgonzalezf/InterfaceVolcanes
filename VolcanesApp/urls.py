from django.conf.urls import url
from django.contrib.auth.views import logout
from .views import   (
    VolcanesList,
    VolcanesDetail,
    VolcanesCreation,
    VolcanesUpdate,
    VolcanesDelete,
    Login,
    send_json
)
from django.contrib.auth.decorators import  login_required


urlpatterns = [


    url(r'^$', VolcanesList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', login_required(VolcanesDetail.as_view()), name='detail'),
    url(r'^nuevo$', login_required(VolcanesCreation.as_view()), name='new'),
    url(r'^editar/(?P<pk>\d+)$', login_required(VolcanesUpdate.as_view()), name='edit'),
    url(r'^borrar/(?P<pk>\d+)$', login_required(VolcanesDelete.as_view()), name='delete'),
    url(r'^login$', Login.as_view(),name='login'),
    url(r'^logout$', logout ,name='logout',kwargs={'next_page': '/volcanes/'}),
    url(r'^Volcanesjson$', send_json ,name='json'),


]