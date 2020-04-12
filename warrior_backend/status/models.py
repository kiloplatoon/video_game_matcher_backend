from django.db import models
from accounts.models import User

class Status(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    status = models.TextField(max_length=400, default = '', blank = True)
