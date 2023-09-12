from django.urls import path

from . import views

urlpatterns = [
    path('', views.SaidasView.as_view(), name='saidas'),
    path('destinacao', views.DestinacaoView.as_view(), name='destinacao'),
]