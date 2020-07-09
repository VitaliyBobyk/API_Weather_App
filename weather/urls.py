from django.contrib import admin
from django.urls import path
from .views import Test

urlpatterns = [
    path('', Test.as_view(), name='get_weather'),
]
