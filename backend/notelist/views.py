from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ListSerializer
from .models import Notelist

# Create your views here.

class ListView(viewsets.ModelViewSet):
    serializer_class = ListSerializer
    queryset = Notelist.objects.all()
