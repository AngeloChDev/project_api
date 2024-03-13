from django.urls import path,include , re_path
from rest_framework.urlpatterns import  format_suffix_patterns
from .views import UserView, LoginView, GenericUsersViewSet #, loadauto #, CarShopView
from rest_framework.routers import SimpleRouter,Route
from cars.views import  CarViewSet, CarShopView,concludeOrder
route = SimpleRouter()
route.register(r"", CarViewSet ,basename="cars")

route_user = SimpleRouter()
route_user.register("", GenericUsersViewSet ,basename="user")

urlpatterns = [
    
  path('<username>/<password>/signup/',GenericUsersViewSet.as_view({"post":"create"})),
  path('<username>/<password>/login/', GenericUsersViewSet.as_view({"get":"retrieve"})),
  path('<username>/<password>/<key>-<val>/update/', GenericUsersViewSet.as_view({"post":"update"})),
  path('<username>/<password>/<to_delete>/delete/', GenericUsersViewSet.as_view({"get":"delete"})),
  path('<username>/<password>/listusers/',GenericUsersViewSet.as_view({"get":"list"})),
  path('<username>/<password>/login/<pk>/concludeorder/',concludeOrder,name='conclude_order'),
  path('<username>/<password>/login/<brand>/<date>/<price>/<ages>/', include(route.urls)),


]



