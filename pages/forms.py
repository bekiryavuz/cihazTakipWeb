from django import forms
from django.forms import ModelForm
from .models import Cihazlar,Gorevli


class CihazForm(ModelForm):
    class Meta:
        model = Cihazlar
        fields = "__all__"
        labels = {
            'btNumarasi': '',
            'domainAdi': '',
            'isyeri': '',
            'cihazTuru': '',
            'gorevli':'',
            'markaAdi': '',
            'gelisNedeni': '',
            'yapilanIs': '',
            'gelisTarihi': '',
            'teslimTarihi': '',
            'cihazSahibi': '',
            'cihazDurum': '',
        }
        widgets = {
            'btNumarasi': forms.TextInput(attrs={'class':'form-control'}),
            'domainAdi': forms.TextInput(attrs={'class':'form-control'}),
            'isyeri': forms.TextInput(attrs={'class':'form-control',}),
            'cihazTuru': forms.TextInput(attrs={'class':'form-control'}),
            'gorevli': forms.Select(attrs={'class':'form-control'}),
            'markaAdi': forms.TextInput(attrs={'class':'form-control'}),
            'gelisNedeni': forms.TextInput(attrs={'class':'form-control'}),
            'yapilanIs': forms.TextInput(attrs={'class':'form-control'}),
            'gelisTarihi': forms.DateTimeInput(attrs={'class':'form-control','type':'date'}),
            'teslimTarihi': forms.DateTimeInput(attrs={'class':'form-control','type':'date'}),
            'cihazSahibi': forms.TextInput(attrs={'class':'form-control'}),
            'cihazDurum': forms.Select(attrs={'class':'form-control'},choices=[("Hazır", ("Hazır")), ("Hazır Değil", ("Hazır Değil"))]),
        }
        