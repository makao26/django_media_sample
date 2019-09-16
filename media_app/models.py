from django.db import models
#from django.contrib.auth.models import User
#from django.contrib.auth.models import AbstractUser
from accounts.models import CustomUser

class Document(models.Model):
    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    title = models.CharField(max_length=255,blank=True)
    description = models.TextField(max_length=1000,blank=True)
    photo = models.ImageField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
