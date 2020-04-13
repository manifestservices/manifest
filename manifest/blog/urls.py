"""chennaiusedbooks URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from views import *
from django.conf import settings
from django.conf.urls.static import static
from blog.views import *
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
# from views import error_404,error_500
admin.site.site_header = 'UsedBooksFactory Admin'
urlpatterns = [
    url('^$', BlogView.as_view(),name='blog'),
]
# handler404 = error_404
# handler500 = error_500