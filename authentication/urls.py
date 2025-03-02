from . import views
from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='authentication/first-page.html'), name='first-page'),
    path('auth/register/', views.RegisterView.as_view(), name='register-page'),
    path('auth/login/', views.LoginView.as_view(), name='login-page'),
    path('auth/logout/', views.LogoutView.as_view(), name='logout-page'),
]
