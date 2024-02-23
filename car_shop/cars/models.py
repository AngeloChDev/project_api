from django.db import models
from django.contrib.auth.models import User

class Autos(models.Model):
      brand = models.CharField(max_length=50, blank=False)
      inmatricolation = models.DateField( help_text="Date as 'Year/month'")
      price = models.FloatField(blank=False)
      quantity = models.IntegerField(null=True)
      selled = models.IntegerField(null=True)
      disponible = models.BooleanField(default=True)

# class Car(models.Model):
#     manufacturer = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#     year = models.IntegerField()
#     color = models.CharField(max_length=50)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     mileage = models.DecimalField(max_digits=10, decimal_places=2)
#     image = models.ImageField(upload_to='car_images/')
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.manufacturer} {self.model} ({self.year}) - {self.color}"

# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     car = models.ForeignKey(Autos, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
#     order_date = models.DateTimeField(auto_now_add=True)

#     def total_price(self):
#         return self.quantity * self.item.price
