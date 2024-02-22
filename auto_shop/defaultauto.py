from random import randint,choice
from .models import Autos
from collections import Counter
from datetime import datetime
brands = ["Audi", "BMW", "Mercedes", "Fiat", "Alfaromeo", "Subaru"]

def defaultload():
      for n in range(35):
            auto = {"brand": choice(brands), 
                  "inmatricolation":datetime(randint(2000 ,2024),randint(1, 12),1),#.strptime("%Y/%m"),
                  "price":randint(30000,60000),
                  }
            A=Autos.objects.create(**auto)
            A.save()
