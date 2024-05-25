from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self) -> str:
        return self.name

class Blog(models.Model):
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Set a default value for the user field
    title = models.TextField(max_length=100, blank=False, null=False)
    image = models.ImageField(blank=False, null=False)
    description = models.TextField(max_length=10000, blank=False, null=False)
    created_by = models.CharField(max_length=100, null=False, default=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self) -> str:
        return self.description
    
class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, default=1)
    blog = models.ForeignKey(Blog, blank=True, null=True, on_delete=models.SET_NULL)    
    comment = models.TextField(max_length=500, null=False, blank=False, default='no comments')
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    created_by = models.CharField(max_length=100, null=False, default=False)

    def __str__(self) -> str:
        return self.comment