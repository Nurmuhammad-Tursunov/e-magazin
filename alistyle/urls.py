from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from asosiy.views import *
from userapp.views import *
from buyurtmaapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view()),
    path('', Home2View.as_view()),
    path('products/', ProductView.as_view()),
    path('bolimlar/', BolimlarView.as_view()),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('savat/', SavatView.as_view()),
    path('savat/<int:pk>/', SavatQoshView.as_view()),
    path('tanlangan_qosh/<int:pk>/', TanlanganQoshView.as_view()),
    path('tanlangan/', TanlanganView.as_view()),
    path('buyurtma/', BuyurtmaView.as_view()),
    path('buyurtma_qosh/', BuyurtmaQoshView.as_view()),
    path('mahsulotlar/', IchkiView.as_view()),
    path('bolim/<int:pk>/', BolimView.as_view()),
    path('mahsulot/<int:pk>/', MahsulotView.as_view()),
    path('savat_q/<int:son>/', savat_qosh),
    path('savat_k/<int:son>/', savat_ayri),
    path('ochirish/<int:son>/', OchirishView.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
