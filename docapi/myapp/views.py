from django.shortcuts import render
from rest_framework import viewsets

from .serializers import MedocSerializer
from .models import Medoc
# Create your views here.



class MedocViewSet(viewsets.ModelViewSet):
    queryset = Medoc.objects.all().order_by('product_name')
    serializer_class = MedocSerializer