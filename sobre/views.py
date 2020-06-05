from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def func_render(request):
    return render(request, 'sobre/index.html')
