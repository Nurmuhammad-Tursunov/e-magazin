from django.db import models
from django.contrib.auth.models import User

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    jinsi = models.CharField(max_length=30)
    davlat = models.CharField(max_length=200)
    shahar = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username
