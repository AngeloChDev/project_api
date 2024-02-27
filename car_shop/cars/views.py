from django.shortcuts import render
from .models import Autos
from django.urls import reverse
from django.http import HttpResponse
import requests
import json



def cars_homepage(request):
    url_cars = reverse("cars:cars")
    url_signup = reverse("signup:signup")
    context = {
        'url_cars': url_cars,
        'url_signup': url_signup,
    }
    return render(request, 'shop.html', context)


def cars(request):
    api_url = 'http://127.0.0.1:5000/'  
    response = requests.get(api_url)
    
    print(response.json())
    return render(request, 'cars.html', {'autos':json.loads(response.json())})
   
    
def cardetails(request, auto_id):
    # auto_pk_int = int(auto_pk)
    api_url = f'http://127.0.0.1:5000/cars/{str(auto_id)}/'  
    response = requests.get(api_url)
    return render(request, 'cardetails.html', {'car':json.loads(response.json())})
  

def order_success(request):
    return render(request, 'order_success.html')
