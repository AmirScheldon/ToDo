from django.db import models
from django.contrib.auth.models import User


user = User()

class ProfilePicture(models.Model):
    user = models.OneToOneField(user, on_delete=models.CASCADE, primary_key=True, related_name='profile_picture')
    profile_picture = models.ImageField(upload_to='common/upload', blank=True, default='common/default/no-profile-picture.png')
    
    def __str__(self):
        return f'{self.user.username} profile picture'
