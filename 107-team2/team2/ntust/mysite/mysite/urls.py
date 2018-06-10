"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import include,url
from django.contrib import admin
from team2 import views
from team2.views import *
from django.conf.urls.static import static
from django.conf import settings
from .settings import MEDIA_ROOT
from django.views.static import serve


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^team2/', include('team2.urls')) ,
    url(r'^team2/my.html/$', post_detail1, name='post_detail1'),
    url(r'^team2/(?P<pk>[0-9]+)/$', post_area, name='post_area'),
    url(r'^team2/about.html/$', post_about, name='post_about'),
    url(r'^team2/m(?P<pk>[0-9]+)/$', post_museum, name='post_museum'),
    url(r'^team2/t(?P<pk>[0-9]+)/$', post_m_type, name='post_m_type'),
    url(r'^team2/c(?P<pk>[0-9]+)/$', comment, name='comment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)