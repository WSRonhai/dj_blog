from django.shortcuts import render, HttpResponse


def doc(request):
    return  render(request,'doc/site/index.html')