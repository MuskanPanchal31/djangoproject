from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'website\index.html')


def about(request):
    return HttpResponse("Hy Muskan this is your about page")

def contact(request):
    return HttpResponse("Hy Muskan this is your contact page")

