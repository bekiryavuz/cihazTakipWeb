from io import BytesIO

from django.shortcuts import render
from django.http import HttpResponse
from .models import Cihazlar
from .models import Telefonlar
from .models import Gorevli
from .forms import CihazForm
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.db.models import Count
from django.views.generic import TemplateView,View,ListView,DetailView,CreateView,UpdateView
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
import datetime
from django.utils.timezone import datetime, now


# Create your views here.


def getPdfPage(request):
    
    gelis = request.POST.get('gelisTarihi')
    teslim = request.POST.get('teslimTarihi')
    if gelis =="":
        gelis = '2021-1-1'
    if teslim =="":
        teslim = '2022-5-30'
    
    
    all_data = Cihazlar.objects.all()
    arizaSiyah = Cihazlar.objects.filter(gelisNedeni__contains="siyah",gelisTarihi__gte=gelis, teslimTarihi__lte=teslim).count()
    arizaAg = Cihazlar.objects.filter(gelisNedeni__contains="Ağ",gelisTarihi__gte=gelis, teslimTarihi__lte=teslim).count()
    arizaGuc = Cihazlar.objects.filter(gelisNedeni__contains="Güç",gelisTarihi__gte=gelis, teslimTarihi__lte=teslim).count()
    arizaMavi = Cihazlar.objects.filter(gelisNedeni__contains="Mavi",gelisTarihi__gte=gelis, teslimTarihi__lte=teslim).count()
    arizaBoot = Cihazlar.objects.filter(gelisNedeni__contains="Boot",gelisTarihi__gte=gelis, teslimTarihi__lte=teslim).count()
    arizaBaski = Cihazlar.objects.filter(gelisNedeni__contains="kalitesi",gelisTarihi__gte=gelis, teslimTarihi__lte=teslim).count()
    arizaC = Cihazlar.objects.filter(gelisNedeni__contains="C sürücüsü",gelisTarihi__gte=gelis, teslimTarihi__lte=teslim).count()
    arizaSistem = Cihazlar.objects.filter(gelisNedeni__contains="Sistem",gelisTarihi__gte=gelis, teslimTarihi__lte=teslim).count()
    arizalar = [
        [arizaSiyah,'Siyah Ekran Sorunu'],
        [arizaAg,'Ağ 2 Sorunu'],
        [arizaGuc,'Güç Kesintisi'],
        [arizaMavi,'Mavi Ekran Sorunu'],
        [arizaBoot,'Boot Sorunu'],
        [arizaBaski,'Baski Kalitesi Sorunu'],
        [arizaC,'C Sürücüsü Sorunu'],
        [arizaSistem,'Sistem Güncellemesi Sorunu']]
    arizalar = sorted(arizalar,reverse=True)

    dataBekir = Cihazlar.objects.all().filter(gorevli=1,gelisTarihi__gte=gelis, teslimTarihi__lte=teslim).count()
    dataNugman = Cihazlar.objects.all().filter(gorevli=2,gelisTarihi__gte=gelis, teslimTarihi__lte=teslim).count()
    dataHamdi = Cihazlar.objects.all().filter(gorevli=3,gelisTarihi__gte=gelis, teslimTarihi__lte=teslim).count()
    personel = [
        [dataBekir,'Bekir Yavuz'],
        [dataNugman, 'Nugman Aydın'],
        [dataHamdi,'Hamdi Ödemiş'],
    ]
    personel = sorted(personel, reverse=True)

    isyeriMali = Cihazlar.objects.filter(isyeri__contains="Mali",gelisTarihi__gte=gelis, teslimTarihi__lte=teslim).count()
    isyeriDestek = Cihazlar.objects.filter(isyeri__contains="Destek",gelisTarihi__gte=gelis, teslimTarihi__lte=teslim).count()
    isyeriEmlak = Cihazlar.objects.filter(isyeri__contains="emlak",gelisTarihi__gte=gelis, teslimTarihi__lte=teslim).count()
    isyeriPersonel = Cihazlar.objects.filter(isyeri__contains="personel",gelisTarihi__gte=gelis, teslimTarihi__lte=teslim).count()
    isyeriModernizasyon = Cihazlar.objects.filter(isyeri__contains="modernizasyon",gelisTarihi__gte=gelis, teslimTarihi__lte=teslim).count()
    isyeriBakim = Cihazlar.objects.filter(isyeri__contains="bakım",gelisTarihi__gte=gelis, teslimTarihi__lte=teslim).count()
    servis = [
        [isyeriMali,'Mali İşler Servis Müdürlüğü'],
        [isyeriDestek,'Destek Hizmetleri Servis Müdürlüğü'],
        [isyeriEmlak,'Emlak Servis Müdürlüğü'],
        [isyeriPersonel,'Personel Servis Müdürlüğü'],
        [isyeriModernizasyon,'Modernizasyon Servis Müdürlüğü'],
        [isyeriBakim,'Bakım Servis Müdürlüğü'],
    ]
    servis = sorted(servis, reverse=True)
    
    date = datetime.now().strftime("%Y-%m-%d ") 

    data={'all_data':all_data,'arizalar':arizalar,'date':date,'servis':servis,'personel':personel,'gelis':gelis,'teslim':teslim,'arizaBaski':arizaBaski,'arizaC':arizaC,'arizaSistem':arizaSistem,'arizaSiyah':arizaSiyah,'arizaAg':arizaAg,'arizaGuc':arizaGuc,'arizaMavi':arizaMavi,'arizaBoot':arizaBoot}
    if 'toplamAriza' in request.POST:
        template=get_template("toplam_ariza.html")
    elif 'toplamIs' in request.POST:
        template=get_template("toplam_is.html")
    elif 'toplamServis' in request.POST:
        template=get_template("toplam_servis.html")
        
    data_p=template.render(data)
    response = BytesIO()
    pdfPage = pisa.CreatePDF(BytesIO(data_p.encode("UTF-8")),response,encoding="UTF-8")
    
    if not pdfPage.err:
        return HttpResponse(response.getvalue(),content_type='application/pdf')
    else:
        return HttpResponse("Error")



