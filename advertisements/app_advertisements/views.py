from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

# HttpResponse('Успех!')

def top_sellers(request):
    return render(request, 'top-sellers.html')