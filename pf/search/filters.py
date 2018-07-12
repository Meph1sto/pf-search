#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 14:23:34 2018

"""

#from django.contrib.auth.models import Search
from .models import Search, Location, Industry
import django_filters
from django import forms

class SearchFilter(django_filters.FilterSet):
    level = django_filters.CharFilter(lookup_expr='icontains')
    TITLE = django_filters.CharFilter(lookup_expr='icontains')
    UNI_NAME = django_filters.CharFilter(lookup_expr='icontains')
    county = django_filters.CharFilter(lookup_expr='icontains')
    country = django_filters.CharFilter(lookup_expr='icontains')

    # country = django_filters.ModelMultipleChoiceFilter(queryset=Search.objects.all(),
    #     widget=forms.CheckboxSelectMultiple)


    class Meta:
        model = Search
        fields = ['level', 'TITLE', 'UNI_NAME', 'county', 'country']

SearchFilter.base_filters['level'].label = 'Level'
SearchFilter.base_filters['TITLE'].label = 'Subject'
SearchFilter.base_filters['UNI_NAME'].label = 'University'
SearchFilter.base_filters['county'].label = 'County'
SearchFilter.base_filters['country'].label = 'Country'

    # def my_custom_filter(self, queryset, TITLE, value):
    #     return queryset.filter(**{
    #         TITLE: value,
    #     })
