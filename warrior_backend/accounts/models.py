from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    profile_picture = models.ImageField(upload_to ='uploads/', null = True, blank=True)
    bio = models.TextField(max_length=400, default = '', blank = True)
    dob = models.DateField(null = True, blank=True)
    casual_competitive = models.BooleanField(null=True, blank=True, default=False)
   
