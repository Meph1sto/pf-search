from __future__ import unicode_literals
from django.db import models
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

class Search(models.Model):
    
    def __str__(self):
        return self.level + " " + self.TITLE + " " + self.UNI_NAME + " " + self.country

    KISCOURSEID = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    TITLE = models.CharField(max_length=100)
    UNI_NAME = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    country = models.CharField(max_length=100)


class Location(models.Model):

    def __str__(self):
        return self.town + " " + self.country

    town = models.CharField(max_length=100)
    country = models.CharField(max_length=100)


class Industry(models.Model):

    def __str__(self):
        return self.industry

    industry = models.CharField(max_length=100)

