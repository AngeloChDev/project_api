from django.urls import path,include 
from .views import GenericUsersViewSet
from rest_framework.routers import SimpleRouter,Route
from cars.views import  CarViewSet, concludeOrder
route = SimpleRouter()
route.register(r"", CarViewSet ,basename="cars")

route_user = SimpleRouter()
route_user.register("", GenericUsersViewSet ,basename="user")

urlpatterns = [
    
  path('<username>/<password>/signup/',GenericUsersViewSet.as_view({"post":"create"})),                #url to sigup only post request or will return an error 404 / username has baan unique
  path('<username>/<password>/login/', GenericUsersViewSet.as_view({"get":"retrieve"})),                 ##url to login only get request to return status code 200 plus user details or return an error 404
  path('<username>/<password>/<key>-<val>/update/', GenericUsersViewSet.as_view({"post":"update"})),    #url post request # key value separed from a dash - # will update the key with the value gived to the user correspond login details 
  path('<username>/<password>/<to_delete>/delete/', GenericUsersViewSet.as_view({"get":"delete"})),     # url get request return true or 404, only admin allowed to delete an or multiple users # values gived in string of single number or multiple number separates with the simbol '&'
  path('<username>/<password>/listusers/',GenericUsersViewSet.as_view({"get":"list"})),                 #url to list all users displayed only id and username, only admin allowed
  path('<username>/<password>/login/<pk>/concludeorder/',concludeOrder,name='conclude_order'),           #url to conclude the order conrispondent to the primary key only admi allowed 
  path('<username>/<password>/login/<brand>/<date>/<price>/<ages>/', include(route.urls)),               # connect with the cars view set depend the scope this detail will be required or not considered. But required as url path like 0 or any 
  path('<username>/<password>/signup/<brand>/<date>/<price>/<ages>/', include(route.urls)),              # same previous


]



