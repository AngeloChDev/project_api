from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator 
from datetime import datetime
# Create your models here.



class User(AbstractUser):
      age = models.IntegerField(blank=False,null=True,  validators=[MinValueValidator(18), MaxValueValidator(90)])
      

# Create your models here.
class Autos(models.Model):
      brand = models.CharField(max_length=50, blank=False)
      inmatricolation = models.DateField( help_text="Date as 'Year/month'")
      price = models.FloatField(blank=False)
      quantity = models.IntegerField(null=True)
      selled = models.IntegerField(null=True)
      disponible = models.BooleanField(default=True)

      
      @property
      def ages(self):
            start =  datetime.strptime(self.inmatricolation.strftime('%Y/%m'), '%Y/%m')
            today_year = datetime.strptime(datetime.now().strftime('%Y/%m'), '%Y/%m')
            days_old = today_year - start
            years = days_old.days / 365
            return round(years, 1)
      
      def __str__(self):
            details = f"Model: {self.brand}\nFirst inmatricolation: {self.inmatricolation}\n Auto years: {self.ages}\nPrice: {self.price}$"
            return details