from django.urls import path
from . import views

urlpatterns = [
    path('', views.Producao.as_view(), name='producao'),
    path('<int:id>', views.Producao.as_view(), name='producao-item'),
    path('produtos', views.Produtos.as_view(), name='produtos'),
    path('produtos/<int:id>', views.Produtos.as_view(), name='produtos-item')
]