from django.shortcuts import render
from django.views import View


# Create your views here.
class Registerview(View):
    def get(self, request):
        return render(request,'page-user-register.html')