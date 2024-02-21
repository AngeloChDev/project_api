from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import ClientUsersCreationForm, AdminUsersChangeForm
from .models import Users


class AdminUsers(UserAdmin):
      add_form = ClientUsersCreationForm
      form = AdminUsersChangeForm
      model = Users
      list_display = [
            "email",
            "username",
            "name",
            "pasword",
            "is_staff",
      ]
      fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("name", )}),)
      add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("name",)}),)


admin.site.register(Users, AdminUsers)