"""
This module will filter the data passed in by the user from file_opener.py into two different lists depending on which
options the user selected during program runtime and then calls terminal_table.py to display the filtered data.

Author:Steven Sousa
version 1.2
release date - December 2023
"""
from meteorite_class import Meteorite


def filter_mass(file, read_mode, mass_lower_limit, mass_upper_limit):
    """This function filters the data source based on the upper and lower limits established by the user"""
    text_file = open(file, read_mode)
    text_file.readline()
    filtered_mass = []
    for line in text_file:
        row = line.strip().split('\t')
        meteorite = Meteorite(*row)
        if meteorite.mass != '' and mass_lower_limit <= float(meteorite.mass) <= mass_upper_limit:
            filtered_mass.append(meteorite)
    return filtered_mass


def filter_year(file, read_mode, year_lower_limit, year_upper_limit):
    """"This function filters the data source based on the upper and lower limits established by the user"""
    text_file = open(file, read_mode)
    text_file.readline()
    filtered_year = []
    for line in text_file:
        row = line.strip().split('\t')
        meteorite = Meteorite(*row)
        if meteorite.year != '' and year_lower_limit <= float(meteorite.year) <= year_upper_limit:
            filtered_year.append(meteorite)
    return filtered_year
