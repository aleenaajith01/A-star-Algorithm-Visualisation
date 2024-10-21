# grid/urls.py
from django.urls import path
from .views import my_path
from .views import design

urlpatterns = [
    path('', design, name='design'),
    path('my_path/', my_path, name='my_path'),
]
