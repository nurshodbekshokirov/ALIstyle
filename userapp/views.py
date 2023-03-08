from django.shortcuts import render,redirect
from django.views import View
from .models import *


# Create your views here.
class Registerview(View):
    def get(self, request):
        return render(request,'page-user-register.html')
    def post(self,request):
        if request.POST.get('p') == request.POST.get('p2'):

            user = User.objects.create_user(
                username = request.POST.get('email'),
                password = request.POST.get('p')
            )



            Profil.objects.create(
                ism = request.POST.get('i') + ' ' + request.POST.get('f'),
                jins = request.POST.get('e'),
                shahar = request.POST.get('sh'),
                davlat = request.POST.get('d'),
                user = user
            )
            return redirect('/')

