from django.db import models
from datetime import datetime


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
            today_year = datetime.strptime(datetime.now().strftime('%Y/%m'), '%Y/%m')
            days_old = today_year - self.inmatricolation
            years = days_old.days / 365
            return round(years, 1)
      
      def __str__(self):
            details = f"Model: {self.model}\nFirst inmatricolation: {self.inmatricolation}\Auto years: {self.ages}\Price: {self.price}$"
            return details