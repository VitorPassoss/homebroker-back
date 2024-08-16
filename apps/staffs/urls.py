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
 path('fechamentos', views.FechamentosView.as_view(), name='fechamentos'),
 re_path(r'^fechamentos/(?P<id>\d+)?$', views.FechamentosView.as_view(), name='fechamentos-item'),
 path('wallet', views.WalletByPersonId.as_view(), name='wallet'),
 re_path(r'^wallet/(?P<id>\d+)?$', views.WalletByPersonId.as_view(), name='wallet-item'),
  path('person', views.PersonView.as_view(), name='person'),
 re_path(r'^person/(?P<id>\d+)?$', views.PersonView.as_view(), name='person-item'),
 ]
