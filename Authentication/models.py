from django.db import models
from django.contrib.auth.models import AbstractUser


# Combined Custom_User Class for both Customer and Manager
class Custom_User_Model(AbstractUser):
    user_position=models.CharField(max_length=10)
    contact_no=models.IntegerField(default=True)
    def __str__(self):
        return self.username
