"""
Definition of models.
"""

from django.db import models

# Create your models here.

class User(models.Model):
    Name =models.CharField(max_length=100)
    Email =models.CharField(max_length=100)
    Subject =models.CharField(max_length=250)
    Message =models.CharField(max_length=2000)
    Time=models.DateField()