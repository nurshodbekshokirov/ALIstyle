from django.contrib.auth.models import User
from django.db import models
class Profil(models.Model):
    ism = models.CharField(max_length=50)
    jins = models.CharField(max_length=9)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sana = models.DateField(auto_now_add=True, blank=True, null=True)
    shahar = models.CharField(max_length=50, blank=True, null=True)
    davlat = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return self.ism



