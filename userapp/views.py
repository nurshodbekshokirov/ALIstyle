from django.shortcuts import render,redirect
from django.views import View
from .models import *
from buyurtma.models import Manzil
from .forms import *

from django.core.mail import send_mail
from django.conf import settings



# Create your views here.
class Registerview(View):
    def get(self, request):
        return render(request,'page-user-register.html')
    def post(self,request):
        if request.POST.get('p') == request.POST.get('p2'):
            # user_email = request.POST.get('email')

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
            # send_mail(
            #
            # subject = 'Xush kelibsiz',
            #
            # message = "Backend-11  jamoasining Alistyle nomli onlayn do'koniga xush kelibsiz !"
            #     "Maroqli xarid tilaymiz:)",
            #
            # from_email = settings.EMAIL_HOST_USER,
            #
            # recipient_list = [user_email])
            return redirect('/')
class ProfileView(View):
    def get(self,request):
        data = {
            'profillar':Profil.objects.filter(user=request.user),
            'adress': Manzil.objects.filter(profil__user=request.user, asosiy=True)
        }
        return render(request, 'page-profile-main.html', data)

class ProfileadresView(View):
    def get(self,request):
        data = {
            "adress":Manzil.objects.filter(profil__user=request.user)
        }
        return render(request, "page-profile-address.html", data)
class AddressPost(View):
    def get(self,request):
        return render(request, "address_create")



    def post(self,request):
        forma = ManzilForm(request.POST)
        if forma.is_valid():
            forma.save()
            return redirect("/user/address")
        return redirect("/user/add/")





