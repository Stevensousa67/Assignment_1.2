"""
This module will filter the data passed in by the user from file_opener.py into two different lists depending on which
options the user selected during program runtime and then calls display_table.py to display the filtered data.

Author:Steven Sousa
version 1.2
release date - December 2023
"""

import display_table
from meteor_data_class import MeteorDataEntry


def filter_mass(file, read_mode, mass_lower_limit, mass_upper_limit):
    file = open(file, read_mode).readline()
    filtered_mass = []
    for x in file:
        data_fields = x.strip().split('\t')
        # Check if meteorite mass field isn't empty and it if it has mass > 2,900,000g
        if data_fields[4] != '' and mass_lower_limit <= float(data_fields[4]) <= mass_upper_limit:
            meteorite = MeteorDataEntry(*data_fields)
            filtered_mass.append(meteorite)
    display_table.print_filtered_mass_list(filtered_mass)


def filter_year(file, read_mode, year_lower_limit, year_upper_limit):
    file = open(file, read_mode).readline()
    filtered_years = []
    for x in file:
        data_fields = x.strip().split('\t')
        # Check if meteorite fell year is empty and if it fell on or after 2013
        year_value = data_fields[6]
        if year_value != '' and year_lower_limit <= int(year_value) <= year_upper_limit:
            meteorite = MeteorDataEntry(*data_fields)
            filtered_years.append(meteorite)
    display_table.print_filtered_year_list(filtered_years)


print()
