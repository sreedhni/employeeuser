
from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Employee

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","password"]
        def create(self,validated_data):
            return User.objects.create_user(**validated_data)

class EmployeeSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Employee
        fields="__all__"