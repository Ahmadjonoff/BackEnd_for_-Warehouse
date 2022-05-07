from django.shortcuts import render, redirect
from django.views import View
from mainapp.models import *
from .models import *
from mainapp.models import Ombor

from mainapp.models import Mahsulot, Client


class StatsView(View):
    def get(self, request):
        if request.user.is_authenticated:
            omborxona = Ombor.objects.get(user = request.user)
            s = Statistika.objects.filter(ombor = omborxona)
            mahsulotlar = Mahsulot.objects.all()
            clients = Client.objects.all()
            return render(request, 'stats.html', {'stats' : s, 'ombor' : omborxona, 'mahsulotlar' : mahsulotlar, 'clients' : clients})
    def post(self, request):
        o = Ombor.objects.get(user = request.user)
        m = Mahsulot.objects.get(id = request.POST['pr'])
        c = Client.objects.get(id = request.POST['cl'])
        Statistika.objects.create(
            mahsulot = m,
            client = c,
            sana = request.POST['sana'],
            miqdor = request.POST['miqdor'],
            umumiy = request.POST['summa'],
            nasiya = request.POST['nasiya'],
            tolandi = request.POST['tolandi'],
            ombor = o
        )
        miq = request.POST['miqdor']
        m.miqdor -= int(miq)
        m.save()
        c.qarz += int(request.POST['nasiya'])
        c.save()
        return redirect('/stats/')