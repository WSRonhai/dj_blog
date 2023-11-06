from django.shortcuts import render, HttpResponse


# Create your views here.

def login(request):
    return HttpResponse('login')


def home(request):
    return render(request,'admin/home.html')
