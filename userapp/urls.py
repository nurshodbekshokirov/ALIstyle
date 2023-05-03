from django.urls import path
from .views import *
urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profil'),
    path('address/', ProfileadresView.as_view(), name='address'),
    path('add/', AddressPost.as_view())



]