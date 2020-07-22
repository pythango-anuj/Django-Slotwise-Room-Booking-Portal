from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms

GENDER_CHOICES = (
    ('M','Male'),
    ('F','Female'),
    ('O','Other')
)

USER_CHOICES = (
    ('M','Manager'),
    ('C','Customer')
)

# Combined Custom_User Class for both Customer and Manager
class Custom_User_Model(AbstractUser):
    user_type = models.CharField(max_length=10,choices=USER_CHOICES)
    gender = models.CharField(choices=GENDER_CHOICES,max_length=100)
    dob = models.DateField(null=True)
    contact_no = models.IntegerField(default=0000000000)
    address = models.CharField(max_length=500)
    def __str__(self):
        return self.username
