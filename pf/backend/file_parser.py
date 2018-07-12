#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 22:49:51 2018

@author: 
"""

from os import getcwd
from os.path import join
from collections import defaultdict
import collections
import csv
import sqlite3
import os


# api_key = 'AIzaSyBp2MmttlmRR9N0INDCUhbptIS-hMJBA8c'
# api_key = 'AIzaSyCVUQwqpKwou-C55zJLKLnjoUF34APFrss'
# api_key = 'AIzaSyAnfBdqLYO2KZ1x7ckYT46FLuze9rM1IzY'
api_key = 'AIzaSyD6a4TgmMWUJLixAt0kcsnSOCqGpsgaxKQ'
from geopy.geocoders import GoogleV3
geolocator = GoogleV3(api_key)


# Set up file paths
curr_path = getcwd()
data_path = join(curr_path, 'data')
base_path = os.path.dirname(os.path.dirname(curr_path))
db_path = join(base_path, 'pf')

#%%

# Open files for code look ups and add to dicts

# Open CSV file containing list of uni id codes (UKPRN) and their names
# And load to memory
d_uni_names = collections.defaultdict(list)
with open(join(data_path, 'UNISTATS_UKPRN_lookup_20160901.csv')) as f:
    next(f)  # skip header line
    reader = csv.reader(f)
    for _ in reader:
        UKPRN = _[0]
        NAME = _[1]
        d_uni_names[UKPRN].append(NAME)
    

# Open CSV file containing list of course types (KISAIMLABEL) and their codes (KISAIMCODE)
# And load to memory
d_course_codes = collections.defaultdict(list)
with open(join(data_path, 'KISAIM.csv')) as f:
    next(f)  # skip header line
    reader = csv.reader(f)
    for _ in reader:
        KISAIMCODE = _[0]
        KISAIMLABEL = _[1]
        d_course_codes[KISAIMCODE].append(KISAIMLABEL)


# Open CSV file containing geo location of courses codes (LOCNAME)
# And load to memory
d_course_county = collections.defaultdict(list)
d_course_country = collections.defaultdict(list)


# Google Maps API parser
def get_component(location, component_type):
    try:
        for component in location.raw['address_components']:
            if component_type in component['types']:
                return (component['long_name']).encode('utf-8')
    except AttributeError:
        return ''
        pass

with open(join(data_path, 'LOCATION.csv')) as f:
    next(f) # skip header line
    reader = csv.reader(f)
    for _ in reader:
        UKPRN = _[0]
        LAT = _[6]
        LONG = _[7]
        geoloc = str(LAT +','+LONG)
        location = geolocator.reverse(geoloc, timeout=10, exactly_one=True)
        county = get_component(location, 'administrative_area_level_2')
        country = get_component(location, 'administrative_area_level_1')

        if UKPRN not in d_course_county:
            d_course_county[UKPRN].append(county)

        if UKPRN not in d_course_country:
            d_course_country[UKPRN].append(country)

#%%
# Helper lookup functions

# Get course Uni name from code
def get_uni_name(UKPRN):
    return str(d_uni_names[UKPRN])


# Get course level (BA etc.) from KISAIMCODE
def get_course_level(KISAIMCODE):
    return str(d_course_codes[KISAIMCODE])


# Get course county from UKPRN
def get_course_county(UKPRN):
    return str(d_course_county[UKPRN])


# Get course country from UKPRN
def get_course_country(UKPRN):
    return str(d_course_country[UKPRN])

#%%

# Set up Db access
conn = sqlite3.connect(join(db_path, 'db.sqlite3'))
conn.text_factory = lambda x: unicode(x, 'utf-8', 'ignore')
c = conn.cursor()
print ('DB open for business')

# Open CSV file KISCOURSE
# And load to memory
with open(join(data_path, 'KISCOURSE.csv')) as f:
    reader = csv.reader(f)
    next(f)  # skip header line
    for _ in reader:
        UKPRN = _[1]
        UNI_NAME = get_uni_name(UKPRN)[2:-2]
        KISCOURSEID = _[14]
        TITLE = _[27]
        KISAIMCODE = _[32]
        level = get_course_level(KISAIMCODE)[2:-2]
        county = get_course_county(UKPRN)[2:-2]
        country = get_course_country(UKPRN)[2:-2]

        print (county, country)
        c.execute("INSERT INTO search_search VALUES (?,?,?,?,?,?,?)",  (None, KISCOURSEID, level, TITLE, UNI_NAME, county, country))
conn.commit()
print ('DB commit ok')
conn.close()
print ('DB closed for business')
