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

# %%

# Set up Db access
conn = sqlite3.connect(join(db_path, 'db.sqlite3'))
c = conn.cursor()
print ('DB open for business')


# Open files for code look ups and add to dicts

# Open CSV file containing list of country and town names
# And load to memory
#locations = collections.defaultdict(list)
with open(join(data_path, 'geography.csv')) as f:
    reader = csv.reader(f)
    for _ in reader:
        country = _[0]
        town = _[1]
#        locations[country].append(town)
        c.execute("INSERT INTO search_location VALUES (?,?,?)",
                  (None, town, country))
conn.commit()
print ('DB commit ok')
conn.close()
print ('DB closed for business')








