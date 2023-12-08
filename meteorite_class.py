"""
This class definition creates and returns an object called Meteorite that data_filter.py sends.

Author: Steven Sousa
version: 1.2
release date - December 2023
"""


class Meteorite:
    """ MeteorDataEntry class receives many parameters that will construct the meteor object"""
    def __init__(self, data):
        self.name = data[0] if data and len(data) > 0 else ""
        self.id = data[1] if data and len(data) > 1 else ""
        self.nametype = data[2] if data and len(data) > 2 else ""
        self.recclass = data[3] if data and len(data) > 3 else ""
        self.mass = data[4] if data and len(data) > 4 else ""
        self.fall = data[5] if data and len(data) > 5 else ""
        self.year = data[6] if data and len(data) > 6 else ""
        self.reclat = data[7] if data and len(data) > 7 else ""
        self.reclong = data[8] if data and len(data) > 8 else ""
        self.geolocation = data[9] if data and len(data) > 9 else ""
        self.states = data[10] if data and len(data) > 10 else ""
        self.counties = data[11] if data and len(data) > 11 else ""

    def to_string(self):
        """This function makes it possible to print the object's values"""
        return (f"{self.name}\t{self.id}\t{self.nametype}\t{self.recclass}\t{self.mass}\t{self.fall}\t{self.year}\t"
                f"{self.reclat}\t{self.reclong}\t{self.geolocation}\t{self.states}\t{self.counties}")
