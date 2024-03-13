

#login/<username>/<password>/
from django.contrib import admin
from django.urls import path, include
from cars.views import CarShopView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", CarShopView.as_view(),name="shop"),
    path("api/", include("main_api.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("dj-rest-auth/", include("dj_rest_auth.urls")),
    
] 
