from django.shortcuts import render
from rest_framework import generics

from .models import *
from .serializers import *


class EmployeeAPIList(generics.ListCreateAPIView):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
