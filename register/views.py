from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def register_page(request):
    info = {}
    return render(request, "register/register.html", info)