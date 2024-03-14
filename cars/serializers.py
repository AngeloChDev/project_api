

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

  