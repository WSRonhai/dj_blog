from django.urls import path,include
from  web.views import  admin
urlpatterns = [
    path('login/', admin.login),
    path('', admin.home),
]
