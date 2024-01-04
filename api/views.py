from django.shortcuts import render
from api.serializers import Userserializer,EmployeeSerializer
from api.models import Employee
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions,authentication

# Create your views here.
class UsercreationView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=Userserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class EmployeeView(ModelViewSet):
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=EmployeeSerializer
    queryset=Employee.objects.all()
    

