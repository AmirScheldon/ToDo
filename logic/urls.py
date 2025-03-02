from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home-page'),
    path('tasks/', views.ListTaskView.as_view(), name='all-tasks-page'),
    path('create-task/', views.CreateTaskView.as_view(), name='create-task-page'),
    path('update-task/<int:pk>', views.UpdateTaskView.as_view(), name='update-task-page'),
    path('delete-task/<int:pk>', views.DeleteTaskView.as_view(), name='delete-task-page'),
]