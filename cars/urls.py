from django.urls import path, re_path
from .views import  CarViewSet, loadauto, CarShopView, concludeOrder
from rest_framework.routers import SimpleRouter,Route
import json

urlpatterns = [
      
      path('', CarShopView.as_view(), name="shop"),
      path('shop/', CarShopView.as_view(), name="shop"),
      path('carsshop/',CarViewSet.as_view({"get":"shop"})),
      path('search/',CarViewSet.as_view({"get":"search"})),
      path('addnewcar/',CarViewSet.as_view({"post":"addnewcar"})),
      path('<pk>/',CarViewSet.as_view({"post":"buy"})),
      path('<pk>/',CarViewSet.as_view({"post":"deletecar"})),
      path('<pk>/',CarViewSet.as_view({"patch":"editcar"})),

      path('<pk>/confirmorder/', loadauto,name = "loaddefault_page"),
      path('defaultAuto/', loadauto,name = "loaddefault_page"),

]