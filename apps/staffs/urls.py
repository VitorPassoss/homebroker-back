from django.urls import path, re_path
from . import views

urlpatterns = [
 path('control', views.ProfissionaisView.as_view(), name='staffs'),
 re_path(r'^control/(?P<id>\d+)?$', views.ProfissionaisView.as_view(), name='staff-item'),
 path('empresas', views.EmpresaView.as_view(), name='empresas'),  
 path('status', views.StatusView.as_view(), name='status'),  
 path('cargos', views.CargoView.as_view(), name='cargos'),  
 path('turnos', views.TurnosView.as_view(), name='turnos'), 
 path('search', views.SearchView.as_view(), name='search'),

 ]
