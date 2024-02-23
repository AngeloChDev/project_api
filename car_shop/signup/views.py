from django.shortcuts import render, redirect
from .models import Users
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.contrib.auth import logout as auth_logout
from django.urls import reverse_lazy
from django.views.generic.base import RedirectView



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cars:cars_homepage') 
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {'form': form})


def thankyou(request):
    return render(request, "thankyou.html")


class CustomLogoutView(RedirectView):
    url = reverse_lazy('signup:thankyou')  # Redirect to 'thankyou' URL after logout

    def dispatch(self, request, *args, **kwargs):
        auth_logout(request)
        return super().dispatch(request, *args, **kwargs)
