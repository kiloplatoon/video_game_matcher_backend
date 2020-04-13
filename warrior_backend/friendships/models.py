from django.db import models
from accounts.models import User
# class User(models.Model):
#     username = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)

class Relationship(models.Model):
    user_one = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_one')
    user_two = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_two')

    # Status Codes:
    # 0 = Pending
    # 1 = Accepted
    # 2 = Declined
    # 3 = Blocked
    status = models.SmallIntegerField()

    # id of user who has performed most recent status update
    action_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='action_user')
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user_one', 'user_two' ], name="unique_users")
        ]
 
    def __str__(self):
        return f'User1: {self.user_one}, User2: {self.user_two}   |  STATUS: {self.status}'
