from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import View
from common.models import ProfilePicture
from .forms import EditProfilePictureForm, EditProfileUSerForm

class ProfileView(View):
    def get(self, request):
        
        user = User.objects.get(id=request.user.id)
        profile_picture= ProfilePicture.objects.filter(user=request.user).first()

        context={
            'user': user,
            'picture': profile_picture
        }

        return render(request, 'user_profile/profile-page.html', context)

        

class UpdateProfileView(View):
    def get(self, request):
        profile_picture, created = ProfilePicture.objects.get_or_create(user=request.user)
        
        user_update_form = EditProfileUSerForm(instance=request.user)
        profile_picture_update_form = EditProfilePictureForm(instance=profile_picture)
        
        return render(request, 'user_profile/profile-update-page.html', {'user_update_form': user_update_form, 'profile_picture_update_form': profile_picture_update_form})
        

    def post(self, request):
        user_update_form = EditProfileUSerForm(request.POST, instance=request.user)
        profile_picture_update_form = EditProfilePictureForm(request.POST, request.FILES, instance=request.user.profile_picture)
        
        
        if user_update_form.is_valid() and profile_picture_update_form.is_valid():
            user_update_form.save(commit=True)
            profile_picture_update_form.save(commit=True)
            
            return redirect(reverse_lazy('profile-page'))
            
        return render(request, 'user_profile/profile-update-page.html', {'user_update_form': user_update_form, 'profile_picture_update_form': profile_picture_update_form})
              