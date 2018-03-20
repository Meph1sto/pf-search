#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 14:23:34 2018

@author: robert_heeley
"""

#from django.contrib.auth.models import Search
from .models import Search, Location, Industry
import django_filters
from django import forms

class SearchFilter(django_filters.FilterSet):
    level = django_filters.CharFilter(lookup_expr='icontains')
    TITLE = django_filters.CharFilter(lookup_expr='icontains')
    UNI_NAME = django_filters.CharFilter(lookup_expr='icontains')
    # location = django_filters.CharFilter(lookup_expr='icontains')
    country = django_filters.CharFilter(lookup_expr='icontains')

    # country = django_filters.ModelMultipleChoiceFilter(queryset=Search.objects.all(),
    #     widget=forms.CheckboxSelectMultiple)


    class Meta:
        model = Search
        fields = ['level', 'TITLE', 'UNI_NAME', 'location', 'country']

    # def my_custom_filter(self, queryset, TITLE, value):
    #     return queryset.filter(**{
    #         TITLE: value,
    #     })