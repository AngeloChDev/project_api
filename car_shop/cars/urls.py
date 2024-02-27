from django.urls import path
from .views import cars, cardetails, cars_homepage, order_success
app_name="cars"

urlpatterns = [
    path("home/", cars_homepage, name="cars_homepage"),
    path("cars/", cars, name="cars"),
    path("cars/<int:auto_id>/", cardetails, name="cardetails"),
    path('order-success/', order_success, name='order_success'),
    ]
