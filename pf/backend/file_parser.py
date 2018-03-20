#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 22:49:51 2018

@author: robert_heeley
"""

from os import getcwd
from os.path import join
from collections import defaultdict
import collections
import csv
import sqlite3
import os

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
    reader = csv.reader(f)
    for _ in reader:
        UKPRN = _[0]
        NAME = _[1]
        d_uni_names[UKPRN].append(NAME)
    

# Open CSV file containing list of course types (KISAIMLABEL) and their codes (KISAIMCODE)
# And load to memory
d_course_codes = collections.defaultdict(list)
with open(join(data_path, 'KISAIM.csv')) as f:
    reader = csv.reader(f)
    for _ in reader:
        KISAIMCODE = _[0]
        KISAIMLABEL = _[1]
        d_course_codes[KISAIMCODE].append(KISAIMLABEL)


# Open CSV file containing location of courses codes (LOCNAME)
# And load to memory
d_course_locs = collections.defaultdict(list)
with open(join(data_path, 'LOCATION.csv')) as f:
    reader = csv.reader(f)
    for _ in reader:
        UKPRN = _[0]
        LOCNAME = _[4]
        d_course_locs[UKPRN].append(LOCNAME)

#%%
# Helper lookup functions

# Get course Uni name from code
def get_uni_name(UKPRN):
    return str(d_uni_names[UKPRN])


# Get course level (BA etc.) from KISAIMCODE
def get_course_level(KISAIMCODE):
    return str(d_course_codes[KISAIMCODE])
       
        
# Get course location from UKPRN
def get_course_location(UKPRN):
    return str(d_course_locs[UKPRN])
        
#%%        
    

# Set up Db access
conn = sqlite3.connect(join(db_path, 'db.sqlite3'))
c = conn.cursor()
print ('DB open for business')


# Create list for storage pre input to sqlite
#my_list = []

# Open CSV file KISCOURSE
# And load to memory
with open(join(data_path, 'KISCOURSE.csv')) as f:
    reader = csv.reader(f)
    ids=0
    for _ in reader:
        ids+=1
        UKPRN = _[1]
        UNI_NAME = get_uni_name(UKPRN)[2:-2]
        KISCOURSEID = _[14]
        TITLE = _[27]
        KISAIMCODE = _[32]
        level = get_course_level(KISAIMCODE)[2:-2]
        location = get_course_location(UKPRN)[2:-2]
#        print (KISCOURSEID, level, TITLE, UNI_NAME, location)
#        my_list.append((KISCOURSEID, level, TITLE, UNI_NAME, location))
        c.execute("INSERT INTO search_search VALUES (?,?,?,?,?,?)",  (None, KISCOURSEID, level, TITLE, UNI_NAME, location))
conn.commit()
print ('DB commit ok')
conn.close()
print ('DB closed for business')
#%%


# Add data to SQLite
#print (len(my_list))
#for item in my_list:
#    NULL = None
#    print (str(item[0]))
#    KISCOURSEID = item[0]
##    print (KISCOURSEID)
#    level = item[1]
#    TITLE = item[2]
#    UNI_NAME = item[3]
#    location = item[4]
##  c.execute('insert into search_search values (?,?,?,?,?)', item)
#    c.execute("INSERT INTO search_search VALUES ('id', 'KISCOURSEID', 'level', 'TITLE', 'UNI_NAME', 'location')", (NULL, KISCOURSEID, level, TITLE, UNI_NAME, location))
#conn.commit()
#conn.close()

  





