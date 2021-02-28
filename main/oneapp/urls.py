from django.urls import path
from .views import CrudexCreate

urlpatterns = [
    path('create/', CrudexCreate.as_view()),
]
