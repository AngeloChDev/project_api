from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import ClientUsersCreationForm, AdminUsersChangeForm
from .models import User, Autos


class AdminUsers(UserAdmin):
      add_form = ClientUsersCreationForm
      form = AdminUsersChangeForm
      model = User
      list_display = [
            "email",
            "username",
            "password",
            "is_staff",
      ]
      fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("age", )}),)
      add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("age",)}),)


admin.site.register(User, AdminUsers)
admin.site.register(Autos)
