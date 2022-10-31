from django.db import models
from userapp.models import *
from asosiy.models import *


class Tanlangan(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)

class Savat(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    miqdor = models.SmallIntegerField(default=1)
    chegirma = models.SmallIntegerField(default=1)
    umumiy = models.SmallIntegerField()

class Buyurtma(models.Model):
    savat = models.ManyToManyField(Savat)
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    sana = models.DateField(auto_now_add=True)
    summa = models.PositiveIntegerField()
    yetkazish = models.PositiveIntegerField(default=0)
    yakuniy = models.PositiveIntegerField()