from django.urls import path
from students.views import *

urlpatterns = [
    path('', index, name='index'),
]