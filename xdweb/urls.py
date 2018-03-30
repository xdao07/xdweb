"""xdweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.views import static
from blog.uploads import upload_image


urlpatterns = [
    url(r'^admin/upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),
    url(r'^admin/', admin.site.urls),
    # 当设置DEBUG=False时，就必须在Django框架前端部署nginx或者其他web服务器来提供静态访问入口，否则需要如此设置static的url
    url(r"^static/(?P<path>.*)$", static.serve, {"document_root": settings.STATIC_ROOT}),
    url(r'^uploads/(?P<path>.*)$', static.serve, {"document_root": settings.MEDIA_ROOT}),
    url(r'^', include('blog.urls', namespace='blog', app_name='blog')),
]
