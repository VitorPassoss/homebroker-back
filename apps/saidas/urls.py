from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.SaidasView.as_view(), name='saidas'),
    path('destinacao', views.DestinacaoView.as_view(), name='destinacao'),
    re_path(r'^destinacao/(?P<id>\d+)?$', views.DestinacaoView.as_view(), name='destinacao'),

]