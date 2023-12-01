"""
This module will print the filtered data received by data_filter set by the user during runtime.

Author:Steven Sousa
version 1.2
release date - December 2023
"""

blank_label = ''
name_label = 'NAME'
mass_label = "MASS (g)"
year_label = "YEAR"


def print_filtered_mass_list(filtered_mass):
    print('\nTable of meteors filtered on mass(g):\n')
    print(f'{blank_label: <8}{name_label: <24}{mass_label: <24}')
    print("=" * 60)
    for x, meteorite in enumerate(filtered_mass, 1):
        print(f'{x: < 8}{meteorite.name: <24}{meteorite.mass: <24}')


def print_filtered_year_list(filtered_year):
    print()
    print('\nTable of meteors filtered on year:\n')
    print(f'{blank_label: <8}{name_label: <24}{year_label: <24}')
    print("=" * 60)
    for x, meteorite in enumerate(filtered_year, 1):
        print(f'{x: < 8}{meteorite.name: <24}{meteorite.year: <24}')
