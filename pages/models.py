from django.db import models

# Create your models here.

class Gorevli(models.Model):
    gorevliNumarasi = models.IntegerField('Görevli Numarası')
    gorevliAdi = models.CharField('Görevli Adı',max_length=50)
    gorevliSoyadi = models.CharField('Görevli Soyadı',max_length=50)
    gorevliTelefon = models.CharField('Gorevli Telefonu',max_length=50)
    def __str__(self):
        return self.gorevliAdi+' '+self.gorevliSoyadi
        


class Cihazlar(models.Model):
    btNumarasi = models.IntegerField('Bt Numarası')
    domainAdi = models.CharField('Domain Adı',max_length=14)
    isyeri = models.CharField('İşyeri Adı',max_length=50)
    cihazTuru = models.CharField('Cihaz Türü,',max_length=20)
    markaAdi = models.CharField('Marka Adı',max_length=50)
    gelisNedeni = models.CharField('Geliş Nedeni',max_length=50,blank=True,null=True)
    yapilanIs = models.CharField('Yapılan İş',max_length=50,blank=True,null=True)
    gorevli = models.ForeignKey(Gorevli,blank=True,null=True,on_delete=models.CASCADE)
    gelisTarihi = models.DateField('Geliş Tarihi')
    teslimTarihi = models.DateField('Teslim Tarihi')
    cihazSahibi = models.CharField('Cihaz Sahibi',max_length=50)
    cihazDurum = models.CharField('Cihaz Durumu',max_length=50)
    def __str__(self):
        return self.domainAdi + ' ' + self.isyeri 



class Telefonlar(models.Model):
    isyeri = models.CharField('İşyeri Adı',max_length=50)
    personelAdi = models.CharField('Personel Adı',max_length=50)
    personelSoyadi = models.CharField('Personel Soyadı',max_length=50)
    personelTelefon = models.IntegerField('Personel Telefonu')
    def __str__(self):
        return self.isyeri+' '+ self.personelAdi + ' ' + self.personelSoyadi + ' '+str(self.personelTelefon)

