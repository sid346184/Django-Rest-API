from django.shortcuts import render
from rest_framework import viewsets
from api.models import Company,Employee
from api.serializers import CompanySerializer, EmployeeSerializer


# Create your views here.

class CompanyView(viewsets.ModelViewSet):
    queryset= Company.objects.all()
    serializer_class=CompanySerializer

class EmployeeView(viewsets.ModelViewSet):
    queryset= Employee.objects.all()
    serializer_class=EmployeeSerializer
