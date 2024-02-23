from django.urls import path, include
from .views import AutoShop, loadauto,Login,AutoData
from .view2 import AutosListApi
app_name = "mainAPI"

urlpatterns = [
    path("", AutoShop.as_view(), name= "shop_page"),
    path("ShopPage/", AutoShop.as_view(), name= "shop_page"),
    path("ShopPage/autodata/<auto_id>", AutoData.as_view(), name= "autodata_page"),
    path("api/", AutosListApi.as_view()),
    path("login/", Login.as_view(), name= "login_page"),
    path("loadauto/", loadauto),
    
]