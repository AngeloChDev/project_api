from random import randint,choice
from .models import Car
from datetime import datetime
brands = ["Audi", "BMW", "Mercedes", "Fiat", "Alfaromeo", "Subaru"]

def defaultload():
      have=Car.objects.all()
      if len(have)>30:
            return "Default cars has already loaded"
      for n in range(35):
            car = {"brand": choice(brands), 
                  "inmatricolation":datetime(randint(2000 ,2024),randint(1, 12),1),
                  "price":randint(30000,60000),
                  }
            C=Car.objects.create(**car)
            C.save()
      return True