def cihazTarihBul(request):
    if request.method == "POST":
        gelis = request.POST.get('gelisTarihi')
        teslim = request.POST.get('teslimTarihi')
        if gelis =="":
            gelis = '2021-1-1'
        if teslim =="":
            teslim = '2022-5-30'
        aranacak = [(Cihazlar.objects.filter(gelisTarihi__gte=gelis, teslimTarihi__lte=teslim)).count()]
        dataBekir = [Cihazlar.objects.all().filter(gorevli=1,gelisTarihi__gte=gelis, teslimTarihi__lte=teslim).count()]
        dataNugman = [Cihazlar.objects.all().filter(gorevli=2,gelisTarihi__gte=gelis, teslimTarihi__lte=teslim).count()]
        dataHamdi = [Cihazlar.objects.all().filter(gorevli=3,gelisTarihi__gte=gelis, teslimTarihi__lte=teslim).count()]
        arizaSiyah = [Cihazlar.objects.filter(gelisNedeni__contains="siyah",gelisTarihi__gte=gelis, teslimTarihi__lte=teslim).count()]
        arizaAg = [Cihazlar.objects.filter(gelisNedeni__contains="Ağ",gelisTarihi__gte=gelis, teslimTarihi__lte=teslim).count()]
        arizaGuc = [Cihazlar.objects.filter(gelisNedeni__contains="Güç",gelisTarihi__gte=gelis, teslimTarihi__lte=teslim).count()]
        arizaMavi = [Cihazlar.objects.filter(gelisNedeni__contains="Mavi",gelisTarihi__gte=gelis, teslimTarihi__lte=teslim).count()]
        arizaBoot = [Cihazlar.objects.filter(gelisNedeni__contains="Boot",gelisTarihi__gte=gelis, teslimTarihi__lte=teslim).count()]
        isyeriMali = [Cihazlar.objects.filter(isyeri__contains="Mali",gelisTarihi__gte=gelis, teslimTarihi__lte=teslim).count()]
        isyeriDestek = [Cihazlar.objects.filter(isyeri__contains="Destek",gelisTarihi__gte=gelis, teslimTarihi__lte=teslim).count()]
        isyeriBakim = [Cihazlar.objects.filter(isyeri__contains="bakım",gelisTarihi__gte=gelis, teslimTarihi__lte=teslim).count()]
        isyeriEmlak = [Cihazlar.objects.filter(isyeri__contains="emlak",gelisTarihi__gte=gelis, teslimTarihi__lte=teslim).count()]
        isyeriPersonel = [Cihazlar.objects.filter(isyeri__contains="personel",gelisTarihi__gte=gelis, teslimTarihi__lte=teslim).count()]
        isyeriModernizasyon = [Cihazlar.objects.filter(isyeri__contains="modernizasyon",gelisTarihi__gte=gelis, teslimTarihi__lte=teslim).count()]
      
        
        return render(request,'pages/cihazTarihBul.html',{'teslim':teslim,'gelis':gelis,"aranacak":aranacak,'isyeriModernizasyon':isyeriModernizasyon,'isyeriPersonel':isyeriPersonel,'isyeriEmlak':isyeriEmlak,'isyeriBakim':isyeriBakim,'isyeriDestek':isyeriDestek,'isyeriMali':isyeriMali,'dataBekir':dataBekir,'dataNugman':dataNugman,'dataHamdi':dataHamdi,'arizaSiyah':arizaSiyah,'arizaAg':arizaAg,'arizaGuc':arizaGuc,'arizaMavi':arizaMavi,'arizaBoot':arizaBoot})
    else:
        return render(request,'pages/cihazTarihBul.html',{})


