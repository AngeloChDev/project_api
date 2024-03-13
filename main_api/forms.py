from django.contrib.auth.forms import  UserCreationForm, UserChangeForm
from .models import GuestUser

class GuestUserForm(UserCreationForm):
      class Meta:
            model = GuestUser
            fields=UserCreationForm.Meta.fields 


class AdminForm(UserChangeForm):
      class Meta:
            model = GuestUser
            fields=UserChangeForm.Meta.fields
      
      