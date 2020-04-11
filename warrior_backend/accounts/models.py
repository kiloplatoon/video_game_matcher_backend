from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE),
    profile_picture = models.ImageField(upload_to ='uploads/',
    bio = models.TextField(),
    dob = models.DateField(),
    casual_competitive = models.BooleanField(null=True)
   


