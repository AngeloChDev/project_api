from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Users(AbstractUser):
      name = models.CharField(blank=False, max_length=50)
      pasword = models.CharField(blank=False, max_length=50)