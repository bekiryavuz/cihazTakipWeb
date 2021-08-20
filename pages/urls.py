from django.urls import path
from . import views
from pages.views import analizGrafik

urlpatterns = [
    path('', views.index,name='index'),
    path('about', views.about,name='about'),
    path('cihazgiris', views.cihazgiris,name='cihazgiris'),
    path('cihazara', views.cihazara,name='cihazara'),
    path('genelanaliz', views.genelanaliz,name='genelanaliz'),
    path('geneldurum', views.geneldurum,name='geneldurum'),
    path('dokumanlar', views.dokumanlar,name='dokumanlar'),
    path('telefonlar', views.telefonlar,name='telefonlar'),
    path('cihazbul/<cihaz_id>',views.cihazbul,name="cihazbul"),
    path('cihazsec',views.cihazsec,name="cihazsec"),
    path('genelanaliz',analizGrafik.as_view,name="genelanaliz"),
    path('cihazTarihBul',views.cihazTarihBul,name="cihazTarihBul"),
    path('getPdfPage',views.getPdfPage,name='getPdfPage'),
    
]
