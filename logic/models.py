from django.db import models
from django.contrib.auth.models import User


user = User()


class Task(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    is_done = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title