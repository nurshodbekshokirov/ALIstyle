from django.shortcuts import render,redirect
from django.views import View
from .models import *
from django.contrib.auth import login,authenticate,logout

from userapp.models import Profil


class Home2view(View):
    def get(self, request):
        return render(request, 'page-index-2.html')

# Create your views here.
class Homeview(View):
    def get(self, request):
        if request.user.is_authenticated:
            data = {
                'bolimlar': Bolim.objects.all()[:7],
                'chegirmalilar':Mahsulot.objects.filter(chegirma__gt=0).order_by('-chegirma')[:5]
            }
            return render(request, 'page-index.html', data)
        return redirect('/')

class Bolimlarview(View):
    def get(self,request):
        if request.user.is_authenticated:

            data = {
                'bolimlar':Bolim.objects.all()
            }
            return render(request, 'page-category.html', data)
        return redirect('/')
class Bolimview(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            data = {
                'mahsulotlar':Mahsulot.objects.filter(bolim__id=pk)
            }
            return render(request, 'page-listing-grid.html', data)
        return redirect('/')
class Loginview(View):
    def get(self,request):


        return render(request, 'page-user-login.html')
    def post(self,request):



        user = authenticate(
            username = request.POST.get('l'),
            password = request.POST.get('p')
        )
        if user is None:
            return redirect('/')
        login(request, user)
        return redirect('/asosiy/bolimlar')
class Logoutview(View):
    def get(self,request):
        logout(request)
        return redirect('/')

class Mahsulot_bitaview(View):
    def get(self,request, pk):
        product = Mahsulot.objects.get(id=pk)
        data = {
            'mahsulot':Mahsulot.objects.get(id=pk),
            'izohlar':Izoh.objects.filter(mahsulot=product),

        }
        return render(request, 'page-detail-product.html',data)
    def post(self,request,pk):


        Izoh.objects.create(
            baho = request.POST.get('rating'),
            matn = request.POST.get('comment'),
            mahsulot = Mahsulot.objects.get(id=pk),
            profil = Profil.objects.get(user=request.user)

        )
        return redirect(f'/asosiy/mahsulot/{pk}')


