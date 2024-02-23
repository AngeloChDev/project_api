from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class ClientUsersCreationForm(UserCreationForm):
      class Meta:
            model = User
            fields = UserCreationForm.Meta.fields + ("age",)


class AdminUsersChangeForm(UserChangeForm):
      class Meta:
            model = User
            fields = UserChangeForm.Meta.fields