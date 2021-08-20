from django.contrib import admin
from .models import Cihazlar
from .models import Telefonlar
from .models import Gorevli

@admin.register(Gorevli)
class GorevliYonet(admin.ModelAdmin):
    list_display = ('gorevliNumarasi','gorevliAdi','gorevliSoyadi','gorevliTelefon')

@admin.register(Cihazlar)
class CihazlarYonet(admin.ModelAdmin):
    list_display = ('btNumarasi','domainAdi','isyeri','gorevli','gelisTarihi','teslimTarihi','cihazDurum',)
    ordering = ('-gelisTarihi',)
    search_fields = ('btNumarasi','domainAdi','isyeri')
    list_filter = ('gelisTarihi','gelisNedeni','gorevli')

@admin.register(Telefonlar)
class TelefonlarYonet(admin.ModelAdmin):
    list_display = ('isyeri','personelAdi','personelSoyadi','personelTelefon')
    ordering = ('isyeri',)
    search_fields = ('isyeri','personelAdi','personelSoyadi','personelTelefon')
    list_filter = ('isyeri',)