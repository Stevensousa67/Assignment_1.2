"""
This module will print the filtered data received by data_filter set by the user during runtime.

Author:Steven Sousa
version 1.2
release date - December 2023
"""

blank_label = ''
name_label = 'NAME'
id_label = 'ID'
nametype_label = 'NAMETYPE'
recclass_label = 'RECCLASS'
mass_label = 'MASS (g)'
fall_label = 'FALL'
year_label = 'YEAR'
reclat_label = 'RECLAT'
reclong_label = 'RECLONG'
geolocation_label = 'GEOLOCATION'
states_label = 'STATES'
counties_label = 'COUNTIES'


def print_filtered_list(filtered_list):
    """This function will print the filtered data in the terminal"""
    print('\nTable of filtered meteors:\n')
    print(f'{blank_label: <8}{name_label: <24}{id_label: <24}{nametype_label: <24}{recclass_label: <24}'
          f'{mass_label: <24}{fall_label: <24}{year_label: <24}{reclat_label: <24}{reclong_label: <24}'
          f'{geolocation_label: <30}{states_label: <24}{counties_label: <24}')
    print("=" * 288)
    for x, meteorite in enumerate(filtered_list, 1):
        print(f'{x: < 8}{meteorite.name: <24}{meteorite.id: <24}{meteorite.nametype: <24}{meteorite.recclass: <24}'
              f'{meteorite.mass: <24}{meteorite.fall: <24}{meteorite.year: <24}{meteorite.reclat: <24}'
              f'{meteorite.reclong: <24}{meteorite.geolocation: <33}{meteorite.states: <23}{meteorite.counties: <24}')

    exit('\nProgram has successfully accomplished its intention and is now exiting. Goodbye!')
