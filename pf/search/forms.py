# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
from django import forms
from django.utils.translation import ugettext_lazy as _


from .models import Search

class SearchFilterForm(forms.Form):
    level = forms.ModelChoiceField(
        label=_("Level"),
        required=False,
        queryset=Search.objects.all(),
    )
    TITLE = forms.ModelChoiceField(
        label=_("Subject"),
        required=False,
        queryset=Search.objects.all(),
    )
    UNI_NAME = forms.ModelChoiceField(
        label=_("University"),
        required=False,
        queryset=Search.objects.all(),
    )
    county = forms.ModelChoiceField(
        label=_("County"),
        required=False,
        queryset=Search.objects.all(),
    )
    country = forms.ModelChoiceField(
        label=_("Country"),
        required=False,
        queryset=Search.objects.all(),
    )

