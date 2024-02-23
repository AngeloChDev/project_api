from django.db import models

# Create your models here.

class Users(models.Model):
    first_name=models.CharField(max_length=20, primary_key=True)
    last_name=models.CharField(max_length=50)
    age=models.IntegerField(default=50)
    password=models.CharField(max_length=15)
    phone=models.IntegerField(null=True)
    email=models.EmailField(null=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


