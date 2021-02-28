from django.shortcuts import render
from rest_framework import generics
from .serializers import CrudexSerializer

class CrudexCreate(generics.CreateAPIView):
    serializer_class = CrudexSerializer
