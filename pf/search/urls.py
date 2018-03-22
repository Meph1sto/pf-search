"""pf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path
import django_filters
from .filters import SearchFilter
from django_filters.views import FilterView
from django_filters.views import object_filter
from . import views
from . import forms
from .models import Search

app_name = 'search'


#urlpatterns = [
#    path('admin/', admin.site.urls),
#]

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^searchlist/$', views.searchlist, name='searchlist'),
    url(r'^searchtree/$', views.searchtree, name='searchtree'),

    #/search/2
    url(r'^(?P<search_id>[0-9]+)/$', views.detail, name='detail')
]