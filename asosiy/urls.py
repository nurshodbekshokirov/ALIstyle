from django.urls import path
from .views import *
urlpatterns = [
    path('home/', Homeview.as_view(), name='home'),


    path('logout/',Logoutview.as_view(), name='logout'),
    path('bolimlar/', Bolimlarview.as_view(), name='bolimlar'),
    path('bolimlar/<int:pk>/', Bolimview.as_view(), name='bolim'),
    path('mahsulot/<int:pk>/', Mahsulot_bitaview.as_view(), name='mahsulot')

]