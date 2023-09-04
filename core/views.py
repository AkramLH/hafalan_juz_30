from django.shortcuts import render

from .utils import get_quran_surahs

def alquran_surahs(request):
    surahs = get_quran_surahs()
    
    context = {
        'surahs': surahs
        }
    return render(request, 'index.html', context)