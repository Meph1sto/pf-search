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
from .models import Search

app_name = 'search'


#urlpatterns = [
#    path('admin/', admin.site.urls),
#]

urlpatterns = [
    # url(r'^search/', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^searchlist/$', views.searchlist, name='searchlist'),
    # url(r'^searchlist/$', FilterView.as_view(model=Search)),
    # url(r'^searchlist/$', object_filter, {'model': Search}),

    # url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    # url(r'^search/$', FilterView.as_view(filterset_class=SearchFilter, template_name='search/searchlist.html'), name='searchlist'),

    # url(r'^search/$', views.search_list, name='search_list'),
    # url(r'^$', views.search_list, name='search_list'),
    # url(r'^search/$', FilterView.as_view(filterset_class=SearchFilter, template_name='search/search_list.html')),

    # url(r'^$', views.search_list, name='search_list'),
    # url(r'^search/$', FilterView.as_view(filterset_class=SearchFilter,
    # 	template_name='search_list.html'), name='search_list'),

    #/search/2
    url(r'^(?P<search_id>[0-9]+)/$', views.detail, name='detail')
]