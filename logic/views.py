from django.shortcuts import render
from .models import Task, User
from django.views import View
from django.views.generic.list import ListView
from django.views.generic import  CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime



class HomeView(View):
    def get(self, request):
        context = User.objects.get(id=self.request.user.id)
        
        return render(request, 'todo/home-page.html', {'context': context})
    

class ListTaskView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "todo/all-tasks-page.html"
    context_object_name = 'tasks'
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user.id)

    
 
class CreateTaskView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "todo/create-task-page.html"
    fields = ['title', 'description']
    success_url = reverse_lazy('all-tasks-page')
    
    def form_valid(self, form):
        object_user = User.objects.get(id=self.request.user.id)
        form.instance.user = object_user
        
        form.save(commit=True)
        return super().form_valid(form)
    
    
class UpdateTaskView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "todo/update-task-page.html"
    fields = ['title', 'description', 'is_done']
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('all-tasks-page')
    
    def form_valid(self, form):
        updated_at = datetime.datetime.now(datetime.timezone.utc)
        form.instance.updated_at = updated_at
        return super().form_valid(form)
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user.id)

class DeleteTaskView(LoginRequiredMixin, DeleteView):
    redirect_unauthenticated_users = 'login-page'
    model = Task
    template_name = "todo/delete-task-page.html"
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('all-tasks-page')    
    context_object_name = 'task'
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user.id)
