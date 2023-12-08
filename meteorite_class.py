"""
This class definition creates and returns an object called Meteorite that data_filter.py sends.

Author: Steven Sousa
version: 1.2
release date - December 2023
"""


class Meteorite:
    """ MeteorDataEntry class receives many parameters that will construct the meteor object"""

    def __init__(self, name='', id='', nametype='', recclass='', mass='', fall='', year='', reclat='', reclong='',
                 geolocation='', states='', counties=''):
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

    def to_string(self):
        """This function makes it possible to print the object's values"""
        return (f"{self.name}\t{self.id}\t{self.nametype}\t{self.recclass}\t{self.mass}\t{self.fall}\t{self.year}\t"
                f"{self.reclat}\t{self.reclong}\t{self.geolocation}\t{self.states}\t{self.counties}")
