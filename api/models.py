from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Employee(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

    
