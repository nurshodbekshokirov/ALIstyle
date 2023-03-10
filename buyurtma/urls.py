from django.urls import path
from .views import *
urlpatterns = [
    path('savat/', SavatView.as_view(), name='savat'),
    path('tanlangan/', TanlanganView.as_view(), name='tanlangan'),
    path('', BuyurtmaView.as_view(), name = 'buyurtma' ),
    path('savat_q/<int:pk>/',Miqdorqoshishview.as_view()),
    path('savat_k/<int:pk>/',Miqdorkamview.as_view()),
    path('tanlangan_ochir/<int:pk>/', Tanlanganochirview.as_view())

]