from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout



class LoginView(View):
    def post(self, request):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')
        
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'invalid username')
            
            return redirect('login-page')
        
        user = authenticate(username=username, password=password)
        
        if user is None:
            messages.error(request, 'invalid password')
            
            return redirect('login-page')
        else:
            login(request, user) 
            
            return redirect('home-page')
        
    def get(self, request):
        return render(request, 'authentication/login-page.html')

                
class RegisterView(View):
    def post(self, request):
        first_name = self.request.POST.get('first_name')
        last_name = self.request.POST.get('last_name')
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')
        
        user = User.objects.filter(username=username)
        
        if user.exists():
            messages.error(request, 'An user with this username already exists!')
            return redirect('register-page')
        
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
        
        user.set_password(password)
        user.save()
        
        messages.info(request, 'Account created Successfully!')
        return render(request, 'authentication/login-page.html')
    
    
    def get(self, request):
        return render(request, 'authentication/register-page.html')
        

class LogoutView(View):
    def post(self, request):
        user = User.objects.filter(id=self.request.user.id)
        
        if user.exists():
            logout(request)
            messages.success(request, 'logout Successfully!')
            return render(request, 'authentication/first-page.html')
        
    def get(self, request):
        return render(request, 'authentication/logout-page.html')
            