"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web.urls')),
# path('doc/', TemplateView.as_view(template_name='doc/site/index.html'), name='doc'),
]
urlpatterns += static('doc/', document_root=settings.BASE_DIR / 'doc/site/index.html')
# 添加下面的代码来处理 'doc/' 路由
# 添加以下配置来提供静态文件
if settings.DEBUG:
    urlpatterns += static('doc/', document_root=settings.BASE_DIR / 'doc/site/index.html')
