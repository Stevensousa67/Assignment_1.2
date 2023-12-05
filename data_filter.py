"""
This module will filter the data passed in by the user from file_opener.py into two different lists depending on which
options the user selected during program runtime and then calls display_table.py to display the filtered data.

Author:Steven Sousa
version 1.2
release date - December 2023
"""

from meteor_data_class import MeteorDataEntry


def filter_mass(file, read_mode, mass_lower_limit, mass_upper_limit):
    file, filtered_mass = open(file, read_mode).readline(), []
    for line in file:
        row = line.strip().split('\t')
        meteorite = MeteorDataEntry(*row)
        if row[4] != '' and mass_lower_limit <= float(row[4]) <= mass_upper_limit: filtered_mass.append(meteorite)
    for meteorite in filtered_mass:
        print(str(meteorite))


def filter_year(file, read_mode, year_lower_limit, year_upper_limit):
    file, filtered_years = open(file, read_mode).readline(), []
    for x in file:
        row = x.strip().split('\t')
        meteorite = MeteorDataEntry(*row)
        if row[6] != '' and year_lower_limit <= int(row[6]) <= year_upper_limit: filtered_years.append(meteorite)


print()
