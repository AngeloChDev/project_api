
from django.contrib import admin
from django.urls import path, include
from cars.views import CarShopView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", CarShopView.as_view(),name="shop"),            #main intial link return a list of all cars
    path("api/", include("main_api.urls")),                 #connect the users view set
    path("api-auth/", include("rest_framework.urls")),
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    
] 
