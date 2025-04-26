from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Quote(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quotes')