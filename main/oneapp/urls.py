from django.urls import path
from .views import *

urlpatterns = [
    path('create/', CrudexCreate.as_view()),
    path('read/', CrudexRead.as_view()),
    path('update/<int:pk>/', CrudexUpdate.as_view()),
]
