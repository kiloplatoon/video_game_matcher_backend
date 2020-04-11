from django.db import models
from accounts.models import User

class User(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE),
    profile_picture = models.ImageField(default='default.jpg', upload_to='profile'),
    models.TextField(max_length=500),
    dob = models.DateField(max_length=8),
    casual_competitive = models.BooleanField(null=True)
    


    def __str__(self):
        return self.username




