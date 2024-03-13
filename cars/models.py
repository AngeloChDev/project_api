from django.db import models

from datetime import datetime, date
# Create your models here.
class Car(models.Model):
      brand = models.CharField(max_length=50, blank=False)
      inmatricolation = models.DateField(null=True,blank=False)
      price = models.FloatField(blank=False)
      disponible = models.BooleanField(default=True,editable=False,auto_created=True)

      
      @property
      def ages(self):
            if self.inmatricolation is None:
                  return int(0)
            today_year =  date.today()
            old = today_year.year - self.inmatricolation.year

            return old
      
      def __str__(self):
            details = f"Model: {self.brand} First inmatricolation: {self.inmatricolation} Auto years: {self.ages} Price: {self.price}$"
            return details
      

class Order(models.Model):
      id_car= models.IntegerField()
      id_user= models.IntegerField()
      completed=models.BooleanField(default=False,editable=False,auto_created=True)