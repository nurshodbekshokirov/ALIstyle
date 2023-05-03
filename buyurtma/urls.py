from django.urls import path
from .views import *
urlpatterns = [
    path('savat/', SavatView.as_view(), name='savat'),
    path('tanlangan/', TanlanganView.as_view(), name='tanlangan'),
    path('tanlangan/<int:pk>/', Tanlangan_qoshview.as_view(), name='tanlanganqosh'),
    path('savat/<int:pk>/', Savatqoshview.as_view(), name='tanlanganqosh'),
    path('', BuyurtmaView.as_view(), name = 'buyurtma' ),
    path('savat_q/<int:pk>/',Miqdorqoshishview.as_view()),
    path('savat_k/<int:pk>/',Miqdorkamview.as_view()),
    path('tanlangan_ochir/<int:pk>/', Tanlanganochirview.as_view()),
    path('savat_ochir/<int:pk>/', Savatochirview.as_view())

]