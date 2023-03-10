from django.shortcuts import render,redirect
from django.db.models import Sum
from .models import *

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
            'yakuniy':summa-round(chegirmalar, 2)
        }
        return render(request, 'page-shopping-cart.html', data)
class TanlanganView(View):
    def get(self,request):
        data = {
            'tanlanganlar':Tanlangan.objects.filter(profil__user=request.user)
        }
        return render(request, 'page-profile-wishlist.html', data)

class Tanlanganochirview(View):
    def get(self,request, pk):
        tanlangan = Tanlangan.objects.get(id=pk)
        if tanlangan.profil.user == request.user:
            tanlangan.delete()
            return redirect('tanlangan')


class BuyurtmaView(View):
    def get(self, request):
        return  render(request, 'page-profile-orders.html')

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
