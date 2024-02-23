from django.urls import path, include
from .views import AutoShop, loadauto,Login


app_name = "auto_shop"

urlpatterns = [
    path("", AutoShop.as_view(), name= "shop_page"),
    path("ShopPage/", AutoShop.as_view(), name= "shop_page"),
    path("login/", Login.as_view(), name= "login_page"),
    path("loadauto/", loadauto)

]