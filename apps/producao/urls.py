from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^(?P<id>\d+)?$', views.ProducaoView.as_view(), name='producao'),
    path('produtos', views.ProdutosView.as_view(), name='produtos'),
    re_path(r'^produtos/(?P<id>\d+)?$', views.ProdutosView.as_view(), name='produtos'),
    path('estoque', views.ProdutoEstoqueView.as_view(), name='produto-estoque'),

]