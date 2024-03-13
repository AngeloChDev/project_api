
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import  MinLengthValidator, MaxLengthValidator
from typing import Self


class GuestUser(AbstractUser):
      __pas=""
      username = models.CharField(max_length=50, blank=False, unique=True)
      password = models.CharField(max_length=30, blank=False, validators=[MinLengthValidator(8), MaxLengthValidator(30)])
      
      def __str__(self) -> str:
            return f"{self.username}"
      



