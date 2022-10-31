from django.db.models import Sum
from django.shortcuts import render, redirect
from django.views import View
from asosiy.models import *
from .models import *
from userapp.models import *


class TanlanganView(View):
    def get(self, request):
        data = {
            "tanlanganlar": Tanlangan.objects.filter(profil__user=request.user)
        }
        return render(request, 'page-profile-wishlist.html', data)

class SavatView(View):
    def get(self, request):
        savatlar = Savat.objects.filter(profil__user=request.user)
        umumiy_sum = savatlar.aggregate(Sum('umumiy'))
        umumiy_chegirma = savatlar.aggregate(Sum('chegirma'))
        yakuniy = umumiy_sum.get("umumiy__sum") - umumiy_chegirma.get("chegirma__sum")
        data = {
            "savatlar": Savat.objects.filter(profil__user=request.user),
            'summa': umumiy_sum.get("umumiy__sum"),
            'chegirma': umumiy_chegirma.get("chegirma__sum"),
            'yakuniy': yakuniy
        }
        return render(request, 'page-shopping-cart.html', data)

class SavatQoshView(View):
    def get(self, request, pk):
        m = Mahsulot.objects.get(id=pk)
        pr = Profil.objects.get(user=request.user)
        if Savat.objects.filter(mahsulot=m, profil=pr).count() == 0:
            Savat.objects.create(
                mahsulot = m,
                profil = Profil.objects.get(user=request.user),
                umumiy = m.narx
            )
        return redirect('/savat/')

class BuyurtmaView(View):
    def get(self, request):
        data = {
            "buyurtmalar": Buyurtma.objects.filter(profil__user=request.user)
        }
        return render(request, 'page-profile-orders.html', data)


class BuyurtmaQoshView(View):
    def get(self, request):
        savatlar = Savat.objects.filter(profil__user=request.user)
        umumiy_sum = savatlar.aggregate(Sum('umumiy'))
        umumiy_chegirma = savatlar.aggregate(Sum('chegirma'))
        yakuniy = umumiy_sum.get("umumiy__sum") - umumiy_chegirma.get("chegirma__sum")

        pr = Profil.objects.get(user=request.user)
        b1 = Buyurtma.objects.create(
            profil = pr,
            summa = yakuniy,
            yetkazish = 3,
            yakuniy = yakuniy - 3

        )
        for s in savatlar:
            b1.savat.add(s)
        b1.save()
        return redirect("/buyurtma/")


def savat_qosh(request, son):
    s = Savat.objects.get(id=son)
    s.miqdor += 1
    s.umumiy = int(s.umumiy) + int(s.mahsulot.narx)
    s.save()
    return redirect('/savat/')

def savat_ayri(request, son):
    s = Savat.objects.get(id=son)
    if int(s.miqdor) > 0:
        s.miqdor -= 1
        s.umumiy = int(s.umumiy) - int(s.mahsulot.narx)
    s.save()
    return redirect('/savat/')


class OchirishView(View):
    def get(self, request, son):
        s = Savat.objects.get(id=son)
        if s.profil.user == request.user:
            s.delete()
        return redirect("/savat/")

class TanlanganQoshView(View):
    def get(self,request, pk):
        s = Savat.objects.get(id=pk)
        pr = Profil.objects.get(user=request.user)
        if Tanlangan.objects.filter(mahsulot=s.mahsulot, profil=pr).count() == 0:
            Tanlangan.objects.create(
                mahsulot = s.mahsulot,
                profil = pr
            )
        return redirect("/savat/")
