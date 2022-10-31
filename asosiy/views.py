from django.db.models import Count
from django.shortcuts import render
from django.views import View
from .models import *


class HomeView(View):
    def get(self, request):
        data = {
            "bolimlar": Bolim.objects.annotate(
                ichki_bolimlar_soni=Count("ichki_bolimlar")).order_by("-ichki_bolimlar_soni")[:6]
        }

        return render(request, "page-index.html", data)



class Home2View(View):
    def get(self, request):
        return render(request, "page-index-2.html")

class ProductView(View):
    def get(self, request):
        return render(request, "page-listing-grid.html")

class BolimlarView(View):
    def get(self, request):
        data = {
            "bolimlar": Bolim.objects.all()
        }
        return render(request, "page-category.html", data)

class BolimView(View):
    def get(self, request, pk):
        # b = Bolim.objects.get(pk)
        # ichki = Ichki.objects.filter(bolim=b)
        data = {
            "ichki_bolimlar": Ichki.objects.filter(bolim__id=pk)
        }
        return render(request, "ichki.html", data)


class MahsulotView(View):
    def get(self, request, pk):
        # b = Bolim.objects.get(pk)
        # ichki = Ichki.objects.filter(bolim=b)
        data = {
            "mahsulot": Mahsulot.objects.get(id=pk)
        }
        return render(request, "page-detail-product.html", data)

class IchkiView(View):
    def get(self, request):
        data = {
            "mahsulotlar": Mahsulot.objects.all()
        }
        return render(request, 'page-listing-grid.html', data)
