from django.urls import path
from .views import  CarViewSet, loadauto, CarShopView

urlpatterns = [
      
      path('', CarShopView.as_view(), name="shop"),       # primary main empty url return a list with all cars
      path('shop/', CarShopView.as_view(), name="shop"),    # secondary url return a list with all cars
      path('carsshop/',CarViewSet.as_view({"get":"carsshop"})), # list cars in api links return lis cars login trequired
      path('search/',CarViewSet.as_view({"get":"search"})),      # url all users return a list of cars which has some value conrensponding to one or more the values passed
      path('addnewcar/',CarViewSet.as_view({"post":"addnewcar"})),      # url to add a new car brand and date are required only admin allowed
      path('<pk>/',CarViewSet.as_view({"post":"buy"})),           # url buy a car login and car primary key are required
      path('<pk>/',CarViewSet.as_view({"post":"deletecar"})),     #url method get return 404 # method post delete a car only admin allowed primary key car required return details of the deleted car
      path('<pk>/',CarViewSet.as_view({"patch":"editcar"})),      # urlmethod patch to edit a car, selecr car with primarykey gived and pass gived details as new if not 0 
      path('defaultAuto/', loadauto,name = "loaddefault_page"), # load 35 random cars in database 

]