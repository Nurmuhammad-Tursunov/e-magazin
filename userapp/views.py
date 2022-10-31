from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from .models import Profil


class RegisterView(View):
    def get(self, request):
        return render(request, 'page-user-register.html')

    def post(self, request):
        if request.POST.get('p1') != request.POST.get('p2'):
            return redirect('/register/')

        u = User.objects.create_user(
            username = request.POST.get('i'),
            password = request.POST.get('p1'),
            email = request.POST.get('e'),
            first_name = request.POST.get('f'),
            last_name = request.POST.get('l'),
        )
        Profil.objects.create(
            user = u,
            jinsi = request.POST.get('gender'),
            shahar = request.POST.get('sh'),
            davlat = request.POST.get('d'),
        )

        return redirect('/login/')



class LoginView(View):
    def get(self, request):
        return render(request, "page-user-login.html")

    def post(self, request):
        user = authenticate(
            username = request.POST.get('l'),
            password = request.POST.get('p'),
        )

        if user is None:
            return redirect('/login/')
        login(request, user)
        return redirect('/home/')
