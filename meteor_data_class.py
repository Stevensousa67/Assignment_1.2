"""
This class definition creates and returns an object called MeteorDataEntry to data_filter.py.

Author: Steven Sousa
version: 1.2
release date - December 2023
"""


# This file contains the constructor for each meteor that has mass > 29000000g and fell on or after 2013 from main.py

class MeteorDataEntry:
    """ MeteorDataEntry class receives many parameters that will construct the meteor object"""

    def __init__(self, data):
        self.name = data[0] if data[0] else ""
        self.id = data[1] if data[1] else ""
        self.nametype = data[2] if data[2] else ""
        self.recclass = data[3] if data[3] else ""
        self.mass = data[4] if data[4] else ""
        self.fall = data[5] if data[5] else ""
        self.year = data[6] if data[6] else ""
        self.reclat = data[7] if data[7] else ""
        self.reclong = data[8] if data[8] else ""
        self.geolocation = data[9] if data[9] else ""
        self.states = data[10] if data[10] else ""
        self.counties = data[11] if data[11] else ""


def __str__(self):
    """This function makes it possible to print the meteorite objects"""
    return (f'{self.name}\t{self.id}\t{self.nametype}\t{self.recclass}\t{self.mass}\t{self.fall}\t{self.year}\t'
            f'{self.reclat}\t{self.reclong}\t{self.geolocation}\t{self.states}\t{self.counties}')
