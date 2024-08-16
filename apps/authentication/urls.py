from django.urls import path
from apps.authentication.services.auth_token import CustomTokenObtainPairView
from . import views

urlpatterns = [
    path("login/", CustomTokenObtainPairView.as_view(),name="login-v1"),
    path('register/', views.UserCreateView.as_view(), name='user-create'),
]
