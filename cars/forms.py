
from .models import Car
from django.db import models
from django.forms import DateInput, NumberInput, CharField, ModelForm,BooleanField,NullBooleanSelect

class CarForm(ModelForm):
      class Meta:
            model=Car
            fields="__all__"
            
