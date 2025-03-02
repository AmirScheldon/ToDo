from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import View
from common.models import ProfilePicture

class ProfileView(View):
    def get(self, request):
        
        user = User.objects.get(id=request.user.id)
        profile_picture, created = ProfilePicture.objects.get_or_create(user=request.user)

        
        context = {
            'user': user,
            'picture': profile_picture
        }
        
        return render(request, 'user_profile/profile-page.html', context)
        
