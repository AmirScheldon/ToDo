from django import forms
from common.models import ProfilePicture
from django.contrib.auth.models import User


class EditProfilePictureForm(forms.ModelForm):
    class Meta:
        model = ProfilePicture
        fields = ['profile_picture']
   
class EditProfileUSerForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        