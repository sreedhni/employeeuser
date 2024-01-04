
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from django.contrib.auth.models import User
from api.views import EmployeeView,UsercreationView
from rest_framework.authtoken.views import ObtainAuthToken

router=DefaultRouter()
router.register("employee",EmployeeView,basename="employee")

urlpatterns = [
    path("register/",UsercreationView.as_view(),name="register"),
    # path("token",ObtainAuthToken.as_view(),name="register")

]+router.urls
