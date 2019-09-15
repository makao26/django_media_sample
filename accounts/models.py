from django.db import models

# Create your models here.
# accounts/models.py
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    def __str__(self):
        return self.email
