from . import views
from django.urls import path
from .views import ProfileView, UpdateProfileView
from django.views.generic import TemplateView


urlpatterns = [
    path('profile', ProfileView.as_view(), name='profile-page'),
    path('profile/update', UpdateProfileView.as_view(), name='update-profile-page'),
    
    
    # path('profile/update', views.UpdateProfileView.as_view(), name='update-profile-page'),
]
