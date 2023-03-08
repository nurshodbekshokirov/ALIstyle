from django.urls import path
from .views import *
urlpatterns = [

    path('register/', Registerview.as_view()),

]