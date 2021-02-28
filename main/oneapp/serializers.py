from rest_framework import serializers
from .models import Crudex


class CrudexCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crudex
        fields = '__all__'


class CrudexReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crudex
        fields = ('id', 'username', 'first_name', 'last_name', 'is_active')