from django.shortcuts import render
from rest_framework.reverse import reverse
from rest_framework.decorators import action, authentication_classes, permission_classes,api_view
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .load_auto import defaultload
from rest_framework.generics import ListAPIView 
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from .serializers import CarSerializer, Car, OrderSerializer, Order
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AND, SAFE_METHODS, IsAuthenticatedOrReadOnly, IsAdminUser,AllowAny
from rest_framework.status import HTTP_202_ACCEPTED,HTTP_404_NOT_FOUND,HTTP_201_CREATED,HTTP_200_OK,HTTP_401_UNAUTHORIZED,HTTP_400_BAD_REQUEST
from collections import Counter
from datetime import datetime
# Create your views here.

class CarShopView(ListAPIView):
      queryset = Car.objects.all()
      permission_classes = (AllowAny,)
      serializer_class = CarSerializer


def loadauto(request, *arg, **kwargs):
      defaultload()
      return HttpResponseRedirect('cars:shop')

@api_view(["GET"])
@permission_classes([IsAdminUser,])
def concludeOrder(request, pk,*arg, **kwargs):
      try:
            order= Order.objects.get(pk=int(pk))
            order.completed=True
            order.save()
            url=reverse('shop')
            return HttpResponseRedirect(url) 
      except Exception as e:
            return Response({"Error":f"{e}"},status=HTTP_400_BAD_REQUEST)


class CarViewSet(GenericViewSet):
      queryset = Car.objects.all()
      serializer_class = CarSerializer
      order_serializer = OrderSerializer

      @permission_classes(IsAuthenticated)
      @action(detail=False, methods=["GET"],url_path="carsshop")
      def carsshop(self,request, *args,**kwargs):
            try:
                  data=self.get_queryset()
                  s=self.serializer_class(data=data,many=True)
                  s.is_valid()
                  return Response(s.data, status=HTTP_200_OK )
            except Exception as e:
                  return Response({"Response":f"Error {e} \non load details"},status=HTTP_404_NOT_FOUND)

      @action(detail=False, methods=["GET"], url_path="search")
      def search(self,request,brand=None,date=None,price=None,ages=None,*args,**kwargs):
            cars = self.queryset
            try:
                  data=request.resolver_match.kwargs
                  items = list(data.items())
                  for item in items:
                        if item[0] in ('ages',"username","password","date") or item[1] in (None, "0"):
                              data.pop(item[0])
                  cars=cars.filter(**data)
                  min_age , max_age= (int(ages) - 1 if int(ages) - 1 >= 0 else 0), int(ages) + 1
                  print(type(min_age ), max_age)
                  if ages is not None:
                        cars = [car for car in cars if round(car.ages) in range(min_age,max_age)]
                  cars_json = self.serializer_class(cars,many=True)
                  return Response(cars_json.data, status=HTTP_200_OK)
            
            except Exception as e:
                  return Response({"Response":f"Error {e} \non load details"},status=HTTP_404_NOT_FOUND)

      @permission_classes([IsAdminUser,])
      @authentication_classes(SessionAuthentication)
      @action(detail=False, methods=["POST"],url_path="addnewcar")
      def addnewcar(self, request,brand,date=None, price=None, *args, **kwargs):
            try:
                  if request.user.is_authenticated:
                        data={"brand":brand,"inmatricolation":datetime.strptime(date, "%Y-%m-%d"),"price":int(price)}      
                        car=self.serializer_class(data=data)
                        car.is_valid()
                        new_car = self.serializer_class().create(data)
                        new_car.save()
                        return Response(car.data, status=HTTP_200_OK)
                  raise Exception("User not authenticated")
            except Exception as e:
                  return Response({"Response":f"Error {e} \non load details"},status=HTTP_404_NOT_FOUND)
            
      @permission_classes([IsAuthenticated,])
      @action(detail=True, methods=["POST"],url_path="buy")
      def buy(self, request, pk, *args,**kwargs):
            try:
                  if request.user.is_authenticated:
                        data={"id_car":int(pk),"id_user":int(self.request.user.id)}      
                        if self.order_serializer(data=data).is_valid():
                              recip = self.order_serializer(data=data)
                              recip.is_valid()
                              recip.save()
                              return Response(recip.data)
                        raise Exception('Data not valid for a new order')
                        
                  raise Exception("User not authenticated")
            except Exception as e:
                  return Response({"Erroe":f"{e}"},status=HTTP_400_BAD_REQUEST)


      @permission_classes([IsAdminUser,])
      @authentication_classes(SessionAuthentication)
      @action(detail=True, methods=["POST"],url_path="deletecar")
      def deletecar(self, request, pk,*args, **kwargs):
            try:
                  car = self.queryset.get(pk=int(pk))
                  data={"id":car.id, "brand":car.brand,"inmatricolation":car.inmatricolation,"price":car.price}
                  s=self.serializer_class(data=data)
                  s.is_valid()
                  car.delete()
                  return Response({"Car deleted":s.data},status=HTTP_200_OK)
            except Exception as e:
                  return Response({"Error":f"{e}"},status=HTTP_400_BAD_REQUEST)

      @permission_classes([IsAdminUser,])
      @authentication_classes(SessionAuthentication)
      @action(detail=True, methods=["PATCH"],url_path="editcar")
      def editcar(self, request, pk,*args, **kwargs):
            try:
                  data=request.resolver_match.kwargs
                  items = list(data.items())
                  for item in items:
                        if item[0] in ('ages',"username","password","date","pk") or item[1] in (None, "0"):
                              data.pop(item[0])
                  car=self.queryset.get(pk=int(pk))
                  for k,v in data.items():
                        car.__setattr__(k,v)
                  car.save()
                  return Response({f"Car id {pk} deleted":data},status=HTTP_200_OK)
            except Exception as e:
                  return Response({"Error":f"{e}"},status=HTTP_400_BAD_REQUEST)

