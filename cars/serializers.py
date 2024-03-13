

from rest_framework import serializers
from .models import  Car, Order
from django.conf import settings
from django.contrib.auth import get_user_model





class CarSerializer(serializers.ModelSerializer):

      class Meta:
            model= Car
            fields =[
                  "id",
                  "brand",
                  "inmatricolation",
                  "price",
            ]
            extra_kwargs = {'inmatricolation': {'input_formats': settings.DATE_INPUT_FORMATS}}


class OrderSerializer(serializers.ModelSerializer):
      class Meta:
            model = Order
            fields =[
                  "id",
                  "id_car",
                  "id_user",
            ]

      #def __init__(self, instance=None, data=..., **kwargs):
      #      super().__init__(instance, data, **kwargs)
#
      #def is_valid(self):
      #      if zip("id_car" , "id_user") in self.data.keys():
      #            if Car.objects.get(pk=self.data["id_car"]):
      #                  users=  get_user_model()
      #                  user= users.filter(pk= self.data["id_user"])
      #                  if user.is_authenticated and users.is_active:
      #                        return True
      #      return False