from django.db import models
from django.contrib.auth.models import AbstractUser


# Combined Custom_User Class for both Customer and Manager
class Custom_User_Model(AbstractUser):
    user_type = models.CharField(max_length=10)
    gender = models.CharField(max_length=100)
    dob = models.DateTimeField(auto_now=True)
    contact_no = models.IntegerField(default=0000000000)
    address = models.TextField()
    def __str__(self):
        return self.username
