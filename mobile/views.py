from django.shortcuts import render

# Create your views here.
def samsung(request):
    p={'model': 'SAMSUNG S23 ULTRA', 'processor': '8GEN2'}
    return render(request,'samsung.html',p)
def vivo(request):
    q={'model': 'VIVO IQOO NEO 7', 'processor': 'MEDIATEK DIMENSITY 8200'}
    return render(request,'vivo.html',q)