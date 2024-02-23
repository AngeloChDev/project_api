from rest_framework import serializers
from .models import Autos
from django.contrib.auth import get_user_model



class AutosSerializer(serializers.ModelSerializer):
      class Meta:
            model=Autos
            fields = (
                  "id",
                  "brand",
                  "inmatricolation",
                  "price",
            )

class UserSerializer(serializers.ModelSerializer):
      class Meta:
            model=get_user_model()
            fields = (
                  "id",
                  "name",
            )