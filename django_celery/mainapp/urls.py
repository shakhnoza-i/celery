from django.urls import path, include
from mainapp.views import test

urlpatterns = [
    path('', test, name='test'),
]