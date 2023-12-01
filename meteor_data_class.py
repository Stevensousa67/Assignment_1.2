"""
This class definition creates and returns an object called MeteorDataEntry to data_filter.py.

Author: Steven Sousa
version: 1.2
release date - December 2023
"""


# This file contains the constructor for each meteor that has mass > 29000000g and fell on or after 2013 from main.py

class MeteorDataEntry:
    """ MeteorDataEntry class receives many parameters that will construct the meteor object"""

    def __init__(self, name, id, nametype, recclass, mass, fall, year, reclat='', reclong='', geolocation='', states='',
                 counties=''):
        self.name = name
        self.id = id
        self.nametype = nametype
        self.recclass = recclass
        self.mass = mass
        self.fall = fall
        self.year = year
        self.reclat = reclat
        self.reclong = reclong
        self.geolocation = geolocation
        self.states = states
        self.counties = counties
