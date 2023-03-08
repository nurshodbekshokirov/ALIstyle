
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from asosiy.views import Home2view
from asosiy.views import Loginview

urlpatterns = [
    path('admin/', admin.site.urls),

    path('asosiy/',include('asosiy.urls')),
    path('buyurtma/',include('buyurtma.urls')),
    path('user/',include('userapp.urls')),
    path('home/', Home2view.as_view(), name = 'home2'),
    path('',Loginview.as_view(),name='login')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
