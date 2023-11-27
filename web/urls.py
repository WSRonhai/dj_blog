from django.urls import path, include
from web.views import admin
from web.views import h5

urlpatterns = [
    path('login/', admin.login),
    path('', admin.home),
]
