from django.shortcuts import render
from .models import Autos
from django.urls import reverse
from django.http import HttpResponse
import requests



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

    if response.status_code == 200:
        try:
            
            autos_data = response.json()
            context = {
                'autos': autos_data,  # Pass the fetched data to the template
            }
            return render(request, 'cars.html', context)
        except ValueError:
            error_message = "API is not in the correct format"
            return render(request, 'error.html', {'error_message': error_message})
    else:
        return HttpResponse("Failed to fetch car data from the API")
    
def cardetails(request, auto_pk):
    auto_pk_int = int(auto_pk)
    api_url = f'http://127.0.0.1:5000/cars/{auto_pk}/'  
    response = requests.get(api_url)

    if response.status_code == 200:
        auto_details = response.json()
        context = {
            'auto_details': auto_details,
        }
        return render(request, 'auto_details.html', context)
    elif response.status_code == 404:
        return HttpResponse("Auto details not found")
    else:
        return HttpResponse("Failed to fetch auto details from the API")

def order_success(request):
    return render(request, 'order_success.html')
