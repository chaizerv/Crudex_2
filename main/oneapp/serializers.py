from rest_framework import serializers
from .models import Crudex


class CrudexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crudex
        fields = '__all__'