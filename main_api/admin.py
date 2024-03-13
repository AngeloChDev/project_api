from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import GuestUserForm  , AdminForm
from .models import GuestUser 


class CustomAdmin(UserAdmin):
      add_form = GuestUserForm
      form = AdminForm
      model = GuestUser
      list_display = [
            "username",
            "email",
            "is_staff",
      ]
      #fieldsets = UserAdmin.fieldsets + ((None, {"fields":("username","password") }),)
      add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("email","is_staff")}),)
admin.site.register(GuestUser,CustomAdmin)





#admin.site.register(GuestUser)
