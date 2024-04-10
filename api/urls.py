from .views import *
from django.urls import path 

urlpatterns = [
    path('',RoomView.as_view()),
]