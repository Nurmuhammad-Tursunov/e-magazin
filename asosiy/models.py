from django.db import models

class Bolim(models.Model):
    nom = models.CharField(max_length=100)
    rasm = models.FileField(upload_to='bolim_rasmlari')

    def __str__(self):
        return self.nom


class Ichki(models.Model):
    nom = models.CharField(max_length=100)
    rasm = models.FileField(upload_to='ichki_bolimlar')
    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE, related_name="ichki_bolimlar")

    def __str__(self):
        return self.nom


class Detal(models.Model):
    brend = models.CharField(max_length=300)
    kafolat = models.CharField(max_length=300)
    yetkazish = models.CharField(max_length=300)

    def __str__(self):
        return self.brend



class Mahsulot(models.Model):
    nom = models.CharField(max_length=100)
    batafsil = models.TextField()
    narx = models.PositiveIntegerField()
    mavjud = models.BooleanField(default=False)
    # rasm = models.FileField(upload_to='ichki_bolimlar')
    ichki = models.ForeignKey(Ichki, on_delete=models.CASCADE, related_name="ichki_mahsulotlari")
    detal = models.ForeignKey(Detal, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom}  {self.narx}"

class Rasm(models.Model):
    rasm = models.FileField(upload_to="mahsulot_rasmlari")
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE, related_name="mahsulot_rasmlari")

