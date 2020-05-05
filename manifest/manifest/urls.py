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
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from views import *
from projects.views import *
from services.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
sitemaps={'statichighsitemaps':StaticHighSitemap,
          'categorysitemaps':CategorySitemap,
          'staticlowsitemaps':StaticLowSitemap,
          }
# from views import error_404,error_500
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^(?:/)?(?:index.htm)?(?:l)?(?:l)?$', HomePageView.as_view(), name='home'),
    url(r'^about-us/', AboutusView.as_view(),name='about_us'),
    url(r'^contact/', ContactView.as_view(),name='contact_us'),
    url(r'^survey/', SurveyView.as_view(),name='survey'),
    url(r'^services/(?P<slug>[^/]+)$', ServicesView.as_view(),name='services'),
    url(r'^projects/', ProjectView.as_view(),name='projects'),
    url(r'^blog/', include('blog.urls'),name='blog'),
    url(r'^thankyou/', ThankyouView.as_view(),name='thankyou'),
    url(r'^sitemap.xml', sitemap, {'sitemaps': sitemaps},name='sitemap-xml'),
    url(r'^html/(?P<template>[\w-]+)', TemplateView.as_view(),name='template')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# handler404 = error_404
# handler500 = error_500