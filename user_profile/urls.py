from . import views
from django.urls import path
from .views import ProfileView
from django.views.generic import TemplateView


urlpatterns = [
    path('profile', ProfileView.as_view(), name='profile-page'),
    path('profile/update', TemplateView.as_view(template_name='user_profile/profile-update-page.html'), name='update-profile-page'),
    
    # path('profile/update', views.UpdateProfileView.as_view(), name='update-profile-page'),
]
