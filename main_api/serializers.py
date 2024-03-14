from rest_framework import serializers
from .models import GuestUser
from django.contrib.auth import get_user_model

class GuestUserSerializer(serializers.ModelSerializer):
      class Meta:
            model= get_user_model()
            fields = ["id","username"]
      
      def get_user(self, data):
            user=self.Meta.model.objects.filter(username=data["username"]).first() if True else None
            try:
                  if user :
                        if user.password == data["password"] or user.check_password(data["password"]):
                              return True
                        raise Exception('Not valid password')
                  raise Exception('Not valid user details, probably username')
            except Exception as e:
                  print(e)
                  return False

class CarSerializer(serializers.ModelSerializer):
      class Meta:
            model= "Car"
            fields = "__all__"