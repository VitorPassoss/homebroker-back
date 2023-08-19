from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^(?P<id>\d+)?$', views.EntradasView.as_view(), name='entradas-item'),
    path('insumos', views.InsumosView.as_view(), name='insumos'),
    re_path(r'^insumos/(?P<id>\d+)?$', views.InsumosView.as_view(), name='insumos-item'),
    path('fornecedores', views.FornecedoresView.as_view(), name='fornecedores'),
    re_path(r'^fornecedores/(?P<id>\d+)?$', views.FornecedoresView.as_view(), name='fornecedores-item'),
    path('estoque', views.EstoqueView.as_view(), name='estoque'),
    re_path(r'^estoque/(?P<id>\d+)?$', views.EstoqueView.as_view(), name='estoque-item')
]
