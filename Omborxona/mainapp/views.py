from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from .models import *

class Home(View):
    def get(self, request):
        return render(request, 'home.html')
    def post(self, request):
        l = request.POST.get('login')
        p = request.POST.get('password')
        user = authenticate(username=l, password=p)
        if user is None:
            return redirect('home')
        else:
            login(request, user)
            return redirect('bolim')

class Bolim(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'bulimlar.html')
        else:
            return redirect(request, 'home')
    def post(self, request):
        pass

class ProductView(View):
    def get(self, request):
        o = Ombor.objects.get(user = request.user)
        products = Mahsulot.objects.filter(ombor = o)
        return render(request, 'products.html', {'mahsulotlar' : products, 'obmor':o})

    def post(self, request):
        o = Ombor.objects.get(user=request.user)
        Mahsulot.objects.create(
            nom = request.POST['name'],
            sana = request.POST['s'],
            brend = request.POST['brand'],
            miqdor = request.POST['m'],
            kelgan_narx = request.POST['k_n'],
            sotuv_narx = request.POST['s_n'],
            ombor = o
        )
        return redirect('/products/')

class ClientView(View):
    def get(self, request):
        o = Ombor.objects.get(user=request.user)
        c = Client.objects.filter(ombor = o)
        return render(request, 'clients.html', {'clients' : c})
    def post(self, request):
        pass

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('home')

class ProductUpdate(View):
    def get(self, request, son):
        product = Mahsulot.objects.get(id = son)
        return render(request, 'product_update.html', {'product' : product})
    def post(self, request, son):
        o = Ombor.objects.get(user=request.user)
        mahsulot = Mahsulot.objects.get(id = son)
        mahsulot.nom=request.POST['name']
        mahsulot.sana=request.POST['s']
        mahsulot.brend=request.POST['brand']
        mahsulot.miqdor=request.POST['m']
        mahsulot.kelgan_narx=request.POST['k_n']
        mahsulot.sotuv_narx=request.POST['s_n']
        mahsulot.save()
        return redirect('/products/')