def cihazsec(request):
    if request.method == "POST":
        arama = request.POST['arama']
        aranacak = Cihazlar.objects.filter(btNumarasi__contains=arama) or Cihazlar.objects.filter(isyeri__contains=arama) or Cihazlar.objects.filter(domainAdi__contains=arama) or Cihazlar.objects.filter(cihazTuru__contains=arama) or Cihazlar.objects.filter(markaAdi__contains=arama) or Cihazlar.objects.filter(gelisNedeni__contains=arama) or Cihazlar.objects.filter(yapilanIs__contains=arama) or Cihazlar.objects.filter(gelisTarihi__contains=arama) or Cihazlar.objects.filter(teslimTarihi__contains=arama) or Cihazlar.objects.filter(cihazSahibi__contains=arama) or Cihazlar.objects.filter(cihazDurum__contains=arama) 
        return render(request,'pages/cihazsec.html',{'arama':arama,'aranacak':aranacak})
    else:
        return render(request,'pages/cihazsec.html',{})

def cihazbul(request,cihaz_id):
    cihaz = Cihazlar.objects.get(pk=cihaz_id)
    return render(request,'pages/cihazbul.html',{'cihaz':cihaz})

def index(request):
    butun_cihazlar = Cihazlar.objects.all().order_by("-id")
    return render (request,'pages/index.html',{'cihazlar':butun_cihazlar})

class analizGrafik(TemplateView):
    template_name = 'pages/genelanaliz.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qs'] = Cihazlar.objects.all()
        return context

def about(request):
    return render (request,'pages/about.html')

def cihazgiris(request):
    submitted = False
    if request.method == "POST":
        form = CihazForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/cihazgiris?subbitted=True')
    else:
        form = CihazForm
        if 'submitted' in request.GET:
            submitted = True
    return render (request,'pages/cihazgiris.html',{'form':form,'submitted':submitted})

def cihazara(request):
    butun_cihazlar = Cihazlar.objects.all().order_by("-id")
    return render (request,'pages/cihazara.html',{'cihazlar':butun_cihazlar})

def genelanaliz(request):
    gorev = Gorevli.objects.all
    dataBekir = [Cihazlar.objects.all().filter(gorevli=1).count()]
    dataNugman = [Cihazlar.objects.all().filter(gorevli=2).count()]
    dataHamdi = [Cihazlar.objects.all().filter(gorevli=3).count()]
    arizaSiyah = [Cihazlar.objects.filter(gelisNedeni__contains="siyah").count()]
    arizaAg = [Cihazlar.objects.filter(gelisNedeni__contains="Ağ").count()]
    arizaGuc = [Cihazlar.objects.filter(gelisNedeni__contains="Güç").count()]
    arizaMavi = [Cihazlar.objects.filter(gelisNedeni__contains="Mavi").count()]
    arizaBoot = [Cihazlar.objects.filter(gelisNedeni__contains="Boot").count()]
    isyeriMali = [Cihazlar.objects.filter(isyeri__contains="Mali").count()]
    isyeriDestek = [Cihazlar.objects.filter(isyeri__contains="Destek").count()]
    isyeriBakim = [Cihazlar.objects.filter(isyeri__contains="bakım").count()]
    isyeriEmlak = [Cihazlar.objects.filter(isyeri__contains="emlak").count()]
    isyeriPersonel = [Cihazlar.objects.filter(isyeri__contains="personel").count()]
    isyeriModernizasyon = [Cihazlar.objects.filter(isyeri__contains="modernizasyon").count()]
    return render (request,'pages/genelanaliz.html',{'isyeriModernizasyon':isyeriModernizasyon,'isyeriPersonel':isyeriPersonel,'isyeriEmlak':isyeriEmlak,'isyeriBakim':isyeriBakim,'isyeriDestek':isyeriDestek,'isyeriMali':isyeriMali,'dataBekir':dataBekir,'dataNugman':dataNugman,'dataHamdi':dataHamdi,'gorev':gorev,'arizaSiyah':arizaSiyah,'arizaAg':arizaAg,'arizaGuc':arizaGuc,'arizaMavi':arizaMavi,'arizaBoot':arizaBoot})

def geneldurum(request):
    return render (request,'pages/geneldurum.html')

def dokumanlar(request):
    return render (request,'pages/dokumanlar.html')

def telefonlar(request):
    butun_telefonlar = Telefonlar.objects.all
    return render (request,'pages/telefonlar.html', {'telefonlar':butun_telefonlar})

