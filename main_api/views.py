from rest_framework import generics, permissions,viewsets
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import GuestUser
from .forms import GuestUserForm
from .serializers import GuestUserSerializer, CarSerializer
from django.http import HttpResponseRedirect, HttpResponse
from rest_framework.permissions import IsAuthenticated, AND, SAFE_METHODS, IsAuthenticatedOrReadOnly, IsAdminUser,AllowAny
from rest_framework.generics import RetrieveAPIView,GenericAPIView, ListAPIView,CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view, authentication_classes, permission_classes,action
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.response import Response
from rest_framework.status import HTTP_202_ACCEPTED,HTTP_404_NOT_FOUND,HTTP_201_CREATED,HTTP_200_OK,HTTP_401_UNAUTHORIZED,HTTP_400_BAD_REQUEST



class GenericUsersViewSet(ModelViewSet):
      queryset = GuestUser.objects.all()
      serializer_class = GuestUserSerializer

      @permission_classes(AllowAny)
      def create(self, request,*args, **kwargs):
            data=request.resolver_match.kwargs
            try:
                  k, s = data.keys(), self.serializer_class(data=data)
                  if all(("username" in k, "password" in k, s.is_valid() )) :
                        user=self.serializer_class().create(data)
                        user.save()
                        return Response({"Success":"New user created, please save your details","Detail":s.data},status=HTTP_201_CREATED)
                  raise ValueError("Url  didnot contain right data")
                        
            except ValueError as e:
                  return Response({"Response":{"message":f"Error {e} \non load details","data":data}},status=HTTP_401_UNAUTHORIZED) 

      @permission_classes(AllowAny)
      def retrieve(self, request, *args, **kwargs):
            data =request.resolver_match.kwargs
            try:
                  k, s = data.keys(), self.serializer_class(data=data)
                  s.is_valid()
                  if all(("username" in k, "password" in k, s.get_user(data))):
                        return Response(True,status=HTTP_202_ACCEPTED)  
                  raise Exception
            except Exception as e:
                  return Response({"Response":{"message":f"Error {e} \non load details","data":data}},status=HTTP_404_NOT_FOUND)
      
      @permission_classes(IsAuthenticated)
      @authentication_classes(SessionAuthentication)
      def update(self, request,*args, **kwargs):
            data =request.resolver_match.kwargs
            try:
            
                  k, s = data.keys(), self.serializer_class(data=data)
                  s.is_valid()
                  if all(("username" in k, "password" in k,"key" in k, "val" in k ,s.get_user(data))):
                        user =self.queryset.filter(username=data["username"]).first()
                        user.__setattr__(data["key"], data["val"])
                        user.save()
                        return Response({"Result":f"{data['key'].upper()} updated successfull"},status=HTTP_202_ACCEPTED)
                  
                  raise Exception
            except Exception as e:
                  return Response({"Response":{"message":f"Error {e} \non load details","data":data}},status=HTTP_404_NOT_FOUND)
      
      

      @permission_classes(IsAdminUser)
      @authentication_classes(SessionAuthentication)
      def delete(self, request,*args, **kwargs):
            data =request.resolver_match.kwargs
            to_delete=data["to_delete"]
            k, s = data.keys(), self.serializer_class(data=data)
            s.is_valid()
            l_todo=[]
            try:
                  if all(("username" in k, "password" in k,"to_delete" in k ,s.get_user(data))):
                        if to_delete.find("&"):
                              l_todo.extend(to_delete.split("&"))
                        elif int(to_delete):
                              l_todo.append(int(to_delete))
                        else:
                              raise Exception("Value selected for delete error")
                        res={'done':[], 'not':[]}
                        for todo in l_todo:
                              try:
                                    user_to_delete = self.queryset.filter(pk=int(todo))
                                    if user_to_delete.is_staff and not request.user.is_superuser:
                                          raise Exception('Only super user can deletea staff member')
                                    user_to_delete.delete()
                                    res["done"].append(todo)
                              except :
                                    res["not"].append(todo)
                                    pass
                  return Response({"Result":{"selected":f"Users selected {l_todo} ","deleted success":f"Usesrs with id {res['done']} deleted successfull","Errors":f"User not deleted for some error {res['not']}"}},status=HTTP_202_ACCEPTED)
            except Exception as e:  
                  return Response({"Response":{"message":f"Error {e} \non load details","data":data}},status=HTTP_404_NOT_FOUND)

      @permission_classes(IsAdminUser)
      @authentication_classes(SessionAuthentication)
      def list(self, request,username,password,*args,**kwargs):
            try:
                  all_users=self.serializer_class(data=self.queryset,many=True)
                  all_users.is_valid()
                  return Response(all_users.data,status=HTTP_202_ACCEPTED)
            except Exception as e:
                  return Response({"Response":{"message":f"Error {e} \non load details","data":None}},status=HTTP_404_NOT_FOUND)







