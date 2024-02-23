from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Users


class ClientUsersCreationForm(UserCreationForm):
      class Meta:
            model = Users
            fields = UserCreationForm.Meta.fields + ("name", "pasword",)


class AdminUsersChangeForm(UserChangeForm):
      class Meta:
            model = Users
            fields = UserChangeForm.Meta.fields