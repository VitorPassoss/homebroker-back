from django.urls import path

from . import views

urlpatterns = [
    path('', views.Saidas.as_view(), name='saidas'),
    path('destinacao', views.Destinacao.as_view(), name='destinacao'),
]