from django.shortcuts import render,redirect
from django.db.models import Sum
from .models import *
from asosiy.views import Mahsulot
from userapp.views import Profil

from django.views import View


class SavatView(View):
    def get(self,request):
        savatlar = Savat.objects.filter(profil__user=request.user)
        chegirmalar = 0
        summa =savatlar.aggregate(Sum('umumiy')).get('umumiy__sum')
        for savat in savatlar:
            chegirmalar += savat.miqdor * (savat.mahsulot.chegirma*savat.mahsulot.narx)/100

        data = {
            'savatlar':savatlar,
            'summa': summa,
            'chg': round(chegirmalar, 2),
            # 'yakuniy':summa-round(chegirmalar, 2)
        }
        return render(request, 'page-shopping-cart.html', data)
class TanlanganView(View):
    def get(self,request):

        data = {
            'tanlanganlar':Tanlangan.objects.filter(profil__user=request.user)
        }
        return render(request, 'page-profile-wishlist.html', data)
class Tanlangan_qoshview(View):
    def get(self,request,pk):
        savatlar = Savat.objects.get(profil__user=request.user,id=pk)
        Tanlangan.objects.create(
            mahsulot=Mahsulot.objects.get(nom=savatlar.mahsulot.nom),
            profil=Profil.objects.get(user=request.user)
        )
        return redirect(f'/buyurtma/tanlangan/')
class Savatqoshview(View):
    def get(self,request,pk):
        mahsulot = Mahsulot.objects.get(id=pk)
        Savat.objects.create(
            mahsulot = mahsulot,
            umumiy = mahsulot.narx,
            miqdor =  1,
            profil = Profil.objects.get(user=request.user)

        )
        return redirect('/buyurtma/savat/')
class Savatochirview(View):
    def get(self,request, pk):
        savat = Savat.objects.get(id=pk)
        if savat.profil.user == request.user:
            savat.delete()
            return redirect('savat')






class Tanlanganochirview(View):
    def get(self,request, pk):
        tanlangan = Tanlangan.objects.get(id=pk)
        if tanlangan.profil.user == request.user:
            tanlangan.delete()
            return redirect('tanlangan')


class BuyurtmaView(View):
    def get(self, request):
        data = {
            'buyurtmalar':Buyurtma.objects.filter(profil__user=request.user),
            'manzil':Manzil.objects.filter(profil__user=request.user, asosiy=True)
        }
        return  render(request, 'page-profile-orders.html', data)

class Miqdorqoshishview(View):
    def get(self,request, pk):
        savat = Savat.objects.get(id=pk)
        if savat.profil.user == request.user:


            savat.miqdor = savat.miqdor + 1

            savat.umumiy = int(savat.mahsulot.narx)*savat.miqdor
            savat.save()
            return redirect('savat')


class Miqdorkamview(View):
    def get(self, request, pk):

        savat = Savat.objects.get(id=pk)
        if savat.profil.user == request.user and savat.miqdor !=1:

            savat.miqdor = savat.miqdor - 1
            savat.umumiy = int(savat.mahsulot.narx) * savat.miqdor
            savat.save()
            return redirect('savat')



# Create your views here.
