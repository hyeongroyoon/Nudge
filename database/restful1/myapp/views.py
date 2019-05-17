from django.shortcuts import render
from rest_framework import viewsets
from myapp.serializers import FoodSerializer
from myapp.models import *

# Create your views here.
class FoodViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = FoodSerializer
