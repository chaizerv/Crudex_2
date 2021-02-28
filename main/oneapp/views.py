from django.shortcuts import render
from rest_framework import generics
from .serializers import CrudexCreateSerializer, CrudexReadSerializer
from .models import Crudex

class CrudexCreate(generics.CreateAPIView):
    serializer_class = CrudexCreateSerializer


class CrudexRead(generics.ListAPIView):
    serializer_class = CrudexReadSerializer
    queryset = Crudex.objects.all()


class CrudexUpdate(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CrudexCreateSerializer
    queryset = Crudex.objects.all()
