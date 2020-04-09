from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email

class Profile(AbstractUser):
    profile_picture = models.ImageField(('profile_picture'),
    bio = models.CharField(blank=True, null=True, max_length=250),
    user = models.ForeignKey(User, on_delete=models.CASCADE),
    dob = models.DateField(max_length=8),
    relationship = models.ForeignKey(Relationship, on_delete=models.CASCADE)
    


    def __str__(self):
        return self.user.username




