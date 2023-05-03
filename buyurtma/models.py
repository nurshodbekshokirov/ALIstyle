from django.db import models
from asosiy.models import Mahsulot
from userapp.models import Profil
class Savat(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    umumiy = models.PositiveSmallIntegerField()
    miqdor = models.PositiveSmallIntegerField(default=1)
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)


class Tanlangan(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)

class Manzil(models.Model):
    tel = models.CharField(max_length=15)
    manzil = models.CharField(max_length=100)
    shahar = models.CharField(max_length=30)
    davlat = models.CharField(max_length=30)
    profil = models.ForeignKey(Profil,on_delete=models.CASCADE)
    asosiy = models.BooleanField(default=False)

    def __str__(self):
        return self.manzil
class Buyurtma(models.Model):
    savat = models.ManyToManyField(Savat,related_name='savatlari')
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    sana = models.DateField(auto_now_add=True)
    summa = models.IntegerField()
    yetkazish = models.IntegerField()
    holat = models.CharField(max_length=25, default="Yo'lda")

# Create your models here.
