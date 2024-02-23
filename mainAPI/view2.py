from rest_framework import generics, permissions
from .models import Autos
from .serializers import AutosSerializer, UserSerializer
from .permissions import IsAdminPermissions

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from rest_framework.views import APIView
from rest_framework import viewsets, status
from django.contrib.auth import get_user_model



#class AutoList(APIView):
#    permission_classes = (permissions.IsAdminUser,)
#    queryset = Autos.objects.all()
#    serializer_class = AutosSerializer
#
#    
#class UserViewSet(viewsets.ModelViewSet):
#    permission_classes = [permissions.IsAdminUser]
#    queryset = get_user_model().objects.all()
#    serializer_class = UserSerializer
    

class AutosListApi(APIView):
    permission_classes = (IsAdminPermissions,)  # authenticated user can see only their own entries, no other entries
    @staticmethod
    def get(request):
        autos=Autos.objects.all()
        serializer=AutosSerializer#(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @staticmethod
    def post(request, *args,**kwargs):
        
        data={
            'brend': request.get("brend"),
            'inmatricolation': request.get('inmatricolation'),
            'price': request.get('price'),
            }
        serializer=AutosSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response("Data Saved", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

